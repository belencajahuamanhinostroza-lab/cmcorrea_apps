import os
import streamlit as st


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Portafolio 2026 | Belen Cajahuaman",
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

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Space+Grotesk:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 8% 4%, rgba(255, 198, 220, .32), transparent 25%),
        radial-gradient(circle at 92% 10%, rgba(200, 197, 255, .28), transparent 25%),
        radial-gradient(circle at 76% 92%, rgba(220, 250, 183, .23), transparent 25%),
        #f4f2f5;
    color: #1d1d22;
}

#MainMenu,
footer {
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


/* ============================================================
   BARRA SUPERIOR
   ============================================================ */

.top-line {
    width: 100%;
    height: 3px;
    background: #1d1d22;
    margin-bottom: 10px;
}

.top-nav {
    padding: 4px 2px 18px;
    color: #817c84;
    font-size: .68rem;
    font-weight: 500;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.brand-text {
    color: #58535c !important;
    font-family: "Space Grotesk", sans-serif;
    font-size: .86rem;
    font-weight: 500;
}


/* ============================================================
   HERO
   ============================================================ */

.st-key-hero {
    position: relative;
    overflow: hidden;
    min-height: 390px;

    padding: 48px 50px;

    border: 1px solid rgba(255,255,255,.82) !important;

    background:
        radial-gradient(
            circle at 88% 14%,
            rgba(255,255,255,.62),
            transparent 17%
        ),
        linear-gradient(
            115deg,
            rgba(255, 220, 232, .82) 0%,
            rgba(226, 221, 255, .80) 52%,
            rgba(224, 249, 190, .74) 100%
        ) !important;

    box-shadow:
        0 20px 45px rgba(51, 42, 59, .08),
        inset 0 1px 0 rgba(255,255,255,.9);

    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);

    margin-bottom: 34px;
}

.st-key-hero:before {
    content: "";
    position: absolute;
    width: 350px;
    height: 190px;
    top: -72px;
    right: -82px;
    background: rgba(166, 176, 255, .45);
    border-radius: 50%;
    transform: rotate(-12deg);
}

.st-key-hero:after {
    content: "";
    position: absolute;
    width: 240px;
    height: 135px;
    right: 85px;
    bottom: -55px;
    background: rgba(255, 176, 210, .48);
    border-radius: 50%;
    transform: rotate(-15deg);
}

.st-key-hero > div {
    position: relative;
    z-index: 5;
}

.st-key-hero h1 {
    font-family: "Space Grotesk", sans-serif !important;
    font-size: clamp(3.4rem, 7vw, 6.6rem) !important;
    font-weight: 500 !important;
    line-height: .9 !important;
    letter-spacing: -4px !important;
    color: #202026 !important;
    margin: 4px 0 0 0 !important;
}

.hero-small {
    color: #77717b !important;
    font-size: .72rem !important;
    font-weight: 500 !important;
    text-transform: uppercase;
    letter-spacing: 1.4px;
}

.hero-name {
    color: #5b5660 !important;
    font-family: "DM Sans", sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 400 !important;
    margin: 5px 0 0 0 !important;
}

.hero-subtitle {
    color: #55505a !important;
    font-family: "Space Grotesk", sans-serif !important;
    font-size: 1.12rem !important;
    font-weight: 400 !important;
    margin-top: 10px !important;
}

.hero-copy {
    max-width: 670px;
    color: #6c6670 !important;
    font-size: .87rem !important;
    font-weight: 400 !important;
    line-height: 1.6 !important;
}

.hero-tag {
    display: inline-block;
    padding: 7px 11px;
    margin-top: 10px;
    border: 1px solid rgba(255,255,255,.75);
    background: rgba(255,255,255,.42);
    color: #56515a !important;
    font-size: .63rem !important;
    font-weight: 600 !important;
    letter-spacing: .7px;
    text-transform: uppercase;
}


/* ============================================================
   SECCIÓN
   ============================================================ */

.section-title {
    font-family: "Space Grotesk", sans-serif !important;
    font-size: 1.75rem !important;
    font-weight: 500 !important;
    letter-spacing: -1px !important;
    color: #222229 !important;
    margin-bottom: 2px !important;
}

.section-subtitle {
    color: #7e7880 !important;
    font-size: .78rem !important;
    font-weight: 400 !important;
    margin-bottom: 18px !important;
}


/* ============================================================
   TARJETAS
   ============================================================ */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.96),
            rgba(252,250,253,.91)
        ) !important;

    border: 1px solid rgba(215,211,220,.88) !important;
    border-radius: 5px !important;

    box-shadow:
        0 9px 24px rgba(41, 34, 48, .06) !important;

    padding: 10px !important;
}

[data-testid="stImage"] img {
    border-radius: 3px !important;
}

.app-meta {
    margin-top: 10px;
}

.app-number {
    color: #7770d9 !important;
    font-size: .63rem !important;
    font-weight: 600 !important;
    letter-spacing: .7px;
}

.app-category {
    color: #9a969e !important;
    font-size: .60rem !important;
    font-weight: 500 !important;
    letter-spacing: .8px;
    text-transform: uppercase;
}

