#associative
a, b, c = 10, 5, 2

# Logical operators
a1, b1, c1 = True, False, True

print("AND:", (a1 and b1) and c1 == a1 and (b1 and c1))
print("OR :", (a1 or b1) or c1 == a1 or (b1 or c1))

# Arithmetic operators
print("+  :", (a + b) + c == a + (b + c))
print("-  :", (a - b) - c == a - (b - c))



#distributive
# Logical values
a, b, c = True, False, True

print("AND over OR:",
      a and (b or c) == (a and b) or (a and c))

print("OR over AND:",
      a or (b and c) == (a or b) and (a or c))


# Arithmetic values
a, b, c = 10, 5, 2

print("+ over -:",
      a + (b - c) == (a + b) - (a + c))

print("- over +:",
      a - (b + c) == (a - b) + (a - c))