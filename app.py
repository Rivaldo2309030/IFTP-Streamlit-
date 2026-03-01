import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

# --- CONFIGURACIÓN DE LA APP ---
st.set_page_config(page_title="Agri-core", page_icon="🌱", layout="wide")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .sensor-card { 
        background-color: #262730; color: #ffffff; padding: 15px; 
        border-radius: 10px; border: 1px solid #41444C; text-align: center; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 15px;
    }
    .sensor-card h3, .sensor-card p { color: #ffffff; margin: 0; }
</style>
""", unsafe_allow_html=True)

st.title("🌱 Agri-core: Inteligencia Agrícola")
st.markdown("Integración Total: Del campo automatizado al mercado digital en Yucatán.")

# --- DATOS BASE DEL MERCADO ---
precios_base = {
    "🌶️ Chile Habanero": 55.50,
    "🍈 Papaya Maradol": 18.20,
    "🍅 Tomate Saladette": 22.00
}

# ==========================================
# PESTAÑAS PRINCIPALES (Ahora son 4)
# ==========================================
tab_mercado, tab_calidad, tab_rutas, tab_tienda = st.tabs([
    "📈 Mercado y Tendencias", 
    "🏅 Reporte de mi Huerto", 
    "📍 Rutas de Venta",
    "🛒 Catálogo Kool-Box"
])

# ==========================================
# PESTAÑA 1: MERCADO (Solo Información)
# ==========================================
with tab_mercado:
    st.subheader("Análisis de Precios (Central de Abastos Mérida)")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🌶️ Chile Habanero", f"${precios_base['🌶️ Chile Habanero']} /kg", "+$2.50 (Sube)")
    col2.metric("🍈 Papaya Maradol", f"${precios_base['🍈 Papaya Maradol']} /kg", "-$0.50 (Baja)")
    col3.metric("🍅 Tomate Saladette", f"${precios_base['🍅 Tomate Saladette']} /kg", "Estable")
    
    st.divider()
    
    st.markdown("### 📋 Tabla Histórica de Precios (2021 - 2026)")
    cultivo_seleccionado = st.radio("Filtro de Cultivo:", list(precios_base.keys()), horizontal=True)
    
    fechas_historicas = pd.date_range(start="2021-01-01", end="2026-02-01", freq="ME")
    if "Habanero" in cultivo_seleccionado:
        precios = np.linspace(35, 55, len(fechas_historicas)) + np.random.normal(0, 3, len(fechas_historicas))
    elif "Papaya" in cultivo_seleccionado:
        precios = np.linspace(15, 18, len(fechas_historicas)) + np.random.normal(0, 1.5, len(fechas_historicas))
    else:
        precios = np.linspace(18, 22, len(fechas_historicas)) + np.random.normal(0, 2, len(fechas_historicas))
        
    df_historico_tabla = pd.DataFrame({
        'Fecha (Mes/Año)': fechas_historicas.strftime("%b-%Y"),
        'Precio Promedio (MXN)': precios.round(2)
    })
    
    st.dataframe(df_historico_tabla, use_container_width=True, hide_index=True,
                 column_config={"Precio Promedio (MXN)": st.column_config.NumberColumn(format="$%.2f")})

# ==========================================
# PESTAÑA 2: REPORTE DEL HUERTO Y CALCULADORA DINÁMICA
# ==========================================
with tab_calidad:
    st.subheader("Sincronización con Sensores Kool-Box")
    st.write("Escribe el PIN de 4 dígitos para desempaquetar tu reporte y calcular el valor de tu cosecha.")
    st.info("💡 **Tips para demo:** Usa **95A2** (Calidad Alta = +15% de valor) o **60X1** (Calidad Baja = -20% de penalización).")
    
    col_pin, col_vacio = st.columns([1, 2])
    with col_pin:
        codigo_usuario = st.text_input("Ingresa tu PIN:", max_chars=4).upper()
        
    if codigo_usuario:
        st.divider()
        
        # --- CASO 1: CALIDAD EXCELENTE ---
        if codigo_usuario == "95A2":
            st.balloons()
            st.success("✅ **Sincronización Exitosa: Cosecha Grado A (Premium)**")
            
            # --- NUEVO: TRAZABILIDAD DEL HUERTO ---
            st.markdown("#### 🧑‍🌾 Información del Productor")
            col_info1, col_info2, col_info3 = st.columns(3)
            col_info1.markdown("**👨‍🌾 Nombre:**<br>Don Julio", unsafe_allow_html=True)
            col_info2.markdown("**🏡 Unidad Productiva:**<br>Kool-Box Sur", unsafe_allow_html=True)
            col_info3.markdown("**📍 Ubicación:**<br>Mérida, Yucatán", unsafe_allow_html=True)
            st.write("") # Espaciador
            # --------------------------------------
            
            c1, c2, c3, c4 = st.columns(4)
            with c1: st.markdown("<div class='sensor-card'><h3>💧 78%</h3><p>Humedad</p><span style='color:#69f0ae;'>Óptimo</span></div>", unsafe_allow_html=True)
            with c2: st.markdown("<div class='sensor-card'><h3>🧪 6.8</h3><p>pH</p><span style='color:#69f0ae;'>Ideal</span></div>", unsafe_allow_html=True)
            with c3: st.markdown("<div class='sensor-card'><h3>🌡️ 24°C</h3><p>Temperatura</p><span style='color:#69f0ae;'>Estable</span></div>", unsafe_allow_html=True)
            with c4: st.markdown("<div class='sensor-card'><h3>☀️ 85%</h3><p>Luz Solar</p><span style='color:#69f0ae;'>Suficiente</span></div>", unsafe_allow_html=True)
            
            st.progress(0.95, text="Cumplimiento NOM-004 (95%)")
            
            # Calculadora dinámica para GRADO A (+15% de valor)
            st.markdown("### 🧮 Calculadora de Trato Justo (Precio Premium)")
            st.info("📈 Debido a que tus niveles de pH y Humedad fueron perfectos, tu producto vale un **15% MÁS** que el mercado regular.")
            
            col_calc1, col_calc2 = st.columns(2)
            with col_calc1:
                prod_vender = st.selectbox("¿Qué vas a vender?", list(precios_base.keys()), key="prod_a")
            with col_calc2:
                kilos_vender = st.number_input("¿Cuántos kilos?", min_value=10, value=50, step=10, key="kg_a")
                
            precio_mercado = precios_base[prod_vender]
            precio_premium = precio_mercado * 1.15
            total = precio_premium * kilos_vender
            
            st.success(f"**Valor de mercado:** ${precio_mercado:.2f}/kg | **Tu Valor Kool-Box:** ${precio_premium:.2f}/kg\n### 💰 Exige un total de: ${total:,.2f} MXN")

        # --- CASO 2: CALIDAD MALA ---
        elif codigo_usuario == "60X1":
            st.warning("⚠️ **Sincronización Exitosa: Cosecha Grado C (Atención)**")
            
            # --- NUEVO: TRAZABILIDAD DEL HUERTO ---
            st.markdown("#### 🧑‍🌾 Información del Productor")
            col_info1, col_info2, col_info3 = st.columns(3)
            col_info1.markdown("**👨‍🌾 Nombre:**<br>Don Roberto", unsafe_allow_html=True)
            col_info2.markdown("**🏡 Unidad Productiva:**<br>Parcela El Zapote", unsafe_allow_html=True)
            col_info3.markdown("**📍 Ubicación:**<br>Oxkutzcab, Yucatán", unsafe_allow_html=True)
            st.write("") # Espaciador
            # --------------------------------------
            
            c1, c2, c3, c4 = st.columns(4)
            with c1: st.markdown("<div class='sensor-card'><h3>💧 45%</h3><p>Humedad</p><span style='color:#ff5252;'>Muy Seco</span></div>", unsafe_allow_html=True)
            with c2: st.markdown("<div class='sensor-card'><h3>🧪 5.2</h3><p>pH</p><span style='color:#ffab40;'>Ácido</span></div>", unsafe_allow_html=True)
            with c3: st.markdown("<div class='sensor-card'><h3>🌡️ 32°C</h3><p>Temperatura</p><span style='color:#ff5252;'>Alta</span></div>", unsafe_allow_html=True)
            with c4: st.markdown("<div class='sensor-card'><h3>☀️ 90%</h3><p>Luz Solar</p><span style='color:#69f0ae;'>Suficiente</span></div>", unsafe_allow_html=True)
            
            st.progress(0.60, text="Cumplimiento NOM-004 (60%)")
            
            # Calculadora dinámica para GRADO C (-20% de valor)
            st.markdown("### 🧮 Calculadora de Trato Justo (Precio Penalizado)")
            st.error("📉 Debido a las anomalías de temperatura y humedad registradas por el Arduino, el comprador podría penalizar el precio de tu cosecha hasta un **20%**.")
            
            col_calc1, col_calc2 = st.columns(2)
            with col_calc1:
                prod_vender = st.selectbox("¿Qué vas a vender?", list(precios_base.keys()), key="prod_c")
            with col_calc2:
                kilos_vender = st.number_input("¿Cuántos kilos?", min_value=10, value=50, step=10, key="kg_c")
                
            precio_mercado = precios_base[prod_vender]
            precio_castigado = precio_mercado * 0.80
            total = precio_castigado * kilos_vender
            
            st.warning(f"**Valor de mercado:** ${precio_mercado:.2f}/kg | **Tu Valor Real:** ${precio_castigado:.2f}/kg\n### 💰 Prepárate para recibir aprox: ${total:,.2f} MXN")
            
        else:
            st.error("❌ Código no reconocido.")

# ==========================================
# PESTAÑA 3: RUTAS DE VENTA (MAPA)
# ==========================================
with tab_rutas:
    st.subheader("📍 Rutas de Mercado en Mérida")
    st.write("Encuentra los puntos de venta oficiales con mayor demanda hoy para evitar intermediarios abusivos.")
    
    # Coordenadas de mercados en Mérida
    mercados = pd.DataFrame({
        'lat': [20.9576, 20.9634, 20.9850, 20.9700],
        'lon': [-89.6542, -89.6225, -89.6150, -89.6300],
        'Mercado': ["Central de Abastos", "Mercado Lucas de Gálvez", "Mercado Alemán", "Mercado de San Benito"]
    })
    
    # Mostrar mapa
    st.map(mercados, zoom=12, color="#ff0000")
    
    st.info("📌 **Tip de ruta:** La *Central de Abastos* reporta hoy escasez de Chile Habanero. Llévalo directo ahí para maximizar tu ganancia.")

# ==========================================
# ==========================================
# PESTAÑA 4: CATÁLOGO Y SOPORTE (NUEVO)
# ==========================================
with tab_tienda:
    st.subheader("Mejora tu infraestructura paso a paso")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("💧 **Nivel 2: Riego Automático ($3,500 MXN)**\n\nAgrega electroválvulas a tu Arduino. Olvídate de regar a mano.")
        st.button("Cotizar Nivel 2", key="ctg1")
    with col_b:
        st.warning("☀️ **Nivel 3: Off-Grid ($6,000 MXN)**\n\nPanel solar y batería. Tu huerto funcionará sin electricidad de CFE.")
        st.button("Cotizar Nivel 3", key="ctg2")

    # --- NUEVO: SECCIÓN DE SOPORTE Y CONTACTO ---
    st.divider()
    st.subheader("📞 Soporte Técnico y Contacto")
    st.write("¿Tu equipo Kool-Box necesita mantenimiento o sufrió algún daño en el campo? ¡No estás solo! Contáctanos para enviarte a uno de nuestros ingenieros.")
    
    col_contacto1, col_contacto2 = st.columns(2)
    
    with col_contacto1:
        st.markdown("**📱 Atención a Productores (WhatsApp/Llamadas):**")
        st.write("+52 999 123 4567")
        st.markdown("**📧 Correo Electrónico:**")
        st.write("soporte@koolbox.mx")
        
    with col_contacto2:
        st.markdown("**🌐 Redes Sociales:**")
        st.write("👍 Facebook: /KoolBoxYucatan")
        st.write("📸 Instagram: @koolbox_agro")
        st.markdown("**📍 Taller Central:**")
        st.write("Mérida, Yucatán")


