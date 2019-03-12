# python script to clean up source code of spring-in-action-5-samples:
# https://github.com/habuma/spring-in-action-5-samples

import os

def pywalker(path):
	if os.path.isdir(path):
		for root, dirs, files in os.walk(path):
			for filename in files:
				if filename.endswith(".java") or filename.endswith('.xml') or filename.endswith('.html') or filename.endswith('.yml') or filename.endswith('.ts'):
					path = os.path.join(root, filename)
					process_file(path)


def process_file(path):
	f = open(path, "r")
	lines = f.readlines()
	f.close()
	f = open(path, "w")
	for line in lines:
		if ("tag::" not in line) and ("end::" not in line):
			f.write(line)
	f.close()


if __name__ == '__main__':
	pywalker('path/to/spring-in-action-5-samples/folder')
