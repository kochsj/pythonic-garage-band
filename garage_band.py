class Musician:

    list_of_artists = []

    def __init__(self, band_name, artist_name, instrument):
        self.name = artist_name
        self.band = band_name
        self.instrument = instrument
        Musician.list_of_artists.append([artist_name, band_name, instrument])

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"I, {self.name}, am a musician in {self.band}!"

    def get_instrument(self):
        return f"{self.name} would love get their {self.instrument} and play."

    def play_solo(self):
        return f"{self.name} finds their {self.instrument} and breaks out into a solo!"


class Guitarist(Musician):
    def __init__(self, artist_name, band_name):
        super().__init__(band_name, artist_name, 'guitar')

class Bassist(Musician):
    def __init__(self, artist_name, band_name):
        super().__init__(band_name, artist_name, 'bass')

class Drummer(Musician):
    def __init__(self, artist_name, band_name):
        super().__init__(band_name, artist_name, 'drums')

class Singer(Musician):
    def __init__(self, artist_name, band_name):
        super().__init__(band_name, artist_name, 'vocals')

class Band:

    list_of_bands = []

    # The Band instance should have its members be set to musicians based on info from the input.
    def __init__(self, band_name, members=[]):
        self.name = band_name
        self.member_list = members
        Band.list_of_bands.append([band_name, members])

    def __repr__(self):
        return f"The band, {self.name}."

    def __str__(self):
        return f"We are the World's greatest band, {self.name}!"

    def play_solos(self):
        string = ''
        for member in self.member_list:
            string += f"And now... {member} breaks out into a solo! "
        return string

    @classmethod
    def to_list(cls):
        return cls.list_of_bands

    @staticmethod
    def create_from_data(data):
        artists = data[1]
        for i in range(len(data[1])):
            if artists[i][0].lower() == 'bassist':
                Bassist(artists[i][1], data[0])
            elif artists[i][0].lower() == 'guitarist':
                Guitarist(artists[i][1], data[0])
            elif artists[i][0].lower() == 'drummer':
                Drummer(artists[i][1], data[0])
            else:
                Singer(artists[i][1], data[0])

        return Band(data[0], data[1])

# - [x] A Band instance should have a name attribute which is a string.
# - [x] A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
# - [x] A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
# - [x] A Band instance should have appropriate __str__ and __repr__ methods.
# - [x] A Band should have a class method to_list which returns a list of previously created Band instances

# - [x] A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance.
#
# - [x] The Band instance should have its members be set to musicians based on info from the input.

# Musician Subclass Tests
# - [x] Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
# - [x] Each kind of Musician instance should have a get_instrument method that returns string.
# - [x] Each kind of Musician instance should have a play_solo method that returns string.


