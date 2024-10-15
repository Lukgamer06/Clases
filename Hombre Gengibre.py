# Clase HombreGengibre
class HombreGengibre:
    def __init__(self, harina, tamaño, cocción, sabor, precio):
        self.harina = harina
        self.tamaño = tamaño
        self.cocción = cocción
        self.sabor = sabor
        self.precio = precio

    def imprimir_datos(self):
        print("Datos del HombreGengibre:")
        print(f"Harina: {self.harina}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Cocción: {self.cocción}")
        print(f"Sabor: {self.sabor}")
        print(f"Precio: {self.precio}")

    def cambiar_sabor(self, nuevo_sabor):
        self.sabor = nuevo_sabor

    def aumentar_precio(self, aumento):
        self.precio += aumento

    def cocinar(self):
        print("Cocinando en el horno...")

    def empaquetar(self):
        print("Empaquetando el HombreGengibre...")

# Clase Galleta
class Galleta:
    def __init__(self, tipo, ingredientes, textura, sabor, precio):
        self.tipo = tipo
        self.ingredientes = ingredientes
        self.textura = textura
        self.sabor = sabor
        self.precio = precio

    def imprimir_datos(self):
        print("Datos de la Galleta:")
        print(f"Tipo: {self.tipo}")
        print(f"Ingredientes: {self.ingredientes}")
        print(f"Textura: {self.textura}")
        print(f"Sabor: {self.sabor}")
        print(f"Precio: {self.precio}")

    def cambiar_textura(self, nueva_textura):
        self.textura = nueva_textura

    def aumentar_precio(self, aumento):
        self.precio += aumento

    def hornear(self):
        print("Horneando la galleta...")

    def envasar(self):
        print("Envasando la galleta...")

# Clase Pastel
class Pastel:
    def __init__(self, tipo, ingredientes, decoración, sabor, precio):
        self.tipo = tipo
        self.ingredientes = ingredientes
        self.decoración = decoración
        self.sabor = sabor
        self.precio = precio

    def imprimir_datos(self):
        print("Datos del Pastel:")
        print(f"Tipo: {self.tipo}")
        print(f"Ingredientes: {self.ingredientes}")
        print(f"Decoración: {self.decoración}")
        print(f"Sabor: {self.sabor}")
        print(f"Precio: {self.precio}")

    def cambiar_decoración(self, nueva_decoración):
        self.decoración = nueva_decoración

    def aumentar_precio(self, aumento):
        self.precio += aumento

    def hornear(self):
        print("Horneando el pastel...")

    def decorar(self):
        print("Decorando el pastel...")

# Crear objetos
hombre_gengibre = HombreGengibre("Trigo", "Grande", "Horno", "Canela", 5.99)
galleta = Galleta("Chocolate", ["Harina", "Azúcar", "Cacao"], "Crujiente", "Chocolate", 2.99)
pastel = Pastel("Tres leches", ["Harina", "Azúcar", "Leche"], "Glaseado", "Vainilla", 9.99)

# Imprimir un atributo de cada objeto
print(hombre_gengibre.sabor)
print(galleta.tipo)
print(pastel.decoración)
