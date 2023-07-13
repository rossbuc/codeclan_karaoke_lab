class Room:
    
    def __init__(self, name, capacity, entry_fee, playlist):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.playlist = playlist
        self.guests_in_room = []

    def check_in_guest(self, guest):
        self.guests_in_room.append(guest)