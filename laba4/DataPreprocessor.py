class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def add_index_ids(self):
        for index, entry in enumerate(self.data, start=1):
            entry['_id'] = index
        return self.data
