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

