import unittest

from src.taxonomy.utils import parse_taxonomy


class TestTaxonomyFunctions(unittest.TestCase):
    def test_parse_taxonomy(self):
        # Test with a simple taxonomy string
        taxonomy_string = "Animal{Mammal,Bird{Fish,Reptile}, Invertebrate}"

        tree = parse_taxonomy(taxonomy_string)

        # Assert that the tree structure is built correctly
        self.assertTrue(tree.contains("Taxonomy"))
        self.assertTrue(tree.contains("Animal"))
        self.assertTrue(tree.contains("Mammal"))
        self.assertTrue(tree.contains("Bird"))
        self.assertTrue(tree.contains("Fish"))
        self.assertTrue(tree.contains("Reptile"))
        self.assertTrue(tree.contains("Invertebrate"))


if __name__ == '__main__':
    unittest.main()
