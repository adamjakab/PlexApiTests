#
#  Author: Adam Jakab
#  Copyright: Copyright (c) 2019., Adam Jakab
#  License: See LICENSE.txt
#  Email: adaja at itu dot dk
#

import os
import shutil


class MovieDeletionHandler:
    _plex = None
    _config = None
    _movie_list = []

    def __init__(self, plex, config):
        self._plex = plex
        self._config = config
        self._classname = self.__class__.__name__
        print("#" * 80 + ": " + self._classname)

    def run(self):
        source_section = self._plex.library.section(self._config["source_section_name"])
        self._list_movies(source_section)
        if len(self._movie_list) == 0:
            return

        source_location_dir = source_section.locations[0]

        for movie in self._movie_list:
            media = movie.media[0]
            part = media.parts[0]
            file_path = part.file
            directory = os.path.dirname(file_path)
            parent_directory = os.path.dirname(directory)
            if parent_directory != source_location_dir:
                print("Bad parent directory: {0}".format(parent_directory))
                continue

            print("DELETING: {0}".format(directory))
            shutil.rmtree(directory, ignore_errors=True)

    def _list_movies(self, source_section):
        target_collection_name = self._config["target_collection_name"]
        self._movie_list = source_section.search(collection=[target_collection_name])
        print("Number of movies in collection '{0}': {1}".format(target_collection_name, len(self._movie_list)))
