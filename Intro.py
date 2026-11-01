
import streamlit as st
import os
import base64

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Belen Cajahuaman | Portafolio 2026",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CARGAR IMAGEN DE FONDO
# ============================================================

def cargar_fondo(ruta):
    if os.path.exists(ruta):
        with open(ruta, "rb") as archivo:
            imagen = base64.b64encode(archivo.read()).decode()

        return f"data:image/jpeg;base64,{imagen}"

    return None


fondo = cargar_fondo("fondo.jpg")

if fondo:
    fondo_css = f"""
    background-image:
        linear-gradient(
            rgba(225, 244, 250, 0.30),
            rgba(240, 232, 249, 0.30)
        ),
        url("{fondo}");
    """
else:
    fondo_css = """
    background: linear-gradient(
        135deg,
        #dff3f8,
        #e9edfa,
        #f0eafa,
        #f9eaf0
    );
    """

# ============================================================
# DISEÑO GENERAL
# ============================================================

st.html(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&family=Caveat:wght@500;600;700&display=swap');

/* FONDO DE TODA LA PÁGINA */

.stApp {{
    {fondo_css}
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
    background-repeat: no-repeat !important;
    font-family: 'Poppins', sans-serif !important;
}}

html, body, [class*="css"] {{
    font-family: 'Poppins', sans-serif !important;
    font-size: 14px !important;
}}

[data-testid="stHeader"] {{
    background: transparent !important;
}}

#MainMenu,
footer {{
    visibility: hidden;
}}

.block-container {{
    max-width: 1550px;
    padding: 2rem 2.5rem 2rem;
}}

/* TEXTOS GENERALES */

p {{
    color: #496b82;
    font-size: 14px !important;
    line-height: 1.8 !important;
}}

h1 {{
    font-family: 'Caveat', cursive !important;
    color: #28799d !important;
    font-size: 82px !important;
    font-weight: 700 !important;
    line-height: 1.05 !important;
    margin-bottom: 0 !important;
}}

h2, h3 {{
    font-family: 'Poppins', sans-serif !important;
    color: #386d8b !important;
    font-weight: 800 !important;
}}

h2 {{
    font-size: 27px !important;
}}

h3 {{
    font-size: 20px !important;
}}

small {{
    font-size: 13px !important;
}}

/* ETIQUETAS */

.top-label {{
    color: #537f9a;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
}}

.name-label {{
    color: #ffffff;
    background: linear-gradient(90deg, #a58cc8, #83bad1);
    display: inline-block;
    padding: 9px 25px;
    border-radius: 30px;
    font-size: 17px;
    font-weight: 800;
    margin: 8px 0 15px;
}}

.section-description {{
    color: #496b82;
    font-size: 14px;
    line-height: 1.8;
}}

.project-number {{
    color: #ffffff;
    background: #5c9eb9;
    border-radius: 20px;
    padding: 4px 10px;
    font-size: 11px;
    font-weight: 900;
    display: inline-block;
}}

.project-category {{
    color: #5687a4;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
}}

.project-description {{
    color: #54748a;
    font-size: 13px;
    line-height: 1.7;
    min-height: 75px;
}}

/* CUADRADOS Y PANELES CELESTES */

[data-testid="stVerticalBlockBorderWrapper"] {{
    background: rgba(219, 244, 251, 0.94) !important;
    border: 2px solid rgba(255, 255, 255, 0.95) !important;
    border-radius: 24px !important;
    box-shadow: 0 9px 25px rgba(60, 119, 153, 0.14) !important;
    padding: 18px !important;
}}

/* TARJETAS INDIVIDUALES */

[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlockBorderWrapper"] {{
    background: rgba(239, 250, 253, 0.98) !important;
    border: 1px solid #ffffff !important;
    border-radius: 19px !important;
    box-shadow: 0 5px 17px rgba(65, 130, 160, 0.12) !important;
    padding: 13px !important;
    transition: transform .2s ease, box-shadow .2s ease;
}}

[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlockBorderWrapper"]:hover {{
    transform: translateY(-4px);
    box-shadow: 0 10px 23px rgba(65, 130, 160, 0.20) !important;
}}

/* IMÁGENES */

[data-testid="stImage"] img {{
    border-radius: 15px !important;
    object-fit: cover;
}}

/* BOTONES CON TEXTO BLANCO */

div.stLinkButton > a {{
    background: linear-gradient(
        100deg,
        #3997b5,
        #777fba
    ) !important;
    border: none !important;
    border-radius: 11px !important;
    color: #ffffff !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 13px !important;
    font-weight: 800 !important;
    letter-spacing: .3px;
    padding: 10px 12px !important;
    transition: .2s ease;
}}

div.stLinkButton > a:hover {{
    background: linear-gradient(
        100deg,
        #287f9f,
        #656ba7
    ) !important;
    color: #ffffff !important;
    transform: translateY(-2px);
}}

/* MÉTRICAS */

[data-testid="stMetric"] {{
    background: rgba(224, 246, 252, .9);
    padding: 14px;
    border-radius: 15px;
}}

