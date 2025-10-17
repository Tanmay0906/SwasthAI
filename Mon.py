# ==================================
# SwasthAI Flask API (All Models)
# ==================================

from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# ============================
# 🔰 Load Models Function
# ============================

def load_bp_models():
    bp_model = pickle.load(open('models/bp_model.pkl', 'rb'))
    sbp_model = bp_model['sbp_model']
    dbp_model = bp_model['dbp_model']
    return sbp_model, dbp_model

try:
    # Load BP models (SBP + DBP)
    sbp_model, dbp_model = load_bp_models()

    # Load other models
    stress_model = pickle.load(open('models/stress_model.pkl','rb'))
    risk_model = pickle.load(open('models/risk_model.pkl','rb'))
    fall_model = pickle.load(open('models/fall_model.pkl','rb'))

    # Load dataset for LabelEncoder fitting
    df = pd.read_csv('SwasthAI_dataset.csv')

    # Initialize label encoders
    le_stress = LabelEncoder().fit(df['Stress'])
    le_risk = LabelEncoder().fit(df['Risk'])
    le_fall = LabelEncoder().fit(df['Fall'])

    print("✅ All models and encoders loaded successfully.")

except Exception as model_load_error:
    print(f"🔴 Error loading models or dataset: {model_load_error}")
    exit(1)  # Exit if models are not loaded properly

# ============================
# 🔰 Home Route
# ============================

@app.route('/')
def home():
    return "✅ SwasthAI Flask ML Server Running"

# ============================
# 🔰 Prediction Route
# ============================

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract sensor data from request
        hr = float(data['heartRate'])
        spo2 = float(data['spo2'])
        body_temp = float(data['body_temperature'])
        room_temp = float(data['room_temperature'])  # optional usage later
        ecg = float(data['ecg'])
        x = float(data['x'])
        y = float(data['y'])
        z = float(data['z'])
        spo2_var = float(data.get('spo2_var', 2.0))  # optional default

        # ============================
        # 🔷 BP Prediction
        # ============================
        X_bp = pd.DataFrame([[hr, spo2]], columns=['HR', 'SpO2'])
        sbp_pred = sbp_model.predict(X_bp)[0]
        dbp_pred = dbp_model.predict(X_bp)[0]

        # ============================
        # 🔷 Stress Prediction
        # ============================
        X_stress = pd.DataFrame([[hr, spo2_var]], columns=['HR', 'SpO2_var'])
        stress_pred_enc = stress_model.predict(X_stress)
        stress_pred = le_stress.inverse_transform(stress_pred_enc)[0]

        # ============================
        # 🔷 Risk Prediction
        # ============================
        X_risk = pd.DataFrame([[hr, spo2, body_temp, ecg]], columns=['HR', 'SpO2', 'Body_Temp', 'ECG'])
        risk_pred_enc = risk_model.predict(X_risk)
        risk_pred = le_risk.inverse_transform(risk_pred_enc)[0]

        # ============================
        # 🔷 Fall Detection Prediction
        # ============================
        X_fall = pd.DataFrame([[x, y, z]], columns=['X', 'Y', 'Z'])
        fall_pred_enc = fall_model.predict(X_fall)
        fall_pred = le_fall.inverse_transform(fall_pred_enc)[0]

        # ============================
        # 🔷 Return Combined Output
        # ============================
        return jsonify({
            "sbpEstimated": round(float(sbp_pred), 2),
            "dbpEstimated": round(float(dbp_pred), 2),
            "stressLevel": stress_pred,
            "riskLevel": risk_pred,
            "fallStatus": fall_pred
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ============================
# 🔰 Run Server
# ============================

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
