import streamlit as st
import urllib.parse
from datetime import date, timedelta

# ── Configuración ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Para ti ✨",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Estilos ───────────────────────────────────────────────────────────────────
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400&display=swap" rel="stylesheet">

<style>
/* ── Variables ── */
:root {
  --blush: #F9EDE8;
  --rose: #C8796A;
  --rose-deep: #9B4F42;
  --petal: #F2D9D3;
  --cream: #FAF7F4;
  --ink: #2E2118;
  --muted: #8C7068;
  --divider: #E8D5CE;
}

/* ── Fondo general ── */
.stApp { background-color: var(--cream) !important; }
.block-container { max-width: 560px !important; padding: 2.5rem 1.5rem 4rem !important; }

/* ── Tipografía global ── */
html, body, [class*="css"] {
  font-family: 'Jost', sans-serif !important;
  font-weight: 300;
  color: var(--ink) !important;
}
/* Forzar color de texto en párrafos y spans de Streamlit */
.stApp p, .stApp span, .stApp label { color: var(--ink) !important; }
div[data-testid="stLinkButton"] a { color: white !important; }
div[data-testid="stButton"] button { color: white !important; }

/* ── Títulos con Cormorant ── */
h1, h2, h3 {
  font-family: 'Cormorant Garamond', serif !important;
  font-weight: 300 !important;
  font-style: italic !important;
  color: var(--ink) !important;
}

/* ── Eyebrow ── */
.eyebrow {
  font-family: 'Jost', sans-serif;
  font-size: 0.68rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--rose);
  margin-bottom: 0.25rem;
}

/* ── Tarjeta principal ── */
.card {
  background: white;
  border-radius: 24px;
  padding: 2.5rem 2rem;
  box-shadow: 0 2px 40px rgba(200,121,106,0.1);
  position: relative;
  overflow: hidden;
  margin-bottom: 1.5rem;
}
.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--petal), var(--rose), var(--petal));
}

/* ── Texto introducción ── */
.intro-text {
  font-size: 0.93rem;
  line-height: 1.8;
  color: var(--muted);
  margin-bottom: 0.5rem;
}

/* ── Labels de preguntas ── */
.q-label {
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  font-size: 1.1rem;
  color: var(--ink);
  margin-bottom: 0.25rem;
  display: block;
}
.q-sub {
  font-size: 0.8rem;
  color: var(--muted);
  margin-bottom: 0.5rem;
  display: block;
}

/* ── Radio buttons ── */
div[data-testid="stRadio"] > label {
  font-family: 'Cormorant Garamond', serif !important;
  font-style: italic !important;
  font-size: 1.05rem !important;
  color: var(--ink) !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
  font-family: 'Jost', sans-serif !important;
  font-style: normal !important;
  font-size: 0.92rem !important;
  background: white !important;
  border: 1px solid var(--divider) !important;
  border-radius: 12px !important;
  padding: 0.65rem 1rem !important;
  margin-bottom: 0.4rem !important;
  color: var(--ink) !important;
  transition: background 0.2s;
  cursor: pointer;
}
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
  background: var(--blush) !important;
  border-color: var(--rose) !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label p,
div[data-testid="stRadio"] div[role="radiogroup"] label span,
div[data-testid="stRadio"] div[role="radiogroup"] label div {
  color: var(--ink) !important;
  font-family: 'Jost', sans-serif !important;
  font-style: normal !important;
  font-size: 0.92rem !important;
}
/* Forzar color en todos los párrafos dentro del radio */
div[data-testid="stRadio"] p {
  color: var(--ink) !important;
}
div[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"] span {
  color: var(--ink) !important;
}

/* ── Selectbox ── */
div[data-testid="stSelectbox"] label {
  font-family: 'Cormorant Garamond', serif !important;
  font-style: italic !important;
  font-size: 1.05rem !important;
  color: var(--ink) !important;
}
div[data-testid="stSelectbox"] > div > div {
  border: 1px solid var(--divider) !important;
  border-radius: 10px !important;
  font-family: 'Jost', sans-serif !important;
  font-size: 0.9rem !important;
}
div[data-testid="stSelectbox"] > div > div:focus-within {
  border-color: var(--rose) !important;
  box-shadow: none !important;
}

