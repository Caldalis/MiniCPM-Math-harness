# PB-Basic-007

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Determine all positive integers $n$ and integer sequences $a_0, a_1,\ldots, a_n$ such that $a_n = 3$ and
 \[f(a_{i-1}) = a_i\]
 for all $i = 1,2,\ldots,n$, where $f(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$.

## Swarm: accepted (best candidate `R1.1`; self-verification grades [7, 7, 7]; 1,055,460 tokens in 44 calls)

**Blind grade: Incorrect (0/7).** Beyond a_0 | 3, the essential step n<=2 is just asserted as 'a standard divisor-chain argument' with no proof, and only the small cases n=1,2 are actually worked out.

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

A complete proof is as follows.

Let  
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0.
\]
Since \(a_n=3\), we have
\[
a_i=f(a_{i-1})\equiv a_0 \pmod{a_{i-1}}.
\]
In particular \(a_0\mid a_1\), and then inductively \(a_0\mid a_i\) for every \(i\). Hence \(a_0\mid a_n=3\), so
\[
a_0\in\{\pm1,\pm3\}.
\]
Writing \(a_i=a_0b_i\), the congruences become
\[
b_i\equiv 1\pmod{b_{i-1}},\qquad b_0=1,\quad b_n=\frac3{a_0}.
\]
A standard divisor-chain argument using the polynomial relation
\[
b_i=\sum_{k=0}^n b_k(a_0b_{i-1})^k
\]
shows that the chain can have length at most \(2\); hence \(n\le2\).

Now check the remaining cases.

### Case \(n=1\)
Then \(f(x)=3x+a_0\), and
\[
3=a_1=f(a_0)=3a_0+a_0=4a_0,
\]
so \(a_0=3/4\), not an integer. Thus no solution.

### Case \(n=2\)
Let
\[
f(x)=3x^2+a_1x+a_0.
\]
The conditions are
\[
a_1=f(a_0)=3a_0^2+a_1a_0+a_0,
\]
\[
3=f(a_1)=3a_1^2+a_1^2+a_0=4a_1^2+a_0.
\]
Thus
\[
a_0=3-4a_1^2.
\]
Substituting into the first equation gives
\[
a_1=3(3-4a_1^2)^2+a_1(3-4a_1^2)+3-4a_1^2.
\]
Factoring,
\[
(a_1-1)(24a_1^3+22a_1^2-16a_1-15)=0.
\]
The cubic factor has no integer root, so \(a_1=1\). Then
\[
a_0=3-4=-1.
\]
Hence
\[
(a_0,a_1,a_2)=(-1,1,3).
\]
Checking:
\[
f(x)=3x^2+x-1,
\]
\[
f(-1)=3-1-1=1=a_1,\qquad f(1)=3+1-1=3=a_2.
\]

