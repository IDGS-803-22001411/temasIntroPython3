
class OperasBas:
    #declaracion de propiedades
    #Si queremos que la propiedad sea privado ponemos un _
    num1=0
    num2=0
    res=0
    #declaracion de constructor de la clase
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    #declaracion de metodos de la clase
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es:{}".format(self.res))

def main():
    obj=OperasBas(3,5)
    obj.suma()

if __name__=="__main__":
    main()