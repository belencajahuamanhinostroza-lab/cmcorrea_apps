
import streamlit as st
import os

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Mi Portafolio 2026",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# DISEÑO Y ESTILOS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Amatic+SC:wght@700&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background: #ffffff;
    color: #24485a;
}

#MainMenu, footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1200px;
    padding-top: 1rem;
    padding-bottom: 0;
}

/* NAVEGACIÓN */

.top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 15px 22px;
}

.logo {
    color: #08799b;
    font-size: 23px;
    font-weight: 900;
    line-height: .85;
    letter-spacing: -2px;
}

.nav-links {
    display: flex;
    gap: 22px;
    font-size: 12px;
    font-weight: 800;
}

.nav-links a {
    color: #34758b !important;
    text-decoration: none;
}

/* HERO */

.hero {
    position: relative;
    overflow: hidden;
    min-height: 530px;
    padding: 35px 35px 65px;
    text-align: center;
    background: linear-gradient(
        180deg,
        #08719a 0%,
        #16a3c3 48%,
        #a8e9e9 100%
    );
    border-radius: 3px;
}

.hero:before {
    content: "";
    position: absolute;
    width: 135px;
    height: 135px;
    background: #ffd66e;
    border-radius: 50%;
    top: 85px;
    right: 12%;
    box-shadow: 0 0 50px rgba(255,226,127,.55);
}

.cloud {
    position: absolute;
    background: #ffffff;
    height: 36px;
    width: 135px;
    border-radius: 50px;
    opacity: .95;
}

.cloud:before,
.cloud:after {
    content: "";
    position: absolute;
    background: #ffffff;
    border-radius: 50%;
}

.cloud:before {
    width: 65px;
    height: 65px;
    top: -35px;
    left: 20px;
}

.cloud:after {
    width: 55px;
    height: 55px;
    top: -24px;
    right: 15px;
}

.cloud-one {
    top: 190px;
    left: 5%;
}

.cloud-two {
    top: 260px;
    right: 5%;
    transform: scale(1.3);
}

.cloud-three {
    top: 380px;
    left: 16%;
    transform: scale(.8);
}

.hero-content {
    position: relative;
    z-index: 3;
}

.hero-label {
    color: #d9ffff;
    font-size: 12px;
    font-weight: 900;
    letter-spacing: 3px;
    margin-top: 30px;
}

.hero h1 {
    color: white !important;
    font-size: clamp(45px, 8vw, 82px) !important;
    font-weight: 900 !important;
    letter-spacing: -4px;
    line-height: 1;
    margin: 20px 0 5px;
    text-shadow: 0 5px 12px rgba(0,54,83,.17);
}

.hero-name {
    color: #fff1c4;
    font-size: 21px;
    font-weight: 800;
    margin-top: 8px;
}

.hero-subtitle {
    color: #ffffff;
    font-size: 19px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-top: 12px;
}

.hero-description {
    max-width: 600px;
    margin: 14px auto;
    color: #e8ffff;
    font-size: 15px;
    line-height: 1.7;
}

.hero-tag {
    display: inline-block;
    margin-top: 15px;
    padding: 9px 18px;
    color: #27637a;
    background: #ffffff;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 1px;
}

.hero-bottom {
    position: absolute;
    z-index: 2;
    height: 95px;
    bottom: -42px;
    left: -3%;
    width: 106%;
    background: white;
    border-radius: 50% 50% 0 0;
}

/* PRESENTACIÓN */

.intro {
    text-align: center;
    padding: 35px 15px 25px;
}

.intro-title {
    font-family: 'Amatic SC', cursive;
    font-size: 43px;
    color: #34758b;
    font-weight: 700;
}

.intro-text {
    color: #7b929b;
    font-size: 14px;
    line-height: 1.7;
    max-width: 650px;
    margin: 5px auto;
}

/* PROYECTOS */

.projects-title {
    text-align: center;
    color: #34758b;
    font-family: 'Amatic SC', cursive;
    font-size: 48px;
    margin-top: 15px;
}

.projects-subtitle {
    text-align: center;
    color: #849ba3;
    font-size: 13px;
    margin-bottom: 30px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border: 1px solid #e1eeee !important;
    border-radius: 13px !important;
    padding: 10px !important;
    box-shadow: 0 5px 18px rgba(30,91,111,.08);
    transition: transform .2s ease, box-shadow .2s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 25px rgba(30,91,111,.15);
}

