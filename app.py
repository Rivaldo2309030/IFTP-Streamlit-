import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

# --- CONFIGURACIÓN DE LA APP ---
st.set_page_config(page_title="Kool-Box Ecosystem", page_icon="🌱", layout="wide")

# ==========================================
# 🎨 CSS AJUSTADO PARA LEGIBILIDAD
# ==========================================
# Se cambió el fondo blanco (#ffffff) de .sensor-card por gris oscuro (#262730)
# y se forzó el color del texto a blanco (#ffffff) para evitar saturación.
st.markdown("""
<style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .kpi-card { background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 10px;}
    
    /* Tarjetas de sensores con fondo oscuro y texto claro (NOM-004) */
    .sensor-card { 
        background-color: #262730; 
        color: #ffffff; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #41444C; 
        text-align: center; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Ajuste de color para los labels de los sensores */
    .sensor-card h3, .sensor-card p {
        color: #ffffff;
        margin: 0;
    }
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
# PESTAÑA 1: MERCADO (TABLA HISTÓRICA)
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
    st.markdown("### 📋 Tabla Histórica de Precios (2021 - 2026)")
    st.write("Selecciona un cultivo para ver el registro detallado de precios.")
    
    # Botones de selección rápida
    cultivo_seleccionado = st.radio(
        "Filtro de Cultivo:", 
        ["🌶️ Chile Habanero", "🍈 Papaya Maradol", "🍅 Tomate Saladette"], 
        horizontal=True
    )
    
    # Generador de datos de prueba (Simulación de 5 años por meses)
    fechas_historicas = pd.date_range(start="2021-01-01", end="2026-02-01", freq="ME")
    
    if "Chile Habanero" in cultivo_seleccionado:
        precios = np.linspace(35, 55, len(fechas_historicas)) + np.random.normal(0, 3, len(fechas_historicas))
    elif "Papaya Maradol" in cultivo_seleccionado:
        precios = np.linspace(15, 18, len(fechas_historicas)) + np.random.normal(0, 1.5, len(fechas_historicas))
    else:
        precios = np.linspace(18, 22, len(fechas_historicas)) + np.random.normal(0, 2, len(fechas_historicas))
        
    # Crear DataFrame con formato de tabla
    df_historico_tabla = pd.DataFrame({
        'Fecha (Mes/Año)': fechas_historicas.strftime("%b-%Y"),
        'Precio Promedio (MXN)': precios.round(2)
    })
    
    # MOSTRAR TABLA INTERACTIVA EN LUGAR DE GRÁFICA
    st.markdown(f"**Registro mensual de precios para {cultivo_seleccionado.split(' ')[1]}**")
    st.dataframe(
        df_historico_tabla, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "Precio Promedio (MXN)": st.column_config.NumberColumn(format="$%.2f")
        }
    )

    st.divider()
    
    # Calculadora rápida
    st.markdown("#### 🧮 Calculadora de Trato Justo")
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        kilos = st.number_input(f"¿Cuántos kilos vas a vender?", min_value=10, value=50, step=10)
        precio_actual_calc = df_historico_tabla['Precio Promedio (MXN)'].iloc[-1]
    
    with col_b:
        st.markdown(f"<div style='margin-top:28px'></div>", unsafe_allow_html=True) # Espaciado
        if st.button("💰 Calcular pago justo"):
            st.success(f"**Exige:** ${kilos * precio_actual_calc:,.2f} MXN")

# ==========================================
# PESTAÑA 2: REPORTE DEL HUERTO (COLOR CORREGIDO)
# ==========================================
with tab_calidad:
    st.subheader("Sincronización con Sensores Kool-Box")
    st.write("Escribe el PIN de 4 dígitos para desempaquetar el reporte de tu cosecha.")
    st.info("💡 **Tips:** Prueba con **95A2** (Excelente) o **60X1** (Problemas de riego).")
    
    col_pin, col_vacio = st.columns([1, 2])
    with col_pin:
        codigo_usuario = st.text_input("Ingresa tu PIN:", max_chars=4).upper()
        
    if codigo_usuario:
        st.divider()
        # SECCIÓN CORREGIDA: FONDO OSCURO EN LAS TARJETAS
        if codigo_usuario == "95A2":
            st.balloons()
            st.success("✅ **Sincronización Exitosa: Cosecha Grado A (Premium)**")
            
            st.markdown("### 📊 Parámetros de tu Cosecha")
            st.write("Tu Arduino registró las siguientes condiciones promedio:")
            
            c1, c2, c3, c4 = st.columns(4)
            # Fondo gris oscuro (#262730), texto blanco garantizado
            with c1:
                st.markdown("<div class='sensor-card'><h3>💧 78%</h3><p>Humedad del Suelo</p><span style='color:#69f0ae;font-weight:bold'>Óptimo</span></div>", unsafe_allow_html=True)
            with c2:
                st.markdown("<div class='sensor-card'><h3>🧪 6.8</h3><p>Nivel de pH</p><span style='color:#69f0ae;font-weight:bold'>Ideal</span></div>", unsafe_allow_html=True)
            with c3:
                st.markdown("<div class='sensor-card'><h3>🌡️ 24°C</h3><p>Temperatura</p><span style='color:#69f0ae;font-weight:bold'>Estable</span></div>", unsafe_allow_html=True)
            with c4:
                st.markdown("<div class='sensor-card'><h3>☀️ 85%</h3><p>Exposición Solar</p><span style='color:#69f0ae;font-weight:bold'>Suficiente</span></div>", unsafe_allow_html=True)
                
            st.write("")
            st.progress(0.95, text="Cumplimiento de la Norma NOM-004")
            st.download_button("📄 Descargar Certificado", data="Certificado Grado A", file_name="Cert_A.txt")

        elif codigo_usuario == "60X1":
            st.warning("⚠️ **Sincronización Exitosa: Cosecha Grado C (Atención)**")
            
            st.markdown("### 📊 Parámetros de tu Cosecha")
            st.write("Se detectaron anomalías en el campo.")
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown("<div class='sensor-card'><h3>💧 45%</h3><p>Humedad</p><span style='color:#ff5252;font-weight:bold'>Muy Seco</span></div>", unsafe_allow_html=True)
            with c2:
                st.markdown("<div class='sensor-card'><h3>🧪 5.2</h3><p>pH</p><span style='color:#ffab40;font-weight:bold'>Ácido</span></div>", unsafe_allow_html=True)
            with c3:
                st.markdown("<div class='sensor-card'><h3>🌡️ 32°C</h3><p>Temperatura</p><span style='color:#ff5252;font-weight:bold'>Alta</span></div>", unsafe_allow_html=True)
            with c4:
                st.markdown("<div class='sensor-card'><h3>☀️ 90%</h3><p>Luz Solar</p><span style='color:#69f0ae;font-weight:bold'>Suficiente</span></div>", unsafe_allow_html=True)
                
            st.write("")
            st.progress(0.60, text="Cumplimiento parcial (60%)")
            
        else:
            st.error("❌ Código no reconocido.")

# ==========================================
# PESTAÑA 3: CATÁLOGO
# ==========================================
with tab_tienda:
    st.subheader("Mejora tu infraestructura paso a paso")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("💧 **Nivel 2: Riego Automático ($3,500 MXN)**\n\nAgrega electroválvulas a tu Arduino.")
        st.button("Cotizar Nivel 2", key="ctg1")
    with col_b:
        st.warning("☀️ **Nivel 3: Off-Grid ($6,000 MXN)**\n\nPanel solar y batería.")
        st.button("Cotizar Nivel 3", key="ctg2")
