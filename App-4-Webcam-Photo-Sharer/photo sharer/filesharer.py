from filestack import Client
# filestack client

from api import api_key as ak
# importing secret api key, sorry i can not share that


class FileSharer():

    def __init__(self, file_path, api_key=ak) -> None:
        self.file_path = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        file_link = client.upload(filepath=self.file_path)
        return file_link.url


if __name__ == '__main__':
    file_sharer = FileSharer('image.png')
    print(file_sharer.share())
