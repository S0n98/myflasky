from app import tran

def translate(text, source_language, des_language):
    result = tran.translate(text, src=source_language, dest=des_language)
    return result.text
