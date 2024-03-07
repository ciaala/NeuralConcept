import os


class Config:
    def __init__(self):
        self.shared_path = os.getenv('SHARED_PATH',".")
        print("Shared path: " + self.shared_path)