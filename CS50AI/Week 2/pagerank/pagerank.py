import os
import random
import re
import sys
from itertools import cycle
import time


DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print("PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    all_pages = list(corpus.keys())

    probability_distribution = dict()

    for part_page in all_pages:
        probability_distribution[part_page] = (
            1 - damping_factor) / len(all_pages)

    for part_page in corpus[page]:
        probability_distribution[part_page] += damping_factor / \
            len(corpus[page])

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Choose a page at random
    start_page = random.choice(list(corpus.keys()))

    page_counter = dict()
    for page in corpus.keys():
        page_counter[page] = 0

    for _ in range(n):
        probablity_distribution = transition_model(
            corpus, start_page, damping_factor)

        page = random.choices(
            list(probablity_distribution.keys()), list(probablity_distribution.values()), k=1)

        page_counter[page[0]] += 1

        start_page = page[0]

    for key in page_counter.keys():
        page_counter[key] /= n

    # sum = 0
    # for value in page_counter.values():
    #     sum += value

    # print(sum)

    return page_counter


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    """
    There are three factors which are affecting the values of each PR(p)
    1. Inital values
    2. 1 - d / N 
    3. PR(i) / Numlinks(i)

    which order should I start to evaluate
    Currently going in this order 

    1 -> add 2 and check -> 2.
    """

    """
    to reverse the order and then calculating in the intiutive way
    """

    # print("corp", corpus)

    # Set default init values for each page
    page_rank = dict()
    for page in corpus.keys():
        page_rank[page] = 1 / len(corpus.keys())

        if len(corpus[page]) == 0:
            corpus[page] = corpus.keys()

    # reversing the corpus
    reversed_corpus = {}
    for filename, linked_files in corpus.items():
        # For each linked file
        for linked_file in linked_files:
            reversed_corpus.setdefault(linked_file, set()).add(filename)

    # print("rev corp", reversed_corpus)

    # print(page_rank)
    # print("performing one iteration")

    while True:
        no_change_counter = 0
        for page, linking_pages in reversed_corpus.items():
            # print(f"For page {page}")
            first_half = (1 - damping_factor) / len(corpus.keys())
            # print(f"First half calulation {first_half}")

            summation = 0
            for linking_page in linking_pages:
                # print(linking_page, end="")
                try:
                    summation += page_rank[linking_page] / \
                        len(corpus[linking_page])
                except ZeroDivisionError:
                    ...
                # print(f"Summation calculation of page{summation}")

            second_half = damping_factor * summation
            # print(f"Second half{second_half}")

            previous_value = page_rank[page]
            page_rank[page] = first_half + second_half

            if abs(previous_value - page_rank[page]) <= 0.0001:
                no_change_counter += 1

        # print(no_change_counter, len(corpus.keys()))
        if no_change_counter == len(corpus.keys()):
            break

        # print("page rank calculate is ", page_rank[page])

        # print("\n\n ---- END OF PAGE ------------------------------------\n")

        # print(page_rank)

    return page_rank


if __name__ == "__main__":
    main()
