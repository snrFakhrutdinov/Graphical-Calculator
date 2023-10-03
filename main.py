import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')


# реализовать метод md для получения данных от пользователя
# обернуть в функции
equation = 2 * sp.asin(2 * x - 1) - (x - 1) / (sp.sqrt(x**2 + 3 * x) - 4)


x_values = np.linspace(-10, 10, 800)  # Задание диапазона x
y_values = []

for val in x_values:
    y_val = equation.evalf(subs={x: val})

    if not sp.im(y_val):
        y_values.append(y_val)

y_values = np.array(y_values)


# обернуть в функцию
plt.figure(figsize=(6, 6))
plt.plot(x_values[:len(y_values)], y_values, label=str(equation), color='b')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title(f'График функции: {equation}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
