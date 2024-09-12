"""
Usage:
    python youtube_to_mp3.py -y "<youtube_url>"

Example:
    python youtube_to_mp3.py -y "https://www.youtube.com/watch?v=H58vbez_m4E"

Description:
    This script downloads a YouTube video from the provided URL and
    converts it to MP3 format. It first downloads the video and then converts the
    downloaded MP4 file to MP3, saving it to a specific directory.
"""

from pytube import YouTube
from moviepy.editor import VideoFileClip
import argparse
import os
import shutil

# Global variables
TEMP_PATH = "./temp/"
MP3_PATH = "./mp3_files/"


def parse_arguments():
    """
    Parses command-line arguments for the script.

    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.

    Arguments:
        - -y or --youtube_url: The URL of the YouTube video to be downloaded
        and converted.

    This function uses the argparse module to handle command-line inputs.
    The --youtube_url argument is required and specifies the YouTube video URL
    that will be processed by the script.
    """

    parser = argparse.ArgumentParser(
        description=(
            "Process command-line arguments for downloading and "
            "converting a YouTube video."
        )
    )

    parser.add_argument(
        "-y",
        "--youtube_url",
        required=True,
        help="The URL of the YouTube video to be downloaded and converted.",
    )

    return parser.parse_args()


def youtube_to_mp3(youtube_url):
    """
    Downloads a YouTube video from the provided URL and converts it to MP3 format.

    Args:
        youtube_url (str): The URL of the YouTube video to be downloaded and converted.

    Raises:
        Exception: If an error occurs during the download or conversion process.
    """

    try:
        # Check if temp path exists
        if not os.path.exists(TEMP_PATH):
            os.makedirs(TEMP_PATH)

        # Download video from YouTube
        YouTube(youtube_url).streams.first().download(TEMP_PATH)

        # Get name of video and convert it to MP3
        files = os.listdir(TEMP_PATH)
        mp4_name = files[0]
        convert_mp4_to_mp3(mp4_name)

        # Delete temp folder
        print(f"Deleting {TEMP_PATH}")
        shutil.rmtree(TEMP_PATH)

    except Exception as e:
        print(f"Error occurred: {e}")


def convert_mp4_to_mp3(mp4_name):
    """
    Converts an MP4 file to MP3 format and saves it in the specified directory.

    Args:
        mp4_name (str): The name of the MP4 file to be converted.

    Raises:
        Exception: If an error occurs during the conversion process.
    """

    mp3_name = f"{mp4_name.split('.')[0]}.mp3"

    try:
        # Check if mp3_path exists
        if not os.path.exists(MP3_PATH):
            os.makedirs(MP3_PATH)

        # Convert mp4 to mp3
        video = VideoFileClip(f"{TEMP_PATH}{mp4_name}")
        audio = video.audio
        audio.write_audiofile(f"{MP3_PATH}/{mp3_name}")

    except Exception as e:
        print(f"Error converting MP4 to MP3: {e}")


def main():
    """
    The main function that parses command-line arguments and initiates
    the YouTube to MP3 conversion process.
    """

    args = parse_arguments()
    youtube_url = args.youtube_url
    youtube_to_mp3(youtube_url)


if __name__ == "__main__":
    main()
