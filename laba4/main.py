from CsvReader import CsvReader
from DataPreprocessor import DataPreprocessor
from DataAnalyzer import DataAnalyzer
from DataUploader import DataUploader
from DatabaseQueries import DatabaseQueries
csv_url = "https://informer.com.ua/dut/python/import/129-indeksi-tsin-na-zhitlo.csv"

csv_reader = CsvReader()
data = csv_reader.read_data(csv_url)

preprocessor = DataPreprocessor(data)
processed_data = preprocessor.add_index_ids()

analyzer = DataAnalyzer(data)

indices = analyzer.get_indices()
print("Індекси:", indices)

periods = analyzer.get_periods()
print("Періоди:", periods)


indices_by_period = analyzer.get_indices_by_period()
print("Індекси за періодами:", indices_by_period)
uploader = DataUploader()
uploader.upload_indices(indices)
uploader.upload_periods(periods)
uploader.close()

print("Дані успішно завантажені у базу даних.")
queries = DatabaseQueries()

indices = queries.find_indices_by_period("2016 Q1")
print("Індекси за періодом '2016 Q1':", indices)

average_indices = queries.get_average_index_by_period()
print("Середні значення індексів за періодами:", average_indices)

queries.close()


