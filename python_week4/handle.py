def process_file():
    # Prompt the user for a filename
    filename = input("Enter the filename to read: ")
    
    try:
        # Try to open and read the file
        with open(filename + ".txt", 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (e.g., reverse the text)
        modified_content = content[::-1]  # Reverses the content
        
        # Write the modified content to a new file
        new_filename = 'modified_' + filename
        with open(new_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"The file has been successfully modified and saved as '{new_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
process_file()
