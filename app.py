import streamlit as st
from textblob import TextBlob
import time

# Animación CSS para los emojis
st.markdown("""
<style>
  @keyframes floatEmoji {
    0%   { transform: translateY(0); }
    50%  { transform: translateY(-20px); }
    100% { transform: translateY(0); }
  }
  .emoji-anim {
    font-size: 5rem;
    text-align: center;
    animation: floatEmoji 2s ease-in-out infinite;
    margin: 1rem 0;
  }
</style>
""", unsafe_allow_html=True)

st.title('Uso de TextBlob')

st.subheader("Analiza la polaridad y subjetividad de tu texto")

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe tu frase aquí:', height=150)
    if text1:
        blob = TextBlob(text1)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write(f'**Polaridad:** {polarity}')
        st.write(f'**Subjetividad:** {subjectivity}')

        # Clasificación y animación
        if polarity >= 0.5:
            st.balloons()
            st.markdown('<div class="emoji-anim">😊</div>', unsafe_allow_html=True)
            st.success('Es un sentimiento **Positivo**')
        elif polarity <= -0.5:
            st.markdown('<div class="emoji-anim">😔</div>', unsafe_allow_html=True)
            st.error('Es un sentimiento **Negativo**')
        else:
            st.markdown('<div class="emoji-anim">😐</div>', unsafe_allow_html=True)
            st.info('Es un sentimiento **Neutral**')

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe tu frase en inglés:', key='corr', height=100)
    if text2:
        blob2 = TextBlob(text2)
        st.write('**Corrección sugerida:**', blob2.correct())
