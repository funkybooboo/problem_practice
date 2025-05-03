SELECT
    N,
    CASE
        -- If the parent is NULL, this is the root node
        WHEN P IS NULL THEN 'Root'

        -- If the node is never a parent to any other node, it's a leaf
        WHEN N NOT IN (
            SELECT DISTINCT P  -- Get all nodes that appear as a parent
            FROM BST
            WHERE P IS NOT NULL  -- Exclude NULLs to avoid including root
        ) THEN 'Leaf'

        -- Otherwise, it's an inner node (has a parent and at least one child)
        ELSE 'Inner'
    END AS NodeType
FROM BST
ORDER BY N;

