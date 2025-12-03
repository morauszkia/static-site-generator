from copystatic import copy_static_files, empty_directory
from generate_page import generate_page


def main():
    empty_directory("public")
    copy_static_files("static", "public")
    print("Finished copying files.")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()