import openpyxl
from total_products import total_products
from total_inventory import total_inventory
from less_than_ten import less_than_ten

inventory = openpyxl.load_workbook("inventory.xlsx")
products = inventory["Sheet1"]

total_products(products)
total_inventory(products)
less_than_ten(products)
inventory.save("inventory_modified.xlsx")
