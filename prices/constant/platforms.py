from typing import get_args
from prices.types.platform import Platform


PLATFORMS = list( get_args(Platform) )