from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


class Sender:
    def __init__(self):
        self.__accumulator = []

    def __fetch(self, input_json_data):
        request_data = {
            'date': input_json_data['date'],
        }

        url = 'http://localhost:8000/getprice/'
        response = requests.post(url, data=request_data)

        return response

    def test_fetch(self, input_json_data):
        return self.__fetch(input_json_data)

    def __fetch_and_calculate_price(self, input_json_data, priceAccumObj):
        response = self.__fetch(input_json_data)
        if response.status_code != 200:
            return {
                'name' : input_json_data['name'],
                'date' : input_json_data['date'],
                'status' : 'Not Found'
            }

        return priceAccumObj.calculate_price(input_json_data, response.json())

    def run(self, input_json_data, price_accum_obj):
        with ThreadPoolExecutor(max_workers=10) as executor:
            threads = []
            for json_data in input_json_data['data']:
                threads.append(executor.submit(self.__fetch_and_calculate_price, json_data, price_accum_obj))

            for task in as_completed(threads):
                print(task.result())

