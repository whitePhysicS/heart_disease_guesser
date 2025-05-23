import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Modeli yükle
with open("UI/kalp_hastaligi_model.pkl", "rb") as f:
    data = pickle.load(f)
    grids = data.best_estimator_  # LogisticRegression objesi

st.title("🩺 Kalp Hastalığı Tahmin Uygulaması")

# Kullanıcı girişi
age = st.slider("Yaş (yıl)", 20, 80, 45)
height = st.slider("Boy (cm)", 140, 210, 165)
weight = st.slider("Kilo (kg)", 40, 150, 70)
ap_hi = st.slider("Sistolik Tansiyon", 90, 200, 120)
ap_lo = st.slider("Diyastolik Tansiyon", 60, 150, 80)
chol_label = st.selectbox("Kolesterol Seviyesi", [
    "1 - Normal",
    "2 - Yüksek",
    "3 - Çok Yüksek"
])
chol = int(chol_label.split(" - ")[0])

gluc_label = st.selectbox("Glikoz Seviyesi", [
    "1 - Normal",
    "2 - Yüksek",
    "3 - Çok Yüksek"
])
gluc = int(gluc_label.split(" - ")[0])


smoke_label = st.selectbox("Sigara Kullanımı",["0 - Hayır", "1 - Evet"])
smoke = int(smoke_label.split("-")[0])

alco_label = st.selectbox("Alkol Kullanımı",["0 - Hayır", "1 - Evet"])
alco = int(alco_label.split("-")[0])

active_label = st.selectbox("Fiziksel Aktivite",["0 - Hayır", "1 - Evet"])
active = int(active_label.split("-")[0])

gender_label = st.radio("Cinsiyet", ["👨 Erkek", "👩 Kadın"])
gender = 1 if gender_label == "Erkek" else 2


# Özellik isimleri
feature_names = ["age_years", "gender", "height", "weight", "ap_hi", "ap_lo", "cholesterol", "gluc", "smoke", "alco", "active"]

# Tahmin butonu
if st.button("Tahmin Et"):
    girdi = pd.DataFrame([[age, gender, height, weight, ap_hi, ap_lo,
                           chol, gluc, smoke, alco, active]], columns=feature_names)

    tahmin = grids.predict(girdi)[0]
    olasilik = grids.predict_proba(girdi)[0][1]  # 1 sınıfının olasılığı

    st.write(f"Olasılık (kalp hastalığı): {olasilik:.2f}")
    sonuc = "🚨 Kalp Hastalığı Riski VAR" if tahmin == 1 else "✅ Kalp Hastalığı Riski YOK"
    st.subheader(sonuc)

