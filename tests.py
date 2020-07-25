from Calculator import PriceAccumulator
from Sender import Sender
from Parser import Parser
import unittest
import json
import os


class Tests(unittest.TestCase):
    def test_read_file_data(self):
        # Create and save sample json
        sample_json = {
            'name': 'John',
            'shares': 100,
            'price': 1230.23
        }

        temp_filename = 'temp.json'
        with open(temp_filename, 'w') as f:
            json.dump(sample_json, f)

        # Read sample json file with parser
        P = Parser(temp_filename)
        self.assertEqual(P.get_data(), sample_json)

        # Remove temporary json file
        os.remove(temp_filename)

    def test_calculate_price_positive(self):
        sample_groundtruth = {'name' : 'cycle1', 'date' : '2013-01-06', 'frame': 111, 'wheel': 163, 'seat': 82, 'handlebar': 133, 'chain': 162, 'total': 651, 'status' : 'Found'}

        # Positive sample data
        sample_input_json_positive = {
            "date" : "2013-01-06",
            "name" : "cycle1",
            "components" : {
                "frame" : ["top_tube", "down_tube", "seat_tube"],
                "wheel" : ["spokes", "hub", "rim"],
                "seat" : ["saddle"],
                "handlebar" : ["handlebar_grip", "fork"],
                "chain" : ["chain", "chain_rings"]
            }
        }

        sample_response_json_positive = {
            'message': 'Here are the details',
            'Pricing': {
                'id': 6,
                'date': '2013-01-06',
                'top_tube': 24, 'down_tube': 71, 'seat_tube': 16, 'seat_stay': 27,
                'chain_stay': 91, 'spokes': 17, 'hub': 52, 'rim': 94, 'tire': 42,
                'valve': 29, 'saddle': 82, 'seat_post': 56, 'handlebar_grip': 70,
                'head_tube': 45, 'shock_absorber': 70, 'front_brakes': 70, 'fork': 63,
                'chain': 76, 'chain_rings': 86, 'pedal': 94, 'crank_arm': 62
            }
        }

        C = PriceAccumulator()
        self.assertEqual(C.calculate_price(sample_input_json_positive, sample_response_json_positive), sample_groundtruth)

    def test_calculate_price_negative(self):
        sample_groundtruth = {'name' : 'cycle1', 'date' : '2013-01-06', 'frame': 111, 'wheel': 163, 'seat': 82, 'handlebar': 133, 'chain': 162, 'total': 651}

        # Negative sample data
        sample_input_json_negative = {
            "date": "2014-05-08",
            "name": "cycle1",
            "components": {
                "frame": ["top_tube", "down_tube", "seat_tube"],
                "wheel": ["spokes", "hub", "rim"],
                "seat": ["saddle"],
                "handlebar": ["handlebar_grip", "fork"],
                "chain": ["chain", "chain_rings"]
            }
        }

        sample_response_json_negative = {
            'message': 'Here are the details',
            'Pricing': {
                'id': 88,
                'date': '2013-01-06',
                'top_tube': 56, 'down_tube': 71, 'seat_tube': 16, 'seat_stay': 27,
                'chain_stay': 79, 'spokes': 17, 'hub': 52, 'rim': 94, 'tire': 12,
                'valve': 29, 'saddle': 56, 'seat_post': 56, 'handlebar_grip': 70,
                'head_tube': 45, 'shock_absorber': 70, 'front_brakes': 50, 'fork': 63,
                'chain': 76, 'chain_rings': 16, 'pedal': 94, 'crank_arm': 62
            }
        }

        C = PriceAccumulator()
        self.assertNotEqual(C.calculate_price(sample_input_json_negative, sample_response_json_negative), sample_groundtruth)

    def test_sender_positive(self):
        sample_input_json = {
            "date": "2013-01-06",
            "name": "cycle1",
            "components": {
                "frame": ["top_tube", "down_tube", "seat_tube"],
                "wheel": ["spokes", "hub", "rim"],
                "seat": ["saddle"],
                "handlebar": ["handlebar_grip", "fork"],
                "chain": ["chain", "chain_rings"]
            }
        }

        S = Sender()
        self.assertEqual(S.test_fetch(sample_input_json).status_code, 200)

    def test_sender_negative(self):
        sample_input_json = {
            "date": "2020-08-09",
            "name": "cycle1",
            "components": {
                "frame": ["top_tube", "down_tube", "seat_tube"],
                "wheel": ["spokes", "hub", "rim"],
                "seat": ["saddle"],
                "handlebar": ["handlebar_grip", "fork"],
                "chain": ["chain", "chain_rings"]
            }
        }

        S = Sender()
        self.assertEqual(S.test_fetch(sample_input_json).status_code, 500)

