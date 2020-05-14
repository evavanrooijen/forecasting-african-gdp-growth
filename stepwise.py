import streamlit as st
from functions import *
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.vector_ar.vecm import coint_johansen

st.title('Forecasting African GDP Growth')
N = 50
T = 50
a = 1
var_eps = 0.5
tao = 0.4
alpha = 2

Y = create_DGP(N, T, alpha, var_eps)

st.subheader('Step 0: Data Simulation')
i = st.slider('Select Country (i): ', 0, N,0)
st.line_chart(Y[i])

result = adfuller(Y[i])
st.write('H0 : unit root (non-stationary)')
st.write('ADF Statistic: %f' % result[0])
st.write('p-value: %f' % result[1])

st.line_chart(growth_rate(Y[i]))

result = adfuller(growth_rate(Y[i]))
st.write('H0 : unit root (non-stationary)')
st.write('ADF Statistic: %f' % result[0])
st.write('p-value: %f' % result[1])

st.subheader('Step 1: Find Cointegration Countries')
tao = st.selectbox('Select tao',[0.4, 0.7], index=0)
JH = CRDW(Y, i, tao)
st.line_chart(np.transpose(JH))


st.subheader('Step 2: Find Cointegration Relation')
st.write('To do')
#coint_johansen(JH, 0, 1)
#st.line_chart(np.transpose(JH))

st.subheader('Step 3: Find Correlated Countries')

st.subheader('Step 4: Define Parameters')

st.subheader('Step 5: Estimate Model')

st.subheader('Step 6: Estimate IMA Model')

st.subheader('Step 7: Compare RMSPE')

st.subheader('Step 8: Repeat 100 Times')


