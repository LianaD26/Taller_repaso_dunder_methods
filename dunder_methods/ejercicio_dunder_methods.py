from dataclasses import dataclass
@dataclass
class Elemento:
    nombre : str

    def __eq__(self, elemento):
        return self.nombre == elemento.nombre #verificar si son iguales


class Conjunto:
    contador = 0
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.lista : list[Elemento] = []
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def atributo(self):
        return self.__id
    def contiene(self, elemento : Elemento) -> bool:
        for e in self.lista:
            if e.nombre == elemento.nombre:
                return True
        return False
    def agregar_elemento(self, elemento : Elemento):
        if not self.contiene(elemento):
            self.lista.append(elemento)
    def unir(self, conjunto : "Conjunto"):
        for e in conjunto.lista:
            if not self.contiene(e):
                self.lista.append(e)

    def __add__(self, conjunto : "Conjunto"):
        conjunto2 = Conjunto
        for e in self.lista:
            conjunto2.agregar_elemento(e)

        for e in conjunto.lista:
            conjunto.agregar_elemento(e)

        return conjunto2
    def intersectar(self, conjunto1 : "Conjunto 1", conjunto2 : "Conjunto 2"):
        elementos_c1 = Conjunto
        elementos_c2 = Conjunto
        #<Nombre Conjunto 1> INTERSECTADO <Nombre Conjunto 2>
        conjunto1_INTERSECTADO_conjunto2 = Conjunto
        for e in conjunto1.lista:
            elementos_c1.agregar_elemento(e)
        for e in conjunto2.lista:
            elementos_c2.agregar_elemento(e)
        for i in elementos_c1:
            if i in elementos_c2:
                conjunto1_INTERSECTADO_conjunto2.agregar_elemento(i)
        return conjunto1_INTERSECTADO_conjunto2
    def __str__(self):
        #Conjunto <nombre>: (<nombre elemento 1>, <nombre elemento 2>,...,<nombre elemento n>)
        return f"Conjunto {self.nombre} : {self.lista}"



