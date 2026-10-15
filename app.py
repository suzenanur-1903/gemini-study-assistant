import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Gizli sifremizi yukleyelim
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Ders Calisma Asistanim", page_icon="🎓")
st.title("🎓 Ders Calisma Asistanim")
st.write("Python ve Gemini API ile gelistirilmis kisisel ogrenme asistani.")

if not API_KEY:
    st.error("⚠️ Yapay zeka anahtari (.env dosyasi) bulunamadi veya ici bos!")
else:
    genai.configure(api_key=API_KEY)

kullanici_sorusu = st.text_input("Dersinizle ilgili bir soru sorun veya anlamadiginiz konuyu yazin:")

if st.button("Soruyu Cevapla ✨"):
    if kullanici_sorusu and API_KEY:
        # Spinner icinde beklerken akis baslayacak
        with st.spinner("Dusunuyorum ve yaziyorum... 🧠"):
            try:
                model = genai.GenerativeModel("gemini-flash-latest")
                sistem_talimati = f"You are a friendly and helpful tutor. Explain the following query to a student clearly and in Turkish language: {kullanici_sorusu}"
                
                # generate_content yerine stream_generate_content kullaniyoruz!
                cevap_akisi = model.generate_content(sistem_talimati, stream=True)
                
                st.success("Iste Cevabin:")
                
                # Kelimeleri ekrana canli canli yazdiran Streamlit sihri
                st.write_stream(chunk.text for chunk in cevap_akisi)
                
            except Exception as hata:
                st.error(f"Bir hata olustu: {hata}")
    elif not kullanici_sorusu:
        st.warning("Lutfen once bir soru yazin!")



