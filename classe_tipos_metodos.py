import datetime
import random

## Os tipos de metodos de classe são:

# @classmethod
# @staticmethod
# @Private Method


## Vamos aplicar os tipos de métodos

class livro():
    #atributo de classe

    anos_atual = datetime.date.today().year
    
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    ## Metodo de instancia ou objeto
    def imprime(self):
        print("Esse livro é %s e o autor %s e o ano %s"%(self.titulo,self.autor,self.ano))



    def anopublicacao(self):
        print("Tempo de publicação",self.anos_atual - self.ano, 'anos')



## Metodo de classe utiliza o decorador @classmethod

    @classmethod
    def calculoanopublicacao(vclasse,nome,ano):
        calcula = vclasse.anos_atual - ano
        return (nome,"Tempo Publicação", str(calcula),'anos')


## Para criar um método oculto basta utilizar o duplo underline

    def __autor(self):
        return(self.autor)


## Metodo do tipo estatico, utilizado com o decorador @staticmethod

    @staticmethod
    def geraisbn():
        isbn = random.randint(0,100)
        return isbn