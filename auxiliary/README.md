# Non-load-bearing exact programs

This directory supplies the four programs and captured outputs referenced in
the manuscript's computation appendix. None is used in the symbolic proof.

- `imbalance_breakthrough_verifier.py` and its `.log` are the original
  NetworkX regression lane for the residual counterpacket, top-set tie choices,
  trees, and head profiles.
- `imbalance_extensions_verifier.py` and its `.log` are the original NetworkX
  regression lane for the strengthened and one-zero statements.
- `imbalance_independent_referee_checker.py` and its `.log` are the
  dependency-free independent checker.
- `imbalance_exhaustive_n7.cpp` and its `.log` are the independent exhaustive
  seven-vertex C++20 lane.

The two independent programs are also exposed under `verification/` with
release-gate-oriented filenames. Their source and output bytes agree with the
copies here. The main release verifier executes those independent copies.

No dependency installation is performed by this repository. The two NetworkX
programs are preserved for transparency and should be run only in an existing,
trusted environment that already provides their declared dependency.
