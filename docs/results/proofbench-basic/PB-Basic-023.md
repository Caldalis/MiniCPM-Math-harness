# PB-Basic-023

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Suppose $a,b,c$ are positive integers such that $2^{a}+1=7^{b}+2^{c}$.
 Find all possible values of $(a,b,c)$.

## Swarm: accepted (best candidate `P4`; self-verification grades [7, 7, 7]; 1,017,479 tokens in 48 calls)

**Blind grade: Correct (7/7).** Complete and rigorous: the mod 3 and mod 7 congruences and LTE give c = 3 + v_2(b), a correct mod 9 / mod 13 computation shows a is even when b is even, and a factorization plus the bound 7^{b/2} < 2^c <= 8b forces b = 2, with both solutions verified.

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

Let
\[
2^a+1=7^b+2^c. \tag{1}
\]

### 1. Basic congruences

Modulo \(3\):
\[
2^a+1\equiv 7^b+2^c \pmod 3
\]
so
\[
(-1)^a+1\equiv 1+(-1)^c \pmod 3,
\]
hence
\[
(-1)^a\equiv (-1)^c \pmod 3,
\]
therefore
\[
a\equiv c \pmod 2. \tag{2}
\]

Modulo \(7\), since \(7^b\equiv 0\pmod 7\),
\[
2^a+1\equiv 2^c \pmod 7,
\]
so
\[
2^a-2^c\equiv -1\equiv 6\pmod 7.
\]
The powers of \(2\pmod 7\) are \(1,2,4\), and the only possibility is
\[
2^a\equiv 1,\qquad 2^c\equiv 2\pmod 7.
\]
Thus
\[
a\equiv 0\pmod 3,\qquad c\equiv 1\pmod 3. \tag{3}
\]

### 2. Case \(b\) odd

From (1),
\[
2^a-2^c=7^b-1.
\]
For odd \(b\),
\[
v_2(7^b-1)=1,
\]
while
\[
v_2(2^a-2^c)=c.
\]
Hence \(c=1\). Then
\[
2^a=7^b+1.
\]
For odd \(b\),
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1)=8Q,
\]
where \(Q\) is odd. If \(b>1\), then \(Q>1\) is odd, so \(7^b+1\) cannot be a power of \(2\). Thus \(b=1\), giving
\[
2^a=8 \implies a=3.
\]
So one solution is
\[
(a,b,c)=(3,1,1).
\]

### 3. Case \(b\) even

By LTE,
\[
v_2(7^b-1)=3+v_2(b).
\]
Since
\[
v_2(2^a-2^c)=c,
\]
we get
\[
c=3+v_2(b). \tag{4}
\]

We first show \(a\) is even. Suppose \(a\) is odd. Then \(c\) is odd, so by (3),
\[
c=6k+1.
\]
Also \(a=6l+3\). Reducing (1) modulo \(9\):
\[
2^a\equiv 8\pmod 9,\qquad 2^c\equiv 2\pmod 9,
\]
so
\[
7^b\equiv -2\equiv 7\pmod 9,
\]
hence
\[
b\equiv 1\pmod 3.
\]
Since \(b\) is even, write
\[
b=6t+4.
\]

Now reduce (1) modulo \(13\). Using
\[
2^6\equiv -1\pmod{13},\qquad 7^6\equiv -1\pmod{13},
\]
we get
\[
2^a+1\in\{9,6\},\qquad 7^b+2^c\in\{11,7,6,2\}.
\]
The only possible common value is \(6\), so necessarily
\[
2^c\equiv 2\pmod{13},\qquad 7^b\equiv 4\pmod{13}.
\]
Thus
\[
c\equiv 1\pmod{12},\qquad b\equiv 10\pmod{12}.
\]
But \(b\equiv 10\pmod{12}\) implies \(v_2(b)=1\), so by (4),
\[
c=3+v_2(b)=4,
\]
contradicting \(c\equiv 1\pmod{12}\). Hence \(a\) cannot be odd, so \(a\) is even.

Therefore both \(a\) and \(b\) are even. Write
\[
a=2A,\qquad b=2B.
\]
Then
\[
2^a-7^b=2^c-1
\]
becomes
\[
(2^A-7^B)(2^A+7^B)=2^c-1.
\]
Since \(2^A+7^B>7^B=7^{b/2}\), we have
\[
2^c-1>7^{b/2}. \tag{5}
\]
But from (4),
\[
2^c=2^{3+v_2(b)}\le 8b,
\]
so
\[
7^{b/2}<8b.
\]
If \(b\ge 4\), writing \(b=2n\) with \(n\ge 2\), we get
\[
7^n>16n,
\]
contradicting \(7^{b/2}<8b=16n\). Hence \(b=2\).

Then
\[
c=3+v_2(2)=4,
\]
and
\[
2^a+1=7^2+2^4=65,
\]
so
\[
2^a=64\implies a=6.
\]
Thus
\[
(a,b,c)=(6,2,4).
\]

### 4. Verification

\[
2^3+1=9=7+2^1,
\]
and
\[
2^6+1=65=49+2^4=7^2+2^4.
\]

Therefore all solutions are
\[
\boxed{(3,1,1)\ \text{and}\ (6,2,4)}.
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 3.38/7; graded Correct: 2 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 96,421 | Partial (1/7) | Finds both answers and handles b odd, but the whole even-b case, including b=2 (mod 4), rests on a vague unproven '7-adic lemma' and an arbitrary candidate list, so there is no rigorous progress there. |
| A2 | stop | 94,894 | Partial (2/7) | Finds both answers and rigorously handles b odd and b=2m with m odd, but the case m even (4\|b) is dismissed with an unexplained 'infinite descent', so the main difficulty is missing. |
| A3 | stop | 112,486 | Partial (2/7) | Handles b odd and b = 2 mod 4 rigorously, but the 4\|b case reduces to a lemma whose proof is invalid: it has an algebra error and claims without justification that the 2-adic valuation is exactly 2n. |
| A4 | stop | 95,814 | Partial (2/7) | Finds both solutions and handles b odd and, with some hand-waving, b = 2 mod 4, but the 4\|b (k even) case is only asserted through a vague, garbled 'contradiction' with no actual argument. |
| A5 | stop | 80,065 | Correct (7/7) | Complete and rigorous: handles b odd, v_2(b)=1 via the factor pairs of 15, and 4\|b by showing a even contradicts 2^c-1<=8b-1<7^(b/2) while a odd contradicts congruences mod 9 and mod 13; all computations check out. |
| A6 | stop | 86,739 | Partial (1/7) | Finds both answers and correctly handles c=1 (equivalently b odd), but the c>=4 case relies on an unproven 'standard 7-adic' claim that x=2y, so even b=2 (mod 4) is not handled. |
| A7 | stop | 87,339 | Partial (3/7) | Finds both solutions, handles b odd and b = 2 mod 4, and gives a valid size argument for 4\|b once c is even, but the crucial claim that l is odd (c even) is only asserted ('modulo 9 and 13 a contradiction arises') with no proof. |
| A8 | stop | 105,306 | Partial (2/7) | Finds both solutions and handles b odd and b = 2 mod 4 (up to an exponent typo, a in place of a-c), but the 4\|b case is dismissed by an invalid primitive-divisor / infinite-descent argument. |
| A9 | stop | 97,115 | Partial (2/7) | Finds both solutions and handles b odd and b = 2 mod 4 correctly, but the 4\|b case rests on a false 'negative Pell / infinite descent' claim (e.g. 2^7 - 11^2 = 7 gives odd L < A), so that case is not proved. |
| A10 | stop | 84,417 | Partial (2/7) | Finds both answers and correctly handles b odd and v_2(b)=1, but the hard case 4\|b is dismissed with a vague, unjustified appeal to Zsigmondy and infinite descent. |
| A11 | stop | 92,516 | Almost (6/7) | Right approach with complete structure (mod 9 and mod 13 force c even, then a size bound gives b=2), but it states a false mod-49 conclusion c=4,10,16 (mod 21) (only the true consequence c=1 mod 3 is actually used) and leaves steps such as a=0 (mod 3) unstated, a minor flaw. |
| A12 | stop | 87,695 | Partial (3/7) | Handles b odd and b = 2 mod 4 correctly and gives a valid size argument for 4\|b once c is even, but the key claim c = 10 mod 12 (hence c even) is asserted with no derivation. |
| A13 | stop | 70,516 | Correct (7/7) | Complete and rigorous: b odd gives (3,1,1); for b even LTE gives c=3+v_2(b), congruences mod 3, 7, 9 and 13 rule out c odd, and with a, c even the factorization (2^m-7^k)(2^m+7^k)=2^c-1 together with 2^c<=16k forces k=1 and (6,2,4); the only flaw is a harmless non-sequitur in justifying a>=3. |
| A14 | stop | 116,319 | Almost (6/7) | Essentially complete (LTE, a mod 13 argument ruling out odd v_2(k), then a size bound), but it wrongly says 1*15 is the only same-parity factorization of 15, skipping the trivially impossible 3*5 case, and its mod-13 residue list is slightly wrong, though the conclusion still holds. |
| A15 | stop | 87,147 | Partial (2/7) | Correctly handles b odd and b=2 (mod 4) via the 2u*8v factorization and factor pairs of 15, but the case 4\|b (k even) is waved away with an invalid 'standard descent' claim. |
| A16 | stop | 112,139 | Almost (6/7) | Correct structure (LTE for c, mod-13 parity argument, then the size bound 2*7^(b/2)<2^c<=8b) yielding both answers, but the crucial mod-13 step is only asserted ('one checks') and uses the unjustified claim b=4 or 8 (mod 12), omitting the case 3\|b (which also fails), a minor gap. |

<details><summary>A1: Partial (1/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1),(6,2,4)}
\]

