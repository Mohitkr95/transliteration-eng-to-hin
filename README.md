# Transliteration: English to Hindi

This repository contains the code for an English to Hindi transliteration model implemented in TensorFlow. It also includes a web application built using Streamlit and FastAPI.

## Requirements
* Python 3.7 or later
* TensorFlow 2.x
* Streamlit
* FastAPI
* Uvicorn

### Link to App - https://mohitkr95-transliteration-eng-to-hin-app-yt0jjq.streamlit.app/

![image](https://user-images.githubusercontent.com/37563886/227764842-3a037086-89f5-42ee-881a-aba4d291acc0.png)

## Installation
Clone this repository to your local machine.

```git clone https://github.com/Mohitkr95/transliteration-eng-to-hin.git```

Install the required Python libraries.

```pip install -r requirements.txt```

Usage

### Streamlit App
To launch the Streamlit app, navigate to the repository directory and run the following command:

```streamlit run app.py```

The app will launch in your web browser at http://localhost:8501.

### FastAPI Server

To launch the FastAPI server, navigate to the repository directory and run the following command:

```uvicorn api:app --reload```

The server will launch and start listening for requests at http://localhost:8000.
