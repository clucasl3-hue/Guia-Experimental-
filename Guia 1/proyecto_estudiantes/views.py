from models import Estudiante, CAMPOS_ESTUDIANTE
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido


# Gestor encargado de leer y guardar estudiantes.
gestor = GestorJSON("data/estudiantes.json")


# TUPLAS: campos que no cambian durante la ejecución.
CAMPOS_OBLIGATORIOS = (
    "nombre",
    "apellido",
    "email",
    "carnet"
)

CAMPOS_BUSCABLES = (
    "nombre",
    "apellido",
    "email",
    "carnet"
)


# ============================================================
# AYUDAS INTERNAS
# ============================================================

def emails_registrados(excepto_id=None):
    """
    SET con los emails que ya están registrados.
    """

    return {
        registro["email"].lower()
        for registro in gestor.leer()
        if registro["id"] != excepto_id
    }


def carnets_registrados(excepto_id=None):
    """
    SET con los carnets que ya están registrados.

    Se utiliza para impedir carnets duplicados.
    """

    return {
        registro["carnet"].lower()
        for registro in gestor.leer()
        if registro["id"] != excepto_id
    }


def siguiente_id():
    """
    Obtiene el siguiente ID disponible.
    """

    ids = [
        registro["id"]
        for registro in gestor.leer()
    ]

    return max(ids) + 1 if ids else 1


# ============================================================
# C · CREATE
# ============================================================

def crear_estudiante(datos):
    """
    Crea un estudiante.

    Devuelve:
    (True, mensaje)
    o
    (False, mensaje)
    """

    try:

        # Normalizamos los datos.
        valores = {
            campo: str(
                datos.get(campo, "")
            ).strip()

            for campo in CAMPOS_ESTUDIANTE
        }

        # Comprobamos campos obligatorios.
        faltantes = [
            campo
            for campo in CAMPOS_OBLIGATORIOS
            if not valores[campo]
        ]

        if faltantes:

            return (
                False,
                "Faltan campos obligatorios: "
                + ", ".join(faltantes)
            )

        # Validamos email.
        if not es_email_valido(
            valores["email"]
        ):

            return (
                False,
                f"El email '{valores['email']}' "
                "no tiene un formato válido"
            )

        # Validamos email duplicado.
        if (
            valores["email"].lower()
            in emails_registrados()
        ):

            return (
                False,
                "Ese email ya está registrado"
            )

        # Validamos carnet duplicado.
        if (
            valores["carnet"].lower()
            in carnets_registrados()
        ):

            return (
                False,
                "Ese carnet ya está registrado"
            )

        # Creamos el objeto.
        estudiante = Estudiante(
            siguiente_id(),
            **valores
        )

        # Leemos la lista actual.
        registros = gestor.leer()

        # Agregamos el estudiante.
        registros.append(
            estudiante.a_diccionario()
        )

        # Guardamos.
        if not gestor.guardar(registros):

            return (
                False,
                "No se pudo escribir el archivo"
            )

        return (
            True,
            f"Estudiante "
            f"{estudiante.obtener_nombre_completo()} "
            f"creado con id {estudiante.id}"
        )

    except Exception as error:

        return (
            False,
            f"Error inesperado: {error}"
        )


# ============================================================
# R · READ
# ============================================================

def obtener_todos():
    """
    Devuelve una LISTA de objetos Estudiante.
    """

    return [
        Estudiante.desde_diccionario(registro)

        for registro in gestor.leer()
    ]


def obtener_por_id(id_estudiante):
    """
    Busca un estudiante por su ID.
    """

    for estudiante in obtener_todos():

        if estudiante.id == id_estudiante:
            return estudiante

    return None


# ============================================================
# S · SEARCH
# ============================================================

def buscar_estudiantes(termino):
    """
    Busca estudiantes por nombre, apellido,
    email o carnet.
    """

    termino = termino.strip().lower()

    if not termino:
        return []

    encontrados = []

    for registro in gestor.leer():

        for campo in CAMPOS_BUSCABLES:

            if termino in str(
                registro.get(campo, "")
            ).lower():

                encontrados.append(
                    Estudiante.desde_diccionario(
                        registro
                    )
                )

                break

    return encontrados


# ============================================================
# U · UPDATE
# ============================================================

