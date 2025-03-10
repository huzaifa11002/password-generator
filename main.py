import streamlit as st
import modules

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

if "checker" not in st.session_state:
    st.session_state["checker"] = False

if "pass_val" not in st.session_state:
    st.session_state.pass_val= ""

with st.sidebar:
    st.session_state["page"] = st.radio("Menu",["Home" , "Check Strength", "Password Generator"], index=["Home", "Check Strength", "Password Generator"].index(st.session_state["page"]))

if st.session_state["page"] == "Home":
    st.title("Welcome to SecurePass! 🚀")
    st.write("A secure and easy-to-use password generator with a built-in strength meter that helps you create strong, unbreakable passwords and evaluate their security in real-time.")

elif st.session_state["page"] == "Password Generator":

    st.title('Secure Password Generator 🔒')
    st.write('This is a simple password generator that generates a secure password for you. You can specify the length of the password and the number of passwords you want to generate.')

    length = st.slider('Length of password', 6, 12, 8)
    digit = st.checkbox('Include digits in password')
    symbol = st.checkbox('Include symbols in password')


    if st.button('Generate Password'):
        st.write('Here is your generated password:')
        st.session_state.pass_val = modules.genrate_password(length,digit,symbol)
        st.success(st.session_state.pass_val)
        st.session_state["checker"] = True

    if st.session_state["checker"]:
        st.write("You want to check your password is secure or not?")
        if st.button("Check Secure", key="security"):
            st.session_state["page"] = "Check Strength"
            st.rerun()

elif st.session_state["page"] == "Check Strength":

    st.title('Secure Password Checker 🔐')
    st.write('This is a simple password generator that generates a secure password for you. You can specify the length of the password and the number of passwords you want to generate.')

    user_password = st.text_input("Enter your password" , st.session_state.pass_val, type='password')

    if st.button("Check" , key="check"):
        if user_password:
            strength, message = modules.password_checker(user_password)
    
        if strength == "Weak":
            st.error("Your password is weak")
            st.subheader("Must be Include")
            for errors in message:
                st.warning(errors)
        elif strength == "Medium":
            st.info("Your password is Medium")
            st.subheader("Must be Include")
            st.write("you want to more secure your password must be include in your password")
            for errors in message:
                st.warning(errors)
        else:
            st.success("Your password is Strong")
