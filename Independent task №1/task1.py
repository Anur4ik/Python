
name = str(input("Ваше прізвище, ім'я, по батькові? "))
age = int(input("Скільки Вам років? "))
home = str(input("Де Ви живете? " ))
studying= str(input("Де Ви навчаєтесь?" ))
group_number = str(input("Номер Вашої групи? "))
number_of_group = int(input("Який Ваш порядковий номер у списку групи? "))
what_is_up = str(input("Як справи? " ))
feeling = str(input("Як Ви себе почуваєте? "))
where_home = str(input("Коли будете вдома? "))
mark= int(input("Яку оцінку отримав на ЗНО по українській мові? "))
today_sunny = str(input("Сьогодні сонячно? "))
quarantine = str(input("Коли нарешті карантин? "))
friend = str(input("Як звати Вашого друга? "))
degree = str(input("Ви думаєте вступати у магістратуру? "))
notebook= str(input("Якого кольору Ваш зошит? "))
mood = str(input("Який Ваш настрій сьогодні? "))
print(f"""
- Ваше ім'я : {name}
- Ваше вік : {age} 
- Ви живете в : {home}
- Ви навчаєтесь в : {studying} 
- Номер вашої групи : {group_number}
- Мій порядковий номер у списку групи : {number_of_group} 
- Ваші справи : {what_is_up}
- Ви себе почуваєте : {feeling} 
- Ви будете дома  : {where_home}
- Ваша оцінка ЗНО по укр мові : {mark} 
- Сьогодні сонячно? : {today_sunny} 
- Карантин буде :  {quarantine}
- Вашого друга звати : {friend} 
- Ви поступете у магістратуру : {degree} 
- Колір вашого зошита : {notebook}
- Ваш настрій : {mood} 
""")
