from copystatic import copy_static_files, empty_directory
from generate_page import generate_page


def main():
    empty_directory("public")
    copy_static_files("static", "public")
    print("Finished copying files.")
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/contact/index.md", "template.html", "public/contact/index.html")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel/index.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")


if __name__ == "__main__":
    main()