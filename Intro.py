
import streamlit as st
import os
import base64
import html
import mimetypes

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Belen Cajahuaman | Portafolio 2026",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CARGA DE IMÁGENES
# =========================================================

def imagen_base64(ruta):
    if not os.path.exists(ruta):
        return None

    mime, _ = mimetypes.guess_type(ruta)

    if not mime:
        mime = "image/jpeg"

    with open(ruta, "rb") as archivo:
        contenido = base64.b64encode(
            archivo.read()
        ).decode("utf-8")

    return f"data:{mime};base64,{contenido}"


fondo = imagen_base64("fondo.jpg")

if fondo:
    fondo_css = f'url("{fondo}")'
else:
    fondo_css = "linear-gradient(135deg, #dff3f8, #e9edfa, #f9eaf0)"


# =========================================================
# ESTILOS GENERALES
# =========================================================

css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&family=Caveat:wght@600;700&display=swap');

:root {
    --azul: #378eae;
    --azul-oscuro: #26366e;
    --azul-texto: #344f65;
}

#MainMenu, footer, [data-testid="stHeader"] {
    visibility: hidden;
    height: 0;
}

.stApp {
    background-image: BACKGROUND_IMAGE !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
    background-repeat: no-repeat !important;
    font-family: 'Poppins', sans-serif !important;
}

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
}

.block-container {
    max-width: 1600px !important;
    padding: 2rem 2.5rem !important;
}

p {
    color: var(--azul-texto);
    font-size: 16px !important;
    line-height: 1.85 !important;
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif !important;
}

/* ENCABEZADO */

.hero {
    padding: 30px 10px 35px;
    text-align: left;
}

.hero-label {
    color: #355d7a;
    font-size: 16px;
    font-weight: 800;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.hero-title {
    font-family: 'Caveat', cursive !important;
    color: #26366e;
    font-size: 100px;
    line-height: 1.05;
    font-weight: 700;
    margin: 0;
}

.hero-subtitle {
    color: #287da3;
    font-size: 30px;
    font-weight: 800;
    margin-top: 5px;
}

.hero-name {
    display: inline-block;
    color: white;
    background: linear-gradient(100deg, #489ab7, #8c83bb);
    padding: 12px 30px;
    border-radius: 40px;
    font-size: 20px;
    font-weight: 800;
    margin-top: 18px;
}

.hero-description {
    max-width: 950px;
    color: #344f65;
    font-size: 18px;
    line-height: 1.9;
    margin-top: 20px;
}

/* DISTRIBUCIÓN */

.portfolio-layout {
    display: grid;
    grid-template-columns: minmax(250px, 0.85fr) minmax(0, 2.4fr);
    gap: 28px;
    align-items: start;
}

/* PANELES BLANCOS */

.white-panel {
    background: #ffffff !important;
    border: 2px solid #ffffff;
    border-radius: 28px;
    padding: 27px;
    box-shadow: 0 10px 30px rgba(42, 78, 110, 0.15);
    opacity: 1 !important;
    color: #344f65;
}

.about-panel {
    position: sticky;
    top: 20px;
}

.panel-title {
    color: #28366e;
    font-size: 27px;
    font-weight: 800;
    margin: 0 0 18px;
}

.panel-text {
    color: #344f65;
    font-size: 16px;
    line-height: 1.9;
    margin-bottom: 17px;
}

.panel-section {
    border-top: 1px solid #e4edf3;
    padding-top: 17px;
    margin-top: 18px;
}

.panel-section h3 {
    color: #287da3;
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 8px;
}

.project-count {
    background: #e8f5fa;
    border-radius: 18px;
    padding: 16px;
    margin-top: 20px;
    text-align: center;
}

.project-count strong {
    display: block;
    color: #287da3;
    font-size: 42px;
    font-weight: 900;
}

.project-count span {
    color: #496b82;
    font-size: 14px;
    font-weight: 700;
}

/* GALERÍA */

.gallery-title {
    color: #28366e;
    font-size: 30px;
    font-weight: 900;
    margin-bottom: 8px;
}

.gallery-description {
    color: #496b82;
    font-size: 16px;
    line-height: 1.8;
    margin-bottom: 25px;
}

/* TARJETAS */

.projects-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 24px;
}

.project-card {
    background: #ffffff !important;
    border: 2px solid #e7f0f5;
    border-radius: 23px;
    padding: 17px;
    box-shadow: 0 6px 20px rgba(43, 86, 115, 0.10);
    display: flex;
    flex-direction: column;
    min-width: 0;
    transition: transform .2s ease, box-shadow .2s ease;
}

.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 26px rgba(43, 86, 115, 0.17);
}

.project-image {
    width: 100%;
    height: 155px;
    object-fit: cover;
    border-radius: 15px;
    display: block;
    margin-bottom: 15px;
}

