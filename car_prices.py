
import streamlit as st
import joblib  # used to load the model into the app
import streamlit as st  # for the web app


# load the model
car_predictor = joblib.load('gb_cars.pkl')


def prediction_generator(car_model, Mileage, age_in_years):

    """function to predict sell price of the car"""

    predictor = car_predictor.predict([[car_model, Mileage, age_in_years]])  # 1D array

    if predictor:
        return predictor


def main_func():
    """handles the layout of the web app"""

    st.title('Car Selling Price Prediction App')

    # enter the car model, its mileage and age in years.

    # car model
    model = st.selectbox('Select the car model', ('BMW X5', 'AUDI A5', 'Mercedez Benz C class'))
    if model == 'BMW X5':
        model = 1
    elif model == 'AUDI A5':
        model = 0
    else:
        model = 2

    mileage = st.slider('Enter the cars mileage:', 20000, 100000)

    age = st.slider('Enter age of car:', 1, 10)

    # button that does the prediction.
    if st.button('Sell Price'):
        result = prediction_generator(model, mileage, age)
        st.success('Selling Price of the car: {0}$'.format(result))


if __name__ == main_func():
    main_func()
