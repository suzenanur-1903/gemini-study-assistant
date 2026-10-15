# 🎓 Ders Çalışma Asistanım

Ücretli yapay zeka ders asistanlarına (Astra AI vb.) alternatif olarak, Google Gemini API ve Streamlit kullanarak geliştirdiğim, tamamen ücretsiz kişisel çalışma arkadaşım.

Bu proje, Python öğrenme sürecimin bir parçası olarak hem derslerimde başarı oranımı artırmak hem de kendimi yazılım alanında geliştirmek amacıyla tasarlanmıştır.

---

## 🌐 Web Sitesine Nasıl Erişilir?

Uygulamamız internet üzerinde canlı bir web sitesi olarak yayınlanmıştır. Sitemizi kullanmak için şu adımları izleyebilirsiniz:

1. **Doğrudan Link İle Erişim:** Tarayıcınızın adres çubuğuna doğrudan `https://streamlit.io` üzerinden oluşturulan size özel canlı site linkini yazarak (Bilgisayarınız kapalı olsa bile) uygulamaya erişebilirsiniz.
2. **Google Üzerinden Erişim:** Projemiz açık kaynaklı bir Streamlit uygulaması olduğu için, Google arama motoruna **"Gemini Study Assistant Streamlit"** veya doğrudan GitHub kullanıcı adınızla birlikte arama yaptığınızda projenin web sayfasına ulaşabilirsiniz.

---

## 🚀 Özellikler
- **Kişisel Öğretmen Modu:** Derslerle ilgili sorularınızı net, cana yakın ve açıklayıcı bir şekilde cevaplar.
- **Ücretsiz & Güvenli:** Pahalı alternatiflerin aksine tamamen ücretsizdir ve kişisel Google API anahtarı altyapısı ile çalışır.
- **Şık ve Kolay Arayüz:** Streamlit kütüphanesi sayesinde kullanıcı dostu ve modern bir web tasarımı sunar.

---

## 🛠️ Kullanılan Teknolojiler
- **Python** (Temel Programlama Dili)
- **Streamlit** (Web Arayüzü Tasarımı ve Cloud Yayınlama)
- **Google Generative AI API** (`gemini-flash-latest` Yapay Zeka Modeli)

---

## 💻 Yerel Bilgisayarda Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda VS Code ile çalıştırmak isterseniz:

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install streamlit google-generativeai
   ```
2. `app.py` dosyasındaki `API_KEY` kısmına kendi Google AI Studio anahtarınızı yazın.
3. Terminal üzerinden uygulamayı başlatın:
   ```bash
   streamlit run app.py
   ```
