#import packages
import pandas as pd
import streamlit as st
import random
import base64

#hiding header
#hide_decoration_bar_style = '''
   # <style>
   # header {visibility: hidden;}
    #</style>'''

#st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

#adding images
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""<style>.stApp {{background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});background-size: cover}}</style>""",unsafe_allow_html=True)

add_bg_from_local('Five/background.JPG')

st.image('Five/header.JPG',width=700)

#loading qatareats dataset
df = pd.read_csv('Five/qatareatss.csv')

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

#list of expressions for selectbox output
expression_list = ["Hmm...I suggest you head to","Why don't you check out this place!","This seems like a good option for you","How about you try this place? I heard its gooood","YUM! CHECK THIS PLACE OUT","Decisions, decisions, let a badly written script decide for you instead! Check this out","You would LOVE this place","I recommend you try out this place!","This place will satisfy ALL your cravings"]

#cuisineselector
st.write("")
st.write("")
st.subheader("What are you in the mood for today?")
cuisineselector = st.selectbox(" ",cuisine,index=0)

col1,col2=st.columns([3,1])

with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    yay = st.button("Dinner plans set?")
    #nay = st.button("Unsatisfied? Click me for more options!")

with col1:
    if cuisineselector == '-':
        st.write("Select a cuisine from the dropdown menu to get started")
    elif cuisineselector == 'American'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(American,k=1))
        st.write("")
        st.write("")
        st.write("")
        #col1,col2,col3 = st.columns(3)
        #with col1:

        nay = st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Chinese'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Chinese,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'French'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(French,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Fusion'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Fusion,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Greek'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Greek,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Italian'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Italian,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Japanese 'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Japanese,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Latin American'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Latin_American,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Levantine'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Levantine,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Mexican'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Mexican,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Qatari'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Qatari,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Southeast Asian'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Southeast_Asian,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Spanish'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Spanish,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Indian'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Indian,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")
    elif cuisineselector == 'Steakhouse'and not yay:
        st.subheader(*random.sample(expression_list,k=1))
        st.write(*random.sample(Steakhouse,k=1))
        st.write("")
        st.write("")
        st.write("")
        nay =st.button("Unsatisfied? Click me for more options!")

#balloons!
if yay:
    col2.balloons()
    st.markdown("<h1 style='text-align: center; color: #f40257 ;'>Sa7tein!</h1>", unsafe_allow_html=True)

with st.expander("Kind reminder to always tip your waiters, expand for Tip Calculator"):
    st.image('Five/line.JPG')
    col4,col5=st.columns(2)
    col4.markdown("**Insert tip %**")
    slider =col4.slider("")
    col4.markdown("**Insert bill total**")
    bill= col4.text_input("  ")

#defining tip calculator functions
    def get_bill_total():
        entered_bill_total = bill
        #try and except block to handle exceptions and check if user entered a number
        try:
            bill_total = float(entered_bill_total)
        except ValueError:
            st.write("Incorrect value entered")
            return
        final_tip = calculate_tip(bill_total)
        st.write('QAR ' + str(final_tip))

    def calculate_tip(total):
        tip = float(total*slider/100)
        return tip



    if bill:
        get_bill_total()

# Footer, code source: https://discuss.streamlit.io/t/streamlit-footer/12181
footer= """<style>
a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: #f40257;
background-color: #f7e2d1;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #f7e2d1;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p> developed by <a style='text-align: center;' href="https://instagram.com/carsoncodes.py?igshid=YzA2ZDJiZGQ=">Sarah</a></p>
</div>
"""

st.markdown(footer,unsafe_allow_html=True)


#<p>made by <a style='display: block; text-align: center;' href="https://instagram.com/carsoncodes.py?igshid=YzA2ZDJiZGQ=" target="_blank">Sarah</a></p>
