#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
using namespace std;


vector<int> fetchProcessIndices(vector<int> robots) {
    // Store the indexes of every element:
    unordered_map<int, vector<int> > indexMap;
    for (int i = 0; i < robots.size(); i++) {
        indexMap[robots[i]].push_back(i);
    }

    // Sort the robots:
    sort(robots.begin(), robots.end());

    // Calculate the sum of the robots:
    vector<int> robotSum(robots.size());
    for (int i = 0; i < robots.size(); i++) {
        robotSum[i] = robots[i];
        if (i > 0) {
            robotSum[i] += robotSum[i - 1];
        }        
    }


}

int main() {
//     STDIN          FUNCTION
// ------         -------------
// 4        →     the size of robots n = 4
// 4        →     robots = [4, 1, 2, 5]
// 1
// 2
// 5

// 1
// 4

    vector<int> robots = {4, 1, 2, 5};
    vector<int> result = fetchProcessIndices(robots);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << endl;
    }
    return 0;
}
