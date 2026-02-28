import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN DE LA APP ---
# Layout "centered" lo hace ver como una app móvil en pantallas grandes
st.set_page_config(page_title="Kool-Box Portal", page_icon="🌱", layout="centered")

# ==========================================
# 🎨 INYECCIÓN DE CSS (El "Hack" Visual)
# ==========================================
st.markdown("""
<style>
    /* Ocultar elementos por defecto de Streamlit para que no parezca un dashboard */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Quitar el espacio en blanco de arriba */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
    }

    /* Estilo de Botones Comerciales (Redondeados y llamativos) */
    div.stButton > button {
        width: 100%;
        border-radius: 15px;
        border: 2px solid #2e7d32;
        background-color: #e8f5e9;
        color: #1b5e20;
        font-weight: 800;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #2e7d32;
        color: white;
        border: 2px solid #1b5e20;
    }

    /* Tarjetas del catálogo */
    .catalogo-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #2e7d32;
    }
    
    /* Texto resaltado */
    .precio-destacado {
        font-size: 24px;
        color: #2e7d32;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- ENCABEZADO DE LA APP ---
st.markdown("<h1 style='text-align: center; color: #2e7d32;'>🌱 Kool-Box App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Tu aliado para precios justos y tecnología accesible.</p>", unsafe_allow_html=True)

# ==========================================
# CREACIÓN DE PESTAÑAS (TABS)
# ==========================================
tab_precios, tab_calidad, tab_catalogo = st.tabs([
    "📊 Mercado", 
    "🏅 Calidad", 
    "🛒 Tienda"
])

# ==========================================
# PESTAÑA 1: PRECIOS DE MERCADO
# ==========================================
with tab_precios:
    st.markdown("### 💡 ¿Qué me conviene hoy?")
    
    sector = st.radio("Elige tu sector:", ["🌽 Agrícola", "🎣 Pesquero"], horizontal=True)
    
    if sector == "🌽 Agrícola":
        data = {
            "Producto": ["Chile Habanero", "Papaya Maradol", "Tomate Saladette"],
            "Precio": ["$55.50 /kg", "$18.20 /kg", "$22.00 /kg"],
            "Acción": ["🟢 Vender Ahora", "🟢 Vender Ahora", "🔴 Esperar"]
        }
    else:
        data = {
            "Producto": ["Mero Fresco", "Pulpo Maya", "Huachinango"],
            "Precio": ["$180.00 /kg", "$145.00 /kg", "$120.00 /kg"],
            "Acción": ["🟢 Vender Ahora", "🔴 Esperar", "🟡 Estable"]
        }
        
    df = pd.DataFrame(data)
    
    # Mostrar tarjetas de precios en lugar de una tabla aburrida
    for index, row in df.iterrows():
        with st.container():
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown(f"**{row['Producto']}**")
                st.markdown(f"<span class='precio-destacado'>{row['Precio']}</span>", unsafe_allow_html=True)
            with col2:
                if "🟢" in row['Acción']:
                    st.success(row['Acción'])
                elif "🔴" in row['Acción']:
                    st.error(row['Acción'])
                else:
                    st.warning(row['Acción'])
            st.divider()

# ==========================================
# PESTAÑA 2: VALIDACIÓN DEL PRODUCTO
# ==========================================
with tab_calidad:
    st.markdown("### 🏅 Certificado de Origen")
    st.write("Escribe el código de tu Kool-Box para validar tu cosecha ante el comprador.")

    codigo_usuario = st.text_input("Ingresa el PIN (Ej. 95A2):", max_chars=4)

    if codigo_usuario:
        if len(codigo_usuario) == 4 and codigo_usuario[1:3].isdigit():
            final_score = int(codigo_usuario[1:3])
            st.write("---")
            if final_score > 90:
                st.balloons()
                st.success(f"🥇 **CALIDAD PREMIUM ({final_score}%)**")
                st.write("Humedad y temperatura perfectas. Cumple NOM-004.")
            elif final_score > 70:
                st.info(f"🥈 **CALIDAD ESTÁNDAR ({final_score}%)**")
                st.write("Parámetros aceptables para mercado local.")
            else:
                st.warning(f"🥉 **ATENCIÓN ({final_score}%)**")
                st.write("El riego fue inconstante. Revisa el huerto.")
        else:
            st.error("❌ PIN inválido.")

# ==========================================
# PESTAÑA 3: CATÁLOGO DE UPGRADES (Estilo Tienda)
# ==========================================
with tab_catalogo:
    st.markdown("### 🛒 Mejora tu Producción")
    
    # Tarjeta 1
    st.markdown("""
    <div class="catalogo-card">
        <h4 style="margin-top:0;">🌱 Nivel 1: Kool-Box Base</h4>
        <p>Monitoreo offline de humedad y temperatura. Generador de código de calidad incluido.</p>
        <h3 style="color:#2e7d32;">$1,500 MXN</h3>
    </div>
    """, unsafe_allow_html=True)
    st.button("Comprar Nivel 1", key="btn1")
    
    # Tarjeta 2
    st.markdown("""
    <div class="catalogo-card">
        <h4 style="margin-top:0;">💧 Nivel 2: Riego Inteligente</h4>
        <p>Agrega electroválvulas a tu sistema. El huerto se regará solo cuando la tierra lo necesite.</p>
        <h3 style="color:#2e7d32;">$3,500 MXN</h3>
    </div>
    """, unsafe_allow_html=True)
    st.button("Comprar Nivel 2", key="btn2")
    
    # Tarjeta 3
    st.markdown("""
    <div class="catalogo-card">
        <h4 style="margin-top:0;">☀️ Nivel 3: Resiliencia Total</h4>
        <p>Kit con Panel Solar y sensores avanzados (pH/Nutrientes) para independizarte de la red eléctrica.</p>
        <h3 style="color:#2e7d32;">$6,000 MXN</h3>
    </div>
    """, unsafe_allow_html=True)
    st.button("Comprar Nivel 3", key="btn3")