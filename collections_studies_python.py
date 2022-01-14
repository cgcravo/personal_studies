import numpy as numpy

from abc import ABCMeta, abstractmethod
#ABCMeta para transformar a classe em abstrata
class Conta(metaclass= ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    @property
    def codigo(self):
        return self._codigo

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_mes(self):
        pass

    def __str__(self):
        return "[>> Codigo {}  Saldo {}<<]".format(self.codigo, self.saldo)

class ContaCorrente(Conta):

    def passa_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimentos(Conta):

    def passa_mes(self):
        pass

#nao pode instanciar uma classe abstrata
'''conta1 = Conta(15)
conta1.deposita(100)'''


conta2 = ContaCorrente(13)
conta2.deposita(200)


conta3 = ContaPoupanca(16)
conta3.deposita(400)

conta4 = ContaInvestimentos(89)

contas = [conta2, conta3, conta4]

for conta in contas:
    conta.deposita(2)
    conta.passa_mes()
    print(conta)

#pip install numpy
#arrays sao especificos no phyton para trabalhar com listas com elementos especificos
#evitamos array puro, se precisamos, e comum usar com numpy
import numpy as np
lista_numeros = np.array([1, 3.5])
print(lista_numeros)
print(lista_numeros + 3)

#igualdade
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        #retorna True se o a comparacao da caracteristica escolhida e igual ao do outro objeto
        return self._codigo == other._codigo and self._saldo == other._saldo

    def deposita(self, valor):
        self._saldo += valor


    def __str__(self):
        return"[>> Conta {} Saldo {} <<]".format(self._codigo, self._saldo)

print("verificacoes de igualdaes e tipos")
CS1 = ContaSalario(15)
CS2 = ContaSalario(18)
CS3 = ContaSalario(18)
CC1 = ContaCorrente(15)

CS1.deposita(100)
CS2.deposita(300)
CS3.deposita(200)

lista_salario = [CS1,CS2, CS3]

print(lista_salario[0] == lista_salario[1])
print(lista_salario[0] == lista_salario[2])
print(lista_salario[1] == lista_salario[2])

#a conta x ta numa lista contendo a conta y? se a igualdade estiver, sim!
print(CS1 in [CS2])
print(CS1 in [CS3])
print(CS2 in [CS3])

print(CC1 == CS1)

#verificacao de hieraquia
print(isinstance(CC1, Conta))
print(isinstance(CS1, Conta))

#enumeracao
lista_numeros = [52, 33, 50, 29, 54, 19, 12, 11, 50]
for i in (range(len(lista_numeros))):
    print(i, lista_numeros[i])

print("USANDO ENUMERATE")
print("cria um enumerate, mas ele nao e utilizado pra nada - lazy")
print(enumerate(lista_numeros))
print("cria um enumerate e chama uma utilizacao com list")
print(list(enumerate(lista_numeros)))
print("cria um enumerate e chama utilizacao com for")
for i in enumerate(lista_numeros):
    print(i)

print("DESEMPACOTANDO TUPLAS")
print("cria um enumerate e chama utilizacao com for ja desempacotoando a tupla")
for indice, numero in enumerate(lista_numeros):
    #strings no meio n entram como indice para o for da lista
    print(indice, "x", "carlos", "x", numero)
usuarios = [("Carlos", 31, 1990), ("Maria", 37, 1984), ("Giselo", 3, 2019)]
for nome, idade, data in usuarios:
    print(nome, data)
for _, idade, _ in usuarios:
    print(idade)


#lazy, ta preparado pra gerar, mas nao gera ate ter um comando
print("...mesma coisa com range e outros metodos...")
print("cria um range, mas ele nao e utilizado pra nada - lazy")
print(range(len(lista_numeros)))
print("cria um enumerate, e chama uma utilizacao com list")
print(list(range(len(lista_numeros))))

print("ORDENADORES")
print(sorted(lista_numeros))
print(list(reversed(lista_numeros))) #reversed devolve um iterador, mas nao usa ele. o reverso da lista original, nao ordenada
print(sorted(lista_numeros, reverse = True))
lista_numeros.sort() #funcao, altera a lista original
print(lista_numeros)


#comparacao de objetos => reduzir o objeto a algum valor comparavel

def extrai_saldo(conta):
    return conta._saldo

for i in sorted(lista_salario, key=extrai_saldo):
    print(i)

#STANDARD OPERATORS AS FUNCTIONS
#"attrgetter" => funcao built-in pra pegar um atributo de uma classe
from operator import attrgetter
print("forma attrgetter...")
for i in sorted(lista_salario, key=attrgetter("_saldo")):
    print(i)


#pra aplicar o total ordering, so precisa definir o __eq__ e o __lt__, o resto e automatico
from functools import total_ordering
@total_ordering
class Exemplo:

    def __init__(self, atributo1, atributo2):
        self._atributo1 = atributo1
        self._atributo2 = atributo2
        self._atributo3 = 0

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self._atributo1 == other._atributo1 and self._atributo2 == other._atributo2

    def __lt__(self, other):
        if self._atributo1 != other._atributo1:
            return self._atributo1 < other._atributo1
        elif self._atributo2 != other._atributo2:
            return self._atributo2 < other._atributo2
        else:
            return self._atributo3 < other._atributo3

    def __str__(self):
        return "[>> {} - {} - {} <<]".format(self._atributo1, self._atributo2, self._atributo3)

    def insere(self, atributo3):
        self._atributo3 = atributo3

objeto1 = Exemplo(12,45)
objeto2 = Exemplo(12,42)
objeto3 = Exemplo(14,45)
objeto1.insere(1)
objeto2.insere(2)
objeto3.insere(3)

lista_exemplo = [objeto1, objeto2, objeto3]

#sem metodo de ordenacao interno
print("ordenando pelo atributo 1")
for i in sorted(lista_exemplo, key=attrgetter("_atributo1")):
    print(i)
print("ordenando pelo atributo 2")
for i in sorted(lista_exemplo, key=attrgetter("_atributo2")):
    print(i)
print("ordenando pelo atributo 3")
for i in sorted(lista_exemplo, key=attrgetter("_atributo3")):
    print(i)
#com metodo de ordenacao interno
print("outra maneira")
for objeto in sorted(lista_exemplo):
    print(objeto)

for objeto in sorted(lista_exemplo, reverse=True):
    print(objeto)

print(objeto1 < objeto2)
print(objeto1 < objeto3)
print(objeto2 < objeto3)

#ordenando por mais de uma condicao
print("ordenando pelo atributo 1, dps 2")
for i in sorted(lista_exemplo, key=attrgetter("_atributo1", "_atributo2")):
    print(i)
print("ordenando pelo atributo 2, dps 1")
for i in sorted(lista_exemplo, key=attrgetter("_atributo2", "_atributo1")):
    print(i)
print("ordenando pelo atributo 2, dps 3")
for i in sorted(lista_exemplo, key=attrgetter("_atributo2", "_atributo3")):
    print(i)

print("ordenando internamente")
for objeto in sorted(lista_exemplo):
    print(objeto)
print(objeto1<objeto2)
print(objeto1<objeto3)
print(objeto2<objeto3)


#total ordering:
print("usando o total_ordering")
print(objeto1<=objeto2)
print(objeto1<=objeto3)
print(objeto2>=objeto3)