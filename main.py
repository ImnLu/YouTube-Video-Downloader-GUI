import os
import shutil
import tkinter.messagebox as messagebox
from threading import Thread
import customtkinter as ctk
import yt_dlp

# Dropdown menu options
options = ['Highest (up to 8K)', '4K (2160p)', '2K (1440p)', '1080p', '720p', '480p', '360p', '240p', '144p']
qualityDictionary = {options[0]: '4320',
                     options[1]: '2160',
                     options[2]: '1440',
                     options[3]: '1080',
                     options[4]: '720',
                     options[5]: '480',
                     options[6]: '360',
                     options[7]: '240',
                     options[8]: '144'}

# Creating folder shortcuts
folders = {'t': 'temp',
           'v': 'videos'}


# Enables or disables the components
def toggle_ui_components(state: bool):
    if state:
        button_download.configure(state='enabled', text='Download')
        dropdown.configure(state='readonly')
        progress_bar.set(0)
        label_ETA.configure(text='ETA: None')
        textbox_URL.delete(0, ctk.END)
        textbox_URL.configure(state='normal')
        app.title('YouTube Video Downloader')
    else:
        button_download.configure(state='disabled', text='Downloading...')
        dropdown.configure(state='disabled')
        textbox_URL.configure(state='disabled')


# Moves files from temp to videos
def move_video_files():
    for filename in os.listdir(folders['t']):
        if filename.endswith(".mp4"):
            os.replace(folders['t'] + "/" + filename, folders['v'] + "/" + filename)
            break


# Cleaning the temp folder after downloading a certain number of videos
def clear_temp_folder(delete_count: int = 3):
    try:
        if os.path.exists(folders['t'] + '/counter.aydin'):
            with open(folders['t'] + '/counter.aydin', 'r') as counter_file:
                counter = int(counter_file.read())
            if counter < delete_count:
                with open(folders['t'] + '/counter.aydin', 'w') as counter_file:
                    counter_file.write(str(counter + 1))
            else:
                shutil.rmtree(folders['t'])
        else:
            with open(folders['t'] + '/counter.aydin', 'w') as counter_file:
                counter_file.write('1')
    except Exception as e:
        print('Error:', e)
        messagebox.showerror('Error', 'Temp folder could not be deleted, please try manually.')


def download_video_with_audio(url: str, quality: str):
    def catch_infos(d):
        if d['status'] == 'downloading':
            try:
                percentage = float(d['_percent_str'].replace('%', '').strip()) / 100  # Extract percentage
                eta = str(d['_eta_str']).strip()  # Extract ETA
                video_title = d['info_dict']['title']
                label_ETA.configure(text=f'ETA: {eta}')  # Update ETA label
                progress_bar.set(percentage)  # Update progress bar value
                app.title(video_title)  # Sets app title to video name
            except Exception as error:
                print(error)

    if quality == '4320':
        try:
            ydl_opts = {
                'format': f'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
                'outtmpl': os.path.join(folders['t'], '%(title)s.%(ext)s'),
                'progress_hooks': [catch_infos],
            }

            if not os.path.exists(folders['t']):
                os.mkdir(folders['t'])

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url)

            if not os.path.exists(folders['v']):
                os.mkdir(folders['v'])
            move_video_files()
            clear_temp_folder()

            toggle_ui_components(True)

        except Exception as e:
            print(f'Failed to download video. Error: {e}')
            toggle_ui_components(True)
            messagebox.showerror('Error', 'Video not found.')

    else:
        try:
            ydl_opts = {
                'format': f'bestvideo[ext=mp4][height={quality}]+bestaudio[ext=m4a]',
                'outtmpl': os.path.join(folders['t'], '%(title)s.%(ext)s'),
                'progress_hooks': [catch_infos],  # Add progress hook
            }

            if not os.path.exists(folders['t']):
                os.mkdir(folders['t'])

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url)

            if not os.path.exists(folders['v']):
                os.mkdir(folders['v'])
            move_video_files()
            clear_temp_folder()

            toggle_ui_components(True)

        except Exception as e:
            print(f'Failed to download video. Error: {e}')
            toggle_ui_components(True)
            messagebox.showerror('Error', f'{quality} quality is not available.')


def start_download():
    textbox_text = textbox_URL.get()  # Gets video link

    if textbox_text == '':
        toggle_ui_components(True)
        messagebox.showerror('Error', 'Video URL cannot be empty.')

    elif textbox_text.startswith('https://www.youtube.com/watch?v=') or textbox_text.startswith(
            'https://youtu.be/') or textbox_text.startswith('www.youtu.be/') or textbox_text.startswith(
            'youtu.be/') or textbox_text.startswith('www.youtube.com/watch?v=') or textbox_text.startswith(
            'youtube.com/watch?v='):
        toggle_ui_components(False)
        selected_quality = qualityDictionary[dropdown.get()]

        # Start a new thread to download the video
        Thread(target=download_video_with_audio, args=(textbox_text, selected_quality)).start()

    else:
        toggle_ui_components(True)
        messagebox.showerror('Error', 'Video URL is invalid.')


# Creating a window
app = ctk.CTk()
app.geometry('400x300')  # Set the initial window size
app.title('Youtube Video Downloader')
ctk.set_appearance_mode('Dark')

# Prevent resizing by setting resizable attributes to False
app.resizable(False, False)

# Video URL label
label_URL = ctk.CTkLabel(app, text='Video URL')
label_URL.pack(pady=10)

# URL textbox
textbox_URL = ctk.CTkEntry(app, width=320, height=30)
textbox_URL.pack(pady=10)

# Video quality dropdown menu
dropdown = ctk.CTkComboBox(app, width=150, values=options, state='readonly')
dropdown.set('Highest (up to 8K)')  # Sets highest quality by default
dropdown.pack(pady=10)

# Download button
button_download = ctk.CTkButton(app, text='Download', command=start_download)
button_download.pack(pady=10)

# ETA label
label_ETA = ctk.CTkLabel(app, text='ETA: None')
label_ETA.pack(pady=10)

# Progress Bar
progress_bar = ctk.CTkProgressBar(app, width=320, height=30)
progress_bar.set(0)
progress_bar.pack()

app.mainloop()
