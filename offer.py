from PIL import Image
import pytesseract
import sympy as sp


# обернуть в класс
image_path = 'offer_files/Screenshot_20231003_214123.png'
image = Image.open(image_path)

equation_text = pytesseract.image_to_char(image)

x = sp.symbols('x')
equation = sp.sympify(equation_text)  # Преобразование текста в символьное уравнение

solutions = sp.solve(equation, x)  # Решение уравнения

print("Решения уравнения:")
for solution in solutions:
    print(solution)
