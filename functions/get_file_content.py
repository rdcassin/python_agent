import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    fullPath = os.path.join(working_directory, file_path)
    absPath = os.path.abspath(fullPath)
    absWorking = os.path.abspath(working_directory)

    if not absPath.startswith(absWorking):
        return f'Error: Cannot read "{file_path}" as it is outside of the permitted working directory'
        
    if not os.path.isfile(fullPath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(fullPath, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            additional_content = f.read()
        
        if len(additional_content) > 0:
            file_content_string = file_content_string + f' [...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
        return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"