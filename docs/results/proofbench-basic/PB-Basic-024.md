# PB-Basic-024

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Find all non-negative integers $a,b,c$ such that $20^{a}+b^{4}=2024^{c}$

## Swarm: accepted (best candidate `P1`; self-verification grades [7, 7, 7]; 409,912 tokens in 52 calls)

**Blind grade: Correct (7/7).** Solves c=0 to get (0,0,0), and for c>=1 divides by (3^a)^2 mod 11 to make -1 a quadratic residue mod 11, a contradiction, giving a complete and rigorous proof.

\[
20^a+b^4=2024^c,\qquad a,b,c\in \mathbb Z_{\ge 0}.
\]

First consider \(c=0\). Then \(2024^0=1\), so

\[
20^a+b^4=1.
\]

Since \(20^a\ge 1\), we must have \(a=0\) and then \(b^4=0\), hence \(b=0\). Thus

\[
(a,b,c)=(0,0,0)
\]

is one solution.

Now suppose \(c\ge 1\). Since

\[
2024=11\cdot 184,
\]

we have \(2024^c\equiv 0\pmod{11}\). Reducing the original equation modulo \(11\),

\[
20^a+b^4\equiv 0\pmod{11}.
\]

But \(20\equiv 9\equiv 3^2\pmod{11}\), so

\[
20^a\equiv (3^a)^2\pmod{11}.
\]

Thus

\[
(b^2)^2\equiv -(3^a)^2\pmod{11}.
\]

Because \(3^a\not\equiv 0\pmod{11}\), we may multiply by the inverse of \((3^a)^2\) modulo \(11\), obtaining

\[
\left((b^2)(3^a)^{-1}\right)^2\equiv -1\pmod{11}.
\]

So \(-1\) would be a quadratic residue modulo \(11\). But the nonzero quadratic residues modulo \(11\) are

\[
1,3,4,5,9,
\]

and

\[
-1\equiv 10\pmod{11}
\]

is not among them. Contradiction.

Therefore \(c\ge 1\) is impossible. Hence the only solution is

