#Crie uma função que recebe uma lista de números e devolve, nesta ordem, o mínimo, a média, o desvio padrão e o máximo

import numpy #importando a biblioteca (alguns comandos só funcionam com ela)

def comandos():                         #inicia a elaboração da função
  
    i = int(input("Digite o primeiro número da lista: ")) #início da lista
    
    f = int(input("Digite o último número da lista: ")) #fim da lista
    
    lista = list(range(i, (f+1)))  #declara uma lista com range de do início ao fim (lembra: um a menos, por isso que coloquei +1
    
    print(f"o mínimo da lista é {min(lista)}")
    
    print(f"a média da lista é {sum(lista)/len(lista)}") #a média é a soma da lista dividido pela sua quantidade
    
    print(f"o desvio padrão da lista é {numpy.std(lista)}") #tive que importar a biblioteca numpy para esse comando funcionar
    
    print (f"o máximo da lista é {max(lista)}")
    
    return (lista)
    
comandos() #executando a função
