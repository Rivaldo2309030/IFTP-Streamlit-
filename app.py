import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

# --- CONFIGURACIÓN DE LA APP ---
st.set_page_config(page_title="Kool-Box Ecosystem", page_icon="🌱", layout="wide")

# CSS para ocultar menús y mejorar el diseño visual
st.markdown("""
<style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .kpi-card { background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 10px;}
    .sensor-card { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
</style>
""", unsafe_allow_html=True)

st.title("🌱 Kool-Box: Inteligencia Agrícola")
st.markdown("Integración Total: Del campo automatizado al mercado digital en Yucatán.")

# ==========================================
# PESTAÑAS PRINCIPALES
# ==========================================
tab_mercado, tab_calidad, tab_tienda = st.tabs([
    "📈 Mercado y Tendencias", 
    "🏅 Reporte de mi Huerto", 
    "🛒 Catálogo Kool-Box"
])

# ==========================================
# PESTAÑA 1: MERCADO Y TENDENCIAS HISTÓRICAS
# ==========================================
with tab_mercado:
    st.subheader("Análisis de Precios (Central de Abastos Mérida)")
    
    # KPIs de hoy
    col1, col2, col3 = st.columns(3)
    col1.metric("🌶️ Chile Habanero", "$55.50 /kg", "+$2.50 (Sube)")
    col2.metric("🍈 Papaya Maradol", "$18.20 /kg", "-$0.50 (Baja)")
    col3.metric("🍅 Tomate Saladette", "$22.00 /kg", "Estable")
    
    st.divider()
    
    # INTERACCIÓN: Botones para historial de años
    st.markdown("### 📊 Comportamiento Histórico (2021 - 2026)")
    st.write("Selecciona un cultivo para ver cómo ha cambiado su precio en los últimos 5 años.")
    
    # Botones de selección rápida (Radio horizontal simula botones)
    cultivo_seleccionado = st.radio(
        "Filtro de Cultivo:", 
        ["🌶️ Chile Habanero", "🍈 Papaya Maradol", "🍅 Tomate Saladette"], 
        horizontal=True
    )
    
    # Generador de datos de prueba (Simulación de 5 años por meses)
    fechas_historicas = pd.date_range(start="2021-01-01", end="2026-02-01", freq="ME")
    
    if cultivo_seleccionado == "🌶️ Chile Habanero":
        # Simulamos que el habanero ha subido mucho por sequías
        precios = np.linspace(35, 55, len(fechas_historicas)) + np.random.normal(0, 3, len(fechas_historicas))
    elif cultivo_seleccionado == "🍈 Papaya Maradol":
        precios = np.linspace(15, 18, len(fechas_historicas)) + np.random.normal(0, 1.5, len(fechas_historicas))
    else:
        precios = np.linspace(18, 22, len(fechas_historicas)) + np.random.normal(0, 2, len(fechas_historicas))
        
    df_historico = pd.DataFrame({'Precio (MXN)': precios}, index=fechas_historicas)
    
    # Mostramos la gráfica interactiva
    st.line_chart(df_historico, color="#2e7d32")

    st.divider()
    
    # Calculadora rápida
    st.markdown("#### 🧮 Calculadora de Trato Justo")
    kilos = st.number_input(f"¿Cuántos kilos de {cultivo_seleccionado.split(' ')[1]} vas a vender?", min_value=10, value=50, step=10)
    precio_actual = df_historico['Precio (MXN)'].iloc[-1]
    st.success(f"**💰 Exige al comprador:** ${kilos * precio_actual:,.2f} MXN")

