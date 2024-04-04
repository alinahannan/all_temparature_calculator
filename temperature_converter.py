import streamlit as st

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

st.title("Temperature Converter")

temperature = st.number_input("Enter temperature:", step=0.1)

conversion_from = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])
conversion_to = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

result = None

if conversion_from == conversion_to:
    st.warning("Please select different units for conversion.")
else:
    if conversion_from == "Celsius":
        if conversion_to == "Fahrenheit":
            result = celsius_to_fahrenheit(temperature)
        elif conversion_to == "Kelvin":
            result = celsius_to_kelvin(temperature)
    elif conversion_from == "Fahrenheit":
        if conversion_to == "Celsius":
            result = fahrenheit_to_celsius(temperature)
        elif conversion_to == "Kelvin":
            result = fahrenheit_to_kelvin(temperature)
    elif conversion_from == "Kelvin":
        if conversion_to == "Celsius":
            result = kelvin_to_celsius(temperature)
        elif conversion_to == "Fahrenheit":
            result = kelvin_to_fahrenheit(temperature)

    if result is not None:
        st.success(f"The converted temperature is {result:.2f} {conversion_to}.")
