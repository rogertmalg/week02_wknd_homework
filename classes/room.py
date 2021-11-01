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
            can_pay = False
        return can_pay

    def charge_guest_entry_fee(self, guest):
        self.room_balance += self.entry_fee
        guest.wallet -= self.entry_fee
    
    def check_in_guest(self, guest):
        if self.check_guest_can_pay(guest) == False:
            return "You don't have enough money"
        
        elif self.capacity > 0:
            self.charge_guest_entry_fee(guest)
            self.add_guest_to_room(guest)
            self.capacity -= 1
 
        return "Sorry, this room is full"

    def check_out_guest_by_name(self, guest_name):
        [self.guests_in_room.remove(guest) for guest in self.guests_in_room 
        if guest.name == guest_name]
        
        
    def add_song_to_play_list(self, song):
        self.play_list.append(song)

    def remove_song_by_name(self, song_name):
        [self.play_list.remove(song) for song in self.play_list 
        if song.name == song_name]      
        

    def remove_song_by_singer(self, singer_name):
        [self.play_list.remove(song) for song in self.play_list[::1] 
        if song.singer == singer_name]

    def fave_song_cheer(self, guest):
        cheer = "Whoooo"
        for song in self.play_list:
            if guest.favourite_song == song.name:
                return cheer
                

        
    