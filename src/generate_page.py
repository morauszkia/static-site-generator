from md_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown_content = file.read()
    
    with open(template_path, "r") as file:
        template = file.read()
    
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)

    with open(dest_path, "w") as file:
        file.write(template)
    
    print("Page generation complete.")