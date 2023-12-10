/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

 func copyRandomList(head *Node) *Node {
    if head == nil {
        return nil
    }
    nodeMap := make(map[*Node]*Node)
    current := head
    for current != nil {
        nodeMap[current] = &Node{Val: current.Val}
        current = current.Next
    }
    current = head
    for current != nil {
        copiedNode := nodeMap[current]
        copiedNode.Next = nodeMap[current.Next]
        current = current.Next
    }
    current = head
    for current != nil {
        copiedNode := nodeMap[current]
        copiedNode.Random = nodeMap[current.Random]
        current = current.Next
    }
    return nodeMap[head]
}