## 🩺 Kalp Hastalığı Tahmini – Makine Öğrenmesi Projesi

## Proje Amacı
Projemiz, bireylerin sağlık verilerinden (yaş, boy, kilo, tansiyon, kolesterol, glikoz vb.) yararlanılarak **kalp hastalığı riskini** tahmin etmeyi amaçlamaktadır.

Bu projede amacımız farklı makine öğrenmesi algoritmalarını kullandıktan sonra, karşılaştırarak **en doğru ve en güvenilir tahmin modelini oluşturmaktır.**



## 📁 Kullanılan Veri Seti
- **Kaynak:** [Kaggle – Cardiovascular Disease Dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)
- **Veri Miktarı:** 70.000 gözlem, 13 özellik

Veri seti, yaş (gün cinsinden), boy, kilo, kan basıncı, kolesterol, glikoz, sigara, alkol, fiziksel aktivite gibi sağlık parametrelerini içermektedir.



## Kullanılan Yöntemler ve Modeller

### 📌 Aşamalar:
1. **Veri Ön İşleme:** `id` kaldırıldı, `age` gün → yıl dönüşümü yapıldı, StandardScaler ile ölçekleme yapıldı veriler ölçeklendirildi.
2. **x ve y ayrımı** yapıldı.
3. **train_test_split:** %70 eğitim / %30 test bölmesi olacak şekilde ayarlandı.
4. **Model Kurulumu:** Aşağıdaki algoritmalar ayrı ayrı test edildi:
    - LogisticRegression (baseline)
    - RandomForestClassifier
    - XGBoostClassifier
5. **Parametre Optimizasyonu:** Aşağıdaki optimizasyon yöntemleri denendi ve en uygun olanı seçildi.
    - GridSearchCV (Logistic Regression)
    - RandomizedSearchCV (Random Forest, XGBoost)
6. **Model Performans Değerlendirmesi:**
    - Accuracy
    - Precision
    - Recall
    - F1 Score
    - Confusion Matrix
                                                                                                              
  şeklindedir.



## ⚙️ En Başarılı Modeller ve Sonuçları

| Model                           | Accuracy | Precision | Recall | F1 Score |
|---------------------------------|----------|-----------|--------|----------|
| Logistic Regression             | 0.72     | 0.74      | 0.68   | 0.71     |
| Random Forest (Optimize)        | 0.74     | 0.76      | 0.70   | 0.73     |
| XGBoost (Optimize)              | 0.74     | 0.76      | 0.70   | 0.73     |

**Verilen Karar:** XGBoost optimize edildiğinde en yüksek skoru verdi, ancak Logistic Regression daha sade, daha yorumlanabilir ve yeterince güçlü olduğu için final model olarak tercih edildi.



## Denenen Ama Uygun Görülmeyen Yöntemler

- KNN: Veri büyüklüğü ve yapısı sebebiyle tercih edilmedi.
- SVM: Eğitim süresi ve doğrusal olmayan yapı ihtimali nedeniyle dışlandı.
- MLP (Yapay Sinir Ağı): Gereksiz karmaşıklık yaratacağı için tercih edilmedi.



## Öğrenilenler

- Basit modeller, iyi hazırlanmış veri ile çok güçlü sonuçlar verebilir.
- Her veri seti için en iyi model farklıdır: model değil **veri belirleyicidir**.
- F1 Score değerlendirmesi, dengesiz sınıflarda en anlamlı metriktir.
- `class_weight`, `GridSearch`, `RandomizedSearch` gibi tekniklerle model performansı artırılabilir.



## Kullanılan Kütüphaneler
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- xgboost



## Projenin Paylaşımı

- **Kaggle:** 
- **GitHub:** 



## Geliştirme Önerileri

- Yeni özellikler (BMI, yaş grubu vs.) oluşturulabilir.
- SMOTE ile sınıf dengesi daha iyi hale getirilebilir.
- Ensemble modeller (Voting, Stacking) denenebilir.
- Cinsiyete göre kalp hastalığı etkisi araştırılıp cinsiyet-hastalık ilişkisi kurulabilir.
- Daha büyük veri setleriyle test edilebilir.
- Klinik özellikler genişletilerek model zenginleştirilebilir.
- Arayüz mobil uyumlu hale getirilebilir.
