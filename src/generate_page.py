import os
import re

from md_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath):
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
    template = template.replace("href=\"/" , f"href=\"{basepath}")
    template = template.replace("src=\"/", f"src=\"{basepath}")

    with open(dest_path, "w") as file:
        file.write(template)
    


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, dest_path, basepath)
        elif entry.endswith(".md"):
            dest_path = re.sub(r"md$", r"html", dest_path)
            generate_page(full_path, template_path, dest_path, basepath)
