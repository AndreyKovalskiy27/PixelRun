import json
import random
import os
import settings
from dataclasses import dataclass, asdict


@dataclass
class Song:
    path: str
    is_enabled: bool = False


class UsersMusic:
    MAX_SONGS = settings.MAX_SONGS

    def __init__(self):
        self.file_path = settings.USERS_MUSIC_PATH
        self.music_list: list[Song] = self.load()

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []

        valid_songs = []
        for item in data:
            song = Song(**item)
            if os.path.exists(song.path):
                valid_songs.append(song)

        if len(valid_songs) != len(data):
            self.music_list = valid_songs
            self.save()

        return valid_songs

    def save(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([asdict(song) for song in self.music_list], f, ensure_ascii=False, indent=2)

    def add_song(self, path: str):
        if len(self.music_list) >= self.MAX_SONGS:
            raise ValueError(f"Cannot add more than {self.MAX_SONGS} songs.")
        if any(song.path == path for song in self.music_list):
            return False
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        self.music_list.append(Song(path=path))
        self.save()
        return True

    def remove_song(self, path: str):
        before = len(self.music_list)
        self.music_list = [s for s in self.music_list if s.path != path]
        if len(self.music_list) < before:
            self.save()
            return True
        return False

    def enable_music(self, path: str):
        for song in self.music_list:
            if song.path == path:
                song.is_enabled = True
                self.save()
                return True
        return False

    def disable_music(self, path: str):
        for song in self.music_list:
            if song.path == path:
                song.is_enabled = False
                self.save()
                return True
        return False

    def choose_random(self):
        enabled_songs = [s for s in self.music_list if s.is_enabled]
        if not enabled_songs:
            return settings.GAME_MUSIC_PATH
        return random.choice(enabled_songs).path
