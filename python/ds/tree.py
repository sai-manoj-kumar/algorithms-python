__author__ = 'saimanoj'


class TreeNode(object):
    """Class that holds every Node of the Tree.

    Attributes:
        data: contains data of this node, of any type.
        parent: TreeNode object corresponding to parent of this node.
        children: List of all TreeNode objects that are children of this node.
    """

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []


class RootNode(TreeNode):
    """Extends TreeNode and represents Root Node of the Tree.

    Attributes:
        data, parent and children are same as TreeNode.
        parent is always None for a RootNode.
    """

    def __init__(self, data):
        TreeNode.__init__(self, data, None)


class Tree(object):
    """Represents a Tree using TreeNode and RootNode classes.

    Attributes:
        root: RootNode object representing root of the tree.
    """
    def __init__(self, data):
        self.root = RootNode(data)

    def add(self, parent, child):
        child.parent = parent
        parent.children.append(child)


