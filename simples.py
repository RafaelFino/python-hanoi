# hanoi simples

origem = [3, 2, 1]
destino = []
auxiliar = []

print(f"Estado inicial: \n Origem:   {origem}\n Auxiliar: {auxiliar}\n Destino:  {destino}")
disco = origem.pop() # remove o disco 1 da origem
destino.append(disco) # move o disco 1 para o destino

print(f"Estado após mover o disco 1: \n Origem:   {origem}\n Auxiliar: {auxiliar}\n Destino:  {destino}")
disco = origem.pop() # remove o disco 2 da origem
auxiliar.append(disco) # move o disco 2 para o auxiliar

print(f"Estado após mover o disco 2: \n Origem:   {origem}\n Auxiliar: {auxiliar}\n Destino:  {destino}")
disco = destino.pop() # remove o disco 1 do destino
auxiliar.append(disco) # move o disco 1 para o auxiliar

print(f"Estado após mover o disco 1 para o auxiliar: \n Origem:   {origem}\n Auxiliar: {auxiliar}\n Destino:  {destino}")
disco = origem.pop() # remove o disco 3 da origem
destino.append(disco) # move o disco 3 para o destino

print(f"Estado após mover o disco 3: \n Origem:   {origem}\n Auxiliar: {auxiliar}\n Destino:  {destino}")
disco = auxiliar.pop() # remove o disco 1 do auxiliar
origem.append(disco) # move o disco 1 para a origem     

print(f"Estado após mover o disco 1 para a origem: \n Origem:   {origem}\n Auxiliar: {auxiliar}\n Destino:  {destino}")
disco = auxiliar.pop() # remove o disco 2 do auxiliar
destino.append(disco) # move o disco 2 para o destino

print(f"Estado após mover o disco 2 para o destino: \n Origem:   {origem}\n Auxiliar: {auxiliar}\n Destino:  {destino}")
disco = origem.pop() # remove o disco 1 da origem
destino.append(disco) # move o disco 1 para o destino

print(f"Estado final: \n Origem:   {origem}\n Auxiliar: {auxiliar}\n Destino:  {destino}")
