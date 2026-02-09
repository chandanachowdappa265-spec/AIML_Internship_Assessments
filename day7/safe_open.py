filename = input("Enter filename to open (e.g., config.txt): ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print("\nOops! That file doesn't exist yet ")
