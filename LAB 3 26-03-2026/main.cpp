// https://takeuforward.org/plus/dsa/problems/n-queen?tab=editorial

// https://takeuforward.org/data-structure/n-queen-problem-return-all-distinct-solutions-to-the-n-queens-puzzle

// https://leetcode.com/problems/n-queens/

class Solution {
    bool check(int row, int col, vector<string> &curr, int n) {
        // Check column conflict
        for (int i = 0; i < row; i++) {
            if (curr[i][col] == 'Q') return false;
        }

        // Check top-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (curr[i][j] == 'Q') return false;
        }

        // Check top-right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (curr[i][j] == 'Q') return false;
        }

        return true;
    }

    void generate(int row, int n, vector<string> &curr, vector<vector<string>> &ans) {
        if (row == n) {
            ans.push_back(curr);
            return;
        }

        for (int col = 0; col < n; col++) {
            if (check(row, col, curr, n)) {
                string s(n, '.');
                s[col] = 'Q';
                curr.push_back(s);
                generate(row + 1, n, curr, ans);
                curr.pop_back();
            }
        }
    }

public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        vector<string> temp;
        generate(0, n, temp, ans);
        return ans;
    }
};
