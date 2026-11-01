
import streamlit as st
import os

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Mi Portafolio | Interfaces Multimodales 2026",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# ESTILOS CSS
# Se utiliza st.html para que el código HTML/CSS no aparezca
# como texto dentro de la aplicación.
# ============================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
    --azul: #5b91ad;
    --azul-oscuro: #315e78;
    --celeste: #dff4f8;
    --lavanda: #eee8fa;
    --rosa: #f9e8ef;
    --texto: #466579;
}

/* FONDO COMPLETO */

.stApp {
    background: linear-gradient(
        135deg,
        #e3f6f8 0%,
        #e9effc 35%,
        #f2eafa 68%,
        #fcecf1 100%
    ) !important;
    font-family: 'Nunito', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

#MainMenu,
footer {
    visibility: hidden;
}

.block-container {
    max-width: 1600px;
    padding: 2rem 2.5rem 2rem;
}

/* COLUMNAS */

[data-testid="stHorizontalBlock"] {
    gap: 2rem !important;
}

/* PANEL IZQUIERDO */

.info-panel {
    background: rgba(255,255,255,.73);
    border: 1px solid rgba(255,255,255,.9);
    border-radius: 25px;
    padding: 30px 25px;
    box-shadow: 0 10px 35px rgba(90,130,160,.10);
}

.eyebrow {
    color: #8a9eb7;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.main-heading {
    color: #416c88;
    font-family: 'Playfair Display', serif;
    font-size: 39px;
    font-weight: 800;
    line-height: 1.15;
    margin: 15px 0 8px;
}

.name-heading {
    color: #8b80b5;
    font-size: 21px;
    font-weight: 900;
    margin: 8px 0 20px;
}

.description {
    color: #71899a;
    font-size: 14px;
    line-height: 1.9;
}

.soft-line {
    height: 3px;
    width: 65px;
    border-radius: 10px;
    background: linear-gradient(90deg, #87cbd9, #b9a9dd);
    margin: 22px 0;
}

.info-label {
    color: #527d96;
    font-size: 13px;
    font-weight: 900;
    margin-top: 17px;
}

.info-value {
    color: #8498a7;
    font-size: 13px;
    line-height: 1.7;
}

.project-count {
    background: linear-gradient(135deg, #d9f1f5, #e9e2f7);
    padding: 20px;
    border-radius: 17px;
    margin-top: 24px;
    text-align: center;
}

.project-count-number {
    color: #557f9b;
    font-size: 37px;
    font-weight: 900;
}

.project-count-text {
    color: #8499a8;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 2px;
}

/* TÍTULO DEL LADO DERECHO */

.projects-heading {
    color: #416c88;
    font-family: 'Playfair Display', serif;
    font-size: 31px;
    font-weight: 800;
    margin-bottom: 3px;
}

.projects-caption {
    color: #8a9eac;
    font-size: 13px;
    margin-bottom: 18px;
}

/* TARJETAS */

[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,.88) !important;
    border: 1px solid rgba(255,255,255,.95) !important;
    border-radius: 18px !important;
    padding: 13px !important;
    box-shadow: 0 7px 24px rgba(85,120,150,.10) !important;
    transition: transform .2s ease, box-shadow .2s ease;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(85,120,150,.16) !important;
}

[data-testid="stImage"] img {
    border-radius: 12px;
    object-fit: cover;
}

/* BOTONES */

div.stLinkButton > a {
    background: linear-gradient(90deg, #82bfd0, #9d9acb) !important;
    border: none !important;
    border-radius: 10px !important;
    color: white !important;
    font-size: 11px !important;
    font-weight: 900 !important;
    letter-spacing: .5px;
    transition: .2s;
}

div.stLinkButton > a:hover {
    background: linear-gradient(90deg, #6aaabd, #8984bb) !important;
    color: white !important;
}

/* TEXTOS DE TARJETAS */

.card-number {
    color: #d49eb1;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 1px;
}

.card-category {
    color: #8a9eb7;
    font-size: 10px;
    font-weight: 900;
    text-align: right;
    text-transform: uppercase;
}

.card-title {
    color: #527b96;
    font-size: 17px;
    font-weight: 900;
    line-height: 1.3;
    margin-top: 8px;
    min-height: 44px;
}

.card-description {
    color: #879aa6;
    font-size: 11px;
    line-height: 1.6;
    min-height: 55px;
}

/* ÁREA DE DESPLAZAMIENTO */

[data-testid="stVerticalBlock"]:has(> [data-testid="stVerticalBlockBorderWrapper"]) {
    min-width: 0;
}

/* PIE */

.footer-text {
    color: #879aaa;
    text-align: center;
    font-size: 11px;
    padding: 15px 0 5px;
    letter-spacing: 1px;
}

/* RESPONSIVE */

@media (max-width: 850px) {
    .block-container {
        padding: 1rem;
    }

    .main-heading {
        font-size: 31px;
    }

    .projects-heading {
        font-size: 25px;
    }
}

</style>
""")

# ============================================================
# DATOS DE LOS 19 PROYECTOS
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
        "descripcion": "Analiza imágenes para identificar expresiones y personas con Teachable Machine.",
        "url": "https://zb8fhzc4q6vjd726eqkviy.streamlit.app/",
        "imagen": "app_10.JPG"
    },
    {
        "numero": "11",
        "titulo": "Evalua Pro",
        "categoria": "Lenguaje",
        "descripcion": "Procesamiento de lenguaje natural y trabajo con documentos.",
        "url": "https://chatpdf-wajopxwdovw7vz87rbnfhe.streamlit.app/",
        "imagen": "app_11.JPG"
    },
    {
        "numero": "12",
        "titulo": "Vision Lab",
        "categoria": "Imagen",
        "descripcion": "Aplicación dedicada al análisis y procesamiento de imágenes.",
        "url": "https://visionapp-zvhnrjnesqyqvadmnjrmc9.streamlit.app/",
        "imagen": "app_12.JPG"
    },
    {
        "numero": "13",
        "titulo": "Detección de dígitos",
        "categoria": "Visión artificial",
        "descripcion": "Reconocimiento de números escritos a mano mediante inteligencia artificial.",
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
# DISTRIBUCIÓN PRINCIPAL: INFORMACIÓN + PROYECTOS
# ============================================================

col_info, col_projects = st.columns([0.85, 2.15], gap="large")

# ============================================================
# PANEL IZQUIERDO: INFORMACIÓN DEL PORTAFOLIO
# ============================================================

with col_info:

    with st.container(border=True):

        st.markdown("""
        <div class="eyebrow">PORTAFOLIO ACADÉMICO</div>

        <div class="main-heading">
            Mi portafolio de<br>
            Interfaces<br>
            Multimodales
        </div>

        <div class="name-heading">
            Belen Cajahuaman
        </div>

        <div class="description">
            Bienvenido a mi espacio creativo. Aquí encontrarás
            una recopilación de mis proyectos desarrollados
            durante el año 2026, donde exploro diferentes
            tecnologías y formas de interacción digital.
        </div>

        <div class="soft-line"></div>

        <div class="info-label">ÁREA DE ESTUDIO</div>
        <div class="info-value">
            Interfaces Multimodales
        </div>

        <div class="info-label">TECNOLOGÍAS</div>
        <div class="info-value">
            Streamlit · Python · Inteligencia Artificial
            · Procesamiento de lenguaje · Visión artificial
            · IoT · MQTT
        </div>

        <div class="info-label">OBJETIVO</div>
        <div class="info-value">
            Diseñar experiencias digitales que integren
            distintas formas de comunicación e interacción
            entre las personas y la tecnología.
        </div>

        <div class="project-count">
            <div class="project-count-number">19</div>
            <div class="project-count-text">
                PROYECTOS DESARROLLADOS
            </div>
        </div>

        <div class="info-label">AÑO</div>
        <div class="info-value">2026</div>

        """, unsafe_allow_html=True)

# ============================================================
# PANEL DERECHO: GALERÍA DE PROYECTOS
# ============================================================

with col_projects:

    st.markdown("""
    <div class="projects-heading">
        Mis proyectos
    </div>

    <div class="projects-caption">
        Explora cada aplicación y descubre lo que he creado.
    </div>
    """, unsafe_allow_html=True)

    # Área con desplazamiento independiente
    with st.container(height=760, border=False):

        for inicio in range(0, len(apps), 2):

            columnas = st.columns(2, gap="large")

            for columna, app in zip(
                columnas,
                apps[inicio:inicio + 2]
            ):

                with columna:

                    with st.container(border=True):

                        # Imagen del proyecto
                        if os.path.exists(app["imagen"]):

                            st.image(
                                app["imagen"],
                                use_container_width=True
                            )

                        else:

                            st.markdown(
                                f"""
                                <div style="
                                    height:150px;
                                    display:flex;
                                    align-items:center;
                                    justify-content:center;
                                    background:linear-gradient(
                                        135deg,
                                        #dff2f5,
                                        #eee8f8
                                    );
                                    border-radius:12px;
                                    color:#7898aa;
                                    font-size:13px;
                                    font-weight:800;
                                ">
                                    IMAGEN DEL PROYECTO {app["numero"]}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        # Número y categoría
                        meta1, meta2 = st.columns(2)

                        with meta1:
                            st.markdown(
                                f'<div class="card-number">PROYECTO {app["numero"]}</div>',
                                unsafe_allow_html=True
                            )

                        with meta2:
                            st.markdown(
                                f'<div class="card-category">{app["categoria"]}</div>',
                                unsafe_allow_html=True
                            )

                        # Nombre
                        st.markdown(
                            f'<div class="card-title">{app["titulo"]}</div>',
                            unsafe_allow_html=True
                        )

                        # Descripción
                        st.markdown(
                            f'<div class="card-description">{app["descripcion"]}</div>',
                            unsafe_allow_html=True
                        )

                        # Enlace
                        st.link_button(
                            "EXPLORAR PROYECTO ↗",
                            app["url"],
                            use_container_width=True
                        )

# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown("""
<div class="footer-text">
    BELEN CAJAHUAMAN · INTERFACES MULTIMODALES · 2026
    <br>
    CREATIVIDAD · TECNOLOGÍA · INNOVACIÓN
</div>
""", unsafe_allow_html=True)
