
# from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

from lib.library_update_handler import LibraryUpdateHandler
from lib.movie_archive_handler import MovieArchiveHandler
from lib.movie_deletion_handler import MovieDeletionHandler
from lib.storage_cleanup_handler import StorageCleanupHandler
'''
To get a token go to any movie, click "Get Info" > "View XML" and in the URL find "X-Plex-Token" param
'''
baseurl = 'http://192.168.1.84:32400'
token = 'LuqDSoWTFjxWTxx-4JaE'
plex = PlexServer(baseurl, token)

SCH = StorageCleanupHandler(plex)


# MDH = MovieDeletionHandler(plex)
# MDH.do_it()
#
# MAH = MovieArchiveHandler(plex)
# MAH.do_it()

# LUH = LibraryUpdateHandler(plex)
# LUH.update_library()

exit(0)



def printVideoInfo(v, detailed=False):
    print("=" * 80)
    if not detailed:
        print("V({0}): W({1}) - WC({2}) - M({3})".format(v.title, v.isWatched, v.viewCount, len(v.media)))
    else:
        print("." * 80)
        keys = v.__dict__.keys()
        for key in keys:
            print("V({0}): {1}".format(key, getattr(v, key)))

    for m in v.media:
        if not detailed:
            print("M({0}): Parts: ".format(m.id), len(m.parts))
        else:
            print("." * 80)
            keys = m.__dict__.keys()
            for key in keys:
                print("M({0}): {1}".format(key, getattr(m, key)))

        for p in m.parts:
            if not detailed:
                print("P({0})-Container({1}): path: '{2}'".format(p.id, p.container, p.file))
            else:
                print("." * 80)
                keys = p.__dict__.keys()
                for key in keys:
                    print("P({0}): {1}".format(key, getattr(p, key)))

    print("=" * 80)


def checkMultipleMediaMovies(all_movies):
    mmmc = 0
    for movie in all_movies:
        num_media = len(movie.media)
        if num_media != 1:
            mmmc += 1
            printVideoInfo(movie)
    if mmmc == 0:
        print("There are no multiple Media movies.")


def checkMuliplePartMovies(all_movies):
    mpmc = 0
    for movie in all_movies:
        for media in movie.media:
            num_parts = len(media.parts)
            if num_parts != 1:
                mpmc += 1
                printVideoInfo(movie)
    if mpmc == 0:
        print("There are no multiple Part movies.")




#movies = plex.library.section('Movies')


# movie = plex.library.section('Movies').get('Toy Story 4')
# printVideoInfo(movie)
# keys = movie.__dict__.keys()
# for k in keys:
#     print("M({0}): {1}".format(k, getattr(movie, k)))
#
# print("#"*80)
# label0 = movie.labels[0]
# keys = label0.__dict__.keys()
# for k in keys:
#     print("M({0}): {1}".format(k, getattr(label0, k)))



# allMovies = movies.search()
# print("TOTAL MOVIES: {0}".format(len(allMovies)))
# checkMultipleMediaMovies(allMovies)
# checkMuliplePartMovies(allMovies)


# Empty - La vera Storia di Sansone - Samson 2018 1080 H264 Ita Eng Ac3 5.1 Sub Ita Eng MIRCrew .mkv
# Karate.Kid,.The.(1984)



'''
'accountID', 'actors', 'addCollection', 'addGenre', 'addLabel', 'addedAt', 'analyze', 'art', 'artUrl', 'audienceRating',
'audienceRatingImage', 'chapterSource', 'chapters', 'collections', 'contentRating', 'countries', 'delete', 'directors',
'download', 'duration', 'edit', 'fetchItem', 'fetchItems', 'fields', 'findItems', 'firstAttr', 'genres', 'getStreamURL'
'guid', 'isFullObject', 'isPartialObject', 'isWatched', 'iterParts', 'key', 'labels', 'lastViewedAt', 
'librarySectionID', 'listAttrs', 'listType', 'locations', 'markUnwatched', 'markWatched', 'media', 'originalTitle', 
'originallyAvailableAt', 'play', 'players', 'playlistItemID', 'primaryExtraKey', 'producers', 'rate', 'rating', 
'ratingImage', 'ratingKey', 'refresh', 'reload', 'removeCollection', 'removeGenre', 'removeLabel', 'roles', 'section',
'session', 'sessionKey', 'similar', 'split', 'stop', 'studio', 'subtitleStreams', 'summary', 'sync', 'tagline', 
'thumb', 'thumbUrl', 'title', 'titleSort', 'transcodeSessions', 'type', 'unmatch', 'updateProgress', 'updateTimeline',
'updatedAt', 'url', 'userRating', 'usernames', 'viewCount', 'viewOffset', 'viewedAt', 'writers', 'year']
'''