class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> ans = new ArrayList<>();
        if (root == null) return ans;
        dfs(root, "", ans);
        return ans;
    }

    // Fixed: Properly declared as a void dfs helper method with parameters
    private void dfs(TreeNode root, String path, List<String> ans) {
        if (root == null) return;

        // Construct the path string
        if (path.length() == 0) {
            path = "" + root.val;
        } else {
            path = path + "->" + root.val;
        }

        // Base case: Leaf node reached
        if (root.left == null && root.right == null) {
            ans.add(path);
            return;
        }

        // Recursively traverse child nodes
        dfs(root.left, path, ans);
        dfs(root.right, path, ans);
    }
}
