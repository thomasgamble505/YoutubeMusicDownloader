import csv
import os
import yt_dlp

# User-defined variables
CSV_FILE_LOCATION = "<Your_File_Location>"  # Replace with your CSV file path
OUTPUT_LOCATION = "<Your_Output_Directory>" # Replace with your desired output directory

def read_csv(file_path):
    """Read song links or names from a CSV file."""
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader if row]
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []

def download_song(song_query, output_dir):
    """Download a song from YouTube as an MP3 using a direct link or search."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': True,
        'default_search': 'ytsearch',  # Set default search to YouTube search
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([song_query])
        except Exception as e:
            print(f"Failed to download {song_query}: {e}")

def start_download(csv_file, output_dir):
    song_links_or_names = read_csv(csv_file)
    if not song_links_or_names:
        print("No song links or names found in the CSV file.")
        return

    total_songs = len(song_links_or_names)
    for i, song_query in enumerate(song_links_or_names, start=1):
        print(f"Downloading song {i} of {total_songs} ({(i / total_songs) * 100:.2f}%)")
        download_song(song_query, output_dir)

    print("Download completed!")

if __name__ == "__main__":
    start_download(CSV_FILE_LOCATION, OUTPUT_LOCATION)
