import os
import subprocess


class StorageCleanupHandler:
    _plex = None
    _movie_container_directory = "/Volumes/Data/Movies"
    _ssh_username = "jackisback"
    _ssh_host = "192.168.1.84"
    _folder_list = []

    def __init__(self, plex):
        self._plex = plex
        self._listFolders()


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


    def _listFolders(self):
        cmd = [
            "ssh",
            "{0}@{1}".format(self._ssh_username, self._ssh_host),
            'ls',
            '-A',
            '-1',
            self._movie_container_directory
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        res = result.stdout.decode('utf-8')
        folders = res.split("\n")

        print(folders)


