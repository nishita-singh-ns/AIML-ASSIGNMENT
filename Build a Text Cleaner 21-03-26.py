### CODE CELL ###
import string

text = "Hiiiii!!! This is sooo cool 😂"

# Lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Remove simple stopwords
stopwords = ["is", "this", "so"]
words = text.split()
cleaned = [word for word in words if word not in stopwords]

print("Cleaned Text:", " ".join(cleaned))

### CODE CELL ###


