# LLM-Drug-Interaction-Checker

A Streamlit-based application that uses Large Language Models (LLMs) from Hugging Face to detect potential drug-drug interactions and side effects. This app allows users to input medications and provides detailed information on interactions and side effects, aiding in safe medication usage.

## Features
- Detects drug-drug interactions based on user input.
- Uses free foundation models from Hugging Face (e.g., GPT-2, GPT-J, BioGPT).
- Simple UI powered by Streamlit for user-friendly interaction.

## Tech Stack
- **Streamlit**: Fast and easy app deployment.
- **Hugging Face Transformers**: Utilized for language models.
- **Python**: Backend logic.
- **Hugging Face Models**: GPT-2, GPT-J, or healthcare-specific models like BioGPT.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LLM-Drug-Interaction-Checker.git
   cd LLM-Drug-Interaction-Checker
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
3. Run the Streamlit app:
    ```bash
    streamlit run app.py


## Usage

- After running the app, navigate to the local URL provided by Streamlit.
- Input the medications you want to check for interactions, separated by commas.
- Press the "Check Interactions" button to get results on potential drug-drug interactions and side effects.
