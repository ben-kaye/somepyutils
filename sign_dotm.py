import re, math

def make_line(text: str):
    length = len(text)
    pre_space = math.floor((61-length) / 2)
    post_space = 67 - length - pre_space

    return "% * " + " " * pre_space + text + " " * post_space + " *\n"

def find_end(lines):
    if re.search("^%\$sign$", lines[0]) != None:
        idx = -1
        for i in range(len(lines)):
            if re.search("^%\$endsign$", lines[i]) != None:
                idx = i
        return idx
    else:
        return -1

def get_content(lines, endx):
    text = lines[1:endx]
    text = [ s[1:-1] for s in text ]  
    return text
        
STAR_COUNT = 36
star_line = "%" + " *" * STAR_COUNT + "\n"

path = "C:\\Users\\Ben\\OneDrive\\Engineering\\EUROP\\BKModel\\"
mat_file_name ="test"
file_ext = ".m"
full_path = path + mat_file_name + file_ext

file = open(full_path, "r")
lines = file.readlines()
file.close()


endx = find_end(lines)

if endx != -1:
    content = get_content(lines,endx)
    del lines[0:endx+1]
    file = open(full_path, "w")
    
    lines.insert(0, star_line)
    lines.insert(0, make_line(""))
    for i in range(len(content)):
        txt = content.pop()
        if txt == "$br":
            lines.insert(0, make_line(""))
            lines.insert(0, star_line)
            lines.insert(0, make_line(""))
        else:
            lines.insert(0,make_line(txt))
    lines.insert(0, make_line(""))
    lines.insert(0, star_line)
        
    file_contents = "".join(lines)
    file.write(file_contents)

    file.close
