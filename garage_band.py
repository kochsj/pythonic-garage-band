class Band:

    list_of_bands = []
    def __init__(self, name, members=[]):
        self.name = name
        self.member_list = members
        Band.list_of_bands.append(name)

    def __repr__(self):
        return 'The band, ' + self.name + '.'

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

    @classmethod
    def create_from_data(cls, data):


a = Band('Nirvana', ['Kurt', 'David'])
print(a)
print(Band.get_all_bands())




# - [x] A Band instance should have a name attribute which is a string.
# - [x] A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
# - [x] A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
# - [x] A Band instance should have appropriate __str__ and __repr__ methods.
# - [x] A Band should have a class method to_list which returns a list of previously created Band instances
# A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance. The Band instance should have its members be set to musicians based on info from the input.


# class Musician:
