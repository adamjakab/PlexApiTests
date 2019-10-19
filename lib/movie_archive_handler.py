import os


class MovieArchiveHandler:
    _plex = None
    _delete_collection_name = "Archive"
    _movie_container_directory = "/Volumes/Data/Movies"
    _move_target_directory = "/Volumes/J/EXT-MOVIES/"
    _ssh_username = "jackisback"
    _ssh_host = "192.168.1.84"
    _section = None
    _movie_list = []

    def __init__(self, plex):
        self._plex = plex
        self._section = self._plex.library.section('Movies')
        self._listMovies()
        if len(self._movie_list) > 0:
            print("Movies to be archived: {0}".format(len(self._movie_list)))


    def do_it(self):
        for movie in self._movie_list:
            media = movie.media[0]
            part = media.parts[0]
            file_path = part.file
            directory = os.path.dirname(file_path)
            parent_directory = os.path.dirname(directory)
            if parent_directory != self._movie_container_directory:
                print("Bad parent directory!")
                continue

            print("ARCHIVING: {0}".format(directory))
            cmd = 'ssh {0}@{1} \'mv -f "{2}" {3}\''.format(self._ssh_username, self._ssh_host,
                                                           directory, self._move_target_directory)
            print("EXECUTING: {0}".format(cmd))
            os.system(cmd)


    def _listMovies(self):
        self._movie_list = self._section.search(collection=[self._delete_collection_name])
