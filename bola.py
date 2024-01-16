# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola():
    def __init__(self, cor, circuf, material):
        self.cor = cor
        self.circunf = circuf
        self.material = material
        
    def trocaCor(self, novacor) :
                
        self.cor=novacor 
       
    
    def mostraCor(self):
       return (print(self.cor))
       
       
bola1 = Bola("Azul", 6, "couro")    
bola1.mostraCor()
#bola1.trocaCor("vermelho")
#bola1.mostraCor()    

    
   