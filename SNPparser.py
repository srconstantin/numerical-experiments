import os
import fnmatch

path = "/Users/sarahconstantin/Desktop/opensnp_datadump.201210311602"
for file in os.listdir(path):
	if file.endswith(".txt")
	f = open(file)
	lines = readlines[f]
	if fnmatch.fnmatch(file, '*23andme*'):
		i = 15
		rsid = []
		chromosomes = []
		position = []
		genotype = []
		while i < len(lines):
			line = lines[i]
			line = line.split()
			rsid.append(line[0])
			chromosomes.append(line[1])
			position.append(line[2])
			genotype.append(line[3])
		end
	end
