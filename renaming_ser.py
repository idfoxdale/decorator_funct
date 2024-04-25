import os

def remove_downsub_from_filenames():
    # Get the directory of the current Python script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    for filename in os.listdir(current_directory):
        if filename.endswith(".txt") and filename.endswith("[DownSub.com].txt"):
            new_filename = filename.replace("[DownSub.com].txt", ".txt")
            os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))
            print(f"Renamed file: {filename} -> {new_filename}")

# Call the function to remove "[DownSub.com]" from the filenames
remove_downsub_from_filenames()
