from garage_band import Band

def test_is_band():
    expected = True
    a = Band('Nirvana')
    actual = isinstance(a, Band)
    assert expected == actual

# A Band instance should have a name attribute which is a string.
def test_name_is_string():
    expected = True
    actual = isinstance((Band('Nirvana').name), str)
    assert expected == actual

def test_name_is_exact_string():
    expected = 'Soundgarden'
    actual = Band('Soundgarden').name
    assert expected == actual

# A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
def test_members_attribute():
    expected = ['Kurt']
    actual = Band('Nirvana', ['Kurt']).member_list
    assert expected == actual

def test_members_attr_two_members():
    expected = ['Kurt', 'David']
    actual = Band('Nirvana', ['Kurt', 'David']).member_list
    assert expected == actual

def test_members_attr_many_members():
    expected = ['Chris Cornell', 'Kim Thayil', 'Ben Shepherd', 'Matt Cameron', 'Hiro Yamamoto']
    actual = Band('Soundgarden', ['Chris Cornell', 'Kim Thayil', 'Ben Shepherd', 'Matt Cameron', 'Hiro Yamamoto']).member_list
    assert expected == actual

# A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
# A Band instance should have appropriate __str__ and __repr__ methods.
# A Band should have a class method to_list which returns a list of previously created Band instances
# A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance. The Band instance should have its members be set to musicians based on info from the input.
