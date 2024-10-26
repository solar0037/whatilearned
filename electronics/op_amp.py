import streamlit as st
import schemdraw
import schemdraw.elements as elm
import matplotlib.pyplot as plt

st.title("Op Amp - Inverting Configuration")

col_slider, col_plot = st.columns(2)

# 사용자 입력 값
v_in = col_slider.slider("Input Voltage (V)", -10.0, 10.0, 1.0)
r1 = col_slider.slider("R1 Resistance (Ω)", 1, 10000, 1000)
r2 = col_slider.slider("R2 Resistance (Ω)", 1, 10000, 1000)

# 회로 다이어그램 생성
with schemdraw.Drawing() as d:
    op = elm.Opamp(leads=True)
    elm.Line().down(d.unit/4).at(op.in2)
    elm.Ground(lead=False)
    Rin = elm.Resistor().at(op.in1).left().idot().label('$R_{1}$', loc='top').label('$v_{I}$', loc='left')
    elm.Line().up(d.unit/2).at(op.in1)
    elm.Resistor().tox(op.out).label('$R_2$')
    elm.Line().toy(op.out).dot()
    elm.Line().right(d.unit/4).at(op.out).label('$v_{o}$', loc='right')

# Streamlit에 다이어그램 표시
d.draw()
col_plot.pyplot(plt.gcf())

# 회로 분석 결과 출력
v_out = (r2 / r1) * v_in
gain = r2 / r1
st.latex(r'''
        v_{o}=-\frac{R_{2}}{R_{1}} v_{i}
        ''')
st.latex(r'''
        G\equiv\frac{v_{o}}{v_{I}}=-\frac{R_{2}}{R_{1}}
        ''')
st.write(f"Output Voltage (V): {v_out:.2f}")
st.write(f"Voltage Gain (V/V): {gain:.2f}")
