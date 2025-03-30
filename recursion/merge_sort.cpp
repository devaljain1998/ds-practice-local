#include <iostream>
#include <vector>
using namespace std;

vector<int> merge(const vector<int> left, const vector<int> right) {
    int i = 0, j = 0, k = 0;
    int m = left.size() - 1, n = right.size() - 1;

    vector<int> arr(m + n);
    for (i = 0; i < (m + n) && j < m && k < n; i++) {
        if (left[j] <= right[k])
            arr[i] = left[i++];
        else
            arr[i] = right[k++];        
    }

    while (i < (m + n) && j < m) arr[i++] = left[j++];

    while (i < (m + n) && k < n) arr[i++] = right[k++];

    return arr;
};

vector<int> mergeSort(const int start, const int end, vector<int> v) {
    // Base condition:
    const int size = end - start;
    if (size <= 1) return v;
    if (size == 2) {
        if (v[0] > v[1]) swap(v[0], v[1]);
        return v;
    }

    // Recursion:
    const int mid = (start + end) / 2;
    vector<int> left = mergeSort(start, mid, v);
    vector<int> right = mergeSort(mid+1, end, v);

    return merge(left, right);
};

int main() {
    vector<int> v{5, 4, 3, 2, 1};
    const auto result = mergeSort(0, v.size() - 1, v);
    for (const auto n: result) cout << n << " ";
    cout << endl;
}