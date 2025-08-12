import csv

class CSVPrinter:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines