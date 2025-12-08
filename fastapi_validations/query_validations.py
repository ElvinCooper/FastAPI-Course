from fastapi import FastAPI, Query
from typing import Annotated

# Validaciones con Strings:
# max_length
# min_length
# pattern

# Validaciones con Numeros (enteros y float)
# gt greather than
# ge greather than or equal
# lt less than
# le less than or equal

#------- validaciones con MATADATA -----------------#
# title
# description
# alias
# deprecated

app = FastAPI()



#@app.get('/items')
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
# 	results: dict = {"message": "Acesso a get(read_items)"}
# 	if q:
# 		results.update({"q": q})
#     return results		

# async def read_items(q: Annotated[int | None, Query(min_length=8)] = None):
# 	results: dict = {"message": "Acesso a get(read_items)"}
# 	if q:
# 		results.update({"q": q})
#     return results		

# @app.get('/items')
# async def read_items(q: Annotated[list[str] | None, Query(gt=3)] = None):
# 	results: dict = {"message": "Acesso a get(read_items)"}
# 	if q:
# 		results.update({"q": q})
# 	return results    		

@app.get('/items')
async def read_items(q: Annotated [int | None, Query(gt=4, 
                                                     title="Query",
                                                     description="what_you_gonna_look", 
                                                     alias="busqueda-item",
                                                     deprecated="True")
                                   ] = None):
	results: dict = {"message": "Acesso a get(read_items)",
                     "q": q}
	if q:
		results.update({"q": q})
	return results  
