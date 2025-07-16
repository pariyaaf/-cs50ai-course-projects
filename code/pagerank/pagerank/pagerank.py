import os
import random
import re
import sys

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
    print(f"PageRank Results from Iteration")
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

    pr = {}

    N = len(corpus)
    links = corpus[page] if corpus[page] else set(corpus.keys())
    num_links = len(links)

    if not corpus[page]:
        for pg in corpus.keys():
            pr[pg] = 1 / N

    for q in corpus.keys():
        pr[q] = pr[q] = (1 - damping_factor) / N

        if q in corpus[page]:
            pr[q] += damping_factor / num_links

    return pr
    # raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    result = {key:0 for key in corpus.keys()}
    page = random.choice(list(corpus.keys()))
    for i in range(n):
        pr = transition_model(corpus, page, damping_factor)
        page = random.choices(population=list(pr.keys()),
                            weights=list(pr.values()),
                            k=1)[0]
        result[page] += 1
    
    for page in result:
        result[page] /= n
    return result
    # raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.
    """
    EPSILON = 0.001
    N = len(corpus)

    old_ranks = {page: 1 / N for page in corpus}

    while True:
        new_ranks = {page: (1 - damping_factor) / N for page in corpus}

        for page_i, links in corpus.items():
            num_links = len(links) if links else N
            share = damping_factor * old_ranks[page_i] / num_links
            if links:
                for dest in links:
                    new_ranks[dest] += share
            else:
                for dest in new_ranks:
                    new_ranks[dest] += share

        diff = max(abs(new_ranks[p] - old_ranks[p]) for p in corpus)
        if diff < EPSILON:
            break

        old_ranks = new_ranks

    return new_ranks
    # raise NotImplementedError


if __name__ == "__main__":
    main()
