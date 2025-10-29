# TODO: Program untuk mencetak bilangan ganjil dari 1 hingga 15
odd_numbers = [x for x in range(1, 16) if x % 2 == 1]
print("Bilangan ganjil 1 sampai 15: ", odd_numbers)

# TODO: Program menghitung jumlah huruf vokal
word = input("Masukkan kata: ").lower()

vowels = "aiueo"
count = 0
for letter in word:
    if letter in vowels:
        count += 1

print("Jumlah huruf vokal:", count)
