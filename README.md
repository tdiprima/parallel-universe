# parallel-universe
## JobLib Junction

`joblib` makes it stupid-easy to run things in parallel in Python. Instead of stressing about threading or managing processes yourself, you just wrap your functions and let `joblib` handle the CPU hustle. It's especially clutch for **embarrassingly parallel tasks** — basically when you're running the same function independently on a bunch of data chunks.

### 🧠 Key Features

* ⚡ **CPU parallelism** – Uses multiprocessing under the hood to dodge Python's GIL and fully tap into your CPU cores.
* 🧍‍♂️ **Simple API** – Just wrap your function with `delayed()` and pass it to `Parallel()`. No complicated setup.
* 🧮 **Automatic load balancing** – It spreads the work smartly across all available cores so you're not wasting resources.
* 🧠 **Memory efficient** – Plays super nicely with NumPy arrays and scientific computing workflows.

### 🧰 Basic Pattern

```python
from joblib import Parallel, delayed

results = Parallel(n_jobs=4)(
    delayed(function)(arg) for arg in args
)
```

This pattern is super popular in the scientific Python world (think scikit-learn, NumPy, etc.) because it nails the common use case of **applying the same function to multiple data inputs** — but way faster and cleaner than writing your own multiprocessing code.

---

## Retries

### 🦾 Why use Tenacity

* ⏳ **Smarter retry strategies** – Supports exponential backoff, jitter, and custom retry conditions, so you're not just blindly retrying.
* 🧰 **Highly configurable** – You can mix and match behaviors easily to fit different use cases.
* 🧪 **Battle-tested** – It's a mature library that gracefully handles a ton of edge cases for you.
* 🧼 **Cleaner architecture** – Keeps retry logic separate from business logic, which makes code more readable and maintainable.

### 🧠 Why roll your own (manual retries)

* 🥇 **No pickling drama** – Manual retries work smoothly in parallel jobs where Tenacity's decorators might run into serialization issues.
* 📦 **Fewer dependencies** – No need to pull in an extra library if your retry needs are simple.
* 🧠 **Total control** – You can customize the retry logic down to the tiniest detail.

### TL;DR:

**Tenacity = polished, flexible, and clean** for most retry scenarios.  
**Manual retries = lightweight and ultra-custom** when you need max control or are working in tricky parallel setups.

<br>
