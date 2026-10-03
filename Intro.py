import os
import streamlit as st
from PIL import Image


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# ESTILO — inspirado en la referencia
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --bg: #e9eaf0;
        --panel: #f6f6f8;
        --white: #ffffff;
        --ink: #1b1a23;
        --muted: #686b76;
        --blue: #4158e8;
        --blue-dark: #2936b5;
        --lime: #b7ff18;
        --lime-soft: #ddff7a;
        --purple: #7168ff;
        --orange: #ff7435;
        --line: #d7d9e1;
    }

    html, body, [class*="css"] {
        font-family: "DM Sans", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 90% 0%, rgba(113,104,255,.10), transparent 25%),
            radial-gradient(circle at 0% 10%, rgba(183,255,24,.08), transparent 20%),
            var(--bg);
        color: var(--ink);
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1400px !important;
        padding-top: 1.4rem !important;
        padding-bottom: 3rem !important;
    }

    h1, h2, h3, h4 {
        font-family: "Space Grotesk", sans-serif !important;
        color: var(--ink) !important;
        letter-spacing: -0.8px !important;
    }

    p {
        color: #4e505b !important;
    }

    /* ---------- ENCABEZADO ---------- */

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 18px;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-mark {
        width: 46px;
        height: 46px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: var(--lime);
        color: var(--blue-dark);
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.35rem;
        font-weight: 700;
        box-shadow: 4px 4px 0 rgba(41,54,181,.15);
    }

    .brand-name {
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        line-height: 1;
    }

    .brand-sub {
        color: #7a7c86;
        font-size: .74rem;
        margin-top: 5px;
    }

    .top-tag {
        padding: 9px 14px;
        border: 1px solid #cfd2dc;
        background: rgba(255,255,255,.55);
        border-radius: 999px;
        color: #474956;
        font-size: .75rem;
        font-weight: 700;
    }

    /* ---------- HERO ---------- */

    .hero {
        position: relative;
        overflow: hidden;
        min-height: 220px;
        padding: 34px 38px;
        border-radius: 26px;
        margin-bottom: 26px;

        background:
            radial-gradient(circle at 88% 12%, rgba(255,255,255,.28), transparent 22%),
            linear-gradient(135deg, #edf2ff 0%, #f8f8fb 100%);

        border: 1px solid #d6d8e1;
        box-shadow: 0 12px 32px rgba(40,43,60,.08);
    }

    .hero:before {
        content: "";
        position: absolute;
        width: 360px;
        height: 220px;
        right: -80px;
        top: -95px;
        border-radius: 50%;
        background: var(--lime);
        transform: rotate(-10deg);
        opacity: .95;
    }

    .hero:after {
        content: "";
        position: absolute;
        width: 240px;
        height: 90px;
        right: 80px;
        bottom: -40px;
        border-radius: 50%;
        background: var(--blue);
        transform: rotate(-14deg);
        opacity: .90;
    }

    .hero-inner {
        position: relative;
        z-index: 2;
        max-width: 760px;
    }

    .hero-kicker {
        color: var(--blue-dark);
        font-size: .78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.3px;
    }

    .hero-title {
        margin-top: 8px;
        color: var(--ink);
        font-family: "Space Grotesk", sans-serif;
        font-size: clamp(2.1rem, 4vw, 4.2rem);
        font-weight: 700;
        line-height: .96;
        letter-spacing: -2.5px;
    }

    .hero-title span {
        color: var(--blue);
    }

    .hero-copy {
        max-width: 680px;
        margin-top: 16px;
        color: #575965;
        font-size: .95rem;
        line-height: 1.55;
    }

    .hero-pill {
        display: inline-block;
        margin-top: 17px;
        padding: 8px 13px;
        border-radius: 999px;
        background: var(--lime);
        color: #263016;
        font-size: .72rem;
        font-weight: 700;
    }

    /* ---------- SIDEBAR ---------- */

    [data-testid="stSidebar"] {
        background: #1f2028 !important;
        border-right: 0 !important;
    }

    [data-testid="stSidebar"] * {
        color: #f4f4f7 !important;
    }

    .side-title {
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .side-box {
        padding: 15px;
        margin: 10px 0 14px;
        border-radius: 18px;
        background: #292b35;
        border: 1px solid #3c3e49;
    }

    .side-label {
        color: var(--lime);
        font-size: .68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 7px;
    }

    .side-copy {
        color: #d9dae1 !important;
        font-size: .84rem;
        line-height: 1.55;
    }

    /* ---------- SECCIÓN ---------- */

    .section-heading {
        display: flex;
        align-items: end;
        justify-content: space-between;
        gap: 15px;
        margin: 4px 0 14px;
    }

    .section-title {
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
    }

    .section-note {
        color: #777984;
        font-size: .75rem;
        font-weight: 600;
    }

    /* ---------- TARJETAS ---------- */

    .app-card {
        background: var(--white);
        border: 1px solid #d8dae2;
        border-radius: 20px;
        padding: 12px;
        margin-bottom: 22px;
        box-shadow: 0 8px 20px rgba(34,36,49,.07);
        transition: transform .18s ease, box-shadow .18s ease;
    }

    .app-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 28px rgba(34,36,49,.11);
    }

    .thumb {
        position: relative;
        height: 170px;
        border-radius: 14px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 15px;
        background:
            linear-gradient(135deg, var(--blue) 0%, #7c78ff 100%);
        color: white;
    }

    .thumb:after {
        content: "";
        position: absolute;
        width: 110px;
        height: 110px;
        right: -35px;
        bottom: -40px;
        border-radius: 50%;
        background: rgba(183,255,24,.95);
    }

    .thumb-number {
        position: relative;
        z-index: 2;
        font-family: "Space Grotesk", sans-serif;
        font-size: .72rem;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .thumb-icon {
        position: relative;
        z-index: 2;
        font-size: 2.7rem;
        line-height: 1;
    }

    .thumb-word {
        position: relative;
        z-index: 2;
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        max-width: 80%;
    }

    .card-meta {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 12px;
        gap: 10px;
    }

    .card-number {
        padding: 5px 8px;
        border-radius: 8px;
        background: #eff1ff;
        color: var(--blue-dark);
        font-size: .68rem;
        font-weight: 700;
    }

    .card-type {
        color: #9698a2;
        font-size: .68rem;
        font-weight: 700;
        text-transform: uppercase;
    }

    .card-title {
        margin-top: 9px;
        color: var(--ink);
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.12rem;
        font-weight: 700;
        line-height: 1.1;
    }

    .card-copy {
        min-height: 47px;
        margin-top: 7px;
        color: #6e707b;
        font-size: .78rem;
        line-height: 1.45;
    }

    .card-link {
        display: inline-block;
        margin-top: 11px;
        padding: 8px 11px;
        border-radius: 999px;
        background: #181922;
        color: white !important;
        text-decoration: none !important;
        font-size: .71rem;
        font-weight: 700;
    }

    .card-link:hover {
        background: var(--blue);
    }

    /* ---------- PIE ---------- */

    .footer-card {
        margin-top: 18px;
        padding: 20px 22px;
        border-radius: 20px;
        background: #1f2028;
        color: white;
    }

    .footer-title {
        font-family: "Space Grotesk", sans-serif;
        font-size: 1rem;
        font-weight: 700;
    }

    .footer-copy {
        margin-top: 4px;
        color: #c9cad1;
        font-size: .8rem;
    }

    @media (max-width: 700px) {
        .hero {
            padding: 25px 22px;
        }

        .hero-title {
            letter-spacing: -1.5px;
        }

        .thumb {
            height: 150px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div class="side-title">
            Aplicaciones con Inteligencia Artificial
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="side-box">
            <div class="side-label">Colección</div>
            <div class="side-copy">
                Explora herramientas y ejercicios prácticos
                relacionados con texto, voz, imágenes y
                análisis de datos mediante Inteligencia Artificial.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="side-box">
            <div class="side-label">Contenido</div>
            <div class="side-copy">
                10 aplicaciones disponibles para consultar,
                probar y explorar.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="side-box">
            <div class="side-label">Temas</div>
            <div class="side-copy">
                Voz · Texto · OCR · Sentimientos ·
                Imágenes · TF-IDF · Visión
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="topbar">
        <div class="brand">
            <div class="brand-mark">✦</div>
            <div>
                <div class="brand-name">Aplicaciones de IA</div>
                <div class="brand-sub">
                    Laboratorio de herramientas y ejercicios prácticos
                </div>
            </div>
        </div>

        <div class="top-tag">10 aplicaciones</div>
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
        <div class="hero-inner">
            <div class="hero-kicker">
                Inteligencia Artificial · Colección
            </div>

            <div class="hero-title">
                Explora <span>nuevas herramientas</span>
                de Inteligencia Artificial.
            </div>

            <div class="hero-copy">
                Accede a cada aplicación desde esta colección:
                conversión de voz y texto, OCR, análisis de sentimientos,
                nube de palabras, TF-IDF y visión por computador.
            </div>

            <div class="hero-pill">
                ✦ Explora · Prueba · Aprende
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# TÍTULO DE SECCIÓN
# ============================================================

st.markdown(
    """
    <div class="section-heading">
        <div class="section-title">Aplicaciones</div>
        <div class="section-note">Selecciona una para abrirla</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DATOS DE LAS NUEVAS APLICACIONES
# ============================================================

apps = [
    {
        "numero": "01",
        "titulo": "Mi primera App",
        "descripcion": "Primera aplicación desarrollada para explorar el uso práctico de la Inteligencia Artificial.",
        "url": "https://clase6-mwpnbk3fsbkennu2xxv2rr.streamlit.app/",
        "icono": "✦",
        "categoria": "Inicio",
    },
    {
        "numero": "02",
        "titulo": "Texto a voz",
        "descripcion": "Convierte contenido escrito en audio mediante una aplicación de síntesis de voz.",
        "url": "https://s273ggysgxrvjc5xqcjjih.streamlit.app/",
        "icono": "◖",
        "categoria": "Voz",
    },
    {
        "numero": "03",
        "titulo": "Voz a texto",
        "descripcion": "Transcribe una entrada de voz y la transforma en texto.",
        "url": "https://traductor-7ggtnhxykyspqhtk6cypby.streamlit.app/",
        "icono": "◉",
        "categoria": "Audio",
    },
    {
        "numero": "04",
        "titulo": "Lector de texto",
        "descripcion": "Herramienta orientada a la lectura de contenido textual mediante audio.",
        "url": "https://e2vymapp8w22ojrpsuvqc2e.streamlit.app/",
        "icono": "◌",
        "categoria": "Lectura",
    },
    {
        "numero": "05",
        "titulo": "OCR · Texto a audio",
        "descripcion": "Extrae texto desde imágenes y permite transformarlo en audio.",
        "url": "https://ocr-audio-ybjvud89srveyxujheuglj.streamlit.app/",
        "icono": "▣",
        "categoria": "OCR",
    },
    {
        "numero": "06",
        "titulo": "Análisis de sentimientos",
        "descripcion": "Analiza textos para identificar el sentimiento presente en el contenido.",
        "url": "https://sentimenta-yvw8kjjhc3k5ahfm2bvbbk.streamlit.app/",
        "icono": "☺",
        "categoria": "Texto",
    },
    {
        "numero": "07",
        "titulo": "Nube de palabras",
        "descripcion": "Genera una representación visual de las palabras más relevantes de un texto.",
        "url": "https://wordcloud-twmeornb88bu5daiohmzth.streamlit.app/",
        "icono": "✧",
        "categoria": "Texto",
    },
    {
        "numero": "08",
        "titulo": "TF-IDF",
        "descripcion": "Compara documentos y preguntas utilizando TF-IDF y similitud de coseno.",
        "url": "https://tdfesp-mmsucjw6w26aff34fpsenn.streamlit.app/",
        "icono": "01",
        "categoria": "NLP",
    },
    {
        "numero": "09",
        "titulo": "Detector de objetos",
        "descripcion": "Detecta objetos presentes en imágenes utilizando visión por computador.",
        "url": "https://yolov5-3qhk7h6k3kr9tjfgepuekf.streamlit.app/",
        "icono": "◎",
        "categoria": "Visión",
    },
    {
        "numero": "10",
        "titulo": "Detector de emociones",
        "descripcion": "Analiza imágenes para detectar expresiones y emociones.",
        "url": "https://zb8fhzc4q6vjd726eqkviy.streamlit.app/",
        "icono": "★",
        "categoria": "Visión",
    },
]


# ============================================================
# TARJETAS
# ============================================================

columns = st.columns(3, gap="medium")

for index, app in enumerate(apps):
    with columns[index % 3]:

        st.markdown(
            f"""
            <div class="app-card">

                <div class="thumb">
                    <div class="thumb-number">
                        APP {app["numero"]}
                    </div>

                    <div class="thumb-icon">
                        {app["icono"]}
                    </div>

                    <div class="thumb-word">
                        {app["titulo"]}
                    </div>
                </div>

                <div class="card-meta">
                    <div class="card-number">
                        {app["numero"]}
                    </div>

                    <div class="card-type">
                        {app["categoria"]}
                    </div>
                </div>

                <div class="card-title">
                    {app["titulo"]}
                </div>

                <div class="card-copy">
                    {app["descripcion"]}
                </div>

                <a
                    class="card-link"
                    href="{app["url"]}"
                    target="_blank"
                >
                    ABRIR APLICACIÓN ↗
                </a>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# PIE
# ============================================================

st.markdown(
    """
    <div class="footer-card">
        <div class="footer-title">
            ✦ Laboratorio de Inteligencia Artificial
        </div>
        <div class="footer-copy">
            Una colección de aplicaciones y ejercicios prácticos
            para explorar diferentes usos de la Inteligencia Artificial.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
