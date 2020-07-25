class PriceAccumulator:

    @staticmethod
    def calculate_price(input_json_data, response_json_data):
        price_json = {
            'name' : input_json_data['name'],
            'date' : input_json_data['date'],
        }

        total_price = 0
        for component in input_json_data['components']:
            component_price = 0
            for part in input_json_data['components'][component]:
                component_price += response_json_data['Pricing'][part]
            total_price += component_price
            price_json[component] = component_price

            # print('Price of ' + component + ' ' + str(component_price))
            # print('Total price of cycle = ' + str(total_price))

        price_json['total'] = total_price
        price_json['status'] = 'Found'

        return price_json
