# StoreInventory-
Store Inventory Management with FastAPI and MongoDB

    --for starting the app--
run: docker-compose up --build or uvicorn app.main:app --reload  

    --view WEB(UI)--
swagger ui:  http://127.0.0.1:8000/docs 
ReDoc: http://127.0.0.1:8000/redoc
tamplates: http://127.0.0.1:8000


pymongo - official driver python-mongo connection
mongoengine - (like sqlalchemy to mysql) odm for mongoDB

    --mongoDB container--
docker exec -it mongo /bin/bash
mongosh mongo
in docker mongo container- 
    use admin
    db.auth("root",passwordPrompt()) 
    #insert password
    use store_db
    show collections
        
    db.item.find()
    db.item.insert({field: "value"})