\[
\boxed{(a,b,c)=(0,0,0)}.
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 26,856 | Correct (7/7) | Complete: writing 20^a = (3^a)^2 (mod 11), x^2+y^2 = 0 (mod 11) with x nonzero forces either -1 to be a square mod 11 or x = 0, both impossible, so c>=1 is excluded, and c=0 gives a=b=0. |
| A2 | stop | 10,340 | Correct (7/7) | Handles c=0 to get (0,0,0), and for c>=1 shows -20^a is a non-residue mod 11 (since 20 = 3^2 and negatives of residues are non-residues) while b^4 is a square, a complete proof. |
| A3 | stop | 9,336 | Correct (7/7) | Explicit (correct) tables of fourth powers and powers of 9 mod 11 show -9^a is never a fourth-power residue, excluding c>=1, and the c=0 case correctly yields only (0,0,0). |
| A4 | stop | 13,818 | Correct (7/7) | Complete mod-11 argument: 20 = 9 = 3^2 (mod 11) makes 20^a a nonzero quadratic residue, so b^4 = -20^a would make -20^a a residue although -1 is a non-residue for 11 = 3 (mod 4), ruling out c>=1, and c=0 correctly forces a=b=0. |
| A5 | stop | 14,141 | Correct (7/7) | Complete: 20 = 3^2 (mod 11) makes -20^a a nonzero non-residue because -1 is not a square mod 11, so it cannot equal the square b^4, ruling out c>=1, and c=0 forces a=b=0. |
| A6 | stop | 12,860 | Correct (7/7) | Computes 20^a mod 11 in {1,3,4,5,9} and fourth powers mod 11 in {0,1,3,4,5,9} (both correct), so b^4 = -20^a is impossible for c>=1, and correctly derives a=b=0 when c=0. |
| A7 | stop | 18,335 | Correct (7/7) | For c>=1 it reduces mod 11 and uses 20 = 3^2 (mod 11) to show b^4 = -20^a would make -1 a quadratic residue mod 11, which it is not, then correctly solves c=0 to get the unique solution (0,0,0) with verification. |
| A8 | stop | 11,760 | Correct (7/7) | Complete: for c>=1, -20^a mod 11 lies in {10,2,7,8,6} and fourth powers mod 11 lie in {0,1,3,4,5,9} (both computations check out), which is a contradiction, and c=0 forces a=b=0. |
| A9 | stop | 13,991 | Correct (7/7) | Valid mod 11 argument: 20^a is a nonzero square since 20 = 3^2 (mod 11), so -20^a is a non-residue while b^4 is a square, ruling out c>=1, and c=0 forces a=b=0; the only flaw is a harmless '=' written for a congruence. |
| A10 | stop | 13,316 | Correct (7/7) | Complete: for c>=1, b^4 = -3^(2a) (mod 11) would make -1 a quadratic residue mod 11, contradicting the explicit list {1,3,4,5,9}, and c=0 correctly forces a=b=0. |
| A11 | stop | 17,038 | Correct (7/7) | Proves the lemma that x^2+y^2 = 0 (mod 11) forces 11 \| x and 11 \| y, applies it to x=3^a, y=b^2 to exclude c>=1, then handles c=0 correctly and verifies (0,0,0). |
| A12 | stop | 12,441 | Correct (7/7) | Complete and verified: for c>=1 the residues of -20^a mod 11 cycle through {10,2,7,8,6} while fourth powers mod 11 lie in {0,1,3,4,5,9}, so the sets are disjoint, and c=0 correctly forces a=b=0. |
| A13 | stop | 12,950 | Correct (7/7) | Valid mod 11 argument: 20^a is a nonzero quadratic residue and -1 is not, so -20^a cannot equal the square b^4, excluding c>=1, and c=0 forces a=b=0 with the solution verified. |
| A14 | stop | 6,739 | Correct (7/7) | Rewrites the mod 11 equation as (3^a)^2+(b^2)^2 = 0 and uses that -1 is a non-residue mod 11 to force 11 \| 3^a, a contradiction, then correctly solves c=0, giving a complete and rigorous proof. |
| A15 | stop | 25,809 | Correct (7/7) | Correct but roundabout: mod 8, 5 and 3 checks (all valid, despite a harmless typo) show a and c are even, then reducing X^2+Y^2=Z^2 to coprime A,B with 11\|C would make -1 a square mod 11, which a Fermat argument rules out; c=0 gives (0,0,0). |
| A16 | stop | 16,955 | Correct (7/7) | Correct but roundabout: a=0 is excluded by mod 4, then for a>=1 mod 5 gives c even and mod 3 gives a even, and (b^2/20^m)^2 = -1 (mod 11) is impossible; every step is valid. |

<details><summary>A1: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof:

First, \(20^0+b^4=2024^0\) gives
\[
1+b^4=1 \implies b=0,
\]
so \((0,0,0)\) is a solution.

Now suppose \(c\ge 1\). Since
\[
2024=11\cdot 184,
\]
we have
\[
2024^c\equiv 0 \pmod{11}.
\]
Also
\[
20\equiv 9\equiv 3^2 \pmod{11},
\]
so
\[
20^a\equiv (3^a)^2 \pmod{11}.
\]
Thus the original equation modulo \(11\) becomes
\[
(3^a)^2+(b^2)^2\equiv 0 \pmod{11}.
\]
Let \(x=3^a\) and \(y=b^2\). Then
\[
x^2+y^2\equiv 0 \pmod{11}.
\]
Now \(x\not\equiv 0\pmod{11}\), since \(3^a\not\equiv 0\pmod{11}\).

If \(y\not\equiv 0\pmod{11}\), then
\[
\left(\frac{x}{y}\right)^2\equiv -1 \pmod{11},
\]
which is impossible because \(-1\) is not a quadratic residue modulo \(11\): the nonzero squares modulo \(11\) are
\[
\{1,3,4,5,9\},
\]
and \(-1\equiv 10\) is not among them.

Therefore \(y\equiv 0\pmod{11}\), so \(x^2\equiv 0\pmod{11}\), hence \(x\equiv 0\pmod{11}\), contradiction. Thus no solutions exist with \(c\ge 1\).

Hence \(c=0\), and then
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), we must have \(a=0\) and \(b=0\).

Therefore the only solution is
\[
\boxed{(0,0,0)}.
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof:

First, note that \(2024=11\cdot 184\), so \(2024\equiv 0 \pmod{11}\).

### Case 1: \(c=0\)

Then
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), equality is possible only when
\[
20^a=1,\qquad b^4=0.
\]
Thus \(a=0\) and \(b=0\). Hence
\[
(a,b,c)=(0,0,0)
\]
is a solution, and indeed
\[
20^0+0^4=1=2024^0.
\]

