import json


# TUPLA de campos: son datos fijos del estudiante.
# Se utiliza desde el Controlador y la Vista.
CAMPOS_ESTUDIANTE = ("nombre", "apellido", "email", "carnet")


class Estudiante:
    """MODELO: representa a un estudiante."""

    def __init__(
        self,
        id_estudiante,
        nombre,
        apellido,
        email,
        carnet,
        notas=None,
        materias=None
    ):
        self.id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet

        # DICCIONARIO DE LISTAS:
        # Ejemplo:
        # {"Matemática": [18, 19], "Inglés": [17]}
        self.notas = notas if notas else {}

        # SET:
        # materias inscritas, sin repetirse.
        self.materias = set(materias) if materias else set()

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def inscribir_materia(self, materia):
        # add() evita duplicar la materia.
        self.materias.add(materia)

    def agregar_nota(self, materia, nota):
        # Primero inscribimos la materia.
        self.inscribir_materia(materia)

        # Después agregamos la nota a la lista.
        self.notas.setdefault(materia, []).append(nota)

    def obtener_promedio(self):
        todas = []

        for lista_notas in self.notas.values():
            todas.extend(lista_notas)

        if not todas:
            return 0

        return round(sum(todas) / len(todas), 2)

    def materias_en_comun(self, otro_estudiante):
        # INTERSECCIÓN de conjuntos.
        # Devuelve las materias que ambos comparten.
        return self.materias & otro_estudiante.materias

    def a_diccionario(self):
        """
        Convierte el objeto Estudiante en un diccionario
        para poder guardarlo en JSON.
        """

        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carnet": self.carnet,
            "notas": self.notas,

            # JSON no puede guardar directamente un SET.
            # Lo convertimos a una lista.
            "materias": sorted(self.materias),
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """
        Convierte un diccionario leído desde JSON
        nuevamente en un objeto Estudiante.
        """

        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["carnet"],
            notas=datos.get("notas", {}),

            # LISTA -> SET
            materias=set(datos.get("materias", [])),
        )

    def __str__(self):
        return (
            f"[{self.carnet}] "
            f"{self.obtener_nombre_completo()} "
            f"- Promedio: {self.obtener_promedio()}"
        )