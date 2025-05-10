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

# You can embed custom business logic here to create realistic dependencies
# between fields. For example, below we tie the 'Spending Amount' distribution
# directly to the chosen 'Subscription Plan', so Premium users spend more on average.

def generate_marketing_data(fields):
    record = {}

    # 1) First pass: pick your plan
    for name, data_type, *params in fields:
        if name == 'Subscription Plan':
            record[name] = random.choice(params)
            break

    # 2) Second pass: generate everything else
    for name, data_type, *params in fields:
        if name == 'Subscription Plan':
            continue

        if name == 'Spending Amount':
            plan = record['Subscription Plan']
            if plan == 'Free':
                record[name] = round(random.uniform(0, 100), 2)
            elif plan == 'Basic':
                record[name] = round(random.uniform(50, 300), 2)
            else:  # Premium
                record[name] = round(random.uniform(200, 1000), 2)

        elif data_type == 'int':
            record[name] = random.randint(params[0], params[1])

        elif data_type == 'float':
            record[name] = round(random.uniform(params[0], params[1]), 2)

        elif data_type == 'str':
            record[name] = random.choice(params)

        elif data_type == 'date':
            start = datetime.strptime(params[0], "%Y-%m-%d")
            end   = datetime.strptime(params[1], "%Y-%m-%d")
            record[name] = generate_date(start, end)

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