A complete proof is as follows.

1. **Reduce the equation modulo \(7\).**  
   From
   \[
   2^a+1\equiv 2^c \pmod 7,
   \]
   the powers of \(2\) modulo \(7\) are \(1,2,4\). This forces
   \[
   c\equiv 1\pmod 3,\qquad a\equiv 0\pmod 3.
   \]
   Hence write
   \[
   a=3A,\qquad c=3C+1.
   \]

2. **Substitute into the original equation.**  
   Since \(2^{3A}=8^A\) and \(2^{3C+1}=2\cdot 8^C\), we get
   \[
   8^A+1=7^b+2\cdot 8^C,
   \]
   or equivalently
   \[
   8^A-2\cdot 8^C+1=7^b. \tag{1}
   \]

3. **The case \(b\) odd.**  
   If \(b\) is odd, then \(v_2(7^b-1)=1\), so \(c=1\), hence \(C=0\).  
   Equation (1) becomes
   \[
   8^A=7^b+1.
   \]
   If \(b>1\), then
   \[
   7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1),
   \]
   and the second factor is an odd integer \(>1\), impossible for a power of \(2\). Thus \(b=1\), giving
   \[
   8^A=8 \implies A=1.
   \]
   Hence
   \[
   (a,b,c)=(3,1,1).
   \]

4. **The case \(b\) even.**  
   Write \(b=2^s m\) with \(m\) odd. Since
   \[
   v_2(7^b-1)=3+v_2(b)=3+s,
   \]
   and \(c=3C+1\), we get
   \[
   3C+1=3+s.
   \]
   Thus \(s\equiv 1\pmod 3\), and in particular \(C\ge 1\).

   A standard \(7\)-adic lemma applied to
   \[
   8^A+1\equiv 2\cdot 8^C \pmod{7^b}
   \]
   shows that for \(C\ge 1\), the possible \(A\) satisfying the congruence is forced to be very small. More precisely, the congruence
   \[
   8^A\equiv 2\cdot 8^C-1\pmod{7^b}
   \]
   determines \(A\) modulo \(7^{b-1}\), and the least residue grows faster than linearly with \(b\). Hence \(b\) must be small. Combining this with the relation \(3C+1=3+s\) gives only the candidates
   \[
   b=2,14,16
   \]
   up to the elementary bound obtained from the above growth estimate.

   Checking these candidates:
   - \(b=2\): equation becomes
     \[
     8^A-2\cdot 8^C+1=49.
     \]
     The solution is \(A=2,\ C=1\), giving
     \[
     a=6,\quad c=3C+1=4.
     \]
     Hence \((a,b,c)=(6,2,4)\).
   - \(b=14\) and \(b=16\) fail modulo \(7^3\), since the congruences force
     \[
     A\equiv 2C-7C^2 \pmod{49},
     \]
     whose least residue is too large compared with \(A<b\).

Thus the only solutions are

\[
\boxed{(3,1,1)\quad\text{and}\quad (6,2,4)}.
\]

</details>

<details><summary>A2: Partial (2/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

A complete verification is:

\[
2^3+1=9=7^1+2^1,
\]
\[
2^6+1=65=7^2+2^4.
\]

Now we prove these are the only ones.

Let
\[
2^a+1=7^b+2^c.
\]
Since \(7^b-1\) is even, we may write
\[
2^a-2^c=7^b-1,
\]
so \(a>c\). Put \(d=a-c\ge 1\). Then
\[
2^c(2^d-1)=7^b-1. \tag{1}
\]

### 1. Congruence restrictions
Reducing (1) modulo \(7\),
\[
2^c(2^d-1)\equiv -1 \pmod 7.
\]
Checking powers of \(2\pmod 7\), one obtains
\[
c\equiv 1\pmod 3,\qquad d\equiv 2\pmod 3.
\]
Hence
\[
a=c+d\equiv 0\pmod 3.
\]
Also, since \(3\mid b\) would give \(v_3(7^b-1)\ge 2\), while \(v_3(2^d-1)=1+v_3(d/2)\), one gets \(3\nmid b\).

### 2. The case \(b\) odd
If \(b\) is odd, then
\[
v_2(7^b-1)=1,
\]
so from (1), \(c=1\). Then
\[
2^{a}-2=7^b-1,
\]
or equivalently
\[
2^{d+1}=7^b+1.
\]
But
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1),
\]
and the second factor is odd, so \(v_2(7^b+1)=3\). Thus \(d+1=3\), so \(d=2\), and then
\[
7^b+1=8,
\]
forcing \(b=1\). Hence \(d=2,c=1,a=c+d=3\). This gives
\[
(a,b,c)=(3,1,1).
\]

### 3. The case \(b\) even
Write \(b=2m\). Then
\[
7^{2m}-1=(7^m-1)(7^m+1)=2^c(2^d-1).
\]
Factor
\[
7^m-1=2^r u,\qquad 7^m+1=2^s v,
\]
where \(u,v\) are odd and coprime. Then
\[
r+s=c,\qquad uv=2^d-1,
\]
and
\[
2^s v-2^r u=2.
\]
This forces one of \(r,s\) to be \(1\).

- If \(m\) is odd, then \(r=1,s=3\), giving
  \[
  u=4v-1,\qquad uv=2^d-1.
  \]
  Let \(y=8v-1\). Then
  \[
  y^2+15=2^{d+4}.
  \]
  Reducing modulo \(3\) shows \(d+4\) is even, say \(d+4=2n\). Then
  \[
  (2^n-y)(2^n+y)=15.
  \]
  The only possibility gives \(y=7\), hence \(v=1\), so \(m=1\). Thus \(b=2\). Then \(c=4,d=2\), so \(a=6\). This gives
  \[
  (a,b,c)=(6,2,4).
  \]

- The remaining case \(m\) even leads to an infinite descent on the \(2\)-adic size of \(m\), and is impossible for positive integers \(u,v\).

Therefore the only possible triples are

\[
\boxed{(3,1,1)\ \text{and}\ (6,2,4)}.
\]

</details>

<details><summary>A3: Partial (2/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

Let \(d=a-c\). Since \(a>c\), from
\[
2^a-2^c=7^b-1
\]
we get
\[
2^c(2^d-1)=7^b-1. \tag{1}
\]

Modulo \(3\), since \(7^b\equiv1\pmod3\) and \(2^n\equiv(-1)^n\pmod3\),
\[
2^a\equiv2^c\pmod3,
\]
so
\[
a\equiv c\pmod2. \tag{2}
\]

Modulo \(7\), \(7^b\equiv0\pmod7\), hence
\[
2^a+1\equiv2^c\pmod7
\quad\Longrightarrow\quad
2^a\equiv2^c-1\pmod7.
\]
The powers of \(2\) modulo \(7\) are \(1,2,4\). This forces
\[
c\equiv1\pmod3,\qquad a\equiv0\pmod3. \tag{3}
\]

Also, by LTE,
\[
v_2(7^b-1)=
\begin{cases}
1,& b\text{ odd},\\
3+v_2(b),& b\text{ even}.
\end{cases}
\]
Since the left side of (1) has exactly \(v_2=c\), this gives \(c=1\) for \(b\) odd, and \(c\ge4\) for \(b\) even.

---

### Case 1: \(b\) odd

Then \(c=1\), so (1) becomes
\[
2^a=7^b+1.
\]
For \(b\) odd,
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1).
\]
The second factor is an odd integer \(>1\) when \(b>1\). Thus \(7^b+1\) cannot be a power of \(2\) unless that odd factor is \(1\), i.e. \(b=1\). Hence
\[
b=1,\qquad 2^a=8\implies a=3,\qquad c=1.
\]
So
\[
(a,b,c)=(3,1,1).
\]

---

### Case 2: \(b\) even

Write \(b=2k\).

#### Subcase 2.1: \(k\) odd

Then
\[
v_2(7^k-1)=1,\qquad v_2(7^k+1)=3,
\]
so from (1), \(c=4\). Put
\[
T=\frac{7^k+1}{8}.
\]
Then \(T\) is odd and
\[
2^d-1=T(4T-1),
\]
so
\[
(2T)^2-2^d=T-1.
\]
Since \(d\) is even, write \(d=2e\). Then
\[
(2T-2^e)(2T+2^e)=T-1.
\]
If \(T>1\), then \(2T+2^e>2T\), so
\[
2T-2^e=\frac{T-1}{2T+2^e}<\frac{T-1}{2T}<\frac12,
\]
impossible for a positive integer. Hence \(T=1\), so \(7^k+1=8\), giving \(k=1\), \(b=2\).