[data-testid="stImage"] img {
    border-radius: 8px;
    object-fit: cover;
}

.app-number {
    color: #e99b38;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 1px;
}

.app-category {
    color: #4b9eb2;
    font-size: 10px;
    font-weight: 900;
    text-transform: uppercase;
    text-align: right;
}

.app-title {
    color: #34758b;
    font-size: 19px;
    font-weight: 900;
    margin-top: 8px;
    line-height: 1.2;
}

.app-description {
    color: #83969c;
    font-size: 12px;
    line-height: 1.6;
    min-height: 58px;
    margin-top: 8px;
}

div.stLinkButton > a {
    width: 100%;
    background: #f3a137 !important;
    border: none !important;
    border-radius: 7px !important;
    color: #ffffff !important;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: .7px;
    transition: .2s;
}

div.stLinkButton > a:hover {
    background: #df8125 !important;
    color: white !important;
}

/* CONTACTO */

.contact-section {
    text-align: center;
    padding: 45px 20px 55px;
    margin-top: 55px;
    background: linear-gradient(
        180deg,
        #e6f8f5,
        #c9f0e9
    );
    border-radius: 15px 15px 0 0;
}

.contact-title {
    font-family: 'Amatic SC', cursive;
    color: #34758b;
    font-size: 43px;
}

.contact-text {
    color: #728d96;
    font-size: 13px;
    line-height: 1.8;
}

.contact-tag {
    display: inline-block;
    margin-top: 12px;
    color: #ffffff;
    background: #328ca1;
    padding: 10px 22px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 900;
}

.footer {
    text-align: center;
    padding: 20px;
    background: #bce9df;
    color: #4c8490;
    font-size: 11px;
    font-weight: 800;
}

/* RESPONSIVE */

