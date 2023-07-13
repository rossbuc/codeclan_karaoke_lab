class Guest: 
    def __init__(self, name, fav_song, money):
        self.name = name
        self.fav_song = fav_song
        self.money = money

    def pay_entry(self, fee):
        self.money -= fee

    def fav_song_in_playlist(self, room):
        for song in room.playlist:
            if song.name == self.fav_song.name:
                return "Wooh! They have my favourite song"