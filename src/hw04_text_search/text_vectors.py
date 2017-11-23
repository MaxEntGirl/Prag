from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os, math

def dot(dictA, dictB):
    """
    >>> dot({'flower': 0, 'du': 3 , 'ich': 1, 'apple': 0}, {'flower': 9, 'du': 3, 'ich': 0, 'apple': 0})
    9
    >>> dot ({'affection': 115, 'jealous': 10 , 'gossip': 2, 'wuthering': 0}, {'affection': 58, 'jealous': 7, 'gossip': 0, 'wuthering': 0})
    6740
    """
    return sum([dictA.get(tok) * dictB.get(tok,0) for tok in dictA])

def normalized_tokens(text):
    """
    >>> normalized_tokens("Test of normaliz funktion")
    ['test', 'of', 'normaliz', 'funktion']
"""
    return [token.lower() for token in word_tokenize(text)]

class TextDocument:
    """
    This class represents a single document and stores an Id, the text and a frequency list
    """
    def __init__(self, text, id=None):
        """
        The constructor gets the text and uses the nltk module to create a freqency list for this document
        :param text: full text of the document
        :param id: Id for the document
        """
        self.text = text.replace('\n',' ') # Remove Line Breaks in text
        self.text = self.text.replace('>', '') # Remove ">>>>"
        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """
        Opens a text file and reads its contents. An instance of TextDocument is created
        :param filename: Name of the file
        :return: returns an instance of class TextDocument
        """
        with open(filename, 'r') as myfile:
            text=myfile.read().strip()
        return cls(text, filename)

class DocumentCollection:
    """
    This class contains information for several documents.
    """
    def __init__(self, term_to_df, term_to_docids, docid_to_doc):
        """
        The construtor sets the following class variables
        :param term_to_df: for each term the number of documents where it occurs (document frequency)
        :param term_to_docids: For each term all documents where it occures (inverted index)
        :param docid_to_doc: list of documents, access via id
        """
        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc

    @classmethod
    def from_dir(cls, dir, file_suffix):
        """
        Reads files from directory with a defined file extension
        :param dir: Input directory
        :param file_suffix: File extension filter
        :return: Returns instance of DocumentCollection
        """
        files = [(dir + "/" + f) for f in os.listdir(dir) if f.endswith(file_suffix)]
        docs = [TextDocument.from_file(f) for f in files]
        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):
        """
        Returns an instance of DocumentCollection for a given document list.
        The document frequency, an inverted index and a list of documents is created and passed
        to the constructor
        :param docs: a list of documents (references to class TextDocument)
        :return: Returns an instance of DocumentCollection
        """
        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()
        for doc in docs:
            docid_to_doc[doc.id] = doc
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)
        return cls(term_to_df, term_to_docids, docid_to_doc)

    def docs_with_all_tokens(self, tokens):
        """
        For a given list of search words (tokens) this method returns a list of document IDs
        where these tokens are in the text
        :param tokens: list of search terms
        :return: list of document ids, where the tokens are found
        """
        docids_for_each_token = [self.term_to_docids[token] for token in tokens]
        docids = set.intersection(*docids_for_each_token) # union?
        if len(docids) == 0:
            docids = set.union(*docids_for_each_token)
        return [self.docid_to_doc[id] for id in docids]

    def tfidf(self, counts):
        """
        Calculates td.idf Weighting for the term in a document of the document collection
        :param counts: frequency list of the currect document
        :return: td.idf value for the current term in the currently analysed document
        """
        N = len(self.docid_to_doc)
        return {tok: tf * math.log(N/self.term_to_df[tok]) for tok,tf in counts.items() if tok in self.term_to_df}

    def cosine_similarity(self, docA, docB):
        """
        Calculates the Cosine Similarity for two documents.
        :param docA: Document
        :param docB: Document to compare
        :return: value for Cosine Similarity
        """
        weightedA = self.tfidf(docA.token_counts)
        weightedB = self.tfidf(docB.token_counts)
        dotAB = dot(weightedA, weightedB)
        normA = math.sqrt(dot(weightedA, weightedA))
        normB = math.sqrt(dot(weightedB, weightedB))
        if (normA == 0 or normB == 0): # check for equal 0, to avoid division by 0.
            return 0
        else:
            return dotAB / (normA * normB)

class SearchEngine:
    """
    Preprocess the query and calls the method of DocumentCollection to get a ranked lists of documents
    for a query. Additionaly selects text snippets from the result documents
    """
    def __init__(self, doc_collection):
        """
        assigns the class variable doc_collection with a given instance of DocumentCollection
        :param doc_collection: Isntance of class DocumentCollection
        """
        self.doc_collection = doc_collection

    def ranked_documents(self, query):
        """
        gets search querey and calls methods of DocumentCollection to get a list of search results
        resulting list is sorted by the cosine similarty to the query to get the most relevant documents first
        :param query:
        :return:
        """
        query_doc = TextDocument(query)
        query_tokens = query_doc.token_counts.keys()
        docs = self.doc_collection.docs_with_all_tokens(query_tokens)
        docs_sims = [(doc, self.doc_collection.cosine_similarity(query_doc, doc)) for doc in docs]
        return sorted(docs_sims, key=lambda x: -x[1])

    def snippets(self, query, document, window=50):
        """
        calculates text snippets of a defined length for a document based on the given query.
        :param query: Query with search terms
        :param document: Instance of class TExtDocument
        :param window: length of text snippet before and after the search term

        """
        tokens = normalized_tokens(query)
        text = document.text
        liste_snippet = []
        for token in tokens:
            i = 0
            for snippet in liste_snippet:
                start = snippet.lower().find(token.lower())
                if start > -1:
                    end = start + len(token)
                    liste_snippet[i] = (snippet[0:start-1] + " [" + snippet[start:end] + "]" + snippet[end:])

                    i += 1
            if i == 0: #not found in liste_snippet
                start = text.lower().find(token.lower())
                if -1 == start: # position; nicht gefunden.
                    continue
                end = start + len(token)
                left = "..." + text[start-window:start]
                middle = "["+ text[start: end] +"]"
                right = text[end:end+window] + "..."
                liste_snippet.append(left + middle + right)

        for snippet in liste_snippet:
            yield snippet
