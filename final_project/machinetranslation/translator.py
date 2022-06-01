"""Translate text between English and French using IBM Watson
Language Translator.

Functions:
    english_to_french(string) -> string
    french_to_english(string) -> string
"""

import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

"""Create a translator instance"""
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

#'https://api.us-south.language-translator.watson.cloud.ibm.com'
language_translator.set_service_url(URL)

def english_to_french(english_text):
    """Translate English text to French and return it."""
    french_text = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """Translate French text to English and return it."""
    english_text = language_translator.translate(text=french_text, model_id="fr-en").get_result()
    return english_text.get("translations")[0].get("translation")
