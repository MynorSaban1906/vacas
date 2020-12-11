

class Data():
    
    def CargarArchivo(pathCSV):
        archivo=open(pathCSV,"r")
        for linea in archivo.readlines():
            print (linea)

        archivo.close()


    

    