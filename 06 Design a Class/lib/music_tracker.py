"""
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
"""

class music_tracker():
    def __init__(self):
        self.track_list = []

    def add_track(self, track):
        if track not in self.track_list:
            self.track_list.append(track)
        else:
            print("Track not added, already in list!")
        return

    def list_tracks(self):
        print("Tracks listened to:\n" + "\n".join(self.track_list))
        return "Tracks listened to:\n" + "\n".join(self.track_list)
    
test = music_tracker()
test.add_track("track1")
test.add_track("track2")
test.add_track("track3")
test.list_tracks()
test.add_track("track3")
test.list_tracks()