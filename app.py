import streamlit as st
import pyshorteners as pys
import pyperclip

st.set_page_config(
    page_title="Link shortener",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "### This is a link shortener app.",
        'Get help': "https://100pa.com"
    }
)

hide_streamlit_style = '''
<style>
footer {visibility: hidden;}
footer:after {
	content:'100pa.com'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
</style>
'''
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

shortner = pys.Shortener()

def copying():
    ''' copies to the clipboard '''
    pyperclip.copy(shorted_url)
    url = ""
    warn= ""

st.write("# 🔗 Skracacz linków")
st.write("#### Wklej długi link, a nowy krótszy zostanie wygenerowany")
form = st.form("skracacz")
url = form.text_input("Tutaj wklej adres url:")
s_btn = form.form_submit_button("Skróć adres internetowy")
if s_btn and url=="": 
    warn=st.warning("🚨 Wklej adres internetowy")
if s_btn and url:
    shorted_url=shortner.tinyurl.short(url)
    st.write("Skrócony adres to:")
    st.write(shorted_url)
    st.button("Skopuj", on_click=copying)
