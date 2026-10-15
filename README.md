# 🎓 Ders Calisma Asistanim

Ucretli yapay zeka ders asistanlarina (Astra AI vb.) alternatif olarak, Google Gemini API ve Streamlit kullanarak gelistirdigim, tamamen ucretsiz kisisel calisma arkadasim.

Bu proje, Python ogrenme surecimin bir parcasi olarak hem derslerimde basari oranimi artirmak hem de kendimi yazilim alaninda gelistirmek amaciyla tasarlanmistir.

---

## 🌐 Web Sitesine Nasil Erisilir?

Uygulamamiz internet uzerinde canli bir web sitesi olarak yayinlanmistir. Sitemizi kullanmak icin şu adimlari izleyebilirsiniz:

1. **Dogrudan Link Ile Erisim:** Tarayicinizin adres cubuguna dogrudan Streamlit Cloud uzerinden olusturulan size ozel canli site linkini yazarak (Bilgisayariniz kapali olsa bile) uygulamaya erisebilirsiniz.
2. **Google Uzerinden Erisim:** Projemiz acik kaynakli bir Streamlit uygulamasi oldugu icin, Google arama motoruna **"Ders Calisma Asistanim Streamlit"** veya dogrudan GitHub kullanici adinizla birlikte arama yaptiginizda projenin web sayfasina ulasabilirsiniz.

---

## 🚀 Ozellikler
- **Kisisel Ogretmen Modu:** Derslerle ilgili sorularinizi net, cana yakin ve aciklayici bir sekilde cevaplar.
- **Ucretsiz & Guvenli:** Pahali alternatiflerin aksine tamamen ucretsizdir ve kisisel Google API anahtari altyapisi ile calisir.
- **Sik ve Kolay Arayuz:** Streamlit kutuphanesi sayesinde kullanici dostu ve modern bir web tasarimi sunar.

---

## 🛠️ Kullanilan Teknolojiler
- **Python** (Temel Programlama Dili)
- **Streamlit** (Web Arayuzu Tasarimi ve Cloud Yayinlama)
- **python-dotenv** (Gelistirici Sifre Gizleme Altyapisi)
- **Google Generative AI API** (`gemini-flash-latest` Yapay Zeka Modeli)

---

## 💻 Yerel Bilgisayarda Kurulum ve Calistirma

Projeyi kendi bilgisayarinizda VS Code ile calistirmak isterseniz:

1. Gerekli kutuphaneleri yukleyin:
   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```
2. Proje ana dizininde **`.env`** adinda bir dosya olusturun ve icine anahtarinizi su sekilde yazin:
   ```text
   GEMINI_API_KEY=AQ.Ab8RN...SifrenizBuraya
   ```
3. Terminal uzerinden uygulamayi baslatin:
   ```bash
   streamlit run app.py
   ```

2. `app.py` dosyasındaki `API_KEY` kısmına kendi Google AI Studio anahtarınızı yazın.
3. Terminal üzerinden uygulamayı başlatın:
   ```bash
   streamlit run app.py
   ```
