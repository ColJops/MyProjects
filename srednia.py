import matplotlib.pyplot as plt

def srednia_ocen(oceny):
    if type(oceny) is not list:
        return f"Błędne dane wejsćiowe: {type(oceny)}"
    
    suma = sum(oceny)
    if oceny.count(5) > 4 or oceny.count(6) > 4:
        suma =+ 4

    srednia = suma / len(oceny)

    # Wykres kołowy
    legenda = ("1", "2", "3", "4", "5", "6")
    #lista ze zliczonymi liczbami ocen
    oceny_zliczone = [oceny.count(x) for x in range(1, 7)]

    plt.title('Oceny wg %', fontsize=16)
    plt.pie(oceny_zliczone, labels=legenda)
    plt.show()

    return round(srednia, 2)

print(srednia_ocen("Błędne dane!"))
print(
    srednia_ocen(
        [2, 3, 3, 4, 5, 1, 2, 2, 2, 3, 3, 6, 5, 5, 4, 4, 4, 4, 1, 1, 3, 4, 2, 1]
    )
)