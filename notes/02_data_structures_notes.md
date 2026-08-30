# 📦 Python Core: Data Structures

A data structure is a container used to organize, store, and manage data so that we can use it efficiently. In Python, there are 4 main built-in containers:

---

## 1. Lists
* **Definition:** A List is an ordered, changeable (mutable) collection that allows duplicate values.
* **Syntax:** `my_list = ["apple", "banana", "cherry"]` or `empty_list = []`

### Core Methods & Functions
* **`list.append(item)`**: Adds an item to the end of the list.
* **`list.insert(idx, item)`**: Adds an item at a specific position/index.
* **`list.remove(item)`**: Removes the first item with that value.
* **`list.pop(idx)`**: Removes and returns the item at `idx` (default is the last item).
* **`list.clear()`**: Removes all items, leaving the list empty.
* **`list.index(item)`**: Returns the index (position) of the first matching item.
* **`list.count(item)`**: Returns the number of times an item appears.
* **`list.sort()`**: Sorts the list in-place (ascending).
* **`list.reverse()`**: Reverses the order of the list in-place.
* **`list.extend(iterable)`**: Appends elements of another collection to the end.
* **`len(list)`**: Returns the number of items.

### List Slicing (`list[start:stop:step]`)
* `list[0]`: Gets the first item.
* `list[-1]`: Gets the last item.
* `list[1:3]`: Gets items at index 1 and 2 (excludes index 3).
* `list[:2]`: Gets everything from the start up to index 1.
* `list[::2]`: Gets every 2nd item in the list.

### Code Example
```python
names = ["Aman", "Rahul"]
names.append("Priya")       # ['Aman', 'Rahul', 'Priya']
names.insert(1, "Amit")     # ['Aman', 'Amit', 'Rahul', 'Priya']
names.remove("Rahul")       # ['Aman', 'Amit', 'Priya']
popped_name = names.pop()   # Removes 'Priya'
print(names)                # Output: ['Aman', 'Amit']
```

---

## 2. Tuples
* **Definition:** A Tuple is an ordered collection that CANNOT be changed (immutable) after it is created. It also allows duplicate values.
* **Syntax:** `my_tuple = ("red", "green", "blue")` or `empty_tuple = ()`
* **⚠️ Crucial Gotcha:** If you want to create a tuple with only 1 item, you MUST put a comma at the end:
  ```python
  single_item = ("apple",)   # Correct tuple
  not_a_tuple = ("apple")    # Just a string!
  ```

### Core Methods & Functions
Since tuples cannot be changed, they have very few methods:
* **`tuple.count(item)`**: Returns the number of times an item appears.
* **`tuple.index(item)`**: Returns the position/index of the first matching item.
* **`len(tuple)`**: Returns the number of items.

### Tuple Unpacking
You can extract values from a tuple directly into variables:
```python
coordinates = (40.7128, -74.0060)
lat, lon = coordinates
print(lat)  # 40.7128
print(lon)  # -74.0060
```

---

## 3. Dictionaries
* **Definition:** A Dictionary stores data in **Key-Value** pairs, similar to a real-world dictionary (Word ➔ Meaning). Keys must be unique and immutable, but values can be anything.
* **Syntax:** `my_dict = {"name": "Aman", "age": 22, "city": "Delhi"}`

### Core Methods & Functions
* **`dict[key] = value`**: Adds or updates a key-value pair.
* **`dict.get(key, default)`**: Safely returns value of `key`. Returns `default` if key is not found (prevents crash).
* **`dict.keys()`**: Returns a list-like view of all keys.
* **`dict.values()`**: Returns a list-like view of all values.
* **`dict.items()`**: Returns a list of `(key, value)` tuples.
* **`dict.pop(key)`**: Removes the key and returns its value.
* **`dict.popitem()`**: Removes and returns the last inserted key-value pair.
* **`dict.clear()`**: Empties the dictionary.

### Code Example
```python
student = {"name": "Aman", "grade": "A"}
print(student.get("age", "Not Found"))  # Outputs: Not Found (No crash!)

# Iterating keys and values
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")
```

---

## 4. Sets
* **Definition:** A Set is an unordered collection of unique items. No duplicates are allowed.
* **Syntax:** `my_set = {"apple", "banana", "cherry"}`
* **⚠️ Crucial Gotcha:** To create an empty set, you MUST use `set()`. Using `{}` creates an empty dictionary!

### Core Methods & Functions
* **`set.add(item)`**: Adds an item to the set.
* **`set.remove(item)`**: Removes an item. Crashes if not found.
* **`set.discard(item)`**: Removes an item safely. Does NOT crash if not found.
* **`set.pop()`**: Removes and returns a random item.
* **`set.clear()`**: Empties the set.

### Mathematical Set Operations
* **Union (`|`)**: Combines elements of both sets.
  ```python
  {1, 2} | {2, 3}  # Output: {1, 2, 3}
  ```
* **Intersection (`&`)**: Elements present in BOTH sets.
  ```python
  {1, 2} & {2, 3}  # Output: {2}
  ```
* **Difference (`-`)**: Elements in set A but NOT in set B.
  ```python
  {1, 2} - {2, 3}  # Output: {1}
  ```
* **Symmetric Difference (`^`)**: Elements in A or B, but NOT in both.
  ```python
  {1, 2} ^ {2, 3}  # Output: {1, 3}
  ```

---

## 📊 Summary Comparison Table

| Data Structure | Syntax | Ordered? | Mutable? | Duplicates? | Common Usage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | `[1, 2, 3]` | Yes | Yes | Yes | Dynamic collection of items |
| **Tuple** | `(1, 2, 3)` | Yes | No | Yes | Fixed records (coordinates, configs) |
| **Dictionary** | `{"key": "value"}` | Yes | Yes | Keys: No, Values: Yes | Key-value records |
| **Set** | `{1, 2, 3}` | No | Yes | No | Removing duplicates, math operations |
