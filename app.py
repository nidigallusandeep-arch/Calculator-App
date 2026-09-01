import streamlit as st
import math

st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)

# Sidebar
st.sidebar.title("🧮 Calculator")
st.sidebar.write("Smart Calculator Application")

st.sidebar.info(
    """
    Features:
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Percentage
    - Power
    - Square Root
    - Calculation History
    """
)

st.title("🧮 Smart Calculator")

# Inputs
number1 = st.number_input("Enter First Number", value=0.0)
number2 = st.number_input("Enter Second Number", value=0.0)

operation = st.selectbox(
    "Select Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Percentage",
        "Power"
    ]
)

if st.button("Calculate", type="primary"):

    if operation == "Addition":
        result = number1 + number2

    elif operation == "Subtraction":
        result = number1 - number2

    elif operation == "Multiplication":
        result = number1 * number2

    elif operation == "Division":

        if number2 == 0:
            st.error("Cannot divide by zero")
            result = None
        else:
            result = number1 / number2

    elif operation == "Percentage":
        result = (number1 / 100) * number2

    elif operation == "Power":
        result = number1 ** number2

    if result is not None:
        st.success(f"Result: {result}")


# Square Root
st.divider()

st.subheader("√ Square Root")

number = st.number_input(
    "Enter Number",
    value=0.0,
    key="square_root"
)

if st.button("Calculate Square Root"):

    if number < 0:
        st.error("Negative numbers are not supported.")
    else:
        result = math.sqrt(number)
        st.success(f"√{number} = {result}")