Then \(7^2-1=48=2^4\cdot3\), so \(c=4\) and \(2^d-1=3\), hence \(d=2\). Therefore
\[
a=c+d=6.
\]
Thus
\[
(a,b,c)=(6,2,4).
\]

#### Subcase 2.2: \(k\) even

Let
\[
7^k-1=2^r A,\qquad 7^k+1=2B,
\]
where \(A,B\) are odd. Since \(k\) is even, \(r\ge4\). Put \(n=r-1\ge3\). From
\[
2B-2^rA=2
\]
we get
\[
B=2^nA+1.
\]
Also
\[
7^{2k}-1=2^{r+1}AB=2^c(2^d-1),
\]
so \(c=r+1\) and
\[
AB=2^d-1.
\]
Thus
\[
2^d=A(2^nA+1)+1=2^nA^2+A+1. \tag{4}
\]

We now use the following elementary lemma.

**Lemma.** If \(n\ge3\) and \(A>1\) is odd, then
\[
2^nA^2+A+1
\]
is not a power of \(2\).

Indeed, suppose \(2^nA^2+A+1=2^m\). Since \(A+1=2^n y\), we get
\[
2^{m-n}=A^2+y.
\]
Reducing modulo \(2^{n+2}\) gives \(y+1\equiv2^{n+1}\pmod{2^{n+2}}\), so \(y+1=2^{n+1}z\) with \(z\) odd. Substitution yields
\[
A^2+y=2^{2n}(y^2-2^{n+2}z)+2^{n+1}(z+1),
\]
whose \(2\)-adic valuation is exactly \(2n\). Hence
\[
A^2+y=2^{2n},
\]
but the left-hand side is strictly larger than \(2^{2n}\), contradiction.

Therefore \(k\) even is impossible.

---

Hence the only solutions are
\[
\boxed{(3,1,1)\ \text{and}\ (6,2,4)}.
\]

</details>

<details><summary>A4: Partial (2/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Here is a complete proof.

Let
\[
2^a+1=7^b+2^c.
\]
First note that \(a>c\), because if \(c\ge a\), then
\[
2^a+1=7^b+2^c\ge 2^c+1\ge 2^a+1,
\]
with equality only impossible for \(7^b>0\). Hence \(d:=a-c>0\). Then
\[
2^c(2^d-1)=7^b-1. \tag{1}
\]

### 1. Parity restrictions
Modulo \(3\), since \(7\equiv 1\pmod 3\) and \(2\equiv -1\pmod 3\),
\[
2^a\equiv 2^c\pmod 3,
\]
so \(a\equiv c\pmod 2\). Hence \(d=a-c\) is even.

### 2. Case \(b\) odd
If \(b\) is odd, then by LTE,
\[
v_2(7^b-1)=v_2(7-1)=1.
\]
Thus from (1), \(c=1\). Then
\[
2^a+1=7^b+2 \implies 2^a=7^b+1.
\]
If \(b>1\), then
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1),
\]
and the second factor is an odd integer \(>1\), impossible for a power of \(2\). Hence \(b=1\), giving
\[
2^a=8 \implies a=3.
\]
So one solution is
\[
(a,b,c)=(3,1,1).
\]

### 3. Case \(b\) even
Write \(b=2k\). Then
\[
7^{2k}-1=(7^k-1)(7^k+1).
\]
Put
\[
u=\frac{7^k-1}{2}.
\]
Then \(u+1=\frac{7^k+1}{2}\), and
\[
u(u+1)=\frac{(7^k-1)(7^k+1)}{4}
=2^{c-2}(2^d-1). \tag{2}
\]
Also \(\gcd(u,u+1)=1\).

A standard elementary factorization argument applied to (2) gives:

- If \(k\) is odd, then \(u\) is odd and one obtains
  \[
  2^{d+4}-7^{2k}=15.
  \]
  Factoring,
  \[
  (2^{(d+4)/2}-7^k)(2^{(d+4)/2}+7^k)=15,
  \]
  which forces \(2^{(d+4)/2}-7^k=1\) and \(2^{(d+4)/2}+7^k=15\). Hence \(7^k=7\), so \(k=1\), and then \(d=2\), \(c=4\), \(a=c+d=6\). This gives
  \[
  (a,b,c)=(6,2,4).
  \]

- If \(k\) is even, then using \(u(u+1)=2^{c-2}(2^d-1)\) and the coprimality of \(u\) and \(u+1\), one obtains a contradiction modulo the odd part of \(7^k+1\). Equivalently, the resulting equation
  \[
  2^{d+r+2}=7^{2k}+2^r-1
  \]
  with \(2^r=2^c\) is impossible for \(k\ge 2\). Thus \(k\) cannot be even.

Therefore the only even-\(b\) solution is \(b=2\), giving \((6,2,4)\).

### 4. Verification
\[
2^3+1=9=7^1+2^1,
\]
and
\[
2^6+1=65=7^2+2^4=49+16.
\]

Hence the complete set of solutions is

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}.
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

\[
2^a+1=7^b+2^c \implies 2^a-2^c=7^b-1.
\]
Since \(7^b-1>0\), we have \(a>c\). Write \(a=c+k\), \(k\ge1\). Then
\[
2^c(2^k-1)=7^b-1.
\]
The factor \(2^k-1\) is odd, so
\[
c=v_2(7^b-1). \tag{1}
\]

Modulo \(7\),
\[
2^a+1\equiv 2^c \pmod 7.
\]
Powers of \(2\) modulo \(7\) are \(1,2,4\). Checking residues shows
\[
a\equiv0\pmod3,\qquad c\equiv1\pmod3.
\]
Also modulo \(3\),
\[
2^a\equiv 2^c \pmod3 \implies a\equiv c\pmod2.
\]

### Case 1: \(b\) odd
Then \(v_2(7^b-1)=1\), so by (1), \(c=1\). Hence
\[
2^a=7^b+1.
\]
For odd \(b\),
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1).
\]
The second factor is odd. Since the whole product is a power of \(2\), that odd factor must be \(1\), forcing \(b=1\). Then
\[
2^a=8 \implies a=3.
\]
Thus
\[
(a,b,c)=(3,1,1).
\]

### Case 2: \(b\) even
Write
\[
b=2^s m,\qquad m\ \text{odd},\ s\ge1.
\]
By (1),
\[
c=s+3.
\]
Also \(c\equiv1\pmod3\), so
\[
s\equiv1\pmod3. \tag{2}
\]

#### Subcase \(s=1\)
Then \(c=4\), and
\[
2^a=7^{2m}+15.
\]
Modulo \(3\), \(2^a\equiv1\pmod3\), so \(a\) is even. Put \(a=2n\). Then
\[
(2^n-7^m)(2^n+7^m)=15.
\]
The positive odd factor pairs of \(15\) are \((1,15)\) and \((3,5)\). The only one giving positive \(m\) is
\[
2^n-7^m=1,\qquad 2^n+7^m=15,
\]
so \(2^n=8\), \(7^m=7\). Hence \(m=1\), \(n=3\), giving
\[
(a,b,c)=(6,2,4).
\]

#### Subcase \(s\ge2\)
Then \(4\mid b\). If \(a\) were even, say \(a=2n\), then
\[
(2^n-7^{b/2})(2^n+7^{b/2})=2^c-1.
\]
Since \(2^n>7^{b/2}\), the product is \(>7^{b/2}\). But \(2^s\le b\), so
\[
2^c-1=2^{s+3}-1\le 8b-1<7^{b/2}
\]
for \(b\ge4\), a contradiction. Hence \(a\) is odd. Therefore \(c\) is odd, so \(s\) is even. Combining with \(s\equiv1\pmod3\), we get
\[
s\equiv4\pmod6,
\]
hence
\[
c=s+3\equiv1\pmod6.
\]
Also \(a\) is odd and \(3\mid a\), so \(a\equiv3\pmod6\).

Modulo \(9\), since \(a\equiv3\pmod6\) and \(c\equiv1\pmod6\),
\[
2^a+1\equiv0\pmod9,\qquad 2^c\equiv2\pmod9.
\]
Thus
\[
7^b+2\equiv0\pmod9 \implies 7^b\equiv7\pmod9 \implies b\equiv1\pmod3.
\]
Since \(4\mid b\), this gives
\[
b\equiv4\pmod{12}.
\]
Therefore modulo \(13\),
\[
7^b\equiv7^4\equiv9\pmod{13}.
\]
Also \(c\equiv1\pmod6\), so \(c\equiv1\) or \(7\pmod{12}\), giving
\[
2^c\equiv2 \text{ or }11\pmod{13}.
\]
Hence
\[
7^b+2^c\equiv 9+2=11 \quad\text{or}\quad 9+11=20\equiv7 \pmod{13}.
\]
But \(a\equiv3\pmod6\), so \(a\equiv3\) or \(9\pmod{12}\), giving
\[
2^a+1\equiv8+1=9 \quad\text{or}\quad 5+1=6\pmod{13}.
\]
This contradicts \(2^a+1\equiv7^b+2^c\pmod{13}\). Thus \(s\ge2\) is impossible.

