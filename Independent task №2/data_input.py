def input_worker():
    worker = {}
    while True:
        name = input("Введіть ім'я співробітника або 'stop' щоб закінчити: ")
        if name.lower() == 'stop':
            break
        salary =float (input("Введіть заробітню плату цього співробітника : "))
        days_worked =  int(input("Введіть кількість відпрацьованих днів : "))
        worker[name] = {'Зарплата': salary, 'Дні': days_worked}

    return worker