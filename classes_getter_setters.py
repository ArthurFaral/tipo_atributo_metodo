## Utilizando os metodos decoradores @ property(getter)
# e o @.setter utilizando boas praticas de abstração de atributos
# utilizamos o getters, para sobrescrever um metodo sem 
# impactar nos objetos
# instanciados préviamente  utilizamos o setter.
## Para utilizar um setter, é necessario utilizar o getter no 
# atributo da classe


## Podemos deixar um atributo privado como publico com o
#  @property usando getters

class VendaProdutos():
    def __init__(self,produto,quantidade,valor):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor = valor


    ## Aplicando Getter no atributo __produto para abstrair o metodo
    # utilizando getters

    @property #Função decoradora para aplicar o getter

    def produto(self):
        return self.__produto


## Vamos fazer um getter do atributo quantidade para apos 
# fazer um setter da quantidade

    @property

    def quantidade(self):
        return self.__quantidade


## Criando setter para aplicar a funcionalidade de 
# alterar a quantidade

    @quantidade.setter
    def quantidade(self,nova_quantidade):
        self.__quantidade = nova_quantidade

    
## Criando um metodo atraves do getter, manipulando valores
#dos atributos

    @property
    def valor_total_compras(self):
        return self.__quantidade * self.__valor