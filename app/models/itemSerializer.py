def itemEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "category": item["category"],
        "description": item["description"],
        "stock": item["stock"],
    }


def itemResponseEntity(item) -> dict:
    return {
        "name": item["name"],
        "stock": item["stock"],
    }



def itemListEntity(items) -> list:
    return [itemResponseEntity(item) for item in items]

