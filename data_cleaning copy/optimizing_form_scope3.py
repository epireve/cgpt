import json

# Load the provided JSON file
file_path = 'json/form_scope3.json'
# print(file_path)

with open(file_path, 'r') as file:
    data = json.load(file)

# Display a snippet of the loaded data for examination
data_snippet = json.dumps(data, indent=4)[:500]  # Display first 500 characters
# print(data_snippet)


def flatten_structure(data):
    """
    Flatten the structure by moving common fields like dates and IDs to category level.
    Also creates global lookups for dropdowns and uses codes for IDs and keys.
    """
    # Global lookups for dropdown options and common fields
    global_lookups = {
        "dropdown_options": {},
        "common_fields": {}
    }

    # Iterate through the categories and sub-categories
    for category, sub_categories in data["Scope3Activity"].items():
        for sub_category, details in sub_categories.items():
            if "fields" in details:
                new_fields = []
                for field in details["fields"]:
                    # Move common fields to global lookup
                    if field['label'] in ["Date", "Source ID"]:
                        if field['label'] not in global_lookups["common_fields"]:
                            global_lookups["common_fields"][field['label']] = field
                    else:
                        # Handle dropdown options
                        if field.get('type', '') == 'dropdown':
                            dropdown_id = field.get('variable', '')
                            if dropdown_id and dropdown_id not in global_lookups["dropdown_options"]:
                                global_lookups["dropdown_options"][dropdown_id] = field["options"]
                                # Replace options with reference to global lookup
                                field["options"] = f"global_lookup:{dropdown_id}"
                        new_fields.append(field)
                # Update fields with modified list
                sub_categories[sub_category]["fields"] = new_fields

    return {
        "global_lookups": global_lookups,
        "Scope3Activity": data["Scope3Activity"]
    }

# Flatten the JSON structure
flattened_data = flatten_structure(data)

# Display a snippet of the modified data for verification
flattened_data_snippet = json.dumps(flattened_data, indent=4)[:500]  # Display first 500 characters
print(flattened_data_snippet)

# Save the modified data to a file
output_file_path = 'json/flattened_form_scope3.json'
with open(output_file_path, 'w') as output_file:
    json.dump(flattened_data, output_file, indent=4)
