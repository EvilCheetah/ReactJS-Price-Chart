from pprint import pprint
from config import config
from prices.generate_prices import generate_prices
from prices.save import save_data


def main():
    config()
    data = generate_prices(20)
    save_data(data)


if __name__ == '__main__':
    try:
        main()
    
    except KeyboardInterrupt:
        print('Program was terminated...')