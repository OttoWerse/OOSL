text = 'all zip files are compressed'
f = 'zip'
l = len(f)
t = text[text.find(f)+l:len(text)]
i = t.find(f)
if i != -1:
    i +=len(text[0:text.find('zip')+l])
print(i)

text = 'all zip files are zipped'
f = 'zip'
l = len(f)
t = text[text.find(f)+l:len(text)]
i = t.find(f)
if i != -1:
    i +=len(text[0:text.find('zip')+l])
print(i)

text = 'all zip files are zipped'
f = 'zip'
i = text.find(f, text.find(f)+1)
print(i)

text = 'all zip files are compressed'
f = 'zip'
i = text.find(f, text.find(f)+1)
print(i)