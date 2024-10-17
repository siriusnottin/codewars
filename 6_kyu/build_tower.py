def return_n_symbol(n, symbol='*'):
  symbols = ''
  for i in range(n):
    symbols += symbol
  return symbols

def tower_builder(n_floors):
  j = n_floors-1
  floors = []
  for i in range(1, n_floors+1):
    floor = ''
    floor += return_n_symbol(j, ' ')
    if i == 1:
      floor += return_n_symbol(i)
    elif i > 1:
      floor += return_n_symbol(i+i-1)
    floor += return_n_symbol(j, ' ')
    floors.append(floor)
    j-=1
  return floors
