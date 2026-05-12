from abc import ABC, abstractmethod
import time

#  CLASE ABSTRACTA (ABSTRACCIÓN) 
class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        self.__nombre = nombre
        self.set_vida(vida)  # Validación mediante setter 
        self.__ataque = ataque
        self.__defensa = defensa

    # ENCAPSULAMIENTO (GETTERS Y SETTERS)
    def get_vida(self):
        return self.__vida

    def set_vida(self, valor):
        # La vida debe estar entre 0 y 100 
        if valor < 0:
            self.__vida = 0
        elif valor > 100:
            self.__vida = 100
        else:
            self.__vida = valor

    def get_nombre(self): return self.__nombre
    def get_ataque(self): return self.__ataque
    def get_defensa(self): return self.__defensa

    def esta_vivo(self):
        return self.__vida > 0

    # MÉTODO ABSTRACTO (POLIMORFISMO OBLIGATORIO)
    @abstractmethod
    def atacar(self, objetivo):
        pass

# --- HERENCIA Y POLIMORFISMO  ---

class Guerrero(Personaje):
    def atacar(self, objetivo):
        # Habilidad: +20% de incremento de daño
        daño_potenciado = self.get_ataque() * 1.2
        final = max(0, daño_potenciado - objetivo.get_defensa())
        objetivo.set_vida(objetivo.get_vida() - final)
        print(f"⚔️ {self.get_nombre()} (Guerrero) asesta un golpe potente! Daño: {final:.1f}")

class Mago(Personaje):
    def atacar(self, objetivo):
        # Habilidad: Ignora la defensa del objetivo
        daño_final = self.get_ataque()
        objetivo.set_vida(objetivo.get_vida() - daño_final)
        print(f"🔮 {self.get_nombre()} (Mago) lanza un hechizo que ignora defensas! Daño: {daño_final}")

class Arquero(Personaje):
    def atacar(self, objetivo):
        daño_base = self.get_ataque()
        # Habilidad: Si ataque > defensa, hace el doble de daño 
        if daño_base > objetivo.get_defensa():
            daño_base *= 2
        final = max(0, daño_base - objetivo.get_defensa())
        objetivo.set_vida(objetivo.get_vida() - final)
        print(f"🏹 {self.get_nombre()} (Arquero) dispara con precisión crítica! Daño: {final}")

# --- LÓGICA DE COMBATE (CICLO DE JUEGO) ---

def iniciar_batalla(p1, p2):
    print(f"✨ ¡BATALLA INICIADA: {p1.get_nombre()} vs {p2.get_nombre()}! ✨")
    turno = 1
    
    while p1.esta_vivo() and p2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        
        # Ataque del primer personaje
        p1.atacar(p2)
        print(f"💖 Vida restante de {p2.get_nombre()}: {p2.get_vida():.1f}")
        
        if not p2.esta_vivo():
            print(f"\n💀 {p2.get_nombre()} ha caído. ¡{p1.get_nombre()} es el vencedor! 🏆")
            break
            
        time.sleep(0.8) # Breve pausa para legibilidad
        
        # Ataque del segundo personaje
        p2.atacar(p1)
        print(f"💖 Vida restante de {p1.get_nombre()}: {p1.get_vida():.1f}")
        
        if not p1.esta_vivo():
            print(f"\n💀 {p1.get_nombre()} ha caído. ¡{p2.get_nombre()} es el vencedor! 🏆")
            break
            
        turno += 1
        time.sleep(0.8)

# --- EJECUCIÓN ---

if __name__ == "__main__":
    arturo = Guerrero("Arturo", 100, 30, 20)
    
    merlin = Mago("Merlín", 80, 40, 10)
    
    iniciar_batalla(arturo, merlin)        