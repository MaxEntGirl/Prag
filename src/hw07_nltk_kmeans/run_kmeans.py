from hw07_nltk_kmeans.nltk_kmean import Reader
from hw07_nltk_kmeans.nltk_kmean import Kmeans
from nltk.cluster import euclidean_distance

# run this code from the src directory with python3 -m hw07_nltk_kmeans.run_kmeans

filename = '../data/courses.txt'
reader = Reader(filename)

# returns list of courses
courses = reader.courses

# vocabulary from file
words = reader.vocabulary
print("vocabulary size:", len(words))

vectorspaced_data =reader.vector_spaced_data

clusterer = Kmeans(10, euclidean_distance)
clusters = clusterer.nltk_cluster(vectorspaced_data)
for el in sorted([(cluster_id, course) for cluster_id, course in zip(clusters, courses)]):
    print(el)


