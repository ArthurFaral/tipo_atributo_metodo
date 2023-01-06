## Os atributps de uma classe que podem ser do tipo
# prvado protect ou publico


# os atributos publicos estao acessiveis para todos os objetos (Abstração)

# os atributos privados podem ser instanciados, porem os valores
# nao serao acessiveis para os objetos (Emcapsulamento)


## Os atributos publicos são escritos de forma normal. 
# Exemplo: self.nome = nome

## Os atributos do tipo privado possuem 2 underlines(dunder) na construção
# Exemplo: self.__nome = nome


class cadastrouser():
    def __init__(self,usuario,senha):
       self.usuario = usuario ## Abstraindo
       self.__senha = senha ## Encapsulado
       




