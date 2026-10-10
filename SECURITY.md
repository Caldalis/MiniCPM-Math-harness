# Security

## Model-written code runs on your machine

Two agents execute Python that the model wrote: the **lab** in `minicpm-math prove` (a brute-force check per
candidate proof) and the **coders** in `minicpm-math solve --coders N`. Each program runs in a subprocess with

- a 20-second timeout and a CPU-time limit; on timeout, and when the run is cancelled (early stop, Ctrl+C), the
  script is killed together with the processes it started (Linux and macOS),
- a 4 GB address-space limit on Linux (macOS does not enforce one),
- at most 256 KB of output kept per stream,
- an empty temporary working directory, a clean environment (no API keys or tokens), Python's isolated mode (`-I`),
  and one thread per math library.

This is not a sandbox. The program runs as your user, can read and write your files and can use the network. A
model can be steered by the problem text it is given, so treat problems from untrusted sources as untrusted code.
Use `--no-exec` to turn code execution off, or run the harness in a container or VM with no credentials and no
access to anything you care about.

## Reporting a vulnerability

Please report security issues privately with GitHub's "Report a vulnerability" button on the Security tab of
this repository, not in a public issue.
