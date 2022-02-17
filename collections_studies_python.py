import numpy as numpy

from abc import ABCMeta, abstractmethod
#ABCMeta transform class into an abstract class
#abstractmethod transform method into a abstract method
class Account(metaclass= ABCMeta):

    def __init__(self, code):
        self._code = code
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @property
    def code(self):
        return self._code

    def deposit(self, value):
        self._balance += value

    @abstractmethod
    def next_month(self):
        pass

    def __str__(self):
        return "[>> Code {}  Balance {}<<]".format(self.code, self.balance)

class CheckingAccount(Account):

    def next_month(self):
        self._balence -= 2

class SavingsAccount(Account):

    def next_months(self):
        self._balance *= 1.01
        self._balance -= 3

class InvestimentsAccount(Account):

    def next_month(self):
        pass

#it's not possible to call an abstract class
'''account1 = Account(15)
account.deposit(100)'''


account2 = CheckingAccount(13)
account2.deposit(200)


account3 = SavingsAccount(16)
account3.deposit(400)

account4 = InvestmentsAccount(89)

accounts = [account2, account3, account4]

for account in accounts:
    account.deposit(2)
    account.next_month()
    print(account)

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

#PARTE 2

usuarios_data_science = [15, 42, 56, 34]
usuarios_machine_learning = [22, 42, 56, 36]

#assistiram = []
#assistiram.extend(usuarios_data_science)
#ou
#criar uma copia raza (quando copia objetos, copia so a referencia)
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)
#SET vem de conjuntos da matematica. remove os elementos repetidos e retorna
#para criar um conjunto simples (type = set) basta usar {}
print(set(assistiram))
print([1,2,4,1,5])
print(set([1,2,4,1,5]))
print({1,2,4,1,5})
#nao existe ordem de entrada num conjunto as posicoes sao aleatorias, porem e um iteravel e mutavel.
#assim, nao se pode acessar uma posicao, como numa lista
#usa-se conjuntos qunado a ordem de entrada nao imporata
for i in set(assistiram):
    print(i)

#OU para conjuntos
usuarios_data_science = {15, 42, 56, 34}
usuarios_machine_learning = {22, 42, 56, 36}
print(usuarios_data_science | usuarios_machine_learning) # OU - um ou outro (uniao dos elementos dos dois conjuntos
print(usuarios_data_science & usuarios_machine_learning) # & - somente os elementos em comum
print(usuarios_data_science - usuarios_machine_learning) # remove os elementos que aparecem tb no segundo conjunto
print(usuarios_data_science ^ usuarios_machine_learning) # OU EXCLUSIVO - aparece em apenas 1 dos dois conjuntos (nao aparece em 2)

usuarios_data_science.add(13) #adiciona elementos no conjunto (.append() nao funciona pq n tem ordem aqui)
print(usuarios_data_science)

usuarios = usuarios_data_science & usuarios_machine_learning
frozenset(usuarios) #transforma um conjunto em imutavel
print(usuarios)

#conjuntos podem ser utilizados com outras coisas, como objetos, strings etc..
texto = "Meu nome e Carlos e eu gosto muito de cachorros de nome Carlos"
texto_quebrado = texto.split()
print(texto_quebrado) #quebra um conjunto de texto, por padrao com espacos vazios
print(set(texto_quebrado))


#dicionario
dicionario = {"Carlos": 2, "cachorro": 1, "sapato": 1, "Marie": 2}
print(dicionario.get("Carlos",0)) #se nao pegar no dicionario, retorna zero
print(dicionario.get("Fernando",0))
dicionario2 = dict(Guilherme = 1, Luffy = 2) #istancia dicionario diretamente
print(dicionario2)
del(dicionario["Carlos"]) #remove 1 elemento do dicionario
print(dicionario)
print("Carlos" in dicionario)
print("sapato" in dicionario)
for i in dicionario: #imprime as chaves, nao os valores
    print(i)
for i in dicionario.keys(): #outra forma
    print(i)
for i in dicionario.values(): #imprime os valores, nao as chaves
    print(i)
for i in dicionario.items(): #imprime linha a linha - como tuplas
    print(i)
for chave, valor in dicionario.items(): #imprime linha a linha - como tuplas ja desempacotadas
    print(chave, valor)

#ja que cria uma lista, podemos fazer list comprehension
list_comprehension = ["palvra {}".format(i) for i in dicionario.keys()]
print(list_comprehension)

#contado elementos na lista de palavras
texto_low = texto.lower()
texto_low_quebrado = texto_low.split()
print(texto_low_quebrado)
aparicoes = {}
for palavra in texto_low_quebrado:
    ate_agr = aparicoes.get(palavra, 0) #procura se ha a palavra em "aparicoes", senao, retorna zero. se sim, pega a chave
    aparicoes[palavra] = ate_agr + 1 #se a palavra nao existe na lista, vai adiciona-la, como no teste abaixo. soma 1 dps
print("contando as palavras do texto:", aparicoes)
aparicoes["testando"] = 10 #no caso das "palavras" acima, nao precisa de aspas pq reconhece a lista de strings
print(aparicoes)

#agr usando defaultdict()
print("agora usando defaultdict")
from collections import defaultdict
#tem que passar uma funcao "fabrica de valor padrao" para o defaultdict
#ferramenta super poderosa, podemos criar qualquer funcao que sera chamada quando o dicionario n achar um valor.
#podemos criar objetos novos, por exemplo etc...
#a funcao int(), quando nenhum valor e passado retorna zero, senao retorna o valor inteiro
#passar so o tipo, nao sei pq
aparicoes2 = defaultdict(int)
for palavra in texto_low_quebrado:
    #ate_agr = aparicoes2[palavra] #agr nao precisa da funcao get, o default ja existe
    #aparicoes2[palavra] = ate_agr + 1
    aparicoes2[palavra] += 1 #agr nem precisa dessa variavel temporaria "ate_agr"
print(aparicoes2)
aparicoes2["testando defaultdict"]
aparicoes2["testando de novo"] = 14
print(aparicoes2)

#usando contador (recebe um iteravel ou um mapping (dicionario) e retorna dicionario que conta os proprios elementos)
from collections import Counter
print("usando funcao contador")
aparicoes3 = Counter(texto_low_quebrado)
print(aparicoes3)

#contando letras num texto
print("contando letras")
texto2 = """ Então o que vamos fazer é o seguinte: vamos pegar dois textos, por exemplo eu posso entrar no blog da Alura e pegar textos do blog da Alura. Eu posso pegar um texto que está falando sobre expressões regulares e posso pegar um outro texto de outro assunto, só para não termos dois assuntos similares. Vou pegar um o outro assunto, temos um de programação e um aqui que é de negócios: B2C, B2B, coisas do gênero. Então dois assuntos distintos, um de programação e um não de programação. """
def conta_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, valor/total_de_caracteres) for letra, valor in aparicoes.items()]
    contador_proporcoes = Counter(dict(proporcoes))
    mais_comuns = contador_proporcoes.most_common(10)

    for caractere,proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao*100))

conta_letras(texto2)