.image-placeholder {
    width: 100%;
    height: 155px;
    border-radius: 15px;
    background: linear-gradient(135deg, #dceef8, #eee8f8);
    display: flex;
    justify-content: center;
    align-items: center;
    color: #547b99;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 15px;
    text-align: center;
}

.project-meta {
    display: flex;
    align-items: center;
    gap: 9px;
    margin-bottom: 12px;
    flex-wrap: wrap;
}

.project-number {
    background: #478eaf;
    color: #ffffff;
    padding: 5px 11px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 900;
}

.project-category {
    color: #3e7595;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
}

.project-title {
    color: #26366e;
    font-size: 19px;
    font-weight: 800;
    line-height: 1.4;
    margin: 0 0 10px;
    min-height: 54px;
}

.project-description {
    color: #435c70;
    font-size: 15px;
    line-height: 1.8;
    margin: 0 0 18px;
    flex-grow: 1;
    min-height: 100px;
}

/* BOTONES */

.project-button {
    display: block;
    width: 100%;
    box-sizing: border-box;
    text-align: center;
    text-decoration: none !important;
    color: #ffffff !important;
    background: linear-gradient(110deg, #378eae, #777db5);
    border-radius: 12px;
    padding: 14px 9px;
    font-family: 'Poppins', sans-serif;
    font-size: 14px;
    font-weight: 800;
    transition: .2s ease;
    margin-top: auto;
}

.project-button:hover {
    color: #ffffff !important;
    background: linear-gradient(110deg, #267b9b, #5f66a3);
    transform: translateY(-2px);
}

/* HABILIDADES */

.skills-panel {
    margin-top: 28px;
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.skill-card {
    background: #ffffff;
    border: 2px solid #e7f0f5;
    border-radius: 20px;
    padding: 20px;
}

.skill-card h3 {
    color: #287da3;
    font-size: 19px;
    font-weight: 800;
    margin: 0 0 10px;
}

.skill-card p {
    color: #435c70;
    font-size: 15px !important;
    line-height: 1.8 !important;
    margin: 0;
}

/* PIE DE PÁGINA */

.footer {
    text-align: center;
    color: #345c79;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 2px;
    padding: 35px 10px 15px;
    line-height: 2;
}

/* RESPONSIVE */

@media (max-width: 1050px) {
    .portfolio-layout {
        grid-template-columns: 1fr;
    }

    .about-panel {
        position: static;
    }

    .projects-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 650px) {
    .block-container {
        padding: 1rem !important;
    }

    .hero-title {
        font-size: 65px;
    }

    .hero-subtitle {
        font-size: 22px;
    }

    .projects-grid,
    .skills-grid {
        grid-template-columns: 1fr;
    }

    .white-panel {
        padding: 18px;
    }

    .project-description {
        min-height: auto;
    }
}
</style>
"""

css = css.replace("BACKGROUND_IMAGE", fondo_css)
st.html(css)


# =========================================================
# INFORMACIÓN DE LOS 19 PROYECTOS
# =========================================================

apps = [
    {
        "numero": "01",
        "titulo": "Mi primera App",
        "categoria": "Inicio",
        "descripcion": "Primera aplicación desarrollada para explorar Streamlit y GitHub.",
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
        "descripcion": "Analiza contenido escrito para identificar el sentimiento presente.",
        "url": "https://sentimenta-yvw8kjjhc3k5ahfm2bvbbk.streamlit.app/",
        "imagen": "app_06.JPG"
    },
    {
        "numero": "07",
        "titulo": "Nube de palabras",
        "categoria": "NLP",
        "descripcion": "Genera una representación visual de las palabras más relevantes.",
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
        "descripcion": "Analiza imágenes para identificar gestos y personas con Teachable Machine.",
        "url": "https://zb8fhzc4q6vjd726eqkviy.streamlit.app/",
        "imagen": "app_10.JPG"
    },
    {
        "numero": "11",
        "titulo": "Evalua Pro",
        "categoria": "Lenguaje",
        "descripcion": "Aplicación de procesamiento de lenguaje para trabajar con documentos.",
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
        "descripcion": "Aplicación para reconocer números escritos a mano.",
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
        "descripcion": "Conecta datos de un dispositivo simulado en Wokwi con Streamlit.",
        "url": "https://recepmqtt-dudyrincxvdsvf8rxrfb55.streamlit.app/",
        "imagen": "app_17.JPG"
    },
    {
        "numero": "18",
        "titulo": "De Streamlit a Wokwi",
        "categoria": "IoT · MQTT",
        "descripcion": "Comunicación desde Streamlit hacia un dispositivo mediante MQTT.",
        "url": "https://sendcmqtt-ddtw2ekzvyfjngaamhbkra.streamlit.app/",
        "imagen": "app_18.JPG"
    },
    {
        "numero": "19",
        "titulo": "Control por Voz",
        "categoria": "Voz",
        "descripcion": "Permite interactuar y controlar funciones mediante comandos de voz.",
        "url": "https://ctrlvoice-9pedwjpvfprq6xjcdzaptz.streamlit.app/",
        "imagen": "app_19.JPG"
    }
]


# =========================================================
# CREAR TARJETAS
# =========================================================

tarjetas = []

for app in apps:

    numero = html.escape(app["numero"])
    titulo = html.escape(app["titulo"])
    categoria = html.escape(app["categoria"])
    descripcion = html.escape(app["descripcion"])
    url = html.escape(app["url"], quote=True)

    imagen = imagen_base64(app["imagen"])

    if imagen:
        imagen_html = f"""
        <img class="project-image"
             src="{imagen}"
             alt="{titulo}">
        """
    else:
        imagen_html = f"""
        <div class="image-placeholder">
            Proyecto {numero}
        </div>
        """

    tarjeta = f"""
    <article class="project-card">

        {imagen_html}

        <div class="project-meta">
            <span class="project-number">{numero}</span>
            <span class="project-category">{categoria}</span>
        </div>

        <h3 class="project-title">{titulo}</h3>

        <p class="project-description">
            {descripcion}
        </p>

        <a class="project-button"
           href="{url}"
           target="_blank"
           rel="noopener noreferrer">
            EXPLORAR PROYECTO ↗
        </a>

    </article>
    """

    tarjetas.append(tarjeta)


# =========================================================
# ENCABEZADO
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-label">
        PORTAFOLIO ACADÉMICO · 2026
    </div>

    <h1 class="hero-title">
        Mi portafolio
    </h1>

    <div class="hero-subtitle">
        Interfaces Multimodales 2026
    </div>

    <div class="hero-name">
        Belen Cajahuaman
    </div>

    <div class="hero-description">
        Un espacio donde la creatividad, el diseño y la tecnología
        se encuentran. En este portafolio presento los proyectos
        que he desarrollado durante mi aprendizaje en Interfaces
        Multimodales.

        <br><br>

        Explora mis experiencias con procesamiento de lenguaje,
        reconocimiento de voz, visión artificial, inteligencia
        artificial, visualización de datos y comunicación IoT.
    </div>

</div>
""")


# =========================================================
# PANEL PERSONAL Y PANEL DE PROYECTOS
# =========================================================

panel_personal = """
<section class="white-panel about-panel">

    <h2 class="panel-title">Sobre mí</h2>

    <p class="panel-text">
        Soy Belen Cajahuaman, Aquí comparto 19 proyectos 
        desarrollados durante mi aprendizaje, combinando
        creatividad, programación y soluciones digitales.
    </p>

    <div class="panel-section">
        <h3>Mi formación</h3>
        <p class="panel-text">
            Interfaces Multimodales · 2026
        </p>
    </div>

    <div class="panel-section">
        <h3>Tecnologías</h3>
        <p class="panel-text">
            Python · Streamlit · Inteligencia Artificial ·
            Procesamiento de Lenguaje · Visión Artificial ·
            IoT · MQTT
        </p>
    </div>

    <div class="panel-section">
        <h3>Mi objetivo</h3>
        <p class="panel-text">
            Crear experiencias digitales que conecten a las
            personas con la tecnología mediante diferentes
            formas de interacción.
        </p>
    </div>

    <div class="project-count">
        <strong>19</strong>
        <span>PROYECTOS DESARROLLADOS</span>
    </div>

</section>
"""

panel_proyectos = f"""
<section class="white-panel">

    <h2 class="gallery-title">
        ✦ Mis proyectos
    </h2>

    <p class="gallery-description">
        Explora cada aplicación, conoce su propósito
        y accede a ella mediante el botón.
    </p>

    <div class="projects-grid">
        {''.join(tarjetas)}
    </div>

</section>
"""

st.html(f"""
<div class="portfolio-layout">
    {panel_personal}
    {panel_proyectos}
</div>
""")


# =========================================================
# HABILIDADES
# =========================================================

st.html("""
<section class="white-panel skills-panel">

    <h2 class="gallery-title">
        ✦ Lo que he desarrollado
    </h2>

    <p class="gallery-description">
        A lo largo de estos proyectos he explorado diferentes
        herramientas y tecnologías para crear experiencias digitales.
    </p>

    <div class="skills-grid">

        <div class="skill-card">
            <h3>Procesamiento de información</h3>
            <p>
                NLP · TF-IDF · Análisis de sentimientos · OCR
            </p>
        </div>

        <div class="skill-card">
            <h3>Interacción multimodal</h3>
            <p>
                Voz · Audio · Imagen · Dibujo · Visión artificial
            </p>
        </div>

        <div class="skill-card">
            <h3>Tecnología y conexión</h3>
            <p>
                Python · Streamlit · MQTT · Wokwi · Dashboards
            </p>
        </div>

    </div>

</section>
""")


# =========================================================
# PIE DE PÁGINA
# =========================================================

st.html("""
<div class="footer">

    BELEN CAJAHUAMAN · INTERFACES MULTIMODALES · 2026

    <br>

    CREATIVIDAD · TECNOLOGÍA · INNOVACIÓN

</div>
""")
