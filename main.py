from UF_web_scrape import get_html, parse_for_table

url = 'https://www.housing.ufl.edu/living-options/rental-rates/'

html = get_html(url)
table = parse_for_table(html)

print(table)
