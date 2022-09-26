from fastapi.encoders import jsonable_encoder


async def create_product(products_collection, product):
    data = jsonable_encoder(product)
    try:
        product = await products_collection.insert_one(data)

        if product.inserted_id:
            product = await get_product(products_collection, product.inserted_id)
            return product

    except Exception as e:
        print(f'create_product.error: {e}')

async def get_product(products_collection, product_id):
    try:
        data = await products_collection.find_one({'_id': product_id})
        if data:
            return data
    except Exception as e:
        print(f'get_product.error: {e}')

async def get_products(products_collection, skip, limit):
    try:
        product_cursor = products_collection.find().skip(int(skip)).limit(int(limit))
        products = await product_cursor.to_list(length=int(limit))
        return products

    except Exception as e:
        print(f'get_products.error: {e}')

async def update_product(products_collection, product_id, product_data):
    try:
        data = {k: v for k, v in product_data.items() if v is not None}

        product = await products_collection.update_one(
            {'_id': product_id},
            {'$set': data}
        )

        if product.modified_count:
            return True, product.modified_count

        return False, 0
    except Exception as e:
        print(f'update_product.error: {e}')

async def delete_product(products_collection, product_id):
    try:
        product = await products_collection.delete_one(
            {'_id': product_id}
        )
        if product.deleted_count:
            return {'status': 'product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')