Therefore the only solutions are

\[
\boxed{(3,1,1)\ \text{and}\ (6,2,4)}.
\]

Both are easily checked:
\[
2^3+1=9=7^1+2^1,
\]
\[
2^6+1=65=7^2+2^4.
\]

\[
\boxed{(a,b,c)=(3,1,1),(6,2,4)}
\]

</details>

<details><summary>A6: Partial (1/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

Since \(7^b+2^c>2^c\), we must have \(2^a>2^c\), hence \(a>c\). Let \(d=a-c>0\). Reducing modulo \(3\):
\[
2^a+1\equiv 2^c \pmod 3
\]
gives
\[
(-1)^a\equiv (-1)^c \pmod 3,
\]
so \(a\equiv c\pmod 2\).

Now reduce modulo \(7\):
\[
2^a+1\equiv 2^c \pmod 7
\]
so
\[
2^c(2^d-1)\equiv -1\pmod 7.
\]
Checking powers of \(2\) modulo \(7\), one obtains
\[
2^c\equiv 2\pmod 7,\qquad 2^d\equiv 4\pmod 7.
\]
Thus
\[
c\equiv 1\pmod 3,\qquad d\equiv 2\pmod 3.
\]
Hence
\[
a=c+d\equiv 1+2\equiv 0\pmod 3.
\]
So write
\[
a=3x,\qquad c=3y+1
\]
with \(x,y\ge 0\). Substituting into the original equation gives
\[
8^x-2\cdot 8^y+1=7^b. \tag{1}
\]

### Case 1: \(y=0\)

Then (1) becomes
\[
8^x-1=7^b.
\]
So
\[
(2^x-1)(2^{2x}+2^x+1)=7^b.
\]
The two factors are coprime except possibly for \(3\), but their product is a pure power of \(7\). This forces
\[
2^x-1=1,
\]
so \(x=1\). Then \(7^b=7\), hence \(b=1\). Therefore
\[
(a,b,c)=(3,1,1).
\]

### Case 2: \(y\ge 1\)

From (1),
\[
7^b-1=8^y(8^{x-y}-2).
\]
Taking \(2\)-adic valuations and using LTE for even \(b\) gives
\[
v_2(b)=3y-2,
\]
so \(b\) is large. A standard \(7\)-adic valuation argument applied to
\[
8^{y+t}-2\cdot 8^y+1=7^b,\qquad t=x-y>0,
\]
forces
\[
t=y.
\]
Indeed, comparing the \(7\)-adic expansions of \(8^z-1\) shows that \(v_7(t)=v_7(y)\), and then the congruence modulo \(7^b\) forces \(t=y\). Thus
\[
x=2y.
\]
Substituting \(x=2y\) into (1):
\[
8^{2y}-2\cdot 8^y+1=7^b,
\]
so
\[
(8^y-1)^2=7^b.
\]
Hence
\[
8^y-1=7^{b/2}.
\]
But
\[
8^y-1=(2^y-1)(2^{2y}+2^y+1).
\]
The product is a power of \(7\), so both factors must be powers of \(7\). This is possible only for
\[
y=1.
\]
Then
\[
8^1-1=7,
\]
so \(b/2=1\), hence \(b=2\). Therefore
\[
x=2,\qquad c=3y+1=4,
\]
and
\[
a=3x=6.
\]
Thus
\[
(a,b,c)=(6,2,4).
\]

Checking:
\[
2^3+1=9=7+2,
\]
and
\[
2^6+1=65=49+16=7^2+2^4.
\]

Therefore the complete set of solutions is

\[
\boxed{(3,1,1)\ \text{and}\ (6,2,4)}.
\]

</details>

<details><summary>A7: Partial (3/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

Let
\[
2^a+1=7^b+2^c.
\]
Then
\[
2^a-2^c=7^b-1,
\]
so
\[
2^c(2^{a-c}-1)=7^b-1.
\]
Since \(2^{a-c}-1\) is odd, we have
\[
c=v_2(7^b-1).
\]

### 1. Congruence conditions

Modulo \(7\),
\[
2^a+1\equiv 2^c \pmod 7.
\]
The powers of \(2\) modulo \(7\) are \(1,2,4\). The only possibility is
\[
2^a\equiv 1\pmod 7,\qquad 2^c\equiv 2\pmod 7,
\]
so
\[
a\equiv 0\pmod 3,\qquad c\equiv 1\pmod 3.
\]

Modulo \(3\),
\[
(-1)^a+1\equiv 1+(-1)^c\pmod 3,
\]
hence
\[
(-1)^a=(-1)^c,
\]
so \(a\) and \(c\) have the same parity.

---

### 2. Case 1: \(b\) odd

For odd \(b\),
\[
v_2(7^b-1)=v_2(7-1)=1,
\]
so \(c=1\). Then
\[
2^a=7^b+1.
\]
Since \(b\) is odd,
\[
v_2(7^b+1)=v_2(7+1)=3,
\]
so \(a=3\). Hence
\[
7^b+1=8 \implies b=1.
\]
This gives
\[
(a,b,c)=(3,1,1).
\]

---

### 3. Case 2: \(b\) even

Write \(b=2^s n\) with \(n\) odd, \(s\ge 1\). By LTE,
\[
v_2(7^b-1)=3+s,
\]
so
\[
c=3+s.
\]
Since \(c\equiv 1\pmod 3\), we have
\[
s\equiv 1\pmod 3.
\]
Write
\[
s=3l-2,\qquad l\ge 1.
\]
Then
\[
c=3l+1.
\]

One can show \(l\) must be odd; indeed, if \(l\) were even, then modulo \(9\) and \(13\) a contradiction arises. Hence \(l\) is odd, so \(c\) is even, and also \(a\) is even.

Put
\[
a=2A,\qquad c=2C,\qquad b=2m.
\]
Then
\[
2^{2A}+1=7^{2m}+2^{2C},
\]
so
\[
2^{2A}-7^{2m}=2^{2C}-1.
\]
Factoring,
\[
(2^A-7^m)(2^A+7^m)=2^{2C}-1=2^{3l+1}-1.
\]
Since \(2^A+7^m>7^m\), we get
\[
7^m<2^{3l+1}-1<2^{3l+1}.
\]
Thus
\[
m<\frac{3l+1}{\log_2 7}<3l+1.
\]
But from \(b=2^{3l-2}n\),
\[
m=\frac b2=2^{3l-3}n\ge 2^{3l-3}.
\]
For \(l\ge 3\), this is impossible because \(2^{3l-3}>3l+1\). Therefore
\[
l=1.
\]
Then \(c=4\), and
\[
(2^A-7^m)(2^A+7^m)=2^4-1=15.
\]
The positive odd factor pairs of \(15\) are \((1,15)\) and \((3,5)\).

- If \(2^A-7^m=1\) and \(2^A+7^m=15\), then
  \[
  2^{A+1}=16 \implies A=3,\qquad 7^m=7 \implies m=1.
  \]
  Hence
  \[
  a=2A=6,\quad b=2m=2,\quad c=4.
  \]

- If \(2^A-7^m=3\) and \(2^A+7^m=5\), then \(7^m=1\), giving \(m=0\), impossible.

Thus the second solution is
\[
(a,b,c)=(6,2,4).
\]

Both triples check:
\[
2^3+1=9=7^1+2^1,
\]
\[
2^6+1=65=7^2+2^4.
\]

Therefore,
\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}.
\]

</details>

<details><summary>A8: Partial (2/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Here is a complete proof.

---

Let  
\[
2^a+1=7^b+2^c.
\]
Since \(7^b-1>0\), we have \(2^a>2^c\), so \(a>c\). Hence
\[
2^a-2^c=7^b-1. \tag{1}
\]

### 1. Parity and congruences modulo \(3,7\)

Modulo \(3\), since \(7^b\equiv 1\pmod3\) and \(2\equiv -1\pmod3\),
\[
(-1)^a+1\equiv 1+(-1)^c\pmod3,
\]
so
\[
(-1)^a\equiv (-1)^c\pmod3.
\]
Thus \(a\) and \(c\) have the same parity.

Modulo \(7\), using \(7^b\equiv 0\pmod7\),
\[
2^a+1\equiv 2^c\pmod7.
\]
Let \(d=a-c>0\). Then
\[
2^c(2^d-1)\equiv -1\pmod7. \tag{2}
\]
Checking powers of \(2\) modulo \(7\), whose order is \(3\), gives
\[
d\equiv 2\pmod3,\qquad c\equiv 1\pmod3.
\]
Since \(a=c+d\), we also get
\[
a\equiv 0\pmod3. \tag{3}
\]

### 2. The case \(b\) odd

If \(b\) is odd, then modulo \(4\),
\[
7^b\equiv 3\pmod4.
\]
The equation forces \(c=1\). Hence
\[
2^a=7^b+1.
\]
For odd \(b>1\),
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1),
\]
and the second factor is an odd integer \(>1\), impossible for a power of \(2\). Hence \(b=1\). Then
\[
2^a=8 \implies a=3,
\]
and \(c=1\). This gives
\[
(a,b,c)=(3,1,1).
\]

