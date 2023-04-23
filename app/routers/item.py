from typing import List
from fastapi import Body, HTTPException, status, APIRouter
from app.models.item import *
from app.database import ItemCol
from app.models.itemSerializer import itemEntity, itemListEntity
from typing_extensions import Annotated
from fastapi.encoders import jsonable_encoder
router = APIRouter()


@router.get("/get_all_items")
def get_all_items():
    """
    get all items Inventory in collection
    """
    item_list = []

    for item in ItemCol.find():
        item_list.append(item)
        
    return  itemListEntity(item_list)


@router.get('/{name}')
def get_item(name):
    """
    get item by name
    """
    try:
        for item in ItemCol.find({"name" : name}):
            return itemEntity(item)
    except: 
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)

@router.post('/create_item', status_code=status.HTTP_201_CREATED)
def create_item(item: Annotated[
                Item,
                    Body(
                        example={
                            "name": "apple",
                            "category": "fruit",
                            "description": "pink lady",
                            "stock": 5,
                        },
                    ),
                ],):
   
    json_item = jsonable_encoder(item)
    try:
        ItemCol.insert_one(jsonable_encoder(json_item))  
        results = {"item": json_item}
    except: 
        raise HTTPException(status_code= status.HTTP_409_CONFLICT)
    
    return results


@router.put('/{name}')
def update_item_Inventory(name: str, stock: int):
    """
    update item stock
    """
    ItemCol.update_one({"name" : name},{"$set":{"stock":stock}})
    return "update successfuly" 


@router.delete('/{name}')
def delete_item(name):
    ItemCol.delete_one({"name" : name})

    return "deleted successfuly"