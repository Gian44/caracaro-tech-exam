import re
from collections import Counter

def the_trigram(raw_input):
    # Combine all lines into one text block
    text = raw_input.strip().lower()

    # Split into sentences so trigrams don’t cross sentence boundaries
    sentences = re.split(r'[.!?]+', text)

    # Count trigrams and record first occurrence
    counts = Counter()
    first_pos = {}
    pos = 0

    for sentence in sentences:
        words = re.findall(r'[a-z]+', sentence)
        for i in range(len(words) - 2):
            trigram = f"{words[i]} {words[i+1]} {words[i+2]}"
            counts[trigram] += 1
            if trigram not in first_pos:
                first_pos[trigram] = pos
            pos += 1

    # Find trigram with max count, break ties by earliest position
    best = ""
    best_count = -1
    best_first = float("inf")

    for trigram, count in counts.items():
        if count > best_count or (count == best_count and first_pos[trigram] < best_first):
            best = trigram
            best_count = count
            best_first = first_pos[trigram]

    return best


if __name__ == "__main__":
    # First sample input
    sample_input_1 = """I came from the moon. He went to the other room. She went to the drawing room."""
    result1 = the_trigram(sample_input_1)
    print(result1)

    # Second sample input
    sample_input_2 = """I love to dance. I like to dance I. like to play chess."""
    result2 = the_trigram(sample_input_2)
    print(result2)
