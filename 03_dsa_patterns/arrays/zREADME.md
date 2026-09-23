## Second Largest Distinct Element

### Problem clues

- "distinct" → `set()`
- "largest" → sorting / max
- "second largest" → second-last after sorting

### Simple Python approach

```python
nums = sorted(set(arr))
return nums[-2]