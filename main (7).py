def ExE(n):
  if n == 1:
      return 3
  elif n == 2:
      return 5
  else:
      return (n - 1) * ExE(n - 1) + (n - 2) * ExE(n - 2)

resultado = ExE(9)
print(resultado)  
