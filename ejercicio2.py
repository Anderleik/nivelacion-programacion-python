# =====================================================================
# EJERCICIO 2 - CONDICIONALES: Clasificador de prioridad
# =====================================================================
# Contexto: El sistema de soporte asigna prioridad según el número de
# usuarios afectados por una falla.
#
# TAREA:
# Dado un número de usuarios afectados (variable usuarios_afectados),
# clasifica la prioridad según estas reglas:
#   1 usuario                -> "Baja"
#   2 a 10 usuarios          -> "Media"
#   11 a 50 usuarios         -> "Alta"
#   Más de 50 usuarios       -> "Crítica" (además imprime "Escalar a nivel 2")
#
# Imprime la prioridad resultante.
#
# RETO EXTRA:
# Agrega una variable sistema_afectado (string, ej: "VPN", "correo", "impresora").
# Si el sistema afectado es "VPN" o "correo" y la prioridad calculada sería
# "Baja" o "Media", súbela automáticamente un nivel
# (Baja -> Media, Media -> Alta), sin importar el número de usuarios.
 
print("\n" + "=" * 60)
print("EJERCICIO 2: Clasificador de prioridad")
print("=" * 60)
 
usuarios_afectados = 55         # cambia este valor para probar distintos casos
sistema_afectado = "VPN"         # cambia este valor para probar el reto extra
 
# TU CÓDIGO AQUÍ
if usuarios_afectados == 1:
    prioridad = "Baja"
elif usuarios_afectados >= 2 and usuarios_afectados <= 10:
    prioridad = "Media"
elif usuarios_afectados >= 11 and usuarios_afectados <= 50:
    prioridad = "Alta"
elif usuarios_afectados > 50:
    prioridad = "Crítica"
else:
    prioridad = "Número de usuarios no válido"

if sistema_afectado == "VPN" or sistema_afectado == "correo":
    if prioridad == "Baja":
        prioridad = "Media"
    elif prioridad == "Media":
        prioridad = "Alta"

print(f"Prioridad {prioridad}")

if prioridad == "Crítica":
    print("Prioridad critica: Escalar a nivel 2")