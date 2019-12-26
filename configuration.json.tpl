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
    "StrangeFileRemoveHandler": {
      "module_path": "plexclient.handler.strange_file_remove_handler",
      "enabled": true,
      "exclude_folders": ["000_Completed_Torrents"],
      "allowed_extensions": [".mkv", ".avi", ".mp4", ".jpg", ".jpeg", ".png",".nfo", ".srt", ".png"]
    },
    "EmptyFolderRemoveHandler": {
      "module_path": "plexclient.handler.empty_folder_remove_handler",
      "enabled": true,
      "exclude_folders": ["000_Completed_Torrents"],
      "movie_extensions": [".mkv", ".avi", ".mp4"]
    },
    "MovieArchiveHandler": {
      "module_path": "plexclient.handler.movie_archive_handler",
      "enabled": true,
      "source_section_name": "Movies",
      "target_section_name": "Archive",
      "target_collection_name": "Archive"
    },
    "MovieDeletionHandler": {
      "module_path": "plexclient.handler.movie_deletion_handler",
      "enabled": true,
      "source_section_name": "Movies",
      "target_collection_name": "Delete"
    },
    "LibraryUpdateHandler": {
      "module_path": "plexclient.handler.library_update_handler",
      "enabled": true
    }
  }
}

