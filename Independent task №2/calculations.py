def calculate_monthly_salary(worker_info):
    for salary, days_worked in worker_info.items():
        monthly_salary =  (salary['Зарплата']/30)*days_worked['Дні']
        print(f"Cпівробітник отримає за місяць  {worker_info} : {monthly_salary} грн")
