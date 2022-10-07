from pprint import pprint
from config import config
from prices.generate_prices import generate_prices
from prices.save import save_data


def main():
    config()
    
    save_data( generate_prices() )


if __name__ == '__main__':
    try:
        main()
    
    except KeyboardInterrupt:
        print('Program was terminated...')