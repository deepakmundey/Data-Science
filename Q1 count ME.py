def count_me_occurrences(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Count occurrences of "ME" (case-insensitive)
            count_me = content.lower().count("me")
            return count_me
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

# Provide the path to the STORY.TXT file
file_path = "D:/PPS/Study Material/12th CS/Practice Text Document.txt"

# Call the function and print the result
result = count_me_occurrences(file_path)
if result is not None:
    print(f"Number of occurrences of 'ME': {result}")
