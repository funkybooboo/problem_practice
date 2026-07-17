#include <stdlib.h>
#include <string.h>

int* findSubstring(char* s, char** words, int wordsSize, int* returnSize) {
    int wordLen = strlen(words[0]);
    int totalLen = wordLen * wordsSize;
    int sLen = strlen(s);
    *returnSize = 0;

    if (sLen < totalLen) {
        return malloc(0); // No possible matches
    }

    // Map each word to a unique index and count occurrences
    int* wordCount = calloc(wordsSize, sizeof(int));
    char** uniqueWords = malloc(wordsSize * sizeof(char*));
    int uniqueWordCount = 0;

    for (int i = 0; i < wordsSize; i++) {
        int found = -1;
        for (int j = 0; j < uniqueWordCount; j++) {
            if (strcmp(words[i], uniqueWords[j]) == 0) {
                found = j;
                break;
            }
        }
        if (found == -1) {
            uniqueWords[uniqueWordCount] = words[i];
            wordCount[uniqueWordCount]++;
            uniqueWordCount++;
        } else {
            wordCount[found]++;
        }
    }

    int* result = malloc(sLen * sizeof(int));
    int* seen = calloc(uniqueWordCount, sizeof(int));

    for (int i = 0; i < wordLen; i++) { // Sliding window for each offset
        int left = i, count = 0;
        memset(seen, 0, uniqueWordCount * sizeof(int));

        for (int right = i; right + wordLen <= sLen; right += wordLen) {
            char* sub = s + right;
            int index = -1;

            for (int j = 0; j < uniqueWordCount; j++) {
                if (strncmp(sub, uniqueWords[j], wordLen) == 0) {
                    index = j;
                    break;
                }
            }

            if (index != -1) {
                seen[index]++;
                count++;

                while (seen[index] > wordCount[index]) {
                    char* leftSub = s + left;
                    for (int j = 0; j < uniqueWordCount; j++) {
                        if (strncmp(leftSub, uniqueWords[j], wordLen) == 0) {
                            seen[j]--;
                            break;
                        }
                    }
                    left += wordLen;
                    count--;
                }

                if (count == wordsSize) {
                    result[(*returnSize)++] = left;
                }
            } else {
                memset(seen, 0, uniqueWordCount * sizeof(int));
                count = 0;
                left = right + wordLen;
            }
        }
    }

    free(uniqueWords);
    free(wordCount);
    free(seen);

    return result;
}
