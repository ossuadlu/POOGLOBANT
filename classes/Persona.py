class Persona:

    def _init_(self):
        self.nombre=None
        self.edad=None
        self.telefono=None

    def saludar(self):
        print(f'Hola me llamo {self.nombre}')
        print(f'mi edad es {self.edad} y tengo sueño')