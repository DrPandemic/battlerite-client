"""
Contains all the helper functions that are not tied to a specific module.
"""
from typing import Dict

def find_node(data: [Dict], id_value: str) -> Dict:
    """
    Find a specific node from a response.
    If not found, KeyError is raised.
    """
    for node in data['included']:
        if node.get('id', None) == id_value:
            return node
    raise KeyError(id_value)
