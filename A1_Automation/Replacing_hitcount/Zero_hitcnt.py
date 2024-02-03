import re

f = open("web-dmz.txt")
list_f = []
for i in f:
    list_f.append(i)
f.close()

pattern = r'.*\(hitcnt=[0-9]?\).*'

to_be_add = []
for i in list_f:
    match_hit = re.match(pattern, i)
    if not match_hit:
        to_be_add.append(i)

new_web = open("new_web_dmz.txt", "w+")

for i in to_be_add:
    new_web.write(i)
new_web.close()
