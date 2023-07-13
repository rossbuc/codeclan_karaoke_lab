class Room:
    
    def __init__(self, name, capacity, entry_fee, playlist):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.playlist = playlist
        self.guests_in_room = []
        self.till = 0

    def check_in_guest(self, guest_to_add):
        if len(self.guests_in_room) < self.capacity:
            self.guests_in_room.append(guest_to_add)
        else:
            return "Sorry! This room is at capacity"

    def check_out_guest(self, guest_to_remove):
        for guest in self.guests_in_room:
            if guest.name == guest_to_remove.name:
               self.guests_in_room.remove(guest) 

    def add_song_to_playlist(self, song_to_add):
        self.playlist.append(song_to_add)

    def charge_guest_entry(self, guest):
        guest.pay_entry(self.entry_fee)
        self.till += self.entry_fee