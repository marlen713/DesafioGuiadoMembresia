from abc import ABC, abstractmethod

class  Membresia (ABC):
    def __init__(self, correo_subs: str, num_tarjeta: str): 
        self.__correo_subs = correo_subs
        self.__num_tarjeta = num_tarjeta

    @property
    def correo_subs(self):
        return self.__correo_subs

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta
    
    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int ):
        pass 

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1: 
            return Membresia_Basica(self.correo_subs, self.num_tarjeta)
        if nueva_membresia == 2: 
            return Membresia_Familiar(self.correo_subs, self.num_tarjeta)
        if nueva_membresia == 3: 
            return Membresia_SinConexion(self.correo_subs, self.num_tarjeta)
        if nueva_membresia == 4: 
            return Membresia_Pro(self.correo_subs, self.num_tarjeta)

    
class Membresia_Gratis(Membresia):
    costo = 0 
    cantidad_dispositivos = 1
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 or nueva_membresia > 4: 
            return self
        else: 
            return self._crear_nueva_membresia(nueva_membresia)


class Membresia_Basica(Membresia):
    costo = 3000
    cantidad_dispositivos = 2

    def cancelar_suscripcion(self):
        return Membresia_Gratis(self.correo_subs, self.num_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 2 or nueva_membresia > 4: 
            return self #retorna 1 que seria la basica
        else:
            return self._crear_nueva_membresia(nueva_membresia)
    
    
    
class Membresia_Familiar(Membresia_Basica):
    costo = 5000
    cantidad_dispositivos = 5 
    
    def cambiar_suscripcion (self, nueva_membresia: int):
        if nueva_membresia not in [1,3,4]:    
            return self 
        else: #Si no, crea la nueva membresia de tipo familiar
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        pass


    
class Membresia_SinConexion(Membresia_Basica):
    costo = 3500
    cantidad_dispositivos =2

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia not in [1,2,4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_contenido(self):
        pass


    
class Membresia_Pro(Membresia_Familiar,Membresia_SinConexion,Membresia_Basica):
    costo = 7000
    cantidad_dispositivos = 6
    
    def __init__(self, correo_subs: str, num_tarjeta: str):
        super().__init__(correo_subs, num_tarjeta)
    
    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 or nueva_membresia >3: 
            return self
        else: 
            return self._crear_nueva_membresia(nueva_membresia)
        
        
#Caso 1: 
g = Membresia_Gratis("usuario_3050", "265149375")
print(type(g))

#Caso 2: Cambiar de gratis a basica 
basica = g.cambiar_suscripcion(1)
print(type(basica))

#Caso 3: Cambiar de básica a familiar 
f = basica.cambiar_suscripcion(2)
print(type(f))

#Caso 4 : Cambiar a Sin Conexion 
sc = f.cambiar_suscripcion(3)
print(type(sc))


#Caso 5: Cambiar a Pro 
p = sc.cambiar_suscripcion(4)
print(type(p))

#Caso 6 : Cancelar suscripcion 
c =  p.cancelar_suscripcion()
print(type(c))



