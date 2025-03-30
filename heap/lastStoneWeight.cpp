#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int lastStoneWeight(vector<int>& stones) {
    priority_queue<int> maxHeap(stones.begin(), stones.end());

    while (maxHeap.size() > 1) {
        // Fetch top two stones:
        const int heavierStone = maxHeap.top(); maxHeap.pop();
        const int lighterStone = maxHeap.top(); maxHeap.pop();

        const int newStone = heavierStone - lighterStone;
        if (newStone) maxHeap.push(newStone);
    }

    return maxHeap.empty() ? 0 : maxHeap.top();
}

// Test cases:
int main() {
    vector<int> stones{2, 7, 4, 1, 8, 1};
    cout << lastStoneWeight(stones) << endl; // Output: 1

    vector<int> stones2{1, 3};
    cout << lastStoneWeight(stones2); // Output: 2
    cout << endl;

    return 0;
}