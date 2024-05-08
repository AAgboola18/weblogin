import streamlit as st
import random
import re


# function to generate the unique username
def generate_username(first_name, surname):
    first_letter = first_name[0].upper()
    username = first_letter + surname.lower() + str(random.randint(1, 99))
    return username

# Function to validate the password
def password_valid(password_val):
    return len(password_val) >= 8 and bool(re.search(r'[A-Z]', password_val)) and bool(re.search(r'\d', password_val))


# Allows the errors to be printed at the button of the screen in a list
def validation_register(first_name,surname,password,confirm_password):
    errors = []

    if len([password]) < 8:
        errors.append("Password must be 8 characters")
    elif not password_valid(password):
        errors.append("Password must contain numbers and letters")
    elif not first_name and surname:
        errors.append("Registration error. Please ensure  in all the fields are filled in")

    if password != confirm_password:
        errors.append("Passwords do not match")

    return errors


# Title of login page
st.title("Registration page")


first_name = st.text_input("First Name")
surname = st.text_input("Surname")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    password_valid = validation_register(first_name, surname, password, confirm_password)

    if not password_valid:
        st.success("Registration successful")
    else:
        for item in password_valid:
            st.error(item)

