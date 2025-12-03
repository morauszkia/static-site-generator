import sys
from copystatic import copy_static_files, empty_directory
from generate_page import generate_pages_recursive


DST_DIR = "docs"

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    empty_directory(DST_DIR)
    copy_static_files("static", DST_DIR)
    print("Finished copying files.")
    generate_pages_recursive("content", "template.html", DST_DIR, basepath)
    print("All pages generated.")


if __name__ == "__main__":
    main()