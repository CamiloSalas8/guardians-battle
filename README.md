# Guardians of the Ancient Kingdom - Sistema de Batalla POO

Este proyecto es un simulador de combates por turnos desarrollado en Python. Ha sido diseñado para poner en práctica e ilustrar de forma clara y funcional los pilares fundamentales de la **Programación Orientada a Objetos (POO)**.

## 🚀 Características del Proyecto

El juego recrea un entorno de duelo interactivo donde se pueden enfrentar tres arquetipos de clases clásicas: **Guerreros**, **Magos** y **Arqueros**. Cada tipo de personaje comparte una estructura base común pero actúa bajo reglas y mecánicas de ataque completamente individuales.

### Pilares de POO Implementados:

1. **Abstracción**: Se define la clase base `Personaje` utilizando el módulo `abc` de Python como una **Clase Abstracta**. Esto establece un contrato de diseño: define el molde del personaje y obliga a la existencia del combate, pero impide que se puedan crear instancias de un "Personaje" genérico.
2. **Herencia**: Las clases específicas (`Guerrero`, `Mago` y `Arquero`) extienden y heredan la estructura de la clase padre `Personaje`. Esto evita la duplicidad innecesaria de código, reutilizando los atributos fundamentales y la validación de estado.
3. **Encapsulamiento**: Todos los atributos críticos de los personajes (`nombre`, `vida`, `ataque`, `defensa`) están protegidos mediante el uso de atributos privados (`__`). El acceso y modificación segura de los datos se realiza estrictamente a través de métodos de acceso (**Getters** y **Setters**). El modificador de la salud incluye lógica de control que restringe el valor de la vida estrictamente en un rango de 0 a 100.
4. **Polimorfismo**: El método abstracto `atacar(objetivo)` se redefine (**sobrescribe**) de manera independiente dentro de cada subclase para alterar el comportamiento final de la acción según el rol:
   * **Guerrero**: Su ofensiva física está potenciada, añadiendo un **20% de incremento de daño** base al golpear.
   * **Mago**: Su poder místico le permite lanzar conjuros letales que **ignoran por completo la defensa** del oponente.
   * **Arquero**: Su precisión le otorga la posibilidad de asestar un golpe crítico que inflige el **doble de daño** si su ataque base supera la defensa enemiga.

## 🛠️ Requisitos Técnicos

* **Python 3.x**
* Módulo `abc` (incorporado en la librería estándar de Python).
* Módulo `time` (incorporado, empleado para añadir dinamismo y pausas en el registro de turnos).

## 📖 Instrucciones de Uso

1. Descarga o clona este repositorio en tu máquina local.
2. Asegúrate de tener los archivos `main.py` y `README.md` en el mismo directorio.
3. Abre una terminal en la ruta correspondiente y ejecuta el script principal:
   ```bash
   python main.py
