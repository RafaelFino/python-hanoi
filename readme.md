# Torre de Hanoi em Python

Este projeto contém duas implementações em Python do clássico problema da **Torre de Hanoi**, utilizando estruturas de dados do tipo **pilha (stack)**. O objetivo é resolver o quebra-cabeça movendo discos entre três torres, seguindo regras específicas, e demonstrar conceitos fundamentais de programação como listas, pilhas, recursão e orientação a objetos. Este README é projetado para ser didático, explicando passo a passo o problema, o algoritmo e as implementações, para que alunos de programação possam aprender de forma gradual.

## O Problema da Torre de Hanoi

A Torre de Hanoi é um quebra-cabeça matemático inventado pelo matemático francês Édouard Lucas em 1883. Ele consiste em três torres (ou hastes) verticais e um conjunto de discos de tamanhos diferentes, com um buraco no centro para que possam ser empilhados nas torres. Os discos são inicialmente empilhados em uma das torres, com o maior disco na base e os menores no topo, formando uma pirâmide.

### Regras do Jogo:
1. **Movimento único**: Apenas um disco pode ser movido por vez.
2. **Regra de empilhamento**: Um disco só pode ser colocado em cima de outro disco maior, ou em uma torre vazia. Nunca um disco maior pode ser colocado sobre um menor.
3. **Objetivo**: Mover todos os discos da torre inicial (origem) para a torre de destino, usando a terceira torre como auxiliar temporário.

Se você violar qualquer regra, o jogo "quebra" – por exemplo, tentar colocar um disco grande sobre um pequeno resulta em erro.

### Exemplo com 3 Discos:
- Disco 1: menor
- Disco 2: médio
- Disco 3: maior

Estado inicial: Torre Origem tem [3, 2, 1] (3 na base, 1 no topo). Torres Auxiliar e Destino estão vazias.

Estado final: Torre Destino tem [3, 2, 1]. Torres Origem e Auxiliar estão vazias.

O número mínimo de movimentos necessários é `2^n - 1`, onde `n` é o número de discos. Para 3 discos: 7 movimentos.

## O Algoritmo Lógico para Resolver a Torre de Hanoi

A solução clássica usa **recursão**, um conceito onde uma função chama a si mesma para resolver subproblemas menores. O algoritmo divide o problema em etapas:

### Passos Gerais:
1. **Caso base**: Se há apenas 1 disco, mova-o diretamente da origem para o destino.
2. **Caso recursivo** (para n discos):
   - Mova os `n-1` discos superiores da origem para a auxiliar (usando o destino como auxiliar temporário).
   - Mova o disco restante (o maior) da origem para o destino.
   - Mova os `n-1` discos da auxiliar para o destino (usando a origem como auxiliar temporário).

Isso garante que as regras sejam seguidas, pois os discos menores são movidos primeiro, liberando espaço para o maior.

### Exemplo Lógico para 3 Discos:
- Mova disco 1 (menor) de Origem para Destino.
- Mova disco 2 de Origem para Auxiliar.
- Mova disco 1 de Destino para Auxiliar (agora Auxiliar tem [2, 1]).
- Mova disco 3 de Origem para Destino.
- Mova disco 1 de Auxiliar para Origem.
- Mova disco 2 de Auxiliar para Destino.
- Mova disco 1 de Origem para Destino.

Resultado: Destino tem [3, 2, 1].

Este algoritmo é eficiente e sempre encontra a solução ótima.

## Implementação 1: Simples (simples.py)

Esta implementação é a mais básica possível, resolvendo manualmente o problema para exatamente 3 discos. Ela usa listas Python como pilhas simples (sem classes ou funções), focando em operações básicas de `pop` (remover do topo) e `append` (adicionar ao topo). Não há recursão ou validação; os movimentos são hardcoded (codificados manualmente) com base no algoritmo lógico acima.

### Código Completo de simples.py:
```python
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
```

### Explicação Passo a Passo:
1. **Inicialização**:
   - `origem = [3, 2, 1]`: Lista representando a torre origem, com 3 (base), 2 (meio), 1 (topo).
   - `destino = []` e `auxiliar = []`: Torres vazias.
   - Imprime o estado inicial.

2. **Primeiro Movimento**:
   - `disco = origem.pop()`: Remove 1 (topo da origem). Origem agora [3, 2].
   - `destino.append(disco)`: Adiciona 1 ao destino. Destino agora [1].
   - Imprime estado.

3. **Segundo Movimento**:
   - Remove 2 da origem, adiciona à auxiliar. Auxiliar [2].
   - Imprime estado.

4. **Terceiro Movimento**:
   - Remove 1 do destino, adiciona à auxiliar. Auxiliar [2, 1].
   - Imprime estado.

5. **Quarto Movimento**:
   - Remove 3 da origem, adiciona ao destino. Destino [3].
   - Imprime estado.

6. **Quinto Movimento**:
   - Remove 1 da auxiliar, adiciona à origem. Origem [1].
   - Imprime estado.

7. **Sexto Movimento**:
   - Remove 2 da auxiliar, adiciona ao destino. Destino [3, 2].
   - Imprime estado.

8. **Sétimo Movimento**:
   - Remove 1 da origem, adiciona ao destino. Destino [3, 2, 1].
   - Imprime estado final.

Esta implementação ilustra o uso básico de listas como pilhas (LIFO: Last In, First Out) e o fluxo manual do algoritmo. É limitada a 3 discos, mas ensina o conceito fundamental.

## Implementação 2: Complexa (complexo.py)

Esta implementação é completa e escalável, resolvendo para qualquer número de discos. Usa classes para organizar o código, recursão para o algoritmo, validação de regras e impressão de estados. Introduz conceitos de orientação a objetos.

