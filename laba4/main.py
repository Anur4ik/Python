from CsvReader import CsvReader

csv_url = "https://informer.com.ua/dut/python/import/129-indeksi-tsin-na-zhitlo.csv"


csv_reader = CsvReader()
data = csv_reader.read_data(csv_url)

print(data[:3])
