#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> previousSmaller(vector<int> &arr) {
    const int endElement = -1;
    vector<int> previousSmallerIndex(arr.size());
    stack<int> s;

    for (int i = 0; i < arr.size(); i++) {
        while (!s.empty() && arr[s.top()] >= arr[i]) {
            s.pop();
        }
        previousSmallerIndex[i] = s.empty() ? endElement : s.top();
        s.push(i);
    }

    return previousSmallerIndex;
}

vector<int> nextSmaller(vector<int> &arr) {
    const int endElement = arr.size();
    vector<int> nextSmallerIndex(arr.size());
    stack<int> s;

    for (int i = arr.size() - 1; i >= 0; i--) {
        while (!s.empty() && arr[s.top()] >= arr[i]) {
            s.pop();
        }
        nextSmallerIndex[i] = s.empty() ? endElement : s.top();
        s.push(i);
    }

    return nextSmallerIndex;
}

int largestRectangleArea(vector<int> &heights) {
    vector<int> left = previousSmaller(heights);
    vector<int> right = nextSmaller(heights);

    int maxArea = 0;
    for (int i = 0; i < heights.size(); i++) {
        int width = right[i] - left[i] - 1;
        maxArea = max(maxArea, heights[i] * width);
    }

    return maxArea;
}

int main() {
    vector<int> v{2, 1, 5, 6, 2, 3};
    cout << largestRectangleArea(v) << endl;
    return 0;
}