from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for browser access

# Check if pymodbus is available
try:
    from pymodbus.client import ModbusTcpClient
    pymodbus_available = True
except ImportError:
    pymodbus_available = False

@app.route('/api/read', methods=['GET'])
def read_modbus():
    ip = request.args.get('ip', '127.0.0.1')
    port = int(request.args.get('port', 502))
    sensor_id = request.args.get('id', 'GD-00')
    
    # If using localhost/mock or if pymodbus is missing, run simulated connection
    if ip == '127.0.0.1' or ip.lower() == 'mock' or not pymodbus_available:
        # Return simulated live sensor readings for testing
        mock_val = random.uniform(0.01, 3.5)
        if "CR-02" in sensor_id:
            mock_val = random.uniform(19.0, 21.8)
        return jsonify({
            "status": "success",
            "ip": ip,
            "port": port,
            "value": round(mock_val, 3)
        })

    # Actual Modbus TCP client request
    client = ModbusTcpClient(ip, port=port, timeout=1.0)
    connected = client.connect()
    
    if not connected:
        return jsonify({
            "status": "error",
            "message": f"Connection timed out to PLC at {ip}:{port}"
        }), 500
        
    try:
        # Read holding register 0 (16-bit register)
        result = client.read_holding_registers(0, 1)
        if result.isError():
            # Try reading input registers as fallback
            result = client.read_input_registers(0, 1)
            
        if result.isError():
            return jsonify({
                "status": "error",
                "message": "Failed to read Modbus register registers"
            }), 500
            
        # Parse registers values and apply standard PLC decimal scaling (divide by 100)
        raw_value = result.registers[0]
        scaled_value = raw_value / 100.0  # e.g., 500 -> 5.00
        
        return jsonify({
            "status": "success",
            "ip": ip,
            "port": port,
            "value": scaled_value
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    finally:
        client.close()

if __name__ == '__main__':
    print("==================================================")
    print("  SCADA Modbus TCP Ethernet Gateway Server Active")
    print("  Access Endpoint: http://localhost:5000/api/read")
    print("==================================================")
    if not pymodbus_available:
        print("  NOTICE: 'pymodbus' is not installed locally.")
        print("  Running in simulated loop. To connect real PLCs run:")
        print("  pip install pymodbus flask flask-cors")
        print("--------------------------------------------------")
    app.run(host='0.0.0.0', port=5000, debug=True)
