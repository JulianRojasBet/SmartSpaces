import os
import openai

from typing import Dict, Any
import prompts
import json

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


def suggestions(request: Dict[str, Any]):
    comments = request["comments"]
    prompt = prompts.create_suggestions_prompt(comments)
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.2, max_tokens = 512)
    suggestion = json.loads(getattr(response["choices"][0],"text"))
    print(suggestion)
    return suggestion

    
def translate(request: Dict[str, Any]):
    sentence = request["sentence"]
    from_lang = request["from"]
    to_lang = request["to"]
    prompt = None
    if from_lang == "en" and to_lang == "es":
        prompt = prompts.create_translate_prompt_en_to_es(sentence)
    elif from_lang == "es" and to_lang == "en":
        prompt = prompts.create_translate_prompt_en_to_es(sentence)

    if prompt:
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens = 512)
        translation = {
            "original" : sentence,
            "translation" : getattr(response["choices"][0],"text")
        }
        return translation

if __name__ == "__main__":
    request = {
        "comments" : ["Realmente es un lugar que tiene una excelente ubicacion", "Me gustaria que mejoraran la iluminacion sobretodo de la sala", "Es un excelente lugar, de pronto la seguirdad del sector no es la mejor"]
    }
    suggestions(request)
