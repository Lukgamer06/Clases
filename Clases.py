# Objeto 1
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
#Objeto 2
class arbol_de_navidad:
  altura = "altura"
  tipo = "tipo"
  color = "color"
  decoraciones = "decoraciones"
  regalos = "regalos"

  def encenderLuces(self):
      print("Las luces están encendidas")
  def apagarLuces(self):
      print("Las luces están apagadas")
  def agregarDecoracion(self):
      print("Se agregó una decoración")
  def quitarDecoracion(self):
      print("Se quitó una decoración")
  def agregarRegalo(self):
      print("Se agregó un regalo")
  def quitarRegalo(self):
      print("Se quitó un regalo")
#Objeto 3
class rosas:
    def __init__(self, cantidad, espinas, hojas, color, cHojas):
        self.cantidad = cantidad
        self.espinas = espinas
        self.hojas = hojas
        self.color = color
        self.cHojas = cHojas

    def AumCantidad(self, cantidad):
        self.cantidad += cantidad

    def QuitarEspinas(self):
        self.espinas = False

    def AumHojas(self, hojas):
        self.hojas += hojas

    def CambiarColorRosa(self, color):
        self.color = color

    def CambiarColorHojas(self, color2):
        self.cHojas = color2

# Crear objetos
hombre_gengibre = HombreGengibre("Trigo", "Grande", "Horno", "Canela", 5.99)
Arbol_navidad = arbol_de_navidad("10 metros","Pino","Blanco","Bolas","5")
Rosa = rosas(2, True, 2, "rojo", "verde")
# Imprimir un atributo de cada objeto
print(hombre_gengibre.sabor)
print(Arbol_navidad.color)
print(Rosa.cantidad)
