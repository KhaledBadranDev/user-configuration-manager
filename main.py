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


def delete_setting(settings: Dict[str, str], key: str) -> str:
    """
    Deletes a specific setting from the dictionary.
    
    Parameters:
    settings (dict): The dictionary containing user settings.
    key (str): The key of the setting to delete.
    
    Returns:
    str: A success or error message.
    """
    # Convert key to lowercase to ensure case-insensitive matching
    key = key.lower()
    
    # Check if the key exists in the settings dictionary
    if key in settings:
        # Remove the key-value pair
        del settings[key]
        # Return success message
        return f"Setting '{key}' deleted successfully!"
    else:
        # Return error message if key is not found
        return "Setting not found!"
    

def view_settings(settings: Dict[str, str]) -> str:
    """
    Returns a formatted string of all settings.
    
    Parameters:
    settings (dict): The dictionary containing user settings.
    
    Returns:
    str: A formatted string of settings or a message if empty.
    """
    # Check if dictionary is empty
    if not settings:
        return "No settings available."
    
    # Initialize the output string
    output = "Current User Settings:\n"
    
    # Loop through the settings dictionary
    for key, value in settings.items():
        # Capitalize the key for display (e.g., 'theme' -> 'Theme')
        formatted_key = key.capitalize()
        # Append the formatted string "Key: value" followed by a newline
        output += f"{formatted_key}: {value}\n"
    
    return output


if __name__ == "__main__":
    print("--- Testing add_setting ---")
    print(add_setting(test_settings, ('THEME', 'dark')))
    print(add_setting(test_settings, ('volume', 'high')))
    
    print("\n--- Testing update_setting ---")
    print(update_setting(test_settings, ('theme', 'light')))
    
    print("\n--- Testing delete_setting ---")
    print(delete_setting(test_settings, 'volume'))
    
    print("\n--- Testing view_settings ---")
    
    # Test 7: View populated settings (should show Theme and Wifi)
    # This covers Test requirements #25, #26, #27
    print("Scenario 1: Viewing populated settings")
    print(view_settings(test_settings))
    
    # Test 8: View empty settings (should show "No settings available.")
    # This covers Test requirement #24
    print("Scenario 2: Viewing empty settings")
    # Create a temporary empty dictionary for this test
    empty_settings = {}
    print(view_settings(empty_settings))