#ifndef DARTS_H
#define DARTS_H

#include <stdint.h>
#include <stdbool.h>

typedef struct {
    float x;
    float y;
} coordinate_t;

bool isInside(coordinate_t circle_cords, float radius, coordinate_t cords);
uint8_t score(coordinate_t cords);

#endif
