
import streamlit as st
import os
import base64

st.set_page_config(
    page_title="Belen Cajahuaman | Portafolio 2026",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# FONDO
# =====================================================

def cargar_fondo(ruta):
    if os.path.exists(ruta):
        with open(ruta, "rb") as archivo:
            return base64.b64encode(archivo.read()).decode()
    return None

fondo = cargar_fondo("fondo.jpg")

if fondo:
    fondo_css = f"""
    background-image:
        linear-gradient(rgba(230, 245, 251, 0.18),
                        rgba(230, 245, 251, 0.18)),
        url("data:image/jpeg;base64,{fondo}");
    """
else:
    fondo_css = """
    background: linear-gradient(
        135deg, #dff3f8, #e9edfa, #f9eaf0
    );
    """

# =====================================================
# ESTILOS
# =====================================================

st.html(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&family=Caveat:wght@600;700&display=swap');

.stApp {{
    {fondo_css}
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
    background-repeat: no-repeat !important;
    font-family: 'Poppins', sans-serif !important;
}}

html, body, [class*="css"] {{
    font-family: 'Poppins', sans-serif !important;
    font-size: 16px !important;
}}

[data-testid="stHeader"] {{
    background: transparent !important;
}}

#MainMenu, footer {{
    visibility: hidden;
}}

.block-container {{
    max-width: 1600px;
    padding: 2.5rem 3rem 2rem;
}}

/* TITULOS */

h1 {{
    font-family: 'Caveat', cursive !important;
    font-size: 96px !important;
    color: #26366e !important;
    font-weight: 700 !important;
    line-height: 1.05 !important;
    margin-bottom: 5px !important;
}}

h2 {{
    font-size: 32px !important;
    color: #28366e !important;
    font-weight: 800 !important;
}}

h3 {{
    font-size: 23px !important;
    color: #344b7c !important;
    font-weight: 800 !important;
}}

/* TEXTOS */

p {{
    color: #344b62 !important;
    font-size: 16px !important;
    line-height: 1.85 !important;
}}

.stCaption, [data-testid="stCaptionContainer"] p {{
    color: #496b82 !important;
    font-size: 14px !important;
    line-height: 1.7 !important;
}}

.top-label {{
    color: #395d7c;
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
}}

.name-label {{
    display: inline-block;
    background: #83bdd4;
    color: white;
    padding: 12px 28px;
    border-radius: 30px;
    font-size: 20px;
    font-weight: 800;
    margin: 10px 0 18px;
}}

/* PANEL PRINCIPAL: FONDO SÓLIDO */

[data-testid="stVerticalBlockBorderWrapper"] {{
    background: #f5fcff !important;
    border: 2px solid #ffffff !important;
    border-radius: 28px !important;
    box-shadow: 0 12px 35px rgba(44, 88, 122, 0.16) !important;
    padding: 22px !important;
}}

/* TARJETAS INTERNAS */

[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlockBorderWrapper"] {{
    background: #e5f5fb !important;
    border: 2px solid #ffffff !important;
    border-radius: 22px !important;
    padding: 17px !important;
    box-shadow: 0 6px 18px rgba(68, 130, 160, 0.12) !important;
    transition: transform .2s ease;
}}

[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlockBorderWrapper"]:hover {{
    transform: translateY(-4px);
}}

/* NUMERACIÓN Y CATEGORÍAS */

.project-number {{
    display: inline-block;
    background: #478eaf;
    color: white;
    border-radius: 20px;
    padding: 5px 12px;
    font-size: 13px;
    font-weight: 900;
}}

.project-category {{
    color: #3e7595;
    font-size: 13px;
    font-weight: 800;
    text-transform: uppercase;
}}

/* DESCRIPCIONES */

.project-description {{
    color: #344f65;
    font-size: 15px;
    line-height: 1.8;
    min-height: 100px;
}}

/* IMAGENES */

[data-testid="stImage"] img {{
    border-radius: 16px !important;
    object-fit: cover;
}}

/* BOTONES */

