player = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        total += v
        print(f'{v} {k}')
    print(f'Total number of items: {total}')


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addedItems):
    for i in dragonLoot:
        if i in player:
            player[i] += 1
        else:
            player.setdefault(i, 1)
