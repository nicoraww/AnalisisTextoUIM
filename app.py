import streamlit as st
from textblob import TextBlob

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Sentimientos",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Imagen de encabezado
st.image("https://cdn.pixabay.com/photo/2017/01/31/17/44/heart-2028247_1280.png", use_column_width=True)

# Estilo con CSS para mejorar la apariencia
st.markdown(
    """
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #ff5733;
        }
        .subheader {
            text-align: center;
            font-size: 20px;
            color: #444;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">🔍 Análisis de Sentimientos con TextBlob</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Descubre la polaridad y subjetividad de cualquier texto</p>', unsafe_allow_html=True)

# Sidebar con información
with st.sidebar:
    st.subheader("📌 Polaridad y Subjetividad")
    st.markdown("""
    - **Polaridad:** Indica si el sentimiento expresado en el texto es positivo, negativo o neutral.  
      *Rango: -1 (muy negativo) a 1 (muy positivo).*
    
    - **Subjetividad:** Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo (hechos).  
      *Rango: 0 (objetivo) a 1 (subjetivo).*
    """)

# Análisis de Sentimiento
with st.expander('📊 Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('✍️ Escribe tu texto aquí:')
    
    if text1:
        blob = TextBlob(text1)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write(f'📌 **Polaridad:** {polarity}')
        st.write(f'📌 **Subjetividad:** {subjectivity}')
        
        # Determinar el sentimiento
        if polarity >= 0.5:
            st.success('😊 ¡Tu texto refleja un sentimiento Positivo!')
        elif polarity <= -0.5:
            st.error('😔 Tu texto refleja un sentimiento Negativo.')
        else:
            st.warning('😐 Tu texto tiene un sentimiento Neutral.')

# Corrección ortográfica
with st.expander('🔠 Corrección en inglés'):
    text2 = st.text_area('✍️ Escribe tu texto en inglés:', key='4')
    
    if text2:
        blob2 = TextBlob(text2)
        st.write("✅ **Texto corregido:**", blob2.correct())

