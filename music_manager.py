import pygame
import random

class MusicManager:
    """Класс для управления музыкой."""

    def __init__(self):
        """Инициализация MusicManager."""
        pygame.mixer.init()

    def play_music(self, music_files):
        """
        Воспроизводит случайную музыку из списка.

        Args:
            music_files (list): Список путей к файлам музыки.
        """
        if not music_files:
            raise ValueError("No music files provided.")
        
        music_file = random.choice(music_files)
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        """Останавливает воспроизведение музыки."""
        pygame.mixer.music.stop()
