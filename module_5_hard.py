#  Интегрируем модуль time в проект для отсчета времени методом sleep
import time

class User:
    
    """
     Создаем класс User и определяем его атрибуты, а также определяем методы для класса:
    __init__ - конструктор класса, вызывается при создании
    __eq__ - для сравнения никнеймов
    __str__ - для вывода имени в виде строки
    __hash__ - для хэша пароля
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
     
    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return f'{self.nickname}'
        
    
class Video:
    
    """
     Создаем класс Video и определяем его атрибуты, а также определяем методы для класса:
    __init__ - конструктор класса, вызывается при создании
    __eq__ - сравнения названий видео
    __str__ - вывод названия видео в виде строки
    dur - возвращения значения длины видео
    
    """
    
    def __init__(self, title: str, duration: str, time_now = 0, adult_mode = bool(False)):
        super().__init__()
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        
    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return f'{self.title}'

    def dur(self):
        return self.duration

class UrTube:
    
    """
    Создаем класс UrTube и определяем его атрибуты - списки (users, videos, current_user), а также определяем метод для класса и функции:
    __init__ - конструктор класса, вызывается при создании
    log_in - вход пользователя (сравнение имени и пароля с имющимся в списке)
    register - регистрация нового пользователя (внесение в список users)
    log_out - выход пользователя (current_user = None)
    add - добавление видео в список videos
    get_videos -  вывод списка видео
    watch_video - просмотр видео (отсчет времени просмотра)
    
    """
    
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        
    def log_in(self, nickname: str, password: int):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                return self.current_user

    def register(self, nickname: str, password: int, age: int):
            Nuser = User(nickname, password, age)
            if Nuser not in self.users:
                self.users.append(Nuser)
                self.log_out()
                self.log_in(nickname, password)
            else:
                print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)
            else:
                print(f'Видео с названием {i.title} уже существует')

    def get_videos(self, text):
        listOfVideos = []
        for i in self.videos:
            if text.lower() in i.title.lower():
                listOfVideos.append(str(i))
        return listOfVideos

    def watch_video(self, video):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for i in self.videos:
                if video in i.title:
                    dur = Video.dur(i)
                    for k in range(1, dur + 1):
                        print(k, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    
# Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
