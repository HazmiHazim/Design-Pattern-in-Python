import threading


class User:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def printHash(self):
        print(hash(self))


class SingletonPattern:

    @staticmethod
    def main():
        thread1 = threading.Thread(
            target=lambda: User().getInstance().printHash())
        thread2 = threading.Thread(
            target=lambda: User().getInstance().printHash())
        thread3 = threading.Thread(
            target=lambda: User().getInstance().printHash())

        thread1.start()
        thread2.start()
        thread3.start()


if __name__ == "__main__":
    SingletonPattern.main()
