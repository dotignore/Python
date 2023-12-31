def get_output_language(lang_in):
    language_mapping = {
        "af-ZA": "af",
        "ar-AE": "ar",
        "bn-IN": "bn",
        "bs": "bs",
        "ca-ES": "ca",
        "cs-CZ": "cs",
        "cy": "cy",
        "da-DK": "da",
        "de-DE": "de",
        "el-GR": "el",
        "en-US": "en",
        "en-GB": "en",
        "en-AU": "en",
        "eo": "eo",
        "es-ES": "es",
        "es-MX": "es",
        "et": "et",
        "fi-FI": "fi",
        "fr-FR": "fr",
        "fr-CA": "fr",
        "fil-PH": "fr",
        "gu": "gu",
        "hi-IN": "hi",
        "hr-HR": "hr",
        "hu-HU": "hu",
        "hy": "hy",
        "id-ID": "id",
        "is-IS": "is",
        "it-IT": "it",
        "ja-JP": "ja",
        "km": "km",
        "kn": "kn",
        "ko-KR": "ko",
        "la": "la",
        "lv": "lv",
        "mk": "mk",
        "ml": "ml",
        "mr": "mr",
        "my": "my",
        "ne": "ne",
        "nl-NL": "nl",
        "nb-NO": "no",
        "pl-PL": "pl",
        "pt-BR": "pt",
        "ro-RO": "ro",
        "ru-RU": "ru",
        "si": "si",
        "sk-SK": "sk",
        "sq": "sq",
        "sr-RS": "sr",
        "sv-SE": "sv",
        "sw": "sw",
        "ta": "ta",
        "te": "te",
        "th-TH": "th",
        "tr-TR": "tr",
        "uk-UA": "uk",
        "ur": "ur",
        "vi-VN": "vi",
        "cmn-Hant-TW": "zh-tw",
        "cmn-Hant-TW": "zh-cn"
    }
    return language_mapping.get(lang_in, lang_in)