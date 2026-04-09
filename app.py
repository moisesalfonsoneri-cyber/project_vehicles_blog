import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("vehicles_us.csv")
df = df.dropna(subset=["price", "days_listed"]).copy()

st.header("Blog Venta de Garage de Vehículos")
st.write(
    "Esta app muestra un histograma de days_listed y un scatter plot de "
    "price vs days_listed."
)

if "show_histogram" not in st.session_state:
    st.session_state.show_histogram = True
if "show_scatter" not in st.session_state:
    st.session_state.show_scatter = True

control_col_1, control_col_2 = st.columns(2)
with control_col_1:
    if st.button("Mostrar/ocultar histograma"):
        st.session_state.show_histogram = not st.session_state.show_histogram
with control_col_2:
    if st.button("Mostrar/ocultar scatter"):
        st.session_state.show_scatter = not st.session_state.show_scatter

show_histogram = st.session_state.show_histogram
show_scatter = st.session_state.show_scatter

if show_histogram:
    st.write("Se genero el histograma de days_listed.")
    histogram_fig = go.Figure(
        data=[go.Histogram(x=df["days_listed"], nbinsx=40, name="days_listed")]
    )
    histogram_fig.update_layout(
        title="Histograma de days_listed",
        xaxis_title="days_listed",
        yaxis_title="Frecuencia",
    )
    st.plotly_chart(histogram_fig, width="stretch")

if show_scatter:
    st.write("Se genero el scatter plot de price vs days_listed.")
    scatter_fig = go.Figure(
        data=[
            go.Scatter(
                x=df["price"],
                y=df["days_listed"],
                mode="markers",
                name="price vs days_listed",
            )
        ]
    )
    scatter_fig.update_layout(
        title="Scatter de price vs days_listed",
        xaxis_title="price",
        yaxis_title="days_listed",
    )
    st.plotly_chart(scatter_fig, width="stretch")

if not show_histogram and not show_scatter:
    st.write("Selecciona al menos una opción para generar un gráfico.")
