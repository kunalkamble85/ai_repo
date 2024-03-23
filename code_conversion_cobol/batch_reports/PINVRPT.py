# Define a class to simulate file records
class GrainRecord:
    def __init__(self, serial, status, grain_type, formula, qa, weight):
        self.serial = serial
        self.status = status
        self.grain_type = grain_type
        self.formula = formula
        self.qa = qa
        self.weight = weight

# Simulate reading records from files
def read_records(filename):
    # Simulate reading records from the file
    # For demonstration purposes, returning a list of dummy records
    records = [
        GrainRecord(123456789012, 0, "Type1", "Formula1", "QA1", 100),
        GrainRecord(987654321098, 1, "Type2", "Formula2", "QA2", 200),
        # Add more dummy records as needed
    ]
    return records

# Simulate writing records to files
def write_records(filename, records):
    # Simulate writing records to the file
    for record in records:
        print(f"Writing record: {record.serial}, {record.status}, {record.grain_type}, {record.formula}, {record.qa}, {record.weight}")

# Function to generate report for a given type of inventory
def generate_report(inventory_type):
    records = read_records(f"IN{inventory_type}")
    header = f"PROPELLANT GRAIN INVENTORY REPORT - {inventory_type.upper()}"
    print(header)
    print("REPORT DATE:", "2024/03/15")  # Assuming the current date
    print("SERIAL      STATUS    TYPE        FORMULA           QA   WEIGHT")
    print("---------------------------------------------------------------")
    for record in records:
        status = "ACTIVE" if record.status == 0 else "SPENT" if record.status == 1 else "DESTROYED"
        print(f"{record.serial} {status.ljust(10)} {record.grain_type.ljust(10)} {record.formula.ljust(15)} {record.qa.ljust(4)} {record.weight}")
    print()

def main():
    generate_report("ALL")
    generate_report("ACT")
    generate_report("SPN")
    generate_report("DES")

if __name__ == "__main__":
    main()
