#
#  Author: Adam Jakab
#  Copyright: Copyright (c) 2019., Adam Jakab
#  License: See LICENSE.txt
#  Email: adaja at itu dot dk
#


class LibraryUpdateHandler:
    _plex = None
    _config = None
    _classname = None

    def __init__(self, plex, config):
        self._plex = plex
        self._config = config
        self._classname = self.__class__.__name__
        print("#" * 80 + ": " + self._classname)

    def run(self):
        print("Updating all Plex libraries...")
        self._plex.library.update()
