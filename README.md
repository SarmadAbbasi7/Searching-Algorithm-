# Binary Search and Linear Search Implementation

## Purpose of the Project
This project implements two fundamental searching algorithms: **Binary Search** and **Linear Search**. 
The purpose is to reinforce understanding of core data structures and searching algorithms while developing 
efficient, well-documented, and maintainable code.

---

## How to Run the Program

1. Clone the repository from GitHub:
   ```
   git clonehttps://github.com/SarmadAbbasi7/Searching-Algorithm-
   ```

2. Navigate to the project directory:
   ```
   cd Searching Algorithm 
   ```

3. Run the program file (Example in Python):
   ```
   python search_algorithms.py
   ```

4. Follow the on-screen instructions to test the algorithms.

---

## Time Complexity Analysis

### **Binary Search**
- **Best Case**: O(1)
- **Average Case**: O(log n)
- **Worst Case**: O(log n)
- The worst-case scenario occurs when the target value is not in the list or at the farthest ends of the search space.

### **Linear Search**
- **Best Case**: O(1)
- **Average Case**: O(n)
- **Worst Case**: O(n)
- The worst-case scenario occurs when the target value is the last element or not present.

---

## Worst-Case Example for Binary Search

Given a sorted list of numbers:
```
[1, 3, 5, 7, 9, 11, 13, 15, 17]
```
- Searching for a value like `18` (not in the list) triggers the **worst-case** scenario.

---

## Output Example
For a sorted array `[1, 3, 5, 7, 9]`:

1. **Binary Search**: Searching for `7`.
   - Output: `Element found at index 3`
   - Time complexity: O(log n)

2. **Linear Search**: Searching for `7`.
   - Output: `Element found at index 3`
   - Time complexity: O(n)

---

## Additional Notes
- Binary Search requires the input array to be sorted.
- Linear Search works for both sorted and unsorted arrays.
- The project includes test cases to validate the algorithms.
