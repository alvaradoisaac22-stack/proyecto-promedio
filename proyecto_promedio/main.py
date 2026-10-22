# Curso: Fundamentos de Tecnologia Digitales
# Estudiante: Isaac Alvarado Chaves
# Profesor: Adonis Aleman G.

#Este programa calcula el promedio de tres notas.
print("Calculadora de promedio")

try:
    # Pedimos las notas y las convertimos en numeros.
    nota1 = float(input("Ingrese la primera nota (0 a 100): "))
    nota2 = float(input("Ingrese la segunda nota (0 a 100): "))
    nota3 = float(input("Ingrese la tercera nota (0 a 100): "))

    #Revisamos que las notas esten entre 0 y 100.
    if 0 <= nota1 <= 100 and 0 <= nota2 <= 100 and 0 <= nota3 <= 100:
        promedio = (nota1 + nota2 + nota3) / 3
        print("El promedio es:", round(promedio, 2))
    else:
        print("Las notas deben estar entre 0 y 100.")
except ValueError:
    # Mostramos un mensaje si no se ingresa un numero.
    pint("Debe ingresar las notas con numeros. Use punto para los deicmales.")


