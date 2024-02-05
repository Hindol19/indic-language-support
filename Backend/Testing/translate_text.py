from googletrans import Translator
from langdetect import detect


def translate_to_english(text):
    translator = Translator()

    source_language = detect(text)
    translation = translator.translate(text, src=source_language, dest='en')

    return translation.text


# Example usage:
text_to_translate = "Kemon acho?"
translated_text = translate_to_english(text_to_translate)
print(f"Original text: {text_to_translate}")
print(f"Translated text: {translated_text}")
