import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Esnupitos GO",
    layout="wide"
)

st.title("📊 Dashboard de Observabilidad - Esnupitos GO")

try:

    df = pd.read_csv("logs.csv")

    total_consultas = len(df)

    latencia_promedio = round(
        df["latencia"].mean(),
        2
    )

    total_errores = len(
        df[df["estado"] == "ERROR"]
    )

    porcentaje_exito = round(
        ((total_consultas - total_errores)
         / total_consultas) * 100,
        2
    ) if total_consultas > 0 else 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Consultas Totales",
            total_consultas
        )

    with col2:
        st.metric(
            "Latencia Promedio (s)",
            latencia_promedio
        )

    with col3:
        st.metric(
            "Errores",
            total_errores
        )

    with col4:
        st.metric(
            "Precisión (%)",
            porcentaje_exito
        )

    st.divider()

    st.subheader("Latencia por consulta")

    st.line_chart(
        df["latencia"]
    )

    st.subheader("Estado de consultas")

    estado_count = (
        df["estado"]
        .value_counts()
    )

    st.bar_chart(
        estado_count
    )

    st.subheader("Historial de consultas")

    st.dataframe(
        df,
        use_container_width=True
    )

except FileNotFoundError:

    st.error(
        "No existe logs.csv. Ejecuta primero el chatbot para generar registros."
    )