#
#  Author: Adam Jakab
#  Copyright: Copyright (c) 2019., Adam Jakab
#  License: See LICENSE.txt
#  Email: adaja at itu dot dk
#

import glob
import os
import shutil


class StrangeFileRemoveHandler:
    _plex = None
    _config = None
    _classname = None
    _file_list = []

    def __init__(self, plex, config):
        self._plex = plex
        self._config = config
        self._classname = self.__class__.__name__
        print("#" * 80 + ": " + self._classname)

    def run(self):
        self._list_files()
        print("Searching for strange files...")
        for file in self._file_list:
            print("Deleting strange file: {0}".format(file))
            os.unlink(file)

    def _list_files(self):
        sections = self._plex.library.sections()
        for section in sections:
            for location in section.locations:
                for folder in glob.glob(location + "/**", recursive=False):
                    if os.path.isdir(folder) and os.path.basename(folder) not in self._config["exclude_folders"]:
                        for file in glob.glob(folder + "/**", recursive=True):
                            if os.path.isfile(file):
                                filename = os.path.basename(file)
                                root, ext = os.path.splitext(filename)
                                if ext not in self._config["allowed_extensions"]:
                                    #print("F({0}): {1}".format(filename, ext))
                                    self._file_list.append(file)
