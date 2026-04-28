import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import random

print("Menyiapkan data fiktif pengiriman semen...")
# Membuat 500 baris data dummy
data = []
for _ in range(500):
    jarak = random.uniform(10, 500) # Jarak 10km - 500km
    berat = random.uniform(5, 40)   # Berat semen 5 - 40 ton
    cuaca = random.choice([0, 1])   # 0 = Cerah, 1 = Hujan/Badai
    
    # Logika sederhana: Jika jarak jauh + cuaca buruk, kemungkinan besar terlambat
    if jarak > 300 and cuaca == 1:
        terlambat = 1
    elif berat > 30 and cuaca == 1:
        terlambat = 1
    else:
        terlambat = random.choice([0, 0, 0, 1]) # Sisanya ada sedikit peluang terlambat

    data.append([jarak, berat, cuaca, terlambat])

# Ubah ke DataFrame Pandas
df = pd.DataFrame(data, columns=['jarak_km', 'berat_ton', 'cuaca_buruk', 'terlambat'])

# Pisahkan Fitur (X) dan Target (y)
X = df[['jarak_km', 'berat_ton', 'cuaca_buruk']]
y = df['terlambat']

print("Melatih model Random Forest...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Simpan model ke file .pkl
joblib.dump(model, 'ml_model.pkl')
print("Selesai! File ml_model.pkl berhasil dibuat.")