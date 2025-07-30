import json

def read_json(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []  
    return data


def create_entry(filepath, new_obj):
    data= read_json(filepath)
    data.append(new_obj)
    with open(filepath, "w") as file:
        json.dump(data, file)  
    print("Entry added successfully.")

def update_entry(filepath, name_to_update, updated_obj):
    data = read_json(filepath)
    for i, obj in enumerate(data):
        if obj.get("name")== name_to_update:
            data[i].update(updated_obj)
            with open(filepath, "w") as f:
                json.dump(data, f)
            print(f"Entry with name '{name_to_update}' updated.")
            return
    print(f"No entry found with name '{name_to_update}'.")

def delete_entry(filepath, name_to_delete):
    data = read_json(filepath)  
    for i, obj in enumerate(data):
        if obj.get("name") == name_to_delete:
            del data[i]  
            with open(filepath, "w") as f:
                json.dump(data, f) 
            print(f"Entry with name '{name_to_delete}' deleted.")
            return
    print(f"No entry found with name '{name_to_delete}'.")





filepath = "file.json"

# Create new entry
create_entry(filepath, {"name": "Sneha", "department": "HR"})

# Update entry
update_entry(filepath, "Sneha", {"department": "Devops"})
# Delete entry
delete_entry(filepath, "Sneha")
# Read all entries
all_data = read_json(filepath)
print(all_data)