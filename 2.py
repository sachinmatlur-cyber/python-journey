import pprint
message1 =open(r"/content/drive/MyDrive/python editor/New Text Document.txt")
message = message1.read()
message1.close()
print('The content in the file is: \n\n', message)
count = {}
for character in message.split():
 count.setdefault(character, 0)
 count[character] = count[character] + 1
print('\nFrequency of words appeared in the Sentence or paragraph\n')
pprint.pprint(count)
print()
sortedcount = sorted(count.items(), key=lambda x:x[1], reverse=True)
converttodict = dict(sortedcount)
print('\nSorted in descending order:\n\n',converttodict)
import itertools
sliceddict = dict(itertools.islice(converttodict.items(), 10))
print('\nTen Most frequently appeared word in a paragraph :\n\n',sliceddict)