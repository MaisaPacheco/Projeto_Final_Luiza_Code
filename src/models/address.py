from src.models.user import get_user


async def create_address(address_collection, users_collection, user_id, new_address = []):
    try:
        user = await get_user(users_collection, user_id)
        if (not user):
            return 
       
            
        AddressSchema = await get_address_by_user(address_collection, user_id) 
        list_of_add = []   
        
        
        if (not AddressSchema):
            AddressSchema = await address_collection.insert_one({
                "user": user,
                "address": new_address
            })
            list_of_add = new_address
        
        else:
            for new_ad in new_address:
             if new_ad not in AddressSchema["address"]:
                    list_of_add.append(new_ad)
                    AddressSchema["address"].append(new_ad)
                    
            if list_of_add != []: 
                address_collection.update_one(
                {'_id': AddressSchema["_id"]},
                {'$set': {
                    "address": AddressSchema["address"]
                }}
            )
               
        return list_of_add
                         
    except Exception as e:
        print(f'create_user.error: {e}')
        
async def get_address_by_user(address_collection, user_id):
    try:
        data = await address_collection.find_one({'user._id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_user.error: {e}')
        
async def get_one_address(address_collection, user_id):
    find_address = await get_address_by_user(address_collection, user_id)
    
    if find_address:
        for add in find_address["address"]:
            if add["is_delivery"]:
                return add
    return "FALHA"  

# async def delete_address(address_collection):
#     try:
#         address = address_collection.delete_one(
#             {'_id': address["_id"]}
#         )
#         if address.deleted_count:
#             return {'status': 'Address deleted'}
#     except Exception as e:
#         return f'delete_address.error: {e}'
    
    
    