import streamlit as st
import pyttsx3                   
from PyPDF2 import PdfReader  

st.title("📘 PDF Reader")

file = st.file_uploader(" ",["pdf"])
st.markdown("---")

def con(file):
    st.sidebar.title("⚙️ Control Panel")
    
    i = st.sidebar.number_input("📄 Enter Page Number:",min_value=0, max_value=100, step=1)
    st.sidebar.info("Note:- Here page number starts from 0")
    reader = PdfReader(file)   
    pages = reader.pages                    
    st.write("You are on Page:",i+1)
    
    melo = pyttsx3.init()     
    page = reader.pages[i]    
    text = page.extract_text()
    
    st.success(text)
    
    col1, col2, col3= st.sidebar.columns(3)

    with col1:
        if st.button("🔊 Play"):
            melo = pyttsx3.init()
            melo.say(text)
            melo.runAndWait()
    
    with col2:
        if st.button("🔇 Stop"):
            melo = pyttsx3.init()
            melo.stop()
            st.sidebar.write("Stopped reading.")

    with col3:
        st.text(" ")
       
if file is not None:
    con(file)

st.write("📝 Description")
st.write("""
PDF Reader is a smart, document assistant designed to help you read and interact with PDF content effortlessly. With a sleek interface and intuitive controls, it allows you to:
- 📄 Upload PDF files up to 200MB.
- 🔢 Select specific pages for focused reading.
- 🔊 Play text aloud using built-in audio controls.
- 🔇 Stop playback anytime.""")
    
st.markdown("---")
st.markdown("Developed by Ravi Prajapati using Streamlit & Python")