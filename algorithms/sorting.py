import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time

# 제목 업데이트
method_names = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
method_complexities = ["O(n^2)", "O(n^2)", "O(n^2)"]
if 'sorting_method' not in st.session_state:
    st.session_state['sorting_method'] = 0
method = st.session_state['sorting_method']
title = st.title(f"{method_names[method]} Visualization ({method_complexities[method]})")

col_slider, col_chart = st.columns(2)
array_size = col_slider.slider("Array Size", min_value=10, max_value=100, value=20)
sort_speed = col_slider.slider("Sort Speed (seconds)", min_value=0.01, max_value=0.5, value=0.1)

arr = np.random.randint(1, 100, array_size)

# Plotly 그래프 설정
fig = go.Figure(
    data=[go.Bar(x=list(range(len(arr))), y=arr, marker=dict(color=['skyblue']*len(arr)))],
    layout=go.Layout(xaxis=dict(title="Index"), yaxis=dict(title="Value"))
)
chart = col_chart.plotly_chart(fig, use_container_width=True)

stop_pressed = 0

# 정렬 과정 업데이트 함수
def update_plot(arr, idx1, idx2):
    colors = ['skyblue']*len(arr)
    if idx1 is not None:
        colors[idx1] = 'orangered'
    if idx2 is not None:
        colors[idx2] = 'orangered'

    fig.data[0].y = arr
    fig.data[0].marker.color = colors
    chart.plotly_chart(fig, use_container_width=True)
    time.sleep(sort_speed)


# 정렬과 plot 업데이트 함수
def bubble_sort_visualize(arr):
    n = len(arr)
    global stop_pressed
    for i in range(n):
        for j in range(0, n - i - 1):
            if stop_pressed:
                return
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                update_plot(arr, j, j+1)


def selection_sort_visualize(arr):
    n = len(arr)
    global stop_pressed
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx = j
            update_plot(arr, i, j)
        if stop_pressed:
            return
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort_visualize(arr):
    n = len(arr)
    global stop_pressed
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1]>arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                update_plot(arr, i, j)
        if stop_pressed:
            return


# 정렬 알고리즘 선택 버튼
col_methods = st.columns(3)
method_functions = [bubble_sort_visualize, selection_sort_visualize, insertion_sort_visualize]
for i, col in enumerate(col_methods):
    if col.button(method_names[i]):
        st.session_state['sorting_method'] = i
        title.title(f"{method_names[i]} Visualization ({method_complexities[method]})")

# 시작, 중지 버튼
start, stop = st.columns(2)
if start.button("Start"):
    stop_pressed = 0
    method = st.session_state['sorting_method']
    method_functions[method](arr)

if stop.button("Stop"):
    stop_pressed = 1
