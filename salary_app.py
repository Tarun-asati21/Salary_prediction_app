import streamlit as st
import pickle 

mean_experience = 5.2875
std_experience = 2.88116188
model = pickle.load(open(r'C:\VScode\Ml\salary_pred.pkl', 'rb'))

st.title("Salary Prediciton App")
st.header("Do you have many expectations from your salary??")

experience_input = st.text_input("Enter Years of Experience :")
st.text("NOTE : Years might be in integer or decimal both.")

if st.button("Predict Salary"):
    if experience_input:
        try:
            experience = float(experience_input)
            experience_scaled = [[(experience - mean_experience) / std_experience]]
            prediction = float(model.predict(experience_scaled)[0])
            st.success(f"Predicted Salary: ₹{prediction:,.2f}")
        except ValueError:
            st.error("❌ Please enter a valid number (e.g., 2, 4.5, 7.25)")
    else:
        st.warning("⚠️ Please enter years of experience")

st.markdown("---")
st.caption("⚠️ DISCLAIMER : This model is build upon the data available on the public domain. The developer is not liable for the accuracy of this prediction. It is for educational/demonstration purposes only.")
