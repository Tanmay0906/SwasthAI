# 🩺 SwasthAI: AN IoT and ML BASED HEALTH MONITORING DASHBOARD

**SwasthAI** is an intelligent healthcare monitoring system that integrates **IoT sensors**, **Machine Learning**, and a **real-time web dashboard** to track vital signs such as heart rate, SpO₂, temperature, ECG.  
It enables continuous remote health tracking and provides smart recommendations through AI analytics.

---

## ⚙️ Key Features

- 💓 **Vital Sign Monitoring** — Heart Rate, SpO₂, ECG, Room & Body Temperature.  
- 🧠 **ML-Based Predictions** —  
  - Blood Pressure Estimation  
  - Risk Level Detection  
  - Stress Level Detection  
  - Fall Detection  
- ☁️ **Cloud Integration** — Sensor data sent to **ThingSpeak** for storage and analytics.  
- 📊 **Interactive Dashboard** — Live charts, health metrics, and history visualization (built using **HTML + CSS + JS + Chart.js**).  
- 🔊 **Text-to-Speech (TTS)** — Voice alerts for abnormal readings.  
- 🧩 **AI Recommendations** — Personalized suggestions for health improvement.  
- 🌙 **Dark Mode Support** and data export (PDF/CSV).

---

## 🧩 Hardware Components

| Category | Component |
|-----------|------------|
| **Microcontroller** | ESP8266|
| **Sensors** | MAX30102 (HR & SpO₂), ADXL345 (Accelerometer), DHT11 (Temp & Humidity), DS18B20 (Body Temp), AD8232 (ECG) |
| **Server/Cloud** | Flask Server + ThingSpeak |
| **ML Models** | BP Estimation, Risk Level, Stress Level, Fall Detection |
| **Dashboard** | HTML + CSS + JavaScript + Chart.js |

---

## 🧠 Machine Learning Workflow

1. **Data Acquisition** → Sensor data collected via ESP8266.  
2. **Pre-Processing** → Cleaning, normalization, and feature extraction.  
3. **Model Training** → Trained `.pkl` models for prediction.  
4. **Prediction** → Flask server performs inference and sends results back to ESP8266 / ThingSpeak.  
5. **Visualization** → Dashboard displays live data & ML outputs with recommendations.

---

## 🗂️ Project Structure

SwasthAI/
│
├── mon.py # Flask server
├── models/
│ ├── bp_model.pkl
│ ├── risk_model.pkl
│ ├── stress_model.pkl
│ └── fall_model.pkl
├── templates/
│ └── mon.html # Dashboard UI
└── requirements.txt

## 🚀 How to Run the Project

### 🟦 **1️⃣ Install Dependencies**

pip install flask pandas numpy scikit-learn requests pyttsx3

### 🟩 2️⃣ Run the Flask Server
python app.py

--The server will start on http://127.0.0.1:5000/

--ESP8266 sends sensor readings here for ML predictions.

### 🟨 3️⃣ Configure ESP8266

-- Open SwasthAI_ESP.ino in Arduino IDE

--Update:

      --Wi-Fi SSID & Password

      -- Flask Server IP or ThingSpeak API key

--Upload to NodeMCU board.

### 🟧 4️⃣ View Dashboard

-- Open mon.html in any browser

-- Live charts will update automatically with new data.

### 🟪 5️⃣ Example Voice Alerts

-- Once connected, SwasthAI’s TTS system announces:

  -- ⚠️ “Heart rate is above normal range!”
 
  -- ✅ “SpO₂ level is stable.”
  
  -- 🩺 “Blood pressure within safe limit.”

### 🖥️ System Architecture
[Sensors] → [ESP8266 NodeMCU] → [Flask Server / ThingSpeak] → [ML Models] → [Dashboard (UI) + AI Recommendations]

### 🧑‍💻 Project Members

Manash Jyoti Mahanta

Ashraful Hoque Barbhuiya

Dhitiman Das

Abujaid Mondal
