# goit-algo-hw-10
# Завдання 2: Обчислення інтеграла методом Монте-Карло

## Опис

Цей проект реалізує алгоритм для обчислення визначеного інтеграла функції \( f(x) = x^2 \) на інтервалі [0, 2] за допомогою методу Монте-Карло. Результати порівнюються з аналітичним значенням, обчисленим за допомогою бібліотеки SciPy.

## Результати

- Значення інтеграла методом Монте-Карло: 2.666
- Аналітичне значення інтеграла: 2.6666666666666665
- Оцінка абсолютної помилки: 2.9605947323337506e-14

## Висновки

Метод Монте-Карло показав високу точність у порівнянні з аналітичним розрахунком. Площа, обчислена методом Монте-Карло, дуже близька до точного значення інтеграла. Метод Монте-Карло є ефективним інструментом для обчислення площі під графіком особливо якщо згенерована велика к-сть випадкових точок для методу (в нащому випадку 100 000).