positive_words = ["good", "great", "awesome", "amazing"]
negative_words = ["bad", "worst", "boring", "poor"]

reviews = [
    "This movie is awesome",
    "The film was boring",
    "Great acting and story",
    "Worst movie ever",
    "Amazing experience"
]

for review in reviews:
    score = 0
    for word in review.lower().split():
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        print(review, "→ Positive")
    else:
        print(review, "→ Negative")