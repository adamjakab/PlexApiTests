import os
import subprocess


class StorageCleanupHandler:
    _plex = None
    _movie_container_directory = "/Volumes/Data/Movies"
    _ssh_username = "jackisback"
    _ssh_host = "192.168.1.84"
    _exclude_folders = ["000_Completed_Torrents"]
    _folder_list = []

    def __init__(self, plex):
        self._plex = plex
        self._listFolders()


    def do_it(self):
        for folder in self._folder_list:
            print("FOLDER: {0}".format(folder))



    def _listFolders(self):
        folders = []

        # r=root, d=directories, f = files
        for r, d, f in os.walk(self._movie_container_directory):
            for folder in d:
                if folder not in self._exclude_folders:
                    self._folder_list.append(os.path.join(r, folder))
