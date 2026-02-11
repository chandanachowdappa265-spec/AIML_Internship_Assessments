import pandas as pd

# Create the Series
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Remove leading/trailing spaces and convert to lowercase
cleaned = usernames.str.strip().str.lower()

# Check which names contain the letter 'a'
contains_a = cleaned.str.contains('a')

# Output
print("Cleaned Usernames:")
print(cleaned)

print("\nContains letter 'a':")
print(contains_a)
