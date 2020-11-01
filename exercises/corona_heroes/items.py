import json

ITEMS = {
    1: {
        'name': 'Apple'
    },

    2: {
        'name': 'Stone'
    }
}

class Item():

    def __init__(self, item_id, name):
        self.id = item_id
        self.name = name

    def __str__(self):
        return self.name
