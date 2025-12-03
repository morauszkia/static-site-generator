from copystatic import copy_static_files, empty_directory
from generate_page import generate_pages_recursive


def main():
    empty_directory("public")
    copy_static_files("static", "public")
    print("Finished copying files.")
    generate_pages_recursive("content", "template.html", "public")
    print("All pages generated.")


if __name__ == "__main__":
    main()