from shopping_cart import Product, ShoppingCart

pan: Product = Product("Pan", "Dechele", 1.00)
pizza: Product = Product("Pizza", "Carbonara", 1.99)


carrito: ShoppingCart = ShoppingCart()

carrito.add_product(pan)
carrito.add_product(pizza)
carrito.add_product(pizza)
carrito.remove_product(pizza)


for i in range(len(carrito.products)):
    print(carrito.products[i])

print(carrito.total_price())
