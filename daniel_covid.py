##### Author: NYAMWEYA DANIEL AKAMA.
##### Project Title: COVID-19 SELF-DIAGNOSIS PREDICITON WEB APPLICATION.
##### Project Description: The web application allows one to enter the symptoms they present and it predicts
                            # whether they are Covid positive or not.


# import needed libraries.

import streamlit as st
import joblib  # used to load the model into the app

# load the model
covid_classifier = joblib.load('svc_covid.pkl')


# we'll define 2 functions:
# 1. prediction generator.
# 2. the main function.

# 1. prediction generator
# its input is the columns of the dataset we trained the model using


def prediction_generator(cough, fever, sore_throat, shortness_of_breath,
                         head_ache, age_60_and_above, gender):
    """function that takes the parameters and predicts if someone has covid or not"""

    # the classifier takes in data as a 1 dimensional array.
    prediction = covid_classifier.predict([[cough, fever, sore_throat, shortness_of_breath,
                                            head_ache, age_60_and_above, gender]])

    # Mapping the output with the result.
    if prediction == 0:
        output = 'NEGATIVE.'
    elif prediction == 1:
        output = 'POSITIVE.'
    else:
        output = 'OTHER'

    return output


# now for the main function
# the main function handles the web app
# user enters his/her symptoms then the prediction generator is called and gives the output.

def main():
    """handles the layout of web app"""

    st.title('COVID-19 Self-Diagnosis Prediction Application.')

    # one selects an option from the dropdown menu if they display the symptom or not.

    # cough
    cough = st.selectbox('Do you have a Cough?', ('Yes', 'No'))
    if cough == 'Yes':
        cough = 1
    else:
        cough = 0

    # fever
    fever = st.selectbox('Are you experiencing Fever?', ('Yes', 'No'))
    if fever == 'Yes':
        fever = 1
    else:
        fever = 0

    # sore_throat
    sore_throat = st.selectbox('Do you have a Sore Throat?', ('Yes', 'No'))
    if sore_throat == 'Yes':
        sore_throat = 1
    else:
        sore_throat = 0

    # shortness_of_breath
    shortness_of_breath = st.selectbox('Are you experiencing a Shortness in Breath?', ('Yes', 'No'))
    if shortness_of_breath == 'Yes':
        shortness_of_breath = 1
    else:
        shortness_of_breath = 0

    # head_ache
    head_ache = st.selectbox('Are you experiencing a headache?', ('Yes', 'No'))
    if head_ache == 'Yes':
        head_ache = 1
    else:
        head_ache = 0

    # verifying the age
    age_60 = st.selectbox('Are you over the age of 60?', ('Yes', 'No'))
    if age_60 == 'Yes':
        age_60 = 1
    else:
        age_60 = 0

    # gender
    gender = st.selectbox('Select gender', ('Male', 'Female', 'Other'))
    if gender == 'Male':
        gender = 1
    elif gender == 'Female':
        gender = 0
    else:
        gender = 2

    # button that displays the result when pressed.

    if st.button('Get Result'):
        result = prediction_generator(cough, fever, sore_throat, shortness_of_breath, head_ache, age_60,
                                      gender)
        st.success('You are COVID-19 {0}'.format(result))


if __name__ == '__main__':
    main()


############### THE END SHUKRAN. ################