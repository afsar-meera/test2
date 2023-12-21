import streamlit as st

def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

st.title('Simple Interest Calculator')

# User input for principal amount
principal_amount = st.number_input('Enter Principal Amount:', min_value=0.0)

# User input for interest rate
interest_rate = st.number_input('Enter Annual Interest Rate:', min_value=0.0)

# User input for time period
time_period = st.number_input('Enter Time Period (in years):', min_value=0.0)

# Calculate simple interest when the 'Calculate' button is clicked
if st.button('Calculate'):
    simple_interest = calculate_simple_interest(principal_amount, interest_rate, time_period)
    st.success(f'Simple Interest: {simple_interest:.2f}')
