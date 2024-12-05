# 1)Hardcoded coefficients
a = 1
b = -3
c = 2

# Simulating weather modeling using a quadratic formula
def quadratic_solution(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, None
    else:
        return None, None

print("Hardcoded roots:", quadratic_solution(a, b, c))

# 2)user given input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

roots = quadratic_solution(a, b, c)
print("Roots from user input:", roots)
