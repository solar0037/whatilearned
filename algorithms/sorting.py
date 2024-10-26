import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time

# Streamlit 설정
st.title("Bubble Sort Visualization")

# 슬라이더로 배열 크기와 정렬 속도 조절
array_size = st.slider("Array Size", min_value=10, max_value=100, value=20)
sort_speed = st.slider("Sort Speed (seconds)", min_value=0.01, max_value=0.5, value=0.1)

# 랜덤 배열 생성
arr = np.random.randint(1, 100, array_size)

# Plotly 그래프 설정
fig = go.Figure(
    data=[go.Bar(x=list(range(len(arr))), y=arr)],
    layout=go.Layout(xaxis=dict(title="Index"), yaxis=dict(title="Value"))
)
chart = st.plotly_chart(fig, use_container_width=True)

stop_pressed = 0

# 정렬 과정 업데이트 함수
def update_plot(arr):
    fig.data[0].y = arr  # y값 업데이트
    chart.plotly_chart(fig, use_container_width=True)  # Streamlit에 업데이트된 그래프 표시
    time.sleep(sort_speed)

# 버블 정렬 함수
def bubble_sort_visualize(arr):
    n = len(arr)
    global stop_pressed
    for i in range(n):
        for j in range(0, n - i - 1):
            if stop_pressed:
                return
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                update_plot(arr)  # 각 단계마다 시각화 업데이트

col1, col2 = st.columns(2)
if col1.button("Start"):
    stop_pressed = 0
    bubble_sort_visualize(arr)

if col2.button("Stop"):
    stop_pressed = 1
