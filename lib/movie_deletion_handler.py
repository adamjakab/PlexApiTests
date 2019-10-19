import os


class MovieDeletionHandler:
    _plex = None
    _delete_collection_name = "Delete"
    _movie_container_directory = "/Volumes/Data/Movies"
    _ssh_username = "jackisback"
    _ssh_host = "192.168.1.84"
    _section = None
    _movie_list = []

    def __init__(self, plex):
        self._plex = plex
        self._section = self._plex.library.section('Movies')
        self._listMovies()
        if len(self._movie_list) > 0:
            print("Movies to be deleted: {0}".format(len(self._movie_list)))


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

            print("DELETING: {0}".format(directory))
            cmd = 'ssh {0}@{1} \'rm -rf "{2}"\''.format(self._ssh_username, self._ssh_host, directory)
            print("EXECUTING: {0}".format(cmd))
            os.system(cmd)


    def _listMovies(self):
        self._movie_list = self._section.search(collection=[self._delete_collection_name])
