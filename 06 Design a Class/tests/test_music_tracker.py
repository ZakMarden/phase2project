from lib.music_tracker import *

#test returns blank list

def test_blank_list():
    test = music_tracker()
    assert test.list_tracks() == "Tracks listened to:\n"

#test add track to list

def test_add_track():
    test = music_tracker()
    test.add_track("track1")
    assert test.list_tracks() == "Tracks listened to:\ntrack1"

#test add multiple tracks

def test_add_mult_tracks():
    test = music_tracker()
    test.add_track("track1")
    test.add_track("track2")
    test.add_track("track3")
    assert test.list_tracks() == "Tracks listened to:\ntrack1\ntrack2\ntrack3"

#test add track already listened to

def test_add_already_listened():
    test = music_tracker()
    test.add_track("track1")
    test.add_track("track2")
    test.add_track("track2")
    assert test.list_tracks() == "Tracks listened to:\ntrack1\ntrack2"