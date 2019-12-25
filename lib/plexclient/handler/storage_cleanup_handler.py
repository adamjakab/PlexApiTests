#
#  Author: Adam Jakab
#  Copyright: Copyright (c) 2019., Adam Jakab
#  License: See LICENSE.txt
#  Email: adaja at itu dot dk
#

import glob
import os
import shutil
import subprocess


class StorageCleanupHandler:
    _plex = None
    _config = None
    _classname = None
    _movie_container_directory = "/Volumes/Data/Movies"
    _exclude_folders = ["000_Completed_Torrents"]
    _movie_extensions = [".mkv", ".avi", ".mp4"]
    _folder_list = []

    def __init__(self, plex, config):
        self._plex = plex
        self._config = config
        self._classname = self.__class__.__name__
        print("#" * 80 + ": " + self._classname)

    def run(self):
        print("fico")

    def do_it(self):
        self._listFolders()
        # Handle Zero movie folders - DELETE
        print("--- NO-MOVIE FOLDERS ---")
        for folder in self._folder_list:
            movie_files = self._getMovieFiles(folder)
            if len(movie_files) == 0:
                print("NO-MOVIE FOLDER({0}): {1}".format(folder, movie_files))
                print("DELETING: {0}".format(folder))
                # shutil.rmtree(folder, ignore_errors=True)

        # Handle Multiple movie folders - DELETE
        # print("#" * 80)
        # print("--- MULTI-MOVIE FOLDERS ---")
        # for folder in self._folder_list:
        #     movie_files = self._getMovieFiles(folder)
        #     if len(movie_files) > 1:
        #         print("MULTI-MOVIE FOLDER({0}): {1}".format(folder, movie_files))




    def _getMovieFiles(self, folder):
        files = []
        for f in glob.glob(folder + "/**", recursive=False):
            if os.path.isfile(f):
                fn, fe = os.path.splitext(f)
                if fe in self._movie_extensions:
                    files.append(f)

        return files

    def _listFolders(self):
        for f in glob.glob(self._movie_container_directory + "/**", recursive=False):
            if os.path.isdir(f):
                if os.path.basename(f) not in self._exclude_folders:
                    self._folder_list.append(f)


