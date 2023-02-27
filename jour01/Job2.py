class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation = Operation()
print("Le nombre1 est {}".format(operation.nombre1))
print("Le nombre2 est {}".format(operation.nombre2))