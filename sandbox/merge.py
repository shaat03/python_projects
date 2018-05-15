# function for merging files given as parameter
import os

def merge_files(output, *args):
    if os.path.isfile(output):
        question1 = 'Output file %s already exists! Do you want to overwrite it? y/n ' % output
        answer1 = input(question1)
    if answer1.lower() == 'y':              # if answer is y, then go forward
        with open(output, 'r') as tmp:
            tmp_out = tmp.read()
        if tmp_out != '':
            question2 = 'File %s has some content! Do you want to append to it? y/n ' % output
            answer2 = input(question2)
    else:                                  # else exit silently
        return 0
    for file in args:
        if not os.path.isfile(file):
            print('File %s does not exist. Skipping...' % file)
    with open(output, 'w') as out:
        if answer2.lower() == 'y':
            out.write(tmp_out)
        for file in args:
            if os.path.isfile(file):
                with open(file, 'r') as inp:
                    out.write(inp.read())
