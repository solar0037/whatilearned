import streamlit as st
import schemdraw
from schemdraw import elements as elm
import matplotlib.pyplot as plt
import math

st.title("Diodes")

col_slider, col_plot = st.columns(2)

# 사용자 입력 값
v_DD = col_slider.slider("Input Voltage (V)", -10.0, 10.0, 1.0)
r = col_slider.slider("Resistance (Ω)", -100.0, 100.0, 10.0)

with schemdraw.Drawing() as d:
    V1 = elm.SourceV().label('$V_{DD}$')
    elm.Line().right(d.unit*.75)
    R = elm.Resistor().right().label('R')
    elm.Line().right(d.unit*.75).at(R.end)
    elm.Diode().down().label('$v_{D}$')
    elm.Line().to(V1.start)


d.draw()
col_plot.pyplot(plt.gcf())

# 회로 분석 결과 출력
I_D = (v_DD-0.7)/r
I_S = I_D*math.exp(-0.7/0.025)
st.latex(r'''
        I_{D}=I_{S} e^{(V_{D}/V_{T})}
        ''')
st.latex(r'''
        I_{D}=\frac{V_{DD}-V_{D}}{R}
        ''')
st.write(f"Diode Current (A): {I_D:.2f}")
st.write(f"Reverse-bias saturation Current (A): {I_S:.20f}")
