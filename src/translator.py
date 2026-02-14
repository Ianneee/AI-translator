import src.config as config
from src.ollama_client import *
from src.utils import *
from ollama import Client

MODEL_NAME = config.MODEL_NAME
SOURCE_LANG = config.SOURCE_LANG
SOURCE_CODE = config.SOURCE_CODE
TARGET_LANG = config.TARGET_LANG
TARGET_CODE = config.TARGET_CODE

client = Client()


def translate_sentence(italian_sentence):
    template_message = [
        {
            'role': 'system',
            'content': f"You are a professional {SOURCE_LANG} ({SOURCE_CODE}) to {TARGET_LANG} ({TARGET_CODE}) translator. Your goal is to accurately convey the meaning and nuances of the original {SOURCE_LANG} text while adhering to {TARGET_LANG} grammar, vocabulary, and cultural sensitivities. Produce only the {TARGET_LANG} translation, without any additional explanations or commentary.\nTranslate the following {SOURCE_LANG} text into {TARGET_LANG}:",
        },
        {
            'role': 'user',
            'content': f"{italian_sentence}",
        },
    ]

    response = client.chat(MODEL_NAME, messages=template_message, stream=False)
    return response.message.content


def run_cli():
    pull_model(MODEL_NAME)

    print("Please provide the sentences you would like me to translate. Type 'exit' or 'quit' to exit.")

    while True:
        italian_sentence = input("> ").strip()
        if italian_sentence.lower() in ["exit", "quit", "q"]:
            print("Exiting...")
            break
        if italian_sentence == "":
            continue

        translation = translate_sentence(italian_sentence)
        copy_to_clipboard(translation)
        if translation:
            print("Translation:", translation)
        else:
            print("Translation failed")


if __name__ == "__main__":
    run_cli()
