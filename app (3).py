import streamlit as st
import re

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Minimum 8 characters required")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number")

    if re.search("[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add a special character")

    if score >= 4:
        st.success(f"Strong Password ({score}/5)")
    elif score == 3:
        st.warning(f"Medium Password ({score}/5)")
    else:
        st.error(f"Weak Password ({score}/5)")

    if feedback:
        st.subheader("Suggestions")
        for f in feedback:
            st.write('•', f)
