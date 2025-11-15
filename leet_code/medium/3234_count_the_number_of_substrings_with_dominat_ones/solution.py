class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zero_pos = []
        for i, ch in enumerate(s):
            if ch == '0':
                zero_pos.append(i)
        m = len(zero_pos)

        ans = 0
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1

        import math
        ZMAX = int(math.sqrt(n)) + 2

        zero_prefix_index = [0] * (n + 1)
        zc = 0
        for idx in range(n):
            zero_prefix_index[idx] = zc
            if s[idx] == '0':
                zc += 1
        zero_prefix_index[n] = zc

        for i in range(n):
            base = zero_prefix_index[i]

            for z in range(1, ZMAX + 1):
                if base + z - 1 >= m:
                    break

                first_z_pos = zero_pos[base + z - 1]

                min_len = z + z * z
                required_end = i + min_len - 1
                end_low = max(first_z_pos, required_end)

                if base + z < m:
                    end_high = zero_pos[base + z] - 1
                else:
                    end_high = n - 1

                if end_low <= end_high:
                    ans += end_high - end_low + 1

        return ans
