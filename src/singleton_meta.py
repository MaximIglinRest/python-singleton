class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class Application(metaclass=Singleton):
    def get_app_id(self) -> None:
        print(id(self))


if __name__ == "__main__":
    app = Application()
    app_2 = Application()

    app.get_app_id()
    app_2.get_app_id()
