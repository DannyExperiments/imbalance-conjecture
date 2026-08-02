# Independent verification programs

This directory contains the two strongest independent finite corroboration lanes.

## Dependency-free Python

```bash
python3 imbalance_independent_referee_checker.py
```

Expected terminal marker:

```text
ALL_INDEPENDENT_CHECKS_PASS
```

The frozen output is `INDEPENDENT_CHECKER_LOG.txt`.

## Exhaustive C++20

```bash
c++ -std=c++20 -O3 -Wall -Wextra -pedantic \
  imbalance_exhaustive_n7.cpp -o imbalance_exhaustive_n7
./imbalance_exhaustive_n7
```

Expected output is exactly the content of `EXHAUSTIVE_N7_LOG.txt`.

The C++ program exhausts all `2,097,152` labeled graphs on seven vertices. Neither program replaces the symbolic proof.

