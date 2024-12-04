import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Custom Sanskrit Translator (Basic Example)
sanskrit_translations = {
    "hello": "नमः",
    "world": "विश्वम्",
    "how are you?": "भवान् कथं अस्ति?",
    "goodbye": "विदाय",
    "thank you": "धन्यवाद",
    "please": "कृपया",
    "yes": "आम्",
    "no": "नाहम्",
    "hello world": "नम विश्वम्",
    "hi": "नमस्कार।",
    "How are you?": "भवान्‌ कथमसि?",
    "I am fine. And you?": "अहं कुशलं अस्मि। त्वं अपि?",
    "What is your name?": "भवतः नाम किमस्ति?",
    "my name is atharva": "मम नाम अथर्व",
    "I am pleased to meet you.": "अहं भवन्तं मिलित्वा प्रसन्नः अस्मि।",
    "Thank you.": "धन्यवाद।",
    "You are welcome.": "भवतः स्वागतम्‌।",
    "Please.": "कृपया।",
    "Excuse me.": "क्षमा प्रयच्छ मे।",
    "Sorry.": "क्षम्यताम्‌।",
    "Yes.": "आम्‌।",
    "No.": "नहि।",
    "Today is a nice day, is not it?": "अद्य सुन्दरः दिवसः अस्ति, किं न ?",
    "Where are you from?": "भवान्‌ कुतः अस्ति?",
    "I am from …": "अहं … अस्मि",
    "Do you live here?": "भवान् अत्र निवसति वा ?",
    "Do you like it here?": "अत्र भवतः रोचते वा ?",
    "Yes, I like it here.": "आम्, अत्र मम रोचते।",
    "How long are you here for?": "कियत्कालं यावत् अत्र असि ?",
    "I am here for three days / weeks.": "अहं त्रयः दिवसाः / सप्ताहान् यावत् अत्र अस्मि।",
    "Where are you going?": "कुत्र गच्छसि ?",
    "I am going to …": "अहं … कर्तुं गच्छामि।",
    "How old are you?": "भवतः वयः कियत्‌?",
    "I Love you": "त्वां कामयामि",
    "Welcome": "स्वागतम्‌",
    "I am fine and you?": "अहं कुशलः त्वं च ?",
    "My name is Kailash": "मम नाम कैलाशः",
    "Pleased to meet you": "भवन्तं मिलित्वा प्रसन्नः",
    "Do you speak English?": "भवान् आङ्ग्लभाषां वदति वा ?",
    "I do not speak Sanskrit well": "अहं संस्कृतं सम्यक् न वदामि",
    "I do not understand": "मया मा विदते",
    "Please speak slowly": "कृपया मन्दं वदतु",
    "Where are the restrooms?": "शौचालयाः कुत्र सन्ति ?",
    "Can I change money?": "अहं धनं परिवर्तयितुं शक्नोमि वा ?",
    "How much is this?": "कियत् एतत् ?",
    "It is too expensive!": "अतीव महत् अस्ति !",
    "Please say it again": "कृपया पुनः वदतु",
    "Left": "वाम",
    "Right": "दक्षिण",
    "Straight": "सीधा"
}


def translate_to_sanskrit(text):
    return sanskrit_translations.get(text.lower(), "Translation not available")

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
st.title("Language Translator")

# Input Text
text_to_translate = st.text_area("Enter text to translate:")

# Get Supported Languages
translator = GoogleTranslator(source='auto', target='en')
languages = translator.get_supported_languages()

# Language Selection for Source and Target
source_language = st.selectbox("Select source language:", ["auto"] + languages)
target_language = st.selectbox("Select target language:", languages)

# Button for Translation
if st.button("Translate"):
    if text_to_translate.strip():
        # If source language is auto, detect it using the GoogleTranslator
        if source_language == "auto":
            detected_language = GoogleTranslator(source='auto', target='en').detect(text_to_translate)
        else:
            detected_language = source_language

        # Translate text to the selected target language
        translated_text = GoogleTranslator(source=detected_language, target=target_language).translate(text_to_translate)

        # Display translated text
        st.success(f"Translated Text ({target_language}): {translated_text}")
        
        # Convert translated text to speech (only for supported languages)
        gtts_lang_code = LANGUAGE_CODE_MAP.get(target_language.lower(), None)
        
        if gtts_lang_code:
            # Generate Speech for translated text
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
    else:
        st.warning("Please enter text to translate.")

# Button for Sanskrit Translation
if st.button("Translate to Sanskrit"):
    if text_to_translate.strip():
        translated_text = translate_to_sanskrit(text_to_translate)
        st.success(f"Translated Text (Sanskrit): {translated_text}")
        st.warning("English to Sanskrit translation is available, but voice feature is not supported for Sanskrit.")
    else:
        st.warning("Please enter text to translate.")
