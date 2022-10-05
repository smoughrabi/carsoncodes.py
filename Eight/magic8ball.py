import random
import pandas as pd
import streamlit as st
import base64

#responses = pd.read_csv("Eight/8ballresponses.csv")
#responses = responses['responses'].tolist()

#hiding header
hide_decoration_bar_style = '''
    <style>
    header {visibility: hidden;}
    </style>'''

st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

#adding background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""<style>.stApp {{background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});background-size: cover}}</style>""",unsafe_allow_html=True)

add_bg_from_local('Eight/bg.png')

#modifying button color, size, and text
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: white;
    color: rgb(145,0,240);
    height:3em;
    width:20em;
}
</style>""", unsafe_allow_html=True)

st.image('Eight/title.JPG')
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
col1,col2,col3 = st.columns([1,2,1])
with col2:
    button = st.button("CLICK ME")
    if button:
        number = random.randint(1,1)
        if number == 1:
            file_ = open("Eight/responses/as i see it yes.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', "<style> height:3em; width:20em;</style>",
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/as i see it yes.gif")
        elif number == 2:
            st.image("Eight/responses/ask again later.gif")
        elif number == 3:
            st.image("Eight/responses/cannot predict now.gif")
        elif number == 4:
            st.image("Eight/responses/concentrate and ask again.gif")
        elif number == 5:
            st.image("Eight/responses/don't count on it.gif")
        elif number == 6:
            st.image("Eight/responses/it is certain.gif")
        elif number == 7:
            st.image("Eight/responses/it is decidedly so.gif")
        elif number == 8:
            st.image("Eight/responses/most likley.gif")
        elif number == 9:
            st.image("Eight/responses/my reply is no.gif")
        elif number == 10:
            st.image("Eight/responses/my sources say no.gif")
        elif number == 11:
            st.image("Eight/responses/no.gif")
        elif number == 12:
            st.image("Eight/responses/outlook good.gif")
        elif number == 13:
            st.image("Eight/responses/outlook not so good.gif")
        elif number == 14:
            st.image("Eight/responses/reply hazy, try again later.gif")
        elif number == 15:
            st.image("Eight/responses/signs point to yes.gif")
        elif number == 16:
            st.image("Eight/responses/very doubtful.gif")
        elif number == 17:
            st.image("Eight/responses/without a doubt.gif")
        elif number == 18:
            st.image("Eight/responses/yes definitley.gif")
        elif number == 19:
            st.image("Eight/responses/yes.gif")
