#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
using namespace std;

int main() {
    vector<int> v;
    // Insert random values into the vector:
    for (int i = 0; i < 10; i++) {
        const int randomValue = rand() % 100;
        v.push_back(randomValue);
    }

    // Print the vector:
    cout << "Vector: ";
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    // Insert random values into the set:
    set<int> s(v.begin(), v.end());
    cout << "Set: ";
    for (auto it = s.begin(); it != s.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    // Insert random values into unordered_set:
    unordered_set<int> us(v.begin(), v.end());
    cout << "Unordered Set: ";
    for (auto it = us.begin(); it != us.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    // Insert random values into the multiset:
    multiset<int> ms(v.begin(), v.end());
    cout << "Multiset: ";
    for (auto it = ms.begin(); it != ms.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    // Insert random values into the unordered_multiset:
    unordered_multiset<int> ums(v.begin(), v.end());
    cout << "Unordered Multiset: ";
    for (auto it = ums.begin(); it != ums.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    // Insert random values into the map:
    map<int, int> m;
    for (int i = 0; i < v.size(); i++) {
        m[v[i]] = i;
    }
    cout << "Map: ";
    for (const auto &p: m) {
        cout << p.first << "," << p.second << "| ";
    }
    cout << endl;

    return 0;
}