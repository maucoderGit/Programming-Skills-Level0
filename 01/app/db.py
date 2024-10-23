import os
import json

from pydantic import BaseModel
import importlib.util
import inspect
from pathlib import Path


def get_all_table_names():
    # Get the path to the models package
    models_dir = Path(__file__).parent / 'models'

    # Initialize a list to store table names
    table_names = []

    # Iterate through all Python files in the models directory
    for file in models_dir.glob('*.py'):
        # Skip __init__.py files
        if file.name == '__init__.py':
            continue
        
        # Construct the full path to the module
        spec = importlib.util.spec_from_file_location(file.stem, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Find all classes in the module
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, BaseModel):
                # Check if the class has a _table_name attribute
                if hasattr(obj, '_table_name'):
                    table_names.append((name, getattr(obj, '_table_name')))

    return table_names

def init_json_db_files(table: str) -> None:
    """Check if json file exists, if not create a new empty json file for table records"""
    if os.path.exists(f"{table}.json"):
        return

    with open(f"{table}.json", 'w') as file:
        json.dump([], file, indent=4)

def get_records_from_json_file(table: str) -> list:
    """Get records list from json file"""
    with open(f"{table}.json", "r") as file:
        return json.loads(file.read())

def update_json_file(table: str, values: list):
    """Overwrite JSON file"""
    with open(f"{table}.json", 'w') as file:
        json.dump(values, file, indent=4)
