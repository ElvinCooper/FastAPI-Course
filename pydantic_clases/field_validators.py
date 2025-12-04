from typing import Annotated  # Annotted = ayuda a colocar metadatos
from pydantic import AfterValidator, BaseModel


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

NumeroPar = Annotated[int, AfterValidator(es_par)]

class Model1(BaseModel):
    numero1 : NumeroPar

example : Model1 = Model1(numero1=5)    
# class Model2(BaseModel):
#     pass
# class Model3(BaseModel):
#     pass
    


 



