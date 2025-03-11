import json

# Constant array that contains acceptable input for "yes"
APPROVE_ARRAY = ["y", "yes", 1, "1"]
# Constant array that contains acceptable input for "no"
DISAPPROVE_ARRAY = ["n", "no", 2, "2"]

# Try's to load the data normal value is "data" + .json


def load_data_from_json(default_filename="data.json"):
    while True:
        try:
            filename = input(
                f"Enter JSON filename (default: {default_filename}): "
            ).strip()
            if filename == "":  # Use default if no input is given
                filename = default_filename
            # Ensure the file extension is .json
            elif not filename.endswith(".json"):
                filename += ".json"

            with open(filename, "r") as json_data:
                data = json.load(json_data)
                print(f"Your data has been loaded successfully from {filename}.")
                return data
        except FileNotFoundError:
            print(f"Error: Could not find the file '{filename}'. Please try again.")


data = load_data_from_json()


# Map's of the valid operations and primary keys
operation_mapping = {
    "sorting": "sorting algorithm",
    "filtering": "filtering algorithm",
    "aggregation": "aggregation algorithm",
    "1": "sorting algorithm",
    "2": "filtering algorithm",
    "3": "aggregation algorithm",
}

# Function to get operation from user input


def get_operation():
    print("\nAvailable operations:")
    print("1. sorting/sorting algorithm")
    print("2. filtering/filtering algorithm")
    print("3. aggregation/aggregation algorithm")
    operation = input("Enter operation (number or name): ").lower().strip()
    # Normalizes the operation token so we don't need 1:1 token matching
    normalized_operation = operation_mapping.get(operation)
    return (
        normalized_operation
        if normalized_operation in set(operation_mapping.values())
        else None
    )


# Function to get primary key from user input


def get_primary_key():
    # Generate a consistent list of keys based on the dataset
    # Order is consistent as it comes from the dictionary structure
    all_keys = list(data[0].keys())

    print("\nAvailable keys:")
    for i, key in enumerate(all_keys, 1):
        print(f"{i}. {key}")
    print(
        "Enter the number corresponding to the key, or the exact key (case-sensitive):"
    )

    # Get user input
    pk = input("Enter your choice: ").strip()

    # Check if input is numeric and corresponds to a valid key
    if pk.isdigit() and 1 <= int(pk) <= len(all_keys):
        return all_keys[int(pk) - 1]  # Return the corresponding key

    # Otherwise, assume it's a key name and validate it
    if pk in all_keys:
        return pk

    print(f"Invalid choice '{pk}'. Please select a valid number or key.")
    return None


# Function to get additional parameters based on operation type


def get_additional_params(operation, pk):
    if operation in ["sorting algorithm", "sorting"]:
        # Get sorting order
        order = (
            input("Would you like to sort in descending order? (y/n): ").lower().strip()
        )
        return 1 if order.lower() in ["y", "yes", 1, "1"] else 0
    elif operation in ["filtering algorithm", "filtering"]:
        # Get filter value
        return input(f"Enter value to filter by for {pk}: ").strip()
    return None


# Bubble sort implementation for sorting the data


def bubble_sort(data, key, order=0):
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            # Compare and swap based on key type (string or numeric)
            if (
                isinstance(data[j][key], str)
                and data[j][key].lower() > data[j + 1][key].lower()
            ) or (
                isinstance(data[j][key], (int, float))
                and data[j][key] < data[j + 1][key]
            ):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:  # Check if it is swapped, if not break it early
            break
    # Return reversed list if order is 1
    return reverse_list(data) if order == 1 else data


# Function to filter the data based on key and value


def filter_list(data, key, value):
    filtered_list = []
    for item in data:
        if str(item[key]).lower() == str(value).lower():  # Case-insensitive comparison
            filtered_list.append(item)
    return filtered_list


# Function to calculate average value for a specific key


