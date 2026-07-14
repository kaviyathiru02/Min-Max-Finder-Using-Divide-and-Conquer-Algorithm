# Min-Max-Finder-Using-Divide-and-Conquer-Algorithm
A Python-based Streamlit application demonstrating the Divide and Conquer algorithm to efficiently find the minimum and maximum values in an array while comparing its performance with the traditional Naive approach

## Features

- Find Minimum Value
- Find Maximum Value
- Compare Divide & Conquer with Naive Method
- Displays Comparison Count
- Performance Analysis for different input sizes
- Interactive Streamlit Web App

## Technologies Used

- Python
- Streamlit

## Algorithm

### Divide and Conquer

1. Divide the array into two halves.
2. Recursively find the minimum and maximum of each half.
3. Compare the two minimum values.
4. Compare the two maximum values.
5. Return the overall minimum and maximum.

### Time Complexity

- Divide & Conquer : O(n)
- Naive Method : O(n)

Although both have O(n) complexity, Divide and Conquer performs fewer comparisons (approximately 3n/2 − 2).

## Run Locally

```bash
pip install -r requirements.txt
```

```bash
streamlit run app.py
```
