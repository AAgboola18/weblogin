import streamlit as st
import random
import re


def generate_username(first_name, surname):
    first_letter = first_name[0].upper()
    username = first_letter + surname.lower() + str(random.randint(1, 99))
    return username


def password_valid(password_val):
    return len(password_val) >= 8 and bool(re.search(r'[A-Z]', password_val)) and bool(re.search(r'\d', password_val))


st.title("Registration page")

first_name = st.text_input("First Name")
surname = st.text_input("Surname")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if password and not password_valid(password):
    st.error("Password must be at least 8 characters long and contain at least 1 uppercase letter and 1 number.")

if st.button("Register"):
    if first_name and surname:
        if password == confirm_password:
            username = generate_username(first_name, surname)
            st.success("Registration successful!")
            st.write("Your Username is:", username)
        else:
            st.error("Passwords do not match")
    else:
        st.error("Registration failed. Please ensure all fields are filled correctly.")


