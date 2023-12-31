import streamlit as st
import joblib
import os
import sklearn

# Get the path to the model.joblib file
model_path = os.path.join('frontend', 'intent_classifier.joblib')
intent_classifier = joblib.load(model_path)

# Streamlit app title
st.title('Intent Prediction App')

# Create a text input widget for user input
user_input = st.text_input('Enter a sentence:', '')
# Define a mapping from numerical predictions to labels
intent_mapping = {
    0: 'payment',
    1: 'order',
    2: 'cancel/modify',
    3: 'info'
}
# Create a button to trigger intent prediction
if st.button('Predict Intent'):
    if user_input:
        # Make a prediction using the loaded model
        intent = intent_classifier.predict([user_input])[0]
        # Map the numerical prediction to the corresponding label
        intent_label = intent_mapping.get(intent, 'Unknown')

        # Display the predicted intent
        st.success(f'Predicted Intent: {intent}')
        st.success(f'Predicted Intent: {intent_label}')
    else:
        st.warning('Please enter a sentence to predict the intent.')
