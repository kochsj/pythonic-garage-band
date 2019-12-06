def format_data_for_bands(data):
    data_list = data.split(',\n')
    list_of_artists_and_their_instrument = []
    formatted_data = [data_list[0]]
    for i in range(1, len(data_list)):
        inst_artist = data_list[i].split(': ')
        artist = [inst_artist[1], inst_artist[0]]
        list_of_artists_and_their_instrument.append(artist)
    formatted_data.append(list_of_artists_and_their_instrument)
    return formatted_data

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
        member_names = []
        for i in range(len(members)):
            member_names.append(members[i])
        self.member_list = member_names
        Band.list_of_bands.append([band_name, members])

    def __repr__(self):
        return f"The band, {self.name}."

    def __str__(self):
        return f"We are the World's greatest band, {self.name}!"

    def play_solos(self):
        string = ''
        for member in self.member_list:
            string += f"And now... {member[0]} breaks out into a solo! "
        return string

    @classmethod
    def to_list(cls):
        return cls.list_of_bands

    @staticmethod
    def create_from_data(band_info_data):
        data = format_data_for_bands(band_info_data)
        artists = data[1]
        for i in range(1, len(data[1])):
            if artists[i][1].lower() == 'bassist':
                Bassist(artists[i][0], data[0])
            elif artists[i][1].lower() == 'guitarist':
                Guitarist(artists[i][0], data[0])
            elif artists[i][1].lower() == 'drummer':
                Drummer(artists[i][0], data[0])
            else:
                Singer(artists[i][0], data[0])

        return Band(data[0], data[1])

