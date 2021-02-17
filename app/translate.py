from app import tran

def translate(text, source_language, des_language):
    result = tran.translate(text, lang_src=source_language, lang_tgt=des_language)
    return result