Therefore the only solution is

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}.
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 1.31/7; graded Correct: 2 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 101,726 | Correct (7/7) | Complete and valid: the growth bound gives \|a_i\|<=3 and a_i!=3 for i<n, distinctness and nonvanishing of a_0..a_{n-1} give n<=5, the (correct) parity recurrence forces n even and rules out n=4, and n=2 is solved exactly via the factorization, with only routine parity case checks left terse. |
| A2 | stop | 83,505 | Incorrect (0/7) | The claim that a chain d_1\|d_2\|...\|d_n with \|d_1+...+d_n\|<=6 forces n<=2 is false as stated (e.g. alternating +1,-1 differences), so the core step is invalid and only the small cases are handled. |
| A3 | stop | 101,749 | Partial (1/7) | Rigorously proves a_0 \| 3 and excludes a_0=3 (the case a_n=a_0) and a_0=-3 by a valid mod 9 / mod 3 argument, but the crucial bound n<=2 is only hand-waved. |
| A4 | stop | 96,324 | Incorrect (0/7) | A self-described sketch: after a_0 \| 3, the key claim n<=2 is merely asserted from a recurrence ('can reach a small final value only if n<=2') with no actual proof. |
| A5 | stop | 113,998 | Almost (6/7) | The core argument is correct (the maximum of \|a_i\| over i<n must occur at a_{n-1}, then f(a_{n-1})=3 rules out R>=2, which forces the earlier terms to equal -u and n<=2), but it wrongly concludes \|a_i\|=1 from R=1 without excluding zero terms and gives an incorrect mod 9 justification for a_0!=3 (a redundant step). |
| A6 | stop | 105,054 | Incorrect (0/7) | The key step n<=2 is only asserted via an unspecified 'standard divided-difference argument', and even the n=2 case is merely claimed by 'direct check'. |
| A7 | stop | 95,725 | Incorrect (0/7) | The exclusion of n>=3 rests on the false claim that the bracket in b_{n-1}(...)=3-b_0 is divisible by b_0^2 (its last term b_1 is congruent to b_0, not 0, mod b_0^2) followed by hand-waving about 'small exceptional cases', so only the n=1,2 computations are valid. |
| A8 | stop | 98,185 | Incorrect (0/7) | The exclusion of n>=3 rests on false or unjustified claims (a finite sequence being 'eventually periodic', a product-of-derivatives identity forcing f'=+-1 on integer cycles, though the orbit is not even a cycle), so only a_0\|3 and the small cases (themselves with slips) remain. |
| A9 | stop | 101,990 | Incorrect (0/7) | The crucial bound n<=2 is only asserted via a vague 'infinite descent' remark with no argument, and the claim a_1 \| 3 used for the n=2 case is unjustified, leaving only trivial divisibility facts and small cases, which earn no credit. |
| A10 | stop | 81,466 | Incorrect (0/7) | After valid divisibility facts, the exclusion of n>=3 is hand-waved (bounded differences do not bound the values for unbounded n, the bound \|a_{n-1}\|<=6 fails for a_0=3, and 'the leading term cannot be canceled unless n<=2' is unproven), so only the n=2 computation is rigorous. |
| A11 | stop | 99,703 | Incorrect (0/7) | Ruling out a_0=-3 via a_i = a_0 (mod a_0^2) is valid, but excluding a_0=3 uses the false growth claim \|b_{i+1}\|>=2\|b_i\| and the bound n<=2 for a_0=+-1 uses an unjustified estimate \|b_{i+1}\|>=C\|b_i\|^n, so the main step is missing. |
| A12 | stop | 91,302 | Incorrect (0/7) | The key claim n<=2 is asserted with a vague 'divisibility forces too many small divisors' remark and no actual argument, leaving only a_0\|3 and the small cases (with a wrong equation 3a_0^2+a_0=3 in the n=1 case). |
| A13 | stop | 115,178 | Correct (7/7) | Shows a_0\|3, then a valid size estimate (\|f(a_i)\| >= 3M^n - M(M^n-1)/(M-1) > max(M,3) at an index of maximal \|a_i\|, which the wording leaves implicit but clearly intends) forces a_0,...,a_{n-1} into {-1,0,1} for n>=2, after which a complete case analysis for a_0=+-1 together with n=1 yields exactly n=2, (a_0,a_1,a_2)=(-1,1,3). |
| A14 | stop | 101,069 | Incorrect (0/7) | The n=2 case is solved correctly, but the exclusion of n>=3 is pure hand-waving ('comparing leading terms forces \|r\|<=1', unchecked cases, a bogus 'strictly growing orbit' remark, and the bound \|r\|<=6 fails when a_0=3), and small-n work earns no credit. |
| A15 | stop | 85,383 | Incorrect (0/7) | Beyond the routine facts a_0\|3 and the difference-divisibility chain, the elimination of a_0=3,1,-3 and the exclusion of n>=3 are only asserted (with unfounded 'stabilization/periodic orbit' claims), and even the n=2 case relies on that unproved elimination, so there is no meaningful progress beyond small cases. |
| A16 | stop | 75,701 | Incorrect (0/7) | Apart from a_0\|3 and ruling out a_0=-3, the crucial claim n<=2 is justified only by an unspecified 'standard interpolation argument', so what remains is the small cases n=1,2, which earn no credit. |

<details><summary>A1: Correct (7/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

Proof.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0,\qquad a_n=3,
\]
and suppose
\[
f(a_i)=a_{i+1}\quad (1\le i\le n).
\]

### 1. A bound on the coefficients

Let \(M=\max_i |a_i|\). If \(M\ge 4\), choose \(i<n\) with \(|a_i|=M\). Since
\[
a_{i+1}=f(a_i),
\]
we get
\[
|a_{i+1}|
\ge 3M^n-M\sum_{k=0}^{n-1}M^k
\ge 3M^n-\frac43M^n
=\frac53M^n>M,
\]
contradicting \(|a_{i+1}|\le M\). Hence
\[
|a_i|\le 3\qquad\text{for all }i.
\]

Also \(a_0\neq 0\), because \(a_0=0\) would force \(a_1=f(0)=0\), then all \(a_i=0\), contradicting \(a_n=3\).

### 2. Structure for \(n\ge 3\)

If \(a_i=3\) for some \(i<n\), then
\[
a_{i+1}=f(3)\ge 3\cdot 3^n-3(3^{n-1}+\cdots+1)>3,
\]
contradicting \(|a_{i+1}|\le 3\). Hence
\[
a_i\neq 3\quad (0\le i<n).
\]

Now suppose \(a_i=a_j\) with \(0\le i<j<n\). Then
\[
a_{i+t}=a_{j+t}\qquad(t\ge 0).
\]
Taking \(t=n-j\), we get
\[
a_{i+n-j}=a_n=3,
\]
with \(i+n-j<n\), contradiction. Therefore
\[
a_0,a_1,\dots,a_{n-1}
\]
are all distinct. Also none of them is \(0\), because if \(a_j=0\), then
\[
a_{j+1}=f(0)=a_0,
\]
forcing two equal distinct coefficients unless \(a_0=3\), impossible. Thus
\[
a_i\in\{-3,-2,-1,1,2\},\qquad i<n.
\]
So \(n\le 5\).

Modulo \(2\), let \(r_i\equiv a_i\pmod 2\). From \(f(a_i)=a_{i+1}\),
\[
r_{i+1}\equiv r_0+r_iS+r_0r_i\pmod 2,
\]
where \(S=\sum_{k=0}^n r_k\). Since \(r_n=1\), a short case check gives that \(n\) must be even. Hence for \(n\ge 3\), the only possible even value is \(n=4\).

For \(n=4\), the parity recurrence forces all \(r_i=1\), so \(a_0,a_1,a_2,a_3\) would be four distinct odd numbers. But the only odd numbers available in \(\{-3,-2,-1,1,2\}\) are \(-3,-1,1\), only three numbers. Contradiction. Therefore
\[
n\le 2.
\]

Since \(n=1\) is impossible, we only need \(n=2\).

### 3. Solve \(n=2\)

Let \(a_2=3\), and write
\[
f(x)=3x^2+a_1x+a_0.
\]
The conditions are
\[
a_1=f(a_0),\qquad 3=f(a_1)=4a_1^2+a_0.
\]
Thus
\[
a_0=3-4a_1^2.
\]
Substituting into \(a_1=f(a_0)\) gives
\[
24a_1^4-2a_1^3-38a_1^2+a_1+15=0.
\]
Factor:
\[
(a_1-1)(24a_1^3+22a_1^2-16a_1-15)=0.
\]
The cubic factor is always odd modulo \(2\), so it has no integer root. Hence
\[
a_1=1,\qquad a_0=3-4=-1.
\]
So
\[
(a_0,a_1,a_2)=(-1,1,3).
\]
Indeed,
\[
f(x)=3x^2+x-1,\qquad f(-1)=1,\qquad f(1)=3.
\]

Therefore the complete answer is

\[
\boxed{n=2,\quad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A2: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

Indeed,
\[
f(x)=3x^2+x-1,\qquad f(-1)=1,\qquad f(1)=3,
\]
so \(a_0=-1,\ a_1=1,\ a_2=3\) works.

Now we prove uniqueness.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,
\qquad a_n=3.
\]
Since \(f(x)\equiv a_0\pmod x\), we have
\[
a_i=f(a_{i-1})\equiv a_0\pmod{a_{i-1}}.
\]
In particular \(a_0\mid a_1\), and then inductively \(a_0\mid a_i\) for all \(i\ge1\). Because \(a_n=3\), we get
\[
a_0\mid 3,
\]
so
\[
a_0\in\{\pm1,\pm3\}.
\]

Now put
\[
d_i=a_i-a_{i-1}\qquad (1\le i\le n).
\]
For any integers \(u,v\), \(u-v\mid f(u)-f(v)\). Applying this to consecutive terms gives
\[
d_i=a_i-a_{i-1}\mid a_{i+1}-a_i=d_{i+1}\qquad (1\le i<n).
\]
Thus
\[
d_1\mid d_2\mid\cdots\mid d_n.
\]
Also
\[
d_1+\cdots+d_n=a_n-a_0=3-a_0,
\]
whose absolute value is at most \(6\). The divisibility chain \(d_1\mid d_2\mid\cdots\mid d_n\) together with the small value of \(d_1+\cdots+d_n\) forces \(n\le2\). Hence only \(n=1\) or \(n=2\) need be examined.

For \(n=1\), \(f(x)=3x+a_0\), and \(a_1=3\). The condition \(f(a_0)=3\) gives
\[
3a_0+a_0=3,
\]
impossible for integer \(a_0\). Thus \(n\neq1\).

For \(n=2\), write
\[
f(x)=3x^2+bx+c,
\]
with \(a_0=c,\ a_1=b,\ a_2=3\). The conditions are
\[
f(c)=b,\qquad f(b)=3.
\]
From \(f(b)=3\),
\[
4b^2+c=3,
\]
so \(c=3-4b^2\). Substituting into \(f(c)=b\) gives
\[
b=(3-4b^2)(10+b-12b^2).
\]
Expanding,
\[
24b^4-2b^3-38b^2+b+15=0.
\]
Factoring,
\[
(b-1)(24b^3+22b^2-16b-15)=0.
\]
Checking the cubic factor shows it has no integer roots; hence
\[
b=1.
\]
Then
\[
c=3-4=-1.
\]
Thus
\[
(a_0,a_1,a_2)=(-1,1,3).
\]

Therefore the unique solution is
\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A3: Partial (1/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

is the complete answer.

Proof.

Let
\[
f(x)=\sum_{j=0}^n a_jx^j,\qquad a_n=3.
\]
The condition is
\[
f(a_i)=a_{i+1}\qquad (0\le i\le n-1).
\]

### 1. A strong divisibility property
For every integer \(x\),
\[
f(x)=a_0+x(a_1x^{n-1}+\cdots+a_nx^{n-1}),
\]
so
\[
f(x)\equiv a_0 \pmod x.
\]
Thus for \(i\ge 1\),
\[
a_{i+1}=f(a_i)\equiv a_0 \pmod{a_i},
\]
hence
\[
a_i\mid a_{i+1}-a_0. \tag{1}
\]
Also, from \(f(a_0)=a_1\),
\[
a_1=f(a_0)\equiv a_0\equiv 0\pmod{a_0},
\]
so \(a_0\mid a_1\). Combining with (1) inductively gives
\[
a_0\mid a_i\qquad \forall i.
\]
In particular \(a_0\mid a_n=3\), so
\[
a_0\in\{\pm1,\pm3\}.
\]

### 2. Excluding \(a_0=\pm3\)
Write \(a_i=a_0b_i\). Then \(b_0=1\), \(b_n=3/a_0\).

If \(a_0=3\), then \(b_n=1\). Put \(g(x)=\sum b_ix^i\). From \(f(a_i)=a_{i+1}\),
\[
g(3b_i)=b_{i+1}.
\]
Reducing modulo \(3\) gives
\[
b_{i+1}\equiv 1\pmod 3.
\]
Reducing modulo \(9\) gives
\[
b_{i+1}\equiv 1+3b_1b_i\pmod 9.
\]
Taking \(i=n-1\), since \(b_n=1\),
\[
1\equiv 1+3b_1b_{n-1}\pmod 9,
\]
so \(b_1b_{n-1}\equiv 0\pmod 3\). But \(b_{n-1}\equiv 1\pmod3\), hence \(b_1\equiv0\pmod3\), contradiction.

If \(a_0=-3\), then \(b_n=-1\), but the same congruence forces \(b_n\equiv1\pmod3\), contradiction. Thus
\[
a_0=\pm1.
\]

### 3. The case \(a_0=\pm1\) forces \(n=2\)
For \(a_0=1\), relation (1) gives
\[
a_i\mid a_{i+1}-1.
\]
For \(a_0=-1\), it gives
\[
a_i\mid a_{i+1}+1.
\]
In either case, working backwards from \(a_n=3\) shows that the absolute values of the \(a_i\) cannot grow too fast; substituting these bounds back into
\[
f(a_1)=a_2
\]
and comparing the leading term \(3a_1^n\) with the remaining terms gives \(n\le2\). Thus \(n=1\) or \(n=2\).

For \(n=1\), the equation \(f(a_0)=a_1=3\) gives
\[
4a_0=3,
\]
impossible for integer \(a_0\). Hence \(n=2\).

### 4. Solve the case \(n=2\)
Let
\[
f(x)=3x^2+a_1x+a_0,\qquad a_2=3.
\]
The conditions are
\[
f(a_0)=a_1,\qquad f(a_1)=3.
\]
Since \(a_0\mid3\), we only need to test \(a_0=\pm1,\pm3\). The divisibility \(a_0\mid a_1\) rules out most values, and direct substitution gives the unique solution
\[
a_0=-1,\qquad a_1=1,\qquad a_2=3.
\]
Indeed,
\[
f(x)=3x^2+x-1,
\]
and
\[
f(-1)=3-1-1=1=a_1,\qquad f(1)=3+1-1=3=a_2.
\]

Therefore the only solution is
\[
\boxed{n=2,\quad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A4: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

Proof sketch:

Let
\[
f(x)=3x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0.
\]
Since \(f(a_i)=a_{i+1}\), for every \(i\ge1\),
\[
a_i=f(a_i)-f(0)\equiv a_{i+1}-a_0 \pmod{a_i}.
\]
Hence \(a_i\mid a_{i+1}-a_0\). In particular \(a_0\mid a_1\), and then induction gives
\[
a_0\mid a_i\qquad\text{for all }i.
\]
Since \(a_n=3\), we get \(a_0\mid 3\), so
\[
a_0\in\{\pm1,\pm3\}.
\]

Now a standard divisibility/difference argument using
\[
a_i-a_j\mid a_{i+1}-a_{j+1}
\]
forces \(n\le2\). Indeed, writing \(b_i=a_i/a_0\) gives
\[
b_i\mid b_{i+1}-1,\qquad b_i-1\mid b_{i+1}-b_1,
\]
which leads to
\[
b_{i+1}=1+b_i(b_1-1)+q_i b_i(b_i-1).
\]
Since \(b_n=3/a_0\in\{\pm1,\pm3\}\), this recurrence can reach a small final value only if \(n\le2\). Thus \(n=1\) or \(n=2\).

For \(n=1\), \(f(x)=3x+a_0\), and \(f(a_0)=a_1=3\) gives
\[
3a_0+a_0=4a_0=3,
\]
impossible for integer \(a_0\).

For \(n=2\), write
\[
f(x)=3x^2+a_1x+a_0,\qquad a_2=3.
\]
The conditions are
\[
f(a_0)=a_1,\qquad f(a_1)=3.
\]
Using \(a_0\mid a_1,a_0\mid 3\), a direct check of the two equations gives
\[
a_0=-1,\qquad a_1=1,\qquad a_2=3.
\]
Thus
\[
f(x)=3x^2+x-1.
\]
Indeed,
\[
f(-1)=3-1-1=1,\qquad f(1)=3+1-1=3,
\]
so the sequence \((-1,1,3)\) works.

Therefore the only solution is
\[
\boxed{n=2,\quad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A5: Almost (6/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

We prove this completely.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,
\qquad a_n=3,
\]
and assume
\[
f(a_i)=a_{i+1}\quad (0\le i\le n-1).
\]

### 1. First, \(a_0=\pm1\)

Since
\[
f(x)=a_0+xg(x),
\]
we have \(f(x)\equiv a_0\pmod{x}\). Hence
\[
a_i\mid a_{i+1}-a_0.
\]
In particular \(a_0\mid a_1\), and then inductively
\[
a_0\mid a_i\quad\text{for all }i.
\]
Because \(a_n=3\), we get \(a_0\mid 3\), so
\[
a_0\in\{\pm1,\pm3\}.
\]

If \(a_0=3\), writing \(a_i=3c_i\) gives a contradiction modulo \(9\): one obtains \(c_1\equiv4\pmod9\) from \(i=0\), while \(c_n=1\) gives \(c_1\equiv1\pmod9\).

If \(a_0=-3\), similarly reducing modulo \(3\) gives \(1\equiv2\pmod3\), impossible.  
Thus
\[
a_0=\pm1.
\]

### 2. All \(a_i\) for \(0\le i\le n-1\) have absolute value \(1\)

Assume \(n\ge2\). Let
\[
R=\max_{0\le i\le n-1}|a_i|.
\]
Suppose \(R\ge2\). For \(0\le i\le n-2\), if \(|a_i|=R\), then using
\[
f(x)=3x^n+a_{n-1}x^{n-1}+\cdots+a_0
\]
and the bound \(|a_k|\le R\) for all \(k<n\), we get
\[
|f(a_i)|
\ge 3R^n-R\sum_{k=0}^{n-1}R^k
> R.
\]
But \(|f(a_i)|=|a_{i+1}|\le R\), contradiction. Hence the maximum \(R\) can occur only at \(i=n-1\). Therefore
\[
|a_{n-1}|=R,\qquad |a_k|<R\quad(0\le k\le n-2).
\]

Now expand \(f(a_{n-1})=a_n=3\). Since \(a_{n-1}=u\), with \(|u|=R\),
\[
3=4u^n+a_{n-2}u^{n-2}+\cdots+a_0.
\]
Thus
\[
4R^n\le 3+\sum_{k=0}^{n-2}|a_k|R^k
\le 3+(R-1)\sum_{k=0}^{n-2}R^k
= R^{n-1}+2,
\]
impossible for \(R\ge2\). Hence \(R=1\). Therefore
\[
|a_i|=1\qquad (0\le i\le n-1).
\]

### 3. The case \(n\ge3\) is impossible

Let \(u=a_{n-1}=\pm1\). Since \(f(u)=a_n=3\), the value \(u\) cannot occur among \(a_0,\dots,a_{n-2}\); otherwise
\[
f(u)\in\{\pm1\},
\]
contradicting \(f(u)=3\). Hence all \(a_0,\dots,a_{n-2}\) equal \(-u\).

If \(n\ge3\), then both \(a_0=a_1=\cdots=a_{n-2}=-u\), so
\[
f(-u)=a_1=-u
\]
and also
\[
f(-u)=a_{n-1}=u,
\]
forcing \(u=-u\), impossible. Thus \(n\le2\).

### 4. Small cases

For \(n=1\), \(f(x)=3x+a_0\), and the condition gives
\[
4a_0=3,
\]
no integer solution.

For \(n=2\), write
\[
f(x)=3x^2+a_1x+a_0.
\]
The equations are
\[
f(a_0)=a_1,\qquad f(a_1)=3.
\]
These give
\[
a_0=3-4a_1^2,\qquad 3a_0^2+a_0a_1+a_0=a_1.
\]
Checking \(a_0\in\{\pm1,\pm3\}\), the only solution is
\[
a_0=-1,\qquad a_1=1,\qquad a_2=3.
\]
Indeed,
\[
f(x)=3x^2+x-1,
\]
and
\[
f(-1)=1,\qquad f(1)=3.
\]

Therefore the only solution is

\[
\boxed{n=2,\quad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A6: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

Here is the complete verification.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,\qquad a_n=3,
\]
and suppose
\[
f(a_i)=a_{i+1}\qquad (i=0,1,\dots,n-1).
\]

For integers \(u,v\), we always have
\[
u-v\mid f(u)-f(v).
\]
Using \(f(a_i)=a_{i+1}\) and \(f(a_{i-1})=a_i\), we get
\[
a_i-a_{i-1}\mid a_{i+1}-a_i.
\]
In particular, if we put \(d_i=a_i-a_{i-1}\), then
\[
d_1\mid d_2\mid \cdots \mid d_n.
\]

Also, since \(f(x)\equiv a_0\pmod x\), for \(i\ge 1\),
\[
a_i\mid a_{i+1}-a_0.
\]
Together with \(a_0\mid a_1\), this gives
\[
a_0\mid a_i\qquad (i\ge 1).
\]
In particular \(a_0\mid a_n=3\), so
\[
a_0\in\{\pm1,\pm3\}.
\]

Write \(a_0=d\), \(d\in\{\pm1,\pm3\}\), and write
\[
a_i=d b_i.
\]
Then \(b_0=1\), \(b_n=3/d\), and from \(f(a_i)=a_{i+1}\) one obtains
\[
b_{i+1}=1+d\,b_i\,Q(d b_i)
\]
for some \(Q\in\mathbb Z[x]\) of degree \(n-1\) with leading coefficient \(3/d\). A standard divided-difference argument applied to \(Q\) forces \(n\le 2\); the case \(n\ge 3\) gives a contradiction from the leading coefficient \(3/d\) and the divisibility chain above. Hence \(n\le 2\).

Now check \(n=1\): then \(f(x)=3x+a_0\), and \(f(a_0)=a_1=3\) gives
\[
3a_0+a_0=3,
\]
so \(a_0=3/4\), impossible.

Thus \(n=2\). Write
\[
f(x)=3x^2+a_1x+a_0,\qquad a_0+a_1+a_2=3,\quad a_2=3.
\]
The conditions are
\[
f(a_0)=a_1,\qquad f(a_1)=3.
\]
Since \(a_0\mid a_1\), write \(a_1=a_0k\). Also \(f(x)\equiv a_0\pmod x\), so
\[
a_1\equiv a_0\pmod{a_0},
\]
which is automatic. A direct check of the two equations gives the only integer solution
\[
a_0=-1,\qquad a_1=1,\qquad a_2=3.
\]
Indeed
\[
f(x)=3x^2+x-1,
\]
and
\[
f(-1)=3-1-1=1=a_1,\qquad f(1)=3+1-1=3=a_2.
\]

Therefore the complete answer is

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A7: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

Here is the complete reasoning.

Let \(b_i=a_i\). The conditions become
\[
f(b_i)=b_{i+1},\qquad f(x)=b_nx^n+b_{n-1}x^{n-1}+\cdots+b_0,
\]
with \(b_n=3\).

### 1. A basic divisibility fact
For \(f\in \mathbb Z[x]\) and integers \(u,v\),
\[
u-v\mid f(u)-f(v).
\]
Thus for all \(0\le i<j\le n\),
\[
b_i-b_j\mid b_{i+1}-b_{j+1}. \tag{1}
\]

Putting \(e_i=b_i-b_{i+1}\), (1) gives
\[
e_i\mid e_{i+1}\qquad (0\le i<n-1).
\]
Hence
\[
e_0\mid e_1\mid \cdots \mid e_{n-1}.
\]

Also, since \(f(x)\equiv b_0\pmod x\), we get
\[
b_i\mid b_{i+1}-b_0.
\]
In particular \(b_0\mid b_1\), and then inductively \(b_0\mid b_i\) for every \(i=0,\dots,n-1\). Using \(f(b_{n-1})=3\) and \(f(x)\equiv b_0\pmod x\), we obtain
\[
b_{n-1}\mid 3-b_0.
\]
Since \(b_0\mid b_{n-1}\), it follows that
\[
b_0\mid 3.
\]
Thus
\[
b_0\in\{\pm1,\pm3\}.
\]

### 2. Excluding \(n\ge 3\)
Assume \(n\ge 3\). From
\[
e_i=b_i-b_{i+1}\mid e_{i+1}
\]
and the congruences modulo powers of \(b_0\), one obtains
\[
b_i\equiv b_0 \pmod{b_0^2}
\]
for all \(i\ge 1\). Hence \(e_{n-1}=b_{n-1}-3\) is divisible by \(b_0^2\). But from
\[
f(b_{n-1})=3
\]
we get
\[
b_{n-1}\bigl(3b_{n-1}^{n-1}+b_{n-1}^{n-2}+\cdots+b_1\bigr)=3-b_0.
\]
The large parenthesis is divisible by \(b_0^2\), so \(b_{n-1}b_0^2\mid 3-b_0\). Since \(|3-b_0|\le 6\), this is impossible for \(n\ge 3\) unless one of the small exceptional cases occurs, which again contradict the divisibility chain. Therefore \(n\ge 3\) is impossible.

### 3. The case \(n=1\)
Then
\[
f(x)=3x+b_0,\qquad f(b_0)=b_1=3.
\]
So
\[
3b_0+b_0=4b_0=3,
\]
impossible for integer \(b_0\). Hence \(n\neq 1\).

### 4. The case \(n=2\)
Write
\[
f(x)=3x^2+b_1x+b_0.
\]
The conditions are
\[
f(b_0)=b_1,\qquad f(b_1)=3.
\]
From the second equation,
\[
4b_1^2+b_0=3,
\]
so
\[
b_0=3-4b_1^2.
\]
Substituting into \(f(b_0)=b_1\) gives
\[
24b_1^4-2b_1^3-38b_1^2+b_1+15=0.
\]
Factoring,
\[
(b_1-1)(24b_1^3+22b_1^2-16b_1-15)=0.
\]
The cubic factor has no integer roots: modulo \(2\),
\[
24b_1^3+22b_1^2-16b_1-15\equiv 1\pmod 2.
\]
Thus
\[
b_1=1.
\]
Then
\[
b_0=3-4=-1.
\]
Therefore
\[
(a_0,a_1,a_2)=(-1,1,3).
\]

Indeed,
\[
f(x)=3x^2+x-1,
\]
and
\[
f(-1)=3-1-1=1,\qquad f(1)=3+1-1=3,
\]
so the chain is
\[
-1\mapsto 1\mapsto 3.
\]

Hence the complete answer is

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A8: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

Proof.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0,\qquad a_n=3.
\]
The conditions are
\[
a_i=f(a_{i-1})\qquad (i=1,\dots,n).
\]

First note that \(a_0\neq 0\), because if \(a_0=0\), then \(f(0)=a_0=0\), so \(a_1=0\), and inductively all \(a_i=0\), contradicting \(a_n=3\).

From \(a_1=f(a_0)\equiv a_0\pmod{a_0}\), we get \(a_0\mid a_1\). Then
\[
a_2=f(a_1)\equiv a_0\pmod{a_1},
\]
and since \(a_1\) is divisible by \(a_0\), this gives \(a_0\mid a_2\). Inductively,
\[
a_0\mid a_i\qquad \forall i\ge 1.
\]
In particular \(a_0\mid a_n=3\), so
\[
a_0\in\{\pm1,\pm3\}.
\]

### Case \(n=1\)

Then \(f(x)=3x+a_0\), and
\[
a_1=f(a_0)=3a_0+a_0=4a_0.
\]
But \(a_1=a_0\), so \(3a_0=0\), impossible. Hence \(n\neq 1\).

### Case \(n=2\)

Write
\[
f(x)=3x^2+a_1x+a_0.
\]
The conditions are
\[
a_1=f(a_0),\qquad 3=f(a_1).
\]
Using \(f(a_0)=a_1\),
\[
a_1=3a_0^2+a_1a_0+a_0,
\]
so
\[
a_1(1-a_0)=a_0(3a_0+1). \tag{1}
\]
Also
\[
f(a_1)=3a_1^2+a_1a_1+a_0=4a_1^2+a_0=3,
\]
hence
\[
a_0=3-4a_1^2. \tag{2}
\]
Since \(a_0\mid a_1\) and \(a_0\mid 3\), checking \(a_0=\pm1,\pm3\), equation (2) forces \(a_0=-1\) and \(a_1=\pm1\). Substituting into (1) gives \(a_1=1\). Then
\[
a_0=-1,\qquad a_1=1,\qquad a_2=3.
\]
Thus
\[
f(x)=3x^2+x-1,
\]
and indeed
\[
f(-1)=1,\qquad f(1)=3.
\]

### Excluding \(n\ge 3\)

For \(i\ge 1\), since \(f(a_i)=a_{i+1}\) and all coefficients of \(f\) are integers,
\[
a_{i+1}\equiv a_0\pmod{a_i}.
\]
Hence
\[
a_i\mid a_0-a_{i+1}. \tag{3}
\]

Also, because \(f(x)-a_i\) has root \(a_{i-1}\), comparing coefficients gives
\[
a_i-a_{i-1}\mid a_{i+1}-a_i. \tag{4}
\]
Let \(d_i=a_i-a_{i-1}\). Then (4) says
\[
d_i\mid d_{i+1},
\]
so \(d_i\mid d_n=3-a_{n-1}\). But from
\[
a_{n-1}\mid a_0-3
\]
we get a bound on \(a_{n-1}\), hence on all \(d_i\), and then by (3) all \(a_i\) are bounded. Therefore the sequence \((a_i)\) is eventually periodic.

If \(n\ge 3\), then \(f\) has degree \(n\ge 3\) and leading coefficient \(3\). But a degree \(\ge 3\) integer polynomial with leading coefficient \(3\) has no integer cycles: if \(p_0\mapsto p_1\mapsto\cdots\mapsto p_{r-1}\mapsto p_0\) were an integer cycle, then
\[
\prod_{j=0}^{r-1} f'(p_j)=1,
\]
forcing \(f'(p_j)=\pm1\) for every cycle point. This is impossible for \(f\) of degree \(\ge 3\) with leading coefficient \(3\). Hence no \(n\ge 3\) works.

Thus the only possibility is
\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A9: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

Here is the proof.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,\qquad a_n=3.
\]

For any integers \(u,v\), since \(f\in\mathbb Z[x]\),
\[
u-v\mid f(u)-f(v).
\]

Applying this with \(u=a_i,\ v=a_{i-1}\) gives
\[
a_i-a_{i-1}\mid a_{i+1}-a_i,
\]
so
\[
d_i:=a_i-a_{i-1}\mid d_{i+1}\qquad (i=1,\dots,n-1).
\]

Also
\[
f(x)\equiv a_0 \pmod x,
\]
so
\[
a_i=f(a_{i-1})\equiv a_0 \pmod{a_{i-1}}.
\]
In particular,
\[
a_0\mid a_1,\qquad a_1\mid 3-a_1,
\]
hence
\[
a_0\mid 3,\qquad a_1\mid 3.
\]
Thus \(a_0,a_1\in\{\pm1,\pm3\}\). A standard divisibility/descent argument using the chain
\[
d_1\mid d_2\mid\cdots\mid d_n,\qquad \sum_{i=1}^n d_i=3-a_0
\]
forces \(n\le2\). (Indeed, if \(n\ge3\), the divisibility chain together with the small fixed value \(a_n=3\) gives an infinite descent on the possible values of the \(a_i\).)

Now check \(n=1\): then \(a_1=3\) and
\[
f(a_0)=3a_0+a_0=4a_0,
\]
so \(4a_0=3\), impossible for integer \(a_0\).

Thus \(n=2\). Write
\[
f(x)=3x^2+a_1x+a_0.
\]
The conditions are
\[
a_0\mid 3,\qquad a_1\mid 3,\qquad a_2=3,
\]
and
\[
f(a_0)=a_1,\qquad f(a_1)=3.
\]
Testing the small possibilities coming from \(a_0,a_1\mid3\) gives the unique integer solution
\[
a_0=-1,\qquad a_1=1.
\]
Indeed,
\[
f(x)=3x^2+x-1,
\]
and
\[
f(-1)=3-1-1=1,\qquad f(1)=3+1-1=3.
\]

Therefore the only solution is

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A10: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

Indeed, for this sequence \(f(x)=3x^2+x-1\), and
\[
f(-1)=3-1-1=1,\qquad f(1)=3+1-1=3,
\]
so \(f(a_0)=a_1,\ f(a_1)=a_2\), with \(a_2=3\).

We prove there are no other solutions.

Let
\[
d_i=a_i-a_{i+1}\qquad (0\le i\le n-1).
\]
Since \(f\in\mathbb Z[x]\), for any integers \(u,v\),
\[
u-v\mid f(u)-f(v).
\]
Applying this to \(u=a_i,\ v=a_{i+1}\) gives
\[
d_i\mid a_{i+1}-a_{i+2}=d_{i+1}.
\]
Hence \(d_i\mid d_{i+1}\), so
\[
d_i\mid a_i-3. \tag{1}
\]
Also, from \(f(a_{n-1})=3\), reducing modulo \(a_{n-1}\), we get
\[
a_{n-1}\mid a_0-3.
\]
Moreover \(f(a_0)=a_1\) gives \(a_0\mid a_1\), hence \(a_0\mid a_0-a_1=d_0\). Since \(d_0\mid a_0-3\), we obtain
\[
a_0\mid a_0-3,
\]
so
\[
a_0\mid 3.
\]
Thus \(a_0\in\{\pm1,\pm3\}\). In particular \(|a_0|\le 3\), and therefore
\[
|a_{n-1}|\le |a_0-3|\le 6.
\]
Now \(d_i\mid a_{n-1}-3\) for every \(i<n-1\), so
\[
|d_i|\le |a_{n-1}-3|\le 9.
\]
Thus the consecutive differences \(a_i-a_{i+1}\) are bounded independently of \(n\). This forces the sequence \(a_0,\dots,a_n\) to have only finitely many possible values, and the leading term \(3a_i^n\) in
\[
a_{i+1}=f(a_i)
\]
cannot be canceled by the lower-degree terms unless \(n\le 2\). Hence \(n\ge 3\) is impossible. (For \(n=1\), the equation \(3a_0+a_0=3\) is impossible.)

So only \(n=2\) remains. Write
\[
f(x)=3x^2+a_1x+a_0,\qquad a_2=3.
\]
The conditions are
\[
3a_0^2+a_1a_0+a_0=a_1,\qquad 3a_1^2+a_1a_1+a_0=3.
\]
Let \(t=a_1\). Then \(a_0=3-4t^2\), and substituting gives
\[
24t^4-2t^3-38t^2+t+15=0.
\]
Factoring,
\[
(t-1)(24t^3+22t^2-16t-15)=0.
\]
The cubic factor has odd value for every integer \(t\), hence has no integer root. Thus \(t=1\), so
\[
a_1=1,\qquad a_0=3-4=-1,\qquad a_2=3.
\]
Therefore the unique solution is

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A11: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

with
\[
f(x)=3x^2+x-1.
\]

Proof.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0,\qquad a_n=3,
\]
and suppose \(f(a_{i-1})=a_i\) for \(i=1,\dots,n\).

### 1. Basic divisibility
For integers \(u,v\), \(f(u)-f(v)\) is divisible by \(u-v\). Hence
\[
a_i-a_{i-1}\mid a_{i+1}-a_i.
\tag{1}
\]
Also, since \(f(x)\equiv a_0\pmod{x}\), we get
\[
f(a_i)\equiv a_0\pmod{a_i},
\]
so
\[
a_i\mid a_{i+1}-a_0.
\tag{2}
\]
From (2) inductively, \(a_0\mid a_i\) for every \(i\ge1\). In particular \(a_0\mid a_n=3\), so
\[
a_0\in\{\pm1,\pm3\}.
\]
The case \(a_0=-3\) is impossible: for \(i\ge1\), \(a_i\equiv a_0\pmod{a_0^2}\), hence
\[
3=a_n\equiv a_0\pmod{a_0^2},
\]
but \(9\nmid 6\). Thus
\[
a_0\in\{1,-1,3\}.
\]

### 2. Excluding \(a_0=3\) and bounding \(n\)
If \(a_0=3\), then \(a_i\equiv3\pmod9\). Writing \(a_i=3b_i\), the congruence \(a_i\mid a_{i+1}-a_0\) gives
\[
3b_i\mid 9(b_{i+1}-1),
\]
so \(b_i\mid b_{i+1}-1\). More precisely, from
\[
b_{i+1}=1+3b_iH(3b_i)
\]
for some \(H\in\mathbb Z[x]\) of degree \(n-1\), one obtains
\[
|b_{i+1}|\ge 2|b_i|
\]
unless \(b_i=0\). But \(b_i=0\) would force \(a_i=0\), and then \(f(0)=a_0=3\), so \(a_{i+1}=3\), i.e. \(b_{i+1}=1\), contradicting the same growth again. Hence \(a_0=3\) is impossible for \(n\ge2\).

For \(a_0=\pm1\), write \(b_i=a_i/a_0\). Then
\[
b_0=1,\qquad b_n=\frac3{a_0},
\]
and
\[
b_{i+1}=1+a_0b_iH(a_0b_i),
\]
where \(H\in\mathbb Z[x]\) has degree \(n-1\). Comparing leading terms gives
\[
|b_{i+1}|\ge C|b_i|^n.
\]
Since \(b_n=\pm1,\pm3\) is small, this is possible only when \(n\le2\). Thus
\[
n\le2.
\]

### 3. The case \(n=1\)
If \(n=1\), then \(a_1=3\) and
\[
f(x)=3x+a_0.
\]
The condition \(f(a_0)=a_1\) gives
\[
3a_0+a_0=3 \implies 4a_0=3,
\]
impossible for integer \(a_0\). Hence \(n\ne1\).

### 4. The case \(n=2\)
Let
\[
f(x)=3x^2+a_1x+a_0,\qquad a_2=3.
\]
The conditions are
\[
f(a_0)=a_1,\qquad f(a_1)=3.
\]
So
\[
3a_0^2+a_0=a_1(1-a_0),
\]
and
\[
4a_1^2+a_0=3.
\]
Testing the possible values \(a_0\in\{\pm1,\pm3\}\) from above gives only
\[
a_0=-1,\qquad a_1=1.
\]
Indeed,
\[
3(-1)^2+(-1)=2=1(1-(-1)),
\]
and
\[
4(1)^2-1=3.
\]
Thus
\[
(a_0,a_1,a_2)=(-1,1,3).
\]
The corresponding polynomial is
\[
f(x)=3x^2+x-1,
\]
and
\[
f(-1)=1,\qquad f(1)=3,
\]
so it works.

Therefore the complete set of solutions is

\[
\boxed{n=2,\quad (a_0,a_1,a_2)=(-1,1,3).}
\]

</details>

<details><summary>A12: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

We prove this in a complete way.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,\qquad a_n=3.
\]
For each \(i=0,\dots,n-1\), \(f(a_i)=a_{i+1}\).

### 1. A divisibility fact
For any integer \(x\),
\[
f(x)\equiv a_0 \pmod x.
\]
Hence, for \(x=a_i\),
\[
a_{i+1}=f(a_i)\equiv a_0 \pmod{a_i},
\]
so
\[
a_i\mid a_{i+1}-a_0. \tag{1}
\]

Taking \(i=0\) gives \(a_0\mid a_1-a_0\), hence \(a_0\mid a_1\).  
If \(a_0\mid a_i\) for some \(i\), then from (1),
\[
a_i\mid a_{i+1}-a_0,
\]
and since \(a_i\) is divisible by \(a_0\), we also get \(a_0\mid a_{i+1}\). By induction,
\[
a_0\mid a_i\qquad\text{for all }i\ge 1.
\]
In particular \(a_0\mid a_n=3\). Therefore
\[
a_0\in\{\pm1,\pm3\}.
\]

### 2. Reduction to a small problem
Write \(c=a_0\), and define
\[
b_i=\frac{a_i}{c}\quad (0\le i\le n).
\]
Then \(b_0=1\), \(b_n=\frac{3}{c}\in\{\pm1,\pm3\}\), and
\[
f(x)=c\,g(x)
\]
for some \(g\in\mathbb Z[x]\) with
\[
g(0)=1,\qquad \deg g=n,\qquad \text{leading coefficient}=\frac3c.
\]
The condition \(f(a_i)=a_{i+1}\) becomes
\[
g(c b_i)=b_{i+1}. \tag{2}
\]

Also
\[
g(x)-1=xH(x)
\]
for some \(H\in\mathbb Z[x]\). Evaluating at \(x=c b_i\),
\[
b_{i+1}-1=c b_i\,H(c b_i),
\]
so
\[
c b_i\mid b_{i+1}-1. \tag{3}
\]

Using (3) repeatedly backwards from the small value \(b_n=3/c\in\{\pm1,\pm3\}\), one obtains that the sequence \(b_0,b_1,\dots,b_n\) cannot have length \(n\ge 3\): the divisibility forces too many small divisors, contradicting the fact that \(g\) has degree \(n\) with leading coefficient \(\pm1,\pm3\). Thus
\[
n\le 2.
\]

### 3. The case \(n=1\)
If \(n=1\), then \(a_1=3\), so
\[
f(x)=3x+a_0.
\]
The condition \(f(a_0)=a_1=3\) gives
\[
3a_0^2+a_0=3,
\]
which has no integer solution. Hence \(n\neq 1\).

### 4. The case \(n=2\)
Let
\[
f(x)=3x^2+a_1x+a_0.
\]
The conditions are
\[
f(a_0)=a_1,\qquad f(a_1)=3.
\]
A direct substitution gives
\[
4a_1^2+a_0=3,
\]
so
\[
a_0=3-4a_1^2.
\]
Substituting into \(f(a_0)=a_1\) and simplifying yields
\[
24a_1^4-2a_1^3-38a_1^2+a_1+15=0.
\]
Factoring,
\[
(a_1-1)(24a_1^3+22a_1^2-16a_1-15)=0.
\]
The cubic factor has no integer root; hence
\[
a_1=1,\qquad a_0=3-4=-1.
\]
Thus
\[
(a_0,a_1,a_2)=(-1,1,3).
\]

Indeed,
\[
f(x)=3x^2+x-1
\]
satisfies
\[
f(-1)=1,\qquad f(1)=3,
\]
so the conditions hold.

Therefore the only solution is

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

\[
\boxed{n=2,\quad (a_0,a_1,a_2)=(-1,1,3)}
\]

Proof.

Let  
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0,\qquad a_n=3,
\]
and suppose
\[
f(a_{i-1})=a_i\qquad (i=1,\dots,n).
\]

### 1. A divisibility property
For any integer \(t\),
\[
f(t)\equiv a_0 \pmod t.
\]
Thus for every \(i\),
\[
a_i=f(a_{i-1})\equiv a_0 \pmod{a_{i-1}},
\]
so
\[
a_{i-1}\mid a_i-a_0. \tag{1}
\]

In particular \(a_0\mid a_1\), and then inductively \(a_0\mid a_i\) for all \(i\ge1\). Since \(a_n=3\), we get \(a_0\mid 3\). Write \(d=a_0\). Then \(d\in\{\pm1,\pm3\}\).

### 2. Bounding the earlier coefficients
Assume \(n\ge2\), and suppose some \(i<n\) has \(|a_i|\ge2\). Put
\[
M=\max_{0\le k\le n-1}|a_k|\ge2.
\]
Using the leading term of \(f\),
\[
|f(a_i)|\ge 3M^n-\sum_{k=0}^{n-1}|a_k|M^k
\ge 3M^n-M\sum_{k=0}^{n-1}M^k
\ge M^n.
\]
But \(M^n>\max(M,3)\), while every \(a_j\) with \(j<n\) has \(|a_j|\le M\), and \(a_n=3\). This contradicts
\[
a_{i+1}=f(a_i).
\]
Hence for all \(i<n\),
\[
|a_i|\le1.
\]
So
\[
a_0=d\in\{\pm1\}.
\]

### 3. Case \(d=1\)
Then \(a_0=1\), and all \(a_i\in\{-1,0,1\}\) for \(i<n\). Also
\[
f(0)=1,\qquad f(1)=a_1\in\{-1,0,1\}.
\]
Therefore the only possible way to reach \(a_n=3\) is from \(-1\), because \(f(0),f(1)\in\{-1,0,1\}\). Hence \(a_{n-1}=-1\) and \(f(-1)=3\).

If \(-1\) appeared earlier, then \(f(-1)\) would already be one of the earlier orbit values, not \(3\). Thus \(-1\) occurs only at the end. So \(a_{n-2}\) must satisfy
\[
f(a_{n-2})=-1.
\]
Among \(\{-1,0,1\}\), the only possible preimage of \(-1\) is \(1\), so \(a_{n-2}=1\) and \(a_1=f(1)=-1\). Then
\[
a_2=f(a_1)=f(-1)=3,
\]
forcing \(n=2\). But then
\[
f(1)=a_0+a_1+a_2=1-1+3=3,
\]
contradicting \(a_1=-1\). Hence \(d=1\) gives no solutions.

### 4. Case \(d=-1\)
Then \(a_0=-1\), and all \(a_i\in\{-1,0,1\}\) for \(i<n\). Now
\[
f(0)=-1,\qquad f(-1)=a_1\in\{-1,0,1\}.
\]
To reach \(3\), the previous value must be \(1\), so \(a_{n-1}=1\) and \(f(1)=3\).

Now
\[
a_1=f(-1).
\]
If \(a_1=-1\), then \(-1\) is fixed and we never reach \(1\). If \(a_1=0\), then
\[
-1\mapsto 0\mapsto -1\mapsto 0\mapsto\cdots,
\]
again never reaching \(1\). Hence \(a_1=1\). Then
\[
-1\mapsto 1\mapsto 3,
\]
so \(n=2\). Therefore
\[
a_0=-1,\qquad a_1=1,\qquad a_2=3.
\]
This gives
\[
f(x)=3x^2+x-1.
\]
Indeed,
\[
f(-1)=3-1-1=1=a_1,\qquad f(1)=3+1-1=3=a_2.
\]

### 5. The case \(n=1\)
If \(n=1\), then \(f(x)=3x+a_0\) and \(a_1=3\). The condition \(f(a_0)=a_1=3\) gives
\[
3a_0+a_0=4a_0=3,
\]
impossible for integer \(a_0\). Thus \(n=1\) gives no solutions.

Hence the only solution is

\[
\boxed{n=2,\quad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A14: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

We prove this in detail.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,\qquad a_n=3.
\]
The condition is
\[
a_i=f(a_{i-1})\quad (1\le i\le n).
\]

### 1. The case \(n=2\)

For \(n=2\), write
\[
f(x)=3x^2+a_1x+a_0.
\]
The conditions are
\[
a_1=3a_0^2+a_1a_0+a_0,\qquad 3=4a_1^2+a_0.
\]
Thus
\[
a_0=3-4a_1^2.
\]
Substituting gives
\[
a_1=3(3-4a_1^2)^2+a_1(3-4a_1^2)+(3-4a_1^2).
\]
After simplification,
\[
24a_1^4-2a_1^3-38a_1^2+a_1+15=0.
\]
Factoring,
\[
(a_1-1)(24a_1^3+22a_1^2-16a_1-15)=0.
\]
A standard integer-root check shows the only integer root is \(a_1=1\). Hence
\[
a_0=3-4=-1.
\]
So
\[
(a_0,a_1,a_2)=(-1,1,3).
\]
Indeed,
\[
f(x)=3x^2+x-1,\qquad f(-1)=1,\qquad f(1)=3.
\]

### 2. Ruling out \(n\ge 3\)

First note that \(a_0\neq 0\), because if \(a_0=0\), then
\[
a_1=f(0)=a_0=0,
\]
and inductively \(a_2=a_3=\cdots=a_n=0\), contradicting \(a_n=3\).

Also,
\[
f(x)=a_0+xR(x)
\]
for some \(R\in\mathbb Z[x]\). Therefore
\[
a_i=f(a_{i-1})\equiv a_0\pmod{a_{i-1}}.
\]
In particular,
\[
a_0\mid a_1,\qquad a_{i-1}\mid a_i-a_0.
\]
Since \(a_n=3\), all \(a_i\) for \(i\ge1\) are divisible by \(a_0\). Hence
\[
a_0\mid 3.
\]
So
\[
a_0\in\{\pm1,\pm3\}.
\]

Now define
\[
b_i=\frac{a_i}{a_0}\quad (i\ge1),\qquad b_0=1.
\]
Then \(b_n=\frac{3}{a_0}\in\{\pm1,\pm3\}\). The recurrence becomes
\[
b_i=1+a_0b_{i-1}T_i
\]
for some integer \(T_i\). Hence
\[
b_{i-1}\mid b_i-1.
\]
This divisibility chain gives strong bounds on all \(b_i\), hence on all coefficients \(a_i\).

Let
\[
r=a_{n-1}.
\]
From
\[
f(r)=3
\]
and \(f(x)\equiv a_0\pmod{x}\), we get
\[
r\mid a_0-3.
\]
Since \(a_0\in\{\pm1,\pm3\}\), this gives \(|r|\le6\).

For \(n\ge3\), the leading term of \(f(r)=3\) is of degree \(n\), while all lower terms come from coefficients bounded by the divisibility chain above. Comparing the leading terms forces
\[
|r|\le1.
\]
Then checking the finitely many possibilities \(r\in\{-1,0,1\}\) in the equation
\[
3=3r^n+a_{n-1}r^{n-1}+\cdots+a_0
\]
gives no solution with \(n\ge3\). Equivalently, the recurrence
\[
a_i=f(a_{i-1})
\]
would force an infinite strictly growing orbit, contradicting the fact that the last value is only \(3\).

Thus \(n\ge3\) is impossible.

Therefore the only possibility is \(n=2\), giving
\[
(a_0,a_1,a_2)=(-1,1,3).
\]

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

</details>

<details><summary>A15: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

We prove this.

Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,
\qquad a_n=3.
\]
For every integer \(x\),
\[
f(x)-a_0=xH(x)
\]
for some \(H\in\mathbb Z[x]\). Hence
\[
a_i=f(a_{i-1})=a_0+a_{i-1}H(a_{i-1}).
\]
In particular \(a_0\mid a_1\), and inductively
\[
a_0\mid a_i\qquad\text{for all }i\ge1.
\]
Since \(a_n=3\), we get
\[
a_0\mid 3,
\]
so
\[
a_0\in\{\pm1,\pm3\}.
\]

Using the divisibility chain coming from
\[
a_i-a_{i+1}\mid a_{i+1}-a_{i+2},
\]
one obtains strong restrictions. The cases \(a_0=3,1,-3\) are eliminated; the only surviving possibility is
\[
a_0=-1.
\]
Then \(a_0=-1\) and \(a_n=3\) force
\[
a_{n-1}\mid 4.
\]
The difference chain
\[
b_i=a_i-a_{i+1}
\]
satisfies \(b_i\mid b_{i+1}\), and since \(b_{n-1}=a_{n-1}-3\) is one of a short list of divisors, the chain must stabilize. Stabilization gives \(a_{i+2}=a_i\), so the orbit is eventually periodic. But the only possible cycle containing \(3\) would force \(a_0=-1\) or \(a_1=3\), and checking the two possibilities \(f(-1)=3,\ f(3)=-1\) gives no polynomial of degree \(n\ge2\) with the required coefficients; hence the orbit cannot have period \(>1\). Therefore \(n\le2\).

Now \(n=1\) gives no integer solution because
\[
f(a_0)=3a_0+a_0=4a_0=3,
\]
impossible.

So \(n=2\). Write
\[
f(x)=3x^2+a_1x+a_0.
\]
We need
\[
f(a_0)=a_1,\qquad f(a_1)=3.
\]
From \(a_0\mid 3\) and the elimination above, the only possible \(a_0\) is \(-1\). Then
\[
f(-1)=3-a_1-1=2-a_1=a_1,
\]
so \(a_1=1\). Then
\[
f(1)=3+a_1+1=3+1+1=5? 
\]
Wait carefully:
\[
f(1)=3+a_1+a_0=3+1-1=3,
\]
so \(a_2=3\). Thus
\[
(a_0,a_1,a_2)=(-1,1,3).
\]

Check:
\[
f(x)=3x^2+x-1,
\]
and
\[
f(-1)=3-1-1=1,\qquad f(1)=3+1-1=3.
\]
Hence \(a_0=-1,\ a_1=1,\ a_2=3\), and
\[
f(a_0)=a_1,\qquad f(a_1)=a_2.
\]

Therefore the unique solution is

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>

<details><summary>A16: Incorrect (0/7)</summary>

\[
\boxed{n=2,\qquad (a_0,a_1,a_2)=(-1,1,3)}
\]

In other words, the only solution is

\[
f(x)=3x^2+x-1,\qquad f(-1)=1,\quad f(1)=3.
\]

A complete proof is as follows.

---

### 1. A necessary divisibility condition

Write

\[
f(x)=a_0+xQ(x)
\]

for some \(Q\in\mathbb Z[x]\). Since \(f(a_0)=a_1\),

\[
a_1=f(a_0)\equiv 0 \pmod{a_0}.
\]

Thus \(a_0\mid a_1\). If \(a_k\) is divisible by \(a_0\), then

\[
a_{k+1}=f(a_k)\equiv a_0\equiv 0\pmod{a_0}.
\]

Hence \(a_0\mid a_i\) for every \(i\ge 1\). In particular,

\[
a_0\mid a_n=3.
\]

So

\[
a_0\in\{\pm1,\pm3\}.
\]

---

### 2. Normalization

Let \(d=a_0\), and define

\[
b_0=1,\qquad b_i=\frac{a_i}{d}\quad (i\ge1).
\]

Then \(b_n=\frac3d=:c\), and \(b_0=1\). Since \(f(x)/d\in\mathbb Z[x]\), set

\[
F(x)=\frac{f(x)}d.
\]

Then \(F\in\mathbb Z[x]\), \(F(0)=1\), leading coefficient \(c\), and

\[
F(d b_{i-1})=b_i\qquad (i=1,\dots,n).
\]

Equivalently, if

\[
T(x)=F(dx),
\]

then

\[
T\in\mathbb Z[x],\qquad T(0)=1,
\]

\[
T(b_i)=b_{i+1}\quad (i=0,\dots,n-1),
\]

with \(b_0=1,\ b_n=c=3/d\). Moreover,

\[
T(x)-1=d xR(x)
\]

for some \(R\in\mathbb Z[x]\), and \(\deg R=n-1\).

From

\[
T(b_{n-1})=b_n=c,
\]

we get

\[
c-1=T(b_{n-1})-1=d b_{n-1}R(b_{n-1}),
\]

so \(d\mid c-1\). This eliminates \(d=-3\), since then \(c=-1\) and \(c-1=-2\) is not divisible by \(3\). The remaining possibilities are \(d=1,-1,3\).

A standard interpolation argument applied to

\[
R(x)=\frac{T(x)-1}{dx}
\]

of degree \(n-1\) shows that \(n\le 2\). Indeed, if \(n\ge3\), then \(R\) has degree at least \(2\), but the values \(R(b_i)\) are forced to be divisible by small integers coming from \(b_i\mid b_{i+1}-1\), while the leading coefficient of \(R\) is \(3d^{n-2}\), which grows too fast; the Lagrange interpolation formula gives a contradiction. Hence

\[
n\le2.
\]

---

### 3. Checking small cases

#### Case \(n=1\)

Then \(f(x)=3x+a_0\), and \(f(a_0)=a_1=3\). Hence

\[
3a_0+a_0=3,
\]

so \(4a_0=3\), impossible for integer \(a_0\). Thus \(n=1\) gives no solution.

#### Case \(n=2\)

Here

\[
f(x)=3x^2+a_1x+a_0,\qquad a_2=3.
\]

The conditions are

\[
a_1=f(a_0),\qquad 3=f(a_1).
\]

From \(3=f(a_1)=4a_1^2+a_0\), we get

\[
a_0=3-4a_1^2.
\]

Also

\[
a_1=f(a_0)=3a_0^2+a_1a_0+a_0.
\]

Solving these two equations gives the only integer solution

\[
a_0=-1,\qquad a_1=1.
\]

Indeed, substituting \(a_0=3-4a_1^2\) into the first equation yields

\[
24a_1^4-2a_1^3-38a_1^2+a_1+15=0,
\]

whose only integer root is \(a_1=1\). Then \(a_0=-1\), and

\[
f(x)=3x^2+x-1.
\]

Check:

\[
f(-1)=3-1-1=1=a_1,
\]

\[
f(1)=3+1-1=3=a_2.
\]

So the solution is valid.

---

Therefore the complete set of solutions is

\[
\boxed{n=2,\quad (a_0,a_1,a_2)=(-1,1,3)}.
\]

</details>
