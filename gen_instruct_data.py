import pandas as pd
import json

# Function to create a formatted text row


def create_text_row(instruction, output, input):
    text_row = f"""<s>[INST] {instruction} Here is the user's request: {input} [/INST] \\n {output} </s>"""
    return text_row

# Read the Excel file


# Read the Excel file from a specific sheet
def read_excel_file(excel_file_path, sheet_name):
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    print(df)
    return df['Inputs'].tolist()
# Read the JSON list


def read_json_list(json_file_path):
    with open(json_file_path, 'r') as file:
        json_list = json.load(file)
    return {item['text'] for item in json_list}

# Process and write the JSONL file


def process_jsonl_file(output_file_path, excel_inputs, json_data):
    with open(output_file_path, "w") as output_jsonl_file:
        for input, output in zip(excel_inputs, json_data):
            # output = json_data.get(input, {}).get('output', '')
            # Replace with your actual instruction
            instruction = 'Generate accurate and correct ManimCE Python code for the animation requested by the user.'
            json_object = {
                "text": create_text_row(instruction, output, input),
                "instruction": instruction,
                "input": input,
                "output": output
            }
            output_jsonl_file.write(json.dumps(json_object) + "\n")


# File paths
excel_file_path = './master_finetune_datasheet_copy.xlsx'
json_file_path = './instructgen/final_combined_animation_data.json'
output_file_path = './instructgen/final_training_dataset.jsonl'

# Read data
excel_inputs = read_excel_file(excel_file_path, "Generated Input")
json_data = read_json_list(json_file_path)
# print(json_data)

# Process and write to JSONL
process_jsonl_file(output_file_path, excel_inputs, json_data)
