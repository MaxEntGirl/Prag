from unittest import TestCase
from hw04_text_search.text_vectors import TextDocument, DocumentCollection, SearchEngine

class DocumentCollectionTest(TestCase):

    def setUp(self):
        test_doc_list = [TextDocument(text_and_id[0], text_and_id[1]) for text_and_id in
                         [("the cat sat on a mat", "doc1"),
                          ("a rose is a rose", "doc2")]]
        self.small_collection = DocumentCollection.from_document_list(test_doc_list)

        # TODO: uncomment in case tests need access to whole document collection.
        #this_dir = os.path.dirname(os.path.abspath(__file__))
        #document_dir = os.path.join(this_dir, os.pardir, 'data/enron/enron1/ham/')
        #self.large_collection = DocumentCollection.from_dir(document_dir, ".txt")

    def test_unknown_word_cosine(self):
        """ Return 0 if cosine similarity is called for documents with only out-of-vocabulary words. """
        # Document that only contains words that never occurred in the document collection.
        query_doc = TextDocument(text="unknownwords", id=None)
        # Some document from collection.
        collection_doc = self.small_collection.docid_to_doc["doc1"]
        # Similarity should be zero (instead of undefined).
        self.assertEqual(self.small_collection.cosine_similarity(query_doc, collection_doc), 0.)

class TextDocumentTest(TestCase):
    def setUp(self):
        self.test_reply_email = TextDocument(">>>>forword", "doc1")
    # TODO: Unittests for TextDocument go here.
    def test_remove_mark(self):
        nach_remove = "forword"
        self.assertEqual(self.test_reply_email.text, nach_remove)

class SearchEngineTest(TestCase):
    def setUp(self):
        test_doc_list = [TextDocument("the cat sat\non a mat", "doc1")]

        self.small_collection = DocumentCollection.from_document_list(test_doc_list)
        self.searcher =  SearchEngine(self.small_collection)

    # TODO: Unittests for SearchEngine go here.
    def test_line_breaks(self):
        test_snippet = "...the [cat] sat on a mat..."
        query = "cat"
        top_docs = self.searcher.ranked_documents(query)

        for doc, sim in top_docs:
            for snippet in self.searcher.snippets(query, doc):
                self.assertEqual(snippet, test_snippet)

    def test_several_search(self):
        test_snippet = ["...the [cat] [sat] on a [mat]..."]
        query = "cat sat mat"
        top_docs = self.searcher.ranked_documents(query)
        liste_snippet = []
        for doc, sim in top_docs:
            for snippet in self.searcher.snippets(query, doc):
                liste_snippet.append(snippet)

        self.assertEqual(liste_snippet, test_snippet)

    def test_at_least_one_of_the_tokens(self):
        test_doc_list = [TextDocument("there is a city named New York", "doc1"), TextDocument("In Britain there is a city named York", "doc2")]
        expected_list = ['doc1', 'doc2']
        small_collection = DocumentCollection.from_document_list(test_doc_list)
        searcher =  SearchEngine(small_collection)
        query = "New York Britain"
        top_docs = searcher.ranked_documents(query)

        result_list = []
        for doc, sim in top_docs:
            result_list.append(doc.id)

        self.assertEqual(result_list, expected_list)