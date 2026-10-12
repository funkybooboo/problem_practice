#include "darts.h"

bool isInside(coordinate_t circle_cords, float radius, coordinate_t cords) {
    return (cords.x - circle_cords.x) * (cords.x - circle_cords.x) +
    (cords.y - circle_cords.y) * (cords.y - circle_cords.y) <=
    radius * radius;
}

uint8_t score(coordinate_t cords) {
    coordinate_t center = { 0.0F, 0.0F };
    if (isInside(center, 1.0F, cords)) {
        return 10;
    } else if (isInside(center, 5.0F, cords)) {
        return 5;
    } else if (isInside(center, 10.0F, cords)) {
        return 1;
    } else {
        return 0;
    }
}
