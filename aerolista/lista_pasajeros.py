# ==============================================================
#  lista_pasajeros.py  ·  Lista enlazada de pasajeros
#  ✍ ESTE ES EL ARCHIVO DONDE TRABAJAS TÚ
# --------------------------------------------------------------
#        head
#         |
#         v
#    +----------+---+    +----------+---+    +----------+---+
#    | #1005    | o-+--->| #1002    | o-+--->| #1009    | o-+---> None
#    | Diana 3C |   |    | Ana 1A   |   |    | Luis 7D  |   |
#    +----------+---+    +----------+---+    +----------+---+
#       data    next        data    next        data    next
#
#  Los pasajeros quedan en ORDEN DE LLEGADA (el orden en que reservaron).
#
#  ✅ Ya funcionan: la clase Nodo, el constructor __init__ y ingresar.
#  ✍ Tú implementas los otros 9 métodos. Reglas:
#     1. Recorre SIEMPRE con el patrón de la Unidad 3:
#            actual = self.head
#            while actual is not None:
#                ...
#                actual = actual.next
#     2. NO conviertas la lista enlazada en una list de Python para
#        buscar, modificar o eliminar (nada de list(), in, index, sort).
#     3. La ÚNICA list de Python permitida es el RESULTADO de listar()
#        y de filtrar_por_clase(): es la "caja" que Flask envía al navegador.
#     4. La clase NUNCA hace print() ni input(): RETORNA valores.
#     5. Para empezar un método, BORRA su línea  raise NotImplementedError(...)
#        y escribe tu código en su lugar.
# ==============================================================

from pasajero import Pasajero


class Nodo:
    """Un vagón del tren: lleva un pasajero (data) y el enganche al siguiente (next)."""

    def __init__(self, data):
        self.data = data          # el Pasajero que viaja en este vagón
        self.next = None          # al nacer no está enganchado a nadie


class ListaPasajeros:
    """Lista enlazada simple con todas las reservas del vuelo."""

    # ----------------------------------------------------------
    # ✅ EJEMPLO RESUELTO 1: el constructor
    # ----------------------------------------------------------
    def __init__(self):
        self.head = None          # la cabeza: el primer nodo (None = avión vacío)
        self.cantidad = 0         # cuántas reservas (nodos) hay

    # ----------------------------------------------------------
    # ✅ EJEMPLO RESUELTO 2: ingresar (= insertar_final de la Unidad 3)
    #    Engancha un pasajero NUEVO al final del tren.
    # ----------------------------------------------------------
    def ingresar(self, pasajero):
        nuevo = Nodo(pasajero)                # 1. creo el vagón con el pasajero

        if self.head is None:                 # 2a. Lista vacía:
            self.head = nuevo                 #     el nuevo es la cabeza
        else:                                 # 2b. Lista con nodos:
            actual = self.head                #     pongo el dedo en la cabeza
            while actual.next is not None:    #     mientras NO sea el último...
                actual = actual.next          #     ...avanzo un vagón
            actual.next = nuevo               #     el último ahora apunta al nuevo

        self.cantidad = self.cantidad + 1     # 3. hay una reserva más
        return True

    # ==========================================================
    # ✍ TAREA · 9 métodos implementados
    # ==========================================================

    def esta_vacia(self):
        """Retorna True si no hay ninguna reserva; False si hay al menos una."""
        return self.head is None

    def longitud(self):
        """Retorna cuántas reservas hay."""
        return self.cantidad

    def listar(self):
        """Retorna una list de Python con TODOS los Pasajero, en orden:
        desde head hasta el último. Si está vacía retorna []."""
        resultado = []
        actual = self.head
        while actual is not None:
            resultado.append(actual.data)
            actual = actual.next
        return resultado

    def buscar(self, numero):
        """Búsqueda lineal por número de reserva (int).
        Retorna el Pasajero encontrado o None si no existe."""
        actual = self.head
        while actual is not None:
            if actual.data.numero == numero:
                return actual.data
            actual = actual.next
        return None

    def buscar_por_asiento(self, asiento):
        """Retorna el Pasajero sentado en ese asiento ("7D") o None si está libre."""
        asiento_buscado = str(asiento).strip().upper()
        actual = self.head
        while actual is not None:
            if str(actual.data.asiento).strip().upper() == asiento_buscado:
                return actual.data
            actual = actual.next
        return None

    def buscar_por_cedula(self, cedula):
        """Retorna el Pasajero con esa cédula (str) o None."""
        cedula_buscada = str(cedula).strip()
        actual = self.head
        while actual is not None:
            if str(actual.data.cedula).strip() == cedula_buscada:
                return actual.data
            actual = actual.next
        return None

    def modificar(self, numero, nuevo_nombre, nueva_edad, nuevo_asiento):
        """Cambia nombre, edad y asiento del pasajero con ese número.
        Usa buscar(). El nodo NO cambia de lugar en la lista: solo cambia su carga.
        Retorna True si lo modificó, False si no existe."""
        pasajero = self.buscar(numero)
        if pasajero is None:
            return False
        pasajero.nombre = nuevo_nombre
        pasajero.edad = nueva_edad
        pasajero.asiento = str(nuevo_asiento).strip().upper()
        return True

    def eliminar(self, numero):
        """Cancela la reserva: desengancha el nodo que tiene ese número.
        Retorna el Pasajero eliminado, o None si no existía."""
        if self.head is None:
            return None

        if self.head.data.numero == numero:
            eliminado = self.head.data
            self.head = self.head.next
            self.cantidad = self.cantidad - 1
            return eliminado

        anterior = self.head
        actual = self.head.next
        while actual is not None:
            if actual.data.numero == numero:
                eliminado = actual.data
                anterior.next = actual.next
                self.cantidad = self.cantidad - 1
                return eliminado
            anterior = actual
            actual = actual.next

        return None

    def filtrar_por_clase(self, clase):
        """Retorna una list con los pasajeros de esa clase ("Ejecutiva" o
        "Económica"), en el mismo orden de la lista."""
        resultado = []
        actual = self.head
        while actual is not None:
            if actual.data.clase() == clase:
                resultado.append(actual.data)
            actual = actual.next
        return resultado
