# import streamlit as st

# st.title("🌎Unit Converter App")
# st.markdown("### Converts Lenght, Weight and, Time Instantly")
# st.write("Welcome! Select a category, enter the value and get the converted resultin real-type.")

# category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# def convert_units(category, value, unit):
#     if category == "Length":
#         if unit == "killometers to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Killometers":
#             return value / 0.621371
        
#     elif category == "Weight":
#         if unit == "kilograms to pounds":
#             return value * 2.20462
#         elif unit == "Pounds to kilograms":
#             return value / 2.20462
#     elif  category == "Time":
#         if unit == "Seconds to minutes":
#             return value / 60
#         elif unit == "Minutes to seconds":
#             return value * 60 
#         elif unit == "Minuts to hours":
#             return value / 60
#         elif unit == "Hours to minutes":
#             return value * 60 
#         elif unit == "Hours to days":
#             return value / 24
#         elif unit == "Days to hours":
#             return value * 24
        
# if category == "Length":
#     unit = st.selectbox("📏 Select Conversation", ["Killometers to Miles", "Miles to Killometers"])
# elif category == "Weight":
#     unit = st.selectbox("⚖️ Select Conversation", ["Kilograms to pounds", "Pounds to kilograms"])                           

# elif category == "Time":
#     unit = st.selectbox("⏱️ Select Conversation", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])
            
# value = st.number_input("Enter the value to convert")

# if st.button("Convert"):
#     result = convert_units(category, value, unit)
#     st.write(f"The result is {result:.2f}")
import streamlit as st

st.title("🌎 Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter the value and get the converted result in real-time.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
            
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60 
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60 
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return None  # Default return agar koi option match na kare

if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])                           
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
            
value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)

    if result is not None:
        st.write(f"The result is {result:.2f}")
    else:
        st.write("⚠️ Error: Invalid conversion. Please check your input.")

            
    
        