def actualizar_estudiante(
    id_estudiante,
    cambios
):
    """
    Actualiza los campos enviados.
    """

    try:

        # DIFERENCIA DE CONJUNTOS:
        # detectamos campos desconocidos.
        desconocidos = (
            set(cambios)
            - set(CAMPOS_ESTUDIANTE)
        )

        if desconocidos:

            return (
                False,
                "Campos no válidos: "
                + ", ".join(
                    sorted(desconocidos)
                )
            )

        if not cambios:

            return (
                False,
                "No se indicó ningún cambio"
            )

        # Si cambia el email, lo validamos.
        if "email" in cambios:

            if not es_email_valido(
                cambios["email"]
            ):

                return (
                    False,
                    "El email no tiene "
                    "un formato válido"
                )

            if (
                cambios["email"].lower()
                in emails_registrados(
                    excepto_id=id_estudiante
                )
            ):

                return (
                    False,
                    "Ese email ya lo usa "
                    "otro estudiante"
                )

        # Si cambia el carnet, lo validamos.
        if "carnet" in cambios:

            if not cambios["carnet"].strip():

                return (
                    False,
                    "El carnet no puede estar vacío"
                )

            if (
                cambios["carnet"].lower()
                in carnets_registrados(
                    excepto_id=id_estudiante
                )
            ):

                return (
                    False,
                    "Ese carnet ya lo usa "
                    "otro estudiante"
                )

        registros = gestor.leer()

        posicion = None

        for indice, registro in enumerate(
            registros
        ):

            if registro["id"] == id_estudiante:

                posicion = indice
                break

        # ID inexistente.
        if posicion is None:

            return (
                False,
                f"No existe un estudiante "
                f"con id {id_estudiante}"
            )

        # Actualizamos.
        registros[posicion].update(
            cambios
        )

        # Guardamos.
        if not gestor.guardar(registros):

            return (
                False,
                "No se pudo guardar el archivo"
            )

        return (
            True,
            f"Estudiante {id_estudiante} "
            f"actualizado "
            f"({len(cambios)} campo/s)"
        )

    except Exception as error:

        return (
            False,
            f"Error inesperado: {error}"
        )


# ============================================================
# D · DELETE
# ============================================================

def eliminar_estudiante(id_estudiante):
    """
    Elimina un estudiante por ID.
    """

    registros = gestor.leer()

    # Creamos una lista nueva sin el estudiante.
    quedan = [
        registro
        for registro in registros
        if registro["id"] != id_estudiante
    ]

    # Si tienen el mismo tamaño,
    # no se encontró el ID.
    if len(quedan) == len(registros):

        return (
            False,
            f"No existe un estudiante "
            f"con id {id_estudiante}"
        )

    if not gestor.guardar(quedan):

        return (
            False,
            "No se pudo guardar el archivo"
        )

    return (
        True,
        f"Estudiante {id_estudiante} eliminado"
    )


# ============================================================
# EXTRA · AGREGAR NOTA
# ============================================================

def agregar_nota(
    id_estudiante,
    materia,
    nota
):
    """
    Agrega una nota a un estudiante.

    La nota debe estar entre 0 y 20.
    """

    estudiante = obtener_por_id(
        id_estudiante
    )

    # Validación de ID.
    if not estudiante:

        return (
            False,
            f"No existe un estudiante "
            f"con id {id_estudiante}"
        )

    materia = materia.strip()

    if not materia:

        return (
            False,
            "La materia no puede estar vacía"
        )

    # Convertimos la nota.
    try:

        nota = float(nota)

    except (ValueError, TypeError):

        return (
            False,
            "La nota debe ser un número"
        )

    # VALIDACIÓN: 0 a 20.
    if nota < 0 or nota > 20:

        return (
            False,
            "La nota debe ser un número "
            "entre 0 y 20"
        )

    # Si es entero, guardamos entero.
    if nota.is_integer():
        nota = int(nota)

    # Agregamos la nota al objeto.
    estudiante.agregar_nota(
        materia,
        nota
    )

    registros = gestor.leer()

    for indice, registro in enumerate(
        registros
    ):

        if registro["id"] == id_estudiante:

            registros[indice] = (
                estudiante.a_diccionario()
            )

            break

    if not gestor.guardar(registros):

        return (
            False,
            "No se pudo guardar la nota"
        )

    return (
        True,
        f"Nota {nota} agregada en {materia}"
    )


# ============================================================
# EXTRA · VER PROMEDIO
# ============================================================

def obtener_promedio(id_estudiante):

    estudiante = obtener_por_id(
        id_estudiante
    )

    if not estudiante:

        return (
            False,
            f"No existe un estudiante "
            f"con id {id_estudiante}"
        )

    return (
        True,
        estudiante.obtener_promedio()
    )


# ============================================================
# EXTRA · MATERIAS OFERTADAS
# ============================================================

def materias_ofertadas():
    """
    Devuelve un SET con todas las materias
    de todos los estudiantes.
    """

    materias = set()

    for estudiante in obtener_todos():

        # UNIÓN DE CONJUNTOS.
        materias |= estudiante.materias

    return materias


# ============================================================
# EXTRA · ESTUDIANTES EN COMÚN
# ============================================================

def estudiantes_en_comun(
    id_a,
    id_b
):
    """
    Devuelve las materias que comparten
    dos estudiantes.
    """

    estudiante_a = obtener_por_id(id_a)
    estudiante_b = obtener_por_id(id_b)

    if not estudiante_a:

        return (
            False,
            f"No existe un estudiante "
            f"con id {id_a}"
        )

    if not estudiante_b:

        return (
            False,
            f"No existe un estudiante "
            f"con id {id_b}"
        )

    # INTERSECCIÓN DE CONJUNTOS.
    comunes = (
        estudiante_a.materias
        & estudiante_b.materias
    )

    return (
        True,
        comunes
    )