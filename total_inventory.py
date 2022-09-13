def total_inventory(products):
  total_per_supplier = {}

  for inventory_row in range(2, products.max_row + 1):
    supplier = products.cell(inventory_row, 4).value
    inventory = products.cell(inventory_row, 2).value
    price = products.cell(inventory_row, 3).value
    total_per_product = products.cell(inventory_row,5)
    total_per_product.value = inventory * price

    if supplier in total_per_supplier:
      total_per_supplier[supplier] = total_per_supplier[supplier] + inventory * price
    else:
      total_per_supplier[supplier] = inventory * price

  print(total_per_supplier)
