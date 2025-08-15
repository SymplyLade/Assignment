# Super Market Price List 
# Items in list
items = ["Phone", "Monitor", "Cake", "Chocolate"]
item1_price = float(input("Phone price: "))
item2_price = float(input("Monitor price: "))
item3_price = float(input("Cake price: "))
item4_price = float(input("Chocolate: "))

store_items = {
     items[0]: (f"#{item1_price}"),
     items[1]: (f"#{item2_price}"),
     items[2]: (f"#{item3_price}"),
     items[3]: (f"#{item3_price}") 
     }
print(f"Store Item and Prices are: {store_items}")

update_item = float(input(f"update {items[3]} price: #"))
store_items.update({items[3] : update_item})

print(f"Available items are : {store_items.keys()}")