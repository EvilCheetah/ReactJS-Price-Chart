from os import getenv
from pathlib import Path
from dotenv import load_dotenv


def config():
    load_dotenv()

    _check_env_variables()
    _create_necessary_directories()


#-------------------------- Private Functions --------------------------#

def _check_env_variables():
    '''
    Checks presence of all env variables
    '''
    if ( not getenv('OUTPUT_DIRECTORY') ):
        raise ValueError("You didn't specify 'OUTPUT_DIRECTORY' in .env file")

    if ( not getenv('OUTPUT_FILENAME') ):
        raise ValueError("You didn't specify 'OUTPUT_FILENAME' in .env file")


def _create_necessary_directories():
    '''
    Creates 'OUTPUT_DIRECTORY' in case it doesn't exist
    '''
    if ( not Path(getenv('OUTPUT_DIRECTORY')).is_dir() ):
        Path(getenv('OUTPUT_DIRECTORY')).mkdir(parents = True, exist_ok = True)