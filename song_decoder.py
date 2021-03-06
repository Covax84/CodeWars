def song_decoder(song: str) -> str:
    """ Input: string(song) where words separated by several WUBs (dubstep remix).
        Output: string without WUBs with words separated by a single space (original).
    """
    return song.replace('WUB', ' ').replace('  ', ' ').replace('  ', ' ').strip()


def song_decoder2(song: str) -> str:
    """ Input: string(song) where words separated by several WUBs (dubstep remix).
        Output: string without WUBs with words separated by a single space (original).
        v.2.0
    """
    return " ".join(song.replace('WUB', ' ').split())
