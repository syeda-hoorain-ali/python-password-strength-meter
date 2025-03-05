import streamlit as st 
from password import check_password_strength, generate_password
from styles import styles, progress_bar


st.set_page_config(
    "Password Strength Meter - Syeda Hoorain Ali",
    layout="centered"
)

st.markdown(styles, unsafe_allow_html=True)

with st.container():
    st.title("Password Strength Meter")

    container = st.container(key="container")
    col, = container.columns(1)


    if 'password' not in st.session_state:
        st.session_state.password = ''

    password = col.text_input("Enter your password", value=st.session_state.password)
    if col.button("Generate password", type='primary'):
        st.session_state.password = generate_password()
        st.rerun()


    status, errors = check_password_strength(password)
    col.markdown(progress_bar(status), unsafe_allow_html=True)

    error = ''.join([f":red[{i + 1}. {error}]  \n" for i, error in enumerate(errors)])
    col.markdown(error)

    # err = ''
    # for i, error in enumerate(errors):
    #     err += f":red[{i + 1}. {error}]  \n"


footer = st.container(key='footer')
footer.write('Made with 💖 by Syeda Hoorain Ali')
