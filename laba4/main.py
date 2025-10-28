from CsvReader import CsvReader
from DataPreprocessor import DataPreprocessor

csv_url = "https://informer.com.ua/dut/python/import/129-indeksi-tsin-na-zhitlo.csv"
csv_reader = CsvReader()
data = csv_reader.read_data(csv_url)

preprocessor = DataPreprocessor(data)
processed_data = preprocessor.add_index_ids()

print(processed_data[:3])