import streamlit as st
import random
comparison_count = 0
def min_max_dc(arr, low, high):
    global comparison_count
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]
    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin
    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax
    return overallmin, overall_max
def min_max_naive(arr):
    mn, mx = arr[0], arr[0]
    comps = 0
    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x
        comps += 1
        if x > mx:
            mx = x
    return mn, mx, comps
st.title("Min-Max Finder using Divide and Conquer")
st.write("Compare Divide & Conquer with Naive Approach.")
numbers = st.text_input(
    "Enter numbers separated by commas",
    "3,1,7,4,9,2,8,5,6,0"
)
if st.button("Find Min & Max"):
    arr = list(map(int, numbers.split(",")))
    comparison_count = 0
    mn, mx = min_max_dc(arr, 0, len(arr)-1)
    dc = comparison_count
    _, _, naive = min_max_naive(arr)
    st.success(f"Minimum Value : {mn}")
    st.success(f"Maximum Value : {mx}")
    st.subheader("Comparison Count")
    st.write(f"Divide & Conquer : **{dc}**")
    st.write(f"Naive Method : **{naive}**")
st.subheader("Performance Analysis")
sizes = [10,100,1000,10000]
table = []
for size in sizes:
    arr = [random.randint(1,10000) for _ in range(size)]
    comparison_count = 0
    min_max_dc(arr,0,len(arr)-1)
    dc = comparison_count
    _,_,naive = min_max_naive(arr)
    formula = 3*size//2 -2
    table.append({
        "Input Size":size,
        "D&C Comparisons":dc,
        "Naive Comparisons":naive,
        "Formula (3n/2-2)":formula
    })

st.table(table)
