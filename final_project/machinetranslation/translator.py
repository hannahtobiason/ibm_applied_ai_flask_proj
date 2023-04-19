'''
This module accesses Watson translator to translate english to french
and French to English
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
   version='2018-05-01',
   authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    This function returns translated text as a string in french from the inputed english string
    '''
    try:
        response = language_translator.translate(text=english_text,
            model_id='en-fr').get_result() #response is a json object


        #access the first translation from the list of translations
        french_text = response['translations'][0].get('translation')
        return french_text
    except ValueError: #handle incorrect input
        return 'text must be provided'

def french_to_english(french_text):
    '''
    This function returns a string in english translated from the inputed string in french
    '''
    try:
        response = language_translator.translate(text=french_text,
            model_id='fr-en').get_result() #response is a json object


        #access the first translation from the list of translations
        english_text = response['translations'][0].get('translation')
        return english_text
    except ValueError: #incorrect input
        return 'text must be provided'
