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
        number = random.randint(1,19)
        if number == 1:
            file_ = open("Eight/responses/as i see it yes.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/as i see it yes.gif")
        elif number == 2:
            file_ = open("Eight/responses/ask again later.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/ask again later.gif")
        elif number == 3:
            file_ = open("Eight/responses/cannot predict now.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/cannot predict now.gif")
        elif number == 4:
            file_ = open("Eight/responses/concentrate and ask again.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/concentrate and ask again.gif")
        elif number == 5:
            file_ = open("Eight/responses/don't count on it.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/don't count on it.gif")
        elif number == 6:
            file_ = open("Eight/responses/it is certain.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/it is certain.gif")
        elif number == 7:
            file_ = open("Eight/responses/it is decidedly so.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/it is decidedly so.gif")
        elif number == 8:
            file_ = open("Eight/responses/most likley.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/most likley.gif")
        elif number == 9:
            file_ = open("Eight/responses/my reply is no.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/my reply is no.gif")
        elif number == 10:
            file_ = open("Eight/responses/my sources say no.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/my sources say no.gif")
        elif number == 11:
            file_ = open("Eight/responses/no.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/no.gif")
        elif number == 12:
            file_ = open("Eight/responses/outlook good.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/outlook good.gif")
        elif number == 13:
            file_ = open("Eight/responses/outlook not so good.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/outlook not so good.gif")
        elif number == 14:
            file_ = open("Eight/responses/reply hazy, try again later.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/reply hazy, try again later.gif")
        elif number == 15:
            file_ = open("Eight/responses/signs point to yes.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/signs point to yes.gif")
        elif number == 16:
            file_ = open("Eight/responses/very doubtful.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/very doubtful.gif")
        elif number == 17:
            file_ = open("Eight/responses/without a doubt.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/without a doubt.gif")
        elif number == 18:
             file_ = open("Eight/responses/yes definitley.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/yes definitley.gif")
        elif number == 19:
            file_ = open("Eight/responses/yes.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="8ball gif">',
            unsafe_allow_html=True,
            )
            #st.image("Eight/responses/yes.gif")
