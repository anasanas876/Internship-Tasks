import os


def organize_files():
 current_dir = os.getcwd()
 print("Current Working Directory:", current_dir)

 # Listing all files and folders
 listing = os.listdir(current_dir)
 # Creating folders if they don't exist
 if not os.path.exists("pdf"):
    os.mkdir("pdf")
 if not os.path.exists("docx"):
    os.mkdir("docx")
 if not os.path.exists("jpg"):
    os.mkdir("jpg")
 # Moving files to their respective folders
 for item in listing:

  if os.path.isfile(item):

        file_name, file_extension = os.path.splitext(item)

        if file_extension.lower() == ".pdf":
            destination = os.path.join(current_dir, "pdf", item)
            os.replace(item, destination)

        elif file_extension.lower() == ".docx":
            destination = os.path.join(current_dir, "docx", item)
            os.replace(item, destination)

        elif file_extension.lower() == ".jpg":
            destination = os.path.join(current_dir, "jpg", item)
            os.replace(item, destination)

print("Files organized successfully!")

if __name__ == "__main__":
 organize_files()