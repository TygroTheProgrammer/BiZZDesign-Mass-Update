# Mass Update Script

## Overview

Welcome to the **Mass Update Script** project! This tool is designed to help you efficiently update large amounts of data in a structured and automated way. It leverages the BiZZDesign API to locate and update specific data blocks based on your input criteria. This script is ideal for managing and modifying structured data at scale.

## What Does It Do?

The Mass Update Script automates the process of finding and updating specific data blocks in a database or system. It uses the BiZZDesign API to:

- Locate objects that meet specific criteria.
- Update or create data blocks with new values.
- Process updates in bulk using a CSV file as input.

This is especially useful for tasks like:

- Updating attributes of application components in a repository.
- Managing large-scale changes to structured data.
- Ensuring consistency across data blocks.

## How Does It Work?

1. **Input Your Data**: Prepare a CSV file (`map.csv`) with the following structure:
   - The first row specifies the attribute to search for and the attribute to update.
   - Subsequent rows contain the values to search for and the corresponding new values.

2. **Define Your Updates**: The script reads the CSV file and uses the BiZZDesign API to locate objects matching the search criteria.

3. **Run the Script**: The script updates existing data blocks or creates new ones if they don't exist.

4. **Review the Results**: The script outputs logs to help you verify the updates.

## Why Use This Tool?

- **Integration with BiZZDesign**: Seamlessly interacts with the BiZZDesign API for efficient data management.
- **Automation**: Eliminates manual updates by processing data in bulk.
- **Flexibility**: Handles both updates to existing data blocks and creation of new ones.

## Who Is This For?

This tool is designed for professionals who use BiZZDesign and need to manage large datasets efficiently. While some familiarity with CSV files and structured data is helpful, the script is user-friendly and does not require programming knowledge.

## Getting Started

To get started, follow these steps:

1. **Set Up Your Environment**:
   - Create a `.env` file with the following variables:
     - `BASE_URL`: The base URL for the BiZZDesign API.
     - `CLIENT_ID`: Your client ID for authentication.
     - `CLIENT_SECRET`: Your client secret for authentication.
     - `AUTH_URL`: The URL for obtaining an access token.

2. **Prepare Your CSV File**:
   - Create a `map.csv` file with the structure described above.

3. **Run the Script**:
   - Execute the script using Python. It will process the CSV file and apply the updates.

4. **Verify the Results**:
   - Check the output logs to ensure the updates were applied correctly.

## Example CSV File

```
find_attribute,update_attribute
current_value,new_value
example_find_value,example_update_value
```

## Notes

- Ensure your `.env` file is correctly configured before running the script.
- The script uses the `requests` library for API calls and `jmespath` for JSON parsing.

If you have any questions or need assistance, feel free to reach out to the project team. We're here to help!

---

Thank you for using the Mass Update Script. We hope it simplifies your data management tasks!
