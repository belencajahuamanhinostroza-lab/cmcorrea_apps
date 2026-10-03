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

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 8% 8%, rgba(255, 185, 213, .18), transparent 24%),
        radial-gradient(circle at 92% 10%, rgba(190, 187, 255, .16), transparent 24%),
        radial-gradient(circle at 75% 88%, rgba(211, 255, 175, .14), transparent 22%),
        #f5f3f6;
    color: #19191f;
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
    background: #19191f;
    margin-bottom: 10px;
}

.top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 4px 2px 18px;
    color: #75727a;
    font-size: .7rem;
    font-weight: 500;
    letter-spacing: .9px;
    text-transform: uppercase;
}

.top-nav .brand {
    color: #55505a;
    font-family: "Space Grotesk", sans-serif;
    font-size: .9rem;
    font-weight: 600;
    letter-spacing: .2px;
}

/* ============================================================
   HERO — PASTEL + TRANSPARENCIA
   ============================================================ */

.hero {
    position: relative;
    overflow: hidden;
    min-height: 420px;
    padding: 54px 52px;
    margin-bottom: 34px;

    background:
        linear-gradient(
            135deg,
            rgba(255, 220, 232, .80) 0%,
            rgba(224, 220, 255, .76) 48%,
            rgba(222, 250, 190, .72) 100%
        );

    border: 1px solid rgba(255,255,255,.68);
    box-shadow:
        0 18px 42px rgba(56, 48, 65, .09),
        inset 0 1px 0 rgba(255,255,255,.75);

    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
}

.hero:before {
    content: "";
    position: absolute;
    width: 390px;
    height: 220px;
    right: -85px;
    top: -68px;
    background: rgba(169, 179, 255, .50);
    transform: rotate(-10deg);
    border-radius: 42% 58% 40% 60%;
}

.hero:after {
    content: "";
    position: absolute;
    width: 260px;
    height: 150px;
    right: 75px;
    bottom: -58px;
    background: rgba(255, 177, 212, .56);
    transform: rotate(-12deg);
    border-radius: 50%;
}

.hero-content {
    position: relative;
    z-index: 4;
    max-width: 820px;
}

.hero-small {
    color: #66616b;
    font-size: .72rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    margin-bottom: 12px;
}

.hero-name {
    font-family: "DM Sans", sans-serif;
    font-size: 1.05rem;
    font-weight: 400;
    color: #5f5a63;
    margin-bottom: 8px;
}

.hero-title {
    font-family: "Space Grotesk", sans-serif;
    font-size: clamp(3.3rem, 8vw, 6.7rem);
    font-weight: 500;
    line-height: .90;
    letter-spacing: -4px;
    color: #19191f;
}

.hero-title span {
    background:
        linear-gradient(
            90deg,
            #d95d7f,
            #877be5,
            #6ea45d
        );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    margin-top: 12px;
    font-family: "Space Grotesk", sans-serif;
    font-size: 1.15rem;
    font-weight: 400;
    color: #48434d;
}

.hero-copy {
    max-width: 670px;
    margin-top: 17px;
    color: #68636c;
    font-size: .88rem;
    font-weight: 400;
    line-height: 1.6;
}

.hero-tag {
    display: inline-block;
    margin-top: 20px;
    padding: 8px 13px;
    background: rgba(255,255,255,.48);
    border: 1px solid rgba(255,255,255,.7);
    color: #504c55;
    font-size: .66rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .8px;
}

/* ============================================================
   SECCIÓN
   ============================================================ */

.section-title {
    font-family: "Space Grotesk", sans-serif;
    font-size: 1.8rem;
    font-weight: 500;
    letter-spacing: -1px;
    color: #1b1b21;
    margin-bottom: 3px;
}

.section-subtitle {
    color: #79747d;
    font-size: .78rem;
    font-weight: 400;
    margin-bottom: 18px;
}

/* ============================================================
   TARJETAS
   ============================================================ */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,.88) !important;
    border: 1px solid rgba(214,210,220,.9) !important;
    border-radius: 6px !important;
    box-shadow: 0 10px 25px rgba(35, 30, 42, .06) !important;
    padding: 10px !important;
    margin-bottom: 24px !important;
}

[data-testid="stImage"] img {
    border-radius: 3px !important;
}

.app-meta {
    margin-top: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.app-number {
    color: #7770d7;
    font-size: .64rem;
    font-weight: 600;
    letter-spacing: .8px;
}

.app-category {
    color: #9b969e;
    font-size: .6rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: .7px;
}

.app-title {
    margin-top: 7px;
    font-family: "Space Grotesk", sans-serif;
    font-size: 1.08rem;
    font-weight: 500;
    line-height: 1.12;
    color: #24232a;
}

.app-description {
    min-height: 52px;
    margin-top: 7px;
    color: #77727b;
    font-size: .74rem;
    font-weight: 400;
    line-height: 1.5;
}

div.stLinkButton > a {
    width: 100% !important;
    background: #25232b !important;
    border: none !important;
    border-radius: 3px !important;
    color: white !important;
    font-family: "DM Sans", sans-serif !important;
    font-size: .64rem !important;
    font-weight: 600 !important;
    letter-spacing: .6px !important;
    text-transform: uppercase !important;
}

div.stLinkButton > a:hover {
    background: #7770d7 !important;
    color: white !important;
}

/* ============================================================
   PIE
   ============================================================ */

.footer-box {
    margin-top: 10px;
    padding: 22px 24px;
    background:
        linear-gradient(
            135deg,
            rgba(219, 214, 255, .82),
            rgba(255, 219, 232, .82),
            rgba(221, 249, 198, .78)
        );
    border: 1px solid rgba(255,255,255,.7);
    color: #292731;
}

.footer-title {
    font-family: "Space Grotesk", sans-serif;
    font-size: 1rem;
    font-weight: 500;
}

.footer-text {
    margin-top: 4px;
    color: #716c75;
    font-size: .74rem;
}

@media (max-width: 700px) {

    .hero {
        min-height: 360px;
        padding: 34px 25px;
    }

    .hero-title {
        letter-spacing: -2.5px;
    }

    .hero:before {
        width: 250px;
        right: -80px;
    }

    .hero:after {
        width: 180px;
        right: 20px;
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
    <div>PORTAFOLIO 2026 · INTERFACES MULTIMODALES</div>
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

    <div class="hero-content">

        <div class="hero-small">
            Portafolio académico · 2026
        </div>

        <div class="hero-name">
            Belen Cajahuaman
        </div>

        <div class="hero-title">
            Mi <span>Portafolio</span>
        </div>

        <div class="hero-subtitle">
            Interfaces Multimodales
        </div>

        <div class="hero-copy">
            Colección de aplicaciones y proyectos desarrollados
            durante 2026 para explorar la interacción entre texto,
            voz, imagen y diferentes tecnologías de Inteligencia Artificial.
        </div>

        <div class="hero-tag">
            2026 · Interfaces Multimodales · 10 aplicaciones
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

                    st.warning(
                        f"No se encontró la imagen: {app['imagen']}"
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

    <div class="footer-title">
        ✦ Belen Cajahuaman · Portafolio 2026
    </div>

    <div class="footer-text">
        Interfaces Multimodales · Aplicaciones de Inteligencia Artificial
    </div>

</div>
""",
    unsafe_allow_html=True,
)
