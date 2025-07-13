from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        # Map each word to its index for quick lookup
        wordIndex = {word: idx for idx, word in enumerate(wordList)}
        wordCount = len(wordList)
        wordLength = len(wordList[0])

        # Build adjacency list: connect words that differ by one letter
        adj = [[] for _ in range(wordCount)]
        for i in range(wordCount):
            for j in range(i + 1, wordCount):
                if self.is_one_letter_diff(wordList[i], wordList[j]):
                    adj[i].append(j)
                    adj[j].append(i)

        # Initialize BFS queue with neighbors of beginWord
        queue = deque()
        visited = set()
        steps = 1  # Includes beginWord

        for i in range(wordLength):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == beginWord[i]:
                    continue
                candidate = beginWord[:i] + c + beginWord[i+1:]
                if candidate in wordIndex:
                    idx = wordIndex[candidate]
                    queue.append(idx)
                    visited.add(idx)

        # Perform BFS
        while queue:
            steps += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                if wordList[current] == endWord:
                    return steps
                for neighbor in adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return 0

    def is_one_letter_diff(self, word1: str, word2: str) -> bool:
        diff = 0
        for a, b in zip(word1, word2):
            if a != b:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1
