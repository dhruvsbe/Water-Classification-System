import streamlit as st 
from streamlit_option_menu import option_menu 
import pickle 
import pandas as pd
from PIL import Image 
import time 
import os 
model = pickle.load(open("C:/Users/nikgu/Downloads/water.pkl", "rb"))
barwater = Image.open("C:/Users/nikgu/Downloads/Water Classifier Model.png")
st.image(barwater)




menu = option_menu(menu_title = None, options = ["Home", "Model", "The Data", "About Us"], 
default_index = 0, orientation="horizontal")      





def home():
    st.title("Home")  
    st.text("""Welcome to our water classifier and prediction app. Our model can 
accruately predict and classify water base on the features you provide us. 
Navigate to our model to test it out, for free. """)  

def network(): 
    st.title("Water Prediction App") 
    features =  ['uranium','radium','nitrates','chloramine','ammonia','silver','arsenic','perchlorate','cadmium','aluminium']
    try:
        predict = {}
        st.text("""Here is the water and classifier and prediction app. 
Below we use several characterisiitcs of water to determine the safety of drinking 
water. 1 indicates it is safefor human consumption and 0 indicates that the 
water is not safe AT ALL. """)
        st.text("Please type ONLY integers in the spaces prompted to determine the safety of your drinking water.") 
        st.text("Please click Enter after every entry.")

        for feature in features:
            val = st.text_input(feature)      
            predict[feature] = val 
        
        
        Button = st.button("Predict")
        if Button == True:
            predict = pd.DataFrame(predict, index=[0])

            output = model.predict(predict)  
            if output < 0.5:
                st.text(f"The grading of the water is {output}, meaning the water is unsafe.")
            elif output == 0.5:
                st.text(f"The grading of the water is {output}, meaning the water is unsafe.") 
            elif output > 0.5:
                st.text(f"The grading of the water is {output}, meaning the water is safe.")
             
    except ValueError:
        st.text("")

def data():
    st.title("Our Data")  
    st.text("""Shown below is the data used to model the water prediction and classifier model. 
We used the most important features and ommited the rest to increase user 
accessability.""")
    water_data = pd.read_csv("C:/Users/nikgu/Downloads/waterQuality1.csv") 
    st.dataframe(water_data)


def about():
    st.title("About Us")   
    st.text("""Nik and Dhruv are 2 highschoolers who are aspiring to be computer science engineers.
Dhruv is a senior who recently commited to Duke and Nik is a Junior hoping to commit to UVA. Both team
members decided to create a water prediction app because """)

if menu == "Home":
    home() 
elif menu == "Model":
    network()
elif menu == "The Data":
    data() 
elif menu == "About Us":
    about() 