### Case 2: \(c\ge 1\)

Reducing modulo \(11\), since \(2024^c\equiv 0\pmod{11}\), we get
\[
20^a+b^4\equiv 0 \pmod{11},
\]
so
\[
b^4\equiv -20^a \pmod{11}.
\]

Now
\[
20\equiv 9=3^2 \pmod{11},
\]
so
\[
20^a\equiv (3^a)^2 \pmod{11}
\]
is a nonzero square modulo \(11\). The nonzero quadratic residues modulo \(11\) are
\[
\{1,3,4,5,9\}.
\]
Their negatives are
\[
\{10,8,7,6,2\}=\{2,6,7,8,10\},
\]
none of which are quadratic residues modulo \(11\). Therefore \(-20^a\) is not a square modulo \(11\).

But
\[
b^4=(b^2)^2
\]
is always a square modulo \(11\). Hence
\[
b^4\equiv -20^a \pmod{11}
\]
is impossible. Therefore \(c\ge 1\) cannot occur.

Combining both cases, the only solution is

\[
\boxed{(0,0,0)}.
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

\[
20^a+b^4=2024^c
\]

First note that \(a=b=c=0\) works:
\[
20^0+0^4=1=2024^0.
\]

Now suppose \(c\ge 1\). Reducing modulo \(11\), we have
\[
20\equiv 9 \pmod{11},\qquad 2024\equiv 0 \pmod{11}.
\]
Thus
\[
9^a+b^4\equiv 0 \pmod{11},
\]
so
\[
b^4\equiv -9^a \pmod{11}.
\]

We compute the fourth-power residues modulo \(11\):
\[
x^4\bmod 11\in \{0,1,3,4,5,9\}.
\]
Indeed, for \(x=0,1,\dots,10\),
\[
0^4,1^4,2^4,\dots,10^4 \equiv 0,1,5,4,3,9,9,3,4,5,1 \pmod{11}.
\]

Now compute powers of \(9\) modulo \(11\):
\[
9^0\equiv 1,\quad 9^1\equiv 9,\quad 9^2\equiv 4,\quad 9^3\equiv 3,\quad 9^4\equiv 5,\quad 9^5\equiv 1 \pmod{11}.
\]
So \(-9^a\pmod{11}\) can only be one of
\[
-1,-9,-4,-3,-5 \equiv 10,2,7,8,6 \pmod{11}.
\]
None of these residues belongs to \(\{0,1,3,4,5,9\}\), the possible fourth-power residues modulo \(11\). Contradiction.

Therefore \(c\ge 1\) is impossible, so \(c=0\). Then
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), equality forces
\[
20^a=1,\qquad b^4=0,
\]
so \(a=0\) and \(b=0\).

Hence the only solution is

\[
\boxed{(a,b,c)=(0,0,0)}.
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof:

If \(c=0\), then
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), we must have \(a=0\) and \(b=0\). Thus \((0,0,0)\) is a solution.

Now suppose \(c\ge 1\). Since
\[
2024=11\cdot 184,
\]
we have
\[
2024^c\equiv 0 \pmod{11}.
\]
Thus
\[
20^a+b^4\equiv 0 \pmod{11}.
\]
But \(20\equiv 9\pmod{11}\), so
\[
9^a+b^4\equiv 0 \pmod{11}.
\]

If \(11\mid b\), then \(b^4\equiv 0\pmod{11}\), forcing \(9^a\equiv 0\pmod{11}\), impossible since \(9\) is invertible modulo \(11\). Hence \(11\nmid b\).

Now \(b^4=(b^2)^2\) is a nonzero quadratic residue modulo \(11\). Also
\[
9^a=(3^a)^2
\]
is a quadratic residue modulo \(11\). The congruence
\[
b^4\equiv -9^a \pmod{11}
\]
therefore says that \(-9^a\) is a quadratic residue modulo \(11\).

But \(-1\) is a quadratic nonresidue modulo \(11\), because \(11\equiv 3\pmod 4\). Since \(9^a\) is a quadratic residue, \(-9^a\) must be a nonresidue. Contradiction.

