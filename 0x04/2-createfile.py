























































































import os  

def create_file_in_specified_directory(directory, file_name, content=None):  
    """Create a new file in the specified directory."""  
    # Create the full path for the file  
    file_path = os.path.join(directory, file_name)  

    # Create the file and write content if provided  
    with open(file_path, 'w') as f:  # Use 'w' to create a file (will overwrite if exists)  
        if content:  
            f.write(content)  

    print(f"File '{file_name}' created successfully at: {file_path}")  

# Use the function  
if __name__ == "__main__":  
    specified_directory = "c:/Users/Smart ICT Concepts/Documents/FUT MINNA/ML-TRAINING 2024/Python_Programming/0x04/"  
    create_file_in_specified_directory(specified_directory, 'demo.txt', 'Hello, this is a test file.')

















import os  

def create_file_in_parent_directory(file_name, content=None):  
    """Create a new file in the parent directory."""  
    # Get the path to the parent directory  
    parent_directory = os.path.abspath(os.path.join(os.getcwd(), ".."))  
    file_path = os.path.join(parent_directory, file_name)  

    # Create the file and write content if provided  
    with open(file_path, 'w') as f:  # Use 'w' to create a file (will overwrite if exists)  
        if content:  
            f.write(content)  

    print(f"File '{file_name}' created successfully at: {file_path}")  

# Use the function  
if __name__ == "__main__":  
    create_file_in_parent_directory('demo2.txt', 'Hello, this is a test file.')