/* ── Text input ── */
div[data-testid="stTextInput"] label {
  font-family: 'Cormorant Garamond', serif !important;
  font-style: italic !important;
  font-size: 1.05rem !important;
  color: var(--ink) !important;
}
div[data-testid="stTextInput"] input {
  border: 1px solid var(--divider) !important;
  border-radius: 10px !important;
  font-family: 'Jost', sans-serif !important;
  font-size: 0.9rem !important;
}
div[data-testid="stTextInput"] input:focus {
  border-color: var(--rose) !important;
  box-shadow: none !important;
}

/* ── Date input ── */
div[data-testid="stDateInput"] label {
  font-family: 'Cormorant Garamond', serif !important;
  font-style: italic !important;
  font-size: 1.05rem !important;
  color: var(--ink) !important;
}
div[data-testid="stDateInput"] input {
  border: 1px solid var(--divider) !important;
  border-radius: 10px !important;
  font-family: 'Jost', sans-serif !important;
  font-size: 0.9rem !important;
}
div[data-testid="stDateInput"] input:focus {
  border-color: var(--rose) !important;
  box-shadow: none !important;
}

/* ── Botones ── */
div[data-testid="stButton"] > button {
  width: 100%;
  background-color: var(--rose) !important;
  color: white !important;
  border: none !important;
  border-radius: 50px !important;
  font-family: 'Jost', sans-serif !important;
  font-weight: 400 !important;
  font-size: 0.9rem !important;
  letter-spacing: 0.05em !important;
  padding: 0.65rem 1.5rem !important;
  transition: background 0.2s !important;
}
div[data-testid="stButton"] > button:hover {
  background-color: var(--rose-deep) !important;
  border: none !important;
}

/* ── Link button (WhatsApp) ── */
div[data-testid="stLinkButton"] > a {
  width: 100%;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 0.5rem !important;
  background-color: #25D366 !important;
  color: white !important;
  border: none !important;
  border-radius: 50px !important;
  font-family: 'Jost', sans-serif !important;
  font-weight: 400 !important;
  font-size: 0.9rem !important;
  padding: 0.65rem 1.5rem !important;
  text-decoration: none !important;
}
div[data-testid="stLinkButton"] > a:hover {
  background-color: #1da851 !important;
}

/* ── Caja resumen ── */
.summary-box {
  background: var(--blush);
  border-radius: 14px;
  padding: 1.25rem 1.5rem;
  margin: 1rem 0 1.5rem;
  font-size: 0.9rem;
  line-height: 2;
}
.summary-row {
  display: flex;
  gap: 0.75rem;
  border-bottom: 1px solid var(--divider);
  padding: 0.25rem 0;
  color: var(--ink);
}
.summary-row:last-child { border-bottom: none; }
.summary-key {
  color: var(--muted);
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  min-width: 80px;
  padding-top: 3px;
}

/* ── Mensaje soft-no ── */
.soft-quote {
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  font-size: 1.2rem;
  color: var(--muted);
  line-height: 1.8;
  text-align: center;
  padding: 1rem 0;
}

/* ── Divider ── */
hr { border-color: var(--divider) !important; margin: 1.5rem 0 !important; }

