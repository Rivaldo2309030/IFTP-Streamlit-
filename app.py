import streamlit as st
import pandas as pd
import numpy as np
from datetime import timedelta, date

# --- CONFIGURACIÓN DE LA APP ---
st.set_page_config(page_title="Kool-Box Ecosystem", page_icon="🌱", layout="wide")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .kpi-card { background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; }
</style>
""", unsafe_allow_html=True)

st.title("🌱 Kool-Box: Ecosistema Inteligente")
st.markdown("Integración Total: Del campo automatizado al mercado digital.")

tab_mercado, tab_calidad, tab_mapa, tab_tienda = st.tabs([
    "📈 Inteligencia de Mercado", 
    "🏅 Auditoría de Calidad", 
    "📍 Puntos de Venta",
    "🛒 Escalabilidad"
])

# ==========================================
# PESTAÑA 1: MERCADO Y PROYECCIONES
# ==========================================
with tab_mercado:
    st.subheader("Análisis de Precios (Mérida, Yucatán)")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🌶️ Chile Habanero", "$55.50", "Tendencia a la alta")
    col2.metric("🍈 Papaya Maradol", "$18.20", "-$0.50 (Baja demanda)")
    col3.metric("🍅 Tomate Saladette", "$22.00", "Estable")
    
    st.divider()
    
    col_chart, col_calc = st.columns([2, 1])
    
    with col_chart:
        st.markdown("**Predicción Semanal (Simulación de Modelo Predictivo)**")
        # Datos simulados con proyección futura
        fechas = pd.date_range(start=date.today() - timedelta(days=4), periods=10)
        datos_ia = pd.DataFrame({
            'Chile Habanero (Histórico + Predicción)': [51, 52, 53, 55.5, 55.5, 56.5, 58.0, 59.5, 60.0, 61.5],
            'Límite de Riesgo': [45]*10
        }, index=fechas)
        st.area_chart(datos_ia)

    with col_calc:
        st.markdown("<div class='kpi-card'>", unsafe_allow_html=True)
        st.markdown("#### 🧮 Calculadora de Trato Justo")
        kilos = st.number_input("Kilos de Habanero a vender:", min_value=10, value=50, step=10)
        st.success(f"**Exige al intermediario:**\n# ${kilos * 55.50:,.2f} MXN")
        st.caption("Basado en el precio actual de $55.50/kg")
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PESTAÑA 2: AUDITORÍA DE CALIDAD (EL PUENTE CON ARDUINO)
# ==========================================
with tab_calidad:
    st.subheader("Sincronización con tu Hardware Kool-Box")
    st.write("Tu Arduino cuidó tus plantas. Ahora valida ese esfuerzo.")
    
    col_pin, col_result = st.columns([1, 2])
    
    with col_pin:
        codigo_usuario = st.text_input("Ingresa el PIN de la pantalla LCD:", max_chars=4, help="Usa el código 95A2 para la demo")
        validar = st.button("Validar Registro de Sensores", use_container_width=True)
        
    with col_result:
        if validar and codigo_usuario:
            if codigo_usuario.upper() == "95A2":
                st.balloons()
                st.success("✅ **Sincronización Exitosa: Score 95%**")
                st.progress(0.95)
                st.write("Los registros del Arduino confirman que la humedad del suelo se mantuvo en el rango óptimo (60%-80%) durante todo el ciclo de cultivo.")
                
                # Simulación de descarga de documento
                st.download_button(
                    label="📄 Descargar Certificado NOM-004 (PDF)",
                    data="Simulacion de datos de validacion. El producto es Grado A.",
                    file_name="KoolBox_Certificado_Calidad.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            else:
                st.error("❌ Código no reconocido. Intenta con 95A2 para la demostración.")

# ==========================================
# PESTAÑA 3: GEOLOCALIZACIÓN
# ==========================================
with tab_mapa:
    st.subheader("📍 Puntos de Venta Estratégicos")
    st.write("¿No quieres usar intermediarios? Lleva tu producto directamente a estos mercados de alta demanda.")
    
    # Coordenadas de Mérida (Central de Abastos y Lucas de Gálvez)
    mercados = pd.DataFrame({
        'lat': [20.9576, 20.9634, 20.9850],
        'lon': [-89.6542, -89.6225, -89.6150],
        'Mercado': ["Central de Abastos", "Mercado Lucas de Gálvez", "Mercado Alemán"]
    })
    
    st.map(mercados, zoom=12)
    st.caption("Puntos rojos: Mercados con déficit de Chile Habanero reportado hoy.")

# ==========================================
# PESTAÑA 4: CATÁLOGO
# ==========================================
with tab_tienda:
    st.subheader("Crece tu infraestructura paso a paso")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("💧 **Nivel 2: Riego Automático ($3,500 MXN)**\n\nAgrega electroválvulas a tu Arduino. Olvídate de regar a mano.")
        st.button("Cotizar Nivel 2")
    with col_b:
        st.warning("☀️ **Nivel 3: Off-Grid ($6,000 MXN)**\n\nPanel solar y batería. Tu huerto funcionará sin pagar electricidad.")
        st.button("Cotizar Nivel 3")
