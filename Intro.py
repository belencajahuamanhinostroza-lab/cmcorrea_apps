
import streamlit as st
import os

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Belen Cajahuaman | Portafolio 2026",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# ESTILOS VISUALES
# ============================================================

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Caveat:wght@500;600;700&display=swap');

/* FONDO PASTEL COMPLETO */

.stApp {
    background: linear-gradient(
        135deg,
        #dff3f8 0%,
        #e9edfa 35%,
        #f0eafa 68%,
        #f9eaf0 100%
    ) !important;
    font-family: 'Poppins', sans-serif !important;
}

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1450px;
    padding: 2rem 3rem 2rem;
}

/* ENCABEZADO */

h1 {
    font-family: 'Caveat', cursive !important;
    color: #3985a5 !important;
    font-size: 76px !important;
    font-weight: 700 !important;
    line-height: 1 !important;
    margin-bottom: 0 !important;
}

h2, h3 {
    font-family: 'Poppins', sans-serif !important;
    color: #527b98 !important;
    font-weight: 700 !important;
}

p {
    color: #71899b;
    font-size: 13px;
    line-height: 1.8;
}

/* ETIQUETA SUPERIOR */

.top-label {
    color: #8a9bb4;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
}

/* PANEL PRINCIPAL */

[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,.87) !important;
    border: 1px solid rgba(255,255,255,.95) !important;
    border-radius: 25px !important;
    box-shadow: 0 12px 38px rgba(91,125,155,.12) !important;
    padding: 18px !important;
}

/* TARJETAS DE PROYECTOS */

.project-card [data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border: 1px solid #e7edf3 !important;
    border-radius: 17px !important;
    box-shadow: 0 5px 18px rgba(90,125,155,.09) !important;
}

[data-testid="stImage"] img {
    border-radius: 12px;
    object-fit: cover;
}

/* BOTONES */

div.stLinkButton > a {
    background: linear-gradient(
        100deg,
        #65b9d0,
        #9994ca
    ) !important;
    border: none !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: .5px;
    transition: .2s ease;
}

div.stLinkButton > a:hover {
    background: linear-gradient(
        100deg,
        #4da5bd,
        #817bb6
    ) !important;
    color: white !important;
    transform: translateY(-2px);
}

/* TEXTOS DE LAS TARJETAS */

.project-number {
    color: #d39db6;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.project-category {
    color: #8d9db8;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
}

.project-description {
    min-height: 75px;
    color: #8294a3;
    font-size: 11px;
    line-height: 1.7;
}

/* PIE DE PÁGINA */

.footer {
    color: #8a9bad;
    font-size: 11px;
    letter-spacing: 1.5px;
    text-align: center;
    padding: 25px 0 10px;
}

/* RESPONSIVE */

@media (max-width: 800px) {
    .block-container {
        padding: 1rem;
    }

    h1 {
        font-size: 55px !important;
    }
}
</style>
""")

# ============================================================
# DATOS DE LOS PROYECTOS
# ============================================================

apps = [
    {
        "numero": "01",
        "titulo": "Mi primera App",
        "categoria": "Inicio",
        "descripcion": "Primera aplicación del portafolio para explorar Streamlit y GitHub.",
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
        "categoria": "Procesamiento de texto",
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
        "categoria": "Visión artificial",
        "descripcion": "Detecta objetos presentes en imágenes mediante visión por computador.",
        "url": "https://yolov5-3qhk7h6k3kr9tjfgepuekf.streamlit.app/",
        "imagen": "app_09.JPG"
    },
    {
        "numero": "10",
        "titulo": "Detector de gestos",
        "categoria": "Visión artificial",
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
# ENCABEZADO PRINCIPAL
# ============================================================

st.markdown(
    '<div class="top-label">PORTAFOLIO ACADÉMICO · 2026</div>',
    unsafe_allow_html=True
)

st.title("Mi portafolio")

st.subheader("Interfaces Multimodales 2026")

st.markdown("### Belen Cajahuaman")

st.write(
    "Un espacio donde la creatividad, el diseño y la tecnología "
    "se encuentran. En este portafolio presento los proyectos que "
    "he desarrollado durante mi aprendizaje en Interfaces "
    "Multimodales, explorando distintas formas de interacción "
    "entre las personas y los sistemas digitales."
)

st.write(
    "A través de estas experiencias he trabajado con procesamiento "
    "de lenguaje, reconocimiento de voz, visión artificial, "
    "inteligencia artificial, visualización de datos y comunicación IoT."
)

st.divider()

# ============================================================
# PANEL PRINCIPAL CON TODOS LOS PROYECTOS
# ============================================================

st.markdown("## ✦ Mis proyectos")

st.caption(
    "Explora cada aplicación, conoce su propósito y accede a ella "
    "mediante el botón correspondiente."
)

with st.container(border=True):

    st.markdown(
        "### Galería de aplicaciones"
    )

    st.caption(
        "19 proyectos · Interfaces multimodales · 2026"
    )

    # Tres tarjetas por fila
    for inicio in range(0, len(apps), 3):

        columnas = st.columns(3, gap="large")

        for columna, app in zip(
            columnas,
            apps[inicio:inicio + 3]
        ):

            with columna:

                with st.container(border=True):

                    # Imagen
                    if os.path.exists(app["imagen"]):
                        st.image(
                            app["imagen"],
                            use_container_width=True
                        )
                    else:
                        st.markdown(
                            f"**Proyecto {app['numero']}**"
                        )
                        st.caption(
                            "Agrega la captura del proyecto para mostrarla aquí."
                        )

                    # Número y categoría
                    st.caption(
                        f"PROYECTO {app['numero']}  ·  {app['categoria']}"
                    )

                    # Título
                    st.subheader(app["titulo"])

                    # Descripción
                    st.write(app["descripcion"])

                    # Enlace
                    st.link_button(
                        "EXPLORAR PROYECTO ↗",
                        app["url"],
                        use_container_width=True
                    )

# ============================================================
# INFORMACIÓN FINAL
# ============================================================

st.divider()

st.markdown("### ✦ Lo que he desarrollado")

st.write(
    "Durante este proceso he creado experiencias que integran "
    "diferentes tecnologías y herramientas digitales."
)

skills = st.columns(3)

with skills[0]:
    st.markdown("**Procesamiento de información**")
    st.caption("NLP · TF-IDF · Análisis de sentimientos · OCR")

with skills[1]:
    st.markdown("**Interacción multimodal**")
    st.caption("Voz · Audio · Imagen · Dibujo · Visión artificial")

with skills[2]:
    st.markdown("**Tecnologías y conexión**")
    st.caption("Python · Streamlit · MQTT · Wokwi · Dashboards")

st.markdown(
    '<div class="footer">'
    'BELEN CAJAHUAMAN · INTERFACES MULTIMODALES · 2026'
    '</div>',
    unsafe_allow_html=True
)
