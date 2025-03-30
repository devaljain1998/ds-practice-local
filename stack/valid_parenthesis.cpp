#include <string>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <cassert>
using namespace std;

class Solution {
    public:
        bool isValid(string str) {
            unordered_set<char> openBrackets{'(', '[', '{'};
            unordered_set<char> closedBrackets{')', ']', '}'};
            unordered_map<char, char> openToCloseMap{{'(', ')'}, {'[', ']'}, {'{', '}'}};
            unordered_map<char, char> closeToOpenMap{{')', '('}, {']', '['}, {'}', '{'}};
    
    
            stack<char> s;
            
            for (const auto bracket: str) {
                // if in open brackets then push into stack:
                if (openBrackets.find(bracket) != openBrackets.end()) {
                    s.push(bracket);
                }
                
                // if they are in closed brackets then pop only if it is the reverse symbol:
                const char openBracket = closeToOpenMap[bracket];
                if (!s.empty() && s.top() == openBracket) {
                    s.pop();
                } else {
                    s.push(bracket);
                }
            }

            return s.empty();
        }
};

int main() {
    Solution s;

    // Test cases:
    // Test case 1:
    string tc1 = "()";
    assert(s.isValid(tc1) == true);

    // Test case 2:
    string tc2 = "()[]{}";
    assert(s.isValid(tc2) == true);

    // Test case 3:
    string tc3 = "(]";
    assert(s.isValid(tc3) == false);

    // Test case 4:
    string tc4 = "([)]";
    assert(s.isValid(tc4) == false);

    // Test case 5:
    string tc5 = "{[]}";
    assert(s.isValid(tc5) == true);

    return 0;
}