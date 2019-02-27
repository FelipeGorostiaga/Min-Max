#Evalua el polinomio en el punto x, es decir calcula p(x)
def evaluate_poly(poly, x):
    y = 0
    for i in range(0, len(poly)):
        y += poly[i] * (x**i)
    return y

#Recibe una lista con los coeficientes del polinomio y retorna una nueva lista con los coeficientes
#del polinomio derivado
def derivate_pol(poly):
    deriv_pol = []
    for i in range(1, len(poly)):
        deriv_pol.append(poly[i] * i)

    return deriv_pol

#Pide por linea de comando el nombre del archivo y lo retorna
def get_filename():
    filename = str(input("Ingresa el nombre del archivo:\n"))
    return filename


#Lee los coeficientes del polinomio del archivo y los retorna en una lista de floats
def read_pol(file):
    poly_coeffs = []
    for line in file.readlines():
        strip_line = line.strip("\n")
        poly_coeffs.append(float(strip_line))
    return poly_coeffs

#Recorre el intervalo de a saltos h hasta encontrar un caso tal que f(xn)*f(xn + h) < 0. Si se encuentra se llama
#a find_point() que retorna el maximo/minimo encontrado y luego se llama a write_inf_point() que agrega el punto
#al archivo.
def get_inf_points(poly_coeffs, lower_limit, upper_limit, file):

    h = 0.01
    count = 0
    i = lower_limit
    der_poly = derivate_pol(poly_coeffs)

    y1 = evaluate_poly(der_poly, i)

    while i <= (upper_limit - h):
        y2 = evaluate_poly(der_poly, i + h)
        if (y1 * y2) < 0:
            count += 1
            inf_point = find_point(der_poly, i, i + h)
            write_inf_point(inf_point, poly_coeffs, file)
        y1 = y2
        i += h
    return count

#Recibe por parametros los coeficientes del polinomio derivado y los dos x encontrados en get_inf_points tales que
#f(x0)*f(x1) < 0, por lo cual hay un máximo/mínimo en [x0,x1]. Se divide el intervalo a la mitad sucesivamente
#hasta encontrar el punto que se aproxime a cero, es decir que en valor absulto sea menor que 10**-6
def find_point(der_poly, x0, x1):
    error = 0.0000006
    xr = (x0 + x1) / 2
    xr_der = evaluate_poly(der_poly, xr)
    x0_der = evaluate_poly(der_poly, x0)
    x1_der = evaluate_poly(der_poly, x1)

    while abs(xr_der) > error:
        if xr_der * x0_der < 0:
            x1_der = xr_der
            x1 = xr
            xr = (x0 + xr) / 2
        elif xr_der * x1_der < 0:
            x0_der = xr_der
            x0 = xr
            xr = (x1 + xr) / 2

        xr_der = evaluate_poly(der_poly, xr)

    return xr

#Evalua el polinomio en el punto y escribe el par ordenado (x,y) correspondiente en el archivo
def write_inf_point(point, poly_coeffs, file):
    par = "(" + str(point) + ", " + str(evaluate_poly(poly_coeffs, point)) + ")\n"
    file.write(par)







