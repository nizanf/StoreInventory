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
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)


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
   
    try:
        # json_item = jsonable_encoder(item)
        ItemCol.insert_one(jsonable_encoder(item))  
        results = {"item": jsonable_encoder(item)}
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


@router.delete('/delete_all')
def delete_all():
    try:
        ItemCol.delete_many({ })
        print(str(get_all_items))
        if not get_all_items:
            return "bad"
        return "ok"
    except: 
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST) 
    

@router.delete('/{name}')
def delete_item(name):
    ItemCol.delete_one({"name" : name})

    return "deleted successfuly"


