from os import getenv
from pathlib import Path
from dotenv import load_dotenv


def config() -> None:
    load_dotenv()

    _check_env_variables()
    _check_variable_types()
    _create_necessary_directories()


#-------------------------- Private Functions --------------------------#

def _check_env_variables() -> None:
    '''
    Checks presence of all necessary env variables
    '''
    if ( not getenv('OUTPUT_DIRECTORY') ):
        raise ValueError("You didn't specify 'OUTPUT_DIRECTORY' in .env file")

    if ( not getenv('OUTPUT_FILENAME') ):
        raise ValueError("You didn't specify 'OUTPUT_FILENAME' in .env file")
    
    if ( not getenv('MIN_NUMBER_OF_ENTRIES_PER_PLATFORM') ):
        raise ValueError("You didn't specify 'MIN_NUMBER_OF_ENTRIES_PER_PLATFORM' in .env file")
    

def _check_variable_types() -> None:
    '''
    Checks the type of all 
    '''
    if ( not getenv('MIN_NUMBER_OF_ENTRIES_PER_PLATFORM').isdigit() ):
        raise ValueError("'MIN_NUMBER_OF_ENTRIES_PER_PLATFORM' MUST be non-negative")
    
    if (
        _is_max_present() and
        not getenv('MAX_NUMBER_OF_ENTRIES_PER_PLATFORM').isdigit()
    ):
        print(f':{getenv("MAX_NUMBER_OF_ENTRIES_PER_PLATFORM")}:')
        raise ValueError("'MAX_NUMBER_OF_ENTRIES_PER_PLATFORM' MUST be non-negative")
    
    if (
        _is_max_present() and
        int(getenv('MIN_NUMBER_OF_ENTRIES_PER_PLATFORM')) > int(getenv('MAX_NUMBER_OF_ENTRIES_PER_PLATFORM'))
    ):
        raise ValueError(
            "'MAX_NUMBER_OF_ENTRIES_PER_PLATFORM' "
            "MUST greater or equal(>=) to "
            "'MIN_NUMBER_OF_ENTRIES_PER_PLATFORM'"
        )


def _is_max_present() -> bool:
    return ( getenv('MAX_NUMBER_OF_ENTRIES_PER_PLATFORM') )


def _create_necessary_directories() -> None:
    '''
    Creates 'OUTPUT_DIRECTORY' in case it doesn't exist
    '''
    if ( not Path(getenv('OUTPUT_DIRECTORY')).is_dir() ):
        Path(getenv('OUTPUT_DIRECTORY')).mkdir(parents = True, exist_ok = True)