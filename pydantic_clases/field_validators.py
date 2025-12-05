from typing import Annotated  # Annotted = ayuda a colocar metadatos
from pydantic import AfterValidator, BaseModel, field_validator


#x: Annotated[int, "numero positivo", "id del usuario"]

#---------- Tipos de field validator de pydantic ----------#
# After  :se ejecuta despues de las validaciones de pydantic
# Before :se ejecuta antes de las validaciones de pydantic
# Plain : igual al before pero terminan la validacion al retornar el valor.
# Wrap : Se pueden ejecutar antes o despues de las validaciones de pydantic

def es_par(value: int) -> int:
    if value % 2 == 1:
        raise ValueError(f"{value} no es numero par")
    return value

#NumeroPar = Annotated[int, AfterValidator(es_par)]

# class Model1(BaseModel):
#     numero1 : NumeroPar

# example : Model1 = Model1(numero1=5)    
# class Model2(BaseModel):
#     pass
# class Model3(BaseModel):
#     pass
        
        
        
        
#------------ Validacion con Decorator ---------------------------#    
class Item(BaseModel):
    item_id: int
    price : float
    
    @field_validator("item_id", "price")
    def check_positive(cls, value : int | float) -> int:
        if value < 0:
            raise ValueError("EL item debe ser un numero positivo")
        return value
    
guineos : Item = Item(item_id=2, price=3.5)     
    


 



