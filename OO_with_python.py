
#tudo em py e um objeto, mesmo classes e metaclasses
#copiando uma lista:
x = ["a", "b", "c"]
y=x #cria uma outra referencia, nao um, novo objeto
y[1] = "z"
print(x) #veremos que alterar y altera o valor de x tb
#para criar outro objeto:
y = list(x)
#ou
y = x[:]

#metodos sao funcoes que pertencem a um objeto especifico. Sao chamadas com a notacao: objeto.metodo(argumento)
#objetos de tipos diferentes podem ter metodos diferentes de mesmo nome. O metodo depende do tipo do objeto.


class Program:
    def __init__(self, name, date):
        self._name = name.title()
        self.date = date
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def like_it(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return "Name: {} - Likes: {}".format(self.name, self.likes)

class Movie(Program):
    def __init__(self, name, date, length):
        super().__init__(name,date)
        self._length = length

    def __str__(self):
        return "Name: {} - Date: {} - Length: {}min - Likes: {} likes".format(self.name, self.date, self._length, self.likes)

class Serie(Program):
    def __init__(self, name, date, seasons):
        super().__init__(name,date)
        self._seasons = seasons

    def __str__(self):
        return "Name: {} - Date: {} - Seasons: {} - Likes: {} likes".format(self.name, self.date, self._seasons, self.likes)

class Playlist:
    def __init__(self, name, list_of_programs):
        self.nome = name
        self._list_of_programs = list_of_programs

    def __getitem__(self, item):
        return self._list_of_programs[item]

    @property
    def list(self):
        return self._list_of_programs

    def __len__(self):
        return len(self.list)


avengers = Movie("avengers infinity war", 2018, 160)
avengers.like_it()
avengers.like_it()

himym = Serie("how i met your mother", 2012, 8)
himym.like_it()
himym.like_it()
himym.like_it()
himym.like_it()

dbz = Serie("dragon ball z", 1997, 12)
dbz.like_it()
dbz.like_it()
dbz.like_it()
dbz.like_it()
dbz.like_it()
dbz.like_it()

th = Movie("300", 2010, 180)
th.like_it()
th.like_it()
th.like_it()
th.like_it()

atlanta = Serie("atltanta", 2018, 2)
atlanta.like_it()

print("Weekend playlist")
little_list = [th, himym]
playlist_weekend = Playlist("weekend", little_list)
for i in playlist_weekend:
    print(i)

print("Amount of programs on the list: {}".format(len(playlist_weekend)))

print("Catalog")
catalog = [avengers, himym, th, dbz]
for program in catalog:
    print(program)
