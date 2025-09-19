# InsightWriter: Blog Generation with LLMs

InsightWriter is a content creation tool that uses the Llama2-7B-Chat-GGML model to generate blog posts based on user inputs. Users can provide the topic, specify the desired word count, and choose the audience category (researcher, data scientist, or general) for tailored content.

## Llama2-7B-Chat-GGML Model
The Llama2-7B-Chat-GGML model is a fine-tuned version of the Generative Pre-trained Transformer (GPT) architecture, optimized for conversational responses and general text generation tasks. With 7 billion parameters, the model is capable of generating high-quality, contextually accurate text across various domains. InsightWriter leverages this model to power its blog generation capabilities.

## Model Download

To use the Llama2-7B-Chat-GGML model locally, download the pre-trained model from the following link:

[Download Llama2-7B-Chat-GGML Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)

## Installation

To set up InsightWriter on your local machine, follow these steps:

- Clone this repository to your local machine.
- Navigate to the project directory
- Install the required libraries by running:
   ```pip install -r requirements.txt```

## Usage

1. After setting up the project locally, navigate to the project directory.
2. Launch the application using Streamlit:
   ```streamlit run app.py```
3. Open your web browser and go to http://localhost:8501.
4. Enter the topic, word count, and audience category.
5. Click on the "Generate Blog" button to generate the blog content.

## Libraries Used


- sentence-transformers
- uvicorn
- ctransformers
- langchain
- python-box
- streamlit
