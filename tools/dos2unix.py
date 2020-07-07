#!/usr/bin/env python
"""\
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py <input> <output>
"""
# original = "final_project_dataset.pkl"
# destination = "regression_code_modified.pkl"

original = "python2_lesson14_keys.pkl"
destination = "new_python2_lesson14_keys.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content) - outsize))
