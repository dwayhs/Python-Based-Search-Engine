import unittest

from py_search_engine.searchengine import (InvertedIndex, SearchIndex,
                                           SimpleIndexPipeline)
from tests.fixtures import load_document_fixture


class TestSearchIndex(unittest.TestCase):
    def setUp(self):
        self.test_documents = [
            load_document_fixture('document_a'),
            load_document_fixture('document_b'),
            load_document_fixture('document_c')
        ]

    def test_query_indexed_documents(self):
        search_index = SearchIndex(
            index_pipeline=SimpleIndexPipeline(indexed_columns=['text']),
            terms_store=InvertedIndex()
        )

        for document in self.test_documents:
            search_index.index(document)

        resulting_documents = search_index.search("President Trump")

        resulting_document_titles = [document['title']
                                     for document
                                     in resulting_documents]

        self.assertEquals(len(resulting_document_titles), 2)

        self.assertTrue('document b' in resulting_document_titles)
        self.assertTrue('document c' in resulting_document_titles)