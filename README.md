# Synthetic Data Generator 📊
## Create Synthetic Datasets for Data Visualization

Primarily created for practising data visualizations, this is a simple, customizable Python script to generate fully synthetic marketing (or any) datasets for testing, development, and demonstration purposes. This project is designed to be easy to use and highly adaptable—perfect for developers, aspiring data scientists, and educators.

---

## ⚠️ Caution

> **This data is 100% synthetic.** Do **NOT** treat it as real customer information or use it for decision-making in production environments.

---

## ✨ Features

* **Flexible Schema**: Define any fields (integers, floats, strings, dates).
* **Customizable Ranges**: Easily set value ranges or categorical options.
* **Custom Business Logic: Embed conditional and functional relationships between fields for realistic data patterns.
* **Quick Setup**: Minimal dependencies (Python + pandas).
* **Instant Preview**: Prints a sample of generated data.
* **CSV Export**: Outputs to CSV for easy integration.

---

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/synthetic-data-generator.git
   cd synthetic-data-generator
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\\Scripts\\activate   # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install pandas
   ```

---

## 🚀 Usage

1. **Customize the schema** in `synthetic_data_generator.py` under the `field_templates` section.

2. **Set the number of records** by modifying the `num_records` variable.

3. **Run the script**:

   ```bash
   python synthetic_data_generator.py
   ```

4. **Find your data** in the generated `synthetic_marketing_data.csv` file.

---

## ⚙️ Customization

* **Add/Remove Fields**: Modify the `field_templates` list.
* **Data Types**: Use `'int'`, `'float'`, `'str'`, or `'date'`.
* **Parameter Ranges**:

  * **Integers**: `(min, max)`
  * **Floats**: `(min, max)`
  * **Strings**: `('Option1', 'Option2', ... )`
  * **Dates**: `('YYYY-MM-DD', 'YYYY-MM-DD')`

Example:

```python
field_templates = [
    ('CustomerID', 'int', 1000, 9999),
    ('SignupDate', 'date', '2021-01-01', '2024-12-31'),
    ('Plan', 'str', 'Free', 'Pro', 'Enterprise'),
    ('Spend', 'float', 0.0, 500.0)
]
```

---

## 📂 Output

* **CSV File**: `synthetic_marketing_data.csv` (by default)
* **Pandas DataFrame** preview in console

---

*Happy data generating!* 🎉
