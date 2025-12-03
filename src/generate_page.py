import os

from md_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.exists(from_path):
        print(f"Source file {from_path} does not exist.")
        print("Page generation aborted.")
        return

    with open(from_path, "r") as file:
        markdown_content = file.read()
    
    if not os.path.exists(template_path):
        print(f"Template file {template_path} does not exist.")
        print("Page generation aborted.")
        return

    with open(template_path, "r") as file:
        template = file.read()
    
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)

    with open(dest_path, "w") as file:
        file.write(template)
    
    print("Page generation complete.")