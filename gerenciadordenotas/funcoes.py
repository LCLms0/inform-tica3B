def calcular_media(listanotas):
    soma = sum(listanotas)
    media = soma / 3
    return media

def verificar_situacao(media):
    if media >= 7:
        print("aprovado")
    if media < 5 <= 6.9 :
        print("recuperação")
    if media < 5:
        print("Reprovado")

