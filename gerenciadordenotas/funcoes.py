def calcular_media(listanotas):
    soma = sum(listanotas)
    media = soma / 3
    return media

def verificar_situacao(media):
    if media >= 7:
        return("aprovado")
    if media < 5 <= 6.9 :
        return("recuperação")
    if media < 5:
        return("Reprovado")
    return verificar_situacao
