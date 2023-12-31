class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words = self.contents.split()
        self.chunk_start_point = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return self.title + ": " + self.contents

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        return len(self.words) / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        if self.chunk_start_point >= len(self.words):
            self.chunk_start_point = 0
        chunk_size_in_words = wpm * minutes
        chunk_end_point = self.chunk_start_point + chunk_size_in_words
        chunk = " ".join(self.words[self.chunk_start_point:chunk_end_point])
        self.chunk_start_point = chunk_end_point
        return chunk
    
