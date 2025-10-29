# TODO: Fungsi untuk memeriksa apakah sebuah bilangan genap
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

    pass

# Tes fungsi
print(is_even(4))   # True
print(is_even(7))   # False

# TODO: Fungsi untuk menghitung faktorial
def factorial(n):
    a = 1
    hasil = 1
    while a <= n:
        hasil *= a
        a += 1
    return hasil
    pass

# Tes fungsi
print(factorial(5))  # 120
print(factorial(0))  # 1
