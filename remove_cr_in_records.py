import csv





outfile=open('outfile', 'wb')

with open('review-5k.csv', 'r', newline="\r\n") as fh:

	tab = csv.reader(fh, quotechar='"', delimiter=',')


	count_dict={}

	for line in tab:
		linestring=','.join(line)
		if '\r\n' in linestring:
			linestring=linestring.replace('\r\n', ' ')
		if '\n' in linestring:
			linestring=linestring.replace('\n', ' ')
		outfile.write(bytes(linestring+'\n', 'UTF-8'))

outfile.close()
