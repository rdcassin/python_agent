import os

def write_file(working_directory, file_path, content):
    fullPath = os.path.join(working_directory, file_path)
    absPath = os.path.abspath(fullPath)
    absWorking = os.path.abspath(working_directory)

    if not absPath.startswith(absWorking):
        return f'Error: Cannot write to "{file_path}" as it is outside of the permitted working directory'
        
    dir_name = os.path.dirname(fullPath)

    if not os.path.exists(dir_name) and dir_name != "":
        os.makedirs(dir_name)

    try:
        with open(fullPath, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"