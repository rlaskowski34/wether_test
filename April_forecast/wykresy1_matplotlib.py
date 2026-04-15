# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5]
# y = [10,15,13,17,20]
#
# # Wykres liniowy
#
# plt.plot(
#     x,
#     y,
#     color="red",
#     linewidth=3,
#     marker="o",
#     markersize=10,
#     linestyle="-.",
# )
# plt.title("Wykres liniowy")
# plt.xlabel("Numer dnia")
# plt.ylabel("Wartość sprzedaży")
# plt.grid(True)
# plt.show()
from itertools import product

import plt

# from matplotlib import pyplot as plt
#
# product = ["A", "B", "C", "D"]
# results = [12,19,7,15]
#
# plt.bar(product, results)
#
# plt.xlabel("Product")
# plt.ylabel("Results")
#
# plt.show()

import matplotlib.pyplot as plt

# oceny = [2,2,5,5,4,3,2,5,4,3]
#
# plt.hist(oceny, bins=4)
# plt.title("Histogram ocen")
# plt.xlabel("Ocena")
# plt.ylabel("Liczba wystąpień")
#
# plt.ylim([0,100])
#
# plt.show()


# label = ["Python", "Java", "C++", "JS"]
# value = [40,25,15,20]
#
# plt.pie(x=value, labels=label, autopct="%1.2f%%")
#
# plt.show()


# product = ["Laptop", "Tablet", "Telefon", "Monitor"]
# results = [25, 18, 40, 12]
#
#
# plt.bar(product, results)
#
# plt.xlabel("Product")
# plt.ylabel("Results")
#
# plt.show()

result = [45, 50, 52, 48, 60, 70, 65, 55, 58, 62, 75, 80, 78, 85, 90]

plt.hist(result, bins=4)
plt.title("Prezentacja ocen")
plt.xlabel("Ocena")
plt.ylabel("Ilość ocen")

plt.ylim([0,100])

plt.show()


