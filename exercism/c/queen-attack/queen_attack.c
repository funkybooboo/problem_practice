#include "queen_attack.h"


attack_status_t can_attack(position_t queen_1, position_t queen_2) {
    if (queen_1.row >= 8 ||
        queen_1.column >= 8 ||
        queen_2.row >= 8 ||
        queen_2.column >= 8 ||
        (queen_1.row == queen_2.row && queen_1.column == queen_2.column)
    ) {
        return INVALID_POSITION;
    }

    if (queen_1.row == queen_2.row || queen_1.column == queen_2.column) {
        return CAN_ATTACK;
    }

    // top left diagonal
    int row = queen_1.row;
    int column = queen_1.column;
    while (row >= 0 && column >= 0) {
        row--;
        column--;
        if (row == queen_2.row && column == queen_2.column) {
            return CAN_ATTACK;
        }
    }

    // bottom left diagonal
    row = queen_1.row;
    column = queen_1.column;
    while (row < 8 && column >= 0) {
        row++;
        column--;
        if (row == queen_2.row && column == queen_2.column) {
            return CAN_ATTACK;
        }
    }

    // top right diagonal
    row = queen_1.row;
    column = queen_1.column;
    while (row >= 0 && column < 8) {
        row--;
        column++;
        if (row == queen_2.row && column == queen_2.column) {
            return CAN_ATTACK;
        }
    }

    // bottom right diagonal
    row = queen_1.row;
    column = queen_1.column;
    while (row < 8 && column < 8) {
        row++;
        column++;
        if (row == queen_2.row && column == queen_2.column) {
            return CAN_ATTACK;
        }
    }

    return CAN_NOT_ATTACK;
}

