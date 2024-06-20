# YouTube-Video-Downloader-GUI
![image](https://github.com/ImnLu/YouTube-Video-Downloader-GUI/assets/37624905/366b0c7b-140d-4b7a-b4f8-84da102563d9)

This program uses the 'yt_dlp' library to download YouTube videos. It includes a simple graphical interface. It is easy to use.

You can download and use the project from the 'Releases' section. (includes ffmpeg.exe)

Features
====================================
  1. Download the video you want in up to 8K quality.
  2. If the video download is interrupted, continue where you left off. (After four successful video downloads, any previous interrupted video remnants will be deleted.) (yt_dlp feature)
  3. You can instantly see the progress bar and how many minutes are left for the video to download.

To do list
====================================
  1. Context menu for textbox
  2. A label showing what percentage it is in

Requirements FFMPEG
====================================
  For Windows
  1. Download FFMPEG files: https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z (in bin folder)
  2. Extract the 'ffmpeg.exe' file to the folder where the 'main.py' file is located.

  For Linux (not tested)
  1. Open terminal and run 'sudo apt install ffmpeg'

To build
====================================
  1. pip install pyinstaller
  2. pyinstaller --onefile --noconsole main.py
  3. You can find it in the '/dist' folder.


Educational Project Disclaimer
====================================
This repository contains an educational project intended solely for learning and teaching purposes. All materials and code provided here are intended to support understanding of the subject matter and should not be used for commercial purposes.

Disclaimer
====================================
Educational Use Only: The content of this repository is provided for educational purposes only. Any commercial use of the materials is strictly prohibited.

No Warranty: The materials provided in this repository are provided "as is" without any guarantees or warranties. The authors make no representations or warranties regarding the accuracy, completeness, or usefulness of the content.

Intellectual Property Rights: The project may include references to third-party intellectual property, including but not limited to code, images, and other media. All such references are made solely for educational purposes, and no infringement is intended. If any intellectual property owners have concerns about the use of their content, please contact us immediately to address the issue.

Fair Use: All third-party content used within this project is believed to be used under the fair use doctrine for educational purposes. Should there be any content that violates any rights, it will be promptly removed upon notification.

No Liability: The authors and contributors are not liable for any damages, direct or indirect, arising from the use of this educational material.



Contact
====================================
If you have any questions or concerns regarding the content of this repository, please feel free to contact the project maintainers.
