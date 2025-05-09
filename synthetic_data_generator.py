"""
synthetic_data_generator.py

A simple, customizable synthetic data generator for marketing (or any) datasets, so you can create a demo data viz with exactly the data you want.
Generates random records based on a user-defined template and exports to CSV.

**CAUTION:** This script produces completely synthetic data for testing, practice and demonstration purposes.
Do NOT treat this output as real or use it to make real-world decisions.

Usage:
    python synthetic_data_generator.py
"""

import random
import pandas as pd
from datetime import datetime, timedelta

def generate_date(start_date, end_date):
    """
    Generate a random datetime between `start_date` and `end_date`.

    Args:
        start_date (datetime): Earliest possible date.
        end_date   (datetime): Latest possible date.

    Returns:
        datetime: A random date within the specified range.
    """
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def generate_marketing_data(fields):
    """
    Create a single record (dict) based on `fields` template.

    Args:
        fields (list of tuples): Each tuple defines a column:
            (name, data_type, *params)
            - data_type 'int': params = (min, max)
            - data_type 'float': params = (min, max)
            - data_type 'str': params = list of valid strings
            - data_type 'date': params = (start_date_str, end_date_str)

    Returns:
        dict: One randomly generated record.
    """
    record = {}
    for field in fields:
        name, data_type, *params = field

        if data_type == 'int':
            # ❗️ Change integer range here:
            record[name] = random.randint(params[0], params[1])

        elif data_type == 'float':
            # ❗️ Change float range here:
            record[name] = round(random.uniform(params[0], params[1]), 2)

        elif data_type == 'str':
            # ❗️ Change list of possible strings here:
            record[name] = random.choice(params)

        elif data_type == 'date':
            # ❗️ Change date range strings here (YYYY-MM-DD):
            start_date = datetime.strptime(params[0], "%Y-%m-%d")
            end_date   = datetime.strptime(params[1], "%Y-%m-%d")
            record[name] = generate_date(start_date, end_date)

        else:
            raise ValueError(f"Unsupported data type: {data_type}")

    return record

def generate_records(field_templates, num_records):
    """
    Generate multiple records according to `field_templates`.

    Args:
        field_templates (list): Schema definition from which to generate data.
        num_records (int): Number of rows to generate.

    Returns:
        list of dicts: All generated records.
    """
    return [generate_marketing_data(field_templates) for _ in range(num_records)]

if __name__ == "__main__":
    # ❗️ Define your dataset schema here. You can:
    #    • Rename fields
    #    • Add or remove fields
    #    • Change datatypes (int, float, str, date)
    #    • Adjust value ranges or choice lists
    field_templates = [
        ('Name',               'str',  'Alice', 'Bob', 'Charlie', 'David', 'Eve'),
        ('Age',                'int',   18,      65),
        ('Email',              'str',  'alice@syntheticdatagen.com', 'bob@syntheticdatagen.com',
                                 'charlie@syntheticdatagen.com', 'david@syntheticdatagen.com', 'eve@syntheticdatagen.com'),
        ('Spending Amount',    'float', 50.0,   1000.0),
        ('Signup Date',        'date',  '2020-01-01',       '2023-01-01'),
        ('Subscription Plan',  'str',  'Free', 'Basic', 'Premium')
    ]

    # ❗️ Set how many records you’d like to generate:
    num_records = 100

    # Generate and convert to DataFrame
    print(f"Generating {num_records} records...")
    data = generate_records(field_templates, num_records)
    df = pd.DataFrame(data)

    # ❗️ Change output filename here if desired:
    output_csv = 'synthetic_marketing_data.csv'
    df.to_csv(output_csv, index=False)
    print(f"Saved synthetic data to {output_csv}")

    # Show a quick preview
    print(df.head())
