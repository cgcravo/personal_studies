class Programa:
    def __init__(self, nome, data):
        self._nome = nome.title()
        self.data = data
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return "Nome: {} - Likes: {}".format(self.nome, self.likes)

class Filme(Programa):
    def __init__(self, nome, data, duracao):
        super().__init__(nome,data)
        self.duracao = duracao

    def __str__(self):
        return "Nome: {} - Duracao: {} -  Likes: {}".format(self.nome, self.duracao, self.likes)


class Serie(Programa):
    def __init__(self, nome, data, temporadas):
        super().__init__(nome,data)
        self.temporadas = temporadas

    def __str__(self):
        return "Nome: {} - Temporadas: {} -  Likes: {}".format(self.nome, self.temporadas, self.likes)

class Playlist:
    def __init__(self, nome, lista_de_programas):
        self.nome = nome
        self._lista_de_programas = lista_de_programas

    def __getitem__(self, item):
        return self._lista_de_programas[item]


    @property
    def lista(self):
        return self._lista_de_programas

    def __len__(self):
        return len(self.lista)


vingadores = Filme("vingadores guerra infinita", 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()

himym = Serie("how i met your mother", 2012, 8)
himym.dar_likes()
himym.dar_likes()
himym.dar_likes()
himym.dar_likes()

dbz = Serie("dragon ball z", 1997, 12)
dbz.dar_likes()
dbz.dar_likes()
dbz.dar_likes()
dbz.dar_likes()
dbz.dar_likes()
dbz.dar_likes()

tzt = Filme("300", 2010, 180)
tzt.dar_likes()
tzt.dar_likes()
tzt.dar_likes()
tzt.dar_likes()

atlanta = Serie("atltanta", 2018, 2)
atlanta.dar_likes()

listinha = [tzt, vingadores, dbz, himym]
playlist_fim_de_semana = Playlist("fim de semana", listinha)
for i in playlist_fim_de_semana:
    print(i)

print("Quantidade de programas na lista: {}".format(len(playlist_fim_de_semana)))


class Programa:

    def __init__(self, nome, data):
        self._nome = nome.title()
        self.data = data
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, data, duracao):
        super().__init__(nome, data)
        self._duracao = duracao

    def __str__(self):
        return "Nome: {} - Data: {} - Duracao: {}min - Likes: {} likes".format(self.nome, self.data, self._duracao, self.likes)

class Serie(Programa):
    def __init__(self, nome, data, temporadas):
        super().__init__(nome, data)
        self._temporadas = temporadas

    def __str__(self):
        return "Nome: {} - Data: {} - Temporadas: {} temporadas - Likes: {} likes".format(self.nome, self.data, self._temporadas, self.likes)


vingadores = Filme("vingadores guerra infinita", 2018, 180)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

how_i_met_your_mother = Serie(" how i met your mother", 2012, 8)
how_i_met_your_mother.dar_like()
how_i_met_your_mother.dar_like()
how_i_met_your_mother.dar_like()
how_i_met_your_mother.dar_like()
how_i_met_your_mother.dar_like()
how_i_met_your_mother.dar_like()
how_i_met_your_mother.dar_like()

lista = [vingadores, how_i_met_your_mother]

for programa in lista:
    print(programa)
