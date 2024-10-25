from pulp import LpProblem, LpMaximize,LpVariable,lpSum,LpStatus,value

# Створення проблеми 
problem = LpProblem("Maximize_Production", LpMaximize)

# Змінні прийняття рішень
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')  # К-сть лимонаду
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')  # К-сть соку

# Цільова функція:
problem += lpSum([lemonade, fruit_juice]), "Total_Products"

# Обмеження на ресурси
problem += (2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint")  # Обмеження на воду
problem += (1 * lemonade <= 50, "Sugar_Constraint")  # Обмеження на цукор
problem += (1 * lemonade <= 30, "Lemon_Juice_Constraint")  # Обмеження на лимонний сік
problem += (2 * fruit_juice <= 40, "Fruit_Puree_Constraint")  # Обмеження на фруктове пюре


problem.solve()

print("Status:", LpStatus[problem.status])
print("Кількість виробленого лимонаду:", value(lemonade))
print("Кількість виробленого фруктового соку:", value(fruit_juice))
print("Максимальна кількість вироблених продуктів:", value(problem.objective))