div.stLinkButton > a {{
    background: linear-gradient(110deg, #378eae, #777db5) !important;
    border: none !important;
    border-radius: 13px !important;
    color: #ffffff !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 15px !important;
    font-weight: 800 !important;
    padding: 14px 12px !important;
    text-align: center !important;
    transition: .2s ease;
}}

div.stLinkButton > a:hover {{
    background: linear-gradient(110deg, #267b9b, #5f66a3) !important;
    color: #ffffff !important;
    transform: translateY(-3px);
}}

/* METRICAS */

[data-testid="stMetric"] {{
    background: #e5f5fb;
    padding: 18px;
    border-radius: 17px;
}}

[data-testid="stMetricLabel"] {{
    color: #365f7c !important;
    font-size: 15px !important;
}}

[data-testid="stMetricValue"] {{
    color: #287b9d !important;
    font-size: 36px !important;
    font-weight: 800 !important;
}}

/* DIVISORES */

hr {{
    border-color: #c9e5f0 !important;
    margin: 30px 0 !important;
}}

.footer {{
    color: #345c79;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 2px;
    text-align: center;
    padding: 30px 0 15px;
}}

@media (max-width: 850px) {{
    .block-container {{
        padding: 1rem;
    }}

    h1 {{
        font-size: 65px !important;
    }}

    h2 {{
        font-size: 26px !important;
    }}

    h3 {{
        font-size: 20px !important;
    }}
}}
</style>
""")

# =====================================================
# PROYECTOS
# =====================================================

apps = [
    ("01", "Mi primera App", "Inicio",
     "Primera aplicación desarrollada para explorar Streamlit y GitHub.",
     "https://clase6-mwpnbk3fsbkennu2xxv2rr.streamlit.app/", "app_01.jpg"),

    ("02", "Texto a voz", "Voz",
     "Convierte contenido escrito en audio mediante síntesis de voz.",
     "https://s273ggysgxrvjc5xqcjjih.streamlit.app/", "app_02.JPG"),

    ("03", "Voz a texto", "Audio",
     "Transforma una entrada de voz en texto para facilitar la transcripción.",
     "https://traductor-7ggtnhxykyspqhtk6cypby.streamlit.app/", "app_03.JPG"),

    ("04", "Lector de texto", "Lectura",
     "Herramienta para trabajar con contenido textual mediante lectura por audio.",
     "https://e2vymapp8w22ojrpsuvqc2e.streamlit.app/", "app_04.JPG"),

    ("05", "OCR · Texto a audio", "OCR",
     "Extrae texto desde imágenes y permite convertir el contenido en audio.",
     "https://ocr-audio-ybjvud89srveyxujheuglj.streamlit.app/", "app_05.JPG"),

    ("06", "Análisis de sentimientos", "Texto",
     "Analiza contenido escrito para identificar el sentimiento presente.",
     "https://sentimenta-yvw8kjjhc3k5ahfm2bvbbk.streamlit.app/", "app_06.JPG"),

    ("07", "Nube de palabras", "NLP",
     "Genera una representación visual de las palabras más relevantes.",
     "https://wordcloud-twmeornb88bu5daiohmzth.streamlit.app/", "app_07.JPG"),

    ("08", "TF-IDF", "NLP",
     "Compara documentos y preguntas mediante TF-IDF y similitud de coseno.",
     "https://tdfesp-mmsucjw6w26aff34fpsenn.streamlit.app/", "app_08.JPG"),

    ("09", "Detector de objetos", "Visión",
     "Detecta objetos presentes en imágenes mediante visión por computador.",
     "https://yolov5-3qhk7h6k3kr9tjfgepuekf.streamlit.app/", "app_09.JPG"),

    ("10", "Detector de gestos", "Visión",
     "Analiza imágenes para identificar gestos y personas con Teachable Machine.",
     "https://zb8fhzc4q6vjd726eqkviy.streamlit.app/", "app_10.JPG"),

    ("11", "Evalua Pro", "Lenguaje",
     "Aplicación de procesamiento de lenguaje para trabajar con documentos.",
     "https://chatpdf-wajopxwdovw7vz87rbnfhe.streamlit.app/", "app_11.JPG"),

    ("12", "Vision Lab", "Imagen",
     "Herramienta para explorar el análisis y procesamiento de imágenes.",
     "https://visionapp-zvhnrjnesqyqvadmnjrmc9.streamlit.app/", "app_12.JPG"),

    ("13", "Detección de dígitos", "Visión artificial",
     "Aplicación para reconocer números escritos a mano.",
     "https://mnistpred-hrccjfx4k2uhhhk7gcyz8u.streamlit.app/", "app_13.JPG"),

    ("14", "Tablero personalizado", "Dashboard",
     "Tablero interactivo y personalizado para visualizar información.",
     "https://tablero-personalizado-xjfuqgnb5qihv88yjjozpv.streamlit.app/", "app_14.JPG"),

    ("15", "Tablero inteligente", "Dashboard",
     "Panel inteligente para consultar y visualizar información.",
     "https://histinf-eru35yru5ruy67cr7gqgts.streamlit.app/", "app_15.JPG"),

    ("16", "Lienzo interactivo: Habla Trazo", "Interacción",
     "Experiencia interactiva que conecta la voz y el dibujo.",
     "https://hablatrazo-kxusb3ttrzyctfph4gktmz.streamlit.app/", "app_16.JPG"),

    ("17", "De Wokwi a Streamlit", "IoT · MQTT",
     "Conecta datos de un dispositivo simulado en Wokwi con Streamlit.",
     "https://recepmqtt-dudyrincxvdsvf8rxrfb55.streamlit.app/", "app_17.JPG"),

    ("18", "De Streamlit a Wokwi", "IoT · MQTT",
     "Comunicación desde Streamlit hacia un dispositivo mediante MQTT.",
     "https://sendcmqtt-ddtw2ekzvyfjngaamhbkra.streamlit.app/", "app_18.JPG"),

    ("19", "Control por Voz", "Voz",
     "Permite interactuar y controlar funciones mediante comandos de voz.",
     "https://ctrlvoice-9pedwjpvfprq6xjcdzaptz.streamlit.app/", "app_19.JPG")
]

# =====================================================
# PRESENTACIÓN
# =====================================================

st.markdown(
    '<div class="top-label">PORTAFOLIO ACADÉMICO · 2026</div>',
    unsafe_allow_html=True
)

st.title("Mi portafolio")

st.subheader("de Interfaces Multimodales 2026")

st.markdown(
    '<div class="name-label">Belen Cajahuaman</div>',
    unsafe_allow_html=True
)

st.write(
    "Un espacio donde la creatividad, el diseño y la tecnología "
    "se encuentran. En este portafolio presento los proyectos que "
    "he desarrollado durante mi aprendizaje en Interfaces "
    "Multimodales."
)

st.write(
    "Explora mis experiencias con procesamiento de lenguaje, "
    "reconocimiento de voz, visión artificial, inteligencia "
    "artificial, visualización de datos y comunicación IoT."
)

st.divider()

# =====================================================
# DISTRIBUCIÓN: INFORMACIÓN Y GALERÍA
# =====================================================

col_info, col_projects = st.columns([0.85, 2.4], gap="large")

# PANEL IZQUIERDO

with col_info:
    with st.container(border=True):

        st.subheader("Sobre mí")

        st.write(
            "Soy Belen Cajahuaman, estudiante apasionada por "
            "la tecnología, la inteligencia artificial y las "
            "interfaces multimodales."
        )

        st.write(
            "Aquí comparto 19 proyectos desarrollados durante "
            "mi aprendizaje, combinando creatividad, programación "
            "y soluciones digitales."
        )

        st.divider()

        st.subheader("Mi formación")
        st.write("Interfaces Multimodales · 2026")

        st.divider()

        st.subheader("Tecnologías")
        st.write(
            "Python · Streamlit · Inteligencia Artificial · "
            "Procesamiento de Lenguaje · Visión Artificial · "
            "IoT · MQTT"
        )

        st.divider()

        st.subheader("Mi objetivo")
        st.write(
            "Crear experiencias digitales que conecten a las "
            "personas con la tecnología mediante diferentes "
            "formas de interacción."
        )

        st.divider()

        st.metric("Proyectos desarrollados", "19")

# PANEL DERECHO

with col_projects:
    with st.container(border=True):

        st.subheader("✦ Mis proyectos")

        st.write(
            "Explora cada aplicación, conoce su propósito "
            "y accede a ella mediante el botón."
        )

        st.divider()

        for inicio in range(0, len(apps), 3):

            columnas = st.columns(3, gap="large")

            for columna, app in zip(columnas, apps[inicio:inicio + 3]):

                numero, titulo, categoria, descripcion, url, imagen = app

                with columna:
                    with st.container(border=True):

                        if os.path.exists(imagen):
                            st.image(
                                imagen,
                                use_container_width=True
                            )
                        else:
                            st.markdown(f"### Proyecto {numero}")
                            st.caption(
                                f"Agrega la imagen {imagen} a GitHub."
                            )

                        st.markdown(
                            f'<span class="project-number">{numero}</span> '
                            f'<span class="project-category">{categoria}</span>',
                            unsafe_allow_html=True
                        )

                        st.subheader(titulo)

                        st.markdown(
                            f'<div class="project-description">'
                            f'{descripcion}</div>',
                            unsafe_allow_html=True
                        )

                        st.link_button(
                            "EXPLORAR PROYECTO ↗",
                            url,
                            use_container_width=True
                        )

# =====================================================
# HABILIDADES
# =====================================================

st.divider()

with st.container(border=True):

    st.subheader("✦ Lo que he desarrollado")

    st.write(
        "A lo largo de estos proyectos he explorado diferentes "
        "herramientas y tecnologías para crear experiencias digitales."
    )

    c1, c2, c3 = st.columns(3, gap="large")

    with c1:
        st.markdown("### Procesamiento de información")
        st.write("NLP · TF-IDF · Análisis de sentimientos · OCR")

    with c2:
        st.markdown("### Interacción multimodal")
        st.write("Voz · Audio · Imagen · Dibujo · Visión artificial")

    with c3:
        st.markdown("### Tecnología y conexión")
        st.write("Python · Streamlit · MQTT · Wokwi · Dashboards")

# =====================================================
# PIE DE PÁGINA
# =====================================================

st.markdown(
    '<div class="footer">'
    'BELEN CAJAHUAMAN · INTERFACES MULTIMODALES · 2026'
    '<br>CREATIVIDAD · TECNOLOGÍA · INNOVACIÓN'
    '</div>',
    unsafe_allow_html=True
)
