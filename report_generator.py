import json

def calcular_empresa(df):
    resultados = {}

    for _, row in df.iterrows():
        dados = json.loads(row["Resultado"])

        for dim, info in dados.items():
            if dim not in resultados:
                resultados[dim] = []

            resultados[dim].append(info["media"])

    final = {}

    for dim, valores in resultados.items():
        media = sum(valores) / len(valores)

        if media <= 2.33:
            risco = "Baixo"
        elif media <= 3.66:
            risco = "Médio"
        else:
            risco = "Alto"

        final[dim] = {
            "media": round(media, 2),
            "risco": risco
        }

    return final
