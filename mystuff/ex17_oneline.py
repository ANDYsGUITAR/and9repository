from sys import argv;script, fr, to = argv;
with open(fr) as in_file,open(to,'w') as out_file:
    indata = in_file.read()
    out_file.write(indata)
