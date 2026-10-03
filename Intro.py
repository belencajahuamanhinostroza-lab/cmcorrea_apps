import os
import streamlit as st


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Mi Portafolio | Belen Cajahuaman",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# ESTILOS
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 15% 0%, rgba(255, 164, 218, .18), transparent 25%),
            radial-gradient(circle at 90% 12%, rgba(255, 214, 72, .14), transparent 22%),
            #f6f3f7;
        color: #171717;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    .block-container {
        max-width: 1240px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 3rem !important;
    }

    /* Barra superior */
    .top-line {
        width: 100%;
        height: 4px;
        background: #171717;
        margin-bottom: 12px;
    }

    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 4px 2px 18px;
        font-size: .72rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
        color: #5e5a62;
    }

    .top-nav .brand {
        color: #e35d4d;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1rem;
        letter-spacing: -.2px;
    }

    /* Hero */
    .hero {
        position: relative;
        overflow: hidden;
        min-height: 430px;
        margin-bottom: 34px;
        padding: 58px 52px;
        background: #fff;
        border: 1px solid #d9d5dd;
        box-shadow: 0 18px 40px rgba(40, 30, 50, .08);
    }

    .hero-shape-blue {
        position: absolute;
        width: 420px;
        height: 220px;
        right: -100px;
        top: -80px;
        background: #4458e7;
        transform: rotate(-8deg);
    }

    .hero-shape-pink {
        position: absolute;
        width: 280px;
        height: 160px;
        right: 90px;
        bottom: -70px;
        background: #ff78b6;
        transform: rotate(-10deg);
    }

    .hero-shape-lime {
        position: absolute;
        width: 145px;
        height: 145px;
        right: 140px;
        top: 95px;
        background: #c5ff1a;
        border-radius: 50%;
    }

    .hero-content {
        position: relative;
        z-index: 3;
        max-width: 800px;
    }

    .hero-small {
        font-size: .75rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
        color: #4458e7;
        margin-bottom: 12px;
    }

    .hero-name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #5c5961;
        margin-bottom: 8px;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(3.5rem, 8vw, 7rem);
        font-weight: 700;
        line-height: .86;
        letter-spacing: -5px;
        color: #171717;
        margin: 0;
    }

    .hero-title span {
        color: #e25b4e;
    }

    .hero-copy {
        max-width: 650px;
        margin-top: 24px;
        color: #6c6870;
        font-size: .93rem;
        line-height: 1.55;
    }

    .hero-tag {
        display: inline-block;
        margin-top: 20px;
        padding: 8px 12px;
        background: #c5ff1a;
        color: #232817;
        font-size: .68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .7px;
    }

    /* Sección */
    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: -1.3px;
        margin: 0;
        color: #171717;
    }

    .section-subtitle {
        color: #77727b;
        font-size: .82rem;
        margin-bottom: 18px;
    }

    /* Tarjetas */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border: 1px solid #d7d4db !important;
        border-radius: 4px !important;
        box-shadow: 0 10px 24px rgba(38, 31, 45, .07) !important;
        padding: 10px !important;
        margin-bottom: 24px !important;
    }

    [data-testid="stImage"] img {
        border-radius: 2px !important;
    }

    .app-meta {
        margin-top: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .app-number {
        color: #4458e7;
        font-size: .66rem;
        font-weight: 700;
        letter-spacing: .8px;
    }

    .app-category {
        color: #97939a;
        font-size: .61rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .8px;
    }

    .app-title {
        margin-top: 7px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.15rem;
        font-weight: 700;
        line-height: 1.08;
        color: #18181c;
    }

    .app-description {
        min-height: 52px;
        margin-top: 7px;
        color: #6d6972;
        font-size: .76rem;
        line-height: 1.48;
    }

    div.stLinkButton > a {
        width: 100% !important;
        background: #171717 !important;
        border: none !important;
        border-radius: 2px !important;
        color: white !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        font-size: .67rem !important;
        letter-spacing: .6px !important;
        text-transform: uppercase !important;
    }

    div.stLinkButton > a:hover {
        background: #4458e7 !important;
        color: white !important;
    }

    /* Pie */
    .footer-box {
        margin-top: 10px;
        padding: 22px;
        background: #171717;
        color: white;
    }

    .footer-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1rem;
        font-weight: 700;
    }

    .footer-text {
        margin-top: 4px;
        color: #cac7cd;
        font-size: .75rem;
    }

    @media (max-width: 700px) {
        .hero {
            padding: 34px 24px;
            min-height: 360px;
        }

        .hero-title {
            letter-spacing: -2.5px;
        }

        .hero-shape-blue {
            width: 260px;
            right: -90px;
        }

        .hero-shape-pink {
            width: 190px;
            right: 35px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# CABECERA
# ============================================================

st.markdown(
    """
<div class="top-line"></div>
<div class="top-nav">
    <div class="brand">✦ BELEN CAJAHUAMAN</div>
    <div>PORTAFOLIO · INTELIGENCIA ARTIFICIAL</div>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
<div class="hero">
    <div class="hero-shape-blue"></div>
    <div class="hero-shape-pink"></div>
    <div class="hero-shape-lime"></div>

    <div class="hero-content">
        <div class="hero-small">Portafolio personal</div>
        <div class="hero-name">Belen Cajahuaman</div>

        <div class="hero-title">
            Mi <span>Portafolio</span>
        </div>

        <div class="hero-copy">
            Una colección de aplicaciones y proyectos prácticos
            desarrollados para explorar diferentes usos de la
            Inteligencia Artificial.
        </div>

        <div class="hero-tag">
            10 aplicaciones · una colección
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# SECCIÓN DE APLICACIONES
# ============================================================

st.markdown(
    '<div class="section-title">Mis aplicaciones</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">Explora cada proyecto y abre la aplicación.</div>',
    unsafe_allow_html=True,
)


# ============================================================
# DATOS
# ============================================================

apps = [
    {
        "numero": "01",
        "titulo": "Mi primera App",
        "categoria": "Inicio",
        "descripcion": "Primera aplicación del portafolio para explorar de forma práctica el uso de Inteligencia Artificial.",
        "url": "https://clase6-mwpnbk3fsbkennu2xxv2rr.streamlit.app/",
        "imagen": "imagenes/app_01.png",
    },
    {
        "numero": "02",
        "titulo": "Texto a voz",
        "categoria": "Voz",
        "descripcion": "Convierte contenido escrito en audio mediante una aplicación de síntesis de voz.",
        "url": "https://s273ggysgxrvjc5xqcjjih.streamlit.app/",
        "imagen": "imagenes/app_02.png",
    },
    {
        "numero": "03",
        "titulo": "Voz a texto",
        "categoria": "Audio",
        "descripcion": "Transforma una entrada de voz en texto para facilitar la transcripción.",
        "url": "https://traductor-7ggtnhxykyspqhtk6cypby.streamlit.app/",
        "imagen": "imagenes/app_03.png",
    },
    {
        "numero": "04",
        "titulo": "Lector de texto",
        "categoria": "Lectura",
        "descripcion": "Herramienta para trabajar con contenido textual mediante lectura por audio.",
        "url": "https://e2vymapp8w22ojrpsuvqc2e.streamlit.app/",
        "imagen": "imagenes/app_04.png",
    },
    {
        "numero": "05",
        "titulo": "OCR · Texto a audio",
        "categoria": "OCR",
        "descripcion": "Extrae texto desde imágenes y permite convertir el contenido en audio.",
        "url": "https://ocr-audio-ybjvud89srveyxujheuglj.streamlit.app/",
        "imagen": "imagenes/app_05.png",
    },
    {
        "numero": "06",
        "titulo": "Análisis de sentimientos",
        "categoria": "Texto",
        "descripcion": "Analiza contenido escrito para identificar el sentimiento presente en el texto.",
        "url": "https://sentimenta-yvw8kjjhc3k5ahfm2bvbbk.streamlit.app/",
        "imagen": "imagenes/app_06.png",
    },
    {
        "numero": "07",
        "titulo": "Nube de palabras",
        "categoria": "NLP",
        "descripcion": "Genera una representación visual de las palabras más relevantes de un texto.",
        "url": "https://wordcloud-twmeornb88bu5daiohmzth.streamlit.app/",
        "imagen": "imagenes/app_07.png",
    },
    {
        "numero": "08",
        "titulo": "TF-IDF",
        "categoria": "NLP",
        "descripcion": "Compara documentos y preguntas mediante TF-IDF y similitud de coseno.",
        "url": "https://tdfesp-mmsucjw6w26aff34fpsenn.streamlit.app/",
        "imagen": "imagenes/app_08.png",
    },
    {
        "numero": "09",
        "titulo": "Detector de objetos",
        "categoria": "Visión",
        "descripcion": "Detecta objetos presentes en imágenes mediante visión por computador.",
        "url": "https://yolov5-3qhk7h6k3kr9tjfgepuekf.streamlit.app/",
        "imagen": "imagenes/app_09.png",
    },
    {
        "numero": "10",
        "titulo": "Detector de emociones",
        "categoria": "Visión",
        "descripcion": "Analiza imágenes para identificar expresiones y emociones.",
        "url": "https://zb8fhzc4q6vjd726eqkviy.streamlit.app/",
        "imagen": "imagenes/app_10.png",
    },
]


# ============================================================
# TARJETAS 3 POR FILA
# ============================================================

for inicio in range(0, len(apps), 3):

    columnas = st.columns(3, gap="medium")

    for columna, app in zip(
        columnas,
        apps[inicio:inicio + 3]
    ):

        with columna:

            with st.container(border=True):

                if os.path.exists(app["imagen"]):

                    st.image(
                        app["imagen"],
                        use_container_width=True
                    )

                else:

                    st.error(
                        f"No se encontró {app['imagen']}"
                    )

                st.markdown(
                    f"""
<div class="app-meta">
    <div class="app-number">APP {app["numero"]}</div>
    <div class="app-category">{app["categoria"]}</div>
</div>
""",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="app-title">{app["titulo"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="app-description">{app["descripcion"]}</div>',
                    unsafe_allow_html=True
                )

                st.link_button(
                    "ABRIR APLICACIÓN ↗",
                    app["url"],
                    use_container_width=True
                )


# ============================================================
# PIE
# ============================================================

st.markdown(
    """
<div class="footer-box">
    <div class="footer-title">✦ Belen Cajahuaman</div>
    <div class="footer-text">
        Portafolio de aplicaciones de Inteligencia Artificial.
    </div>
</div>
""",
    unsafe_allow_html=True,
)
