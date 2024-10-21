import re


ENV= {
    "commonprogramw6432": "C:\Program Files\Common Files",
    "commonprogramfiles": "C:\Program Files\Common Files",
    "comspec": "C:\Windows\system32\cmd.exe",
    "pathext": ".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL",
    "allusersprofile": "C:\ProgramData",
    "programfiles": "C:\Program Files",
    "programdata": "C:\ProgramData",
    "systemroot": "C:\Windows",
    "windir": "C:\Windows",
    "systemdrive": "C:",
    "homedrive": "C:",
    "public": "C:/Users/Public"  # / instead of \ to avoid unicode decode stuff
    }


def decode_content(text):
    
    parts = text.split(" -f ")
    first_part = parts[0]
    second_part = parts[1]

    items = second_part.split(",")
    decoded_text = ""
    for item in items:
        if item.startswith("["):
            match = re.findall(r'\[char\]([0-9]+)', item)
            decoded_text += chr(int(match[0]))
        else:
            matches = re.findall(r'\$env:([a-zA-Z0-9;z]*)\[([0-9]+)\]', item)
            pname = matches[0][0].lower()
            offset = int(matches[0][1])
            decoded_text += ENV[pname][offset]

    final_decoded_text = ""

    offsets = first_part.replace("iex ('", "").split("}{")
    offsets[0] = offsets[0].replace("{", "")
    offsets[-1] = offsets[-1].replace("}'", "")
    

    for n in offsets:
        final_decoded_text += decoded_text[int(n)]

    
    if "flag{" not in final_decoded_text:
        decode_content(final_decoded_text)
    else:
        print(final_decoded_text)
    


with open("eco_friendly", "r") as infile:
    text = infile.read()
    decode_content(text)
