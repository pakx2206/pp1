movie_title = ["x","d","p","a","s"]
file = open("movies.txt","w")
for x in range(0,len(movie_title)):
    file.write(movie_title[x]+"\n")
file.close()