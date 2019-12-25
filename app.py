
# from plexapi.myplex import MyPlexAccount
import json
import os
import sys

from plexapi.server import PlexServer

from lib.class_loader import ClassLoader

# from lib.library_update_handler import LibraryUpdateHandler
# from lib.movie_archive_handler import MovieArchiveHandler
# from lib.movie_deletion_handler import MovieDeletionHandler
# from lib.storage_cleanup_handler import StorageCleanupHandler
# from lib.plex_info_handler import PlexInfoHandler

config = None

__script_dir__ = os.path.dirname(os.path.realpath(__file__))
config_file = __script_dir__ + '/configuration.json'
try:
    with open(config_file) as config_file:
        config = json.load(config_file)
except Exception as e:
    print("The configuration file cannot be opened! Fatal error: {0}".format(e))
    sys.exit(201)


'''
To get a token go to any movie, click "Get Info" > "View XML" and in the URL find "X-Plex-Token" param
'''
plex = PlexServer(config["PLEX"]["url"], config["PLEX"]["token"])

CL = ClassLoader()

for class_name in config["HANDLERS"]:
    handler_config = config["HANDLERS"][class_name]
    if "enabled" in handler_config and handler_config["enabled"] is True:
        module_path = "lib." + handler_config["module_path"]
        handler_instance = CL.get_instance(module_path, class_name, plex=plex, config=handler_config)
        handler_instance.run()



exit(0)


PIH = PlexInfoHandler(plex, config)
PIH.do_it()


#
# MDH = MovieDeletionHandler(plex)
# MDH.do_it()
#
# MAH = MovieArchiveHandler(plex)
# MAH.do_it()
#
# LUH = LibraryUpdateHandler(plex)
# LUH.update_library()

exit(0)
