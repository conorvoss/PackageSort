def sort(width, height, length, mass):
  if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
    return "Error: inputs must be greater than 0"
    
  bulky = width * height * length >= 1000000 or width >= 150 or height >= 150 or length >= 150
  heavy = mass >= 20
  
  if bulky and heavy:
    return "REJECTED"
  elif bulky or heavy:
    return "SPECIAL"
  else:
    return "STANDARD"

#width = input("Enter Width: ")
#height = input("Enter Height: ")
#length = input("Enter Length: ")
#mass = input("Enter Mass: ")

print(sort(1, 1, 1, 1))
