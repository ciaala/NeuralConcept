from injector import Injector

from app.application import Application

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    injector = Injector()
    app = injector.get(Application)
    app.start()
