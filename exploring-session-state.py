# ---- Modules ------- 
import streamlit as st


if "correct_state" not in st.session_state:
    st.session_state.correct_state = False

if "wrong_state" not in st.session_state:
    st.session_state.wrong_state = False



st.text("Is the emotion shown correct?")
new = st.button("Yes")
wrong = st.button("No")




if new or st.session_state.correct_state:
    st.session_state.correct_state = True
    st.text("yeay")

elif wrong or  st.session_state.wrong_state:
    st.session_state.wrong_state = True
    st.text("oops")

    # it works when i clear the cache