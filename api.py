from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from elt import translit

# define the FastAPI app
app = FastAPI()

# define the transliteration object
to_hindi = translit('hindi')

# define the request body
class InputText(BaseModel):
    text: str

# define the response body
class OutputText(BaseModel):
    text: str

# define the root endpoint
@app.get('/')
def home():
    return {'message': 'Welcome to the English to Hindi Transliteration API'}

# define the transliteration endpoint
@app.post('/transliterate/', response_model=OutputText)
def transliterate(input_text: InputText):
    output_text = to_hindi.convert([input_text.text])[0]
    return {'text': output_text}
