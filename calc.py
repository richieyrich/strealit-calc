# Import libraries
import streamlit as st

# title 
st.title('Simple Calculator App')

# Add number input widgets for the operands
num1 = st.number_input('Enter the first operand:')
num2 = st.number_input('Enter the second operand:')

# selectbox for operation
operation = st.selectbox('Select an operation:', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

# calculation based on the selected operation
if operation == 'Addition':
    result = num1 + num2
elif operation == 'Subtraction':
    result = num1 - num2
elif operation == 'Multiplication':
    result = num1 * num2
elif operation == 'Division':
    if num2 == 0:
        result = 'Error: Division by zero'
    else:
        result = num1 / num2

# Display the result
st.write(f'The result is: {result}')