Therefore no solutions exist with \(c\ge 1\).

Hence the only solution is
\[
\boxed{(a,b,c)=(0,0,0)}.
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

\[
20^a+b^4=2024^c
\]

First note that
\[
2024=11\cdot 184,
\]
so \(2024\equiv 0\pmod{11}\).

### Case 1: \(c\ge 1\)

Reduce modulo \(11\):
\[
20^a+b^4\equiv 0\pmod{11},
\]
so
\[
b^4\equiv -20^a\pmod{11}.
\]

Now compute residues modulo \(11\). The squares modulo \(11\) are
\[
0,1,3,4,5,9.
\]
In particular, \(-1\equiv 10\pmod{11}\) is not a square modulo \(11\). Also,
\[
20\equiv 9\equiv 3^2\pmod{11},
\]
so
\[
20^a\equiv (3^a)^2\pmod{11}
\]
is a quadratic residue modulo \(11\). Therefore \(-20^a\) is a non-residue modulo \(11\).

But \(b^4=(b^2)^2\) is always a quadratic residue modulo \(11\), or \(0\). Since \(-20^a\not\equiv 0\pmod{11}\), \(b^4\equiv -20^a\) would force a non-residue to equal a residue, impossible. Hence \(c\ge 1\) is impossible.

### Case 2: \(c=0\)

Then
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), we must have
\[
20^a=1,\qquad b^4=0.
\]
Thus \(a=0\) and \(b=0\).

Checking:
\[
20^0+0^4=1+0=1=2024^0.
\]

Therefore the only solution is

\[
\boxed{(a,b,c)=(0,0,0)}.
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof:

Suppose first that \(c\ge 1\). Since
\[
2024=11\cdot 184,
\]
we have
\[
2024^c\equiv 0 \pmod{11}.
\]
Thus
\[
20^a+b^4\equiv 0 \pmod{11},
\]
so
\[
b^4\equiv -20^a \pmod{11}.
\]

Now
\[
20\equiv 9 \pmod{11},
\]
and the powers of \(9\) modulo \(11\) are
\[
9^0=1,\quad 9^1=9,\quad 9^2=4,\quad 9^3=3,\quad 9^4=5,\quad 9^5=1.
\]
Hence
\[
20^a\equiv 1,3,4,5,9 \pmod{11}.
\]
Therefore
\[
-20^a\equiv 10,8,7,6,2 \pmod{11}.
\]

But a direct check modulo \(11\) shows that every fourth power is congruent to one of
\[
0,1,3,4,5,9 \pmod{11}.
\]
The numbers
\[
10,8,7,6,2
\]
are not among these residues. Hence \(b^4\equiv -20^a\pmod{11}\) is impossible for \(c\ge 1\).

So necessarily
\[
c=0.
\]
Then the equation becomes
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), equality forces
\[
20^a=1,\qquad b^4=0.
\]
Thus \(a=0\) and \(b=0\).

Finally,
\[
20^0+0^4=1+0=1=2024^0,
\]
so \((0,0,0)\) indeed works.

\[
\boxed{(a,b,c)=(0,0,0)}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof:

Suppose first that \(c\ge 1\). Since  
\[
2024=11\cdot 184,
\]
we have \(2024\equiv 0\pmod{11}\). Reducing the equation modulo \(11\),
\[
20^a+b^4\equiv 0\pmod{11},
\]
so
\[
b^4\equiv -20^a\pmod{11}.
\]

Now \(20\equiv 9\equiv 3^2\pmod{11}\), hence
\[
20^a\equiv (3^a)^2\pmod{11}.
\]
Also \(b^4=(b^2)^2\). Multiplying
\[
b^4\equiv -20^a\pmod{11}
\]
by the inverse of \(20^a\), which is invertible modulo \(11\), gives
\[
-1\equiv b^4(20^a)^{-1}
\equiv (b^2)^2(3^a)^{-2}
\equiv \bigl(b^2(3^a)^{-1}\bigr)^2\pmod{11}.
\]
Thus \(-1\) would be a quadratic residue modulo \(11\). But the nonzero quadratic residues modulo \(11\) are
\[
1,3,4,5,9,
\]
and \(-1\equiv 10\pmod{11}\) is not among them. Contradiction.

Therefore \(c\ge 1\) is impossible, so
\[
c=0.
\]

Then the equation becomes
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), we must have
\[
20^a=1,\qquad b^4=0.
\]
Thus \(a=0\) and \(b=0\).

