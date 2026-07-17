#include <limits.h>

int divide(const int dividend, const int divisor) {
    // Handle the edge case of overflow
    if (dividend == INT_MIN && divisor == -1) {
        return INT_MAX;
    }

    // Handle divisor equals 1 or -1 for INT_MIN directly
    if (divisor == 1) {
        return dividend;
    }
    if (divisor == -1) {
        return -dividend;
    }

    // Determine if the result will be negative
    const int negative = (dividend < 0) ^ (divisor < 0);

    // Work with absolute values using long long to avoid overflow
    long long dividend_abs =(long long)dividend < 0 ? -(long long)dividend : (long long)dividend;
    const long long divisor_abs = (long long)divisor < 0 ? -(long long)divisor : (long long)divisor;

    int quotient = 0;
    while (dividend_abs >= divisor_abs) {
        long long temp = divisor_abs;
        long long multiple = 1;
        while (dividend_abs >= (temp << 1)) {
            temp <<= 1;
            multiple <<= 1;
        }
        dividend_abs -= temp;
        quotient += multiple;
    }

    // Apply the sign to the quotient
    return negative ? -quotient : quotient;
}
