# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.


try:
    # get filename from user
    filename = input('Upload a file: ')

    # read input file
    with open(filename, 'r') as file:
        data = file.read()


    # Example modification: convert to uppercase
    modified_data = data.upper() 

    
    # Write to output file
    output_filename = input('Save as: ')
    with open(output_filename, 'w') as file:
        file.write(modified_data)
        

    print(f"Success! File saved as '{output_filename}'")


except FileNotFoundError:
    print(f"Error: '{filename}' does not exist.")

except PermissionError:
    print(f"Permission Denied: Cannot read/write '{filename}'.")

except Exception as e:       # Anything else that goes wrong
    print(f"Unexpected error: {e}")
    