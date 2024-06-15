class NotificationManager:
    """Класс для управления уведомлениями."""
    
    def send_notification(self, message: str):
        """
        Отправляет уведомление с заданным сообщением.

        :param message: Сообщение для отправки
        """
        print(f"Уведомление: {message}")
