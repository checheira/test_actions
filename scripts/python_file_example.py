import os
from datetime import date

# Obtener la fecha de hoy
hoy = date.today()

# Imprimir la fecha de hoy
print("La fecha de hoy es:", hoy)
print(f'Name is {os.getenv("ENV_VARIABLE1")}')
print(f'PASS is {os.getenv("SECRET_VALUE")}')
print(os.getenv('ENV_VARIABLE1', "unknown"))
print(os.getenv('SECRET_VALUE', "unknown"))