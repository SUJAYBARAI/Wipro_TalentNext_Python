# Project 1 :Tech Module:Exception Handling

def process_purchase_file():
    try:
        filename = input("Enter the file name:\n")
        with open(filename, 'r') as file:
            lines = file.readlines()

        purchased_items = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue  # Skip blank lines
            try:
                parts = line.split()
                if len(parts) == 2:
                    item, value = parts[0], parts[1]
                    if value.lower() == 'free':
                        free_items += 1
                    elif item.lower() == 'discount':
                        discount = int(value)
                    else:
                        total_amount += int(value)
                        purchased_items += 1
                else:
                    raise ValueError("Invalid line format")
            except ValueError as ve:
                print(f"Warning: Skipping invalid line -> '{line}'. Reason: {ve}")
                continue

        final_amount = total_amount - discount

        print(f"No of items purchased: {purchased_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
process_purchase_file()