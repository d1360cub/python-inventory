def total_products(products):
  products_per_supplier = {}

  for inventory_row in range(2, products.max_row + 1):
    supplier = products.cell(inventory_row, 4).value

    if supplier in products_per_supplier:
      products_per_supplier[supplier] = products_per_supplier[supplier] + 1
    else:
      products_per_supplier[supplier] = 1

  print(products_per_supplier)
