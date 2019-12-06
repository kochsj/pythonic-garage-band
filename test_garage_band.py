import pytest
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
def test_solos_method_no_members():
    expected = ''
    actual = Band('Nirvana').play_solos()
    assert expected == actual

def test_solos_method_one_member():
    expected = "And now... Kurt breaks out into a solo! "
    actual = Band('Nirvana', ['Kurt']).play_solos()
    assert expected == actual

def test_solos_method_two_members():
    expected = "And now... Kurt breaks out into a solo! And now... David breaks out into a solo! "
    actual = Band('Nirvana', ['Kurt', 'David']).play_solos()
    assert expected == actual

def test_solos_method_many_members():
    expected = "And now... Chris Cornell breaks out into a solo! And now... Kim Thayil breaks out into a solo! And now... Ben Shepherd breaks out into a solo! And now... Matt Cameron breaks out into a solo! And now... Hiro Yamamoto breaks out into a solo! "
    actual = Band('Soundgarden', ['Chris Cornell', 'Kim Thayil', 'Ben Shepherd', 'Matt Cameron', 'Hiro Yamamoto']).play_solos()
    assert expected == actual

# A Band should have a class method to_list which returns a list of previously created Band instances
def test_no_previous_bands():
    expected = []
    actual = Band.to_list()
    assert expected == actual

def test_one_previous_band():
    expected = [['Alice in Chains', ['Jerry']]]
    Band('Alice in Chains', ['Jerry'])
    actual = Band.to_list()
    assert expected == actual

def test_two_previous_bands():
    expected = [['Alice in Chains', ['Jerry']], ['Nirvana', ['Kurt', 'David']]]
    Band('Alice in Chains', ['Jerry'])
    Band('Nirvana', ['Kurt', 'David'])
    actual = Band.to_list()
    assert expected == actual

def test_many_previous_bands():
    expected = [['Alice in Chains', ['Jerry']], ['Nirvana', ['Kurt', 'David']], ['Soundgarden', ['Chris Cornell', 'Kim Thayil', 'Ben Shepherd', 'Matt Cameron', 'Hiro Yamamoto']]]
    Band('Alice in Chains', ['Jerry'])
    Band('Nirvana', ['Kurt', 'David'])
    Band('Soundgarden', ['Chris Cornell', 'Kim Thayil', 'Ben Shepherd', 'Matt Cameron', 'Hiro Yamamoto'])
    actual = Band.to_list()
    assert expected == actual

def test_no_bands_out_of_order():
    expected = False
    Band('Nirvana', ['Kurt', 'David'])
    Band('Alice in Chains', ['Jerry'])
    actual = Band.to_list() == [['Alice in Chains', ['Jerry']], ['Nirvana', ['Kurt', 'David']]]
    assert expected == actual

# A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance. The Band instance should have its members be set to musicians based on info from the input.

@pytest.fixture(autouse=True)
def clean():
    Band.list_of_bands = []
