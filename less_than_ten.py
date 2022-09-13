def less_than_ten(products):
  product_less_than_ten = {}

  for inventory_row in range(2, products.max_row + 1):
    inventory = products.cell(inventory_row, 2).value

    if inventory < 10:
      product_less_than_ten[int(products.cell(inventory_row, 1).value)] = int(inventory)

  print(product_less_than_ten)
