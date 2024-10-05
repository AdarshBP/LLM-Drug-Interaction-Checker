import streamlit as st
from transformers import pipeline

# Load a pre-trained model from Hugging Face (e.g., GPT-2 or GPT-J)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")  # You can replace gpt2 with a healthcare-specific model

# Initialize the model
model = load_model()

# Function to fetch drug interactions and side effects
def get_drug_interactions(medications):
    medications_str = ", ".join(medications)
    prompt = f"Identify potential interactions and side effects between the following medications: {medications_str}. Provide advice for safe usage."
    print("")
    # Generate response from Hugging Face model
    response = model(prompt, max_length=200, num_return_sequences=1)
    
    return response[0]["generated_text"]

# Streamlit UI
st.title("Drug Interaction and Side Effect Checker")

# Input for medications
medications_input = st.text_area("Enter the medications (separated by commas):", placeholder="e.g., Dolo 650, B-complex")

if st.button("Check Interactions"):
    if medications_input:
        # Parse the input into a list
        medications = [med.strip() for med in medications_input.split(",")]
        
        # Fetch interactions from the model
        with st.spinner('Checking interactions...'):
            result = get_drug_interactions(medications)
        
        # Display the result
        st.subheader("Results")
        st.write(result)
    else:
        st.error("Please enter at least one medication.")
