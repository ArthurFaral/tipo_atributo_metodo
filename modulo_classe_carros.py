
## Todos os atributos que estiverem dentro do metodo construtor __init__
# e tem o self/namespace são atributos de instancia/objeto

## Os atributos de classe são declarados fora do metodo construtor
# __init__ não tem self


class carros():

#Atributo de classe
    cor = "Branco"


    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo


    def resumocarro(self):
        print(f"Esse carro é {self.marca} e o modelo {self.modelo}")





