text = input('Enter text: >>> ')
text_split = text.split()
acronym = []
for charac in text_split:
    acronym.append(charac[0])

acronym = "".join(acronym)
print(acronym)