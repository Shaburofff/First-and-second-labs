import re

def number_to_words(number):
    DIGITS = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return ' '.join(DIGITS[digit] for digit in number)

def process_stream(filename):
    with open(filename, 'r') as file:
        data = file.read().split()
    
    pattern = re.compile(r'^97\d[13579]$')  # 97xx, где xx - нечетное число
    valid_numbers = [num for num in data if pattern.match(num)]
    
    count = len(valid_numbers)
    min_odd_number = min(valid_numbers, key=int) if valid_numbers else None
    
    print(f"Количество чисел: {count}")
    if min_odd_number:
        print("Минимальное число прописью:", number_to_words(min_odd_number))

process_stream("1lab.txt")