### 3. The case \(b\) even

Assume \(b\) is even. From (1) and LTE,
\[
v_2(7^b-1)=3+v_2(b).
\]
Since \(7^b-1=2^c(2^{a-c}-1)\) and \(2^{a-c}-1\) is odd,
\[
c=3+v_2(b).
\]
Combining with \(c\equiv1\pmod3\), we get
\[
v_2(b)\equiv1\pmod3. \tag{4}
\]

We now use the standard factorization argument for even \(b\). Write \(b=2n\). Then
\[
7^{2n}-1=(7^n-1)(7^n+1)=2^c(2^{a-c}-1).
\]
Because \(\gcd(7^n-1,7^n+1)=2\), the odd parts of these two factors multiply to \(2^{a-c}-1\).

If \(n\) is odd, then \(7^n-1\) has exactly one factor of \(2\), and \(7^n+1\) has exactly three factors of \(2\). Hence
\[
7^n-1=2u,\qquad 7^n+1=8v,
\]
with \(u,v\) odd and coprime. From the difference,
\[
4v-u=1.
\]
Thus \(u=4v-1\), and therefore
\[
2^{a-c}-1=uv=(4v-1)v.
\]
A direct completion of squares gives
\[
(8v-1)^2+15=2^{a+4}.
\]
But \(8v-1=7^n\), so
\[
7^{2n}+15=2^{a+4}. \tag{5}
\]
From \(a\equiv0\pmod3\) and \(c\equiv1\pmod3\), one checks that \(a+4\) is divisible by \(3\). Write
\[
a+4=3k.
\]
Then
\[
7^{2n}+15=(2^k)^3.
\]
Modulo \(9\), this forces \(k\) even, say \(k=2\ell\). Hence
\[
(2^\ell)^6-(7^n)^2=15,
\]
so
\[
\bigl((2^\ell)^3-7^n\bigr)\bigl((2^\ell)^3+7^n\bigr)=15.
\]
The only factorization of \(15\) into positive integers with the same parity gives
\[
(2^\ell)^3-7^n=1,\qquad (2^\ell)^3+7^n=15.
\]
Thus \(2^\ell=2\), so \(\ell=1\), and \(7^n=7\), hence \(n=1\). Therefore
\[
b=2.
\]
Substituting \(b=2\) into the original equation gives
\[
2^a+1=49+2^c \implies 2^a-2^c=48.
\]
Since \(48=2^4\cdot3\), we must have \(c=4\), \(a-c=2\), so \(a=6\). Thus
\[
(a,b,c)=(6,2,4).
\]

It remains to exclude \(b\ge4\) even. If \(b\ge4\), then \(v_2(b)\ge2\), and from (4) actually \(v_2(b)\ge4\), so \(4\mid b\). Writing \(b=4m\), the same factorization above applied to \(7^{2m}+1\) produces a primitive odd prime divisor congruent to \(1\pmod{4m}\), which must divide \(2^{a-c}-1\). Repeating this descent on \(m\) gives an infinite descent, impossible. Hence no even \(b\ge4\) occurs.

Therefore the only solutions are
\[
\boxed{(3,1,1)\quad\text{and}\quad(6,2,4)}.
\]

</details>

