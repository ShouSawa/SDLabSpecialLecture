import unittest

from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))

    def test_case2(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        for row in line: # 行ごとに分解
            print(row)
            self.assertEqual(4, len(row))

    def test_case3(self):
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter("sample2.csv")
            printer.read()