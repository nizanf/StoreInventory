from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
   
    name: str
    category: str
    description: str
    stock: int

    class Config:
        schema_extra = {
            "example": {
                "name": "apple",
                "category": "fruit",
                "description": "pink lady",
                "stock": 5,
            }
        }
# class CreateItemSchema(BaseModel):
 
#     name: str
#     category: str
#     description: str
#     stock: int
    

# class UpdateItemSchema(BaseModel):

#     name: Union[str, None]
#     category: Union[str, None]
#     description: Union[str, None]
#     stock: Union[int, None]
