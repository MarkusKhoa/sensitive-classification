import streamlit as st
import numpy as np
import pandas as pd
import os

from setfit import SetFitModel
from database import init_mongo_collection

@st.cache_resource
def load_model(saved_checkpoint):
    return SetFitModel.from_pretrained(saved_checkpoint)

def predict(loaded_model, test_sents):
    predictions = loaded_model.predict(test_sents).tolist()
    return predictions

def evaluate_model(predictions, test_labels):
    predictions = np.array(predictions)
    test_labels = np.array(test_labels)
    accuracy = (predictions == test_labels).mean()
    return accuracy

def save_feedback(data, file_path):
    df = pd.DataFrame([data])  # Create a DataFrame with the new data
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)  # Append to the existing file
    else:
        df.to_csv(file_path, index=False)  

def main():
    # First Streamlit command: set_page_config
    st.set_page_config(page_title='Testing Sensitive Sentences', page_icon=':books:')
    st.title("Testing Sensitive sentences")
    
    db_collection = init_mongo_collection()
    saved_checkpoint = "KhoaUSA76/contrastive-sensitive-classification"
    loaded_model = load_model(saved_checkpoint)
    res_dict = {0: "normal", 1: "sensitive"}
    
    # Allow user question
    user_question = st.text_input("Ask a question")
    if user_question:
        prediction = predict(loaded_model=loaded_model, test_sents=user_question)
        st.write("Prediction: ", res_dict[prediction])
        
        feedback_label = st.radio("Is this prediction correct?", ("Yes", "No"))
        if st.button("Submit Feedback"):
            feedback_data = {
                "text": user_question,
                "prediction": res_dict[prediction],
                "feedback": feedback_label
            }
            # file_path = os.path.abspath("official_feedback_data.csv")
            # save_feedback(data = feedback_data, file_path = file_path)
            db_collection.insert_one(feedback_data)
            st.success("Feedback submitted")
    
if __name__ == '__main__':
    main()