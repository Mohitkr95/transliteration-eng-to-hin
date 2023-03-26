import streamlit as st
from elt import translit

# Set transliteration language
to_hindi = translit('hindi')

# Define app layout
st.set_page_config(page_title='English to Hindi Transliteration', page_icon='🌐')
st.title('English to Hindi Transliteration')
st.markdown('''
            📝 *Transliteration* is the process of converting text from one script to another 
            script while keeping the pronunciation and meaning of the words intact. This app 
            allows you to transliterate English text to Hindi text using the most accurate 
            pre-trained model available.
            ''')

# Get user input
user_input = st.text_area('Enter English text', height=150)

# Transliterate user input on button press
if st.button('Transliterate'):
    if user_input:
        transliterated_text = to_hindi.convert([user_input])[0]
        st.markdown('---')  # Add horizontal line after output
        st.success('Transliterated Text:')
        st.write(transliterated_text)