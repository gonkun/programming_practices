def displayInventory(inventory):
    print('Inventory:')
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        total_items = total_items + v

    print('Total number of items: ' + str(total_items))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        num_item = inventory.get(i, 0)
        inventory[i] = num_item + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
