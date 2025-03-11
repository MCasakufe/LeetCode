long long countOfSubstrings(char* word, int k) {
    int n = strlen(word);
    if (n < 5 + k) return 0;

    static int prefix[100001][6];
    memset(prefix, 0, sizeof(prefix));

    for (int i = 0; i < n; i++) {
        for (int x = 0; x < 6; x++) prefix[i + 1][x] = prefix[i][x];
        switch (word[i]) {
            case 'a': prefix[i + 1][0]++; break;
            case 'e': prefix[i + 1][1]++; break;
            case 'i': prefix[i + 1][2]++; break;
            case 'o': prefix[i + 1][3]++; break;
            case 'u': prefix[i + 1][4]++; break;
            default:  prefix[i + 1][5]++; break;
        }
    }

    int valid(int start, int mid) {
        int freq[6];
        for (int x = 0; x < 6; x++)
            freq[x] = prefix[mid + 1][x] - prefix[start][x];
        if (freq[5] != k) return 0;
        for (int x = 0; x < 5; x++)
            if (freq[x] < 1) return 0;
        return 1;
    }

    long long ans = 0;
    for (int start = 0; start + 5 + k <= n; start++) {
        int left = start + 5 + k - 1, right = n - 1, bestLeft = -1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (valid(start, mid)) {
                bestLeft = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        if (bestLeft == -1) continue;

        left = bestLeft; right = n - 1;
        int bestRight = bestLeft;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (valid(start, mid)) {
                bestRight = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        ans += (bestRight - bestLeft + 1);
    }
    return ans;
}
