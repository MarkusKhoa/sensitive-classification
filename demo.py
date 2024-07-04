import streamlit as st
import numpy as np

from setfit import SetFitModel, SetFitTrainer

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

def main():
    saved_checkpoint = "KhoaUSA76/contrastive-sensitive-classification"
    loaded_model = load_model(saved_checkpoint)

    st.set_page_config(page_title = 'Testing Sensitive Sentences', page_icon=':books:')
    st.title("Testing Sensitive sentences")
    
    res_dict = {0: "normal", 1:"sensitive"}
    
    # Allow user question
    user_question = st.text_input("Ask a question")
    if user_question:
        prediction = predict(loaded_model=loaded_model, test_sents = user_question)
        st.write("Prediction: ", res_dict[prediction])
    
if __name__ == '__main__':
    main()