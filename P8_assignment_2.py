source = input("Enter source python file: ")
destination = input("Enter destination file: ")

try:
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        for line in f1:
            line = line.strip()
            
            if line.startswith("#") or line == "":
                continue
            
            f2.write(line + "\n")

    print("\nContent copied without comments.\n")

    print("Source File Content:")
    with open(source, 'r') as f:
        print(f.read())

    print("\nDestination File Content:")
    with open(destination, 'r') as f:
        print(f.read())

except FileNotFoundError:
    print("File not found.")