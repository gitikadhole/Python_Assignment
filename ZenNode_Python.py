import math
# Catalog of products
products = {'Product A': 20, 'Product B': 40, 'Product C': 50}

quantities = {}
total_items = 0
for product, price in products.items():
  quantity = int(input(f"Enter the quantity of {product}: "))
  gift_wrap = input(
      f"Do you want to wrap {quantity} units of {product} as a gift? (yes/no): "
  ).lower() == 'yes'
  quantities[product] = {'quantity': quantity, 'gift_wrap': gift_wrap}
  total_items += quantity

cart_total = 0
shipping_price = math.ceil(total_items / 10) * 5

for product, details in quantities.items():
  price_per_unit = products[product]
  quantity = details['quantity']
  total_cost = quantity * price_per_unit
  cart_total += total_cost

total_before_discount = cart_total

discounted_value_1 = {'val': 0, 'name': 'flat_10_discount'}
discounted_value_2 = {'val': 0, 'name': 'bulk_10_discount'}
discounted_value_3 = {'val': 0, 'name': 'bulk_5_discount'}
discounted_value_4 = {'val': 0, 'name': 'tiered_50_discount'}

#flat_10_discount
if cart_total > 200:
  discounted_value_1['val'] = cart_total - 10
#bulk_10_discount
if total_items > 20:
  discounted_value_2['val'] = cart_total - (cart_total * 0.1)

#bulk_5_discount
for product, details in quantities.items():
  price_per_unit = products[product]
  quantity = details['quantity']
  total_cost = quantity * price_per_unit
  if quantity > 10:
    discount = 0.05 * total_cost
    discounted_value_3['val'] += total_cost - discount
  else:
    discounted_value_3['val'] += total_cost

#tiered_50_discount
for product, details in quantities.items():
  price_per_unit = products[product]
  quantity = details['quantity']
  if total_items > 30 and quantity > 15:
    discounted_units = quantity - 15
    discount = 0.5 * discounted_units * price_per_unit
    total_cost = (15 * price_per_unit) + (
        (quantity - 15) * price_per_unit - discount)
    discounted_value_4['val'] += total_cost
  else:
    total_cost = quantity * price_per_unit
    discounted_value_4['val'] += total_cost

discounted_values = [
    discounted_value_1, discounted_value_2, discounted_value_3,
    discounted_value_4
]

max_discount = min(discounted_values, key=lambda x: x['val'])

gift_wrap_fee = sum(details['quantity'] for details in quantities.values()
                    if details['gift_wrap']) * 1

final_total = 0

for name, details in quantities.items():
  print("Product: ", name)
  print("Quantity:  ", details['quantity'])
  print("Total: ", details['quantity'] * products[name], "\n")
  final_total += details['quantity'] * products[name]

print("\nTotal before disount: ", final_total, "\n")
print("Subtotal: ", max_discount['val'], "\n")
print(
    "Discount Name :",
    max_discount['name'],
    "\n",
)
print("Discount Amount: ", total_before_discount - max_discount['val'], "\n")
print("Shipping Fee: ", shipping_price, "\n")
print("Gift Wrap Fee: ", gift_wrap_fee, "\n")
print("Total: ", max_discount['val'] + shipping_price + gift_wrap_fee, "\n")
