import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість випадкових точок для методу
N = 100000

# Генерація випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Підрахунок кількості точок, що лежать під кривою
under_curve = np.sum(y_random < f(x_random))

# Обчислення площі під кривою Монте-Карло
area = (b - a) * (f(b)) * (under_curve / N)

# Аналітичний інтеграл для порівняння
result, error = spi.quad(f, a, b)

# Виведення результатів
print("Значення інтеграла методом Монте-Карло: ", area)
print("Аналітичне значення інтеграла: ", result)
print("Оцінка абсолютної помилки: ", error)

# Графік функції
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# графік
fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b, 400)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# графік
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# межі інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
