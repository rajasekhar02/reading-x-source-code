let tree = {
    val: "a",
    left: {
        val: "a"
    },
    right: {
        val: "b",
        left:  {
            val: "b"
        },
        right:{
            val: "b",
            left:  {
                val: "b"
            },
            right:{
                val: "b"
            }
        }
    }
}


let tree2 = {
    val: "a",
    left: {
        val: "a"
    },
    right: {
        val: "b",
        left:  {
            val: "b"
        },
        right:{
            val: "b",
            right:{
                val: "b"
            }
        }
    }
}

function cnt_unival(root){
    if(root == undefined){
        return [true,0]
    }
    if(root.left == undefined && root.right == undefined){
        return [true, 1];
    }
    
    let currNodesVals = [root.val]
    let [left_isunival, left_subtree_cnt] = cnt_unival(root.left)
    if(root.left != undefined){
        currNodesVals.push(root.left.val)
    }
    
    
    let [right_isunival, right_subtree_cnt] = cnt_unival(root.right)
    if(root.right != undefined){
        currNodesVals.push(root.right.val)
    }
    
    let is_root_unival = left_isunival && right_isunival && (new Set(currNodesVals).size === 1)

    return [is_root_unival, is_root_unival + left_subtree_cnt + right_subtree_cnt]
    
}

console.log(cnt_unival(tree2))
