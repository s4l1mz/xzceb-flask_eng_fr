"""
Module with translator IBM Watson
"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('{url}}')

def english_to_french(english_text):
    """
    Method translate english texto to french
    """
    french_text = language_translator.translate(
    text='{english_text}',
    model_id='en-fr').get_result()
    print(english_text)
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text

def french_to_english(french_text):
    """
    Method translate english texto to french
    """
    english_text = language_translator.translate(
    text='{french_text}',
    model_id='fr-en').get_result()
    print(french_text)
    print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text
