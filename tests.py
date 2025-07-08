from functions.get_files_info import get_files_info

if __name__ == "__main__":
    # Test listing the working directory
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    # Test listing a subdirectory
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    # Test with a directory outside permitted scope
    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

    # Test moving up a directory
    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))