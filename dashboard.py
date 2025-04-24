import streamlit as st
from password_generator import RandomPasswordGenerator, MemorablePasswordGenerator, PinCodeGenerator
from nltk.corpus import words

# Title of the Application
st.image('./images/image1.png', width = 400)
st.title(":zap: Password Generator")

option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))

if option == 'Random Password':
    length = st.slider("Length", min_value=5, max_value=50, value=8)
    include_numbers = st.toggle("Include Numbers")
    include_symbole = st.toggle("Include Symbole")

    generator = RandomPasswordGenerator(length, include_numbers, include_symbole)

elif option == 'Memorable Password':
    number_of_words = st.slider ("Number of Words:",min_value=2, max_value=10, value=5)
    separator = st.text_input('Separator', value='-')
    capitalization = st.toggle('Capitalization')

    generator = MemorablePasswordGenerator(number_of_words,separator, capitalization, words.words())

else:
    length = st.slider('Length of password:',min_value=2, max_value=10, value=4)
    generator = PinCodeGenerator(length)


password = generator.generate()
st.write('Your Password is:')
st.header(fr"``` {password} ```")
