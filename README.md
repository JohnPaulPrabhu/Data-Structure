# Data-Structure

A small, growing collection of **data structure & algorithm** implementations in **Python**. Right now the repo focuses on classic **sorting** routines; it’s structured so you can add more topics (arrays/strings, stacks/queues, trees, graphs, DP, etc.) as you go.

> Current layout (as of this README): a top‑level `sort/` package and this README. Python is the only language in the repo.

---

## 📁 Project Structure

```
Data-Structure/
├─ sort/
│  ├─ # sorting algorithms live here (see below)
└─ README.md
```

Recommended convention inside `sort/` (one file per algorithm):

```
sort/
├─ bubble_sort.py
├─ selection_sort.py
├─ insertion_sort.py
├─ merge_sort.py
├─ quick_sort.py
├─ heap_sort.py
├─ tim_sort.py (Python's default algorithm)
└─ counting_sort.py
```

Each file should export a pure function (e.g., `bubble_sort(arr)`), document complexity, and include a minimal `if __name__ == "__main__":` demo.

---

## 🚀 Quick Start

### 1) Clone

```bash
git clone https://github.com/JohnPaulPrabhu/Data-Structure.git
cd Data-Structure
```

### 2) (Optional) Create a virtual environment

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

> No external dependencies are required for the algorithms; the standard library is enough.

### 3) Run an algorithm demo

```bash
python sort/quick_sort.py
```

Or import from another script / notebook:

```python
from sort.quick_sort import quick_sort
print(quick_sort([3,1,4,1,5,9]))
```


---

## 📚 Complexity Cheatsheet

| Algorithm      | Stable | Time (avg/worst)       |   Space  |
| -------------- | :----: | ---------------------- | :------: |
| Bubble Sort    |    ✅   | O(n²)/O(n²)            |   O(1)   |
| Selection Sort |    ❌   | O(n²)/O(n²)            |   O(1)   |
| Insertion Sort |    ✅   | O(n²)/O(n²), best O(n) |   O(1)   |
| Merge Sort     |    ✅   | O(n log n)/O(n log n)  |   O(n)   |
| Quick Sort     |    ❌   | O(n log n)/O(n²)       | O(log n) |
| Heap Sort      |    ❌   | O(n log n)/O(n log n)  |   O(1)   |

---

## 🤝 Contributing

* Keep one algorithm per file with a short docstring.
* Include a small demo in `__main__` and at least one test.
* Use type hints and prefer immutable inputs (copy before sorting).

---

## 📄 License

MIT © John Paul Prabhu
