# =====================================================================
# EJERCICIO 1 - VARIABLES: Ticket de soporte
# =====================================================================
# Contexto: Cada ticket de soporte tiene un ID, categoría, prioridad y
# un tiempo estimado de resolución en minutos.
#
# TAREA:
# 1. Crea las variables: id_ticket, categoria, prioridad, minutos_estimados
#    con los valores que quieras (ejemplo: 4521, "Hardware", "Alta", 30)
# 2. Imprime un resumen con este formato exacto (usa f-strings):
#    Ticket #4521 | Categoría: Hardware | Prioridad: Alta | Tiempo estimado: 30 min
#
# RETO EXTRA:
# 3. Dada una variable hora_inicio (por ejemplo 14 para las 2:00 PM) y los
#    minutos_estimados, calcula y muestra a qué hora se resolvería el ticket.
#    Ejemplo de salida: "El ticket se resolvería aproximadamente a las 14:30"
#    (No te preocupes por manejar cambios de día, solo suma minutos a la hora)
 
print("=" * 60)
print("EJERCICIO 1: Ticket de soporte")
print("=" * 60)
 
# TU CÓDIGO AQUÍ
id_ticket = 4521
categoria = "Hardware"
prioridad = "Alta"
minutos_estimados = 30
hora_inicio = 14

print(f"Ticket #{id_ticket} | Categoría: {categoria} | Prioridad: {prioridad} | Tiempo estimado: {minutos_estimados} min")

# RETO EXTRA:
hora_fin = hora_inicio + (minutos_estimados // 60)
minutos_fin = minutos_estimados % 60
print(f"El ticket se resolvería aproximadamente a las {hora_fin}:{minutos_fin:02d}")