# ==========================================
# PESTAÑA 2: REPORTE DEL HUERTO (EL PIN DEL ARDUINO)
# ==========================================
with tab_calidad:
    st.subheader("Sincronización con Sensores Kool-Box")
    st.write("Escribe el PIN de 4 dígitos que generó tu sistema en el campo para desempaquetar el reporte de tu cosecha.")
    
    st.info("💡 **Tips para el Jurado:** Prueba con **95A2** (Cosecha Excelente) o **60X1** (Cosecha con problemas de riego).")
    
    col_pin, col_vacio = st.columns([1, 2])
    with col_pin:
        codigo_usuario = st.text_input("Ingresa tu PIN:", max_chars=4).upper()
        
    if codigo_usuario:
        st.divider()
        if codigo_usuario == "95A2":
            st.balloons()
            st.success("✅ **Sincronización Exitosa: Cosecha Grado A (Premium)**")
            
            # DASHBOARD AMIGABLE DE SENSORES
            st.markdown("### 📊 Parámetros de tu Cosecha")
            st.write("Tu Arduino registró las siguientes condiciones promedio durante el ciclo:")
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown("<div class='sensor-card'><h3>💧 78%</h3><p>Humedad del Suelo</p><span style='color:green'>Óptimo</span></div>", unsafe_allow_html=True)
            with c2:
                st.markdown("<div class='sensor-card'><h3>🧪 6.8</h3><p>Nivel de pH</p><span style='color:green'>Neutro/Ideal</span></div>", unsafe_allow_html=True)
            with c3:
                st.markdown("<div class='sensor-card'><h3>🌡️ 24°C</h3><p>Temperatura Promedio</p><span style='color:green'>Estable</span></div>", unsafe_allow_html=True)
            with c4:
                st.markdown("<div class='sensor-card'><h3>☀️ 85%</h3><p>Exposición Solar</p><span style='color:green'>Suficiente</span></div>", unsafe_allow_html=True)
                
            st.write("")
            st.progress(0.95, text="Cumplimiento de la Norma NOM-004")
            
            st.download_button(
                label="📄 Descargar Certificado de Calidad (PDF)",
                data="Simulacion de Certificado Grado A. Listo para venta en Central de Abastos.",
                file_name="Certificado_KoolBox.txt",
                mime="text/plain"
            )

        elif codigo_usuario == "60X1":
            st.warning("⚠️ **Sincronización Exitosa: Cosecha Grado C (Atención Requerida)**")
            
            st.markdown("### 📊 Parámetros de tu Cosecha")
            st.write("Se detectaron anomalías en el campo. Revisa tu sistema de riego.")
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown("<div class='sensor-card'><h3>💧 45%</h3><p>Humedad del Suelo</p><span style='color:red'>Muy Seco</span></div>", unsafe_allow_html=True)
            with c2:
                st.markdown("<div class='sensor-card'><h3>🧪 5.2</h3><p>Nivel de pH</p><span style='color:orange'>Ácido</span></div>", unsafe_allow_html=True)
            with c3:
                st.markdown("<div class='sensor-card'><h3>🌡️ 32°C</h3><p>Temperatura Promedio</p><span style='color:red'>Alta</span></div>", unsafe_allow_html=True)
            with c4:
                st.markdown("<div class='sensor-card'><h3>☀️ 90%</h3><p>Exposición Solar</p><span style='color:green'>Suficiente</span></div>", unsafe_allow_html=True)
                
            st.write("")
            st.progress(0.60, text="Cumplimiento parcial de la Norma NOM-004")
            
        else:
            st.error("❌ Código no reconocido. Verifica la pantalla de tu Arduino.")

# ==========================================
# PESTAÑA 3: CATÁLOGO
# ==========================================
with tab_tienda:
    st.subheader("Mejora tu infraestructura paso a paso")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("💧 **Nivel 2: Riego Automático ($3,500 MXN)**\n\nAgrega electroválvulas a tu Arduino. Olvídate de regar a mano.")
        st.button("Cotizar Nivel 2")
    with col_b:
        st.warning("☀️ **Nivel 3: Off-Grid ($6,000 MXN)**\n\nPanel solar y batería. Tu huerto funcionará sin pagar electricidad.")
        st.button("Cotizar Nivel 3")
