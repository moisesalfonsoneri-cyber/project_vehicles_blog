import streamlit as st
import pandas as pd
import scipy.stats
import plotly.graph_objects as go

# Carga de datos
df = pd.read_csv("vehicles_us.csv")
df = df.dropna(subset=["type", "price", "days_listed", "model"]).copy()

# Presentacion
st.header("Blog análisis disponibilidad de vehículos")
st.write(
    "La aplicación presenta una muestra de la lista de autos disponibles y gráficos que comparan los datos \n"
    "interaccción del inventario, días de disponibilidad y precio."
)

# Dataset listo para visualizacion basica
st.write("Dataset listo para visualizacion básica")
st.write(df.head(15))

# Controles
if "show_histogram" not in st.session_state:
    st.session_state.show_histogram = False
if "show_scatter" not in st.session_state:
    st.session_state.show_scatter = False

control_col_1, control_col_2 = st.columns(2)
with control_col_1:
    if st.button("Construir histogramas"):
        st.session_state.show_histogram = not st.session_state.show_histogram
with control_col_2:
    if st.button("Construir scatter plot"):
        st.session_state.show_scatter = not st.session_state.show_scatter

show_histogram = st.session_state.show_histogram
show_scatter = st.session_state.show_scatter

# Resultados
if show_histogram:
    st.write("Se generaron histogramas de Conteo por tipo de vehículo y tipo vs precio")

    type_count_df = (
        df.groupby("type", as_index=False)["model"]
        .count()
        .rename(columns={"model": "listing_count"})
        .sort_values("listing_count", ascending=False)
    )

    histogram_type_fig = go.Figure()
    histogram_type_fig.add_trace(go.Histogram(x=df["type"], name="Conteo por type"))
    histogram_type_fig.update_layout(
        title="Conteo por tipo de auto",
        xaxis_title="tipo de auto",
        yaxis_title="Número de Autos",
    )
    st.plotly_chart(histogram_type_fig, width="stretch")

    top_types = type_count_df["type"].head(6).tolist()
    histogram_type_price_fig = go.Figure()
    for car_type in top_types:
        type_prices = df.loc[df["type"] == car_type, "price"]
        histogram_type_price_fig.add_trace(
            go.Histogram(x=type_prices, name=car_type, opacity=0.6)
        )

    histogram_type_price_fig.update_layout(
        title="Tipo de vehículo vs precio vs numero de unidades",
        xaxis_title="precio",
        yaxis_title="cantidad",
        barmode="overlay",
    )
    st.plotly_chart(histogram_type_price_fig, width="stretch")

if show_scatter:
    st.write("Se genero una gráfica de dispersión para comparar si efecta los días de inventario en relación precio y tipo.")
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
        title="Correlación entre si el precio influye en los días de inventario",
        xaxis_title="Precio",
        yaxis_title="Días de inventario",
    )
    st.plotly_chart(scatter_fig, width="stretch")

if not show_histogram and not show_scatter:
    st.write("Activa al menos un control para generar visualizaciones.")
