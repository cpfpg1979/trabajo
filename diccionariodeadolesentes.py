meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "YOLO": "solo vives una vez",
            "POV": "punto de vista",
            "WHEN": "cuando en ingles",
            "MEME": "chiste anonimo",
            "GOD": "soy bueno en algo",
            "NOOB": "ser malo en algo",}
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("esta palabra no se encuentra en el diccionario")
        a = input("ingresa el significado de la palabra...")
        meme_dict[word]=a
