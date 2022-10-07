from random import randrange, uniform
from faker import Faker

from prices.platforms import PLATFORMS


def generate_prices(
    min_entries_per_platform: int = 0,
    max_entries_per_platform: int = None
) -> list[dict]:
    if ( not max_entries_per_platform ):
        max_entries_per_platform = min_entries_per_platform
    
    if ( min_entries_per_platform > max_entries_per_platform):
        raise ValueError("'max_entries_per_platform' MUST be greater or equal to the 'min_entries_per_platform'")

    fake = Faker('en_US')

    return [
        {
            'id':        fake.uuid4(),
            'platform':  platform,
            'amount':    round( uniform(20.00, 200.00), 2),
            'timestamp': fake.date_time_this_decade(before_now = True)

        }
        for _ in range( randrange(min_entries_per_platform, max_entries_per_platform + 1) )
        for platform in PLATFORMS
    ]