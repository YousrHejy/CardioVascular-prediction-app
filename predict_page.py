
import streamlit as st
import pickle  
import numpy as np

def load_model():
    with open('Predict_model.pkl', 'rb') as file:
        data = pickle.load(file)  
        mlp_loaded=data["model"]  
    return mlp_loaded

Mode=load_model()


def show_predict_page():
    st.title("""Cardiovascular Disease Detection""")
    st.write("""We need some information to predict the disease""")
    st.write("""So please fill this form""")


    
    # gender=(1,2)
    type={
        "male",
        "Female",
    } 
    # cholestrol=(1,2,3)
    CHOL={
        "Normal",
        "Above Normal",
        "Well Above Normal",
    }
    # glucose=(1,2,3)
    Gol={
        "Normal",
        "Above Normal",
        "Well Above Normal",
    }
    # Smoke=(0,1)
    smoking={
        "Non-Smoking",
        "Smoking",
    }
    # alco=(0,1)
    Alchol={
        "Non-Alcoholic",
        "Alcoholic",
    }
    # active=(0,1)
    Activation={
        "Non-Active",
        "Active",
    }
    age=st.number_input("Age")
    gender=st.selectbox("Gender",type)  
    if gender=="male":
        Gender=1
    else :
        Gender=2     
    weight=st.number_input("Weight in (KG)")
    api_hi=st.number_input("Systolic Blood Pressure")
    api_lo=st.number_input("Dystolic Blood Pressure")
    Cholestrol=st.selectbox("Cholestrol level",CHOL)
    if Cholestrol=="Normal":
        Chol=1
    elif Cholestrol=="Above Normal":
        Chol=2
    else :
        Chol=3
    glucose=st.selectbox("Glucose level",Gol)
    if glucose=="Normal":
        Glucose=1
    elif glucose=="Above Normal":
        Glucose=2
    else :
        Glucose=3

    Smoke=st.selectbox("Smoking",smoking)
    if Smoke=="Non-Smoking":
        smoke=0
    else :
        smoke=1

    Alco_h=st.selectbox("Alchole intake",Alchol)
    if Alco_h=="Non-Alcoholic":
        Alco=1
    else :
        Alco=2
    Active_h=st.selectbox("Physical Activity",Activation)
    if Active_h=="Non-Active":
        Active=1
    else :
        Active=2            


    ok=st.button("Predict")
    if ok:
        X=[[age,Gender,weight,api_hi,api_lo,Chol,Glucose,smoke,Alco,Active]]
        # mlp_loaded = data["model"]
        Prediction=Mode.predict(X)
        if Prediction[0]==1:
            st.subheader(f"The patient unfortenattly have the disease")
        else :
            st.subheader(f"The patient doesn't have the disease")

        # st.subheader(f"Prediction of the disease is {Prediction[0]}")