import streamlit as st
import pandas as pd
import numpy as np
from datetime import timedelta, date

# --- CONFIGURACIÓN DE LA APP ---
st.set_page_config(page_title="Kool-Box Portal", page_icon="🌱", layout="centered")

# --- CSS PARA DISEÑO DE APP MÓVIL ---
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding-top: 2rem; padding-bottom: 0rem; }
    .catalogo-card {
        background-color: #ffffff; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px;
        border-left: 5px solid #2e7d32;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #2e7d32;'>🌱 Kool-Box</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Tu aliado para precios justos en Yucatán.</p>", unsafe_allow_html=True)

# ==========================================
# CREACIÓN DE PESTAÑAS (TABS)
# ==========================================
tab_precios, tab_calidad, tab_catalogo = st.tabs(["📊 Mercado", "🏅 Calidad", "🛒 Tienda"])

# ==========================================
# PESTAÑA 1: PRECIOS, GRÁFICAS Y CALCULADORA
# ==========================================
with tab_precios:
    st.markdown("### 📈 Tendencias de Hoy (Mérida)")
    
    # 1. TARJETAS DE MÉTRICAS (KPIs con Deltas)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="🌶️ Chile Habanero", value="$55.50", delta="+$2.50 vs ayer")
    col2.metric(label="🍈 Papaya Maradol", value="$18.20", delta="-$0.80 vs ayer", delta_color="inverse")
    col3.metric(label="🍅 Tomate Saladette", value="$22.00", delta="Estable", delta_color="off")
    
    st.divider()

    # 2. GRÁFICA INTERACTIVA DE HISTORIAL (Generación de datos realistas)
    st.markdown("### 📊 Historial de la semana")
    st.write("Mira cómo se ha movido el mercado en los últimos 7 días.")
    
    # Generar fechas de los últimos 7 días
    hoy = date.today()
    fechas = [(hoy - timedelta(days=i)).strftime("%d %b") for i in range(6, -1, -1)]
    
    # Datos de tendencia (Simulados de forma realista)
    datos_grafica = pd.DataFrame({
        'Chile Habanero': [48.0, 49.5, 51.0, 50.0, 52.5, 53.0, 55.5],
        'Tomate Saladette': [21.5, 22.0, 22.5, 22.0, 21.5, 22.0, 22.0]
    }, index=fechas)
    
    st.line_chart(datos_grafica)

    st.divider()
    
    # 3. CALCULADORA INTERACTIVA
    st.markdown("### 🧮 Calcula tu venta")
    productos = ["Chile Habanero", "Papaya Maradol", "Tomate Saladette"]
    precios = [55.50, 18.20, 22.00]
    df_precios = pd.DataFrame({"Producto": productos, "Precio": precios})
    
    col_a, col_b = st.columns(2)
    with col_a:
        producto_elegido = st.selectbox("¿Qué vendes?", productos)
    with col_b:
        kilos = st.number_input("¿Kilos a vender?", min_value=1, value=50)
    
    precio_actual = df_precios[df_precios['Producto'] == producto_elegido]['Precio'].values[0]
    ganancia_total = kilos * precio_actual
    
    if st.button("💰 Calcular pago justo", use_container_width=True):
        st.success(f"Por {kilos}kg de {producto_elegido}, debes recibir: **${ganancia_total:,.2f} MXN**")

# ==========================================
# PESTAÑA 2: VALIDACIÓN CON BARRA DE PROGRESO
# ==========================================
with tab_calidad:
    st.markdown("### 🏅 Valida tu Cosecha")
    st.info("💡 Ingresa el código **95A2** para probar el sistema.")
    codigo_usuario = st.text_input("Ingresa el PIN de tu Kool-Box:", max_chars=4)

    if codigo_usuario:
        if len(codigo_usuario) == 4 and codigo_usuario[1:3].isdigit():
            final_score = int(codigo_usuario[1:3])
            st.write("---")
            
            # Barra de progreso visual
            st.write("**Nivel de cumplimiento NOM-004:**")
            st.progress(final_score / 100.0)
            
            if final_score > 90:
                st.balloons()
                st.success(f"🥇 **CALIDAD PREMIUM ({final_score}%)**")
                st.write("Humedad perfecta. Tienes poder para negociar el precio máximo.")
            elif final_score > 70:
                st.info(f"🥈 **CALIDAD ESTÁNDAR ({final_score}%)**")
            else:
                st.warning(f"🥉 **ATENCIÓN ({final_score}%)**")
        else:
            st.error("❌ PIN inválido.")

# ==========================================
# PESTAÑA 3: CATÁLOGO DE UPGRADES
# ==========================================
with tab_catalogo:
    st.markdown("### 🛒 Mejora tu Producción")
    
    if 'producto_seleccionado' not in st.session_state:
        st.session_state['producto_seleccionado'] = None

    # Tarjeta 1
    st.markdown("""
    <div class="catalogo-card">
        <h4 style="margin-top:0;">🌱 Nivel 1: Kool-Box Base ($1,500)</h4>
        <p>Monitoreo offline de humedad y temperatura.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Adquirir Nivel 1", key="btn1"):
        st.session_state['producto_seleccionado'] = "Kool-Box Base"

    # Tarjeta 2
    st.markdown("""
    <div class="catalogo-card">
        <h4 style="margin-top:0;">💧 Nivel 2: Riego Inteligente ($3,500)</h4>
        <p>Válvulas automáticas para regar solo cuando se necesita.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Adquirir Nivel 2", key="btn2"):
        st.session_state['producto_seleccionado'] = "Riego Inteligente"

    # Formulario de Compra
    if st.session_state['producto_seleccionado']:
        st.divider()
        st.markdown(f"### 📦 Finalizar Pedido: {st.session_state['producto_seleccionado']}")
        
        with st.form("formulario_compra"):
            nombre = st.text_input("Nombre completo")
            municipio = st.text_input("Municipio (Ej. Oxkutzcab)")
            submit = st.form_submit_button("Generar Orden de Compra", use_container_width=True)
            
            if submit:
                if nombre and municipio:
                    st.success(f"✅ ¡Pedido confirmado! Enviaremos tu equipo a {municipio}.")
                else:
                    st.error("⚠️ Por favor, llena tus datos.")
