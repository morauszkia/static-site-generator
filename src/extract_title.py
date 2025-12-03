def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith(("# ", "#\t")):
            title = line[2:].strip()
            if title == "":
                raise Exception("Invalid title: Title cannot be empty")
            
            return title
        
    raise Exception("No valid title found in markdown")