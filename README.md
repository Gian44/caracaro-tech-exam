# Caracaro tech exam

This repository contains Python solutions for the two HackerRank problems given by CaraCaro:

1. **The Trigram**  
2. **Expand the Acronyms**

Both solutions:
- Use the sample inputs from HackerRank, placed directly in the `__main__` section.
- Have a function that takes the whole input as a string, processes it, and returns the answer.
- Print only the final answer(s).

---

## 1. The Trigram

**Function:**  
```python
the_trigram(raw_input)
````

**Sample Input #1**

```
I came from the moon. He went to the other room. She went to the drawing room.
```

**Sample Output #1**

```
went to the
```

**Sample Input #2**

```
I love to dance. I like to dance I. like to play chess.
```

**Sample Output #2**

```
i like to
```

### How I approached the problem

1. Lowercase all text so comparisons are case-insensitive.
2. Split into sentences by `.`, `!`, or `?` so trigrams stay inside sentence boundaries.
3. Extract words using regex to ignore punctuation.
4. Slide a 3-word window across each sentence to collect trigrams.
5. Count occurrences of each trigram and track the order they first appeared.
6. Select the trigram with the highest frequency; if there’s a tie, pick the one that appeared first.

**Time complexity:** O(N) where N is the number of words.
**Space complexity:** O(U) where U is the number of unique trigrams.

---

## 2. Expand the Acronyms

**Function:**

```python
expand_the_acronyms(raw_input)
```

**Sample Input #1**

```
3
The United Nations Children's Fund (UNICEF) is a United Nations Programme headquartered in New York City, that provides long-term humanitarian and developmental assistance to children and mothers in developing countries.
The National University of Singapore is a leading global university located in Singapore, Southeast Asia. NUS is Singapore's flagship university which offers a global approach to education and research.
Massachusetts Institute of Technology (MIT) is a private research university located in Cambridge, Massachusetts, United States.
NUS
MIT
UNICEF
```

**Sample Output #1**

```
National University of Singapore
Massachusetts Institute of Technology
United Nations Children's Fund
```

**Sample Input #2**

```
3
International Business Machines (IBM) is a technology company.
NASA stands for National Aeronautics and Space Administration.
I like coffee in the morning.
IBM
NASA
LOL

```

**Sample Output #2**

```
International Business Machines
National Aeronautics and Space Administration
LOL
```

### How I approached the problem

1. Read the input: first number is how many sentence lines, then the lines, then the queries.
2. Split each line into sentences by `.`, `!`, or `?`.
3. Look for direct matches (the 2 common way to detect acronyms in defined text):

   * `"Full Form (ACR)"`
   * `"ACR stands for Full Form"`
     These are stored in a dictionary mapping acronym → full form.
4. Handle missing direct definitions:

   * If an acronym appears but isn’t defined, search the same or previous sentence for the longest proper-noun phrase whose initials match the acronym.
   * Ignore common stopwords like “the”, “of”, “and” when matching initials.
5. Return the results:

   * If an acronym is in the dictionary, print its expansion.
   * Otherwise, print the acronym unchanged.

**Time complexity:** O(N + Q) where N is number of sentences and Q is number of queries.
**Space complexity:** O(A) where A is number of acronym definitions stored.

---

## How to run

```bash
python3 the_trigram.py
python3 expand_the_acronyms.py
```
