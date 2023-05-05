import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('yWO-Q37IixICnVIaBZ3IsII82P4CckjCWAZjNOVqFphw')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/df8c3549-be32-42d1-b0d9-be069c5ca484')
language_translator.set_disable_ssl_verification(True)

def englishtofrench(englishtext):
    #write the code here
    translation = language_translator.translate(
    text = englishtext,
    model_id = 'en-fr').get_result()
    frenchtext = translation['translations'][0]['translation']
    return frenchtext

def frenchtoenglish(frenchtext):
    #write the code here
    translation = language_translator.translate(
    text = frenchtext,
    model_id = 'fr-en').get_result()
    englishtext = translation['translations'][0]['translation'] 
    return englishtext

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))



