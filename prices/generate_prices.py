from os import getenv
from random import randrange, uniform
from faker import Faker

from prices.platforms import PLATFORMS


def generate_prices() -> list[dict]:
    fake = Faker('en_US')

    return [
        {
            'id':        fake.uuid4(),
            'platform':  platform,
            'amount':    round( uniform(20.00, 200.00), 2),
            'timestamp': fake.date_time_this_decade(before_now = True).isoformat()

        }
        for _ in range( _get_randrange() )
        for platform in PLATFORMS
    ]


#-------------------------- Private Functions --------------------------#
def _get_randrange() -> int:
    return randrange(
        int( getenv('MIN_NUMBER_OF_ENTRIES_PER_PLATFORM') ),
        _get_maximum_range()
    )


def _get_maximum_range() -> int:
    '''
    Either returns:
        - MAX
        - MIN + 1, if MAX is absent
    '''
    if (not getenv('MAX_NUMBER_OF_ENTRIES_PER_PLATFORM')):
        return (
            int( getenv('MIN_NUMBER_OF_ENTRIES_PER_PLATFORM') ) + 1
        )
    
    return int( getenv('MAX_NUMBER_OF_ENTRIES_PER_PLATFORM') )