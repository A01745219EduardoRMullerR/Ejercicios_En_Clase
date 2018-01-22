#autor :Eduardo Müller
#encoding: UTF-8
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

x1 = (-b + ((b*b - 4*a*c))**.5) / (2 * a)
x2 = (-b - ((b*b - 4*a*c))**.5) / (2 * a)

print("solución 1 = %.2f" % x1, "\n", "solución 2 =%.2f"% x2)