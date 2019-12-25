{
  "PLEX": {
    "url": "http://127.0.0.1:32400",
    "token": ""
  },
  "HANDLERS": {
    "PlexInfoHandler": {
      "module_path": "plexclient.handler.plex_info_handler",
      "enabled": true
    },
    "StorageCleanupHandler": {
      "module_path": "plexclient.handler.storage_cleanup_handler",
      "enabled": false,
      "movie_extensions": [".mkv", ".avi", ".mp4"],
      "image_extensions": [".jpg", ".jpeg", ".png"],
      "other_extensions": [".nfo", ".srt", ".png"]
    }
  }
}

