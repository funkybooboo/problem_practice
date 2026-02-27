pub fn binarySearch(comptime T: type, target: T, items: []const T) ?usize {
    if (items.len == 0) return null;

    var left: usize = 0;
    var right: usize = items.len - 1;

    while (left <= right) {
        const mid: usize = left + (right - left) / 2;
        const current = items[mid];

        if (target > current) {
            left = mid + 1;
        } else if (target < current) {
            if (mid == 0) return null;
            right = mid - 1;
        } else {
            return mid;
        }
    }

    return null;
}
