import os
from .window import BaseWindow
from ui.text import Text
from ui.button import Button
from utils.sound import SoundTracks,SoundEffects
from utils.message import Message
import tkinter as tk
from tkinter import filedialog
import settings


def choose_music_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Chose song",
        filetypes=[("Audio files", "*.mp3 *.wav *.ogg *.flac"), ("All files", "*.*")]
    )
    return file_path


class MusicWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.title = Text((550, 0), "CHOSE YOUR OWN SONGS!!!", 100, True)
        self.message_to_much_songs = Message(f"You can't add more than {settings.MAX_SONGS} songs", (255, 0, 0), 70000)
        self.users_music = SoundTracks._get_instance().users_music
        self.songs = dict()

        self.button_add = Button((300, 600), "Add", 50, button_size=(300, 75), center_x=True)

    def shorten_text(self, text, max_length=20):
        if len(text) > max_length:
            return text[:max_length-3] + "..."
        return text

    def draw_and_update_songs(self):
        y = 120
        for song in self.users_music.music_list:
            self.songs[song.path] = [
                Text((520, y), self.shorten_text(os.path.basename(song.path)), 30),
                Button((925, y), "Enabled" if song.is_enabled else "Disabled", button_size=(150, 70)),
                Button((1125, y), "Remove", button_size=(150, 70)),
                song
            ]
            y += 100

    def draw(self, screen, event):
        super().draw(screen)

        if self.is_on:
            self.title.draw(screen)
            self.button_add.draw(screen)
            self.message_to_much_songs.draw(screen)

            if not self.songs:
                self.draw_and_update_songs()

            for text, btn_status, btn_remove, song in self.songs.values():
                text.draw(screen)
                btn_status.draw(screen)
                btn_remove.draw(screen)

                if btn_status.is_clicked(event):
                    song.is_enabled = not song.is_enabled
                    btn_status.set_text("Enabled" if song.is_enabled else "Disabled")

                    if song.is_enabled:
                        self.users_music.enable_music(song.path)

                    else:
                        self.users_music.disable_music(song.path)

                if btn_remove.is_clicked(event):
                    self.users_music.remove_song(song.path)
                    del self.songs[song.path]
                    self.draw_and_update_songs()
                    break

            if self.button_add.is_clicked(event):
                file = choose_music_file()
                if file:
                    try:
                        self.users_music.add_song(file)
                        self.draw_and_update_songs()
                    except ValueError:
                        self.message_to_much_songs.show()
                        SoundEffects.error()

                    except FileNotFoundError:
                        print(f"File not found: {file}")
