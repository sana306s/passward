import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔓")

st.title("🔓 Password Strength Checker")
st.markdown("""
## Welcome to the unlimited password strength checker⭐ 
Use this simple tool to check your password strength
           and get helpful suggestions for a **Stronger Password** 🔓""")

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Increase password length to at least 8 characters.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Use both uppercase and lowercase letters.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Include at least one number (0-9).")

    if re.search(r'[@$!%*?&#]', password):
        score += 1
    else:
        feedback.append("❌ Add a special character (@, $, #, !, etc.) for better security.")

    # Strength Messages
    if score == 4:
        st.success("✔ Your Password is Strong 🎉")
    elif score == 3:
        st.warning("⚠️ Your Password is medium strength. Try making it stronger!")
    else:
        st.error("🚨 Your Password is weak, please make it stronger.")

    # Suggestions Section
    if feedback:
        st.markdown("### 🔹 Suggestions to Improve Your Password")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")
