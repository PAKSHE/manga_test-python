import streamlit as st

def local_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit&display=swap');

        html, body, div, span, input, label, textarea, select, button, h1, h2, h3, h4, h5, h6, p {
            font-family: 'Kanit', sans-serif !important;
        }

        /* ครอบ css class ที่ Streamlit ใช้ */
        [class^="css"] {
            font-family: 'Kanit', sans-serif !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
