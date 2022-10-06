a = 10
print(type(a))
a = float(10)
print(type(a))
a = str(10)
print(type(a))

from random import randrange
rastgele_sayi = randrange(1, 100)
print(rastgele_sayi)

print("a' nın uzunluğu :", len(a))

if a == "balikesir":
    print("a balikesir eşit")

if "kes" in a:
    print("a'da kes var")