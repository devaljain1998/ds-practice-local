#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <string>
using namespace std;

int main() {
    vector<int> v1 = {1, 2, 3, 4, 5};
    // Print vector v1:
    // using copy:
    copy(v1.begin(), v1.end(), ostream_iterator<int>(cout, " "));
    cout << endl;

    // Print a vector with pair of int and string:
    vector<pair<int, string>> v2 = {{1, "one"}, {2, "two"}, {3, "three"}};
    // using copy:
    copy(v2.begin(), v2.end(), ostream_iterator<pair<int, string>>(cout, " "));
    cout << endl;
}