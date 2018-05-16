class Song:
    """Class to represent a song

    Attributes:
        title (str): the title of the song
        artist (Artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds. May be zero
        """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent album, using its track list

    Attributes:
        name (str): Name of the album
        year (int): year album released
        artist (Artist) : artist responsible for the album
            if not specified the artist will default to
            'Various Artists'
        tracks (list[song]): a list of the songs on the album

    Methods:
        add_song: used to add a new song to the albums track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = Artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): song to add
            position (optional [int]): if specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the track list
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details

    Attributes:
        name (str): the name of the artist
        albums (List[album]): a list of albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artists published albums.

    Methods:
        add_album: use to add a new album to the artists albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list

        Args:
            album (Album): an album object to add to the list.
                if the album already present it will not be added again (yet to be implemented)
        """
        self.albums.append(album)


def find_object(field, object_list):
    """check 'object_list' to see if an object with a 'name' attribute equal to field exists and return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # we have just read new details for artist
                # retrieve the srtist object if there is one,
                # otherwise create a new artist object and add it to the artist list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # we have just read a new album for the current artist
                # retrieve the album object if there is one,
                # otherwise create a new album object and store it in the artists collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current albums collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_check_file(artist_list):
    """create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", "w") as check_file:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=check_file)


if __name__ == "__main__":  # this check means execute only if the program is being run as a script
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_check_file(artists)
