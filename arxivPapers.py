import arxiv
# cheock out: https://pypi.org/project/arxiv/

# Construct the default API client.
client = arxiv.Client()

# Search for the 10 most recent articles matching the keyword "quantum."
search = arxiv.Search(
  query = "Machine learning",
  max_results = 10,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

results = client.results(search)

# `results` is a generator; you can iterate over its elements one by one...
for i, r in enumerate(client.results(search)):
  print(f"{i}. {r.title}")
# ...or exhaust it into a list. Careful: this is slow for large results sets.
# all_results = list(results)
# print([r.title for r in all_results])

# For advanced query syntax documentation, see the arXiv API User Manual:
# https://arxiv.org/help/api/user-manual#query_details
search = arxiv.Search(query = "ti:machine learning AND abs:neural networks")
paper_link = next(client.results(search))
print(paper_link)
# print(type(paper_link))
paper_id = str(paper_link).split("/")[-1]
print(paper_id)

# Search for the paper with ID "1605.08386v1"
search_by_id = arxiv.Search(id_list=[paper_id])
# Reuse client to fetch the paper, then print its title.
first_result = next(client.results(search))
print(first_result.title)

##############
# Downloading papers
paper = next(arxiv.Client().results(arxiv.Search(id_list=[paper_id])))
# Download the PDF to the PWD with a default filename.
paper.download_pdf()
# Download the PDF to the PWD with a custom filename.
paper.download_pdf(filename="downloaded-paper.pdf")
# Download the PDF to a specified directory with a custom filename.
# paper.download_pdf(dirpath="./papers", filename="downloaded-paper.pdf")