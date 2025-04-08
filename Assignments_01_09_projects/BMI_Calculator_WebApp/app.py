import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚕️",
    layout="centered"
)

# App title and description
st.title("BMI Calculator")
st.markdown("Enter your height and weight to calculate your Body Mass Index (BMI)")

# Create two columns for input
col1, col2 = st.columns(2)

# Input fields
with col1:
    # Weight input with options for units
    weight_unit = st.radio("Weight unit", ["Kilograms (kg)", "Pounds (lb)"])
    weight = st.number_input("Enter your weight", min_value=0.0, step=0.1)

with col2:
    # Height input with options for units
    height_unit = st.radio("Height unit", ["Meters (m)", "Centimeters (cm)", "Feet/Inches"])
    
    if height_unit == "Feet/Inches":
        height_feet = st.number_input("Feet", min_value=0, step=1)
        height_inches = st.number_input("Inches", min_value=0, max_value=11, step=1)
        # Convert feet and inches to meters
        height = (height_feet * 0.3048) + (height_inches * 0.0254)
    elif height_unit == "Centimeters (cm)":
        height_cm = st.number_input("Enter your height", min_value=0.0, step=0.1)
        height = height_cm / 100  # Convert cm to meters
    else:  # Meters
        height = st.number_input("Enter your height", min_value=0.0, step=0.01)

# Convert weight to kg if needed
if weight_unit == "Pounds (lb)":
    weight_kg = weight * 0.453592
else:
    weight_kg = weight

# Add a calculate button
if st.button("Calculate BMI"):
    # Check for valid inputs
    if height <= 0 or weight_kg <= 0:
        st.error("Please enter valid height and weight values.")
    else:
        # Calculate BMI
        bmi = weight_kg / (height ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif bmi < 25:
            category = "Normal weight"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"
        
        # Display results
        st.subheader("Results")
        st.markdown(f"Your BMI is: **{bmi:.2f}**")
        st.markdown(f"Category: <span style='color:{color};font-weight:bold'>{category}</span>", unsafe_allow_html=True)
        
        # Display BMI chart
        st.subheader("BMI Categories")
        bmi_data = {
            "Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
            "BMI Range": ["Less than 18.5", "18.5 - 24.9", "25 - 29.9", "30 or higher"]
        }
        bmi_df = pd.DataFrame(bmi_data)
        st.table(bmi_df)

# Add information about BMI
with st.expander("About BMI"):
    st.markdown("""
    **Body Mass Index (BMI)** is a measure of body fat based on height and weight that applies to adult men and women.
    
    **Formula**: BMI = weight(kg) / height²(m²)
    
    **Limitations**: BMI is a general indicator and doesn't account for factors like muscle mass, bone density, and overall body composition. Athletes might have a high BMI due to increased muscle mass rather than body fat.
    
    Always consult with healthcare professionals for a comprehensive health assessment.
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 BMI Calculator | This app is for educational purposes only.")