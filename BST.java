public class BST<T extends Comparable<T>> {
  private Node<T> root;

  public BST() {
    root = null;
  }

  public Node<T> getRoot() {
    return root;
  }

  /**
   * Insert a new node into the tree.
   * If the tree is empty, create a new node and set it as the root.
   * Otherwise, find the right place to insert the new node.
   * If the data is less than the root, go to the left subtree.
   * If the data is greater than the root, go to the right subtree.
   * Repeat the process until we find the right place to insert the new node.
   * If the data is already in the tree, do nothing.
   *
   * @param data the data to be inserted
   */
  public void insert(T data) {
    root = insert(root, data);
  }

  /**
   * This is an internal method to insert a new node into the tree.
   * Used in insert()
   *
   * @param node the root node of the tree
   * @param data the data to be inserted
   * @return the new node
   */
  Node<T> insert(Node<T> node, T data) {
    if (node == null) {
      node = new Node<T>(data);
    }
    // We use compareTo() to compare two generic objects
    if (data.compareTo(node.getData()) < 0) {
      node.setLeft(insert(node.getLeft(), data));
    } else if (data.compareTo(node.getData()) > 0) {
      node.setRight(insert(node.getRight(), data));
    }
    return node;
  }

  /**
   * Delete a node from the tree with the given data.
   * If the tree is empty, do nothing.
   * Otherwise, find the node with the given data.
   * If the data is less than the root, go to the left subtree.
   * If the data is greater than the root, go to the right subtree.
   * Repeat the process until we find the node with the given data.
   * If the node is found, delete it.
   * If the node is not found, do nothing.
   *
   * @param data the data to be deleted
   */
  public void delete(T data) {
    root = delete(root, data);
  }

  /**
   * This is an internal method to delete a node from the tree.
   * Used in delete()
   *
   * @param node the root node of the tree
   * @param data the data to be deleted
   * @return the new node
   */
  Node<T> delete(Node<T> node, T data) {
    if (node == null) {
      return node;
    }
    if (data.compareTo(node.getData()) < 0) {
      node.setLeft(delete(node.getLeft(), data));
    } else if (data.compareTo(node.getData()) > 0) {
      node.setRight(delete(node.getRight(), data));
    } else {
      // else is triggered when we find the node with the given data
      // node with only one child or no child
      if (node.getLeft() == null) {
        return node.getRight();
      } else if (node.getRight() == null) {
        return node.getLeft();
      }
      // node with two children: Get the inorder successor (smallest
      // in the right subtree)
      node.setData(minValue(node.getRight()));
      // Delete the inorder successor
      node.setRight(delete(node.getRight(), node.getData()));
    }
    return node;
  }

  /**
   * This is an internal method to calculate the minimum value of the tree.
   * Used in delete()
   *
   * @param node
   * @return the minimum value of the tree
   */
  private T minValue(Node<T> node) {
    T minv = node.getData();
    while (node.getLeft() != null) {
      minv = node.getLeft().getData();
      node = node.getLeft();
    }
    return minv;
  }

  /**
   * Traverse the tree in order. Print the data of each node.
   */
  void inorder() {
    inorder(root);
  }

  /**
   * This is an internal method to traverse the tree in order.
   * Used in inorder()
   *
   * @param node the root node of the tree
   */
  void inorder(Node<T> node) {
    if (node != null) {
      inorder(node.getLeft());
      System.out.print(node.getData() + " ");
      inorder(node.getRight());
    }
  }

  public static void main(String[] args) {
    // Several test cases for the BST class
    BST<Integer> bst = new BST<Integer>();
    bst.insert(5);
    bst.insert(3);
    bst.insert(7);
    bst.insert(2);
    bst.insert(4);
    bst.insert(6);
    bst.insert(8);
    bst.insert(1);
    bst.insert(9);
    bst.insert(10);
    bst.insert(11);

    System.out.println("Inorder traversal of the given tree");
    bst.inorder();
    System.out.println("\nThis should be 1 2 3 4 5 6 7 8 9 10 11");

    System.out.println("\nDelete 10");
    bst.delete(10);
    System.out.println("Inorder traversal of the modified tree");
    bst.inorder();

    System.out.println("\nDelete 7");
    bst.delete(7);
    System.out.println("Inorder traversal of the modified tree");
    bst.inorder();

    System.out.println("\nDelete 5");
    bst.delete(5);
    System.out.println("Inorder traversal of the modified tree");

    System.out.println("=".repeat(10));
    System.out.println("\nSTRING TREE TEST\n");
    System.out.println("=".repeat(10));

    BST<String> bst2 = new BST<String>();
    bst2.insert("E");
    bst2.insert("B");
    bst2.insert("G");
    bst2.insert("A");
    bst2.insert("C");
    bst2.insert("F");
    bst2.insert("H");
    bst2.insert("D");
    bst2.insert("I");
    bst2.insert("J");
    bst2.insert("K");

    System.out.println("Inorder traversal of the given tree");
    bst2.inorder();

    System.out.println("\nDelete E");
    bst2.delete("E");
    System.out.println("Inorder traversal of the modified tree");
    bst2.inorder();

    System.out.println("\nDelete G");
    bst2.delete("G");

    System.out.println("Inorder traversal of the modified tree");
    bst2.inorder();

  }
}