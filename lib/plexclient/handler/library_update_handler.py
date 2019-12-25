
class LibraryUpdateHandler:
    _plex = None

    def __init__(self, plex):
        self._plex = plex

    def update_library(self):
        self._plex.library.update()
