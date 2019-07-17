function iterativeInOrderTraversal(tree, callback) {
	// O(n) time | O(n) space
	// let curr = tree
	// while (curr) {
	// 	if (curr.left && !curr.left.visited) {
	// 		curr = curr.left
	// 	} else {
	// 		if (!curr.visited) {
	// 			callback(curr)
	// 			curr.visited = true
	// 		}
	// 		if (curr.right && !curr.right.visited)
	// 			curr = curr.right
	// 		else {
	// 			curr = curr.parent
	// 		}
	// 	}
	// }
	// O(n) time | O(1) space
	let prev = null
	let curr = tree
	while (curr) {
		let next
		if (prev === curr.parent && curr.left) {
			next = curr.left
		} else if (prev !== curr.right && curr.right) {
			callback(curr)
			next = curr.right
		} else {
			if (!curr.left || !curr.right) {
				callback(curr)
			}
		 	next = curr.parent
		}
		prev = curr
		curr = next
	}
}

// Do not edit the line below.
exports.iterativeInOrderTraversal = iterativeInOrderTraversal;