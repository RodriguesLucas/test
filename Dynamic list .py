class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinckdList:
    def __init__(self, ):
        self.head = None
        self.size = 0  # Quantidade de elementos da lista contador

    # inserir
    def append(self, elem):
        pointer = self.head
        if self.head:
            # inserção quando a lista possui elementos
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self.size = self.size + 1

    # Função imprimir
    def print(self):
        pointer = self.head
        position = 0
        if pointer is None:
            print("Lista vazia!")
        else:
            while pointer is not None:
                print(f"[{position}]{pointer.data}", end=" ")
                position += 1
                pointer = pointer.next

    # pesquisar na lista
    def search(self, elem):
        pointer = self.head
        position = 0
        if pointer is None:
            print("Lista vazia!")
        else:
            while pointer is not None:
                if elem == pointer.data:
                    print(f"[{position}]{pointer.data}", end=" ")
                    return
                position += 1
                pointer = pointer.next
            print("Valor não encontrado!")

    # remove da lista
    def remove(self, elem):
        if self.head is None:
            print("Não há elementos pra excluír!")
        elif self.head.data == elem:
            self.head = self.head.next
            print("Elemento excluído!")
        else:
            antec = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    antec.next = pointer.next
                    pointer.next = None
                antec = pointer
                pointer = pointer.next
            print("Elemento não encontrado!")

    # ordena de forma crescente
    def sort_crescent(self):
        if self.head is None:
            print("A Lista está vazia!")
        else:
            pointer = self.head
            while pointer is not None:
                aux = pointer.next
                while aux is not None:
                    if aux.data < pointer.data:
                        pointeraux = pointer.data
                        pointer.data = aux.data
                        aux.data = pointeraux
                    aux = aux.next
                pointer = pointer.next
            print("Lista ordenada de forma crescente!")

    # ordena de forma decrescente
    def sort_decrescent(self):
        if self.head is None:
            print("A Lista está vazia!")
        else:
            pointer = self.head
            while pointer is not None:
                aux = pointer.next
                while aux is not None:
                    if aux.data > pointer.data:
                        pointeraux = pointer.data
                        pointer.data = aux.data
                        aux.data = pointeraux
                    aux = aux.next
                pointer = pointer.next
            print("Lista ordenada de forma decrescente!")

    def append_randow(self, elem):
        from random import randint
        for i in range(elem):
            pointer = self.head
            if self.head:
                while pointer.next:
                    pointer = pointer.next
                pointer.next = Node(randint(0, 1000))
            else:
                self.head = Node(randint(0, 1000))


listt = LinckdList()
#menu
while True:
    print()
    print("1 - Inserir na lista")
    print("2 - Excluir")
    print("3 - Busca")
    print("4 - Imprime lista")
    print("5 - Ordenar crescente")
    print("6 - Ordenar descrescente")
    print("7 - Acrescentar aleatóriamente")
    print("0 - Sair")
    opc = int(input())
    print("")
    if 0 <= opc <= 8:
        if opc == 1:
            a = int(input("Informe um  valor:\n"))
            listt.append(a)

        elif opc == 2:
            a = int(input("Informe o valor: \n"))
            listt.remove(a)

        elif opc == 3:
            a = int(input("Informe o valor: \n"))
            listt.search(a)

        elif opc == 4:
            listt.print()

        elif opc == 5:
            listt.sort_crescent()

        elif opc == 6:
            listt.sort_decrescent()

        elif opc == 7:
            a = int(input("Informe a quantidade de valores que quer adicionar: \n"))
            listt.append_randow(a)

        elif opc == 0:
            print("Finalizando...")
            break
    else:
        print("Informe uma opcão valida!")
