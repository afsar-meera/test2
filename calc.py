import streamlit as st

# Streamlit app header
st.title("Simple Calculator")

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"
    return result

# Streamlit app content
num1 = st.number_input("Enter the first number:", step=0.1)
num2 = st.number_input("Enter the second number:", step=0.1)

operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")
