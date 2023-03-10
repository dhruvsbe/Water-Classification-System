import streamlit as st 
from streamlit_option_menu import option_menu 
import pickle 
import pandas as pd
from PIL import Image 
model = pickle.load(open("C:/Users/nikgu/Downloads/water.pkl", "rb"))
barwater = Image.open("C:/Users/nikgu/Downloads/Water Classifier Model (1).png")
st.image(barwater)

image = Image.open("C:/Users/nikgu/Downloads/IndianW.jpeg") 
imagetwo = Image.open("C:/Users/nikgu/Downloads/developing-countries-clean-water.jpg")



menu = option_menu(menu_title = None, options = ["Home", "Classifier", "The Data", "About Us"], 
default_index = 0, icons = ["house", "hdd-network", "clipboard-data", "people-fill"], orientation="horizontal")      





def home():
    st.title("Home")  
    st.text("""Welcome to our machine learning water classification app. This system can 
accurately classify water as drinkable or non-drinkable based on scientifically 
measurable factors that are inputted. Please use the menu bar above to navigate 
to our classifier page and test it out for free. """)  
    st.text("") 
    st.text("")
    st.image(imagetwo)
def network(): 
    st.title("Water Potability Classification") 
    features =  ['uranium','radium','nitrates','chloramine','ammonia','silver','arsenic','perchlorate','cadmium','aluminium']
    try:
        predict = {}
        st.text(""" This system was trained using a random forest classification model and a large
dataset which can be seen on the next page. Based on the input of several 
scientific measurements of water, this system is able to determine the 
potability of water at a 97% accuracy. An output of "[1.]" indicates 
it is drinkable and an output of "[0.]" indicates that the water is NOT 
drinkable. """)
        st.text(""" Example inputs that result in the prediction of drinkable water: 
        0.02, 6.78, 16.08, 0.35, 9.08, 0.34, 0.04, 37.75, 0.007, 1.65 """)
        st.text(""" Example inputs that result in the prediction of non-drinkable water: 
        0.01, 7.07, 14.16, 4.24, 14.02, 0.44, 0.04, 50.28, 0.008, 1.01 """)

        for feature in features:
            val = st.text_input(f"{feature} levels") 
            predict[feature] = val 
        
        
        Button = st.button("Predict")
        if Button == True:
            predict = pd.DataFrame(predict, index=[0])

            output = model.predict(predict)  
            if output == 0.:
                st.text(f"Based on the levels inputted, the model predicted of the water is {output}.")
                st.text("This data indicates the water is NOT safe to drink.")
            elif output == 1.:
                st.text(f"Based on the levels inputted, the grading of the water is {output}.")
                st.text("This data indicates the water is safe to drink.")
             
    except ValueError:
        st.text("")

def data():
    st.title("Our Data")  
    st.text("""Shown below is the data used to train the system. After using sklearn to discover 
the most important features in the dataset, we only used the top 10 most 
important features and omitted the rest to increase the ease of use and 
user accessibility.""")
    water_data = pd.read_csv("C:/Users/nikgu/Downloads/waterQuality1.csv") 
    st.dataframe(water_data)


def about():
    st.title("About Us")   
    st.text("""Nik and Dhruv are 2 highschoolers who are working to be innovative entrepreuners and
aspire to positively change the world using machine-learning and deep-learning. 
Dhruv is a senior who recently committed to Duke and Nik is a junior hoping to
commit to UVA. Both team members decided to create a water prediction app because
this is a large problem for disadvantaged communities in third-world countries. 
In the future, we hope to continue working on this project and potentially partner 
with a non-profit organization to scale this functional solution to this important
problem.""")
    st.text("") 
    st.text("")
    st.image(image)

if menu == "Home":
    home() 
elif menu == "Classifier":
    network()
elif menu == "The Data":
    data() 
elif menu == "About Us":
    about() 
