# https://quera.org/problemset/275506
# -----------------------------------

from math import ceil

number_of_reports = int(input().strip())
report_pages = list(
    map(int, input().strip().split())
)  # report (index) : number of pages (value)

required_paper_sheets: int = 0

for pages_count in report_pages:
    required_paper_sheets += ceil(pages_count / 2)

print(required_paper_sheets)
