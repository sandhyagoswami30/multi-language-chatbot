from deep_translator import GoogleTranslator

def translate_text(text, source_lang="auto", target_lang="en"):
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        return f"Translation Error: {e}"