# YouTube to MP3 Script

This project provides a Python script that downloads a YouTube video and converts it to MP3 format. Below are the instructions for setting up the environment and using the script.

## Requirements

- Python 3.6 or higher

## Setting Up the Environment

Follow these steps to create a virtual environment and install the necessary dependencies:

### Clone the Repository

If you haven't already cloned the repository, do so with:
```bash
git clone <repository_url>  
cd <repository_directory>
```

### Create a Virtual Environment

Create a virtual environment using `venv`:
``` bash
python -m venv venv
```

### Activate the Virtual Environment
```bash
source venv/bin/activate
```

### Install Dependencies

Ensure you have a `requirements.txt` file in your project directory. Install the required packages using:

```bash
pip install -r requirements.txt
```

## Using the Script

Once the environment is set up and dependencies are installed, you can use the `youtube_to_mp3.py` script to download and convert YouTube videos to MP3.

### Usage

```bash
python youtube_to_mp3.py -y "<youtube_url>"
```

### Example

To download and convert a YouTube video with the URL `https://www.youtube.com/watch?v=H58vbez_m4E`, run:

```bash
python youtube_to_mp3.py -y "https://www.youtube.com/watch?v=H58vbez_m4E"
```

## Script Overview

- **parse_arguments()**  
  Parses command-line arguments. The required argument is:
  - `-y` or `--youtube_url`: The URL of the YouTube video to download and convert.

- **youtube_to_mp3(youtube_url)**  
  Downloads the video from YouTube and converts it to MP3 format.
