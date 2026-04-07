def classificar(media):
    if media <= 2.33:
        return "Baixo Risco"
    elif media <= 3.66:
        return "Risco Moderado"
    else:
        return "Alto Risco"


def calcular(respostas):
    resultado = {}

    for dim, valores in respostas.items():
        if len(valores) == 0:
            continue

        media = sum(valores) / len(valores)

        resultado[dim] = {
            "media": round(media, 2),
            "classificacao": classificar(media)
        }

    return resultado
