import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_loaded = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### We need some information to predict the salary""")

    countries = {
    "United States of America", 
    "Germany",    
    "United Kingdom of Great Britain and Northern Ireland",    
    "India",    
    "France",    
    "Canada",    
    "Ukraine",    
    "Netherlands",    
    "Brazil",    
    "Italy",    
    "Spain",    
    "Australia",                
    }

    education = {
        'Master’s degree', 
        'Less than a Bachelors', 
        'Bachelor’s degree', 
        'Post grad'
    }

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education) 

    experience = st.slider("Years of Experience", 0, 100, 3)

    predict = st.button("Calculate Salary")           
    if predict:
        X = np.array([[country, education, experience ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor_loaded.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")