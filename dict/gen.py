import os

# Define the root directory where your directories are located
root_directory = "."

# Initialize an empty Markdown content
markdown_content = ""

# Function to add directories as headers with image links
def add_directories_with_images(directory):
    global markdown_content
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            # Add the directory name as a header
            markdown_content += f"# {item}\n"
            # List image files within the directory
            for image in os.listdir(item_path):
                if image.endswith((".jpg", ".png", ".gif", "webp")):
                    image_link = os.path.join(item_path, image).replace(' ', '\\ ')
                    markdown_content += f"![image](\"{image_link}\" \"{image}\")\n"
            markdown_content += "\n"

# Start the process with the root directory
add_directories_with_images(root_directory)

# Write the Markdown content to a single .md file
with open("gallery.md", "w") as md_file:
    md_file.write(markdown_content)
