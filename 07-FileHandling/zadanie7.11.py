film_titles = ["a","b","c","d","e"]
with open('07-FileHandling/filmtitles.txt','w')as f:
    for title in film_titles:
        f.write(title)
        f.write("\n")
    f.close()