import re
import os

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

baseDir = os.getcwd ()

sourceDir = os.path.join (baseDir, 'source', 'includes')

re_include = re.compile (r".*(includes/.*)")
re_mdName = re.compile (r"_(.*)\.md")

for root, dirs, files in os.walk (sourceDir):
	if (len (files) > 0):
		fileList = sorted_alphanumeric (files)

		shallowRootMatch = re_include.match (root)
		if (shallowRootMatch):
			shallowRoot = shallowRootMatch.group (1)
			print (shallowRoot)



	#<%= partial "includes/ir/1-SendIR" %>


