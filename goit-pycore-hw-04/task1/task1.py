def total_salary(path):
    with open(path, 'r') as file:
        text = [el.strip() for el in file.readlines()]
        total = 0
        qty = 0

        for item in text:
            splited = item.split(',')
            number = int(splited[1])
            total = total + number
            qty += 1 

        avg = total / qty
           
        return total, avg

total, avg = total_salary("task1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avg}")