/* ── Ocultar elementos de Streamlit ── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)

# ── Estado de la sesión ────────────────────────────────────────────────────────
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "landing"
if "datos" not in st.session_state:
    st.session_state.datos = {}

TELEFONO = "573123894546"


# ── Helper: tarjeta con borde rosa ────────────────────────────────────────────
def abrir_card(titulo_eyebrow, titulo_h1, subtexto=None):
    st.markdown(f"""
    <div class="card">
      <p class="eyebrow">{titulo_eyebrow}</p>
      <h2 style="font-size:1.9rem; margin-bottom:0.75rem;">{titulo_h1}</h2>
      {"<p class='intro-text'>" + subtexto + "</p>" if subtexto else ""}
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# PANTALLA 1 — Landing
# ════════════════════════════════════════════════════════════════════════════════
if st.session_state.pantalla == "landing":

    abrir_card(
        "Una invitación para María Clara",
        "Hay algo que quiero preguntarte",
        "Sé que apenas nos estamos conociendo, y eso es justo lo que me parece bonito. "
        "Quiero que nuestra primera salida sea algo tuyo, algo que te haga sentir cómoda "
        "y con ganas de estar ahí. ¿Me dejas preguntarte unas cositas?"
    )

    st.markdown('<span class="q-label">¿Te animarías a salir conmigo un día de estos?</span>', unsafe_allow_html=True)

    respuesta = st.radio(
        label="respuesta_principal",
        options=["Sí, me gustaría mucho 🌷", "Necesito pensarlo un poco 🌿"],
        label_visibility="collapsed",
    )

    st.write("")
    if st.button("Continuar →"):
        st.session_state.datos["respuesta"] = respuesta
        if "Sí" in respuesta:
            st.session_state.pantalla = "formulario"
        else:
            st.session_state.pantalla = "soft_no"
        st.rerun()


# ════════════════════════════════════════════════════════════════════════════════
# PANTALLA 2 — Soft No
# ════════════════════════════════════════════════════════════════════════════════
elif st.session_state.pantalla == "soft_no":

    abrir_card("Sin prisa", "Está bien, no hay apuro")

    st.markdown("""
    <div class="soft-quote">
      "Las cosas bonitas no se apresuran,<br>
      simplemente llegan cuando deben llegar."
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align:center; color:var(--muted); font-size:0.92rem; line-height:1.8; margin-top:1rem;">
      Si en algún momento cambias de opinión, aquí estaré.<br>
      Y si no, también está bien. Gracias por tu honestidad 🌸
    </p>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("← Quiero cambiar mi respuesta"):
        st.session_state.pantalla = "landing"
        st.rerun()


# ════════════════════════════════════════════════════════════════════════════════
# PANTALLA 3 — Formulario
# ════════════════════════════════════════════════════════════════════════════════
elif st.session_state.pantalla == "formulario":

    abrir_card(
        "Cuéntame un poco",
        "Ayúdame a hacer algo pensado en ti",
        "No hay respuestas malas, solo quiero que el plan te guste de verdad."
    )

    # Pregunta 1 — Comida
    st.markdown('<span class="q-label">¿Qué tipo de comida disfrutas más?</span>', unsafe_allow_html=True)
    comida = st.selectbox(
        label="comida",
        options=[
            "Elige lo que más te llame...",
            "Italiana — pasta, pizza, sabores que abrazan 🍝",
            "Japonesa / Asiática — algo fresco y delicado 🍣",
            "Hamburguesas o tacos — sin pretensiones y rico 🍔",
            "Café y algo dulce — mi tipo favorito de plan ☕",
            "Sorpréndeme — confío en tu criterio ✨",
        ],
        label_visibility="collapsed",
    )

    st.write("")

    # Pregunta 2 — Bebida
    st.markdown('<span class="q-label">¿Y para tomar, qué prefieres?</span>', unsafe_allow_html=True)
    bebida = st.selectbox(
        label="bebida",
        options=[
            "Lo que más te apetezca...",
            "Algo con espíritu — cócteles o vino 🍹",
            "Una buena cerveza artesanal 🍺",
            "Café, té, o algo calentito ☕",
            "Jugos naturales o agua — me gusta mantenerme fresca 🥤",
        ],
        label_visibility="collapsed",
    )

    st.write("")

    # Pregunta 3 — Ambiente
    st.markdown('<span class="q-label">¿Cómo imaginas el ambiente ideal?</span>', unsafe_allow_html=True)
    ambiente = st.radio(
        label="ambiente",
        options=[
            "Tranquilo, para conversar sin prisa 🛋️",
            "Con música de fondo y buen ambiente 🎵",
            "Al aire libre, que corra el viento 🌳",
        ],
        label_visibility="collapsed",
    )

    st.write("")

    # Pregunta 4 — Fecha
    st.markdown('<span class="q-label">¿Qué día podrías estar disponible?</span>', unsafe_allow_html=True)
    st.markdown('<span class="q-sub">Elige la fecha que mejor te quede, lo organizamos con tiempo.</span>', unsafe_allow_html=True)
    fecha = st.date_input(
        label="fecha",
        value=date.today() + timedelta(days=7),
        min_value=date.today() + timedelta(days=1),
        max_value=date.today() + timedelta(days=90),
        format="DD/MM/YYYY",
        label_visibility="collapsed",
    )

    st.write("")

    # Pregunta 5 — Nota
    st.markdown('<span class="q-label">¿Hay algo que deba saber?</span>', unsafe_allow_html=True)
    st.markdown('<span class="q-sub">Alergias, cosas que no te gusten, cualquier detalle es bienvenido.</span>', unsafe_allow_html=True)
    nota = st.text_input(
        label="nota",
        placeholder="Opcional, pero lo tendré muy en cuenta...",
        label_visibility="collapsed",
    )

    st.write("")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("Ver mi plan antes de enviar →"):
            if comida == "Elige lo que más te llame..." or bebida == "Lo que más te apetezca...":
                st.warning("Cuéntame un poquito más antes de continuar 🌷")
            else:
                meses = {
                    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
                    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
                    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
                }
                dias_semana = {
                    0: "lunes", 1: "martes", 2: "miércoles", 3: "jueves",
                    4: "viernes", 5: "sábado", 6: "domingo"
                }
                fecha_fmt = f"{dias_semana[fecha.weekday()]} {fecha.day} de {meses[fecha.month]}"

                st.session_state.datos.update({
                    "comida": comida,
                    "bebida": bebida,
                    "ambiente": ambiente,
                    "fecha": fecha_fmt,
                    "nota": nota if nota else "Ninguna en especial",
                })
                st.session_state.pantalla = "confirmar"
                st.rerun()
    with col2:
        if st.button("← Volver"):
            st.session_state.pantalla = "landing"
            st.rerun()


# ════════════════════════════════════════════════════════════════════════════════
# PANTALLA 4 — Confirmación
# ════════════════════════════════════════════════════════════════════════════════
elif st.session_state.pantalla == "confirmar":

    d = st.session_state.datos

    st.markdown("""
    <div style="text-align:center; font-size:2rem; margin-bottom:1rem;
         animation: pulse 2s ease-in-out infinite;">🌸</div>
    <style>
    @keyframes pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.1); }
    }
    </style>
    """, unsafe_allow_html=True)

    abrir_card(
        "Ya tengo el plan",
        "Hecho especialmente para ti",
        "Así quedó tu elección. Si quieres ajustar algo, puedes volver. "
        "Si todo está bien, solo envíamelo y empezamos a planear."
    )

    st.markdown(f"""
    <div class="summary-box">
      <div class="summary-row">
        <span class="summary-key">Comida</span>
        <span>{d.get('comida','')}</span>
      </div>
      <div class="summary-row">
        <span class="summary-key">Bebida</span>
        <span>{d.get('bebida','')}</span>
      </div>
      <div class="summary-row">
        <span class="summary-key">Ambiente</span>
        <span>{d.get('ambiente','')}</span>
      </div>
      <div class="summary-row">
        <span class="summary-key">Fecha</span>
        <span>{d.get('fecha','')}</span>
      </div>
      <div class="summary-row">
        <span class="summary-key">Nota</span>
        <span>{d.get('nota','')}</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Construir mensaje de WhatsApp
    mensaje = (
        f"¡Hola! Aquí va mi plan ideal para nuestra cita 🌸\n\n"
        f"🍽️ Comida: {d.get('comida','')}\n"
        f"🥂 Bebida: {d.get('bebida','')}\n"
        f"🌿 Ambiente: {d.get('ambiente','')}\n"
        f"📅 Fecha: {d.get('fecha','')}\n"
        f"📝 Nota: {d.get('nota','Ninguna')}"
    )
    url_wa = f"https://wa.me/{TELEFONO}?text={urllib.parse.quote(mensaje)}"

    st.link_button("💬 Enviar por WhatsApp", url_wa)

    st.write("")
    if st.button("← Quiero ajustar algo"):
        st.session_state.pantalla = "formulario"
        st.rerun()