.app-title {
    color: #24232a !important;
    font-family: "Space Grotesk", sans-serif !important;
    font-size: 1.08rem !important;
    font-weight: 500 !important;
    line-height: 1.15 !important;
    margin-top: 6px !important;
}

.app-description {
    min-height: 50px;
    color: #747079 !important;
    font-size: .74rem !important;
    font-weight: 400 !important;
    line-height: 1.5 !important;
    margin-top: 6px !important;
}

div.stLinkButton > a {
    width: 100% !important;
    min-height: 40px !important;
    background: #242329 !important;
    border: 0 !important;
    border-radius: 3px !important;
    color: #ffffff !important;
    font-family: "DM Sans", sans-serif !important;
    font-size: .63rem !important;
    font-weight: 600 !important;
    letter-spacing: .6px !important;
    text-transform: uppercase !important;
}

div.stLinkButton > a:hover {
    background: #7770d9 !important;
    color: white !important;
}


/* ============================================================
   PIE
   ============================================================ */

.st-key-footer {
    margin-top: 14px;
    padding: 22px 24px;

    background:
        linear-gradient(
            110deg,
            rgba(222, 216, 255, .78),
            rgba(255, 216, 232, .75),
            rgba(225, 250, 198, .72)
        ) !important;

    border: 1px solid rgba(255,255,255,.75) !important;
    box-shadow: 0 10px 24px rgba(40, 32, 49, .06);
}

.st-key-footer .footer-title {
    font-family: "Space Grotesk", sans-serif;
    font-size: 1rem;
    font-weight: 500;
    color: #2a2830;
}

.st-key-footer .footer-text {
    margin-top: 4px;
    color: #746f77;
    font-size: .73rem;
}


@media (max-width: 700px) {

    .st-key-hero {
        min-height: 340px;
        padding: 32px 25px;
    }

    .st-key-hero h1 {
        font-size: 3.4rem !important;
        letter-spacing: -2.5px !important;
    }

    .st-key-hero:before {
        width: 260px;
    }

    .st-key-hero:after {
        width: 180px;
        right: 15px;
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
    '<div class="top-line"></div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="top-nav"><span class="brand-text">✦ BELEN CAJAHUAMAN</span> &nbsp;&nbsp; PORTAFOLIO 2026 · INTERFACES MULTIMODALES</div>',
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

with st.container(key="hero"):

    st.caption("PORTAFOLIO ACADÉMICO · 2026")

    st.markdown(
        '<div class="hero-name">Belen Cajahuaman</div>',
        unsafe_allow_html=True,
    )

    st.title("Mi Portafolio")

    st.markdown(
        '<div class="hero-subtitle">Interfaces Multimodales</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-copy">Colección de aplicaciones y proyectos desarrollados durante 2026 para explorar la interacción entre texto, voz, imagen y diferentes tecnologías de Inteligencia Artificial.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-tag">2026 · Interfaces Multimodales · 10 aplicaciones</div>',
        unsafe_allow_html=True,
    )


# ============================================================
# SECCIÓN
# ============================================================

st.markdown(
    '<div class="section-title">Mis aplicaciones</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">Proyectos desarrollados para Interfaces Multimodales durante 2026.</div>',
    unsafe_allow_html=True,
)


# ============================================================
# APLICACIONES
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
# TARJETAS — 3 POR FILA
# ============================================================

for inicio in range(0, len(apps), 3):

    columnas = st.columns(3, gap="medium")

    for columna, app_data in zip(
        columnas,
        apps[inicio:inicio + 3],
    ):

        with columna:

            with st.container(border=True):

                if os.path.exists(app_data["imagen"]):

                    st.image(
                        app_data["imagen"],
                        use_container_width=True,
                    )

                else:

                    st.warning(
                        f"No se encontró la imagen: {app_data['imagen']}"
                    )

                meta_col1, meta_col2 = st.columns(
                    [1, 1],
                    gap="small",
                )

                with meta_col1:
                    st.markdown(
                        f'<div class="app-number">APP {app_data["numero"]}</div>',
                        unsafe_allow_html=True,
                    )

                with meta_col2:
                    st.markdown(
                        f'<div class="app-category">{app_data["categoria"]}</div>',
                        unsafe_allow_html=True,
                    )

                st.markdown(
                    f'<div class="app-title">{app_data["titulo"]}</div>',
                    unsafe_allow_html=True,
                )

                st.markdown(
                    f'<div class="app-description">{app_data["descripcion"]}</div>',
                    unsafe_allow_html=True,
                )

                st.link_button(
                    "ABRIR APLICACIÓN ↗",
                    app_data["url"],
                    use_container_width=True,
                )


# ============================================================
# PIE
# ============================================================

with st.container(key="footer"):

    st.markdown(
        '<div class="footer-title">✦ Belen Cajahuaman · Portafolio 2026</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer-text">Interfaces Multimodales · Aplicaciones de Inteligencia Artificial</div>',
        unsafe_allow_html=True,
    )
