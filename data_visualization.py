import matplotlib.pyplot as plt # Matplotlib import
import pandas as pd # Panda import

# Zahlen von 0 bis 9
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Berechnung der Zahlen
quadratzahlen = [i**2 for i in x]  # Quadratzahlen
kubikzahlen = [i**3 for i in x]     # Kubikzahlen

# DataFrame mit Pandas
daten = pd.DataFrame({
    'Zahl': x,
    'Quadratzahl': quadratzahlen,
    'Kubikzahl': kubikzahlen
})

# Speichern des DataFrames in einer CSV-Datei
daten.to_csv('zahlen.csv', index=False)

# Diagramm für Quadratzahlen
plt.plot(x, quadratzahlen, label='Quadratzahlen', color='blue', marker='o')

# Diagramm für Kubikzahlen
plt.plot(x, kubikzahlen, label='Kubikzahlen', color='red', marker='x')

# Diagramm einrichten hinzufügen
plt.title('Quadratzahlen und Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Wert')

# Legende anzeigen
plt.legend()

# Bild gespeichert als PNG mit einer dpi 300 Auflösung
plt.savefig('quadratzahlen_kubikzahlen.png', format='png', dpi=300)

# Diagramm anzeigen
plt.show()