# Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma como argumentos. O idioma é opcional e padrão para "inglês". A função deve retornar uma saudação no idioma especificado.

def saudacao_personalizada(nome, idioma):
    if idioma == 'fr':
        print(f'Bonjour {nome}')
    if idioma == "ptbr":
        print(f'Olá {nome}')
    else:
        print(f'Hello there {nome}!')
saudacao_personalizada("Gabriel", "fr")
saudacao_personalizada("Gabriel", "ptbr")
saudacao_personalizada("Gabriel", '')
