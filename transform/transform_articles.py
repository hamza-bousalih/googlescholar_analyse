def transform_article_count(data):
    for ind, item in enumerate(data):
        data[ind]["Article Count"] = len(item["Article"])
        

def transform_authors_of_article(data):
    for ind, item in enumerate(data):
        for article in item["Article"]:
            count = len(article['auteur'].split(","))
            article["Author Count"] = count
   
   
def decompose_description(description):
    first_digit_index = next((i for i, c in enumerate(description) if c.isdigit()), None)

    journal_title = description[:first_digit_index].strip()
    remaining_info = description[first_digit_index:].strip()

    components = [item.strip() for item in remaining_info.split(',')]

    # Extracting values
    volume_issue = components[0]
    pages = components[1]
    year = components[2]

    # Further splitting volume and issue
    volume_issue = [part.strip() for part in volume_issue.split('(')]
    if len(volume_issue) > 1:
        volume, issue = [part.strip() for part in volume_issue.split('(')]
    else:
        volume = volume_issue[0]
        issue = ""

    return {
        'Title:': journal_title,
        'Volume:': int(volume),
        'Issue:': issue.replace(")", ""),
        'Pages:': pages,
        'Year:': int(year),
    }
    
    
def decompose_articles(articles):
    articles_decomposed = []
    for article in articles:
        authors = [author.strip() for author in article["auteur"].split(",")]
        if all(s.lower() != article["Author"].lower() for s in author):
            authors.append(article["Author"])
        for author in authors:
            if "..." in author: break
            desc = article["description"]
            information = decompose_description(desc)
            author_data = {
                "Article_Title": article["Nom Article"],
                "Author": author,
                "Year": article["Annee"],
                "Description": desc,
                'Title': information['Title'],
                'Volume': information['Volume'],
                'Issue': information['Issue'],
                'Pages': information['Pages'],
                '_Year': information['Year'],
            }
            articles_decomposed.append(author_data)
    return articles_decomposed

if __name__ == "__main__":
    pass