import os
import streamlit as st


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Mi Portafolio - Belen Cajahuaman",
    page_icon="✦",
    layout="wide",
)


# ============================================================
# ESTILOS
# ============================================================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap'
    );

    html, body, [class*="css"] {
        font-family: "DM Sans", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 10% 5%,
                rgba(63,82,229,.10),
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 80%,
                rgba(186,255,25,.08),
                transparent 25%
            ),
            #eef0f4;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    #MainMenu,
    footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1250px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 3rem !important;
    }


    /* ========================================================
       CABECERA
       ======================================================== */

    .nombre-superior {
        font-family: "Space Grotesk", sans-serif;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 0.8px;
        color: #20222c;
        margin-bottom: 20px;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero-box {
        position: relative;
        overflow: hidden;

        background: #f8f8f8;

        border: 1px solid #d7d9df;

        padding: 48px;

        min-height: 330px;

        box-shadow:
            0 15px 35px rgba(30, 35, 50, 0.08);

        margin-bottom: 35px;
    }

    .hero-box:before {
        content: "";

        position: absolute;

        width: 390px;
        height: 210px;

        right: -90px;
        top: -65px;

        background: #4155df;

        transform: rotate(-10deg);
    }

    .hero-box:after {
        content: "";

        position: absolute;

        width: 240px;
        height: 120px;

        right: 80px;
        bottom: -50px;

        background: #baff19;

        transform: rotate(-12deg);
    }

    .hero-contenido {
        position: relative;
        z-index: 2;
    }

    .hero-pequeno {
        color: #4155df;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.4px;
    }

    .hero-titulo {
        margin-top: 10px;

        font-family: "Space Grotesk", sans-serif;

        font-size: clamp(3.3rem, 8vw, 6.8rem);

        line-height: 0.86;

        letter-spacing: -5px;

        font-weight: 700;

        color: #181a22;
    }

    .hero-titulo span {
        color: #e55b4a;
    }

    .hero-nombre {
        margin-top: 24px;

        font-family: "Space Grotesk", sans-serif;

        font-size: 1.35rem;

        font-weight: 700;

        color: #32343e;
    }

    .hero-texto {
        max-width: 650px;

        margin-top: 9px;

        color: #6c6e78;

        font-size: 0.92rem;

        line-height: 1.55;
    }

    .hero-etiqueta {
        display: inline-block;

        margin-top: 18px;

        padding: 8px 13px;

        background: #baff19;

        color: #293018;

        font-size: 0.68rem;

        font-weight: 700;

        text-transform: uppercase;

        letter-spacing: 0.8px;
    }


    /* ========================================================
       TÍTULO SECCIÓN
       ======================================================== */

    .seccion-titulo {
        font-family: "Space Grotesk", sans-serif;

        font-size: 1.7rem;

        font-weight: 700;

        color: #1d1e27;

        margin-bottom: 4px;
    }

    .seccion-subtitulo {
        color: #777983;

        font-size: 0.78rem;

        margin-bottom: 18px;
    }


    /* ========================================================
       TARJETAS STREAMLIT
       ======================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;

        border: 1px solid #d8dae0 !important;

        border-radius: 4px !important;

        padding: 10px !important;

        box-shadow:
            0 8px 22px rgba(33, 36, 49, 0.07) !important;

        margin-bottom: 22px !important;
    }


    /* ========================================================
       IMÁGENES
       ======================================================== */

    [data-testid="stImage"] img {
        border-radius: 2px !important;
    }


    /* ========================================================
       TEXTO DE LAS TARJETAS
       ======================================================== */

    .numero-app {
        color: #4155df;

        font-size: 0.65rem;

        font-weight: 700;

        letter-spacing: 1px;

        margin-top: 9px;
    }

    .categoria-app {
        color: #999ba3;

        font-size: 0.63rem;

        font-weight: 700;

        text-transform: uppercase;

        letter-spacing: 0.8px;

        float: right;

        margin-top: -14px;
    }

    .titulo-app {
        font-family: "Space Grotesk", sans-serif;

        color: #181a22;

        font-size: 1.15rem;

        font-weight: 700;

        line-height: 1.1;

        margin-top: 8px;
    }

    .descripcion-app {
        color: #6f717a;

        font-size: 0.76rem;

        line-height: 1.5;

        min-height: 48px;

        margin-top: 7px;

        margin-bottom: 12px;
    }


    /* ========================================================
       BOTONES
       ======================================================== */

    div.stLinkButton > a {
        width: 100% !important;

        border-radius: 2px !important;

        background: #191a21 !important;

        border: none !important;

        color: white !important;

        font-family: "Space Grotesk", sans-serif !important;

        font-size: 0.68rem !important;

        font-weight: 700 !important;

        letter-spacing: 0.5px;

        text-transform: uppercase;

        text-align: center !important;
    }

    div.stLinkButton > a:hover {
        background: #4155df !important;

        color: white !important;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .pie {
        background: #191a21;

        padding: 22px;

        margin-top: 20px;

        color: white;
    }

    .pie-titulo {
        font-family: "Space Grotesk", sans-serif;

        font-size: 1rem;

        font-weight: 700;
    }

    .pie-texto {
        color: #c6c7ce;

        font-size: 0.75rem;

        margin-top: 5px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# CABECERA
# ============================================================

st.markdown(
    '<div class="nombre-superior">✦ BELEN CAJAHUAMAN</div>',
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero-box">

        <div class="hero-contenido">

            <div class="hero-pequeno">
                Portafolio personal
            </div>

            <div class="hero-titulo">
                Mi <span>Portafolio</span>
            </div>

            <div class="hero-nombre">
                Belen Cajahuaman
            </div>

            <div class="hero-texto">
                Una colección de aplicaciones y proyectos
                prácticos desarrollados para explorar diferentes
                usos de la Inteligencia Artificial.
            </div>

            <div class="hero-etiqueta">
                10 aplicaciones · Inteligencia Artificial
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SECCIÓN
# ============================================================

st.markdown(
    '<div class="seccion-titulo">Mis aplicaciones</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="seccion-subtitulo">Explora cada proyecto y abre la aplicación.</div>',
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
        "descripcion": (
            "Primera aplicación del portafolio para "
            "explorar de forma práctica el uso de "
            "Inteligencia Artificial."
        ),
        "url": (
            "https://clase6-mwpnbk3fsbkennu2xxv2rr.streamlit.app/"
        ),
        "imagen": "imagenes/app_01.png",
    },

    {
        "numero": "02",
        "titulo": "Texto a voz",
        "categoria": "Voz",
        "descripcion": (
            "Convierte contenido escrito en audio "
            "mediante una aplicación de síntesis de voz."
        ),
        "url": (
            "https://s273ggysgxrvjc5xqcjjih.streamlit.app/"
        ),
        "imagen": "imagenes/app_02.png",
    },

    {
        "numero": "03",
        "titulo": "Voz a texto",
        "categoria": "Audio",
        "descripcion": (
            "Transforma una entrada de voz en texto "
            "para facilitar la transcripción."
        ),
        "url": (
            "https://traductor-7ggtnhxykyspqhtk6cypby.streamlit.app/"
        ),
        "imagen": "imagenes/app_03.png",
    },

    {
        "numero": "04",
        "titulo": "Lector de texto",
        "categoria": "Lectura",
        "descripcion": (
            "Herramienta para trabajar con contenido "
            "textual mediante lectura por audio."
        ),
        "url": (
            "https://e2vymapp8w22ojrpsuvqc2e.streamlit.app/"
        ),
        "imagen": "imagenes/app_04.png",
    },

    {
        "numero": "05",
        "titulo": "OCR · Texto a audio",
        "categoria": "OCR",
        "descripcion": (
            "Extrae texto desde imágenes y permite "
            "convertir el contenido en audio."
        ),
        "url": (
            "https://ocr-audio-ybjvud89srveyxujheuglj.streamlit.app/"
        ),
        "imagen": "imagenes/app_05.png",
    },

    {
        "numero": "06",
        "titulo": "Análisis de sentimientos",
        "categoria": "Texto",
        "descripcion": (
            "Analiza contenido escrito para identificar "
            "el sentimiento presente en el texto."
        ),
        "url": (
            "https://sentimenta-yvw8kjjhc3k5ahfm2bvbbk.streamlit.app/"
        ),
        "imagen": "imagenes/app_06.png",
    },

    {
        "numero": "07",
        "titulo": "Nube de palabras",
        "categoria": "NLP",
        "descripcion": (
            "Genera una representación visual de las "
            "palabras más relevantes de un texto."
        ),
        "url": (
            "https://wordcloud-twmeornb88bu5daiohmzth.streamlit.app/"
        ),
        "imagen": "imagenes/app_07.png",
    },

    {
        "numero": "08",
        "titulo": "TF-IDF",
        "categoria": "NLP",
        "descripcion": (
            "Compara documentos y preguntas mediante "
            "TF-IDF y similitud de coseno."
        ),
        "url": (
            "https://tdfesp-mmsucjw6w26aff34fpsenn.streamlit.app/"
        ),
        "imagen": "imagenes/app_08.png",
    },

    {
        "numero": "09",
        "titulo": "Detector de objetos",
        "categoria": "Visión",
        "descripcion": (
            "Detecta objetos presentes en imágenes "
            "mediante visión por computador."
        ),
        "url": (
            "https://yolov5-3qhk7h6k3kr9tjfgepuekf.streamlit.app/"
        ),
        "imagen": "imagenes/app_09.png",
    },

    {
        "numero": "10",
        "titulo": "Detector de emociones",
        "categoria": "Visión",
        "descripcion": (
            "Analiza imágenes para identificar "
            "expresiones y emociones."
        ),
        "url": (
            "https://zb8fhzc4q6vjd726eqkviy.streamlit.app/"
        ),
        "imagen": "imagenes/app_10.png",
    },

]


# ============================================================
# TARJETAS — 3 POR FILA
# ============================================================

for inicio in range(0, len(apps), 3):

    columnas = st.columns(3, gap="medium")

    grupo = apps[inicio:inicio + 3]

    for columna, app in zip(columnas, grupo):

        with columna:

            # Contenedor nativo de Streamlit
            with st.container(border=True):

                # Imagen
                if os.path.exists(app["imagen"]):

                    st.image(
                        app["imagen"],
                        use_container_width=True
                    )

                else:

                    st.warning(
                        f"No se encontró la imagen: {app['imagen']}"
                    )


                # Número
                st.markdown(
                    f"""
                    <div class="numero-app">
                        APP {app["numero"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                # Categoría
                st.markdown(
                    f"""
                    <div class="categoria-app">
                        {app["categoria"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                # Título
                st.markdown(
                    f"""
                    <div class="titulo-app">
                        {app["titulo"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                # Descripción
                st.markdown(
                    f"""
                    <div class="descripcion-app">
                        {app["descripcion"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                # BOTÓN NATIVO
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
    <div class="pie">

        <div class="pie-titulo">
            ✦ Belen Cajahuaman
        </div>

        <div class="pie-texto">
            Portafolio de aplicaciones de Inteligencia Artificial.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)
