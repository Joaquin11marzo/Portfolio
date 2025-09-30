def usar_la_fuerza(mochila, m=0, retirados=None):
    if retirados is None:
        retirados = []
    if m == len(mochila):
        return ("No se ha encontrado el sable de luz",
                f"Objetos revisados: {m}",
                f"Objetos retirados: {retirados}")
    if mochila[m].lower() == "sable de luz":
        return ("Se encontró el sable de luz",
                f"Se necesitaron sacar {m} objetos",
                f"Objetos retirados: {retirados}")
    retirados.append(mochila[m])
    return usar_la_fuerza(mochila, m+1, retirados)

mochila1 = ["Agua", "Pan", "Mapa", "Sable de luz", "Celular"]
mochila2 = ["Agua", "Pan", "Mapa", "Celular"]

print("Mochila con sable:")
print(usar_la_fuerza(mochila1))
print("\nMochila sin sable:")
print(usar_la_fuerza(mochila2))
