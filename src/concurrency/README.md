# 🌀 Concurrency vs. Parallelism

## 🎨 Meme-y Cheat Sheet

### Concurrency vs. Parallelism

* 🧑 juggling convos = **concurrency**
* 👯 clones doing convos = **parallelism**

### GIL

* 🚷 bouncer: only 1 CPU-bound thread at a time
* ✅ chill if you're just waiting on I/O

### Threads

* 📞 waiting on hold (network, file, etc.) → use threads

### Multiprocessing

* 🧠🧠🧠 many brains → real CPU parallelism

### AsyncIO

* 💬 texting 1,000 people and not waiting for replies
* Perfect for servers, scrapers, bots

### When to Use

* Threads = I/O waiting
* Multiprocessing = CPU crunch
* AsyncIO = mega I/O scale
* Combo = galaxy brain 🪐

### Best Practices

* Keep it simple 🙏
* Always `.join()` (clean up)
* Benchmark > vibes
* Use `concurrent.futures` (easy mode)

<br>
