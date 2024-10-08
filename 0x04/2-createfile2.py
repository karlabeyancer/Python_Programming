import os  

def create_file(file_name, content=None):  
    """Create a new file. Raises an error if it already exists."""  
    try:  
        # Create the file  
        with open(file_name, 'x') as f:  
            if content:  
                f.write(content)  
        # Print the full path of the created file  
        absolute_path = os.path.abspath(file_name)  
        print(f"File '{file_name}' created successfully at: {absolute_path}")  
    except FileExistsError:  
        print(f"Error: The file '{file_name}' already exists.")  

def delete_file(file_name):  
    """Delete a file if it exists."""  
    try:  
        os.remove(file_name)  
        print(f"File '{file_name}' deleted successfully.")  
    except FileNotFoundError:  
        print(f"Error: The file '{file_name}' does not exist.")  

# Use the functions:  
if __name__ == "__main__":  
    current_directory = os.getcwd()  
    print(f"Current working directory: {current_directory}")  
    create_file('demo1.txt', 'Hello, this is a test file.')  
    delete_file('demo1.txt') 