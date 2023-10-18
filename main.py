import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def main():
    n = int(input("Введите количество чисел Фибоначчи (N): "))
    fib_sequence = fibonacci(n)
    x = np.arange(1, n + 1)  # Номера чисел Фибоначчи
    y = np.array(fib_sequence)  # Значения чисел Фибоначчи

    plt.plot(x, y, marker='o')
    plt.title('Числа Фибоначчи')
    plt.xlabel('Номер числа')
    plt.ylabel('Значение числа')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()