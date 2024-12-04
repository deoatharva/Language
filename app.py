import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Mapping of supported languages to gTTS language codes
LANGUAGE_CODE_MAP = {
    'english': 'en',
    'hindi': 'hi',
    'french': 'fr',
    'german': 'de',
    'spanish': 'es',
    'italian': 'it',
    'portuguese': 'pt',
    'russian': 'ru',
    'chinese': 'zh',
    'japanese': 'ja',
    'arabic': 'ar',
    'korean': 'ko',
    'turkish': 'tr',
    'dutch': 'nl',
    'swedish': 'sv',
    'norwegian': 'no',
    'danish': 'da',
    'polish': 'pl',
    'romanian': 'ro',
    'finnish': 'fi',
    'hungarian': 'hu',
    'czech': 'cs',
    'slovak': 'sk',
    'ukrainian': 'uk',
    'greek': 'el',
    'belarusian': 'be',
    'serbian': 'sr',
    'bulgarian': 'bg',
    'croatian': 'hr',
    'slovenian': 'sl',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'estonian': 'et',
    'maltese': 'mt',
    'icelandic': 'is',
    'basque': 'eu',
    'galician': 'gl',
    'catalan': 'ca',
    'turkish': 'tr',
    'vietnamese': 'vi',
    'thai': 'th',
    'indonesian': 'id',
    'malay': 'ms',
    'filipino': 'tl',
    'swahili': 'sw',
    'zulu': 'zu',
    'xhosa': 'xh',
    'afrikaans': 'af',
    'klingon': 'tlh',
    'esperanto': 'eo',
    'yiddish': 'yi',
    'hebrew': 'he',
    'bengali': 'bn',
    'gujarati': 'gu',
    'marathi': 'mr',
    'tamil': 'ta',
    'telugu': 'te',
    'urdu': 'ur',
    'malayalam': 'ml',
    'kannada': 'kn',
    'punjabi': 'pa',
    'nepali': 'ne',
    'sinhala': 'si',
    'bhojpuri': 'bho',
    'haryanvi': 'hrv',
    'assamese': 'as',
    'odia': 'or',
    'maithili': 'mai',
    'sindhi': 'sd',
    'kurdish': 'ku',
    'tigrinya': 'ti',
    'amharic': 'am',
    'somali': 'so',
    'mayan': 'es',
    'mongolian': 'mn',
    'georgian': 'ka',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'kyrgyz': 'ky',
    'tajik': 'tg',
    'uzbek': 'uz',
    'turkmen': 'tk',
    'pashto': 'ps',
    'dari': 'fa',
    'swahili': 'sw',
    'maori': 'mi',
    'samoan': 'sm',
    'fijian': 'fj',
    'tongan': 'to',
    'hawaiian': 'haw',
    'javanese': 'jv',
    'balinese': 'ban',
    'basa': 'ban',
    'romani': 'ro',
}


# Streamlit App Title
st.title("Language Translator with Voice")

# Input Text
text_to_translate = st.text_area("Enter text to translate:")

# Get Supported Languages
translator = GoogleTranslator(source='auto', target='en')
languages = translator.get_supported_languages()

# Language Selection
source_language = st.selectbox("Select source language:", ["auto"] + languages)
target_language = st.selectbox("Select target language:", languages)

if st.button("Translate"):
    if text_to_translate.strip():
        try:
            # Translation
            translated_text = GoogleTranslator(source=source_language, target=target_language).translate(text_to_translate)
            st.success(f"Translated Text: {translated_text}")
            
            # Get the language code for gTTS
            gtts_lang_code = LANGUAGE_CODE_MAP.get(target_language.lower(), None)
            
            if gtts_lang_code:
                # Generate Speech
                tts = gTTS(text=translated_text, lang=gtts_lang_code)
                audio_file = "translated_audio.mp3"
                tts.save(audio_file)
                
                # Play Audio
                audio_bytes = open(audio_file, "rb").read()
                st.audio(audio_bytes, format="audio/mp3", start_time=0)

                # Provide Download Option
                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name=f"{target_language}_translation.mp3",
                    mime="audio/mp3"
                )
            else:
                st.error(f"Sorry, the language '{target_language}' is not supported for voice generation.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter text to translate.")
