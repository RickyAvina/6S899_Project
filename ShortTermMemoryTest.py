import sys
import unittest
from scipy.spatial import distance

sys.path.append(".")
from ShortTermMemory import ShortTermMemory


class MemoryTests(unittest.TestCase):

	def test_basic(self):
		stm = ShortTermMemory(k=2, n=2, delta=1)
		stm.forward([1, 2])

		for el in stm.sequences[1:]:
			self.assertIsNone(el)

		stm.forward([2,3])
		for el in stm.sequences:
			self.assertIsNotNone(el)

	def test_simimar(self):
		stm = ShortTermMemory(k=2, n=2, delta=1)
		stm.forward([1, 2])
		stm.forward([1, 2])

		for el in stm.sequences[1:]:
			self.assertIsNone(el)

		stm.forward([2, 3])
		for el in stm.sequences:
			self.assertIsNotNone(el)

		stm.forward([2, 3])
		stm.forward([1, 2])


	def test_hamming(self):
		def dist(seq, seq2, n):
			return distance.hamming(seq, seq2) * n

		d1 = dist([1, 2], [1, 3], 2)
		self.assertEqual(d1, 1)

		d2 = dist([1, 2], [1, 2], 2)
		self.assertEqual(d2, 0)

		d3 = dist([1, 2], [2, 1], 2)
		self.assertEqual(d3, 2)


	def test_similar_hamming(self):
		stm = ShortTermMemory(k=2, n=2, delta=1)
		stm.forward([1, 1])
		stm.forward([1, 2])
		stm.forward([2, 1])

		for el in stm.sequences[1:]:
			self.assertIsNone(el)


if __name__ == '__main__':
	unittest.main()