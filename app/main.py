from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="API Logistik Semen", version="1.0")

# Load model Machine Learning saat aplikasi baru menyala
model = joblib.load('ml_model.pkl')

# Skema data untuk input prediksi
class DataPengiriman(BaseModel):
    jarak_km: float
    berat_ton: float
    cuaca_buruk: int

# 1. Endpoint Health Check (Wajib untuk AWS ALB)
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# 2. Endpoint Data Stok Dummy
@app.get("/stok")
def cek_stok():
    return {
        "gudang_A": {"semen_portland": 1500, "semen_slag": 300},
        "gudang_B": {"semen_portland": 800, "semen_slag": 120}
    }

# 3. Endpoint Prediksi Keterlambatan (Machine Learning Inference)
@app.post("/predict-delay")
def prediksi_keterlambatan(data: DataPengiriman):
    fitur = [[data.jarak_km, data.berat_ton, data.cuaca_buruk]]
    prediksi = model.predict(fitur)
    
    hasil = "Terlambat" if prediksi[0] == 1 else "Tepat Waktu"
    return {"status_prediksi": hasil, "rekomendasi": "Hubungi koordinator armada" if prediksi[0] == 1 else "Lanjutkan pengiriman"}