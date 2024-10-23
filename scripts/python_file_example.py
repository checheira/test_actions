import os
from datetime import date

# Obtener la fecha de hoy
hoy = date.today()

# Imprimir la fecha de hoy
print("La fecha de hoy es:", hoy)

var1 = os.environ["nosec_value"]
var2 = os.environ["sec_value"]

print(f({var1}))
print({var2})