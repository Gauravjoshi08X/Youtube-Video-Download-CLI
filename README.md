# YouTube Video Downloader CLI
A simple command-line interface (CLI) tool for downloading YouTube videos and playlists using Python. This tool leverages the `pytubefix` library to provide an easy and efficient way to download videos directly to your local machine.

# Features
* Download individual YouTube videos.
*  Download entire playlists.
* Specify download location.

# Requirements
* Python 3.x
* `pytubefix` library

# Installation
To use this script from any terminal window, you need to add it to your system's PATH. Make sure you have Python installed on your system. You can install the `pytubefix` library using pip:

```bash
pip install pytubefix
```
# Usage
You can run the script from the command line with the following options:
```bash
python youtube_downloader.py -m <mode> -u <url> -d <destination>
```

# Parameters
* `-m`: Specify the mode of download. Use `m` for downloading a playlist and `s` for a single video. Default is `s`.
* `-u`: The URL of the YouTube video or playlist you wish to download.
* `-d`: The directory where you want the downloaded files to be saved. Default can be set.

# Examples
## Download a Single Video
To download a single video, use the following command:

```bash
python youtube_downloader.py -m s -u <video_url>
```

## Download a Playlist
To download a playlist, use the following command:
```bash
python youtube_downloader.py -m m -u <playlist_url>
```
# Error Handling
If you provide an invalid mode `(-m)`, the script will prompt you to check the help for valid options.
If you do not provide a video URL `(-u)`, the script will notify you that it is a required argument.
