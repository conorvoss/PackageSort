def sort(width, height, length, mass):
  if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
    return "Error: Inputs must be greater than 0"
    
  bulky = width * height * length >= 1000000 or width >= 150 or height >= 150 or length >= 150
  heavy = mass >= 20
  
  if bulky and heavy:
    return "REJECTED"
  elif bulky or heavy:
    return "SPECIAL"
  else:
    return "STANDARD"

try:
  width = float(input("Enter Width: "))
  height = float(input("Enter Height: "))
  length = float(input("Enter Length: "))
  mass = float(input("Enter Mass: "))
except ValueError:
  print("Error: Inputs must be properly formatted as floats")
except:
  print("Error")
else:
  print(sort(width, height, length, mass))