Finally,
\[
20^0+0^4=1=2024^0,
\]
so the triple \((0,0,0)\) indeed works.

Hence the only solution is

\[
\boxed{(0,0,0)}.
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

\[
20^a+b^4=2024^c
\]

First note that \(2024=11\cdot 184\), so for \(c\ge 1\),

\[
2024^c\equiv 0 \pmod{11}.
\]

Thus, if \(c\ge 1\), reducing modulo \(11\) gives

\[
20^a+b^4\equiv 0 \pmod{11},
\qquad\text{so}\qquad
b^4\equiv -20^a \pmod{11}.
\]

Now compute fourth powers modulo \(11\). A direct check gives

\[
x^4\bmod 11\in \{0,1,3,4,5,9\}\qquad (x\in\mathbb Z).
\]

But \(20\equiv 9\pmod{11}\), and \(9^5\equiv 1\pmod{11}\), so the residues of \(-20^a\pmod{11}\) cycle through

\[
-1,\,-9,\,-4,\,-3,\,-5
\equiv 10,2,7,8,6 \pmod{11},
\]

none of which are in \(\{0,1,3,4,5,9\}\). Hence \(b^4\equiv -20^a\pmod{11}\) is impossible when \(c\ge 1\). Therefore \(c=0\).

If \(c=0\), then

\[
20^a+b^4=1.
\]

Since \(20^a\ge 1\) and \(b^4\ge 0\), equality forces

\[
20^a=1,\qquad b^4=0,
\]

so \(a=0\) and \(b=0\). This indeed works:

\[
20^0+0^4=1=2024^0.
\]

Therefore the only solution is

\[
\boxed{(a,b,c)=(0,0,0)}.
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof:

Suppose first that \(c\ge 1\). Since
\[
2024=11\cdot 184,
\]
we have \(2024^c\equiv 0\pmod{11}\). Reducing the equation modulo \(11\),
\[
20^a+b^4\equiv 0\pmod{11},
\]
so
\[
b^4\equiv -20^a\pmod{11}.
\]

Now \(20\equiv 9\equiv 3^2\pmod{11}\), hence
\[
20^a=(3^a)^2
\]
is a nonzero square modulo \(11\). Therefore \(-20^a=-1\cdot 20^a\) would be a square if and only if \(-1\) were a square modulo \(11\). But the quadratic residues modulo \(11\) are
\[
0,1,3,4,5,9,
\]
so \(-1\equiv 10\pmod{11}\) is not a square. Thus \(-20^a\) is not a square modulo \(11\).

On the other hand,
\[
b^4=(b^2)^2
\]
is a square modulo \(11\), contradiction. Hence \(c\ge 1\) is impossible, so \(c=0\).

Then
\[
20^a+b^4=2024^0=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), we must have
\[
20^a=1,\qquad b^4=0.
\]
Thus \(a=0\) and \(b=0\).

Finally,
\[
20^0+0^4=1=2024^0,
\]
so the triple \((0,0,0)\) indeed works.

\[
\boxed{(0,0,0)}
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

\[
20^a+b^4=2024^c
\]

First note that \(2024=11\cdot 184\), so \(2024\equiv 0\pmod{11}\).

### Case 1: \(c=0\)
Then
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), we must have \(20^a=1\), so \(a=0\), and then \(b^4=0\), so \(b=0\). Thus
\[
(a,b,c)=(0,0,0)
\]
works:
\[
20^0+0^4=1=2024^0.
\]

### Case 2: \(c\ge 1\)
Reduce modulo \(11\). Since \(2024\equiv 0\pmod{11}\),
\[
20^a+b^4\equiv 0\pmod{11},
\]
so
\[
b^4\equiv -20^a\pmod{11}.
\]

Now \(20\equiv 9\equiv 3^2\pmod{11}\). Hence
\[
-20^a\equiv -3^{2a}\pmod{11}.
\]
But \(b^4=(b^2)^2\) is a square modulo \(11\), so \(-3^{2a}\) would be a square modulo \(11\). If
\[
x^2\equiv -3^{2a}\pmod{11},
\]
then multiplying by \(3^{-2a}\) gives
\[
(x3^{-a})^2\equiv -1\pmod{11}.
\]
So \(-1\equiv 10\) would be a quadratic residue modulo \(11\).

But the nonzero quadratic residues modulo \(11\) are
\[
1^2,2^2,3^2,4^2,5^2 \equiv 1,4,9,5,3 \pmod{11},
\]
so the set of nonzero squares is \(\{1,3,4,5,9\}\), which does not contain \(10\equiv -1\). Contradiction.

Therefore \(c\ge 1\) is impossible.

Hence the only solution is

\[
\boxed{(a,b,c)=(0,0,0)}.
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof:

Since
\[
2024=11\cdot 184,
\]
we have
\[
2024\equiv 0 \pmod{11}.
\]

### Case 1: \(c\ge 1\)

Then modulo \(11\),
\[
20^a+b^4\equiv 2024^c\equiv 0\pmod{11}.
\]

Now \(20\equiv 9\equiv 3^2\pmod{11}\), so
\[
20^a\equiv (3^a)^2\pmod{11}.
\]
Also,
\[
b^4=(b^2)^2.
\]
Thus
\[
(3^a)^2+(b^2)^2\equiv 0\pmod{11}.
\]

We use the standard fact that for \(p=11\equiv 3\pmod 4\), the congruence
\[
x^2+y^2\equiv 0\pmod{11}
\]
forces
\[
x\equiv y\equiv 0\pmod{11}.
\]
Indeed, if \(y\not\equiv0\pmod{11}\), then
\[
\left(\frac{x}{y}\right)^2\equiv -1\pmod{11},
\]
which is impossible because \(-1\) is not a quadratic residue modulo \(11\). Hence \(y\equiv0\pmod{11}\), and then \(x\equiv0\pmod{11}\).

Applying this to \(x=3^a\) and \(y=b^2\), we get
\[
11\mid 3^a,
\]
which is impossible since \(3^a\) is never divisible by \(11\). Therefore \(c\ge 1\) is impossible.

### Case 2: \(c=0\)

Then
\[
20^a+b^4=2024^0=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), we must have
\[
20^a=1,\qquad b^4=0.
\]
Thus
\[
a=0,\qquad b=0.
\]

So the only solution is
\[
\boxed{(0,0,0)}.
\]

Verification:
\[
20^0+0^4=1+0=1=2024^0.
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

\[
20^a+b^4=2024^c
\]

First note that
\[
2024=11\cdot 184,
\]
so \(2024\equiv 0\pmod{11}\).

Assume \(c\ge 1\). Then modulo \(11\),
\[
20^a+b^4\equiv 0\pmod{11},
\]
so
\[
b^4\equiv -20^a\pmod{11}.
\]

Now \(20\equiv 9\equiv -2\pmod{11}\). Computing powers of \(20\) modulo \(11\):
\[
20^0\equiv 1,\quad
20^1\equiv 9,\quad
20^2\equiv 4,\quad
20^3\equiv 3,\quad
20^4\equiv 5,\quad
20^5\equiv 1 \pmod{11}.
\]
Thus the residues \(-20^a\pmod{11}\) cycle through
\[
10,2,7,8,6.
\]

On the other hand, for any integer \(x\), the fourth powers modulo \(11\) are
\[
x^4\in \{0,1,3,4,5,9\}\pmod{11}.
\]
Indeed, the squares modulo \(11\) are \(\{0,1,3,4,5,9\}\), and squaring those residues again gives the same set.

But
\[
\{10,2,7,8,6\}\cap \{0,1,3,4,5,9\}=\varnothing,
\]
so \(b^4\equiv -20^a\pmod{11}\) is impossible. Hence \(c\ge 1\) cannot occur.

Therefore \(c=0\). Then
\[
20^a+b^4=2024^0=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), we must have
\[
20^a=1,\qquad b^4=0.
\]
Thus \(a=0\) and \(b=0\). This gives
\[
20^0+0^4=1+0=1=2024^0,
\]
which is valid.

\[
\boxed{(a,b,c)=(0,0,0)}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof:

Suppose \(c\ge 1\). Since \(2024=11\cdot 184\), we have
\[
2024^c\equiv 0 \pmod{11}.
\]
Thus
\[
20^a+b^4\equiv 0 \pmod{11},
\]
so
\[
b^4\equiv -20^a \pmod{11}.
\]

Now \(20\equiv 9\equiv 3^2\pmod{11}\), hence
\[
20^a\equiv (3^a)^2 \pmod{11},
\]
so \(20^a\) is a nonzero quadratic residue modulo \(11\). The nonzero quadratic residues modulo \(11\) are
\[
\{1,3,4,5,9\},
\]
and \(-1\equiv 10\pmod{11}\) is not among them. Therefore \(-20^a\) is not a quadratic residue modulo \(11\).

But
\[
b^4=(b^2)^2
\]
is a quadratic residue modulo \(11\), contradiction. Hence \(c\ge 1\) is impossible, so \(c=0\).

Then
\[
20^a+b^4=2024^0=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), the only possibility is
\[
20^a=1,\qquad b^4=0.
\]
Thus \(a=0\) and \(b=0\).

Checking:
\[
20^0+0^4=1+0=1=2024^0.
\]

Therefore the unique solution is

\[
\boxed{(0,0,0)}.
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

\[
20^a+b^4=2024^c
\]

First factor:
\[
2024=11\cdot 184,
\]
so \(11\mid 2024\).

Assume for contradiction that \(c\ge 1\). Then modulo \(11\),
\[
2024^c\equiv 0 \pmod{11}.
\]
Thus
\[
20^a+b^4\equiv 0 \pmod{11}.
\]

Now
\[
20\equiv 9\equiv 3^2 \pmod{11},
\]
so
\[
20^a\equiv (3^a)^2 \pmod{11}.
\]
Also
\[
b^4=(b^2)^2.
\]
Hence
\[
(3^a)^2+(b^2)^2\equiv 0 \pmod{11}.
\]

But modulo \(11\), the squares are
\[
0,1,3,4,5,9,
\]
and \(-1\equiv 10\) is not a square modulo \(11\). Therefore the only way two squares can sum to \(0\pmod{11}\) is if both are \(0\pmod{11}\). So
\[
3^a\equiv 0\pmod{11},
\]
which is impossible because \(3^a\) is never divisible by \(11\).

Therefore \(c\ge 1\) is impossible, so
\[
c=0.
\]

Then the equation becomes
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), we must have
\[
20^a=1,\qquad b^4=0.
\]
Thus
\[
a=0,\qquad b=0.
\]

Finally,
\[
20^0+0^4=1+0=1=2024^0,
\]
so \((a,b,c)=(0,0,0)\) works.

\[
\boxed{(0,0,0)}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof:

First consider \(c=0\). Then
\[
20^a+b^4=1.
\]
Since \(20^a\ge 1\) and \(b^4\ge 0\), the only possibility is
\[
20^a=1,\qquad b^4=0,
\]
so \(a=0,\ b=0\). Thus \((0,0,0)\) is a solution.

Now assume \(c\ge 1\). Work modulo \(8\). Since \(2024\equiv 0\pmod 8\), we have
\[
2024^c\equiv 0\pmod 8.
\]
But
\[
b^4\equiv 0 \text{ or } 1 \pmod 8,
\]
so checking \(a=0,1\ge2\) modulo \(8\) shows that \(a\ge 2\). In particular \(20^a\equiv 0\pmod 5\).

Modulo \(5\), we have \(20^a\equiv 0\pmod 5\) and \(2024\equiv -1\pmod 5\), so
\[
b^4\equiv (-1)^c \pmod 5.
\]
But fourth powers modulo \(5\) are only \(0\) or \(1\). Hence \(c\) must be even. Write
\[
c=2m.
\]

Modulo \(3\), we have \(2024\equiv -1\pmod 3\), so
\[
2024^{2m}\equiv 1\pmod 3.
\]
Also \(20\equiv -1\pmod 3\), hence
\[
(-1)^a+b^4\equiv 1\pmod 3.
\]
Fourth powers modulo \(3\) are only \(0\) or \(1\), so \(a\) cannot be odd. Thus \(a\) is even. Write
\[
a=2n.
\]
Then the original equation becomes
\[
(20^n)^2+(b^2)^2=(2024^m)^2.
\]
Set
\[
X=20^n,\qquad Y=b^2,\qquad Z=2024^m.
\]
Then
\[
X^2+Y^2=Z^2.
\]

Let
\[
g=\gcd(X,Y).
\]
Since \(X=20^n=2^{2n}5^n\), we have \(11\nmid g\). Also \(g^2\mid X^2+Y^2=Z^2\), so \(g\mid Z\). Define
\[
A=\frac{X}{g},\qquad B=\frac{Y}{g},\qquad C=\frac{Z}{g}.
\]
Then
\[
A^2+B^2=C^2,\qquad \gcd(A,B)=1.
\]
Because \(11^m\mid Z\) and \(11\nmid g\), we get
\[
11\mid C.
\]
Thus modulo \(11\),
\[
A^2+B^2\equiv 0\pmod{11}.
\]
If \(11\mid A\), then \(11\mid B\), contradicting \(\gcd(A,B)=1\). Similarly \(11\nmid B\). Hence \(B\) is invertible modulo \(11\), and
\[
(AB^{-1})^2\equiv -1\pmod{11}.
\]
But for \(p=11\equiv 3\pmod 4\), \(-1\) is not a quadratic residue modulo \(11\): if \(t^2\equiv -1\pmod{11}\), then by Fermat’s little theorem,
\[
t^{10}\equiv 1\pmod{11},
\]
while
\[
t^{10}=(t^2)^5\equiv (-1)^5=-1\pmod{11},
\]
a contradiction.

Therefore no solution exists with \(c\ge 1\). Hence the only solution is

\[
\boxed{(a,b,c)=(0,0,0)}.
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(0,0,0)}
\]

Proof.

First, \((0,0,0)\) works:
\[
20^0+0^4=1=2024^0.
\]

Now suppose \((a,b,c)\) is another solution.

### 1. Excluding \(a=0\) except for \(b=c=0\)

If \(a=0\), then
\[
1+b^4=2024^c.
\]
If \(c=0\), then \(b=0\), giving \((0,0,0)\).

If \(c\ge 1\), then \(2024^c\equiv 0\pmod 4\). But
\[
1+b^4\equiv 
\begin{cases}
1 \pmod 4,& b\text{ even},\\
2 \pmod 4,& b\text{ odd},
\end{cases}
\]
so \(1+b^4\not\equiv 0\pmod 4\), contradiction. Thus for \(a=0\), only \((0,0,0)\) occurs.

Henceforth assume \(a\ge 1\). Then \(c\ge 1\), since \(2024^0=1<20^a\).

### 2. Parity of \(c\) modulo \(5\)

Modulo \(5\),
\[
20^a\equiv 0,\qquad 2024\equiv -1.
\]
Thus
\[
b^4\equiv 2024^c\equiv (-1)^c \pmod 5.
\]
But for every integer \(b\), \(b^4\equiv 0\) or \(1\pmod 5\). Therefore \(c\) cannot be odd, so
\[
c=2k.
\]

### 3. Parity of \(a\) modulo \(3\)

Since \(c\) is even,
\[
2024^{2k}\equiv (-1)^{2k}\equiv 1\pmod 3.
\]
Also \(20\equiv -1\pmod 3\), so
\[
20^a\equiv (-1)^a\pmod 3.
\]
If \(a\) were odd, then
\[
20^a\equiv -1\pmod 3,
\]
so the equation modulo \(3\) would give
\[
b^4\equiv 2\pmod 3,
\]
impossible because fourth powers modulo \(3\) are only \(0\) or \(1\). Hence \(a\) is even:
\[
a=2m.
\]

### 4. Final contradiction modulo \(11\)

Now
\[
20^{2m}+b^4=2024^{2k},
\]
so
\[
(20^m)^2+(b^2)^2=(2024^k)^2.
\]
Since
\[
2024=11\cdot 184,
\]
we have
\[
(2024^k)^2\equiv 0\pmod{11}.
\]
Therefore
\[
(20^m)^2+(b^2)^2\equiv 0\pmod{11}.
\]
But \(11\nmid 20\), so \(20^m\) is invertible modulo \(11\). Hence
\[
(b^2(20^m)^{-1})^2\equiv -1\pmod{11}.
\]
This would mean \(-1\) is a quadratic residue modulo \(11\). But the squares modulo \(11\) are
\[
0,1,3,4,5,9,
\]
and \(-1\equiv 10\pmod{11}\) is not among them. Contradiction.

Thus no solution exists with \(a\ge 1\).

Therefore the only non-negative integer solution is

\[
\boxed{(a,b,c)=(0,0,0)}.
\]

</details>