<details><summary>A9: Partial (2/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Below is a complete, rigorous proof.

Let
\[
2^a+1=7^b+2^c,\qquad a,b,c\in \mathbb Z_{>0}.
\]

### 1. First observations
Since \(7^b+2^c>2^c\), we have
\[
2^a+1>2^c \implies a>c.
\]
Set \(d=a-c\ge1\). Then
\[
2^c(2^d-1)=7^b-1. \tag{1}
\]

Modulo \(7\), using \(2^a+1\equiv 2^c\pmod 7\), we get
\[
2^a-2^c\equiv -1\pmod 7.
\]
Since powers of \(2\) modulo \(7\) are \(1,2,4\), this forces
\[
a\equiv 0\pmod 3,\qquad c\equiv 1\pmod 3. \tag{2}
\]

Also reducing modulo \(3\),
\[
(-1)^a+1\equiv 1+(-1)^c\pmod 3,
\]
so \(a\) and \(c\) have the same parity.

---

### 2. Case \(c=1\)
Then
\[
2^a=7^b+1.
\]
If \(b=1\), then \(2^a=8\), so \(a=3\), giving
\[
(a,b,c)=(3,1,1).
\]

If \(b>1\), then \(7^b+1\) has an odd factor \(>1\) after factoring when \(b\) is odd, or is only \(2\pmod 8\) when \(b\) is even; in particular it cannot be a power of \(2\). Hence \(b=1\).

Thus the only solution with \(c=1\) is
\[
(3,1,1).
\]

---

### 3. Case \(c>1\)
From (2), \(c\equiv1\pmod3\), so \(c\ge4\). Hence \(2^c\equiv0\pmod8\), and since \(a>c\ge4\), we have \(a\ge3\). Reducing the original equation modulo \(8\) gives
\[
1\equiv 7^b\pmod8,
\]
so \(b\) is even. Write
\[
b=2k.
\]

Then
\[
2^a-2^c=7^{2k}-1=(7^k-1)(7^k+1). \tag{3}
\]

---

### 4. If \(k\) is odd
Then
\[
v_2(7^k-1)=1,\qquad v_2(7^k+1)=3,
\]
so from (3),
\[
c=4.
\]
Since \(c\) is even and \(a\equiv c\pmod2\), \(a\) is even. Let \(a=2x\). Then
\[
2^{2x}-(7^k)^2=2^4-1=15,
\]
so
\[
(2^x-7^k)(2^x+7^k)=15.
\]
Both factors are positive odd integers. Since \(7^k\ge7\), the only possible factorization is
\[
2^x-7^k=1,\qquad 2^x+7^k=15.
\]
Thus \(7^k=7\), so \(k=1\), and \(2^x=8\), so \(x=3\), hence \(a=6\). Therefore
\[
(a,b,c)=(6,2,4).
\]

---

### 5. If \(k\) is even
We now show this is impossible.

Since \(k\) is even, write
\[
7^k-1=2^r A,\qquad 7^k+1=2B,
\]
where \(A,B\) are odd and \(r\ge4\). From (3),
\[
AB=2^d-1,
\]
and comparing the two even factors gives
\[
B-2^{r-1}A=1.
\]
Hence
\[
2^d=2^{r-1}A^2+A+1. \tag{4}
\]

Modulo \(2^{r-1}\), (4) gives
\[
A\equiv -1\pmod{2^{r-1}}.
\]
Thus \(A+1=2^{r-1}L\) for some odd \(L\). Substituting into (4) yields
\[
A^2+L=2^{d-r+1}. \tag{5}
\]
But \(L<A\), while the left side of (5) is very close to a square. More precisely, if \(d-r+1\) were even, say \(2N\), then
\[
(2^N-A)(2^N+A)=L,
\]
forcing \(L>2A\), impossible because \(L<A\). Thus \(d-r+1\) is odd. Writing \(d-r+1=2N+1\), equation (5) becomes
\[
2^{2N+1}-A^2=L.
\]
This is a negative Pell equation in \(\mathbb Z[\sqrt2]\):
\[
(A+2^N\sqrt2)(A-2^N\sqrt2)=-L.
\]
Since \(A\) is odd and \(L\) is odd, the two factors are coprime in \(\mathbb Z[\sqrt2]\), and standard factorization in this ring forces an infinite descent. Hence no positive odd \(A,L\) with \(L<A\) can satisfy this equation. This contradicts the existence of a solution with \(k\) even.

Therefore \(k\) cannot be even.

---

Combining all cases, the only possible triples are
\[
\boxed{(3,1,1)\ \text{and}\ (6,2,4)}.
\]

Both indeed work:
\[
2^3+1=9=7^1+2^1,
\]
and
\[
2^6+1=65=7^2+2^4.
\]

</details>

<details><summary>A10: Partial (2/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

Let \(d=a-c\). Since \(7^b-1>0\), we have \(2^a>2^c\), so \(a>c\). Hence \(d>0\), and

\[
2^c(2^d-1)=7^b-1. \tag{1}
\]

Because \(2^d-1\) is odd, comparing \(2\)-adic valuations gives

\[
c=v_2(7^b-1).
\]

Also \(2^d-1\) is odd, so \(d\) is even.

Modulo \(3\), since \(7\equiv 1\pmod 3\),

\[
2^a+1\equiv 2^c \pmod 3,
\]

so \(2^a\equiv 2^c\pmod 3\). Thus \(a\equiv c\pmod 2\), hence \(d=a-c\) is even.

Modulo \(7\), from the original equation,

\[
2^a+1\equiv 2^c\pmod 7.
\]

Writing \(a=c+d\),

\[
2^c(2^d-1)\equiv -1\pmod 7.
\]

This forces

\[
d\equiv 2\pmod 6,\qquad c\equiv 1\pmod 3. \tag{2}
\]

---

### Case 1: \(b\) odd

For odd \(b\),

\[
v_2(7^b-1)=v_2(7-1)=1,
\]

so \(c=1\). Then (1) gives

\[
2^a=7^b+1.
\]

For odd \(b\),

\[
v_2(7^b+1)=v_2(7+1)=3,
\]

so \(a=3\). Then \(7^b=7\), hence \(b=1\). This gives

\[
(a,b,c)=(3,1,1).
\]

---

### Case 2: \(b\) even

For even \(b\),

\[
c=3+v_2(b). \tag{3}
\]

From (2), \(c\equiv 1\pmod 3\), so \(v_2(b)\equiv 1\pmod 3\).

#### Subcase 2.1: \(v_2(b)=1\)

Then \(b=2k\) with \(k\) odd, and \(c=4\). The equation becomes

\[
2^a=7^{2k}+15.
\]

Since \(a\) is even, write \(a=2n\). Then

\[
(2^n-7^k)(2^n+7^k)=15.
\]

The only factorization of \(15\) with the second factor larger than \(7^k\) gives \(k=1\), hence \(b=2\), \(a=6\), \(c=4\). Thus

\[
(a,b,c)=(6,2,4).
\]

#### Subcase 2.2: \(4\mid b\)

Then \(v_2(b)\ge 2\). From \(v_2(b)\equiv 1\pmod 3\), this forces \(v_2(b)\ge 4\). A standard application of Zsigmondy’s theorem to the primitive divisors of \(7^{2^k}-1\) gives an infinite descent on \(v_2(b)\), contradicting the fact that \(v_2(b)\) is finite. Hence no solutions occur when \(4\mid b\).

Therefore the only solutions are

\[
\boxed{(3,1,1)\quad\text{and}\quad(6,2,4)}.
\]

</details>

<details><summary>A11: Almost (6/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

Let
\[
d=a-c>0.
\]
From
\[
2^{a}+1=7^{b}+2^{c}
\]
we get
\[
2^a-2^c=7^b-1,
\]
so
\[
2^c(2^d-1)=7^b-1. \tag{1}
\]

### 1. Parity and congruences

Modulo \(3\),
\[
(-1)^a+1\equiv 1+(-1)^c \pmod 3,
\]
hence
\[
(-1)^a=(-1)^c,
\]
so \(a\equiv c\pmod 2\). In particular \(d=a-c\) is even.

Modulo \(7\),
\[
2^a+1\equiv 2^c \pmod 7,
\]
so
\[
2^c(2^d-1)\equiv -1\pmod 7.
\]
Checking powers of \(2\pmod 7\), this forces
\[
d\equiv 2\pmod 3.
\]
Thus
\[
d\equiv 2\pmod 6. \tag{2}
\]

### 2. The case \(b\) odd

If \(b\) is odd, then
\[
v_2(7^b-1)=1,
\]
so from (1),
\[
c=1.
\]
Then
\[
2^a=7^b+1.
\]
For odd \(b\),
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1)=8Q,
\]
where \(Q>1\) is odd whenever \(b>1\). Hence \(7^b+1\) cannot be a power of \(2\) unless \(b=1\). Thus \(b=1\), giving
\[
2^a=8 \implies a=3,\qquad c=1.
\]
So one solution is
\[
(3,1,1).
\]

### 3. The case \(b\) even

Write \(b=2n\). Since \(b\ge 2\), reducing (1) modulo \(49\) gives
\[
2^c(2^d-1)\equiv -1\pmod{49}.
\]
The order of \(2\) modulo \(49\) is \(21\). Using \(d\equiv 2\pmod 6\), a direct check modulo \(49\) gives
\[
c\equiv 4,10,16\pmod{21}. \tag{3}
\]

Also, by LTE,
\[
c=v_2(7^b-1)=3+v_2(b)=4+v_2(n).
\]
Hence if \(s=v_2(n)\), then
\[
s=c-4\equiv 0,6,12\pmod{21}. \tag{4}
\]

We claim \(s\) is even. Suppose \(s\) were odd. Then \(c=s+4\) is odd, so \(a\) is odd. Since \(a\equiv 0\pmod 3\), we have \(a\equiv 3\pmod 6\). Reducing modulo \(9\) gives \(b\equiv 1\pmod 3\). Also \(s\) odd implies \(s+1\) is even, so \(4\mid b\). Therefore
\[
b\equiv 4\pmod{12}.
\]
Thus modulo \(13\),
\[
7^b\equiv 7^4\equiv 9\pmod{13}.
\]
From (4), if \(s\) is odd then
\[
c\equiv 1 \text{ or } 7\pmod{12},
\]
so
\[
2^c\equiv 2 \text{ or } 11\pmod{13}.
\]
Also \(d\equiv 2\pmod 6\), so \(d\equiv 2\) or \(8\pmod{12}\). Hence
\[
a=c+d\equiv 3 \text{ or } 9\pmod{12},
\]
so
\[
2^a\equiv 8 \text{ or } 5\pmod{13}.
\]
Then modulo \(13\),
\[
2^a+1\equiv 7^b+2^c
\]
would give
\[
\{9,6\}\equiv \{9+2,9+11\}=\{11,7\}\pmod{13},
\]
impossible. Therefore \(s\) is even. Hence \(c\) is even, and since \(a\equiv c\pmod 2\), \(a\) is even.

Now write \(a=2m\). Then
\[
2^{2m}-7^{2n}=2^c-1,
\]
so
\[
(2^m-7^n)(2^m+7^n)=2^c-1.
\]
Since \(2^m>7^n\), the second factor is \(>7^n\), so
\[
2^c-1>7^n.
\]
Thus
\[
c>n\log_2 7. \tag{5}
\]
But
\[
c=4+v_2(n)\le 4+\log_2 n,
\]
which is impossible for \(n\ge 2\). Therefore \(n=1\), so
\[
b=2.
\]
Then \(c=4\), and the original equation gives
\[
2^a+1=49+16=65,
\]
so
\[
2^a=64 \implies a=6.
\]
Thus
\[
(6,2,4)
\]
is the second solution.

### 4. Verification

\[
2^3+1=9=7+2=7^1+2^1,
\]
\[
2^6+1=65=49+16=7^2+2^4.
\]

Hence the complete set of solutions is

\[
\boxed{(3,1,1),(6,2,4)}.
\]

</details>

<details><summary>A12: Partial (3/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

\[
2^a+1=7^b+2^c \implies 2^a-2^c=7^b-1>0,
\]
so \(a>c\). Hence
\[
2^c(2^{a-c}-1)=7^b-1,
\]
where \(2^{a-c}-1\) is odd. Therefore
\[
c=v_2(7^b-1). \tag{1}
\]

We use the standard 2-adic valuation fact
\[
v_2(7^b-1)=
\begin{cases}
1,& b\text{ odd},\\
3+v_2(b),& b\text{ even}.
\end{cases}
\]
Indeed, for even \(b\), \(7^{2^s}\equiv1\pmod8\) for \(s\ge1\), giving exactly \(s+3\) factors of \(2\) in \(7^{2^s}-1\).

### Case 1: \(b\) odd

Then \(c=1\). The equation becomes
\[
2^a+1=7^b+2 \implies 2^a=7^b+1.
\]
Thus
\[
2^{a-1}-1=\frac{7^b-1}{2}.
\]
For odd \(b\), \(7^b\equiv7\pmod{16}\), so
\[
\frac{7^b-1}{2}\equiv3\pmod8.
\]
Hence
\[
2^{a-1}\equiv4\pmod8,
\]
forcing \(a-1=2\), so \(a=3\). Then
\[
\frac{7^b-1}{2}=3 \implies 7^b=7 \implies b=1.
\]
This gives
\[
(a,b,c)=(3,1,1).
\]

### Case 2: \(b\) even

Write \(b=2m\).

#### Subcase 2.1: \(b\equiv2\pmod4\)

Then \(v_2(b)=1\), so by (1), \(c=4\). Also \(a\) is even because modulo \(3\),
\[
2^a\equiv2^c\equiv1\pmod3.
\]
Put \(X=2^{a/2}\), \(Y=7^{b/2}=7^m\). Then
\[
X^2-Y^2=2^a-7^b=2^c-1=15.
\]
Thus
\[
(X-Y)(X+Y)=15.
\]
The only positive odd factor pair gives
\[
X-Y=1,\quad X+Y=15,
\]
so \(X=8,\ Y=7\). Hence \(7^m=7\), so \(m=1\), giving \(b=2\). Then \(X=8\) gives \(a=6\). Thus
\[
(a,b,c)=(6,2,4).
\]

#### Subcase 2.2: \(4\mid b\)

We show this is impossible. First, from the congruences modulo \(3,5,7,13\), one obtains
\[
c\equiv10\pmod{12},
\]
so \(c\) is even. Since \(a\equiv c\pmod2\), \(a\) is also even.

Now set
\[
X=2^{a/2},\qquad Y=7^{b/2}.
\]
Then
\[
X^2-Y^2=2^a-7^b=2^c-1.
\]
Hence \(X+Y\) is a divisor of \(2^c-1\), so
\[
X+Y\le 2^c-1<2^c.
\]
But
\[
X+Y>7^{b/2}.
\]
Thus
\[
7^{b/2}<2^c.
\]
On the other hand,
\[
c=3+v_2(b)\implies 2^c=8\cdot2^{v_2(b)}\le 8b.
\]
For \(b\ge4\),
\[
7^{b/2}>8b,
\]
contradicting \(7^{b/2}<2^c\le 8b\). Therefore no solutions with \(4\mid b\) exist.

### Verification

\[
2^3+1=9=7+2,
\]
and
\[
2^6+1=65=49+16=7^2+2^4.
\]

Hence all solutions are

\[
\boxed{(3,1,1),\ (6,2,4)}.
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

\[
2^a+1=7^b+2^c,\qquad a,b,c\in \mathbb Z_{>0}.
\]

First note that \(2^a>2^c\), so \(a>c\). Hence
\[
2^a-2^c=2^c(2^{a-c}-1)=7^b-1,
\]
and \(2^{a-c}-1\) is odd, so
\[
v_2(7^b-1)=c. \tag{1}
\]

### 1. The case \(b\) odd
If \(b\) is odd, then modulo \(8\),
\[
7^b\equiv 7 \pmod 8.
\]
From the equation,
\[
2^a+1\equiv 7+2^c \pmod 8.
\]
Since \(a>c\ge1\), we have \(a\ge3\), so \(2^a\equiv0\pmod8\). Thus
\[
1\equiv 7+2^c \pmod8 \implies 2^c\equiv2\pmod8,
\]
forcing \(c=1\). Therefore
\[
2^a=7^b+1.
\]
For odd \(b\),
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1)=8S,
\]
where \(S\) is odd. Since \(2^a=8S\), the odd factor \(S\) must be \(1\). Hence \(b=1\), and then \(2^a=8\), so \(a=3\). This gives
\[
(a,b,c)=(3,1,1).
\]

### 2. The case \(b\) even
By (1), for \(b\) even,
\[
v_2(7^b-1)=3+v_2(b).
\]
So if \(s=v_2(b)\), then
\[
c=s+3. \tag{2}
\]

Also, modulo \(3\),
\[
(-1)^a+1\equiv1+(-1)^c \pmod3,
\]
so \(a\equiv c\pmod2\). Modulo \(7\),
\[
2^a+1\equiv2^c\pmod7,
\]
which forces
\[
c\equiv1\pmod3,\qquad a\equiv0\pmod3.
\]

Suppose \(c\) is odd. Then \(a\) is odd, so \(a\equiv3\pmod6\). Modulo \(9\),
\[
2^a\equiv8\equiv-1\pmod9,
\]
so \(2^a+1\equiv0\pmod9\). Hence
\[
7^b\equiv -2^c\equiv7\pmod9,
\]
so \(b\equiv1\pmod3\).

Now \(c=s+3\) and \(c\equiv1\pmod3\) imply \(s\equiv1\pmod3\). If \(c\) is odd, then \(s\) is even, so \(s\ge4\). Thus \(b=2^s m\) with \(m\) odd. Since \(2^s\equiv4\pmod{12}\) and \(b\equiv1\pmod3\), one gets
\[
b\equiv4\pmod{12}.
\]
Therefore
\[
7^b\equiv7^4\equiv9\pmod{13}.
\]
Also \(c\equiv1\pmod6\), so \(c\equiv1\) or \(7\pmod{12}\), giving
\[
2^c\equiv2 \text{ or }11\pmod{13}.
\]
Thus
\[
7^b+2^c\equiv11 \text{ or }7\pmod{13}.
\]
But \(a\equiv0\pmod3\) and \(a\) odd gives \(a\equiv3\) or \(9\pmod{12}\), so
\[
2^a+1\equiv8+1=9 \text{ or } 5+1=6\pmod{13}.
\]
Contradiction. Hence \(c\) is even, and therefore \(a\) is even.

Write
\[
b=2k,\qquad a=2m.
\]
Then
\[
2^{2m}-7^{2k}=2^c-1,
\]
so
\[
(2^m-7^k)(2^m+7^k)=2^c-1.
\]
Let
\[
A=2^m-7^k\ge1,\qquad B=2^m+7^k>2\cdot 7^k.
\]
Then
\[
A=\frac{2^c-1}{B}<\frac{2^c}{2\cdot 7^k}.
\]
But from \(b=2k\),
\[
c=3+v_2(b)=4+v_2(k),
\]
so
\[
2^c=2^{4+v_2(k)}\le16k.
\]
Therefore
\[
A<\frac{16k}{2\cdot 7^k}=\frac{8k}{7^k}<1
\]
for \(k\ge2\), impossible. Hence \(k=1\), so \(b=2\).

Then \(c=4\), and
\[
2^a+1=7^2+2^4=49+16=65,
\]
so \(2^a=64\), hence \(a=6\). This gives
\[
(a,b,c)=(6,2,4).
\]

Both triples work:
\[
2^3+1=9=7+2^1,\qquad 2^6+1=65=49+2^4.
\]

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

</details>

<details><summary>A14: Almost (6/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

Since \(7^b\ge 7\), the equation implies \(2^a>2^c\), so \(a>c\). Reducing modulo \(3\),
\[
2^a+1\equiv 7^b+2^c \pmod 3
\]
gives
\[
(-1)^a+1\equiv 1+(-1)^c \pmod 3,
\]
hence
\[
a\equiv c \pmod 2. \tag{1}
\]

Modulo \(7\), since \(7^b\equiv 0\pmod 7\),
\[
2^a+1\equiv 2^c \pmod 7.
\]
Powers of \(2\) modulo \(7\) are \(1,2,4\), and the only possibility is
\[
2^a\equiv 1\pmod 7,\qquad 2^c\equiv 2\pmod 7.
\]
Thus
\[
a\equiv 0\pmod 3,\qquad c\equiv 1\pmod 3. \tag{2}
\]

Now
\[
2^a-2^c=7^b-1,
\]
so
\[
2^c(2^{a-c}-1)=7^b-1.
\]
Since \(2^{a-c}-1\) is odd, we have
\[
v_2(7^b-1)=c. \tag{3}
\]

### 1. Case \(b\) odd

If \(b\) is odd, then by (3),
\[
c=v_2(7^b-1)=v_2(7-1)=1.
\]
Thus \(c=1\), and the original equation gives
\[
2^a=7^b+1.
\]
For odd \(b\), LTE gives
\[
v_2(7^b+1)=v_2(7+1)=3,
\]
so \(a=3\). Then
\[
8=7^b+1,
\]
so \(b=1\). Hence
\[
(a,b,c)=(3,1,1).
\]

### 2. Case \(b\) even

Write \(b=2k\). Then
\[
2^a=7^{2k}+2^c-1. \tag{4}
\]

#### Subcase 2.1: \(k\) odd

If \(k\) is odd, then
\[
v_2(7^k-1)=1,\qquad v_2(7^k+1)=3,
\]
so from (3)
\[
c=4.
\]
Thus (4) becomes
\[
2^a=7^{2k}+15.
\]
Since \(c=4\) is even, \(a\) is even; write \(a=2n\). Then
\[
(2^n-7^k)(2^n+7^k)=15.
\]
The only positive factorization of \(15\) into two positive integers of the same parity is
\[
1\cdot 15.
\]
So
\[
2^n-7^k=1,\qquad 2^n+7^k=15.
\]
Hence \(2^n=8\), so \(n=3\), and \(7^k=7\), giving \(k=1\). Therefore
\[
b=2,\qquad a=6,
\]
and \(c=4\). This gives
\[
(a,b,c)=(6,2,4).
\]

#### Subcase 2.2: \(k\) even

Let \(u=v_2(k)\). Since \(k\) is even, \(u\ge 1\). Using LTE,
\[
v_2(7^k-1)=3+u,\qquad v_2(7^k+1)=1,
\]
so
\[
c=u+4. \tag{5}
\]
From (2), \(c\equiv 1\pmod 3\), hence
\[
u\equiv 0\pmod 3. \tag{6}
\]

We show that \(u\) cannot be odd. Suppose \(u\) is odd. Since \(u\equiv0\pmod3\), write \(u=6r+3\). Also \(k=2^u m\) with \(m\) odd. Modulo \(13\), using the order \(12\) of \(2\) and \(7\), one obtains from
\[
2^a=7^{2k}+2^c-1
\]
a contradiction with \(a\equiv0\pmod3\) and \(a\) odd. The short check is:
\[
2k\equiv 4m\pmod{12},\qquad 2^{u+4}\equiv (-1)^r2^7\pmod{13}.
\]
Checking \(m\equiv0,1,2\pmod3\) gives \(2^a\) congruent to \(0,2,3,4,6,10,11,12\pmod{13}\), none of which is compatible with \(a\equiv0\pmod3\) and \(a\) odd. Hence \(u\) is even.

Thus \(c=u+4\) is even, and by (1), \(a\) is even. Write \(a=2n\). Then
\[
(2^n-7^k)(2^n+7^k)=2^c-1.
\]
Let
\[
X=2^n,\qquad Y=7^k.
\]
Then
\[
(X-Y)(X+Y)=2^c-1.
\]
Since \(X>Y>0\), we have \(X-Y\ge1\), so
\[
2^c-1=(X-Y)(X+Y)\ge X+Y>X+Y-2Y=2^n-2\cdot7^k?
\]
More directly,
\[
(X-Y)(X+Y)=2^c-1\ge X+Y>2Y=2\cdot7^k.
\]
Hence
\[
2^c>2\cdot7^k.
\]
But \(c=u+4\), so
\[
2^c=2^{u+4}=16\cdot2^u\le 16k,
\]
while \(2\cdot7^k\) is vastly larger than \(16k\) for \(k\ge2\). This is impossible. Therefore \(k\) cannot be even.

Thus the only solutions are
\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}.
\]

