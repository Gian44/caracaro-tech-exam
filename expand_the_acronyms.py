import re
from typing import List

def expand_the_acronyms(raw_input):
    lines = raw_input.strip().splitlines()

    # First line: number of sentence lines
    n = int(lines[0])
    sentence_lines = lines[1:1 + n]
    queries = lines[1 + n:]

    # Split each line into sentences by ., !, ?
    all_sents = []
    for s in sentence_lines:
        parts = re.split(r'[.!?]+\s*', s)
        for p in parts:
            p = p.strip()
            if p:
                all_sents.append(p)

    expansions = {}

    def clean_full(full: str) -> str:
        full = full.strip()
        if full.lower().startswith("the "):
            full = full[4:]
        return full

    # 1) Direct patterns:
    #    - Full Form (ACR)
    #    - ACR stands for Full Form
    for s in all_sents:
        # allow letters, spaces, and apostrophes in the full form
        for m in re.finditer(r"([A-Za-z' ]+?)\s*\(([A-Z]{2,})\)", s):
            full = clean_full(m.group(1))
            acr = m.group(2).strip()
            expansions[acr] = full

        m2 = re.search(r"\b([A-Z]{2,})\s+stands\s+for\s+([A-Za-z' ]+)", s, flags=re.I)
        if m2:
            acr = m2.group(1).upper().strip()
            full = clean_full(m2.group(2))
            expansions[acr] = full

    # 2) Simple inference when acronym appears without direct definition.
    stop = {"the", "of", "and", "for", "in", "on", "at", "to", "a", "an"}

    def initials_from_phrase(phrase):
        words = re.findall(r"[A-Za-z]+", phrase)
        letters = [w[0].upper() for w in words if w.lower() not in stop]
        return "".join(letters)

    def infer_from_sentence(acr, sentence):
        # Find the longest span of Title-Case words (allow stopwords)
        tokens = re.findall(r"[A-Za-z][A-Za-z']*", sentence)
        L = len(tokens)
        # try longer spans first
        for i in range(L):
            for j in range(L, i + 1, -1):
                span = tokens[i:j]
                # each token must be Title-Case or a stopword
                if all(t[0].isupper() or t.lower() in stop for t in span):
                    phrase = " ".join(span)
                    if initials_from_phrase(phrase) == acr:
                        return clean_full(phrase)
        return None

    # Try to infer for any queried acronym not already known
    for acr in queries:
        if acr not in expansions:
            for idx, s in enumerate(all_sents):
                if re.search(r"\b" + re.escape(acr) + r"\b", s):
                    # same sentence
                    guess = infer_from_sentence(acr, s)
                    if guess:
                        expansions[acr] = guess
                        break
                    # previous sentence
                    if idx > 0:
                        guess = infer_from_sentence(acr, all_sents[idx - 1])
                        if guess:
                            expansions[acr] = guess
                            break

    return [expansions.get(q, q) for q in queries]


if __name__ == "__main__":
    sample_input1 = """3
The United Nations Children's Fund (UNICEF) is a United Nations Programme headquartered in New York City, that provides long-term humanitarian and developmental assistance to children and mothers in developing countries.
The National University of Singapore is a leading global university located in Singapore, Southeast Asia. NUS is Singapore's flagship university which offers a global approach to education and research.
Massachusetts Institute of Technology (MIT) is a private research university located in Cambridge, Massachusetts, United States.
NUS
MIT
UNICEF"""

    outputs1 = expand_the_acronyms(sample_input1)
    for out in outputs1:
        print(out)
    print("\n")

    sample_input2 = """3
International Business Machines (IBM) is a technology company.
NASA stands for National Aeronautics and Space Administration.
I like coffee in the morning.
IBM
NASA
LOL

"""

    outputs2 = expand_the_acronyms(sample_input2)
    for out in outputs2:
        print(out)
