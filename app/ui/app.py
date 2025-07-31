import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"  # Cambia si corres FastAPI en otro host/puerto

st.set_page_config(page_title="Orquestador Contabilidad", layout="wide")
st.title("Orquestador de Servicios - Contabilidad")

# 🔄 Sincronizar con CRS
st.subheader("Sincronizar datos con CRS")
col1, col2, col3 = st.columns(3)
with col1:
    location_id = st.number_input("Location ID", min_value=1, value=1)
with col2:
    start_date = st.text_input("Fecha inicio (DD/MM/YYYY)", "14/07/2025")
with col3:
    end_date = st.text_input("Fecha fin (DD/MM/YYYY)", "15/07/2025")

if st.button("Sincronizar con CRS"):
    url = f"{API_URL}/crs/fetch?location_id={location_id}&start_date={start_date}&end_date={end_date}"
    response = requests.post(url)
    st.write(response.json())

st.divider()

# 📄 Listar journals
st.subheader("📄 Journals almacenados")
journals = requests.get(f"{API_URL}/journals").json()

if journals:
    df = pd.DataFrame(journals)
    st.dataframe(df, use_container_width=True)

    selected_id = st.selectbox("Selecciona un Journal", df["id"])
    if st.button("Ver transacciones"):
        transactions = requests.get(f"{API_URL}/journals/{selected_id}").json()
        st.subheader(f"Transacciones del Journal {selected_id}")
        st.dataframe(pd.DataFrame(transactions), use_container_width=True)
else:
    st.warning("No hay journals cargados aún.")
