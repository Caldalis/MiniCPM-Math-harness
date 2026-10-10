# PB-Basic-020

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Find all pairs of primes $(a, b)$ such that $a^2 - ab - b^3 = 1$.

## Swarm: accepted (best candidate `P5`; self-verification grades [7, 7, 7]; 500,690 tokens in 52 calls)

**Blind grade: Correct (7/7).** Rules out b=2, writes a = mb +/- 1, bounds m via (m-1)(m-2) <= 0 and (b-1)(d-1) = m(3-m) respectively, finding only (7,3) and the non-prime a=14; all algebra checks out and the answer is verified.

\[
\boxed{(a,b)=(7,3)}
\]

Proof:

Given
\[
a^2-ab-b^3=1,
\]
we rewrite as
\[
a(a-b)=b^3+1>0.
\]
Since \(a>0\), this forces \(a>b\).

Now reduce the original equation modulo \(b\):
\[
a^2\equiv 1 \pmod b.
\]
So
\[
b\mid (a-1)(a+1).
\]

If \(b=2\), then
\[
a^2-2a-9=0,
\]
whose discriminant is \(40\), not a square, so there is no prime \(a\). Hence \(b\) is odd.

Since \(b\) is an odd prime, \(b\nmid 2\), so \(b\) cannot divide both \(a-1\) and \(a+1\). Thus
\[
a\equiv 1 \pmod b \quad \text{or} \quad a\equiv -1 \pmod b.
\]
Because \(a>b\), we may write either
\[
a=mb+1 \quad \text{or} \quad a=mb-1.
\]

### Case 1: \(a=mb+1\)

Then
\[
a(a-b)=(mb+1)((m-1)b+1).
\]
Expanding,
\[
a(a-b)=m(m-1)b^2+(2m-1)b+1.
\]
Thus
\[
m(m-1)b^2+(2m-1)b+1=b^3+1.
\]
Dividing by \(b\),
\[
m(m-1)b+2m-1=b^2.
\]
So
\[
b(b-m(m-1))=2m-1.
\]
Let \(d=b-m(m-1)>0\). Then
\[
bd=2m-1.
\]
Hence
\[
b\le 2m-1,\qquad b\ge m(m-1)+1.
\]
Therefore
\[
m(m-1)+1\le 2m-1,
\]
so
\[
(m-1)(m-2)\le 0.
\]
Thus \(m\le 2\). Since \(m=1\) gives \(b^2=1\), impossible, we get \(m=2\). Then
\[
b(b-2)=3,
\]
so \(b=3\). Hence
\[
a=2\cdot 3+1=7.
\]

### Case 2: \(a=mb-1\)

Since \(a>b\), we have \(m\ge 2\). Substituting,
\[
a(a-b)=(mb-1)((m-1)b-1),
\]
so
\[
m(m-1)b^2-(2m-1)b+1=b^3+1.
\]
Dividing by \(b\),
\[
m(m-1)b-(2m-1)=b^2.
\]
Thus
\[
b(m(m-1)-b)=2m-1.
\]
Let
\[
d=m(m-1)-b>0.
\]
Then
\[
bd=2m-1,\qquad b+d=m(m-1).
\]
Hence
\[
(b-1)(d-1)=bd-b-d+1=(2m-1)-m(m-1)+1=m(3-m).
\]
Since \(b,d\ge 1\), the left side is nonnegative, so \(m\le 3\). Thus \(m=2\) or \(m=3\).

- If \(m=2\), then \(b+d=2\) and \(bd=3\), impossible.
- If \(m=3\), then \(b+d=6\) and \(bd=5\), so \(\{b,d\}=\{1,5\}\). Since \(b\) is prime, \(b=5\), giving
\[
a=3\cdot 5-1=14,
\]
which is not prime.

Therefore Case 2 gives no solutions.

Finally,
\[
7^2-7\cdot 3-3^3=49-21-27=1,
\]
so \((7,3)\) is valid.

