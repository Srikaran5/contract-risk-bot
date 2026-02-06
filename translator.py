import re
import requests

HINDI_TO_ENGLISH_DICT = {
    "क्षतिपूर्ति": "Indemnity",
    "सेवा प्रदाता": "Service Provider",
    "कंपनी": "Company",
    "नुकसान": "Loss",
    "क्षति": "Damage",
    "कानूनी": "Legal",
    "खर्चों": "Expenses",
    "क्षेत्राधिकार": "Jurisdiction",
    "न्यायालय": "Court",
    "भारत": "India",
    "कानून": "Law",
    "अनुबंध": "Agreement",
    "समाप्त": "Terminate",
    "जुर्माना": "Penalty",
    "गैर-प्रतिस्पर्धा": "Non-Compete"
}

def offline_translate(text):
    translated = text
    for hi, en in HINDI_TO_ENGLISH_DICT.items():
        translated = re.sub(hi, en, translated)
    return translated

def translate_to_english(text):
    try:
        url = "https://translate.argosopentech.com/translate"
        payload = {
            "q": text,
            "source": "hi",
            "target": "en",
            "format": "text"
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        data = response.json()

        if "translatedText" in data and data["translatedText"] != text:
            return data["translatedText"]
        else:
            return offline_translate(text)

    except:
        return offline_translate(text)