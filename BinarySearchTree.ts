import { assertEquals } from "https://deno.land/std@0.201.0/assert/mod.ts";

type Maybe<T> = T | undefined;

class BST<T> {
  root?: BSTNode<T>;
  size = 0;

  constructor(public comparator: (a: T, b: T) => number) {}
  public insert(value: T): void {
    if (!this.root) {
      this.root = new BSTNode(value);
    } else {
      this.root.insert(value);
    }
    this.size++;
  }
  public search(value: T): Maybe<BSTNode<T>> {
    return this.root?.search(value);
  }

  public log(): void {
    console.log(this.root?.toString() ?? "Empty Tree");
  }
}

class BSTNode<T> {
  left?: BSTNode<T>;
  right?: BSTNode<T>;

  constructor(public value: T) {}

  public insert(value: T) {
    if (value < this.value) {
      if (!this.left) {
        this.left = new BSTNode(value);
      } else {
        this.left.insert(value);
      }
    } else {
      if (!this.right) {
        this.right = new BSTNode(value);
      } else {
        this.right.insert(value);
      }
    }
  }
  public search(value: T): Maybe<BSTNode<T>> {
    if (value === this.value) {
      return this;
    }
    if (value < this.value) {
      return this.left?.search(value);
    }
    return this.right?.search(value);
  }
  public min(): BSTNode<T> {
    return this.left?.min() ?? this;
  }

  toString() {
    const [lines] = this._displayAux();
    return lines.join("\n");
  }

  private _displayAux(): [string[], number, number, number] {
    // stolen from https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    if (!this.right && !this.left) {
      const line = `${this.value}`;
      const width = line.length;
      const height = 1;
      const middle = Math.floor(width / 2);
      return [[line], width, height, middle];
    }

    if (!this.right) {
      const [lines, n, p, x] = this.left!._displayAux();
      const s = `${this.value}`;
      const u = s.length;
      const firstLine = " ".repeat(x + 1) + "_".repeat(n - x - 1) + s;
      const secondLine = " ".repeat(x) + "/" + " ".repeat(n - x - 1 + u);
      const shiftedLines = lines.map((line) => line + " ".repeat(u));
      return [
        [firstLine, secondLine, ...shiftedLines],
        n + u,
        p + 2,
        n + Math.floor(u / 2),
      ];
    }

    if (!this.left) {
      const [lines, n, p, x] = this.right!._displayAux();
      const s = `${this.value}`;
      const u = s.length;
      const firstLine = s + "_".repeat(x) + " ".repeat(n - x);
      const secondLine = " ".repeat(u + x) + "\\" + " ".repeat(n - x - 1);
      const shiftedLines = lines.map((line) => " ".repeat(u) + line);
      return [
        [firstLine, secondLine, ...shiftedLines],
        n + u,
        p + 2,
        Math.floor(u / 2),
      ];
    }

    const [leftLines, n, p, x] = this.left!._displayAux();
    const [rightLines, m, q, y] = this.right!._displayAux();
    const s = `${this.value}`;
    const u = s.length;

    const firstLine =
      " ".repeat(x + 1) +
      "_".repeat(n - x - 1) +
      s +
      "_".repeat(y) +
      " ".repeat(m - y);
    const secondLine =
      " ".repeat(x) +
      "/" +
      " ".repeat(n - x - 1 + u + y) +
      "\\" +
      " ".repeat(m - y - 1);

    if (p < q) {
      leftLines.push(...new Array(q - p).fill(" ".repeat(n)));
    } else if (q < p) {
      rightLines.push(...new Array(p - q).fill(" ".repeat(m)));
    }

    const zippedLines: string[] = [];
    for (let i = 0; i < Math.max(leftLines.length, rightLines.length); i++) {
      const leftPart = leftLines[i] || " ".repeat(n);
      const rightPart = rightLines[i] || " ".repeat(m);
      zippedLines.push(leftPart + " ".repeat(u) + rightPart);
    }

    return [
      [firstLine, secondLine, ...zippedLines],
      n + m + u,
      Math.max(p, q) + 2,
      n + Math.floor(u / 2),
    ];
  }
}

function generateBSTs(
  n: number,
  generateBST: () => BST<number>,
  rng: () => number
) {
  const bst = generateBST();
  for (let i = 0; i < n; i++) {
    bst.insert(rng());
  }
  return bst;
}

Deno.test("Initial Creation", () => {
  const bst = new BST<number>(Math.sign);
  assertEquals(bst.root, undefined);
  assertEquals(bst.size, 0);
});

Deno.test("1 Insertion", () => {
  const bst = new BST<number>(Math.sign);
  bst.insert(1);
  assertEquals(bst.root?.value, 1);
  assertEquals(bst.size, 1);
});

Deno.test("2 Insertions", () => {
  const bst = new BST<number>(Math.sign);
  bst.insert(1);
  bst.insert(2);
  assertEquals(bst.root?.value, 1);
  assertEquals(bst.root?.right?.value, 2);
  assertEquals(bst.size, 2);
});

Deno.test("3 Insertions", () => {
  const bst = new BST<number>(Math.sign);
  bst.insert(1);
  bst.insert(2);
  bst.insert(3);
  assertEquals(bst.root?.value, 1);
  assertEquals(bst.root?.right?.value, 2);
  assertEquals(bst.root?.right?.right?.value, 3);
  assertEquals(bst.size, 3);
});

Deno.test("20 Insertions", () => {
  const bst = generateBSTs(
    100,
    () => new BST<number>(Math.sign),
    () => Math.floor(Math.random() * 100)
  );
  // assertEquals(bst.size, 20);
  bst.log();
});

Deno.test("3 sized search", () => {
  const bst = generateBSTs(
    3,
    () => new BST<number>(Math.sign),
    () => Math.floor(Math.random() * 100)
  );
  const value = Math.floor(Math.random() * 100);
  bst.insert(value);
  assertEquals(bst.search(value)?.value, value);
});

Deno.test("20 sized search", () => {
  const bst = generateBSTs(
    20,
    () => new BST<number>(Math.sign),
    () => Math.floor(Math.random() * 100)
  );
  const value = Math.floor(Math.random() * 100);
  bst.insert(value);
  assertEquals(bst.search(value)?.value, value);
});