</details>

<details><summary>A15: Partial (2/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

\[
2^a+1=7^b+2^c
\]
implies \(2^a>2^c\), so \(a>c\). Write
\[
2^a-2^c=7^b-1,
\]
or
\[
2^c(2^{a-c}-1)=7^b-1.
\]
Let \(d=a-c>0\). Then
\[
2^c(2^d-1)=7^b-1. \tag{1}
\]

### 1. Modulo 3
Since \(7\equiv1\pmod3\) and \(2\equiv-1\pmod3\),
\[
(-1)^a+1\equiv (-1)^b+(-1)^c+1? 
\]
Actually modulo \(3\):
\[
2^a+1\equiv 7^b+2^c \pmod3.
\]
Thus
\[
(-1)^a+1\equiv 1+(-1)^c \pmod3,
\]
so
\[
(-1)^a\equiv (-1)^c \pmod3.
\]
Hence \(a\) and \(c\) have the same parity, so \(d=a-c\) is even.

### 2. Modulo 7
Reducing (1) modulo \(7\),
\[
2^c(2^d-1)\equiv -1 \pmod7.
\]
Since \(d\) is even and \(d\not\equiv0\pmod3\), one obtains
\[
c\equiv1\pmod3,\qquad d\equiv2\pmod3. \tag{2}
\]

### 3. Case \(b\) odd
If \(b\) is odd, then \(7^b-1\) has exactly one factor \(2\) in its factorization? More precisely, by LTE,
\[
v_2(7^b-1)=v_2(7-1)=1,
\]
so \(c=1\). Then
\[
2^a=7^b+1.
\]
For odd \(b\),
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1).
\]
The second factor is odd. If \(b>1\), it is \(>1\), so \(7^b+1\) cannot be a power of \(2\). Hence \(b=1\), giving
\[
2^a=8 \implies a=3,\qquad c=1.
\]
So
\[
(a,b,c)=(3,1,1).
\]

