class Room: 
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee 
        self.play_list = []
        self.guests_in_room = []
        self.room_balance = 0.00
    
    def add_guest_to_room(self, guest):
        self.guests_in_room.append(guest)

    def check_guest_can_pay(self, guest):
        can_pay = True 
        if guest.wallet < self.entry_fee:
            can_pay = false
        return can_pay

    def charge_guest_entry_fee(self, guest):
        self.room_balance += self.entry_fee
        guest.wallet -= self.entry_fee
    
    def check_in_guest(self, guest):
        if self.capacity > 0 and self.check_guest_can_pay(guest) == True:
            self.charge_guest_entry_fee(guest)
            self.add_guest_to_room(guest)
            self.capacity -= 1

        return "Sorry, this room is full"

    def check_out_guest_by_name(self, guest_name):
        check_out = [self.guests_in_room.remove(guest) for guest in self.guests_in_room if guest.name == guest_name]
        return check_out
        
    def add_song_to_play_list(self, song):
        self.play_list.append(song)      

