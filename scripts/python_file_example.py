import os
from datetime import date

# Obtener la fecha de hoy
hoy = date.today()

# Imprimir la fecha de hoy
print("La fecha de hoy es:", hoy)
print(f'Name is {os.environ.get("NO_SEC_VARIABLE", "<unknown")}')
print(f'PASS is {os.environ.get("SECRET_VALUE", "<unknown")}')