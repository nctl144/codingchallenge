import pandas


class DataHelper:

    @staticmethod
    def read_json(file_path):
        return pandas.read_json(file_path)
