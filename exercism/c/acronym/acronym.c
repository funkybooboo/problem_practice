#include "acronym.h"
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

char *abbreviate(const char *phrase) {
    if (phrase == NULL || strlen(phrase) == 0) {
        return NULL;
    }

    char *abbrev = malloc(strlen(phrase) + 1);
    if (!abbrev) {
        return NULL;
    }

    size_t j = 0;
    bool new_word = true;

    for (size_t i = 0; phrase[i] != '\0'; i++) {
        if (isalpha(phrase[i])) {
            if (new_word) {
                abbrev[j++] = toupper(phrase[i]);
                new_word = false;
            }
        } else if (phrase[i] != '\'') {
            new_word = true;
        }
    }

    abbrev[j] = '\0';
    return abbrev;
}
