number=(input())
number_str = str(number)
sum_of_digits = 0
for digit_char in number_str:
    digit = int(digit_char)  
    sum_of_digits += digit 
    print(f"Сумма цифр числа {number} равна {sum_of_digits}")