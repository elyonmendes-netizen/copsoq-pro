import matplotlib.pyplot as plt

def gerar_grafico(resultados):
    dims = list(resultados.keys())
    medias = [v["media"] for v in resultados.values()]

    plt.figure()
    plt.bar(dims, medias)
    plt.xticks(rotation=45)

    plt.savefig("grafico.png")
    plt.close()
