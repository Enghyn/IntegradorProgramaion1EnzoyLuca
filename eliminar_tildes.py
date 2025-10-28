import unicodedata

#esta función, usando la librería unidodedata, remplaza las tildes de la palabra puesta como parametro.
def sin_tilde(texto:str):
    texto = texto.lower()
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_sin_tildes