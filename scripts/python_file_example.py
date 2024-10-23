import os
from datetime import date

# Obtener la fecha de hoy
hoy = date.today()

# Imprimir la fecha de hoy
print("La fecha de hoy es:", hoy)
print(os.getenv('nosec_value', "unknown"))
print(os.getenv('sec_value', "unknown"))