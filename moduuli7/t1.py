numero = int(input("kerro kuukauden numero"))
vuodenaika = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
aika = vuodenaika[numero-1]
print (f"{numero}. kuukausi on {aika}.")