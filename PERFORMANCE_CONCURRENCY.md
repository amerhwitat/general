# Performance & Concurrency Policy

Repository-wide guidance: parallelize only independent work, use bounded workers, avoid shared mutable state, prevent oversubscription, retain deterministic test modes, and benchmark real workloads before adopting concurrency changes.
