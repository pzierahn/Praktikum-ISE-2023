import unittest

from src.taxonomy.parser import parse_nodes


class TestTaxonomyParser(unittest.TestCase):

    def test_valid_taxonomy(self):
        taxonomy = "Animal{Mammal,Bird{Fish,Reptile}, Invertebrate}"
        result = parse_nodes(taxonomy)

        self.assertIsNotNone(result)

        self.assertEqual(len(result), 1)
        root_node = result[0]
        self.assertEqual(root_node.name, "Animal")
        self.assertEqual(len(root_node.children), 3)

        mammal_node = root_node.children[0]
        self.assertEqual(mammal_node.name, "Mammal")
        self.assertEqual(len(mammal_node.children), 0)

        bird_node = root_node.children[1]
        self.assertEqual(bird_node.name, "Bird")
        self.assertEqual(len(bird_node.children), 2)

        fish_node = bird_node.children[0]
        self.assertEqual(fish_node.name, "Fish")
        self.assertEqual(len(fish_node.children), 0)

        reptile_node = bird_node.children[1]
        self.assertEqual(reptile_node.name, "Reptile")
        self.assertEqual(len(reptile_node.children), 0)

        invertebrate_node = root_node.children[2]
        self.assertEqual(invertebrate_node.name, "Invertebrate")
        self.assertEqual(len(invertebrate_node.children), 0)

    def test_invalid_taxonomy(self):
        invalid_taxonomies = [
            "{Animal,{Mammal,Bird,Reptile},Invertebrate}",  # Mismatched '{' and '}'
            "{Animal,{Mammal,{Bird,Reptile},Invertebrate}",  # Mismatched '{' and '}'
            "{Animal,Mammal,}Invertebrate",  # Mismatched '{' and '}'
            "{Animal,{Mammal,,Bird},Invertebrate}",  # Empty node name
            "{Animal,{Mammal,Bird,},Invertebrate}",  # Empty node name
            "{Animal,{Mammal,{Bird,},Invertebrate}",  # Empty node name
            "{Animal,{Mammal,Bird,,Reptile},Invertebrate}",  # Empty node name
        ]

        for invalid_taxonomy in invalid_taxonomies:
            with self.subTest(invalid_taxonomy=invalid_taxonomy):
                result = parse_nodes(invalid_taxonomy)
                self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
