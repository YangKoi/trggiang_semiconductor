# Semiconductor Facility Gas Monitor - SCADA HMI Dashboard

An ultra-modern, high-fidelity, web-based SCADA (Supervisory Control and Data Acquisition) dashboard for a semiconductor factory gas monitoring system. This application overlays live telemetry readouts on top of a Piping and Instrumentation Diagram (P&ID) and simulates industrial Ethernet data polling, alerts, safety sirens, and admin configuration control.

## 🚀 Live Preview & Deployment
Since the project is built using pure HTML, Tailwind CSS, and Vanilla JavaScript, it can be hosted directly on GitHub Pages without any compilation or server-side build steps.
- Repo: [https://github.com/YangKoi/trggiang_semiconductor](https://github.com/YangKoi/trggiang_semiconductor)
- URL: `https://yangkoi.github.io/trggiang_semiconductor/`

---

## 🛠️ Technology Stack
1. **Core Structure**: HTML5 Semantic markup.
2. **Styling**: Tailwind CSS (integrated dynamically via CDN) for responsive layout and styling.
3. **Data Visualization**: Chart.js for real-time sparkline telemetry and historical leak trend analysis.
4. **Icons**: Lucide Icons for vector indicators.
5. **Acoustic Warning**: Web Audio API synthesizer for a synthesized industrial emergency siren (no external audio assets required).
6. **Interactivity**: Vanilla JavaScript with zero external runtime dependencies.

---

## 📡 Key Features & SCADA Architecture

### 1. Interactive P&ID Overlays
- Centered background P&ID container showing cleanroom (`C/R`), utility floor (`U/T`), cylinder cabinets (`C/C`), and scrubber units.
- **Value Boxes** are absolutely positioned on percentage coordinates (`left`, `top`) mapped directly to safety sensor positions. The readouts scale and align perfectly on all screen resolutions (Responsive SCADA Design).
- Neon borders and color codes change dynamically based on PPM concentrations:
  - **Normal**: Safe green border with slight neon glow.
  - **Warning (Low Alarm)**: Amber border with breathing pulsing animation.
  - **Critical (High Alarm)**: Red border with rapid blinking and deep red neon glow.

### 2. Multi-Tab Operator Investigation Panel
Clicking on any overlay box displays a detailed modal window:
- **[Real-time]**: Live PPM telemetry feeding a scrolling sparkline chart that updates every 1 second. Shows current Modbus IP address, port, and alarm limits.
- **[History]**: A 24-hour historical log displaying a simulated gas leak curve (a past incident lifecycle showing normal -> leak -> peak -> recovery) and a table of recent samples.
- **[Settings]**: Administrative panel allowing calibration of the sensor IP, port, sampling rate, and low/high alarm thresholds. 
  - *Note*: Protected by a security lock. Enter password **`admin`** to unlock.

### 3. Simulation Incident Generator
Test safety integrity dynamically using the built-in control room:
- **Cabinet Leak**: Causes Silane ($SiH_4$) levels to rise steadily, triggering WARNING and CRITICAL alarms.
- **Cleanroom Arsine Leak**: Initiates an Arsine ($AsH_3$) leak inside the photolithography/CVD zone.
- **Pump Ammonia Leak**: Mimics a pump seal failure in the utility floor.
- **Sensor Comm Lost**: Disconnects Modbus handshake on a sensor, turning status to a greyed-out `FAULT` state.
- **Force Vent Purge**: Activates auxiliary cleanroom exhaust vents at 100% capacity, purging leak levels back to normal.
- **Reset System**: Clears all safety overrides and restarts mock baseline telemetry.

### 4. Acoustic Safety Siren
- When a **CRITICAL (High Alarm)** threshold is reached on any sensor, a global evacuation banner flashes at the top of the screen.
- A simulated dual-tone acoustic alarm horn will trigger using Web Audio API frequency sweeps.
- Use the **Mute Siren** button in the header to toggle the audible alarm sound on or off.

---

## 🧑‍💻 File Structure
```bash
trggiang_semiconductor/
├── assets/
│   └── layout.png     # P&ID semiconductor layout diagram
├── index.html         # Main SCADA GUI dashboard markup and logic
└── README.md          # Technical documentation
```

---

## 🏃 Running the Project Locally
Simply open the `index.html` file in any modern web browser:
1. Double-click `index.html` in your file explorer, OR
2. Run a local development server using VS Code Live Server or Python:
   ```bash
   python -m http.server 8000
   ```
   Then open `http://localhost:8000` in your web browser.
