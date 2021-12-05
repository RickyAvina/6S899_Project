''' This module mocks short term memory '''

from scipy.spatial import distance


class ShortTermMemory:
	'''
	Short Term memory which can memorize "k" input sequences of length "n"
	Sequences are "similar" if their hamming distance is "delta" away

	k: int
	l: int
	delta: int
	'''

	def __init__(self, k, n, delta):
		self.k = k
		self.n = n
		self.delta = delta
		self.sequences = [None for _ in range(k)]  # None or sequence

	def find_similar(self, input_sequence):
		''' 
		If the sequence is "close" to an existing sequence, return the index of that sequence.
		Return None otherwise.
		'''

		for index, sequence in enumerate(self.sequences):
			if sequence is None:
				return None
			else:
				# calculate hamming distance between se
				hamming_distance = distance.hamming(sequence, input_sequence) * self.n
				if hamming_distance <= self.delta:
					return index

		# should not get here, this means that we've gotten more than K input sequences
		raise ValueError("Sequences are filled, and similar sequence not found. Can either mean we've seen more than k sequences or hamming distance doesn't work.")

	def forward(self, input_sequence):
		if len(input_sequence) != self.n:
			raise ValueError(f"Input sequence is of length {len(input_sequence)}, however expected size {self.k}")

		# TODO: compression of input_sequence

		# compare similarity of sequence to other sequences
		similar_index = self.find_similar(input_sequence)
		
		if similar_index is not None:
			return similar_index

		# allocate new spot, if no spots available, this is an error
		for i in range(self.k):
			if self.sequences[i] is None:
				self.sequences[i] = input_sequence
				return i

		raise ValueError("No spots available")


if __name__ == '__main__':
	pass