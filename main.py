from functions import *

#Limites del intervalo de búsqueda
lower_limit = -100.0
upper_limit = 100.0
filename = get_filename()

#En caso de que no se pueda abrir el archivo, se muestra un mensaje de error y el programa termina
try:
    file = open(filename, "r+")
except IOError:
    print("Error: no existe el archivo ingresado.")
    exit(1)

#Lee los coeficientes del polinomio del archivo, hay que recordar borrar los puntos del mismo
#luego de cada uso sin dejar lineas vacias
poly_coeffs = read_pol(file)
print("Coeficientes del polinomio: ", end="")
print(poly_coeffs)
points_count = get_inf_points(poly_coeffs, lower_limit, upper_limit, file)


s = {"uno": "", "muchos": "s"}
if points_count > 0:
    if points_count > 1:
        opt = "muchos"
    else:
        opt = "uno"

    print("%s punto%s encontrado%s en el intervalo [%f,%f]" % (str(points_count), s[opt], s[opt],
                                                                       lower_limit, upper_limit))
    print("Los máximos/mínimos fueron agregados al archivo %s" % filename)
else:
    print("No se encontraron máximos o mínimos...")

file.close()