\[
\boxed{(7,3)}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 16,282 | Correct (7/7) | Complete and rigorous: excludes b=2, shows a \| b^2-b+1, derives c^2=1 (mod b) with 1<=c<=b-1, rules out c=b-1 because b-1 \| b(b-1)+1 forces b=2, and c=1 gives only (7,3), verified. |
| A2 | stop | 26,931 | Correct (7/7) | Uses a = +/-1 (mod b): the case a=kb+1 bounds k to give (7,3), and the case a=kb-1 is validly excluded via a \| k^3+1, hence a \| k^2-k+1, forcing b < k and a size contradiction bc >= 3(k-1)^2 > 2k-1; complete. |
| A3 | stop | 17,083 | Correct (7/7) | Complete and rigorous: excludes b=2, proves a \| b^2-b+1, writes b^2-b+1=ac to get a=b+(b+1)c with 1<=c<b, uses a^2=1 (mod b) and a=c (mod b) to force c in {1, b-1}, correctly solves both cases to get only (7,3), and verifies it. |
| A4 | stop | 18,362 | Correct (7/7) | Complete and correct alternative argument: writes a=qb+e with e=+-1, derives b \| 2q-1 and the valid bound q^2-4q+2<=0, rules out q=1, and checks q=2 (giving (7,3)) and q=3 (giving a=14, not prime), so only (7,3) remains, verified. |
| A5 | stop | 16,186 | Correct (7/7) | Complete and rigorous: excludes b=2, shows a \| b^2-b+1, derives k^2=1 (mod b) with 1<=k<=b-1, eliminates k=b-1 with correct algebra (b^3-2b+1=b^2-b+1 is impossible), and k=1 gives only (7,3), which is verified. |
| A6 | stop | 15,923 | Correct (7/7) | Complete and rigorous: excludes b=2, uses parity to get a>=b+2 so a \| b^2-b+1, derives c^2=1 (mod b) with 1<=c<=b-1, and correctly solves the cases c=1 and c=b-1 to obtain only (7,3), which is verified. |
| A7 | stop | 17,914 | Correct (7/7) | From a^2 = 1 (mod b) it writes a = kb +/- 1, derives b \| 2k-1 and bounds k in both sign cases (using b+n <= bn+1 for the minus case), correctly isolating (7,3) and excluding a=14, with verification; complete and rigorous. |
| A8 | stop | 15,537 | Correct (7/7) | Proves a \| b^2-b+1 = ac, deduces c^2 = 1 (mod b) with 1 <= c <= b-1 so c in {1, b-1}, and correctly solves both cases (the second giving b(b^2-b-1)=0) to get only the verified pair (7,3); complete. |
| A9 | stop | 15,029 | Correct (7/7) | Complete and rigorous: rules out a \| b+1 via b^3=b, gets a \| b^2-b+1 and a=(k+1)b+k with k^2=1 (mod b) and 1<=k<=b-1, correctly eliminates k=b-1 by algebra, and k=1 gives only (7,3), which is verified. |
| A10 | stop | 19,505 | Correct (7/7) | Complete and rigorous: excludes b=2, shows a \| b^2-b+1 (a=b+1 impossible by parity), derives a=(c+1)b+c with c^2=1 (mod b) and the bound c(c+1)<b, which forces c=1 and hence only (7,3), which is verified. |
| A11 | stop | 21,485 | Correct (7/7) | Proves a \| b^2-b+1 = at, obtains t^2 = 1 (mod b) with 1 <= t <= b-1, correctly eliminates t=b-1 and solves t=1 to get b=3, a=7 with verification; complete and rigorous. |
| A12 | stop | 24,543 | Correct (7/7) | Complete and rigorous: rules out a \| b+1, writes b^2-b+1=am to get a=(m+1)b+m with m^2=1 (mod b) and 1<=m<=b-1, and correctly treats m=1 and m=b-1 (all primes b, including 2, covered) to get only (7,3), verified. |
| A13 | stop | 25,006 | Correct (7/7) | Complete and correct alternative argument: uses parity to write a=2kb+-1, reduces to (b-A)^2=A^2+-(4k-1) with A=k(2k-1), and correctly shows this is a perfect square only for k=1 in the + case, giving only (7,3); the unstated reason that b-A>0 is immediate from b^2>2Ab. |
| A14 | stop | 13,790 | Correct (7/7) | Excludes b=2, proves a \| b^2-b+1 = ac, and for c >= 2 shows the quadratic in b cannot have a square discriminant since t(S+t) = c^2-1 < S+t, leaving c=1 and the verified pair (7,3); complete. |
| A15 | stop | 17,839 | Correct (7/7) | Proves a \| b^2-b+1 = ka, uses a = k (mod b) and a^2 = 1 (mod b) with k < b to get k in {1, b-1}, and correctly solves both cases to obtain only (7,3), verified; complete and rigorous. |
| A16 | stop | 19,327 | Correct (7/7) | Shows a does not divide b+1, so b^2-b+1 = ac, derives b(b-(c^2+c+1)) = c^2-1 and rules out c >= 2 since then b > c^2+c+1 > c^2-1 > 0 yet b \| c^2-1, leaving c=1 and the verified pair (7,3); complete. |

<details><summary>A1: Correct (7/7)</summary>

\[
a^2-ab-b^3=1
\]

Rewrite as

\[
a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]

Since \(a>0\) and \(b^3+1>0\), we must have \(a>b\).

First check \(b=2\):

\[
a^2-2a-9=0,
\]

whose discriminant is \(40\), not a square. Hence \(b\neq 2\), so \(b\ge 3\). Then \(b\) is odd, so \(b+1\) is even and greater than \(2\), hence composite.

Now \(a\mid (b+1)(b^2-b+1)\). If \(a\mid b+1\), then since \(a>b\) and \(b+1<2a\), we must have \(a=b+1\), impossible because \(b+1\) is composite. Thus

\[
a\mid b^2-b+1.
\]

Write

\[
b^2-b+1=ac
\]

for some positive integer \(c\). Substituting into the original equation gives

\[
a(a-b)=(b+1)ac,
\]

so dividing by \(a\),

\[
a-b=c(b+1).
\]

Thus

\[
a=(c+1)b+c.
\]

Also \(a>b\) implies

\[
c=\frac{b^2-b+1}{a}<\frac{b^2-b+1}{b}<b,
\]

so \(1\le c\le b-1\).

Now using \(ac=b^2-b+1\) and \(a=(c+1)b+c\),

\[
c\big((c+1)b+c\big)=b^2-b+1.
\]

Rearranging,

\[
b^2-(c^2+c+1)b+(1-c^2)=0.
\]

Reducing modulo \(b\),

\[
c^2\equiv 1\pmod b.
\]

Since \(b\) is prime and \(1\le c\le b-1\), we must have

\[
c=1 \quad \text{or} \quad c=b-1.
\]

### Case 1: \(c=1\)

Then

\[
a=2b+1.
\]

But also \(a=b^2-b+1\), so

\[
2b+1=b^2-b+1,
\]

hence

\[
b^2-3b=0,
\]

so \(b=3\). Therefore

\[
a=2(3)+1=7.
\]

### Case 2: \(c=b-1\)

Then \(b-1\mid b^2-b+1\). But

\[
b^2-b+1=b(b-1)+1,
\]

so \(b-1\mid 1\), forcing \(b=2\), contradiction.

Thus the only possible pair is

\[
(a,b)=(7,3).
\]

Check:

\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

\[
\boxed{(7,3)}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

\[
\boxed{(a,b)=(7,3)}
\]

Proof:

\[
a^2-ab-b^3=1 \iff a(a-b)=b^3+1.
\]

Since \(a>0\) and \(b^3+1>0\), we have \(a>b\).

First check \(b=2\):
\[
a^2-2a-8=1 \iff a^2-2a-9=0 \iff (a-1)^2=10,
\]
which has no integer solution. Hence \(b\ge 3\) is odd.

Now reduce the original equation modulo \(b\):
\[
a^2\equiv 1 \pmod b.
\]
Thus
\[
b\mid (a-1)(a+1).
\]
Since \(b\) is prime, either
\[
a\equiv 1 \pmod b \quad \text{or} \quad a\equiv -1 \pmod b.
\]

### Case 1: \(a=kb+1\), \(k\ge 1\)

Then
\[
a-b=(k-1)b+1.
\]
Using \(a(a-b)=b^3+1\),
\[
(kb+1)((k-1)b+1)=b^3+1.
\]
Expanding and simplifying gives
\[
b^2=k(k-1)b+2k-1,
\]
so
\[
b\bigl(b-k(k-1)\bigr)=2k-1.
\]
Thus \(b>k(k-1)\), and since \(b\le 2k-1\), we need
\[
k(k-1)<2k-1.
\]
This forces \(k\le 2\).  
- If \(k=1\), then \(b^2=1\), impossible since \(b\ge 3\).  
- If \(k=2\), then
\[
b(b-2)=3,
\]
so \(b=3\). Hence
\[
a=2\cdot 3+1=7.
\]
This gives \((a,b)=(7,3)\), which works:
\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

### Case 2: \(a=kb-1\), \(k\ge 2\)

Then
\[
a-b=(k-1)b-1.
\]
Again using \(a(a-b)=b^3+1\),
\[
(kb-1)((k-1)b-1)=b^3+1.
\]
Expanding and simplifying gives
\[
b\bigl(k(k-1)-b\bigr)=2k-1.
\]
Let
\[
c=k(k-1)-b>0.
\]
Then
\[
bc=2k-1,\qquad b+c=k(k-1).
\]

From \(a(a-b)=b^3+1\), reducing modulo \(a\),
\[
b^3\equiv -1 \pmod a.
\]
Since \(a=kb-1\), we have \(kb\equiv 1\pmod a\). Multiplying by \(k^3\),
\[
k^3b^3\equiv -k^3 \pmod a.
\]
But \(k^3b^3=(kb)^3\equiv 1\pmod a\), so
\[
k^3\equiv -1 \pmod a,
\]
hence
\[
a\mid k^3+1=(k+1)(k^2-k+1).
\]

For \(k=2\), the equation \(b^2-2b+3=0\) has no real solutions, so \(k\ge 3\). Then \(a=kb-1\ge 3k-1>k+1\), so \(a\nmid k+1\). Since \(a\) is prime, it must divide \(k^2-k+1\). Therefore
\[
a\le k^2-k+1.
\]
But \(a=kb-1\), so
\[
kb-1\le k^2-k+1
\]
which gives
\[
b<k.
\]
Thus \(b\le k-1\). Hence
\[
c=k(k-1)-b\ge k(k-1)-(k-1)=(k-1)^2.
\]
Since \(b\ge 3\),
\[
bc\ge 3(k-1)^2,
\]
but \(bc=2k-1\), impossible for \(k\ge 3\). So Case 2 gives no solutions.

Therefore the only pair is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

\[
a^2-ab-b^3=1
\]

Rewrite as

\[
a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]

Since \(b^3+1>0\) and \(a>0\), we must have \(a>b\).

First check \(b=2\). Then

\[
a(a-2)=9,
\]

so \(a\mid 9\), hence \(a=3\), but \(3\cdot 1=3\neq 9\). Thus \(b\neq 2\), so \(b\ge 3\). Hence \(a,b\) are odd primes and \(a>b\) implies \(a-b\ge 2\), i.e. \(a\ge b+2\).

Now reduce the original equation modulo \(a\):

\[
-b^3\equiv 1 \pmod a,
\]

so

\[
a\mid b^3+1=(b+1)(b^2-b+1).
\]

But \(a\ge b+2>b+1\), so \(a\nmid b+1\). Since \(a\) is prime, we must have

\[
a\mid b^2-b+1.
\]

Write

\[
b^2-b+1=ac
\]

for some positive integer \(c\). Then

\[
a(a-b)=(b+1)(b^2-b+1)=(b+1)ac,
\]

so

\[
a-b=(b+1)c.
\]

Thus

\[
a=b+(b+1)c.
\]

Also,

\[
c=\frac{b^2-b+1}{a}\le \frac{b^2-b+1}{b+2}<b,
\]

so \(1\le c<b\).

Now reduce the original equation modulo \(b\):

\[
a^2\equiv 1 \pmod b.
\]

Hence

\[
b\mid a^2-1=(a-1)(a+1).
\]

Since \(b\) is prime,

\[
b\mid a-1 \quad \text{or} \quad b\mid a+1.
\]

But from \(a=b+(b+1)c\), we have \(a\equiv c\pmod b\). Therefore

\[
b\mid c-1 \quad \text{or} \quad b\mid c+1.
\]

Because \(1\le c<b\), this forces

\[
c=1 \quad \text{or} \quad c=b-1.
\]

### Case 1: \(c=1\)

Then

\[
a-b=b+1,
\]

so

\[
a=2b+1.
\]

Also \(b^2-b+1=ac=a\), hence

\[
b^2-b+1=2b+1.
\]

Thus

\[
b^2-3b=0,
\]

so \(b=3\). Therefore

\[
a=2(3)+1=7.
\]

This gives the pair \((7,3)\).

### Case 2: \(c=b-1\)

Then

\[
a=b+(b+1)(b-1)=b^2+b-1.
\]

Also

\[
b^2-b+1=a(b-1).
\]

Substituting \(a=b^2+b-1\),

\[
b^2-b+1=(b^2+b-1)(b-1)=b^3-2b+1.
\]

So

\[
b^3-b^2-b=0,
\]

i.e.

\[
b(b^2-b-1)=0.
\]

Since \(b\ge 3\), this is impossible.

Therefore the only possible pair is \((7,3)\). Checking:

\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

Hence the complete set of prime pairs is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

\[
a^2-ab-b^3=1
\]

First note that

\[
a^2-ab=b^3+1>0,
\]

so \(a(a-b)>0\). Since \(a>0\), we must have \(a>b\).

Reducing the original equation modulo \(b\),

\[
a^2\equiv 1 \pmod b.
\]

Because \(b\) is prime,

\[
a\equiv \pm 1 \pmod b.
\]

Thus we may write

\[
a=qb+\varepsilon,
\]

where \(q\ge 1\) and \(\varepsilon\in\{1,-1\}\).

Now substitute into the original equation. Since

\[
a(a-b)=b^3+1,
\]

we get

\[
(qb+\varepsilon)\big((q-1)b+\varepsilon\big)=b^3+1.
\]

Expanding the left-hand side,

\[
q(q-1)b^2+(2q-1)\varepsilon b+1=b^3+1.
\]

Canceling \(1\) and dividing by \(b\),

\[
q(q-1)b+(2q-1)\varepsilon=b^2. \tag{1}
\]

Rearranging,

\[
b\big(b-q(q-1)\big)=(2q-1)\varepsilon.
\]

Hence \(b\mid 2q-1\). Write

\[
2q-1=bm
\]

with \(m\ge 1\). Then

\[
b-q(q-1)=m\varepsilon,
\]

so

\[
q(q-1)=b-m\varepsilon\le b+m.
\]

Also,

\[
m=\frac{2q-1}{b}\le \frac{2q-1}{2}=q-\frac12,
\]

so \(m\le q-1\). Therefore

\[
q(q-1)\le b+m\le (2q-1)+(q-1)=3q-2.
\]

Thus

\[
q^2-q\le 3q-2,
\]

so

\[
q^2-4q+2\le 0.
\]

This implies \(q\le 3\). Also \(q=1\) is impossible from (1), since then \(b^2=\varepsilon\), impossible for \(b\ge2\). Hence

\[
q=2 \quad \text{or} \quad q=3.
\]

### Case 1: \(q=2\)

Then

\[
2q-1=3,
\]

so \(b=3\). Substituting into (1),

\[
9=2\cdot1\cdot3+3\varepsilon=6+3\varepsilon,
\]

so \(\varepsilon=1\). Hence

\[
a=2\cdot3+1=7.
\]

This gives \((a,b)=(7,3)\), and indeed

\[
7^2-7\cdot3-3^3=49-21-27=1.
\]

### Case 2: \(q=3\)

Then

\[
2q-1=5,
\]

so \(b=5\). Substituting into (1),

\[
25=3\cdot2\cdot5+5\varepsilon=30+5\varepsilon,
\]

so \(\varepsilon=-1\). Hence

\[
a=3\cdot5-1=14,
\]

which is not prime. So this case is invalid.

Therefore the only prime pair is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

\[
\boxed{(a,b)=(7,3)}
\]

Proof:

From
\[
a^2-ab-b^3=1
\]
we get
\[
a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]
Since \(a>0\) and \(b^3+1>0\), we must have \(a-b>0\), so \(a>b\). Also \(a,b\) are primes, hence \(a,b\ge 2\).

### 1. Exclude \(b=2\)

If \(b=2\), then
\[
a(a-2)=9.
\]
Since \(a>2\) is prime, the only possible prime divisor of \(9\) is \(3\), so \(a=3\). But then
\[
3(3-2)=3\ne 9,
\]
contradiction. Hence \(b\ge 3\).

### 2. Use divisibility

For \(b\ge 3\), \(b\) is odd, so \(a>b\) also implies \(a\ge b+2>b+1\). Thus \(a\nmid b+1\). Since
\[
a\mid (b+1)(b^2-b+1),
\]
and \(a\) is prime, we must have
\[
a\mid b^2-b+1.
\]
Write
\[
b^2-b+1=ka
\]
for some positive integer \(k\). Then
\[
a(a-b)=(b+1)(b^2-b+1)=(b+1)ka.
\]
Dividing by \(a\),
\[
a-b=k(b+1),
\]
so
\[
a=b+k(b+1).
\]
Substituting into \(b^2-b+1=ka\) gives
\[
b^2-b+1=k\bigl(b+k(b+1)\bigr),
\]
or
\[
b^2-b+1=kb+k^2(b+1). \tag{1}
\]

### 3. Bound \(k\)

Since \(a>b\),
\[
k=\frac{b^2-b+1}{a}<\frac{b^2-b+1}{b}=b-1+\frac1b<b.
\]
Thus
\[
1\le k\le b-1.
\]

Now reduce (1) modulo \(b\):
\[
1\equiv k^2 \pmod b,
\]
so
\[
k^2\equiv 1\pmod b.
\]
Because \(b\) is prime,
\[
k\equiv \pm 1\pmod b.
\]
But \(1\le k\le b-1\), so either \(k=1\) or \(k=b-1\).

### 4. Rule out \(k=b-1\)

If \(k=b-1\), then from (1),
\[
b^2-b+1=(b-1)b+(b-1)^2(b+1).
\]
The right-hand side simplifies to
\[
b^3-2b+1.
\]
Thus
\[
b^3-2b+1=b^2-b+1,
\]
so
\[
b^3-b^2-b=0,
\]
i.e.
\[
b(b^2-b-1)=0,
\]
which is impossible for a prime \(b\ge 3\). Hence \(k=1\).

### 5. Solve for \(b\)

With \(k=1\), equation (1) becomes
\[
b^2-b+1=b+(b+1)=2b+1.
\]
Therefore
\[
b^2-3b=0,
\]
so
\[
b=3.
\]
Then
\[
a=b+k(b+1)=3+1\cdot 4=7.
\]

### 6. Verification

\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

Thus the only solution is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

\[
\boxed{(a,b)=(7,3)}
\]

Proof:

\[
a^2-ab-b^3=1 \iff a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]

Since \(a>0\) and \(b^3+1>0\), we must have \(a-b>0\), so \(a>b\).

First check \(b=2\). Then

\[
a(a-2)=9,
\]

so \(a=3\) is the only possible prime divisor, but \(3\cdot 1\neq 9\). Thus \(b\neq 2\), so \(b\) is odd.

Since \(a>b\) and both are odd primes, \(a-b\) is a positive even integer, hence \(a\ge b+2\). In particular, \(a>b+1\), so \(a\nmid b+1\). Because \(a\) is prime and

\[
a\mid (b+1)(b^2-b+1),
\]

we must have

\[
a\mid b^2-b+1.
\]

Write

\[
b^2-b+1=ac
\]

for some positive integer \(c\). Substituting into \(a(a-b)=(b+1)(b^2-b+1)\), we get

\[
a(a-b)=(b+1)ac,
\]

so

\[
a-b=c(b+1).
\]

Thus

\[
a=b+c(b+1).
\]

Reducing modulo \(b\),

\[
a\equiv c \pmod b.
\]

Also,

\[
ac=b^2-b+1\equiv 1 \pmod b,
\]

so

\[
c^2\equiv 1 \pmod b.
\]

Since \(a>b\),

\[
c=\frac{b^2-b+1}{a}<\frac{b^2-b+1}{b}<b,
\]

so \(1\le c\le b-1\). Because \(b\) is prime, \(c^2\equiv 1\pmod b\) implies

\[
c=1 \quad \text{or} \quad c=b-1.
\]

### Case 1: \(c=1\)

Then

\[
a=b+(b+1)=2b+1.
\]

But also \(ac=a=b^2-b+1\), so

\[
2b+1=b^2-b+1.
\]

Hence

\[
b^2-3b=0,
\]

so \(b=3\). Then

\[
a=2(3)+1=7.
\]

This gives \((a,b)=(7,3)\).

### Case 2: \(c=b-1\)

Then

\[
a=b+(b-1)(b+1)=b^2+b-1.
\]

Using \(ac=b^2-b+1\),

\[
(b^2+b-1)(b-1)=b^2-b+1.
\]

Expanding,

\[
b^3-2b+1=b^2-b+1,
\]

so

\[
b^3-b^2-b=0,
\]

or

\[
b(b^2-b-1)=0.
\]

No prime \(b\) satisfies \(b^2-b-1=0\), since its discriminant is \(5\), not a perfect square. Thus this case is impossible.

Finally, checking:

\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

Therefore the only pair is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

\[
\boxed{(a,b)=(7,3)}
\]

Proof:

Given
\[
a^2-ab-b^3=1,
\]
we rewrite as
\[
a(a-b)=b^3+1>0.
\]
Since \(a>0\), this implies \(a>b\).

Now reduce modulo \(b\):
\[
a^2\equiv 1 \pmod b,
\]
so
\[
b\mid (a-1)(a+1).
\]
Because \(b\) is prime,
\[
b\mid a-1 \quad \text{or} \quad b\mid a+1.
\]
Thus we may write
\[
a=kb+\varepsilon,
\qquad \varepsilon\in\{1,-1\},
\]
with \(k\ge 1\). For \(\varepsilon=-1\), since \(a>b\), actually \(k\ge 2\).

Substitute \(a=kb+\varepsilon\) into \(a(a-b)=b^3+1\):
\[
(kb+\varepsilon)\bigl((k-1)b+\varepsilon\bigr)=b^3+1.
\]
Expanding,
\[
k(k-1)b^2+\varepsilon(2k-1)b+1=b^3+1,
\]
so
\[
b^3=k(k-1)b^2+\varepsilon(2k-1)b.
\]
Dividing by \(b\),
\[
b^2=k(k-1)b+\varepsilon(2k-1). \tag{1}
\]
Taking (1) modulo \(b\), we get
\[
b\mid 2k-1.
\]
Write
\[
2k-1=bn
\]
for some positive integer \(n\).

### Case 1: \(\varepsilon=1\)

Then (1) becomes
\[
b^2=k(k-1)b+bn,
\]
so
\[
b=k(k-1)+n.
\]
Since \(n\ge 1\),
\[
b\ge k(k-1)+1.
\]
Also \(bn=2k-1\), so
\[
2k-1=bn\ge b\ge k(k-1)+1.
\]
Hence
\[
2k-1\ge k^2-k+1,
\]
so
\[
k^2-3k+2\le 0,
\]
i.e.
\[
(k-1)(k-2)\le 0.
\]
Thus \(k\le 2\). Since \(k=1\) would force \(b=1\), impossible, we must have \(k=2\). Then
\[
b=2+n,\qquad bn=3.
\]
The only positive solution is \(n=1\), giving
\[
b=3,\qquad a=kb+1=2\cdot 3+1=7.
\]
So \((a,b)=(7,3)\) is a solution.

### Case 2: \(\varepsilon=-1\)

Then (1) becomes
\[
b^2=k(k-1)b-bn,
\]
so
\[
b=k(k-1)-n,
\]
or equivalently
\[
b+n=k(k-1).
\]
Also \(bn=2k-1\). Since for positive integers \(b,n\),
\[
b+n\le bn+1,
\]
we get
\[
k(k-1)=b+n\le bn+1=2k.
\]
Thus \(k\le 3\). Since \(k\ge 2\), we only need to check \(k=2,3\).

- If \(k=2\), then \(b+n=2\) and \(bn=3\), impossible.
- If \(k=3\), then \(b+n=6\) and \(bn=5\), so \(\{b,n\}=\{1,5\}\). Since \(b\) is prime, \(b=5\). Then
\[
a=kb-1=3\cdot 5-1=14,
\]
which is not prime.

Therefore the only prime pair is

\[
\boxed{(7,3)}.
\]

Indeed,
\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

\[
\boxed{(7,3)}
\]

Proof:

\[
a^2-ab-b^3=1 \iff a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]

Since \(a>0\) and \(b^3+1>0\), we have \(a-b>0\), so \(a>b\).

Also, reducing the original equation modulo \(a\),

\[
-b^3\equiv 1 \pmod a,
\]

so

\[
a\mid b^3+1=(b+1)(b^2-b+1).
\]

Because \(a\) is prime, \(a\mid b+1\) or \(a\mid b^2-b+1\).

If \(a\mid b+1\), then since \(a>b\), we must have \(a=b+1\). The only consecutive primes are \(2\) and \(3\), so \((a,b)=(3,2)\), but

\[
3^2-3\cdot 2-2^3=9-6-8=-5\ne 1.
\]

Thus

\[
a\mid b^2-b+1.
\]

Write

\[
b^2-b+1=ac
\]

for some positive integer \(c\). Then

\[
b^3+1=(b+1)(b^2-b+1)=a(b+1)c.
\]

Comparing with \(a(a-b)=b^3+1\), we get

\[
a-b=c(b+1).
\]

Hence

\[
a=b+c(b+1),
\]

so modulo \(b\),

\[
a\equiv c \pmod b.
\]

Also,

\[
ac=b^2-b+1\equiv 1 \pmod b,
\]

so

\[
c^2\equiv ac\equiv 1 \pmod b.
\]

Thus

\[
b\mid c^2-1=(c-1)(c+1).
\]

But since \(a>b\),

\[
c=\frac{b^2-b+1}{a}<\frac{b^2-b+1}{b}=b-1+\frac1b<b,
\]

so \(1\le c\le b-1\). Therefore the only possibilities are

\[
c=1 \quad \text{or} \quad c=b-1.
\]

### Case 1: \(c=1\)

Then

\[
a-b=b+1 \implies a=2b+1.
\]

Also \(ac=b^2-b+1\) gives

\[
a=b^2-b+1.
\]

So

\[
2b+1=b^2-b+1 \implies b^2-3b=0 \implies b=3.
\]

Then

\[
a=2(3)+1=7.
\]

Thus \((a,b)=(7,3)\), and indeed

\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

### Case 2: \(c=b-1\)

Then

\[
a-b=(b-1)(b+1)=b^2-1,
\]

so

\[
a=b^2+b-1.
\]

Also

\[
(b-1)a=b^2-b+1.
\]

Substituting \(a=b^2+b-1\),

\[
(b-1)(b^2+b-1)=b^2-b+1.
\]

Expanding,

\[
b^3-2b+1=b^2-b+1,
\]

so

\[
b^3-b^2-b=0 \implies b(b^2-b-1)=0.
\]

No prime \(b\ge 2\) satisfies \(b^2-b-1=0\). Thus this case gives no solutions.

Therefore the only pair is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

\[
a^2-ab-b^3=1 \quad\Longleftrightarrow\quad a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]

Since \(a,b\) are primes, \(b\ge 2\). Also \(a(a-b)>0\), so \(a>b\).

First, \(a\nmid b+1\). Indeed, if \(a\mid b+1\), then because \(a>b\), we must have \(a=b+1\). Then \(a-b=1\), so
\[
a(a-b)=a=b+1,
\]
but the equation gives
\[
b+1=b^3+1,
\]
so \(b^3=b\), impossible for a prime \(b\).

Thus, since \(a\) is prime and \(a\mid (b+1)(b^2-b+1)\), we must have
\[
a\mid b^2-b+1.
\]
Write
\[
b^2-b+1=ka
\]
for some positive integer \(k\). Substituting into the original equation:
\[
a(a-b)=(b+1)ka,
\]
so dividing by \(a\),
\[
a-b=k(b+1).
\]
Hence
\[
a=b+k(b+1)=(k+1)b+k.
\]

Modulo \(b\), this gives
\[
a\equiv k \pmod b.
\]
Also, from \(ka=b^2-b+1\), reducing modulo \(b\),
\[
ka\equiv 1 \pmod b,
\]
so
\[
k^2\equiv 1 \pmod b.
\]
Thus
\[
b\mid k^2-1=(k-1)(k+1).
\]

Now \(a>b\) implies
\[
k=\frac{b^2-b+1}{a}<\frac{b^2-b+1}{b}=b-1+\frac1b<b.
\]
So \(1\le k\le b-1\). Since \(b\) is prime, the congruence \(k^2\equiv1\pmod b\) gives
\[
k\equiv \pm1 \pmod b.
\]
Because \(1\le k\le b-1\), the only possibilities are
\[
k=1 \quad\text{or}\quad k=b-1.
\]

### Case 1: \(k=1\)
Then
\[
a=b+b+1=2b+1.
\]
Also \(a=b^2-b+1\), so
\[
b^2-b+1=2b+1
\]
\[
b^2-3b=0.
\]
Since \(b\) is prime, \(b=3\). Then
\[
a=2(3)+1=7.
\]

### Case 2: \(k=b-1\)
Then
\[
a=b+(b-1)(b+1)=b^2+b-1.
\]
But also
\[
ka=b^2-b+1,
\]
so
\[
(b-1)(b^2+b-1)=b^2-b+1.
\]
Expanding the left side,
\[
b^3-2b+1=b^2-b+1,
\]
so
\[
b^3-b^2-b=0.
\]
Thus
\[
b(b^2-b-1)=0.
\]
Since \(b\ge2\), this would require \(b^2-b-1=0\), which has no integer solutions. Hence this case gives no solutions.

Finally, check \((a,b)=(7,3)\):
\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

Therefore the only pair is
\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

\[
\boxed{(a,b)=(7,3)}
\]

Proof:

\[
a^2-ab-b^3=1 \quad\Longrightarrow\quad a(a-b)=b^3+1.
\]

Since \(b^3+1>0\) and \(a>0\), we must have \(a>b\).

First check \(b=2\):
\[
a^2-2a-8=1 \implies a^2-2a-9=0,
\]
whose discriminant is \(4+36=40\), not a perfect square. So \(b\neq 2\). Hence \(b\) is odd, so \(b\ge 3\).

Modulo \(b\), the original equation gives
\[
a^2\equiv 1 \pmod b.
\]
Since \(b\) is prime,
\[
a\equiv \pm 1 \pmod b.
\]

Now from
\[
a(a-b)=b^3+1=(b+1)(b^2-b+1),
\]
the prime \(a\) divides \((b+1)(b^2-b+1)\). Since \(a>b\), \(a\) cannot divide \(b+1\): if \(a\mid b+1\), then \(a=b+1\), but \(b+1\) is even and greater than \(2\), hence not prime. Therefore
\[
a\mid b^2-b+1.
\]
Write
\[
b^2-b+1=ac
\]
for some positive integer \(c\). Then
\[
a(a-b)=b^3+1=(b+1)(b^2-b+1)=a(b+1)c,
\]
so
\[
a-b=(b+1)c.
\]
Thus
\[
a=b+(b+1)c=(c+1)b+c.
\]
Hence modulo \(b\),
\[
a\equiv c \pmod b.
\]
Since \(a^2\equiv 1\pmod b\), we get
\[
c^2\equiv 1\pmod b.
\]
Because \(b\) is prime,
\[
c\equiv 1 \text{ or } -1 \pmod b.
\]

Also,
\[
ac=b^2-b+1<b^2.
\]
But
\[
a=(c+1)b+c>(c+1)b,
\]
so
\[
ac>c(c+1)b.
\]
Therefore
\[
c(c+1)b<b^2,
\]
so
\[
c(c+1)<b.
\]
In particular \(0<c<b\). Since \(c\equiv \pm1\pmod b\), we must have \(c=1\) or \(c=b-1\). The second possibility is impossible because \(c=b-1\) would give \(c(c+1)=(b-1)b>b\), contradicting \(c(c+1)<b\). Hence
\[
c=1.
\]

So
\[
a=2b+1
\]
and also
\[
a=b^2-b+1.
\]
Equating gives
\[
2b+1=b^2-b+1
\]
\[
b^2-3b=0.
\]
Since \(b\ge 3\), we get
\[
b=3.
\]
Then
\[
a=2(3)+1=7.
\]

Finally,
\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

Thus the only pair of primes is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

\[
a^2-ab-b^3=1
\]

Rewrite as

\[
a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]

Let

\[
N=b^2-b+1.
\]

Since \(a(a-b)>0\) and \(a>0\), we have \(a>b\).

First, \(a\nmid b+1\). Indeed, if \(a\mid b+1\), then because \(a>b\), we must have \(a=b+1\). The only consecutive primes are \(2\) and \(3\), so \((a,b)=(3,2)\), but

\[
3^2-3\cdot 2-2^3=9-6-8=-5\neq 1.
\]

Thus \(a\nmid b+1\). Since \(a\) is prime and \(a\mid (b+1)N\), we get

\[
a\mid N.
\]

Write

\[
N=at
\]

for some positive integer \(t\). Then

\[
a(a-b)=(b+1)N=(b+1)at,
\]

so dividing by \(a\),

\[
a-b=(b+1)t.
\]

Hence

\[
a=b+(b+1)t.
\]

Also,

\[
N=at=t(b+(b+1)t).
\]

Reducing modulo \(b\),

\[
N=b^2-b+1\equiv 1 \pmod b,
\]

while

\[
t(b+(b+1)t)\equiv t^2 \pmod b.
\]

Therefore

\[
t^2\equiv 1 \pmod b.
\]

Since \(a>b\), we have

\[
t=\frac{N}{a}<\frac{N}{b}=b-1+\frac1b<b,
\]

so \(1\le t\le b-1\). Thus

\[
t=1 \quad \text{or} \quad t=b-1.
\]

If \(t=b-1\), then \(t\mid N\). But modulo \(t=b-1\), we have \(b\equiv 1\), so

\[
N=b^2-b+1\equiv 1 \pmod{t}.
\]

Thus \(t\mid 1\), forcing \(t=1\) and \(b=2\). But then \(a=b+(b+1)t=5\), while \(N=3\) gives \(a=3\), contradiction. Hence \(t\neq b-1\), so

\[
t=1.
\]

Therefore

\[
a=N=b^2-b+1,
\]

and from \(a-b=(b+1)t=b+1\),

\[
a=b+b+1=2b+1.
\]

So

\[
b^2-b+1=2b+1,
\]

hence

\[
b^2-3b=0.
\]

Since \(b\) is prime, \(b=3\). Then

\[
a=2(3)+1=7.
\]

Check:

\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

Thus the only pair is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

\[
a^2-ab-b^3=1 \quad\Longrightarrow\quad a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]

Since \(a>0\) and \(b^3+1>0\), we have \(a-b>0\), so \(a>b\).

Modulo \(a\),
\[
a\mid b^3+1=(b+1)(b^2-b+1).
\]

First, \(a\nmid b+1\). Indeed, if \(a\mid b+1\), then because \(a>b\), we must have \(a=b+1\), so \(a-b=1\). But then
\[
a(a-b)=a=b^3+1,
\]
while \(a=b+1\), giving \(b+1=b^3+1\), i.e. \(b^3=b\), impossible for a prime \(b\). Hence
\[
a\mid b^2-b+1.
\]

Write
\[
b^2-b+1=am
\]
for some positive integer \(m\). Then
\[
a(a-b)=(b+1)(b^2-b+1)=a m(b+1),
\]
so
\[
a-b=m(b+1).
\]
Thus
\[
a=(m+1)b+m. \tag{1}
\]
Also \(am=b^2-b+1\). Since \(a>b\), we have
\[
m=\frac{b^2-b+1}{a}<\frac{b^2-b+1}{b}<b,
\]
so \(1\le m\le b-1\).

Reducing \(am=b^2-b+1\) modulo \(b\), and using \(a=(m+1)b+m\), gives
\[
m^2\equiv 1 \pmod b.
\]
Hence
\[
b\mid (m-1)(m+1).
\]
Because \(b\) is prime and \(1\le m\le b-1\), either
\[
m=1 \quad\text{or}\quad m=b-1.
\]

### Case 1: \(m=1\)
Then \(a=(m+1)b+m=2b+1\), and also \(a=b^2-b+1\). Therefore
\[
2b+1=b^2-b+1
\]
so
\[
b^2-3b=0.
\]
Since \(b\) is prime, \(b=3\), and then \(a=7\).

### Case 2: \(m=b-1\)
Then
\[
a=(m+1)b+m=b^2+b-1.
\]
But \(am=b^2-b+1\) gives
\[
(b^2+b-1)(b-1)=b^2-b+1.
\]
Expanding,
\[
b^3-2b+1=b^2-b+1,
\]
so
\[
b^3-b^2-b=0
\]
or
\[
b(b^2-b-1)=0,
\]
which is impossible for a prime \(b\ge2\).

Thus the only possible pair is \((a,b)=(7,3)\). Verification:
\[
7^2-7\cdot3-3^3=49-21-27=1.
\]

\[
\boxed{(7,3)}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

\[
a^2-ab-b^3=1 \quad\Longrightarrow\quad a(a-b)=b^3+1>0.
\]
Since \(a>0\), we get \(a>b\).

If \(b=2\), then
\[
a(a-2)=9.
\]
Since \(a\) is prime, \(a=3\), but \(3(1)\neq 9\). Hence \(b\neq 2\), so \(b\) is odd, and therefore \(a\) is also odd.

Reducing the original equation modulo \(b\),
\[
a^2\equiv 1 \pmod b.
\]
Because \(b\) is prime,
\[
a\equiv \pm 1 \pmod b.
\]
Since \(a>b\) and both are odd, we may write
\[
a=2kb\pm 1
\]
for some integer \(k\ge 1\).

### Case 1: \(a=2kb+1\)

Then
\[
a-b=(2k-1)b+1.
\]
Thus
\[
a(a-b)=(2kb+1)((2k-1)b+1)=b^3+1.
\]
Expanding and simplifying gives
\[
b^2=2k(2k-1)b+4k-1.
\]
Let
\[
A=k(2k-1).
\]
Then
\[
b^2-2Ab-(4k-1)=0,
\]
so
\[
(b-A)^2=A^2+4k-1.
\]
Put \(c=b-A>0\). Then
\[
c^2-A^2=4k-1,
\]
hence
\[
(c-A)(c+A)=4k-1.
\]
Since \(c>A\), write \(d=c-A\ge 1\). Then
\[
4k-1=d(d+2A)\ge 1+2A.
\]
But for \(k\ge 2\),
\[
1+2A=1+2k(2k-1)>4k-1,
\]
a contradiction. Therefore \(k=1\). Then
\[
b^2-2b-3=0,
\]
so \(b=3\), and hence
\[
a=2(1)(3)+1=7.
\]

### Case 2: \(a=2kb-1\)

Then
\[
a-b=(2k-1)b-1,
\]
so
\[
(2kb-1)((2k-1)b-1)=b^3+1.
\]
Expanding and simplifying gives
\[
b^2=2k(2k-1)b-(4k-1).
\]
Thus
\[
(b-A)^2=A^2-(4k-1),
\]
where \(A=k(2k-1)\). For \(k=1\), the right-hand side is negative, impossible. For \(k\ge 2\), let
\[
c=|b-A|.
\]
Then
\[
c^2=A^2-(4k-1),
\]
so \(c<A\). Let \(d=A-c\ge 1\). Then
\[
4k-1=A^2-c^2=d(2A-d).
\]
But for \(1\le d\le A\),
\[
d(2A-d)\ge 2A-1.
\]
Yet
\[
2A-1=2k(2k-1)-1>4k-1
\]
for all \(k\ge 2\), contradiction. Thus Case 2 gives no solutions.

Finally, checking \((a,b)=(7,3)\):
\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

Therefore the only pair is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

\[
a^2-ab-b^3=1 \implies a(a-b)=b^3+1=(b+1)(b^2-b+1). \tag{1}
\]

Since the right-hand side is positive and \(a>0\), we must have \(a>b\).

### 1. Exclude \(b=2\)
If \(b=2\), then
\[
a(a-2)=2^3+1=9.
\]
Since \(a\) is prime, \(a\mid 9\), so \(a=3\). But then \(a(a-2)=3\ne 9\), contradiction. Thus \(b\neq 2\).

### 2. Assume \(b>2\)
Then \(b\) is odd, so \(b+1\) is an even integer greater than \(2\), hence composite. Since \(a>b\) and \(a\) is prime, we cannot have \(a=b+1\); therefore
\[
a>b+1.
\]
From (1), \(a\) is prime and divides \((b+1)(b^2-b+1)\). But \(a>b+1\), so \(a\nmid b+1\). Hence
\[
a\mid b^2-b+1.
\]
Write
\[
b^2-b+1=ac
\]
for some positive integer \(c\). Substituting into (1):
\[
a(a-b)=(b+1)ac,
\]
so, dividing by \(a\),
\[
a-b=c(b+1).
\]
Thus
\[
a=b+c(b+1).
\]
Now substitute this into \(b^2-b+1=ac\):
\[
c\bigl(b+c(b+1)\bigr)=b^2-b+1.
\]
Expanding and rearranging gives
\[
b^2-(c^2+c+1)b+(1-c^2)=0. \tag{2}
\]

### 3. Determine \(c\)
Let
\[
S=c^2+c+1.
\]
Then (2) is
\[
b^2-Sb+1-c^2=0.
\]
If \(c=1\), then
\[
b^2-3b=0,
\]
so \(b=0\) or \(b=3\). Since \(b\) is prime, \(b=3\). Then
\[
a=b+c(b+1)=3+1\cdot 4=7.
\]

Now suppose \(c\ge 2\). For (2) to have an integer root \(b\), its discriminant must be a perfect square:
\[
D=S^2-4(1-c^2)=S^2+4c^2-4.
\]
Let \(D=n^2\). Since \(S\) is odd, \(D\) is odd, so \(n\) is odd. Also \(D>S^2\), so \(n>S\). Write \(n-S=2t\) with \(t\ge 1\). Then
\[
n^2-S^2=4t(S+t).
\]
But
\[
n^2-S^2=4c^2-4=4(c^2-1),
\]
so
\[
t(S+t)=c^2-1.
\]
However,
\[
S+t\ge S+1=c^2+c+2>c^2-1,
\]
which is impossible because \(t\ge 1\). Therefore \(c\ge 2\) is impossible.

Thus \(c=1\), giving
\[
b=3,\qquad a=7.
\]

### 4. Verification
\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

Hence the only pair is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

\[
\boxed{(7,3)}
\]

Proof:

\[
a^2-ab-b^3=1 \implies a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]

Since \(a>0\) and \(b^3+1>0\), we have \(a>b\).

Also \(a\mid (b+1)(b^2-b+1)\), so by Euclid’s lemma,
\[
a\mid b+1 \quad \text{or} \quad a\mid b^2-b+1.
\]

### 1. Excluding \(a\mid b+1\)

If \(a\mid b+1\), then \(b+1=ma\) for some positive integer \(m\). Since \(a>b\), we have \(a\ge b+1\), so
\[
b+1=ma\ge a\ge b+1.
\]
Thus \(m=1\) and \(a=b+1\).  
If \(b>2\), then \(b+1\) is even and greater than \(2\), so it cannot be prime.  
If \(b=2\), then \(a=3\), but
\[
3^2-3\cdot 2-2^3=9-6-8=-5\ne 1.
\]
So \(a\nmid b+1\). Therefore
\[
a\mid b^2-b+1.
\]

### 2. Solving with \(a\mid b^2-b+1\)

Write
\[
b^2-b+1=ka
\]
for some positive integer \(k\). Then
\[
a(a-b)=(b+1)(b^2-b+1)=(b+1)ka.
\]
Dividing by \(a>0\),
\[
a-b=k(b+1).
\]
Hence
\[
a=b+k(b+1),
\]
so
\[
a\equiv k \pmod b.
\]

From the original equation modulo \(b\),
\[
a^2\equiv 1 \pmod b.
\]
Thus
\[
k^2\equiv 1 \pmod b.
\]

Now since \(a>b\),
\[
k=\frac{b^2-b+1}{a}<\frac{b^2-b+1}{b}=b-1+\frac1b<b.
\]
So \(1\le k\le b-1\). Therefore
\[
b\mid (k-1)(k+1).
\]
Because \(b\) is prime, \(b\mid k-1\) or \(b\mid k+1\). With \(1\le k\le b-1\), this gives
\[
k=1 \quad \text{or} \quad k=b-1.
\]

#### Case \(k=1\)

Then
\[
a=b^2-b+1
\]
and also
\[
a=b+(b+1)=2b+1.
\]
So
\[
b^2-b+1=2b+1
\]
\[
b^2-3b=0.
\]
Since \(b\) is prime, \(b=3\). Then
\[
a=2\cdot 3+1=7.
\]

#### Case \(k=b-1\)

Then
\[
(b-1)a=b^2-b+1=b(b-1)+1,
\]
so
\[
(b-1)(a-b)=1.
\]
Thus \(b-1=1\) and \(a-b=1\), giving \(b=2\), \(a=3\). But
\[
3^2-3\cdot2-2^3=-5\ne 1,
\]
so this is impossible.

Finally, check:
\[
7^2-7\cdot 3-3^3=49-21-27=1.
\]

Therefore the only pair is

\[
\boxed{(7,3)}.
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

\[
a^2-ab-b^3=1 \quad\Longleftrightarrow\quad a(a-b)=b^3+1=(b+1)(b^2-b+1).
\]

Since the right-hand side is positive and \(a>0\), we have \(a>b\). In particular \(b\ge2\).

First, \(a\nmid b+1\). Indeed, if \(a\mid b+1\), then because \(a>b\ge2\), we have \(b+1<2a\), so \(b+1=a\). Thus \(a=b+1\), which forces \(b=2,\ a=3\), but \((a,b)=(3,2)\) does not satisfy the equation:
\[
3^2-3\cdot2-2^3=9-6-8=-5\ne1.
\]
So \(a\nmid b+1\).

Because \(a\) is prime and
\[
a\mid (b+1)(b^2-b+1),
\]
we must have
\[
a\mid b^2-b+1.
\]
Write
\[
b^2-b+1=ac
\]
for some positive integer \(c\). Then
\[
a(a-b)=(b+1)(b^2-b+1)=ac(b+1),
\]
so dividing by \(a\),
\[
a-b=c(b+1).
\]
Hence
\[
a=(c+1)b+c.
\]
Substituting into \(ac=b^2-b+1\),
\[
c\big((c+1)b+c\big)=b^2-b+1.
\]
Expanding and rearranging gives
\[
b^2-(c^2+c+1)b=c^2-1. \tag{1}
\]

If \(c=1\), then
\[
b^2-3b=0,
\]
so \(b=3\). Then
\[
a=(1+1)3+1=7.
\]

If \(c\ge2\), then \(c^2-1>0\), so from (1),
\[
b>c^2+c+1.
\]
Thus \(b\mid c^2-1\), but \(0<c^2-1<b\), impossible. Therefore \(c=1\).

So the only candidate is \((a,b)=(7,3)\). Checking:
\[
7^2-7\cdot3-3^3=49-21-27=1.
\]

Hence the unique pair is

\[
\boxed{(7,3)}.
\]

</details>
