
def get_product(**datos):
    print(datos["id"], datos["name"], datos["desc"]) 
    #Para usar los parámetros nombrados abajo, hay que llamarlos 
    #como aparece en el print anterior


get_product(id="id", name="iphone", desc="Iphone12plus")#Cuando la función es Kwargs hay que indicarle
                    # obligatoriamente como se el argumento que es este caso es id