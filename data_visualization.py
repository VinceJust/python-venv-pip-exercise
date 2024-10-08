import matplotlib.pyplot as plt

# Beispiel-Daten: Zahlen von 0 bis 9
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Berechnung der Quadratzahlen und Kubikzahlen
quadratzahlen = [i**2 for i in x]
kubikzahlen = [i**3 for i in x]

# Liniendiagramm für Quadratzahlen erstellen
plt.plot(x, quadratzahlen, label='Quadratzahlen', color='blue', marker='o')

# Liniendiagramm für Kubikzahlen erstellen
plt.plot(x, kubikzahlen, label='Kubikzahlen', color='red', marker='x')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Quadratzahlen und Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Wert')

# Legende anzeigen
plt.legend()

# Diagramm speichern
plt.savefig('quadratzahlen_kubikzahlen.png')

# Optional: Diagramm anzeigen
# plt.show()
