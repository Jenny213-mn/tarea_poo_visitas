class VisitaServicio:
    def __init__(self):
        self._visitantes = []

    def registrar(self, visitante):
        # Evitar duplicados por cédula
        for v in self._visitantes:
            if v.cedula == visitante.cedula:
                return False
        self._visitantes.append(visitante)
        return True

    def obtener_todos(self):
        return self._visitantes

    def eliminar(self, cedula):
        for v in self._visitantes:
            if v.cedula == cedula:
                self._visitantes.remove(v)
                return True
        return False