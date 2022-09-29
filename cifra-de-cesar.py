class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque
def adicionar_alfabeto(deque, alfabeto):
    for item in alfabeto:#para cada letra da string alfabeto
      deque.add_front(item)#coloca no final do deque
    return None
def decifrar(deque,texto_cifrado, chave):
    lista_decifrada=[]
    #descolar ate achar a letra igual a da string, depois descolar de acordo com a chave e adicionar a correspondente a lista 
    for i in texto_cifrado:
        c=0
        while c==0: #um substituto para o while True   
            a= deque.remove_rear()
            deque.add_front(a)
            if a==i:
                b=0
                while b<=chave:
                    l=deque.remove_front()
                    deque.add_rear(l)
                    b+=1
                c=1
            
        lista_decifrada.append(l)
    text_decifrado=''.join(map(str,lista_decifrada))
    return text_decifrado


d = Deque()
adicionar_alfabeto(d, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
texto_cifrado = 'ECUC'
print(f'texto_plano: {decifrar(d, texto_cifrado, 2)}')
print(f'{str(d)}')
print(f'{len(str(d))}')
