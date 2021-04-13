# NER-Streamlit-App

This is a web based app in which one can visualize the output of the result of Name Entity Recognition. There can two inputs to the app - 
1. Providing a keyword search or any search of choice in the main page, where results are fetched automatically from the wikipedia.
2. Providing a sentence in the input box manually to visualize the output diagramatically

## How to run the app

1. Either fork or download the git as a zip and open the folder in the CLI. To edit or see the code, I preferably open the folder in the VS code editor.
2. Requirements are fulfilled using the pip in the CLI or terminal.
3. We then import the required libraries especially the streamlit
4. Defining the choices in the main function for the user inputs, we run the app which will be served in the web browser (preferably the chrome browser), by typing in ( streamlit run app.py ) in the terminal

## How to use

The app is structured in a serial manner for visualizing various output to the given input. Tap into the live url of the deployed project or run the cli command in the terminal. In the main page of the Wiki Search, there will be buttons presented that be activated, after performing a search in the input box. Else if having a sentence to analyse, then go to left sidebar and choose "Analyse a sentence" option to do so. 

## Features

- Streamlit app which is responsive to any device
- Deployed app, just needs a url to run the app
- Uses the concept of forming RESTful API using Flask
- Show annotated text based on various entities
- Customize our very own entity

## Dependencies

- en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0-py3-none-any.whl
- wikipedia
- wikipedia-api
- streamlit>=0.80.0
- spacy-streamlit
- datetime
- sumy
- spacy>=0.8.1

## Live Project URL

https://ner-streamlit-appy.herokuapp.com/
