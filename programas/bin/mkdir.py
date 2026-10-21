input=command.split()
for dir in input[1:]:
    if "/" in dir:
        way=path_way(dir)
        at=0
        for a,pos in enumerate(way):
            if a==len(way)-1:continue
            at[pos]
        at[way[-1]]={}
    else:
        curdir[dir]={}