#include <stdio.h>
#include <stdlib.h>

#define MOD 1000000007

static long long modPow(long long base, long long exp) {
    long long result = 1;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

static int primeFactorCount(int n) {
    int count = 0, f = 2;
    while (f * f <= n) {
        if (n % f == 0) {
            count++;
            while (n % f == 0) n /= f;
        }
        f = (f == 2 ? 3 : f + 2);
    }
    if (n > 1) count++;
    return count;
}

static long long possibleSubarrays(int *counts, int size, int idx) {
    int val = counts[idx], l = idx, r = idx;
    while (l > 0 && counts[l - 1] < val) l--;
    while (r < size - 1 && counts[r + 1] <= val) r++;
    return (long long)(r - idx + 1) * (idx - l + 1);
}

int maximumScore(int* nums, int numsSize, int k) {
    int *pf = malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) pf[i] = primeFactorCount(nums[i]);

    typedef struct { int val, idx; } Pair;
    Pair *arr = malloc(numsSize * sizeof(Pair));
    for (int i = 0; i < numsSize; i++) {
        arr[i].val = nums[i]; arr[i].idx = i;
    }

    int compare(const void* a, const void* b) {
        return ((Pair*)b)->val - ((Pair*)a)->val;
    }
    qsort(arr, numsSize, sizeof(Pair), compare);

    long long score = 1, ops = 0;
    for (int p = 0; p < numsSize && ops < k; p++) {
        long long canUse = possibleSubarrays(pf, numsSize, arr[p].idx);
        if (canUse > k - ops) canUse = k - ops;
        score = (score * modPow(arr[p].val, canUse)) % MOD;
        ops += canUse;
    }
    free(pf); free(arr);
    return (int)score;
}