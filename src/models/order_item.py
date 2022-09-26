from src.models.order import get_cart_by_id, update_order_price


async def create_cart_item(order_collection, order_item_collection, cart_id, new_product):
    try:  
        cart = await get_cart_by_id(order_collection, cart_id)
        
        if (not cart):
            return {"error": "cart not found or it's already paided"}
        update_price = await update_order_price(order_collection, cart, new_product["price"])
        if (not update_price):
            return {"error": "the price has not been updated"}
       
        cart_item_data = {
            "order": cart,
            "product": new_product
        }
        cart_item = await order_item_collection.insert_one(cart_item_data)
        if cart_item.inserted_id:
            cart_item = await get_cart_item(order_item_collection, cart_item.inserted_id)
            return cart_item
    except Exception as e:
        return {"error": f"the cart_item has not been inserted {e}"}


async def get_cart_item(order_item_collection,  cart_item_id):
    try:
        # data = await order_item_collection.find_one()
        data = await order_item_collection.find_one({'_id': cart_item_id})
        if data:
            return data
    except Exception as e:
        print(f'get_cart.error: {e}')
