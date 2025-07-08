import os

def get_files_info(working_directory, directory=None):
    try:
        fullPath = os.path.join(working_directory, directory)
        absPath = os.path.abspath(fullPath)
        absWorking = os.path.abspath(working_directory)

        if not absPath.startswith(absWorking):
            return f'Error: Cannot list "{directory}" as it is outside of the permitted working directory'

        if not os.path.isdir(fullPath):
            return f'Error: "{directory}" is not a directory'

        file_contents = os.listdir(path=fullPath)
        contents = []
        for file in file_contents:
            current_path = os.path.join(absPath, file)
            contents.append(
                f'- {file}: file_size={os.path.getsize(current_path)}, is_dir={os.path.isdir(current_path)}'
            )
        return '\n'.join(contents)
    except Exception as e:
        return f"Error: {str(e)}"