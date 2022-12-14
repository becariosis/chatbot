# CREDITOS: Programado por Jose Pablo Ibarra Medrano el 12/12/2022
# © 2022 Desarrollo y Mantenimiento por: Jose Pablo Ibarra Medrano

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

# Creamos nuestra funcion ActionCarousel para que nuestro bot pueda dar varias preguntas como posibles respuesta.
class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_carousels"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "IP/MAC",
                        "subtitle": "Encontrar la IP o MAC de tu dispositivo",
                        "image_url": "images/IP.jpg",
                        "buttons": [ 
                            {
                            "title": "Identifica tu IP o MAC",
                            "payload": "ip",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Duda 2",
                        "subtitle": "Encuentra tu ....",
                        "image_url": "https://image.freepik.com/free-vector/city-illustration_23-2147514701.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://image.freepik.com/free-vector/city-illustration_23-2147514701.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

# Creamos nuestra funcion ActionCarousel para que nuestro bot pueda dar varias preguntas como posibles respuesta.
class ActionResolve(Action):
    def name(self) -> Text:
        return "action_resolve"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "¿Solucionó tu problema?",
                        "image_url": "images/duda.png",
                        "buttons": [ 
                            {
                            "title": "Si",
                            "payload": "/agradecimiento",
                            "type": "postback"
                            },
                            {
                            "title": "No",
                            "payload": "/enojo",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []