var lcaDeepestLeaves = function(root) {
    const helper = (node) => {
        if (!node) return [0, null];

        let [ldepth, llca] = helper(node.left);
        let [rdepth, rlca] = helper(node.right);

        if (ldepth === rdepth) {
            return [ldepth + 1, node];
        } else if (ldepth > rdepth) {
            return [ldepth + 1, llca];
        } else {
            return [rdepth + 1, rlca];
        }
    };

    return helper(root)[1];
};