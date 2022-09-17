#import packages
import pandas as pd
import streamlit as st
import random
import base64


#add images
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background.jpg')

st.image('header.jpg',width=700)

#loading qatareats dataset
df = pd.read_csv('qatareatss.csv')

#lists for every cuisine
American = df['American'].dropna().tolist()
Chinese = df['Chinese'].dropna().tolist()
French = df['French'].dropna().tolist()
Fusion = df['Fusion'].dropna().tolist()
Greek = df['Greek'].dropna().tolist()
Indian = df['Indian'].dropna().tolist()
Italian = df['Italian'].dropna().tolist()
Japanese = df['Japanese'].dropna().tolist()
Latin_American = df['Latin American'].dropna().tolist()
Levantine = df['Levantine'].dropna().tolist()
Mexican = df['Mexican'].dropna().tolist()
Qatari = df['Qatari'].dropna().tolist()
Southeast_Asian = df['Southeast Asian'].dropna().tolist()
Spanish = df['Spanish '].dropna().tolist()
Steakhouse = df['Steakhouse'].dropna().tolist()

#list of cuisine names for selectbox
cuisine = df['Cuisine '].tolist()
cuisine = list(dict.fromkeys(cuisine))
cuisine.insert(0, '-')
print(cuisine)

#list of expressions for selectbox output
expression_list = ["Hmm...I suggest you head to","Why don't you check out this place!","This seems like a good option for you","How about you try this place? I heard its gooood","YUM! CHECK THIS PLACE OUT","Decisions, decisions, let a badly written script decide for you instead! Check this out","You would LOVE this place","I recommend you try out this place!","This place will satisfy ALL your cravings"]

#cuisineselector
st.subheader("What are you in the mood for today?")
cuisineselector = st.selectbox("",cuisine)

if cuisineselector == '-':
    st.write("Select a cuisine from the dropdown menu to get started")
elif cuisineselector == 'American':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(American,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Chinese':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Chinese,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'French':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(French,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Fusion':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Fusion,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Greek':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Greek,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Italian':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Italian,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Japanese ':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Japanese,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Latin American':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Latin_American,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Levantine':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Levantine,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Mexican':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Mexican,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Qatari':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Qatari,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Southeast Asian':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Southeast_Asian,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Spanish':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Spanish,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Indian':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Indian,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
elif cuisineselector == 'Steakhouse':
    st.subheader(*random.sample(expression_list,k=1))
    st.write(*random.sample(Steakhouse,k=1))
    st.write("")
    st.write("")
    st.write("")
    st.button("Unsatisfied? Click me for more options!")
