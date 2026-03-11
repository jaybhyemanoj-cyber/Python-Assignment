source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

try:
    with open(source, 'r') as f1:
        data = f1.read()

    upper_data = data.upper()

    with open(destination, 'w') as f2:
        f2.write(upper_data)

    print("File copied successfully in uppercase.")

except FileNotFoundError:
    print("Source file not found.")