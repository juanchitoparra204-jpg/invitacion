import streamlit as st
import urllib.parse

# Configuración de la página (Título en la pestaña del navegador)
st.set_page_config(page_title="Invitación Especial ✨", page_icon="💌", layout="centered")

# --- ESTILOS PERSONALIZADOS (Para darle un toque tierno) ---
st.markdown("""
    <style>
    .main { background-color: #FFF5F5; }
    h1 { color: #D32F2F; text-align: center; }
    .stButton>button { background-color: #FF4B4B; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIO DE LA TARJETA ---
st.title("✨ Una invitación para alguien especial ✨")
st.write("Hola. Como todavía no hemos hablado muchísimo, quería preparar algo diferente para nuestra primera cita. ¡Ayúdame a armar el plan perfecto respondiendo esto!")

st.write("---")

# 1. La pregunta del millón
cita = st.radio("¿Te animas a salir conmigo a tomar o comer algo? 🫣", 
                ("¡Sí, de una! 🚀", "Mmm, déjame pensarlo... 🤔"))

if cita == "¡Sí, de una! 🚀":
    st.balloons() # ¡Efecto de globos en la pantalla!
    st.subheader("🥳 ¡Buenísimo! Ahora, configuremos el plan ideal:")
    
    # 2. Cuestionario dinámico de gustos
    comida = st.selectbox("1. ¿Qué tipo de comida te hace más feliz? 🍽️", 
                         ["Italiana (Pasta/Pizza) 🍝", 
                          "Sushi / Comida Asiática 🍣", 
                          "Hamburguesas / Tacos 🍔🌮", 
                          "Algo ligero (Café y postre) ☕🍰", 
                          "¡Sorpréndeme! Me gusta todo ✨"])
    
    bebida = st.selectbox("2. ¿Qué prefieres para tomar? 🍹", 
                         ["Cócteles / Tragos coquetos 🍹", 
                          "Una buena cerveza 🍺", 
                          "Una copa de vino 🍷", 
                          "Café / Té / Frappé ☕", 
                          "Agua / Jugo natural 🥤"])
                         
    ambiente = st.radio("3. ¿Qué tipo de plan prefieres para ese día? 🗺️", 
                        ("Tranquilo para charlar bastante 🛋️", 
                         "Algo con música de fondo o más movido 🎵", 
                         "Un plan al aire libre 🌳"))
    
    restricciones = st.text_input("4. ¿Hay algo que NO te guste o alguna alergia? (Opcional) ⚠️")

    st.write("---")
    st.write("✨ **¡Todo listo!** Para confirmarme, dale clic al botón de abajo. Se abrirá tu WhatsApp con las respuestas listas para enviármelas.")

    # --- CONFIGURACIÓN DEL MENSAJE DE WHATSAPP ---
    # REEMPLAZA ESTE NÚMERO POR EL TUYO (Incluye el código de tu país, ej: 57 para Colombia, 34 para España, 52 para México)
    tu_telefono = "573000000000" 
    
    mensaje_final = (
        f"¡Hola! Ya armé mi cita ideal 💌:\n\n"
        f"🍕 Comida: {comida}\n"
        f"🍹 Bebida: {bebida}\n"
        f"🛋️ Mood: {ambiente}\n"
        f"🚫 Nota: {restricciones if restricciones else '¡Ninguna!'}"
    )
    
    # Codificar el texto para que sea válido en un enlace web
    mensaje_codificado = urllib.parse.quote(mensaje_final)
    url_whatsapp = f"https://wa.me/{tu_telefono}?text={mensaje_codificado}"
    
    # Botón final de envío
    st.link_button("💌 Enviar mis respuestas por WhatsApp", url_whatsapp)

else:
    st.write("¡Prometo que habrá buena comida, gran conversación y cero presiones! 😉 Piénsalo y, si te convences, cambia tu respuesta arriba.")