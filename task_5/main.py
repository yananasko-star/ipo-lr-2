number=(input()) # ввод значения с клавиатуры
number_str = str(number) # Преобразование числа в строку
sum_of_digits = 0 # Инициализация переменной для хранения суммы
#Итерация по символам строки и суммирование цифр
for digit_char in number_str: 
    digit = int(digit_char) #Преобразование символа в число  
    sum_of_digits += digit  #Добавление цифры к сумме

    print(f"Сумма цифр числа {number} равна {sum_of_digits}") # вывод получившегося значения

