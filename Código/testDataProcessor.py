import os
import unittest
from dataProcessor import read_json_file, avgAgeCountry

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Alice')
        self.assertEqual(data[1]['age'], 25)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")

    # Funções avge
    def test_avgAgeCountry_empty_data(self):
        data = []
        result = avgAgeCountry(data)
        self.assertEqual(result, {})

    def test_avgAgeCountry_missing_age(self):
        data = [{"name": "Alice", "country": "US"}]
        result = avgAgeCountry(data)
        self.assertEqual(result, {})

    def test_avgAgeCountry_missing_country(self):
        data = [{"name": "Bob", "age": 30}]
        result = avgAgeCountry(data)
        self.assertEqual(result, {})

    def test_avgAgeCountry_with_transform_func(self):
        data = [{"name": "Charlie", "age": 60, "country": "UK"}]

        # Uma função de transformação simples que converte idade de anos para meses
        def transform_age(age):
            return age * 12

        result = avgAgeCountry(data, transform_func=transform_age)
        self.assertEqual(result, {"UK": 720})

if __name__ == '__main__':
    unittest.main()