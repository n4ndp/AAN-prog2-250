# Operadores aritméticos: Realizan operaciones matemáticas básicas
# + (suma), - (resta), * (multiplicación), / (división), % (módulo), ** (potencia), // (división entera)
a = 10
b = 3

print("Suma:", a + b)  # Resultado: 13
print("Resta:", a - b)  # Resultado: 7
print("Multiplicación:", a * b)  # Resultado: 30
print("División:", a / b)  # Resultado: 3.333...
print("Módulo:", a % b)  # Resultado: 1
print("Potencia:", a ** b)  # Resultado: 1000
print("División entera:", a // b)  # Resultado: 3

# Operadores de comparación: Devuelven un valor booleano
# == (igual a), != (diferente de), > (mayor que), < (menor que), >= (mayor o igual que), <= (menor o igual que)
c = 5
d = 8

print("¿c es igual a d?", c == d)  # Resultado: False
print("¿c es diferente de d?", c != d)  # Resultado: True
print("¿c es mayor que d?", c > d)  # Resultado: False
print("¿c es menor que d?", c < d)  # Resultado: True
print("¿c es mayor o igual que d?", c >= d)  # Resultado: False
print("¿c es menor o igual que d?", c <= d)  # Resultado: True

# Operadores lógicos: Combinan valores booleanos
# and, or, not
e = True
f = False

print("e AND f:", e and f)  # Resultado: False
print("e OR f:", e or f)  # Resultado: True
print("NOT e:", not e)  # Resultado: False

# Operadores de asignación: Asignan valores a variables
# =, +=, -=, *=, /=, %=, //=, **=
g = 10
g += 5  # Equivalente a g = g + 5
print("Valor de g tras g += 5:", g)  # Resultado: 15

# Operadores bit a bit: Trabajan a nivel de bits
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (desplazamiento a la izquierda), >> (desplazamiento a la derecha)
h = 4  # Binario: 0100
i = 5  # Binario: 0101

print("AND bit a bit:", h & i)  # Resultado: 4 (0100)
print("OR bit a bit:", h | i)  # Resultado: 5 (0101)
print("XOR bit a bit:", h ^ i)  # Resultado: 1 (0001)
print("NOT bit a bit:", ~h)  # Resultado: -5
print("Desplazamiento a la izquierda:", h << 1)  # Resultado: 8 (1000)
print("Desplazamiento a la derecha:", h >> 1)  # Resultado: 2 (0010)
