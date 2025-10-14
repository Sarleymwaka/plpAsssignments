def modify_file():

    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            contents = file.read()

        modified_text = contents.upper()

        new_filename = f"modified_{filename}"

        with open(new_filename, "w") as file:
            file.write(modified_text)

        print(f"Success! The modified file has been saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You cannot read or write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

modify_file()