import os
from datetime import date

# Obtener la fecha de hoy
hoy = date.today()

# Imprimir la fecha de hoy
print("La fecha de hoy es:", hoy)

# Imprimir la variable normal
print(os.getenv('nosec_value'))

# Imprimir la variable secreta
print(os.environ.get("sec_value"))
