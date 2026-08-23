#include "acronym.h"
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

char *abbreviate(const char *phrase) {
    char *abbereviation = "";
    size_t phrase_len = strlen(phrase);
    bool prev_is_space = false;
    char space = ' ';
    for (size_t i = 0; i < phrase_len; i++) {
        if (phrase[i] == space || (i == 0 && phrase[i] != space)) {
            prev_is_space = true;
            continue;
        }
        if (prev_is_space) {
            abbereviation += toupper(phrase[i]);
        }
        prev_is_space = false;
    }
    return abbereviation;
}