[data-testid="stMetricLabel"] {{
    color: #527a94 !important;
    font-size: 13px !important;
}}

[data-testid="stMetricValue"] {{
    color: #317b9d !important;
    font-size: 30px !important;
}}

/* DIVISORES */

hr {{
    border-color: rgba(255,255,255,.8) !important;
    margin: 25px 0 !important;
}}

/* PIE */

.footer {{
    color: #416f8a;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-align: center;
    padding: 25px 0 10px;
}}

/* RESPONSIVE */

@media (max-width: 850px) {{
    .block-container {{
        padding: 1rem;
    }}

    h1 {{
        font-size: 58px !important;
    }}

    h2 {{
        font-size: 23px !important;
    }}
}}

</style>
""")

# ============================================================
# INFORMACIÓN DE LOS 19 PROYECTOS
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
# ENCABEZADO
# ============================================================

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
    "se encuentran. Explora mis proyectos y descubre cómo la "
    "innovación transforma la interacción digital."
)

st.write(
    "Durante este proceso he desarrollado aplicaciones que integran "
    "procesamiento de lenguaje, reconocimiento de voz, visión artificial, "
    "inteligencia artificial, visualización de datos y comunicación IoT."
)

st.divider()

# ============================================================
# PANEL DE INFORMACIÓN Y PROYECTOS
# ============================================================

col_info, col_projects = st.columns(
    [0.85, 2.4],
    gap="large"
)

# ============================================================
# PANEL IZQUIERDO
# ============================================================

with col_info:

    with st.container(border=True):

        st.subheader("Sobre mí")

        st.write(
            "Soy Belen Cajahuaman, estudiante apasionada por la "
            "tecnología, la inteligencia artificial y las interfaces "
            "multimodales."
        )

        st.write(
            "En este portafolio comparto 19 proyectos desarrollados "
            "durante mi aprendizaje, donde combino creatividad, "
            "programación y soluciones innovadoras."
        )

        st.divider()

        st.subheader("Mi formación")

        st.write("Interfaces Multimodales")

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

        st.metric(
            label="Proyectos desarrollados",
            value="19"
        )

        st.caption("Año académico: 2026")

# ============================================================
# PANEL DERECHO: GALERÍA DE PROYECTOS
# ============================================================

with col_projects:

    with st.container(border=True):

        st.subheader("✦ Mis proyectos")

        st.caption(
            "Explora cada aplicación y accede a ella mediante su botón."
        )

        st.divider()

        # Tres proyectos por fila
        for inicio in range(0, len(apps), 3):

            columnas = st.columns(3, gap="large")

            for columna, app in zip(
                columnas,
                apps[inicio:inicio + 3]
            ):

                with columna:

                    with st.container(border=True):

                        # IMAGEN DEL PROYECTO
                        if os.path.exists(app["imagen"]):

                            st.image(
                                app["imagen"],
                                use_container_width=True
                            )

                        else:

                            st.markdown(
                                f"### Proyecto {app['numero']}"
                            )

                            st.caption(
                                "Agrega la captura correspondiente "
                                "con el nombre indicado."
                            )

                        # NÚMERO Y CATEGORÍA
                        st.markdown(
                            f'<span class="project-number">'
                            f'{app["numero"]}</span> '
                            f'<span class="project-category">'
                            f'{app["categoria"]}</span>',
                            unsafe_allow_html=True
                        )

                        # TÍTULO
                        st.subheader(app["titulo"])

                        # DESCRIPCIÓN
                        st.markdown(
                            f'<div class="project-description">'
                            f'{app["descripcion"]}'
                            f'</div>',
                            unsafe_allow_html=True
                        )

                        # BOTÓN
                        st.link_button(
                            "EXPLORAR PROYECTO ↗",
                            app["url"],
                            use_container_width=True
                        )

# ============================================================
# HABILIDADES DESARROLLADAS
# ============================================================

st.divider()

with st.container(border=True):

    st.subheader("✦ Lo que he desarrollado")

    st.write(
        "A lo largo de estos proyectos he explorado diferentes "
        "herramientas y tecnologías para crear experiencias digitales."
    )

    habilidad1, habilidad2, habilidad3 = st.columns(3)

    with habilidad1:
        st.markdown("### Procesamiento de información")
        st.write(
            "NLP · TF-IDF · Análisis de sentimientos · OCR"
        )

    with habilidad2:
        st.markdown("### Interacción multimodal")
        st.write(
            "Voz · Audio · Imagen · Dibujo · Visión artificial"
        )

    with habilidad3:
        st.markdown("### Tecnología y conexión")
        st.write(
            "Python · Streamlit · MQTT · Wokwi · Dashboards"
        )

# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown(
    '<div class="footer">'
    'BELEN CAJAHUAMAN · INTERFACES MULTIMODALES · 2026'
    '<br>CREATIVIDAD · TECNOLOGÍA · INNOVACIÓN'
    '</div>',
    unsafe_allow_html=True
)
