public class Node<T extends Comparable<T>> {
  private T data;
  private Node<T> left;
  private Node<T> right;

  /**
   * Constructor for a generic Node.
   * A Node contains data, a left child, and a right child.
   *
   * @param data The data to be stored in the Node.
   */
  public Node(T data) {
    this.data = data;
    left = null;
    right = null;
  }

  public T getData() {
    return data;
  }

  public Node<T> getLeft() {
    return left;
  }

  public Node<T> getRight() {
    return right;
  }

  public void setData(T data) {
    this.data = data;
  }

  public void setLeft(Node<T> left) {
    this.left = left;
  }

  public void setRight(Node<T> right) {
    this.right = right;
  }

  public String toString() {
    return data.toString();
  }
}