### Código Completo de complexo.py:
```python
# Implementação de pilha para o jogo da Torre de Hanoi
class Tower:
    def __init__(self, name: str):
        self.items = []
        self._name = name

    def name(self) -> str:
        return self._name

    def push(self, item):
        if not self.is_empty() and item > self.peek():
            raise ValueError("Não podemos empilhar um disco maior sobre um menor.")
        
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0
    
# Implementação do jogo da Torre de Hanoi
class Hanoi:
    def __init__(self):
        self.Source = Tower("Origem  ")
        self.Aux =    Tower("Auxiliar")
        self.Target = Tower("Destino ")
        self.Steps = 0

    # Inicia o jogo com o número de discos especificado
    def start(self, disks: int= 3):
        for i in range(disks, 0, -1):
            self.Source.push(i)

        print("Estado inicial:")
        self.print_state()            

        self.execute(disks, self.Source, self.Target, self.Aux)

        print(f"\nNúmero final de passos para completar: {self.Steps}")        

    # Método recursivo para resolver o problema da Torre de Hanoi
    def execute(self, n: int, source: Tower, target: Tower, auxiliary: Tower):
        if n == 1:
            self.move_disk(source, target)
        else:
            self.execute(n-1, source, auxiliary, target)
            self.move_disk(source, target)
            self.execute(n-1, auxiliary, target, source)

    # Método para mover um disco de uma torre para outra
    def move_disk(self, source: Tower, target: Tower):
        disk = source.pop()
        target.push(disk)
        print(f"\nMovendo o disco {disk} de {source.name()} para {target.name()}")
        self.print_state()
        self.Steps += 1            

    # Método para imprimir o estado atual das torres
    def print_state(self):
        print(f" {self.Source.name()}: {self.Source.items}")
        print(f" {self.Aux.name()}: {self.Aux.items}")
        print(f" {self.Target.name()}: {self.Target.items}")


# Execução do jogo
n = int(input("Digite o número de discos: "))

if n <= 0:
    print("O número de discos deve ser maior que 2.")
    n = 3

hanoi = Hanoi()
hanoi.start(n)
```

### Explicação Detalhada por Parte:

#### 1. Classe Tower (Pilha Personalizada)
- **Propósito**: Representa uma torre como uma pilha com validação.
- **`__init__(self, name: str)`**: Inicializa a torre com uma lista vazia `self.items` e um nome `self._name`.
- **`name(self) -> str`**: Retorna o nome da torre (ex: "Origem  ").
- **`push(self, item)`**: Adiciona um item ao topo.
  - Verifica se a torre não está vazia e se o item é maior que o topo (`self.peek()`). Se sim, lança `ValueError` para impedir violação da regra.
  - Usa `self.items.append(item)` para adicionar.
- **`pop(self)`**: Remove e retorna o item do topo (`self.items.pop()`), ou `None` se vazia.
- **`peek(self)`**: Retorna o item do topo sem removê-lo, ou `None` se vazia.
- **`is_empty(self)`**: Retorna `True` se a lista estiver vazia.

Esta classe ensina encapsulamento e validação em pilhas.

#### 2. Classe Hanoi (Gerenciador do Jogo)
- **Propósito**: Controla o jogo, as torres e a lógica recursiva.
- **`__init__(self)`**: Cria três instâncias de `Tower` (Source, Aux, Target) e inicializa `self.Steps = 0` para contar movimentos.
- **`start(self, disks: int = 3)`**:
  - Loop `for i in range(disks, 0, -1)`: Adiciona discos de `disks` a 1 na Source (maior primeiro).
  - Imprime estado inicial via `self.print_state()`.
  - Chama `self.execute(disks, self.Source, self.Target, self.Aux)` para resolver.
  - Imprime o total de passos.
- **`execute(self, n: int, source: Tower, target: Tower, auxiliary: Tower)`**:
  - Implementa o algoritmo recursivo.
  - Se `n == 1`: Chama `self.move_disk(source, target)`.
  - Senão: Recursão para mover `n-1` para auxiliar, move o maior, recursão para mover `n-1` para destino.
- **`move_disk(self, source: Tower, target: Tower)`**:
  - Remove disco de `source`, adiciona a `target` (com validação).
  - Imprime o movimento e chama `self.print_state()`.
  - Incrementa `self.Steps`.
- **`print_state(self)`**: Imprime as listas de cada torre.

#### 3. Execução Principal
- Pede input para `n` (número de discos).
- Valida se `n > 0`, senão define 3.
- Cria `hanoi = Hanoi()` e chama `hanoi.start(n)`.

Esta implementação combina todos os conceitos: pilhas, recursão, classes, validação e saída interativa.

## Como Executar

1. Certifique-se de ter Python 3 instalado.
2. Clone ou baixe este repositório.
3. Navegue para a pasta: `cd python-hanoi`

### Para simples.py:
- Execute: `python3 simples.py`
- Mostra passos manuais para 3 discos.

### Para complexo.py:
- Execute: `python3 complexo.py`
- Digite o número de discos (ex: 3).

## Exercícios Sugeridos para Alunos

1. Modifique `simples.py` para 4 discos, adicionando movimentos manuais.
2. Em `complexo.py`, adicione uma pausa (`time.sleep`) entre movimentos para simular animação.
3. Implemente uma versão sem recursão (iterativa) em `complexo.py`.
4. Adicione cores à saída usando `colorama` (ex: discos coloridos).
5. Crie uma função para verificar se o jogo foi resolvido corretamente.

## Conclusão

Este projeto guia do problema básico à implementação avançada, ensinando algoritmos, estruturas de dados e boas práticas de código. Execute os arquivos, observe as saídas e experimente modificações para consolidar o aprendizado!