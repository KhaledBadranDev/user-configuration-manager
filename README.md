# User Configuration Manager

This is a Python application designed to manage user preferences (like themes, wifi settings, or volume levels). It stores settings in a dictionary and ensures all data is handled consistently.

## Features & Logic

* **Add Settings:** Add new key-value pairs. It automatically converts keys to lowercase (e.g., 'THEME' becomes 'theme') and prevents duplicates.
* **Update Settings:** Change the value of an existing setting. It warns you if you try to update a setting that doesn't exist.
* **Delete Settings:** Remove a specific setting by its key.
* **View Settings:** Displays all current settings in a clean, capitalized format (e.g., `Theme: dark`).

## Test Scenarios

When running the script, it automatically tests the following scenarios to ensure robustness:

1. **Adding:**
   * Successfully adding a new setting (`volume`).
   * Blocking an attempt to add a duplicate setting (`theme`).
2. **Updating:**
   * Successfully updating an existing setting.
   * Showing an error when trying to update a missing key.
3. **Deleting:**
   * Successfully removing a setting.
   * Handling cases where the setting to delete is not found.
4. **Viewing:**
   * Displaying a formatted list of active settings.
   * Handling empty lists by showing "No settings available."

## How to Run

1. Ensure you have Python installed.
2. Run the script in your terminal:
   ```bash
   python main.py
   ```

## License

This project is licensed under the [MIT License](LICENSE).