def aggregate(data, key):
    if not data:
        print("No data to aggregate.")
        return None

    # Collect valid entries (skip None values)
    valid_entries = [
        item[key] for item in data if key in item and item[key] is not None
    ]

    if not valid_entries:
        print(f"No valid data found for key '{key}'.")
        return None

    # Detect data type
    value_type = type(valid_entries[0])

    if value_type in [int, float]:  # Numeric data
        numeric_data = [
            item for item in valid_entries if isinstance(item, (int, float))
        ]
        if not numeric_data:
            print(f"No numeric data found for key '{key}'.")
            return None

        return {
            "Average": round(sum(numeric_data) / len(numeric_data), 2),
            "Max": max(numeric_data),
            "Min": min(numeric_data),
        }

    elif value_type is str:  # String data (categorical)
        value_counts = {}
        for value in valid_entries:
            if isinstance(value, str):
                value_counts[value] = value_counts.get(value, 0) + 1

        if not value_counts:
            print(f"No valid string data found for key '{key}'.")
            return None

        return {
            "Most Frequent": max(value_counts, key=value_counts.get),
            "Max ": max(value_counts.keys()),
            "Min ": min(value_counts.keys()),
            "Occurrences": value_counts,
        }

    else:
        print(f"Cannot aggregate data of type '{value_type}' for key '{key}'.")
        return None


def print_aggregation_result(result):
    if not result:
        print("No aggregation results to display.")
        return

    print("\nAggregation Results:")

    # Handle dictionary results with better formatting
    for key, value in result.items():
        if isinstance(value, dict):  # If it's occurrences of categories
            print(f"{key}:")
            for sub_key, count in value.items():
                print(f"   {sub_key}: {count}")
        else:
            print(f"{key}: {value}")


# Function to pretty print the data in a readable format
def pretty_print(data):
    if not data:
        print("No data to display")
        return

    # Get all possible keys from the first item
    keys = data[0].keys()

    # Print each item with all its key-value pairs
    for item in data:
        # Build the output string dynamically
        output_parts = []
        for key in keys:
            # Format the key name (capitalize words, replace underscores)
            formatted_key = key.title().replace("_", " ")
            # Get and format the value
            value = item.get(key, "N/A")
            output_parts.append(f"{formatted_key}: {value}")

        # Join all parts with commas and print
        print(", ".join(output_parts))


# Function to reverse a list (used for sorting in reverse order)


# used input_list as an internal var in order to not confuse with list function of python
def reverse_list(input_list):
    return list(reversed(input_list))


# Main function to handle user interaction


def main():
    while True:  # Keep running until user wants to exit
        operation = get_operation()
        if not operation:
            print("Invalid operation, please try again")
            continue

        pk = get_primary_key()
        if not pk:
            print("Invalid primary key, please try again")
            continue

        # Get additional parameters and perform the selected operation
        value = get_additional_params(operation, pk)
        sorted_list = bubble_sort(data, pk)  # Always start with a sorted list

        # Execute the appropriate operation based on user input
        if operation in ["sorting algorithm"]:
            if value == 1:
                sorted_list = reverse_list(sorted_list)
            pretty_print(sorted_list)
        elif operation in ["filtering algorithm"]:
            filtered_list = filter_list(sorted_list, pk, value)
            pretty_print(filtered_list)
        elif operation in ["aggregation algorithm"]:
            result = aggregate(sorted_list, pk)
            print_aggregation_result(result)

        # Ask if user wants to perform another operation
        perform_another_operation = input(
            "\nWould you like to perform another operation? (y/n): "
        ).lower()
        if perform_another_operation.lower() in APPROVE_ARRAY:
            continue

        elif perform_another_operation.lower() in DISAPPROVE_ARRAY:
            exit_opt = 0
            exit_opt_confirm = input("Are you sure you want to exit ? (y/n)")

        if exit_opt_confirm.lower() in APPROVE_ARRAY and exit_opt == 0:
            break


if __name__ == "__main__":
    main()
