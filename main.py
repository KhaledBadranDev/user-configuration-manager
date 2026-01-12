"""
User Configuration Manager
--------------------------
This module allows users to add, update, delete, and view settings.
"""
from typing import Dict, Tuple, Union


# 1. Create a dictionary named test_settings to store user configuration
# We initialize it with some default values for testing purposes.
test_settings = {
    'theme': 'light',
    'wifi': 'on'
}


def add_setting(settings: Dict[str, str], new_setting: Tuple[str, str]) -> str:
    """
    Adds a new setting to the dictionary.
    
    Parameters:
    settings (dict): The dictionary containing user settings.
    new_setting (tuple): A tuple containing (key, value) for the new setting.
    
    Returns:
    str: A success or error message.
    """
    # Unpack the tuple into key and value
    key, value = new_setting
    
    # Convert key and value to lowercase as per requirements
    key = key.lower()
    value = value.lower()
    
    # Check if the key already exists in the dictionary
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    # If key does not exist, add it to the dictionary
    settings[key] = value
    
    # Return success message
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: Dict[str, str], setting: Tuple[str, str]) -> str:
    """
    Updates an existing setting in the dictionary.
    
    Parameters:
    settings (dict): The dictionary containing user settings.
    setting (tuple): A tuple containing (key, value) for the setting to update.
    
    Returns:
    str: A success or error message.
    """
    # Unpack the tuple
    key, value = setting
    
    # Convert key and value to lowercase as per requirements
    key = key.lower()
    value = value.lower()
    
    # Check if key exists in the dictionary
    if key in settings:
        # Update the value
        settings[key] = value
        # Return success message with lowercase key and value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        # Return error if key does not exist
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


if __name__ == "__main__":
    print("--- Testing add_setting ---")
    
    # Test 1: Try to add a setting that already exists (should fail)
    result_exist = add_setting(test_settings, ('THEME', 'dark'))
    print(f"Test 1 (Duplicate): {result_exist}")
    
    # Test 2: Add a new setting (should succeed)
    result_success = add_setting(test_settings, ('volume', 'high'))
    print(f"Test 2 (New): {result_success}")
    
    print("\n--- Testing update_setting ---")
    
    # Test 3: Update an existing key (should succeed)
    # This covers Test requirement #13
    result_update_success = update_setting(test_settings, ('theme', 'dark'))
    print(f"Test 3 (Update Existing): {result_update_success}")
    
    # Test 4: Update a non-existing key (should fail)
    # This covers Test requirement #14
    result_update_fail = update_setting(test_settings, ('brightness', 'low'))
    print(f"Test 4 (Update Missing): {result_update_fail}")
    
    # Verify the dictionary was actually updated
    # This covers Test requirement #15
    print(f"Current Settings State: {test_settings}")