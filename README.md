## Transliteration: English to Hindi

This repository contains the code for an English to Hindi transliteration model implemented in TensorFlow. It also includes a web application built using Streamlit and FastAPI.

Requirements
Python 3.7 or later
TensorFlow 2.x
Streamlit
FastAPI
uvicorn

Installation
Clone this repository to your local machine.
bash
Copy code
git clone https://github.com/Mohitkr95/transliteration-eng-to-hin.git
Install the required Python libraries.
bash
Copy code
pip install -r requirements.txt
Usage
Streamlit App
To launch the Streamlit app, navigate to the repository directory and run the following command:

bash
Copy code
streamlit run app.py
The app will launch in your web browser at http://localhost:8501.

FastAPI Server
To launch the FastAPI server, navigate to the repository directory and run the following command:

bash
Copy code
uvicorn api:app --reload
The server will launch and start listening for requests at http://localhost:8000.