@media (max-width: 700px) {

    .top-nav {
        padding: 10px 5px;
    }

    .nav-links {
        gap: 9px;
        font-size: 9px;
    }

    .hero {
        min-height: 480px;
        padding: 25px 15px 55px;
    }

    .hero h1 {
        font-size: 48px !important;
        letter-spacing: -2px;
    }

    .hero-name {
        font-size: 17px;
    }

    .hero-subtitle {
        font-size: 15px;
    }

    .hero-description {
        font-size: 13px;
    }

    .projects-title {
        font-size: 39px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVEGACIÓN
# ============================================================

st.markdown("""
<div class="top-nav">
    <div class="logo">B.<br>CAJAHUAMAN</div>

    <div class="nav-links">
        <a href="#inicio">INICIO</a>
        <a href="#proyectos">PROYECTOS</a>
        <a href="#contacto">CONTACTO</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# ENCABEZADO PRINCIPAL
# ============================================================

st.markdown("""
<div class="hero" id="inicio">

    <div class="cloud cloud-one"></div>
    <div class="cloud cloud-two"></div>
    <div class="cloud cloud-three"></div>

    <div class="hero-content">

        <div class="hero-label">
            PORTAFOLIO ACADÉMICO · 2026
        </div>

        <h1>MI PORTAFOLIO</h1>

        <div class="hero-name">
            Belen Cajahuaman
        </div>

        <div class="hero-subtitle">
            INTERFACES MULTIMODALES
        </div>

        <div class="hero-description">
            Un espacio donde la creatividad, la tecnología y la
            interacción se unen. Explora mis aplicaciones y proyectos
            desarrollados durante el año 2026.
        </div>

        <div class="hero-tag">
            19 PROYECTOS · TECNOLOGÍA · CREATIVIDAD
        </div>

    </div>

    <div class="hero-bottom"></div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PRESENTACIÓN
# ============================================================

st.markdown("""
<div class="intro">

    <div class="intro-title">
        ¡Bienvenido a mi mundo creativo!
    </div>

    <div class="intro-text">
        Cada proyecto representa una nueva experiencia de aprendizaje.
        He explorado herramientas para trabajar con texto, voz,
        imágenes, inteligencia artificial y diferentes formas de
        interacción digital.
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# TÍTULO DE PROYECTOS
# ============================================================

st.markdown("""
<div id="proyectos" class="projects-title">
    Mis aplicaciones
</div>

<div class="projects-subtitle">
    Explora los 19 proyectos que he desarrollado.
</div>
""", unsafe_allow_html=True)


# ============================================================
# LISTA COMPLETA DE 19 PROYECTOS
# ============================================================

apps = [
    {
        "numero": "01",
        "titulo": "Mi primera App",
        "categoria": "Inicio",
        "descripcion": "Primera aplicación del portafolio para explorar Streamlit y Github.",
        "url": "https://clase6-mwpnbk3fsbkennu2xxv2rr.streamlit.app/",
        "imagen": "app_01.jpg"
    },
    {
        "numero": "02",
        "titulo": "Texto a voz",
        "categoria": "Voz",
        "descripcion": "Convierte contenido escrito en audio mediante síntesis de voz.",
        "url": "https://s273ggysgxrvjc5xqcjjih.streamlit.app/",
        "imagen": "app_02.JPG"
    },
    {
        "numero": "03",
        "titulo": "Voz a texto",
        "categoria": "Audio",
        "descripcion": "Transforma una entrada de voz en texto para facilitar la transcripción.",
        "url": "https://traductor-7ggtnhxykyspqhtk6cypby.streamlit.app/",
        "imagen": "app_03.JPG"
    },
    {
        "numero": "04",
        "titulo": "Lector de texto",
        "categoria": "Lectura",
        "descripcion": "Herramienta para trabajar con contenido textual mediante lectura por audio.",
        "url": "https://e2vymapp8w22ojrpsuvqc2e.streamlit.app/",
        "imagen": "app_04.JPG"
    },
    {
        "numero": "05",
        "titulo": "OCR · Texto a audio",
        "categoria": "OCR",
        "descripcion": "Extrae texto desde imágenes y permite convertir el contenido en audio.",
        "url": "https://ocr-audio-ybjvud89srveyxujheuglj.streamlit.app/",
        "imagen": "app_05.JPG"
    },
    {
        "numero": "06",
        "titulo": "Análisis de sentimientos",
        "categoria": "Texto",
        "descripcion": "Analiza contenido escrito para identificar el sentimiento presente en el texto.",
        "url": "https://sentimenta-yvw8kjjhc3k5ahfm2bvbbk.streamlit.app/",
        "imagen": "app_06.JPG"
    },
    {
        "numero": "07",
        "titulo": "Nube de palabras",
        "categoria": "NLP",
        "descripcion": "Genera una representación visual de las palabras más relevantes de un texto.",
        "url": "https://wordcloud-twmeornb88bu5daiohmzth.streamlit.app/",
        "imagen": "app_07.JPG"
    },
    {
        "numero": "08",
        "titulo": "TF-IDF",
        "categoria": "NLP",
        "descripcion": "Compara documentos y preguntas mediante TF-IDF y similitud de coseno.",
        "url": "https://tdfesp-mmsucjw6w26aff34fpsenn.streamlit.app/",
        "imagen": "app_08.JPG"
    },
    {
        "numero": "09",
        "titulo": "Detector de objetos",
        "categoria": "Visión",
        "descripcion": "Detecta objetos presentes en imágenes mediante visión por computador.",
        "url": "https://yolov5-3qhk7h6k3kr9tjfgepuekf.streamlit.app/",
        "imagen": "app_09.JPG"
    },
    {
        "numero": "10",
        "titulo": "Detector de gestos",
        "categoria": "Visión",
        "descripcion": "Analiza imágenes para identificar expresiones y personas con Teachable Machine.",
        "url": "https://zb8fhzc4q6vjd726eqkviy.streamlit.app/",
        "imagen": "app_10.JPG"
    },
    {
        "numero": "11",
        "titulo": "Evalua Pro",
        "categoria": "Lenguaje",
        "descripcion": "Aplicación de procesamiento de lenguaje natural para trabajar con documentos y evaluaciones.",
        "url": "https://chatpdf-wajopxwdovw7vz87rbnfhe.streamlit.app/",
        "imagen": "app_11.JPG"
    },
    {
        "numero": "12",
        "titulo": "Vision Lab",
        "categoria": "Imagen",
        "descripcion": "Herramienta para explorar el análisis y procesamiento de imágenes.",
        "url": "https://visionapp-zvhnrjnesqyqvadmnjrmc9.streamlit.app/",
        "imagen": "app_12.JPG"
    },
    {
        "numero": "13",
        "titulo": "Detección de dígitos",
        "categoria": "Visión artificial",
        "descripcion": "Aplicación para reconocer y detectar números escritos a mano.",
        "url": "https://mnistpred-hrccjfx4k2uhhhk7gcyz8u.streamlit.app/",
        "imagen": "app_13.JPG"
    },
    {
        "numero": "14",
        "titulo": "Tablero personalizado",
        "categoria": "Dashboard",
        "descripcion": "Tablero interactivo y personalizado para visualizar información.",
        "url": "https://tablero-personalizado-xjfuqgnb5qihv88yjjozpv.streamlit.app/",
        "imagen": "app_14.JPG"
    },
    {
        "numero": "15",
        "titulo": "Tablero inteligente",
        "categoria": "Dashboard",
        "descripcion": "Panel inteligente para consultar y visualizar información.",
        "url": "https://histinf-eru35yru5ruy67cr7gqgts.streamlit.app/",
        "imagen": "app_15.JPG"
    },
    {
        "numero": "16",
        "titulo": "Lienzo interactivo: Habla Trazo",
        "categoria": "Interacción",
        "descripcion": "Experiencia interactiva que conecta la voz y el dibujo.",
        "url": "https://hablatrazo-kxusb3ttrzyctfph4gktmz.streamlit.app/",
        "imagen": "app_16.JPG"
    },
    {
        "numero": "17",
        "titulo": "De Wokwi a Streamlit",
        "categoria": "IoT · MQTT",
        "descripcion": "Conecta datos de un dispositivo simulado en Wokwi con una interfaz en Streamlit.",
        "url": "https://recepmqtt-dudyrincxvdsvf8rxrfb55.streamlit.app/",
        "imagen": "app_17.JPG"
    },
    {
        "numero": "18",
        "titulo": "De Streamlit a Wokwi",
        "categoria": "IoT · MQTT",
        "descripcion": "Comunicación desde una interfaz Streamlit hacia un dispositivo mediante MQTT.",
        "url": "https://sendcmqtt-ddtw2ekzvyfjngaamhbkra.streamlit.app/",
        "imagen": "app_18.JPG"
    },
    {
        "numero": "19",
        "titulo": "Control por Voz",
        "categoria": "Voz",
        "descripcion": "Aplicación que permite interactuar y controlar funciones mediante comandos de voz.",
        "url": "https://ctrlvoice-9pedwjpvfprq6xjcdzaptz.streamlit.app/",
        "imagen": "app_19.JPG"
    }
]


# ============================================================
# GENERAR TARJETAS AUTOMÁTICAMENTE
# ============================================================

for inicio in range(0, len(apps), 3):

    columnas = st.columns(3, gap="medium")

    for columna, app_data in zip(
        columnas,
        apps[inicio:inicio + 3]
    ):

        with columna:

            with st.container(border=True):

                imagen = app_data["imagen"]

                if os.path.exists(imagen):
                    st.image(
                        imagen,
                        use_container_width=True
                    )
                else:
                    st.info(
                        f"Imagen pendiente: {imagen}"
                    )

                meta_col1, meta_col2 = st.columns(2)

                with meta_col1:
                    st.markdown(
                        f'<div class="app-number">PROYECTO {app_data["numero"]}</div>',
                        unsafe_allow_html=True
                    )

                with meta_col2:
                    st.markdown(
                        f'<div class="app-category">{app_data["categoria"]}</div>',
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f'<div class="app-title">{app_data["titulo"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="app-description">{app_data["descripcion"]}</div>',
                    unsafe_allow_html=True
                )

                st.link_button(
                    "EXPLORAR PROYECTO ↗",
                    app_data["url"],
                    use_container_width=True
                )


# ============================================================
# CONTACTO Y PIE DE PÁGINA
# ============================================================

st.markdown("""
<div class="contact-section" id="contacto">

    <div class="contact-title">
        ¡Gracias por visitar mi portafolio!
    </div>

    <div class="contact-text">
        Este es un recorrido por mis proyectos, ideas y aprendizajes.
        <br>
        La tecnología es una herramienta para imaginar y crear nuevas experiencias.
    </div>

    <div class="contact-tag">
        BELEN CAJAHUAMAN · PORTAFOLIO 2026
    </div>

</div>

<div class="footer">
    ✦ INTERFACES MULTIMODALES · STREAMLIT · GITHUB · 2026
</div>
""", unsafe_allow_html=True)
