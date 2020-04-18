import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly_express as px


def write():
    # with st.spinner("Loading Home ..."):

    @st.cache
    def load_data(URL):
        return pd.read_csv(URL)

    # data_load_state = st.text('Loading datasets...')
    URL = 'datasets/kepler_processed.csv'
    df = load_data(URL)
    # data_load_state.text('Loading datasets...done')

    # DISPOSITION
    st.title('Disposition of Kepler\'s detections')

    fig = px.histogram(df, x="disposition", opacity=0.8, color='disposition')
    fig.update_layout(
        xaxis_title_text='Disposition',
        yaxis_title_text='Count',
        showlegend=False
    )
    st.plotly_chart(fig)

    # THIRD LAW
    st.title('Third law of Kepler')
    st.info("'The square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit.'")

    URL = 'datasets/phl_new_processed.csv'
    df = load_data(URL)

    df_kepler = df[['p_period', 'p_semi_major_axis']].copy()
    df_kepler.dropna(inplace=True)
    df_kepler['period_squared'] = df['p_period']**2
    df_kepler['p_semi_major_axis_cubed'] = df['p_semi_major_axis']**3

    fig = px.scatter(df_kepler, x='period_squared', y='p_semi_major_axis_cubed', trendline='ols')
    fig.update_layout(
        xaxis_title_text='Orbital period ^ 2 (days)',
        yaxis_title_text='Semi-major axis ^ 3 (AU)',
        showlegend=False
    )
    fig.update_xaxes(range=[0, 6500])
    fig.update_yaxes(range=[0, 0.045])
    st.plotly_chart(fig)

    from scipy import stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(df_kepler['period_squared'], df_kepler['p_semi_major_axis_cubed'])
    st.write('The R squared is ', round(r_value**2,4), '!')

    # TYPE OF PLANETS
    st.title('Types of exoplanets')
    df_type = df.dropna()
    fig = px.histogram(df_type, x="p_type", opacity=0.8, color='p_type')
    fig.update_layout(
        xaxis_title_text='Planet type',
        yaxis_title_text='Count',
        showlegend=False
    )
    st.plotly_chart(fig)

    st.subheader('Planet radius/mass by type')
    df_planet = df[['p_mass', 'p_radius', 'p_type']].dropna()
    fig = px.scatter(df_planet, x="p_mass", y='p_radius', opacity=0.8, color='p_type')
    fig.update_layout(
        xaxis_title_text='Mass (EU)',
        yaxis_title_text='Radius (ER)'
    )
    fig.update_xaxes(range=[-0.1, 80])
    fig.update_yaxes(range=[-0.05, 10])
    st.plotly_chart(fig)