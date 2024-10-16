import argparse, sys, pytubefix
from concurrent.futures import ThreadPoolExecutor

def download(args):
    if args.m not in ["m", "s"]:
        print("Invalid argument. Use -h to get help.")
        return

    if not args.u:
        print("Error: You must provide a video URL using the -u argument.")
        return
    
    if args.m=="m":
        url_list=pytubefix.Playlist(args.u).video_urls
        def download_playlist(url):
            parsed_url=pytubefix.YouTube(url)
            print(f"\nDownloading: {parsed_url.title}\nLength: {(parsed_url.length)/60 :.2f} Minutes\nFile Size: {parsed_url.streams.get_highest_resolution().filesize_mb} Mb\n{'='*40}")
            try:
                parsed_url.streams.get_highest_resolution().download(args.d)
            except Exception as e:
                return e
        
        with ThreadPoolExecutor() as executor:
            executor.map(download_playlist, url_list)

    elif args.m=="s":
        parsed_url=pytubefix.YouTube(args.u)
        parsed_url.streams.get_highest_resolution().download(args.d)
        return parsed_url.title+" \nDownloaded at "+args.d

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-m", type=str, default="s", help="Enter mode (Video or Playlist)")
    parser.add_argument("-u", type=str, help="Enter Video URL")
    parser.add_argument("-d", type=str, default=r"C:\Users", help="Enter file destination")
    args=parser.parse_args()
    sys.stdout.write(str(download(args)))