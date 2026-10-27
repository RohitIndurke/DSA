# Singly Linked List (SSL) Algorithms

## 1. Algorithm: Insert at Start

1. Start.
2. Create class `Node`.
   - `data ← data`
   - `next ← None`
3. Create class `SSL`.
4. Initialize `head ← None`.
5. Create function `insert_start(data)`.
6. Create a new node.
   - `new_node ← Node(data)`
7. Set `new_node.next ← head`.
8. Set `head ← new_node`.
9. Display "Inserted at start successfully".
10. End function.
11. Stop.

---

## 2. Algorithm: Insert at End

1. Start.
2. Create class `Node`.
   - `data ← data`
   - `next ← None`
3. Create class `SSL`.
4. Initialize `head ← None`.
5. Create function `insert_end(data)`.
6. Create a new node.
   - `new_node ← Node(data)`
7. If `head = None`, then:
   - `head ← new_node`
   - Return.
8. Otherwise, set `current ← head`.
9. Repeat while `current.next ≠ None`:
   - `current ← current.next`
10. Set `current.next ← new_node`.
11. Display "Inserted at end successfully".
12. End function.
13. Stop.

---

## 3. Algorithm: Insert at Position

**Note:** Position starts from `0`.

1. Start.
2. Create class `Node`.
3. Create class `SSL`.
4. Initialize `head ← None`.
5. Create function `insert_pos(pos, data)`.
6. If `pos < 0`, then:
   - Display "Invalid position".
   - Return.
7. Create a new node.
   - `new_node ← Node(data)`
8. If `pos = 0`, then:
   - `new_node.next ← head`
   - `head ← new_node`
   - Display "Inserted successfully".
   - Return.
9. Set `current ← head`.
10. Set `count ← 0`.
11. Repeat while `current ≠ None` AND `count < pos - 1`:
    - `current ← current.next`
    - `count ← count + 1`
12. If `current = None`, then:
    - Display "Invalid position".
    - Return.
13. Set `new_node.next ← current.next`.
14. Set `current.next ← new_node`.
15. Display "Inserted successfully".
16. End function.
17. Stop.

---

## 4. Algorithm: Delete from Start

1. Start.
2. Create class `Node`.
3. Create class `SSL`.
4. Initialize `head ← None`.
5. Create function `delete_start()`.
6. If `head = None`, then:
   - Display "List is empty".
   - Return.
7. Set `head ← head.next`.
8. Display "First node deleted successfully".
9. End function.
10. Stop.

---

## 5. Algorithm: Delete from End

1. Start.
2. Create class `Node`.
3. Create class `SSL`.
4. Initialize `head ← None`.
5. Create function `delete_end()`.
6. If `head = None`, then:
   - Display "List is empty".
   - Return.
7. If `head.next = None`, then:
   - Set `head ← None`.
   - Display "Last node deleted successfully".
   - Return.
8. Set `current ← head`.
9. Repeat while `current.next.next ≠ None`:
   - `current ← current.next`
10. Set `current.next ← None`.
11. Display "Last node deleted successfully".
12. End function.
13. Stop.

---

## 6. Algorithm: Delete from Position

**Note:** Position starts from `0`.

1. Start.
2. Create class `Node`.
3. Create class `SSL`.
4. Initialize `head ← None`.
5. Create function `delete_pos(pos)`.
6. If `head = None`, then:
   - Display "List is empty".
   - Return.
7. If `pos < 0`, then:
   - Display "Invalid position".
   - Return.
8. If `pos = 0`, then:
   - Set `head ← head.next`.
   - Display "Node deleted successfully".
   - Return.
9. Set `current ← head`.
10. Set `count ← 0`.
11. Repeat while `current.next ≠ None` AND `count < pos - 1`:
    - `current ← current.next`
    - `count ← count + 1`
12. If `current.next = None`, then:
    - Display "Invalid position".
    - Return.
13. Set `current.next ← current.next.next`.
14. Display "Node deleted successfully".
15. End function.
16. Stop.

---

## 7. Algorithm: Display Linked List

1. Start.
2. Create function `display()`.
3. If `head = None`, then:
   - Display "List is empty".
   - Return.
4. Set `current ← head`.
5. Repeat while `current ≠ None`:
   - Display `current.data`.
   - Set `current ← current.next`.
6. Display `None`.
7. End function.
8. Stop.

---

## Quick Revision for Your Exam

| Operation            | Main logic                                                     |
| -------------------- | -------------------------------------------------------------- |
| Insert at Start      | `new_node.next ← head`, then `head ← new_node`                 |
| Insert at End        | Traverse to the last node, then `current.next ← new_node`      |
| Insert at Position   | `new_node.next ← current.next`, then `current.next ← new_node` |
| Delete from Start    | `head ← head.next`                                             |
| Delete from End      | `current.next ← None`                                          |
| Delete from Position | `current.next ← current.next.next`                             |
| Display              | Traverse using `current` until `None`                          |
