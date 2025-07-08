import os

def get_files_info(working_directory, directory=None):
    fullPath = os.path.join(working_directory, directory)
    absPath = os.path.abspath(fullPath)
    absWorking = os.path.abspath(working_directory)

    if not absPath.startswith(absWorking):
        return f'Error: Cannot list "{directory}" as it is outside of the permitted working directory'

    if not os.path.isdir(fullPath):
        return f'Error: "{directory}" is not a directory'

    try:
        dir_contents = os.listdir(fullPath)
        contents = []
        for item in dir_contents:
            current_path = os.path.join(absPath, item)
            contents.append(
                f'- {item}: file_size={os.path.getsize(current_path)}, is_dir={os.path.isdir(current_path)}\n'
            )
        return ''.join(contents)
    except Exception as e:
        return f"Error: {str(e)}"