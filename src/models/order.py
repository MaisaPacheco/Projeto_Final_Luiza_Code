from datetime import datetime

from src.models.address import get_one_address
from src.models.user import get_user


async def get_cart(order_collection, user_id):
    try:
        cart = await order_collection.find_one({"$and": [{'user._id': user_id}, {'paid': False}]})
        return cart
    except Exception as e:
        print(f'get_cart.error: {e}')
        
async def get_cart_by_id(order_collection, cart_id):
    try:
        cart = await order_collection.find_one({"$and": [{'_id': cart_id}, {'paid': False}]})
        return cart
    except Exception as e:
        print(f'get_cart.error: {e}')


async def create_cart(order_collection, users_collection, address_collection, user_id):
    try:  
        user = await get_user(users_collection, user_id)
        
        if (not user):
            return {"error": "user not found"}
        
        cart = await get_cart(order_collection, user_id)
        if (not cart): 
            address = await get_one_address(address_collection, user_id)
            if address == "FALHA":
                return {"error": "user address not found"}
            cart_data = {
                "user": user,
                "price": 0,
                "address": address,
                "paid": False,
                "create": datetime.now(),
                "authority": ""
                
            }
            cart = await order_collection.insert_one(cart_data)
            
            if cart.inserted_id:
                cart = await get_cart(order_collection, user_id)
                return cart
               
    except Exception as e:
        print(f'get_cart.error: {e}') 
        

async def delete_cart(orders_collection, cart_id):
        try: 
            cart = await orders_collection.delete_one(
                {'_id': cart_id}
            )
            
            if cart.deleted_count:
                return {'status': 'Order deleted'}
        except Exception as e:
            print(f"delete_order.error {e}")
            
async def update_order_price(orders_collection, cart, product_price):
    try:
        cart_total_price = {"price": cart["price"] + product_price}
        
        cart = await orders_collection.update_one(
            {'_id': cart["_id"]},
            {'$set': cart_total_price}
        )
        if cart.modified_count:
            return True, cart.modified_count

        return False, 0
    except Exception as e:
        print(f'update_user.error: {e}')
    
    return cart