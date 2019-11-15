def song_decoder(song):
    """ input: string(song) where words separated by several WUBs (dubstep remix).
        output: string without WUBs with words separated by a single space (original).
    """
    return song.replace('WUB', ' ').replace('  ', ' ').replace('  ', ' ').strip()


def song_decoder2(song):
    """ input: string(song) where words separated by several WUBs (dubstep remix).
        output: string without WUBs with words separated by a single space (original).
        v.2.0
    """
    return " ".join(song.replace('WUB', ' ').split())


# print(song_decoder("AWUBBWUBC"))  # "a B C","WUB should be replaced by 1 space")
# print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))  # "a B C","multiples WUB should be replaced by only 1 space")
# print(song_decoder("WUBAWUBBWUBCWUB"))  # "a B C","heading or trailing spaces should be removed")
# print(song_decoder("WUBWUBIWUBAMWUBWUBX"))  # "I AM X"
#
# print(song_decoder2("AWUBBWUBC"))  # "a B C","WUB should be replaced by 1 space")
# print(song_decoder2("AWUBWUBWUBBWUBWUBWUBC"))  # "a B C","multiples WUB should be replaced by only 1 space")
# print(song_decoder2("WUBAWUBBWUBCWUB"))  # "a B C","heading or trailing spaces should be removed")
# print(song_decoder2("WUBWUBIWUBAMWUBWUBX"))  # "I AM X"
