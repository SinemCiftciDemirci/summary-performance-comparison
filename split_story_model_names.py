import pandas as pd
import os

# Original Excel file
input_file = './metrics/Model_Performance.xlsx'
output_file = './metrics/Model_Performance_Updated.xlsx'

# Load Excel data
df = pd.read_excel(input_file)

# Function to correctly parse file names into story and model names
def parse_file_name(file_name):
    try:
        # Split by "__" to get Story Name, Model Name, and Timestamp
        parts = file_name.rsplit("__", maxsplit=2)

        if len(parts) == 3:  # Expecting: StoryName, ModelName, Timestamp
            story_name = parts[0].replace('_', ' ').strip()
            model_name = parts[1].replace('_', '/').strip()
            return story_name, model_name
        else:
            return file_name.replace('_', ' '), "Unknown"  # Fallback if format is incorrect
    except Exception as e:
        print(f"Error parsing {file_name}: {e}")
        return "Unknown", "Unknown"

# Apply parsing function to create new columns
df[['Story Name', 'Model Name']] = df['File Name'].apply(lambda x: pd.Series(parse_file_name(x)))

# Reorder columns (Story Name and Model Name at the front)
cols = ['Story Name', 'Model Name'] + [col for col in df.columns if col not in ['Story Name', 'Model Name']]
df = df[cols]

# Save updated DataFrame to new Excel file
df.to_excel(output_file, index=False)

print(f"Updated Excel file saved as '{output_file}'")
