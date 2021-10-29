class Room: 
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee 
        self.play_list = []
        self.room_balance = 0.00
