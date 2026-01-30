> # OSINT Image Search Tool
# Overview

This Python script performs reverse image search based on facial recognition using the FaceCheck.id API. It allows users to find similar face matches across the internet for OSINT (Open-Source Intelligence) investigations.

# Key Features

    Facial recognition-based image search

    GUI file selector for image upload

    Real-time search progress tracking

    Results saved to text file

    Automatic browser opening for web results

    Error handling and status reporting

# How It Works
1. Authentication

    Uses API token authentication with FaceCheck.id

    apitoken variable stores the authentication key

    testingmode flag controls demo/production mode

2. Search Process

    User selects an image file through a graphical file dialog

    Image is uploaded to FaceCheck.id API

    Receives a unique id_search for tracking

    Polls API for search completion with progress updates

    Retrieves matching results with confidence scores

3. Output

    Saves all found URLs to results.txt

    Opens browser with direct link to FaceCheck.id results page

    Displays error messages if search fails

# File Structure
```bash
OsintImageSearch.py
results.txt (generated after successful search)
```

# Dependencies
```python

import os
import time
import requests
import webbrowser
from tkinter import Tk, filedialog
```
# etup & Usage
Prerequisites

    Install Python 3.x

    Install required packages:

```bash

pip install requests
```
# Configuration

    Replace the apitoken with your valid FaceCheck.id API key

    Set testingmode to False for production use

# Running the Script
```bash

python OsintImageSearch.py

    Select an image file when prompted

    Wait for search completion

    View results in results.txt and web browser
```
# API Endpoints Used
```bash
    POST /api/upload_pic - Upload image for analysis

    POST /api/search - Check search status and retrieve results
```
# Security Notes

    ⚠️ Warning: The API token in the code is exposed. In production, use environment variables or configuration files

    Only supports JPG, PNG, and JPEG formats

    Requires internet connection for API calls

# Output Format

Results are saved in results.txt with format:
```bash

[+] - [1] - Url: https://example.com/image1.jpg
[+] - [2] - Url: https://example.com/image2.jpg
```
# Possible Enhancements

    Add support for multiple images

    Implement batch processing

    Add result filtering by confidence score

    Create GUI for better user experience

    Add proxy support for anonymity

    Implement rate limiting and error retry logic

# Limitations

    Dependent on FaceCheck.id API availability

    Requires valid API token

    Search speed depends on image complexity and server load

    May have usage limits based on API plan

# License

This tool is for educational and legitimate OSINT purposes only. Users are responsible for complying with applicable laws and terms of service.