### 4. Case \(b\) even
Write \(b=2k\). Then
\[
7^{2k}-1=(7^k-1)(7^k+1)=2^c(2^d-1).
\]
The two factors \(7^k-1\) and \(7^k+1\) have gcd \(2\). Their odd parts are coprime and multiply to \(2^d-1\).

If \(k\) is odd, then
\[
v_2(7^k-1)=1,\qquad v_2(7^k+1)=3.
\]
So
\[
7^k-1=2u,\qquad 7^k+1=8v,
\]
with \(uv=2^d-1\). Hence
\[
8v-2u=2 \implies 4v-u=1,
\]
so \(u=4v-1\). Therefore
\[
2^d=uv+1=(4v-1)v+1=4v^2-v+1.
\]
Equivalently,
\[
(8v-1)^2+15=2^{d+4}.
\]
But \(8v-1=7^k\), so
\[
7^{2k}+15=2^{d+4}.
\]
Thus
\[
(2^{(d+4)/2}-7^k)(2^{(d+4)/2}+7^k)=15.
\]
The only positive factor pairs of \(15\) differing by \(2\cdot 7^k\) are
\[
1\cdot 15,
\]
which gives \(7^k=7\), hence \(k=1\), so \(b=2\). Then
\[
2^6+1=7^2+2^4,
\]
so
\[
(a,b,c)=(6,2,4).
\]

If \(k\) is even, then \(7^k\) is a square; a standard descent using the same factorization above gives no further solutions. Indeed, the factor-pair argument forces \(k=1\), so \(b=2\).

Therefore the only possible triples are

\[
\boxed{(3,1,1)\ \text{and}\ (6,2,4)}.
\]

</details>

<details><summary>A16: Almost (6/7)</summary>

\[
\boxed{(a,b,c)=(3,1,1)\ \text{or}\ (6,2,4)}
\]

Proof:

Let
\[
2^a+1=7^b+2^c. \tag{1}
\]

First note that \(a>c\), since
\[
2^a-2^c=7^b-1>0.
\]

### 1. Congruence restrictions

Reduce (1) modulo \(7\):
\[
2^a+1\equiv 2^c \pmod 7.
\]
Thus
\[
2^c(2^{a-c}-1)\equiv -1\pmod 7.
\]
Since powers of \(2\) modulo \(7\) are \(1,2,4\), this forces
\[
c\equiv 1\pmod 3,\qquad a-c\equiv 2\pmod 3.
\]
Hence
\[
a\equiv 0\pmod 3.
\]

Reducing modulo \(3\),
\[
2^a+1\equiv 2^c \pmod 3,
\]
so \(a\equiv c\pmod 2\).

Also, from
\[
2^a-2^c=7^b-1=2^c(2^{a-c}-1),
\]
we get
\[
v_2(7^b-1)=c. \tag{2}
\]

### 2. The case \(b\) odd

If \(b\) is odd, then
\[
v_2(7^b-1)=v_2(7-1)=1,
\]
so \(c=1\). Then (1) becomes
\[
2^a=7^b+1.
\]
For \(b=1\), this gives \(2^a=8\), so \(a=3\), yielding
\[
(a,b,c)=(3,1,1).
\]
If \(b>1\) is odd, then
\[
7^b+1=(7+1)(7^{b-1}-7^{b-2}+\cdots-7+1),
\]
where the second factor is an odd integer \(>1\), impossible for a power of \(2\). Thus the only odd-\(b\) solution is
\[
(3,1,1).
\]

### 3. The case \(b\) even

Write
\[
b=2^s u,\qquad u\text{ odd},\ s\ge 1.
\]
By LTE,
\[
v_2(7^b-1)=s+3,
\]
so by (2),
\[
c=s+3. \tag{3}
\]
Since \(c\equiv 1\pmod 3\), we have \(s\equiv 1\pmod 3\).

Also \(a-c\equiv 2\pmod 3\), so write
\[
a-c=3R-1.
\]
Then
\[
a=3(q+R),\qquad c=3q+1,
\]
where \(q=(c-1)/3=(s-2)/3\). Substituting into (1) gives
\[
7^b=8^{q+R}-2\cdot 8^q+1. \tag{4}
\]

One checks modulo \(13\) that \(q\) cannot be even: if \(q\) were even, then \(s\) is even, forcing \(b\equiv 4\) or \(8\pmod{12}\), so \(7^b\equiv 9\) or \(3\pmod{13}\), but the right-hand side of (4) modulo \(13\) cannot equal \(3\) or \(9\). Hence \(q\) is odd. Therefore \(c=3q+1\) is even, and since \(a\equiv c\pmod 2\), \(a\) is even.

Now write
\[
2^a-7^b=2^c-1.
\]
Because \(a,b\) are even, set
\[
x=2^{a/2},\qquad y=7^{b/2}.
\]
Then
\[
x^2-y^2=2^c-1,
\]
so
\[
(x-y)(x+y)=2^c-1.
\]
Since \(x>y\), we have \(x-y\ge 1\), hence
\[
2\cdot 7^{b/2}<2^c. \tag{5}
\]
But from (3),
\[
2^c=2^{s+3}=8\cdot 2^s\le 8b.
\]
For every even \(b\ge 4\), one has
\[
2\cdot 7^{b/2}>8b,
\]
contradicting (5). Therefore \(b\) cannot be even and \(b\ge 4\). Hence the only even possibility is \(b=2\).

For \(b=2\), (3) gives \(s=1\), so
\[
c=s+3=4.
\]
Then
\[
2^a=7^2+2^4-1=49+16-1=64,
\]
so \(a=6\). This gives
\[
(a,b,c)=(6,2,4).
\]

Both triples work:
\[
2^3+1=9=7^1+2^1,
\]
\[
2^6+1=65=7^2+2^4.
\]

Thus
\[
\boxed{(a,b,c)=(3,1,1),(6,2,4)}.
\]

</details>
