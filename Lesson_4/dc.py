from dataclasses import dataclass


class Userdata:
    def __init__(self):
        self.user_id = 10  # Дабы зарезервировать служебные ID
        self.user_name = 'Unknown'


# Ну или умнее
@dataclass
class Userdata2:
    user_id: int = 10
    user_name: str = 'Unknown'
