from injector import Injector

from app.Application import Application

if __name__ == '__main__':
    injector = Injector()
    app = injector.get(Application)
    app.start()
