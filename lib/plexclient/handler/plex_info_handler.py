#
#  Author: Adam Jakab
#  Copyright: Copyright (c) 2019., Adam Jakab
#  License: See LICENSE.txt
#  Email: adaja at itu dot dk
#


class PlexInfoHandler:
    _plex = None
    _config = None

    def __init__(self, plex, config):
        self._plex = plex
        self._config = config
        self._classname = self.__class__.__name__
        print("#" * 80 + ": " + self._classname)

    def run(self):
        sections = self.get_sections()
        for section in sections:
            self.show_section_info(section)

    def show_section_info(self, section):
        movie_count = len(section.search())
        print("SECTION: '{0}' has {1} movies".format(section.title, movie_count))
        print("LOCATION: '{0}'".format(section.locations))

    def get_sections(self):
        return self._plex.library.sections()
