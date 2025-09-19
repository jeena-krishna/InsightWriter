import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Getting response from llam2 model
def getllamaresponse(input_text, no_words, blog_style):

    ##llama 2 model
    llm = CTransformers(model = "models/llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type = 'llama',
                        config = {'max_new_tokens':256,
                                  'temperature': 0.01})
    # template
    template='''
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
'''

    promt=PromptTemplate(input_variables=['blog_style','input_text','no_words'],
                        template=template)
    
    # gereneating response from the llama2 model
    response = llm(promt.format(blog_style= blog_style,
                     input_text= input_text,
                     no_words= no_words))
    print(response)
    return response

st.set_page_config(
    page_title = "Generate blogs",
    page_icon = '👾',
    layout = 'centered',
    initial_sidebar_state = 'collapsed')

st.header("Generate Blogs 👾")

input_text = st.text_input("Enter Blog Topic")

#creating columns for additional fields
col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('no. of words') 

with col2:
    blog_style = st.selectbox('Writing Blog for: ', 
                              ('Researcher','Data Scientist','General Purpose'), index=0)
    
submit = st.button('Generate')

# Final Result
if submit:
    st.write(getllamaresponse(input_text, no_words, blog_style))