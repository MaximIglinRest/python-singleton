class Application:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_app_id(self) -> None:
        print(id(self))


if __name__ == "__main__":
    app = Application()
    app_2 = Application()

    app.get_app_id()
    app_2.get_app_id()
