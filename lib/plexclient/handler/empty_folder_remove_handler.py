#
#  Author: Adam Jakab
#  Copyright: Copyright (c) 2019., Adam Jakab
#  License: See LICENSE.txt
#  Email: adaja at itu dot dk
#

import glob
import os
import shutil


class EmptyFolderRemoveHandler:
    _plex = None
    _config = None
    _classname = None
    _folder_list = []

    def __init__(self, plex, config):
        self._plex = plex
        self._config = config
        self._classname = self.__class__.__name__
        print("#" * 80 + ": " + self._classname)

    def run(self):
        self._list_folders()
        print("Searching for empty folders...")
        for folder in self._folder_list:
            movie_files = self._get_movie_files(folder)
            if len(movie_files) == 0:
                print("Deleting empty folder: {0}".format(folder))
                shutil.rmtree(folder, ignore_errors=True)

    def _get_movie_files(self, folder):
        files = []
        for f in glob.glob(folder + "/**", recursive=False):
            if os.path.isfile(f):
                fn, fe = os.path.splitext(f)
                if fe in self._config["movie_extensions"]:
                    files.append(f)

        return files

    def _list_folders(self):
        sections = self._plex.library.sections()
        for section in sections:
            for location in section.locations:
                for f in glob.glob(location + "/**", recursive=False):
                    if os.path.isdir(f):
                        if os.path.basename(f) not in self._config["exclude_folders"]:
                            self._folder_list.append(f)
