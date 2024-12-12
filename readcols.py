import csv
file_name='car.csv'
columns_to_read=['company','Car Model']
try:
    with open(file_name,newline='')as csvfile:
        reader=csv.DictReader(csvfile)
        missing_columns=[col for col in columns_to_read if col not in reader.fieldnames]
        if missing_columns:
            print(f"Error:Missing columns in the file:{','.join(missing_columns)}")
        else:
            print(",".join(columns_to_read))
            for row in reader:
                print(",".join(row[col]for col in columns_to_read))
except FileNotFoundError:
    print(f"Error:File'{file_name}' not found")
except Exception as e:
    print(f"An error occured:{e}")