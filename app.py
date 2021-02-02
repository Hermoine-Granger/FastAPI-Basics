from fastapi import FastAPI

app=FastAPI()
database=[
{"ID":1,
"Name":"Bread"
},
{
"ID":2,
"Name":"Fruits"
}
]

@app.get("/")
async def root() -> dict:
    return{"Message":"Hello"}
    
''' Implementing CRUD 

Create
Read
Update
Delete

'''

#GET
@app.get("/shopping_list")
async def get_shopping_list() -> dict:
    return{"Data":database}
    
#POST
@app.post("/shopping_list")
async def add_shopping_list(item:dict) -> dict:
    database.append(item)
    return{"Message":"Item added successfully"}
    
#PUT
@app.put("/shopping_list/{id}")
async def update_shopping_list(id:int,detail:dict) -> dict:
    for item in database:
        if item["ID"]==id:
            item["Name"]=detail["Name"]
            return {"Update":"Shopping list for the id {} has been updated".format(id)}
    return {"Message":"Item for the id {} was not found !".format(id)}
            
            
#DELETE
@app.delete("/shopping_list/{id}")
async def update_shopping_list(id:int) -> dict:
    for item in database:
        if item["ID"]==id:
            database.remove(item)
            return {"Message":"Item for the id {} has been deleted".format(id)}
    return {"Message":"Item for the id {} was not found !".format(id)}