import datetime
from tkinter import Tk, Label, Button, Entry, Toplevel, messagebox
from tkinter import ttk
from music_manager import MusicManager
from notification_manager import NotificationManager

class Alarm:
    """Класс будильника."""

    def __init__(self):
        """
        Инициализация будильника.
        """
        self.alarm_window = None
        self.root = Tk()  # Создаем главное окно Tkinter
        self.root.title("Будильник")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)  # Обработка закрытия окна

        self.music_manager = MusicManager()
        self.notification_manager = NotificationManager()

        self.label_hour = Label(self.root, text="Часы:", font=("Arial", 12))
        self.label_hour.grid(row=0, column=0, padx=5, pady=10)
        self.hour_entry = ttk.Combobox(self.root, width=5, font=("Arial", 12))
        self.hour_entry['values'] = tuple(str(i).zfill(2) for i in range(24))
        self.hour_entry.grid(row=0, column=1, padx=5, pady=10)
        self.hour_entry.set(datetime.datetime.now().strftime('%H'))

        self.label_separator = Label(self.root, text=":", font=("Arial", 12))
        self.label_separator.grid(row=0, column=2, padx=5, pady=10)

        self.label_minute = Label(self.root, text="Минуты:", font=("Arial", 12))
        self.label_minute.grid(row=0, column=3, padx=5, pady=10)
        self.minute_entry = ttk.Combobox(self.root, width=5, font=("Arial", 12))
        self.minute_entry['values'] = tuple(str(i).zfill(2) for i in range(60))
        self.minute_entry.grid(row=0, column=4, padx=5, pady=10)
        self.minute_entry.set(datetime.datetime.now().strftime('%M'))

        self.set_alarm_button = Button(self.root, text="Установить будильник", command=self.set_alarm, font=("Arial", 12))
        self.set_alarm_button.grid(row=1, column=0, columnspan=5, padx=5, pady=10)

    def set_alarm(self):
        """Устанавливает будильник на заданное время."""
        hour = int(self.hour_entry.get())
        minute = int(self.minute_entry.get())
        alarm_time = datetime.time(hour, minute)
        current_time = datetime.datetime.now().time()
        if current_time >= alarm_time:
            messagebox.showwarning("Предупреждение", "Выбранное время уже прошло.")
            return
        # Hide the main window after setting the alarm
        self.root.withdraw()
        # Schedule checking the time periodically
        self.check_time(alarm_time)

    def check_time(self, alarm_time):
        """Проверяет текущее время и запускает будильник, если время совпадает."""
        current_time = datetime.datetime.now().time()
        if current_time >= alarm_time:
            # Trigger the alarm
            self.trigger_alarm()
        else:
            # Check again after 1 second
            self.root.after(1000, self.check_time, alarm_time)

    def trigger_alarm(self):
        """Запускает будильник."""
        music_files = ["song1.mp3", "song2.mp3", "song3.mp3", "song4.mp3", "song5.mp3", "song6.mp3", "song7.mp3", "song8.mp3", "song9.mp3"]  # List of music files
        self.music_manager.play_music(music_files)
        messagebox.showinfo("Будильник", "Доброе утро!")
        self.root.deiconify()  # Show the main window again
        self.notification_manager.send_notification("Доброе утро!")
        


    def close_window(self):
        """Метод для закрытия окна будильника."""
        self.root.destroy()
        self.music_manager.stop_music()





if __name__ == "__main__":
    alarm = Alarm()
    alarm.root.mainloop()

