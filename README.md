# UEIC IY499 Introduction to Programming - Algorithm Portfolio

## Student Information

- **Name:** Fatih Sina Dilek
- **Course:** IY499 Introduction to Programming
- **Institution:** UEIC

## Project Description

This project implements a data processing system that demonstrates various algorithmic operations on JSON data. The system supports three main operations:

1. **Sorting Algorithm**: Implementation of bubble sort with both ascending and descending capabilities
2. **Filtering Algorithm**: Filters data based on specific key-value pairs
3. **Aggregation Algorithm**: Performs statistical analysis on numeric and categorical data

## Features

- Dynamic JSON file loading with error handling
- Interactive command-line interface
- Support for multiple data types (strings and numbers)
- Statistical operations including:
  - Average (for numeric data)
  - Sum (for numeric data)
  - Maximum and minimum values
  - Frequency counting (for categorical data)

## Setup Instructions

1. Ensure you have Python installed on your system
2. Place your JSON data file in the same directory as `main.py`
3. The JSON file should contain an array of objects with consistent keys

## Usage

1. Run the program:

   ```bash
   python main.py
   ```

2. When prompted, either:
   - Press Enter to use the default `data.json` file
   - Enter a custom JSON filename
3. Choose from available operations:
   - Enter 1 or "sorting" for sorting operations
   - Enter 2 or "filtering" for filtering operations
   - Enter 3 or "aggregation" for aggregation operations
4. Follow the prompts to:
   - Select the primary key for operation
   - Provide additional parameters as needed
   - Choose whether to perform another operation

## Input Data Requirements

- The input JSON file must contain an array of objects
- All objects should have consistent keys
- Supports both numeric and string data types

## Implementation Details

- **Sorting**: Uses bubble sort algorithm with optimization for early termination
- **Filtering**: Case-insensitive string matching
- **Aggregation**:
  - For numeric data: calculates average, sum, max, and min
  - For string data: determines frequency, most common value, max, and min

## Error Handling

- Validates JSON file existence and format
- Handles invalid user inputs gracefully
- Provides clear error messages for troubleshooting

## Contact

You can use github to reach me for inqureys.

## License

This project is created for educational purposes as part of the IY499 Introduction to Programming course.
