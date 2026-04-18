# Torre de Hanoi em Python

Este projeto contém implementações em Python do clássico problema da **Torre de Hanoi**, utilizando estruturas de dados do tipo **pilha (stack)**. O objetivo é resolver o quebra-cabeça movendo discos entre três torres, seguindo regras específicas, e demonstrar conceitos fundamentais de programação como recursão, pilhas e validação de regras.

## O Problema da Torre de Hanoi

A Torre de Hanoi é um quebra-cabeça matemático composto por três torres (ou hastes) e um número de discos de tamanhos diferentes. Os discos são empilhados em uma torre inicial, com o maior disco na base e os menores no topo.

### Regras:
- Apenas um disco pode ser movido por vez.
- Um disco só pode ser colocado em cima de outro maior (ou em uma torre vazia).
- O objetivo é mover todos os discos da torre inicial para a torre de destino, usando a terceira torre como auxiliar.

O número mínimo de movimentos para resolver o quebra-cabeça com `n` discos é `2^n - 1`.

## Conceitos Aprendidos

Este projeto ajuda a entender:
- **Recursão**: A solução usa uma função recursiva para dividir o problema em subproblemas menores.
- **Pilhas (Stacks)**: As torres são implementadas como pilhas, onde operações de empilhar (`push`) e desempilhar (`pop`) simulam os movimentos.
- **Validação de Regras**: Verificação para garantir que discos maiores não sejam colocados sobre menores.
- **Representação Visual**: Uso de caracteres no terminal para visualizar o estado das torres a cada movimento.

## Implementações

### Implementação 1: Básica com Recursão e Pilhas

A primeira implementação foca na solução recursiva do problema usando pilhas simples. Ela imprime cada movimento no terminal, mostrando de qual torre para qual o disco foi movido.

#### Estrutura do Código:
- **Classe `Tower`**: Representa uma torre como uma pilha, com métodos `push`, `pop`, `peek`, `is_empty` e `size`.
- **Função `move_disk`**: Move um disco de uma torre para outra, imprimindo o movimento.
- **Função `hanoi`**: Implementa a solução recursiva:
  - Se há apenas 1 disco, move diretamente.
  - Caso contrário, move `n-1` discos para a auxiliar, move o maior disco para o destino, e move os `n-1` discos da auxiliar para o destino.

#### Como Funciona:
1. Inicializa três torres: Source (origem), Aux (auxiliar) e Target (destino).
2. Empilha os discos na torre Source (maior na base).
3. Chama a função recursiva `hanoi` para resolver.
4. Imprime cada movimento.

### Implementação 2: Com Validação e Visualização

A segunda implementação aprimora a primeira adicionando:
- **Validação**: Impede colocar um disco maior sobre um menor, lançando um erro se a regra for violada.
- **Visualização Gráfica**: Após cada movimento, imprime o estado atual das três torres no terminal usando caracteres (`-` para discos, `|` para a haste vazia).

#### Diferenças da Implementação 1:
- A classe `Tower` agora valida no `push`: se a torre não estiver vazia e o novo disco for maior que o topo, lança `ValueError`.
- Função `print_towers`: Imprime as torres lado a lado, com discos representados por traços (`-`) de largura proporcional ao tamanho do disco.
- `move_disk` chama `print_towers` após cada movimento.
- O programa imprime o estado inicial e final das torres.

#### Como Funciona:
1. Mesmo setup inicial.
2. Durante os movimentos, valida cada `push`.
3. Após cada movimento, exibe visualmente as torres.
4. Conta e imprime o número total de movimentos.

## Como Executar

1. Certifique-se de ter Python 3 instalado.
2. Clone ou baixe este repositório.
3. Navegue para a pasta do projeto: `cd python-hanoi`
4. Execute o script: `python3 hanoi.py`
5. Digite o número de discos quando solicitado (ex: 3).

### Exemplo de Saída para 3 Discos:
```
Initial state:
  |    |    |
  |    |    |
 ---   |    |
  S    A    T 

Move disk 1 from Source -> Target
  |    |    |
  |    |   -  
 ---   |    |
  S    A    T 

... (movimentos subsequentes)

Solved in 7 steps.
Final state:
  |    |    |
  |    |    |
  |    |  ---
  S    A    T 
```

## Explicação Detalhada do Código

### Classe Tower
```python
class Tower:
    def __init__(self, name: str):
        self.items = []  # Lista para armazenar os discos
        self._name = name

    def push(self, item):
        if not self.is_empty() and item > self.peek():
            raise ValueError("Cannot place larger disk on top of smaller disk")
        self.items.append(item)

    # Outros métodos...
```
- `items` é uma lista onde o final representa o topo da pilha.
- `push` adiciona ao final, mas valida a regra.

### Função Hanoi
```python
def hanoi(n, source, target, auxiliary, steps=0):
    if n == 1:
        steps = move_disk(source, target, steps, Source, Aux, Target, n)
    else:
        steps = hanoi(n-1, source, auxiliary, target, steps)
        steps = move_disk(source, target, steps, Source, Aux, Target, n)
        steps = hanoi(n-1, auxiliary, target, source, steps)
    return steps
```
- Recursão: Divide o problema até o caso base (n=1).

### Visualização
- `print_towers` itera de cima para baixo pelas torres.
- Para cada nível, imprime o disco ou a haste.
- Discos são centrados com padding.

## Exercícios Sugeridos para Alunos

1. Modifique o código para aceitar o número de torres como parâmetro (generalização do problema).
2. Implemente uma versão iterativa (não recursiva) da solução.
3. Adicione cores aos discos na visualização (usando bibliotecas como `colorama`).
4. Conte o número de movimentos recursivos e compare com `2^n - 1`.
5. Teste com discos grandes (n=10) e observe o desempenho da recursão.

## Conclusão

Este projeto demonstra como problemas complexos podem ser resolvidos com recursão e estruturas de dados simples. A visualização ajuda a entender o processo passo a passo, tornando o aprendizado mais intuitivo. Explore o código, faça modificações e experimente!