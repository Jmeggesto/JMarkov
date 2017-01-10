import markovify

# Get raw text as string.
with open("corpus.txt") as f:
    text = f.read()

txt = ""
model = markovify.Text(text)
for i in range(10):
	sentence = model.make_sentence()
	if sentence is not None:
		txt += sentence + " "

print(txt)