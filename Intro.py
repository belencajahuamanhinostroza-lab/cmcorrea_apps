import os
import base64
import streamlit as st


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Mi Portafolio — Belen Cajahuaman",
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

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap'
    );

    :root {
        --ink: #171820;
        --muted: #686b75;
        --blue: #3f52e5;
        --lime: #baff19;
        --cream: #f7f7f5;
        --line: #d8d9de;
        --white: #ffffff;
        --red: #e85b49;
    }

    html, body, [class*="css"] {
        font-family: "DM Sans", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 10% 5%,
                rgba(64,84,229,.09),
                transparent 23%
            ),
            radial-gradient(
                circle at 90% 70%,
                rgba(186,255,25,.07),
                transparent 22%
            ),
            #eef0f4;

        color: var(--ink);
    }

    #MainMenu,
    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    .block-container {
        max-width: 1280px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 3rem !important;
    }

    h1, h2, h3, h4 {
        font-family: "Space Grotesk", sans-serif !important;
        color: var(--ink) !important;
    }


    /* ========================================================
       CABECERA
       ======================================================== */

    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 4px 18px;
    }

    .nav-left {
        font-family: "Space Grotesk", sans-serif;
        font-weight: 700;
        font-size: .92rem;
    }

    .nav-right {
        color: #777984;
        font-size: .72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {
        position: relative;
        overflow: hidden;

        min-height: 345px;

        border-radius: 6px;

        padding: 42px 48px;

        background:
            linear-gradient(
                120deg,
                rgba(255,255,255,.96),
                rgba(244,245,249,.96)
            );

        border: 1px solid #d4d6dd;

        box-shadow:
            0 16px 35px rgba(33,37,52,.08);

        margin-bottom: 34px;
    }

    .hero:before {
        content: "";

        position: absolute;

        width: 370px;
        height: 210px;

        right: -75px;
        top: -75px;

        background: var(--blue);

        transform: rotate(-11deg);

        border-radius: 12px;
    }

    .hero:after {
        content: "";

        position: absolute;

        width: 250px;
        height: 125px;

        right: 95px;
        bottom: -48px;

        background: var(--lime);

        transform: rotate(-16deg);

        border-radius: 6px;
    }

    .hero-content {
        position: relative;
        z-index: 2;

        max-width: 780px;
    }

    .hero-kicker {
        font-size: .75rem;

        text-transform: uppercase;

        letter-spacing: 1.4px;

        font-weight: 700;

        color: var(--blue);

        margin-bottom: 10px;
    }

    .hero-title {
        font-family: "Space Grotesk", sans-serif;

        font-size: clamp(
            3.2rem,
            7vw,
            6.8rem
        );

        line-height: .86;

        letter-spacing: -5px;

        font-weight: 700;

        color: var(--ink);
    }

    .hero-title .red {
        color: var(--red);
    }

    .hero-name {
        margin-top: 20px;

        font-family: "Space Grotesk", sans-serif;

        font-size: 1.25rem;

        font-weight: 700;

        color: #32343e;
    }

    .hero-description {
        max-width: 650px;

        margin-top: 10px;

        color: #6e7079;

        font-size: .9rem;

        line-height: 1.55;
    }

    .hero-tag {
        display: inline-block;

        margin-top: 18px;

        padding: 8px 12px;

        background: var(--lime);

        color: #252b18;

        border-radius: 4px;

        font-size: .68rem;

        font-weight: 700;

        text-transform: uppercase;

        letter-spacing: .8px;
    }


    /* ========================================================
       SECCIÓN
       ======================================================== */

    .section-head {
        display: flex;

        justify-content: space-between;

        align-items: baseline;

        margin-bottom: 14px;
    }

    .section-title {
        font-family: "Space Grotesk", sans-serif;

        font-size: 1.55rem;

        font-weight: 700;

        letter-spacing: -1px;
    }

    .section-count {
        color: #858790;

        font-size: .72rem;

        font-weight: 700;

        text-transform: uppercase;

        letter-spacing: 1px;
    }


    /* ========================================================
       TARJETAS
       ======================================================== */

    .app-card {
        background: var(--white);

        border: 1px solid #d7d9df;

        padding: 9px 9px 15px;

        margin-bottom: 24px;

        box-shadow:
            0 9px 22px rgba(34,36,47,.07);

        transition:
            transform .18s ease,
            box-shadow .18s ease;
    }

    .app-card:hover {
        transform: translateY(-2px);

        box-shadow:
            0 14px 28px rgba(34,36,47,.11);
    }

    .app-image {
        width: 100%;

        aspect-ratio: 1.5 / 1;

        object-fit: cover;

        display: block;
    }

    .app-meta {
        display: flex;

        justify-content: space-between;

        align-items: center;

        margin:
            12px 5px 0;
    }

    .app-number {
        color: var(--blue);

        font-size: .68rem;

        font-weight: 700;

        letter-spacing: .7px;
    }

    .app-category {
        color: #999ba3;

        font-size: .63rem;

        font-weight: 700;

        letter-spacing: .8px;

        text-transform: uppercase;
    }

    .app-title {
        margin:
            7px 5px 0;

        color: var(--ink);

        font-family:
            "Space Grotesk",
            sans-serif;

        font-size: 1.12rem;

        font-weight: 700;

        line-height: 1.1;
    }

    .app-description {
        min-height: 48px;

        margin:
            7px 5px 0;

        color: #6f717b;

        font-size: .76rem;

        line-height: 1.48;
    }

    .open-wrap {
        margin:
            12px 5px 0;
    }

    .open-link {
        display: inline-block;

        padding:
            9px 12px;

        border-radius: 3px;

        background: var(--ink);

        color: white !important;

        text-decoration: none !important;

        font-size: .67rem;

        font-weight: 700;

        letter-spacing: .5px;

        text-transform: uppercase;

        transition: .15s ease;
    }

    .open-link:hover {
        background: var(--blue);

        transform: translateY(-1px);
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        margin-top: 16px;

        padding: 22px 24px;

        background: var(--ink);

        color: white;

        border-radius: 4px;
    }

    .footer-title {
        font-family:
            "Space Grotesk",
            sans-serif;

        font-size: 1rem;

        font-weight: 700;
    }

    .footer-copy {
        margin-top: 5px;

        color: #c7c8cf;

        font-size: .75rem;
    }


    /* ========================================================
       MÓVIL
       ======================================================== */

    @media (max-width: 700px) {

        .hero {
            padding: 30px 25px;

            min-height: 300px;
        }

        .hero-title {
            letter-spacing: -2.5px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FUNCIÓN PARA LAS IMÁGENES
# ============================================================

def imagen_base64(path):

    with open(path, "rb") as archivo:

        return base64.b64encode(
            archivo.read()
        ).decode("utf-8")


# ============================================================
# CABECERA
# ============================================================

st.markdown(
    """
    <div class="nav">

        <div class="nav-left">
            ✦ BELEN CAJAHUAMAN
        </div>

        <div class="nav-right">
            Portafolio · Inteligencia Artificial
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <section class="hero">

        <div class="hero-content">

            <div class="hero-kicker">
                Portafolio personal
            </div>

            <div class="hero-title">
                Mi <span class="red">Portafolio</span>
            </div>

            <div class="hero-name">
                Belen Cajahuaman
            </div>

            <div class="hero-description">
                Una colección de aplicaciones y proyectos
                prácticos desarrollados para explorar
                diferentes usos de la Inteligencia Artificial.
            </div>

            <div class="hero-tag">
                10 aplicaciones · 1 colección
            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# TÍTULO DE LAS APLICACIONES
# ============================================================

st.markdown(
    """
    <div class="section-head">

        <div class="section-title">
            Mis aplicaciones
        </div>

        <div class="section-count">
            01 — 10
        </div>

    </div>
    """,
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
        "descripcion": (
            "Primera aplicación del portafolio para "
            "explorar de forma práctica el uso de "
            "Inteligencia Artificial."
        ),
        "url": (
            "https://clase6-mwpnbk3fsbkennu2xxv2rr.streamlit.app/"
        ),
        "imagen": "app_01.png",
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
        "imagen": "app_02.png",
    },

    {
        "numero": "03",
        "titulo": "Voz a texto",
        "categoria": "Audio",
        "descripcion": (
            "Transforma una entrada de voz en texto "
            "para facilitar la transcripción y el procesamiento."
        ),
        "url": (
            "https://traductor-7ggtnhxykyspqhtk6cypby.streamlit.app/"
        ),
        "imagen": "app_03.png",
    },

    {
        "numero": "04",
        "titulo": "Lector de texto",
        "categoria": "Lectura",
        "descripcion": (
            "Herramienta enfocada en convertir contenido "
            "textual en una experiencia de lectura mediante audio."
        ),
        "url": (
            "https://e2vymapp8w22ojrpsuvqc2e.streamlit.app/"
        ),
        "imagen": "app_04.png",
    },

    {
        "numero": "05",
        "titulo": "OCR · Texto a audio",
        "categoria": "OCR",
        "descripcion": (
            "Extrae texto desde una imagen y permite "
            "llevar ese contenido a una salida de audio."
        ),
        "url": (
            "https://ocr-audio-ybjvud89srveyxujheuglj.streamlit.app/"
        ),
        "imagen": "app_05.png",
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
        "imagen": "app_06.png",
    },

    {
        "numero": "07",
        "titulo": "Nube de palabras",
        "categoria": "NLP",
        "descripcion": (
            "Representa visualmente las palabras relevantes "
            "y frecuentes de un conjunto de texto."
        ),
        "url": (
            "https://wordcloud-twmeornb88bu5daiohmzth.streamlit.app/"
        ),
        "imagen": "app_07.png",
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
        "imagen": "app_08.png",
    },

    {
        "numero": "09",
        "titulo": "Detector de objetos",
        "categoria": "Visión",
        "descripcion": (
            "Detecta objetos presentes en imágenes "
            "mediante técnicas de visión por computador."
        ),
        "url": (
            "https://yolov5-3qhk7h6k3kr9tjfgepuekf.streamlit.app/"
        ),
        "imagen": "app_09.png",
    },

    {
        "numero": "10",
        "titulo": "Detector de emociones",
        "categoria": "Visión",
        "descripcion": (
            "Analiza imágenes para identificar expresiones "
            "y emociones mediante visión artificial."
        ),
        "url": (
            "https://zb8fhzc4q6vjd726eqkviy.streamlit.app/"
        ),
        "imagen": "app_10.png",
    },

]


# ============================================================
# MOSTRAR LAS TARJETAS DE 3 EN 3
# ============================================================

for inicio in range(
    0,
    len(apps),
    3
):

    columnas = st.columns(
        3,
        gap="medium"
    )

    grupo = apps[
        inicio:inicio + 3
    ]

    for columna, app in zip(
        columnas,
        grupo
    ):

        with columna:

            ruta_imagen = os.path.join(
                "imagenes",
                app["imagen"]
            )

            if os.path.exists(
                ruta_imagen
            ):

                imagen = imagen_base64(
                    ruta_imagen
                )

                imagen_html = f"""
                <img
                    class="app-image"
                    src="data:image/png;base64,{imagen}"
                    alt="{app['titulo']}"
                >
                """

            else:

                imagen_html = """
                <div
                    class="app-image"
                    style="
                        background:
                            linear-gradient(
                                135deg,
                                #3f52e5,
                                #baff19
                            );
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        color:white;
                        font-size:3rem;
                        font-weight:700;
                    "
                >
                    ✦
                </div>
                """


            st.markdown(
                f"""
                <article class="app-card">

                    {imagen_html}

                    <div class="app-meta">

                        <div class="app-number">
                            APP {app["numero"]}
                        </div>

                        <div class="app-category">
                            {app["categoria"]}
                        </div>

                    </div>

                    <div class="app-title">
                        {app["titulo"]}
                    </div>

                    <div class="app-description">
                        {app["descripcion"]}
                    </div>

                    <div class="open-wrap">

                        <a
                            class="open-link"
                            href="{app["url"]}"
                            target="_blank"
                        >
                            Abrir aplicación ↗
                        </a>

                    </div>

                </article>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown(
    """
    <div class="footer">

        <div class="footer-title">
            ✦ Belen Cajahuaman
        </div>

        <div class="footer-copy">
            Portafolio de aplicaciones de Inteligencia Artificial.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)
