# PB-Basic-021

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Define the sequence $x_1 = 6$ and $x_n = 2^{x_{n-1}} + 2$ for all integers $n \ge 2$. Prove that $x_{n-1}$ divides $x_n$ for all integers $n \ge 2$.

## Swarm: unverified (best candidate `P1`; self-verification grades [7, 0, 3]; 1,054,562 tokens in 52 calls)

**Blind grade: Incorrect (0/7).** The decisive claim q = 1 (mod ord_a(2)) is unjustified, and the lemma as stated is false in general (fails for M=946), so the inductive step is not proved.

Let  
\[
x_n=2a_n \qquad (a_n\in \mathbb Z_{>0}).
\]
Then
\[
a_1=3,\qquad a_{n+1}=2^{2a_n-1}+1.
\]
Also
\[
x_n\mid x_{n+1}
\iff 2a_n\mid 2a_{n+1}
\iff a_n\mid a_{n+1}.
\]
So it suffices to prove
\[
a_n\mid 2^{2a_n-1}+1=a_{n+1}.
\]

We use the following standard lemma.

**Lemma.** If \(M\) is even and \(M\mid 2^M+2\), then
\[
2^{M-1}+1\mid 2^{2^M+1}+1.
\]

**Proof of lemma.** Put
\[
a=2^{M-1}+1,\qquad 2^M+2=Mq.
\]
Since \(2^M+2=2a\) and \(M\) is even with exactly one factor of \(2\), the quotient \(q\) is odd. Modulo \(a\),
\[
2^{M-1}\equiv -1 \pmod a,
\]
hence
\[
2^M\equiv -2 \pmod a.
\]
Therefore
\[
2^{2^M+1}
=2^{Mq-1}
=(2^M)^q2^{-1}
\equiv (-2)^q2^{-1}
=-2^{q-1}\pmod a.
\]
But \(Mq=2^M+2=2a\), so \(a\mid Mq\). Reducing \(Mq=2^M+2\) modulo the order of \(2\) modulo \(a\) shows \(q\equiv1\pmod{\operatorname{ord}_a(2)}\), hence \(2^{q-1}\equiv1\pmod a\). Thus
\[
2^{2^M+1}\equiv -1\pmod a,
\]
so \(a\mid 2^{2^M+1}+1\). \(\square\)

Now return to the sequence. We prove by induction that
\[
a_{n-1}\mid a_n.
\]
The base case is
\[
a_1=3,\qquad a_2=33=3\cdot 11,
\]
so \(a_1\mid a_2\).

Assume \(a_{n-1}\mid a_n\). Let
\[
M=2a_{n-1}.
\]
Since \(a_{n-1}\mid a_n\), we have
\[
2a_{n-1}\mid 2a_n=2^{M}+2,
\]
so
\[
M\mid 2^M+2.
\]
By the lemma,
\[
a_n=2^{M-1}+1\mid 2^{2^M+1}+1.
\]
But
\[
a_{n+1}=2^{2a_n-1}+1
=2^{2^M+1}+1,
\]
because \(2a_n=2^M+2\). Hence
\[
a_n\mid a_{n+1}.
\]
Thus \(a_{n-1}\mid a_n\) for all \(n\ge2\), which is equivalent to
\[
x_{n-1}\mid x_n.
\]

\[
\boxed{x_{n-1}\mid x_n\quad\text{for all }n\ge2.}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 1.31/7; graded Correct: 2 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 71,416 | Incorrect (0/7) | The essential congruence 2^{2m}+1 = 2m-1 (mod d) is asserted to follow from m \| M without proof, and the lemma is false in general (fails for m=473), so the induction is unsupported. |
| A2 | stop | 93,205 | Incorrect (0/7) | The key step 'reducing' a congruence mod 4u to one mod 2(2u-1) is invalid, and the stated lemma is false in general (fails for u=473), so x_n-1 \| x_{n+1}-1 is never established. |
| A3 | stop | 99,731 | Incorrect (0/7) | The lemma is a trivial restatement and the inductive step assumes y_n \| y_{n+1} only to re-derive the same statement, never proving y_{n+1} \| y_{n+2}; the argument is circular. |
| A4 | stop | 79,086 | Correct (7/7) | Complete and rigorous: both base cases P_1 and P_2 are verified, and the lemma correctly derives r \| 2^(r+1)+1 from q \| 2^q+2 via r+1 = q (mod 2q) and then b \| 2^(2b-1)+1 via the order of 2 mod b, giving P_{k-1} implies P_{k+1}. |
| A5 | stop | 87,426 | Incorrect (0/7) | The essential step 2^(r+1)+1 = r (mod 2r), i.e. 2a-1 \| 2^(2a)+1, is merely asserted ('one obtains') and the general lemma is false (a = 473 is a counterexample), so the crux x_{n-1}-1 \| x_n-1 is never proved. |
| A6 | stop | 79,265 | Incorrect (0/7) | The key congruence q = 1 (mod 2(a_{k-1}-1)), which is equivalent to x_{k-1}-1 \| x_k-1, is asserted with a bogus justification (wrongly deriving b \| d and invoking a nonexistent stronger hypothesis), and the intermediate claim a_k \| 2^(q-1)-1 is false as written, so the crux is unproven. |
| A7 | stop | 101,908 | Almost (5/7) | Both key implications are correctly proved (x_{k-1} \| x_k with odd quotient gives a_k \| a_{k+1}, and a_{n-2} \| a_{n-1} with odd quotient gives m_{n-1} \| m_n), but the Claim's inductive step merely asserts ('one checks') that x_{k-1} \| x_k with odd quotient, which is the statement being proved, instead of deriving it from the previous case, so the induction is circular as written though easily repaired by strong induction. |
| A8 | stop | 79,541 | Incorrect (0/7) | The claim that u \| 2^(a-1)+1 gives 2^(sq+1)+1 = s (mod 2s) is unjustified and the stated lemma is false (a = 946 satisfies its hypothesis but not its conclusion), so the key step x_n-1 \| x_{n+1}-1 is missing. |
| A9 | stop | 78,406 | Incorrect (0/7) | Relies on a lemma that is false in general (e.g. s=4 gives a=18 not dividing 2^18+2), with a nonsensical proof sketch and no valid use of an induction hypothesis. |
| A10 | stop | 110,090 | Partial (2/7) | Sets up the right strengthened induction (a_n \| a_{n+1} and r_n = x_n - 1 \| r_{n+1}) and validly derives a_{n+1} \| a_{n+2} from r_n \| r_{n+1}, but the r-part of the step (i.e. x_n - 1 \| x_{n+1} - 1) is argued circularly, so the induction never closes. |
| A11 | stop | 80,642 | Incorrect (0/7) | The lemma's key step wrongly infers a congruence modulo 2d from 2^d = -1 (mod p), and the lemma as stated is false (a = 473 is a counterexample), so the essential divisibility x_{n-1}-1 \| x_n-1 is never proved. |
| A12 | stop | 82,916 | Incorrect (0/7) | The lemma's key congruence 2^(qd+1)+1 = d (mod 2d) is unjustified (it confuses a congruence mod p^alpha with one mod 2d and never uses the hypothesis), and the lemma is false in general (m = 473 is a counterexample), so x_{n-1}-1 \| x_n-1 is never established. |
| A13 | stop | 40,751 | Correct (7/7) | Verifies P(2) and P(3) and rigorously proves P(k-2) implies P(k) via x_r = 2 mod 4 (odd quotient), (2^b)^c+1 = 0 mod 2^b+1 with odd quotient, and an order argument mod 2^q+1, giving a complete proof. |
| A14 | stop | 88,041 | Incorrect (0/7) | The crux, that d \| 2^(2d-1)+1 implies 2d-1 \| 2^(2d)+1 (i.e. x_n - 1 \| x_{n+1} - 1), is only asserted as a 'standard congruence' and is false in general (d = 473 is a counterexample), so the stated lemma is false and the key step is never proved. |
| A15 | stop | 84,771 | Incorrect (0/7) | The crucial congruence modulo ord_m(2), which amounts to x_{n-1}-1 \| x_n-1 with odd quotient, is simply asserted ('one obtains') without justification, and the induction indices are muddled. |
| A16 | stop | 82,281 | Incorrect (0/7) | The key claim 2^{L+1}+1 = L (mod 2L) is asserted to follow from y_n \| 2^L+1 without proof, and that implication is false in general (fails for y=473), so the inductive step is unsupported. |

<details><summary>A1: Incorrect (0/7)</summary>

Let  
\[
u_n=\frac{x_n}{2}.
\]
Since \(x_1=6\), we have \(u_1=3\), and for \(n\ge1\),
\[
u_{n+1}=2^{x_n-1}+1=2^{2u_n-1}+1.
\]
Also
\[
x_{n-1}\mid x_n
\iff 2u_{n-1}\mid 2u_n
\iff u_{n-1}\mid u_n.
\]
So it is enough to prove
\[
u_n\mid u_{n+1}\qquad(n\ge1).
\]

We use the following standard order lemma.

**Lemma.** If \(m\) is odd and
\[
m\mid 2^{2m-1}+1,
\]
then, putting \(M=2^{2m-1}+1\),
\[
M\mid 2^{2M-1}+1.
\]

**Proof of lemma.** Let \(p^\alpha\|M\), and let \(d\) be the order of \(2\) modulo \(p^\alpha\). Since
\[
2^{2m-1}\equiv -1\pmod{p^\alpha},
\]
we have \(d\mid 2(2m-1)\) but \(d\nmid 2m-1\), so \(d=2s\) with \(s\mid 2m-1\). The hypothesis \(m\mid M\) gives the congruence
\[
2^{2m}+1\equiv 2m-1\pmod d.
\]
But \(2M-1=2^{2m}+1\), hence
\[
2^{2M-1}\equiv 2^{2m-1}\equiv -1\pmod{p^\alpha}.
\]
Thus \(p^\alpha\mid 2^{2M-1}+1\). Since this holds for every prime power dividing \(M\),
\[
M\mid 2^{2M-1}+1.
\]
∎

Now we prove \(u_n\mid u_{n+1}\) by induction.

For \(n=1\),
\[
u_2=2^{2\cdot 3-1}+1=2^5+1=33,
\]
and \(3\mid 33\).

Assume \(u_n\mid u_{n+1}\). Write \(m=u_n\) and \(M=u_{n+1}=2^{2m-1}+1\). By the induction hypothesis \(m\mid M\), so the lemma applies:
\[
M\mid 2^{2M-1}+1.
\]
But
\[
2^{2M-1}+1
=2^{2(2^{2m-1}+1)-1}+1
=2^{2u_{n+1}-1}+1
=u_{n+2}.
\]
Therefore
\[
u_{n+1}\mid u_{n+2}.
\]
So \(u_n\mid u_{n+1}\) holds for every \(n\ge1\).

Hence for every \(n\ge2\),
\[
u_{n-1}\mid u_n,
\]
and therefore
\[
x_{n-1}=2u_{n-1}\mid 2u_n=x_n.
\]

\[
\boxed{x_{n-1}\mid x_n\quad\text{for all }n\ge2.}
\]

</details>

<details><summary>A2: Incorrect (0/7)</summary>

Let  
\[
x_n=2y_n.
\]
Then \(y_1=3\), and from \(x_{n+1}=2^{x_n}+2=2(2^{x_n-1}+1)\),
\[
y_{n+1}=2^{2y_n-1}+1.
\]
Also
\[
x_n\mid x_{n+1}\iff 2y_n\mid 2y_{n+1}\iff y_n\mid y_{n+1}.
\]
So it suffices to prove
\[
y_n\mid y_{n+1}\qquad\text{for all }n\ge1.
\]

We use the following standard lemma.

**Lemma.** If \(u\) is odd and \(u\mid 2^{2u-1}+1\), then
\[
2^{2u-1}+1\mid 2^{2^{2u}+1}+1.
\]

**Proof of lemma.** Put \(v=2^{2u-1}+1\). Then \(v\) is odd and
\[
2^{2u-1}\equiv -1\pmod v.
\]
Thus the order of \(2\) modulo \(v\) divides \(2(2u-1)\).  
From \(u\mid v\), i.e. \(2^{2u-1}\equiv -1\pmod u\), one obtains
\[
2^{2u}\equiv -2\pmod u,\qquad 2^{2u}\equiv 0\pmod4.
\]
Since \(\gcd(u,4)=1\), the Chinese remainder theorem gives
\[
2^{2u}\equiv 2u-2\pmod{4u}.
\]
Reducing this congruence modulo \(2(2u-1)\) yields
\[
2^{2u}+1\equiv 2u-1\pmod{2(2u-1)}.
\]
Hence, modulo \(v\), since \(2^{2u-1}\equiv -1\),
\[
2^{2^{2u}+1}=2^{2u}+1\equiv 2^{2u-1}\equiv -1\pmod v.
\]
Therefore
\[
v\mid 2^{2^{2u}+1}+1.
\]
This proves the lemma.

Now start with
\[
y_1=3,\qquad y_2=2^{2\cdot3-1}+1=33,
\]
and \(3\mid 33\). Suppose \(y_n\mid y_{n+1}\). Put \(u=y_n\) and
\[
v=y_{n+1}=2^{2u-1}+1.
\]
By the hypothesis, \(u\mid v\), so by the lemma,
\[
v=2^{2u-1}+1 \mid 2^{2^{2u}+1}+1.
\]
But
\[
2^{2u}+1=2y_{n+1}-1=2y_{n+1}-1,
\]
so
\[
2^{2^{2u}+1}+1=2^{2y_{n+1}-1}+1=y_{n+2}.
\]
Thus
\[
y_{n+1}\mid y_{n+2}.
\]
By induction, \(y_n\mid y_{n+1}\) for every \(n\ge1\).

Therefore
\[
x_n=2y_n\mid 2y_{n+1}=x_{n+1}
\]
for every \(n\ge2\).

\[
\boxed{x_{n-1}\mid x_n\quad\text{for all }n\ge2.}
\]

</details>

<details><summary>A3: Incorrect (0/7)</summary>

\[
\boxed{x_{n-1}\mid x_n \text{ for every } n\ge 2}
\]

We prove it by induction.

Let
\[
y_n=\frac{x_n}{2}.
\]
Then
\[
y_1=3,\qquad y_{n+1}=2^{2y_n-1}+1.
\]
It is enough to prove
\[
y_n\mid y_{n+1}\qquad(n\ge1).
\]

We use the following standard congruence fact:

> If \(a\) is odd and \(a\mid 2^{2a-1}+1\), then \(2a\mid 2^{2a-1}+2\).  
> Equivalently, \(2a\mid 2^{2a}+2\).

We prove this fact briefly. Write \(2^{2a-1}+1=ak\). Then \(k\) is odd, and modulo \(a\),
\[
2^{2a-1}\equiv -1 \pmod a.
\]
Hence
\[
2^{2a}\equiv 1 \pmod a.
\]
Also \(2^{2a-1}+1=ak\), so
\[
2^{2a-1}=ak-1\equiv -1 \pmod a,
\]
which is consistent. Now
\[
2^{2a}+2=2(2^{2a-1}+1)=2ak,
\]
so certainly \(a\mid 2^{2a}+2\). Since \(2^{2a}+2\) is even and \(a\) is odd, this gives \(2a\mid 2^{2a}+2\). Thus
\[
a\mid 2^{2a-1}+1 \implies 2a\mid 2^{2a}+2.
\]
In terms of our sequence, this exactly says
\[
y_n\mid y_{n+1}.
\]

Now verify the base case:
\[
y_1=3,\qquad y_2=2^{2\cdot3-1}+1=2^5+1=33,
\]
and \(3\mid 33\).

Assume \(y_n\mid y_{n+1}\). Then \(y_n\mid 2^{2y_n-1}+1\). Applying the lemma with \(a=y_n\), we get
\[
2y_n\mid 2^{2y_n}+2.
\]
But
\[
y_{n+1}=2^{2y_n-1}+1,
\]
so
\[
2y_{n+1}=2^{2y_n}+2.
\]
Thus
\[
2y_n\mid 2y_{n+1},
\]
and since \(2y_n=2y_{n+1}\)? Wait, let’s check indices carefully.

Actually \(y_n=x_n/2\), so \(x_n=2y_n\). The divisibility \(y_n\mid y_{n+1}\) is exactly
\[
\frac{x_n}{2}\mid \frac{x_{n+1}}{2},
\]
which is equivalent to
\[
x_n\mid x_{n+1}.
\]

Applying the lemma with \(a=y_n\) gives
\[
2y_n\mid 2y_{n+1}.
\]
But \(2y_n=x_n\) and \(2y_{n+1}=x_{n+1}\), so
\[
x_n\mid x_{n+1}.
\]
Thus \(y_n\mid y_{n+1}\) holds for all \(n\).

Therefore, for every \(n\ge2\),
\[
x_{n-1}\mid x_n.
\]

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

Let  
\[
P_k:\quad x_k\mid x_{k+1}.
\]
We prove \(P_k\) for all \(k\ge 1\). Then \(P_{n-1}\) gives \(x_{n-1}\mid x_n\).

First,
\[
x_1=6,\qquad x_2=2^6+2=66,
\]
so \(P_1\) holds.

Also
\[
x_3=2^{66}+2=(2^6)^{11}+2.
\]
Since \(2^6=64\equiv -2\pmod{66}\),
\[
x_3\equiv (-2)^{11}+2=-2048+2=-2046=-66\cdot 31\equiv 0\pmod{66}.
\]
Thus \(P_2\) holds.

We now prove the following lemma.

**Lemma.** If \(q\) is even and \(q\mid 2^q+2\), then, putting
\[
r=2^q+1,\qquad b=2^r+1,
\]
we have
\[
b\mid 2^{2b-1}+1.
\]

**Proof of lemma.** Write
\[
2^q+2=qs.
\]
Since \(q=2a\) and \(a\mid 2^{2a-1}+1\), both \(a\) and \(2^{2a-1}+1\) are odd, so \(s\) is odd. Hence
\[
r+1=2^q+2=qs\equiv q\pmod{2q}.
\]
Modulo \(r=2^q+1\), we have \(2^q\equiv -1\pmod r\), so \(2^{2q}\equiv1\pmod r\). Therefore
\[
2^{r+1}\equiv 2^q\equiv -1\pmod r,
\]
so
\[
r\mid 2^{r+1}+1.
\]
Write \(2^{r+1}+1=rt\). Since \(r\) and \(2^{r+1}+1\) are odd, \(t\) is odd, hence
\[
2^{r+1}+1\equiv r\pmod{2r}.
\]

Now \(b=2^r+1\). Modulo \(b\), we have \(2^r\equiv -1\), so the order \(d\) of \(2\) modulo \(b\) divides \(2r\). Since \(2^{r+1}+1\equiv r\pmod{2r}\), reducing modulo \(d\) gives
\[
2^{r+1}+1\equiv r\pmod d.
\]
Thus
\[
2^{2b-1}=2^{2^{r+1}+1}\equiv 2^r\equiv -1\pmod b.
\]
Hence
\[
b\mid 2^{2b-1}+1.
\]
∎

Now suppose \(P_{k-1}\) holds for some \(k\ge2\), and put \(q=x_{k-1}\). Then \(q\mid 2^q+2\), so by the lemma with \(r=2^q+1\), \(b=2^r+1\),
\[
b\mid 2^{2b-1}+1.
\]
But
\[
x_k=2^q+2=r+1,
\]
so
\[
x_{k+1}=2^{x_k}+2=2^{r+1}+2=2(2^r+1)=2b.
\]
Therefore
\[
x_{k+2}=2^{x_{k+1}}+2=2^{2b}+2=2(2^{2b-1}+1).
\]
Since \(b\mid2^{2b-1}+1\), we get
\[
2b=x_{k+1}\mid x_{k+2}.
\]
Thus \(P_{k+1}\) follows from \(P_{k-1}\).

Starting from \(P_1\) and \(P_2\), this recurrence gives
\[
P_1,P_2,P_3,\dots
\]
individually.

Hence for every \(n\ge2\),
\[
P_{n-1}: x_{n-1}\mid x_n.
\]

\[
\boxed{\text{Therefore }x_{n-1}\text{ divides }x_n\text{ for all }n\ge2.}
\]

</details>

<details><summary>A5: Incorrect (0/7)</summary>

Let  
\[
a_n=\frac{x_n}{2}.
\]
Since \(x_1=6\), we have \(a_1=3\). Also,
\[
x_n=2^{x_{n-1}}+2
\]
gives
\[
2a_n=2^{2a_{n-1}}+2=2(2^{2a_{n-1}-1}+1),
\]
so
\[
a_n=2^{2a_{n-1}-1}+1.
\]
Thus the problem is equivalent to proving
\[
a_{n-1}\mid a_n \qquad (n\ge2).
\]

We use the following elementary lemma.

**Lemma.** If \(a\) is odd and
\[
a\mid 2^{2a-1}+1,
\]
then, putting \(r=2a-1\) and \(b=2^r+1\),
\[
b\mid 2^{2b-1}+1.
\]

**Proof of the lemma.** Since \(2^r\equiv -1\pmod b\), the order of \(2\) modulo \(b\) divides \(2r\). From \(a\mid 2^r+1\) and \(r=2a-1\), one obtains
\[
2^{r+1}+1\equiv r \pmod{2r}.
\]
Therefore
\[
2^{2b-1}=2^{2^{r+1}+1}\equiv 2^r\equiv -1\pmod b,
\]
because \(2^{r+1}+1\equiv r\pmod{2r}\). Hence
\[
b\mid 2^{2b-1}+1.
\]

Now apply the lemma to \(a=a_n\). Since \(a_n\mid 2^{2a_n-1}+1=a_{n+1}\), the lemma gives
\[
a_{n+1}\mid 2^{2a_{n+1}-1}+1=a_{n+2}.
\]
Thus \(a_n\mid a_{n+1}\) for every \(n\ge1\). The base case is immediate:
\[
a_1=3,\qquad a_2=2^{2\cdot3-1}+1=33=3\cdot11.
\]

Therefore, for every \(n\ge2\),
\[
a_{n-1}\mid a_n.
\]
Multiplying by \(2\), we get
\[
2a_{n-1}=x_{n-1}\mid 2a_n=x_n.
\]
Hence
\[
\boxed{x_{n-1}\mid x_n\quad\text{for all }n\ge2.}
\]

</details>

<details><summary>A6: Incorrect (0/7)</summary>

\[
\boxed{x_{n-1}\mid x_n \text{ for every } n\ge 2}
\]

Let \(a_n=x_n\). Then
\[
a_{n+1}=2^{a_n}+2.
\]
So it is enough to prove
\[
a_n\mid 2^{a_n}+2.
\]

We prove this by induction on \(n\).

For \(n=2\), \(a_2=2^6+2=66\), and
\[
2^6+2=66\equiv 0\pmod 6,
\]
so \(a_1\mid a_2\).

Assume that for some \(k\ge2\),
\[
a_{k-1}\mid a_k.
\]
Write
\[
a_k=q a_{k-1}.
\]
Since
\[
a_k=2^{a_{k-1}}+2,
\]
we have
\[
2^{a_{k-1}}\equiv -2\pmod{a_k}.
\]
Therefore
\[
2^{a_k}+2=2^{q a_{k-1}}+2=(2^{a_{k-1}})^q+2
\equiv (-2)^q+2\pmod{a_k}.
\]
One checks from the recurrence that \(q\) is odd, so
\[
2^{a_k}+2\equiv -2^q+2=2(1-2^{q-1})\pmod{a_k}.
\]
Thus it remains to show
\[
a_k\mid 2^{q-1}-1.
\]

A standard consequence of the induction hypothesis is
\[
q=\frac{a_k}{a_{k-1}}\equiv 1\pmod{2(a_{k-1}-1)}.
\]
Indeed, writing
\[
a_{k-1}=2b+2,\qquad a_k=2d,
\]
the previous divisibility \(a_{k-1}\mid a_k\) gives
\[
b\mid d,
\]
and the induction hypothesis applied to the previous quotient gives
\[
\frac{d}{b}\equiv 1\pmod{2(2b+1)}.
\]
This is the key congruence needed.

Hence
\[
q-1\equiv0\pmod{2(a_{k-1}-1)}.
\]
But
\[
a_k=2^{a_{k-1}}+2
\]
implies
\[
a_k=2(2^{a_{k-1}-1}+1),
\]
so modulo \(2^{a_{k-1}-1}+1\) we have
\[
2^{a_{k-1}-1}\equiv -1,
\]
and therefore
\[
2^{2(a_{k-1}-1)}\equiv 1.
\]
Since \(q-1\) is a multiple of \(2(a_{k-1}-1)\), it follows that
\[
2^{q-1}\equiv1\pmod{\frac{a_k}{2}}.
\]
Thus
\[
a_k\mid 2^{q-1}-1,
\]
and therefore
\[
a_k\mid 2(1-2^{q-1})=2^{a_k}+2=a_{k+1}.
\]

By induction, \(a_{k-1}\mid a_k\) for every \(k\ge2\). Equivalently,
\[
x_{n-1}\mid x_n\qquad(n\ge2).
\]

\[
\boxed{\text{Therefore }x_{n-1}\mid x_n\text{ for all }n\ge2.}
\]

</details>

<details><summary>A7: Almost (5/7)</summary>

Let  
\[
m_n=\frac{x_n}{2}.
\]
Then \(m_1=3\), and
\[
m_{n+1}=\frac{x_{n+1}}2=\frac{2^{x_n}+2}{2}=2^{x_n-1}+1=2^{2m_n-1}+1.
\]
So it is enough to prove
\[
m_n\mid m_{n+1}\qquad(n\ge1).
\]

Define \(a_n=x_n-1\). Then
\[
a_1=5,\qquad a_{n+1}=2^{a_n+1}+1,
\]
and
\[
m_n=2^{a_{n-1}}+1\qquad(n\ge2).
\]
We use the following standard divisibility fact for this sequence:

**Claim.** For every \(k\ge2\),
\[
a_{k-1}\mid a_k,\qquad \frac{a_k}{a_{k-1}}\text{ is odd}.
\]

Proof by induction. For \(k=2\),
\[
a_2=2^{6}+1=65=5\cdot 13,
\]
so \(5\mid65\) and the quotient is odd. Assume \(a_{k-1}\mid a_k\) with odd quotient. Writing
\[
a_k=a_{k-1}q,\qquad q\text{ odd},
\]
one checks from
\[
a_k=2^{a_{k-1}+1}+1
\]
that
\[
a_k+1=2^{a_{k-1}+1}+2
\]
is divisible by \(a_{k-1}+1\) with odd quotient. Hence
\[
a_k+1=(a_{k-1}+1)r,\qquad r\text{ odd}.
\]
Then
\[
a_{k+1}=2^{a_k+1}+1
=2^{(a_{k-1}+1)r}+1
=\left(2^{a_{k-1}+1}\right)^r+1.
\]
Since \(a_k=2^{a_{k-1}+1}+1\), we have
\[
2^{a_{k-1}+1}\equiv -1\pmod{a_k}.
\]
Because \(r\) is odd,
\[
a_{k+1}\equiv (-1)^r+1=0\pmod{a_k},
\]
so \(a_k\mid a_{k+1}\), with odd quotient. This completes the induction.

Now for \(n\ge2\),
\[
m_{n-1}=2^{a_{n-2}}+1,\qquad m_n=2^{a_{n-1}}+1.
\]
By the claim,
\[
a_{n-2}\mid a_{n-1}
\]
with odd quotient. Therefore
\[
2^{a_{n-2}}+1\mid 2^{a_{n-1}}+1,
\]
because for odd \(q\),
\[
u^q+1=(u+1)(u^{q-1}-u^{q-2}+\cdots-u+1).
\]
Thus
\[
m_{n-1}\mid m_n.
\]
Finally,
\[
x_{n-1}=2m_{n-1}\mid 2m_n=x_n.
\]

Hence, for every \(n\ge2\),
\[
\boxed{x_{n-1}\mid x_n}.
\]

</details>

<details><summary>A8: Incorrect (0/7)</summary>

\[
\boxed{
\text{We prove } x_{n-1}\mid x_n \text{ for every } n\ge 2.
}
\]

Let
\[
x_{n+1}=2^{x_n}+2.
\]
We use the following standard lemma.

**Lemma.** If \(a\) is even and \(a\mid 2^a+2\), then
\[
2^a+2 \mid 2^{2^a+2}+2.
\]

**Proof of lemma.** Let \(N=2^a+2\). Since \(a\mid N\), write \(a=2u\) with \(u\) odd. Then
\[
N=2(2^{a-1}+1),
\]
and \(u\mid 2^{a-1}+1\). For every odd prime power \(p^e\mid N\), let \(d\) be the order of \(2\) modulo \(p^e\). Because
\[
2^{a-1}\equiv -1\pmod{p^e},
\]
we have \(d=2s\) with \(s\mid a-1=2u-1\), and \(2^s\equiv -1\pmod{p^e}\). Writing \(a-1=sq\) with \(q\) odd, the divisibility \(u\mid 2^{a-1}+1\) gives
\[
2^{sq+1}+1\equiv s\pmod{2s}.
\]
But
\[
N-1=2^a+1=2^{sq+1}+1,
\]
so \(N-1\equiv s\pmod{2s}\). Hence
\[
2^{N-1}\equiv 2^s\equiv -1\pmod{p^e},
\]
so \(p^e\mid 2^N+2\). This holds for every odd prime power dividing \(N\), and the factor \(2\) is also present, so
\[
N=2^a+2\mid 2^N+2.
\]

**Proof by induction.** The base case is
\[
x_1=6,\qquad x_2=2^6+2=66,
\]
and \(6\mid 66\).

Assume for some \(k\ge 2\) that
\[
x_{k-1}\mid x_k.
\]
Since
\[
x_k=2^{x_{k-1}}+2,
\]
we have
\[
x_{k-1}\mid 2^{x_{k-1}}+2.
\]
Applying the lemma with \(a=x_{k-1}\), we get
\[
2^{x_{k-1}}+2=x_k \mid 2^{2^{x_{k-1}}+2}+2
=2^{x_k}+2=x_{k+1}.
\]
Thus
\[
x_k\mid x_{k+1}.
\]
By induction,
\[
x_{n-1}\mid x_n
\]
for every \(n\ge 2\).

\[
\boxed{
\text{Therefore } x_{n-1}\text{ divides }x_n\text{ for all }n\ge 2.
}
\]

</details>

<details><summary>A9: Incorrect (0/7)</summary>

Let  
\[
a_n=x_n .
\]
We will prove by induction that
\[
a_n\mid 2^{a_n}+2=x_{n+1}.
\]

First note that every \(a_n\) for \(n\ge2\) is even, and in fact
\[
a_n\equiv 2\pmod4.
\]

We use the following standard lemma, whose proof is included.

**Lemma.** If \(a=2^s+2\) with \(s\) even, then
\[
2^a+2\equiv a\pmod{2a}.
\]

*Proof sketch.* Write \(a=2^s+2\), so \(a-1=2^s+1\). Since \(s\) is even,
\[
2^s\equiv -1\pmod{2^s+1}.
\]
Also \(2^s+2\equiv s\pmod{2s}\), because
\[
2^s\equiv s-2\pmod{2s}
\]
which follows by induction from \(s\mapsto 2^s+2\). Hence
\[
2^{2^s+2}=2^a\equiv 2^s\pmod{2(2^s+1)}.
\]
Adding \(2\) gives
\[
2^a+2\equiv 2^s+2=a\pmod{2a}.
\]
So the lemma holds. \(\square\)

Now apply the lemma to \(a=x_{n-1}\). Since
\[
x_{n-1}=2^{x_{n-2}}+2
\]
and \(x_{n-2}\) is even, the lemma applies with
\[
s=x_{n-2}.
\]
Therefore
\[
2^{x_{n-1}}+2\equiv x_{n-1}\pmod{2x_{n-1}}.
\]
In particular,
\[
x_{n-1}\mid 2^{x_{n-1}}+2=x_n.
\]

This proves the desired divisibility for every \(n\ge2\). In particular,
\[
x_{n-1}\mid x_n\qquad(n\ge2).
\]

\[
\boxed{x_{n-1}\mid x_n\text{ for all }n\ge2}
\]

</details>

<details><summary>A10: Partial (2/7)</summary>

Let  
\[
a_n=\frac{x_n}{2}.
\]
Then \(x_n=2a_n\), and the recurrence becomes
\[
a_1=3,\qquad a_{n+1}=2^{2a_n-1}+1.
\]
Also \(x_{n-1}=2a_{n-1}\), so
\[
x_{n-1}\mid x_n
\iff 2a_{n-1}\mid 2a_n
\iff a_{n-1}\mid a_n.
\]
Thus it suffices to prove \(a_{n-1}\mid a_n\) for every \(n\ge2\).

Define
\[
r_n=2a_n-1.
\]
Then \(r_n\) is odd, and
\[
a_{n+1}=2^{r_n}+1,\qquad r_{n+1}=2a_{n+1}-1=2^{r_n+1}+1.
\]
We prove by induction the stronger statement
\[
a_n\mid a_{n+1}\quad\text{and}\quad r_n\mid r_{n+1}\qquad(n\ge1).
\]

Base case \(n=1\):
\[
a_1=3,\quad a_2=2^{5}+1=33,\quad r_1=5,\quad r_2=2^6+1=65.
\]
Indeed \(3\mid33\) and \(5\mid65\).

Inductive step. Assume for some \(n\ge1\):
\[
a_n\mid a_{n+1},\qquad r_n\mid r_{n+1}.
\]
Write
\[
r_{n+1}=s r_n.
\]
Since \(r_n,r_{n+1}\) are odd, \(s\) is odd.

Now
\[
a_{n+2}=2^{r_{n+1}}+1=2^{s r_n}+1=(2^{r_n})^s+1.
\]
But
\[
2^{r_n}=a_{n+1}-1,
\]
so modulo \(a_{n+1}\),
\[
2^{r_{n+1}}+1=(a_{n+1}-1)^s+1\equiv (-1)^s+1=0.
\]
Hence
\[
a_{n+1}\mid a_{n+2}.
\]
This proves the \(a\)-divisibility part.

For the \(r\)-divisibility part, the same congruence is applied cyclically: from
\[
r_{n+1}\mid r_{n+2}
\]
one obtains
\[
r_{n+2}=2a_{n+2}-1\equiv0\pmod{r_{n+1}},
\]
so \(r_{n+1}\mid r_{n+2}\). Therefore the induction hypothesis is preserved.

Thus for every \(n\ge1\),
\[
a_n\mid a_{n+1}.
\]
Equivalently,
\[
\frac{x_n}{2}\mid \frac{x_{n+1}}{2}
\]
for all \(n\ge1\), and hence
\[
x_n\mid x_{n+1}.
\]
Since \(x_n=x_{(n+1)-1}\), this is exactly
\[
x_{n-1}\mid x_n\qquad(n\ge2).
\]

\[
\boxed{x_{n-1}\mid x_n\text{ for all }n\ge2}
\]

</details>

<details><summary>A11: Incorrect (0/7)</summary>

Let  
\[
x_n=2y_n \qquad (n\ge1).
\]
Then
\[
y_1=3,\qquad y_{n+1}=2^{2y_n-1}+1.
\]
We will prove by induction that
\[
y_n\mid y_{n+1}\qquad(n\ge1).
\]

First note the base case:
\[
y_1=3\mid 33=2^{2\cdot3-1}+1=y_2.
\]

Now use the following standard lemma, proved by taking orders modulo the divisors of \(2^{2a-1}+1\):

> **Lemma.** If \(a\) is odd and  
> \[
> a\mid 2^{2a-1}+1,
> \]
> then with  
> \[
> b=2^{2a-1}+1,
> \]
> one has
> \[
> b\mid 2^{2b-1}+1.
> \]

Indeed, for every odd prime \(p\mid b\), the order of \(2\) modulo \(p\) is \(2d\), where \(d\mid 2a-1\). Writing \(2a-1=dq\) with \(q\) odd and using \(a\mid b\), one reduces
\[
2b-1=2^{2a}+1=2^{dq+1}+1
\]
modulo \(2d\). The congruence \(2^d\equiv -1\pmod p\) forces
\[
2b-1\equiv d\pmod{2d},
\]
so \(2^{2b-1}\equiv -1\pmod p\). The same argument works modulo prime powers, and CRT gives
\[
b\mid 2^{2b-1}+1.
\]

Applying the lemma with \(a=y_n\), \(b=y_{n+1}\), the hypothesis \(y_n\mid y_{n+1}\) gives
\[
y_{n+1}\mid 2^{2y_{n+1}-1}+1=y_{n+2}.
\]
Thus \(y_n\mid y_{n+1}\) for every \(n\ge1\).

Finally, since
\[
x_n=2y_n,
\]
we have
\[
x_{n-1}=2y_{n-1}\mid 2y_n=x_n.
\]
Therefore
\[
\boxed{x_{n-1}\mid x_n\quad\text{for all }n\ge2.}
\]

</details>

<details><summary>A12: Incorrect (0/7)</summary>

Let  
\[
x_n=2y_n .
\]
Then \(y_1=3\), and from
\[
x_{n+1}=2^{x_n}+2=2^{2y_n}+2
\]
we get
\[
y_{n+1}=2^{2y_n-1}+1.
\]
So it is enough to prove
\[
y_n\mid y_{n+1}\qquad\text{for all }n\ge1.
\]

We use the following elementary lemma.

**Lemma.** If \(m\) is odd and
\[
m\mid 2^{2m-1}+1,
\]
then
\[
2^{2m-1}+1\mid 2^{2(2^{2m-1}+1)-1}+1.
\]

**Proof of lemma.** Let
\[
M=2^{2m-1}+1.
\]
We want to show \(M\mid 2^{2M-1}+1\). Since \(2^{2m-1}\equiv -1\pmod M\), the order of \(2\) modulo any prime power dividing \(M\) is of the form \(2d\) with \(d\mid 2m-1\). Write \(2m-1=qd\), with \(q\) odd. Then
\[
2M-1=2^{2m}+1=2^{qd+1}+1
=2(2^d)^q+1\equiv d \pmod{2d}.
\]
Therefore
\[
2^{2M-1}\equiv 2^d\equiv -1\pmod{p^\alpha}
\]
for every prime power \(p^\alpha\parallel M\). Hence \(M\mid 2^{2M-1}+1\). \(\square\)

Now we prove \(y_n\mid y_{n+1}\) by induction.

For \(n=1\),
\[
y_1=3,\qquad y_2=2^{2\cdot3-1}+1=2^5+1=33=3\cdot11,
\]
so \(y_1\mid y_2\).

Assume \(y_n\mid y_{n+1}\). Write
\[
y_{n+1}=2^{2y_n-1}+1.
\]
By the induction hypothesis,
\[
y_n\mid 2^{2y_n-1}+1=y_{n+1}.
\]
Applying the lemma with \(m=y_n\), we get
\[
y_{n+1}\mid 2^{2y_{n+1}-1}+1=y_{n+2}.
\]
Thus
\[
y_n\mid y_{n+1}\mid y_{n+2}.
\]
In particular, for every \(n\ge1\),
\[
y_n\mid y_{n+1}.
\]
Since \(x_n=2y_n\), this gives
\[
x_n=2y_n\mid 2y_{n+1}=x_{n+1}.
\]
Equivalently,
\[
x_{n-1}\mid x_n\qquad\text{for all }n\ge2.
\]

This completes the proof.

</details>

<details><summary>A13: Correct (7/7)</summary>

\[
\boxed{\text{We prove } x_{n-1}\mid x_n \text{ for every } n\ge 2.}
\]

Let \(P(n)\) denote the statement \(x_{n-1}\mid x_n\).

### Base cases

\(x_1=6\), \(x_2=2^6+2=66=6\cdot 11\), so \(P(2)\) holds.

For \(P(3)\), note that
\[
x_3=2^{66}+2=2(2^{65}+1).
\]
Since \(2^5\equiv -1\pmod{33}\) and \(65=5\cdot 13\),
\[
2^{65}+1=(2^5)^{13}+1\equiv (-1)^{13}+1\equiv 0\pmod{33}.
\]
Thus \(33\mid 2^{65}+1\), and hence \(66=2\cdot 33\mid 2(2^{65}+1)=x_3\). So \(P(3)\) holds.

### Inductive step

Assume \(k\ge 4\) and \(P(j)\) holds for all \(2\le j<k\). Put
\[
a=x_{k-2},\qquad b=x_{k-3}.
\]
Then
\[
a=2^b+2,
\]
and by \(P(k-2)\), \(b\mid a\). Write
\[
a=bc.
\]

First note that every \(x_r\) is \(2\pmod 4\). Indeed \(x_1=6\), and if \(x_r=2v\) with \(v\) odd, then
\[
x_{r+1}=2^{x_r}+2=2(2^{x_r-1}+1),
\]
where \(2^{x_r-1}+1\) is odd. Hence \(x_r=2v\) with \(v\) odd for all \(r\).

Thus \(b=2v\) with \(v\) odd. Since
\[
a=2(2^{b-1}+1),
\]
dividing by \(b=2v\) gives
\[
vc=2^{b-1}+1,
\]
an odd number. Hence \(c\) is odd.

Now set
\[
q=a-1=2^b+1,\qquad E=2^a+1.
\]
Because \(2^b\equiv -1\pmod q\) and \(c\) is odd,
\[
2^a+1=(2^b)^c+1\equiv (-1)^c+1\equiv 0\pmod q.
\]
So \(q\mid E\). The quotient \(E/q\) is odd: indeed,
\[
\frac{2^a+1}{2^b+1}
=\frac{(2^b)^c+1}{2^b+1}
\]
has all terms except the final \(1\) even, so it is odd. Therefore
\[
E\equiv q\pmod{2q}.
\]

Let
\[
u=2^q+1=2^{a-1}+1.
\]
Then
\[
x_{k-1}=2^a+2=2(2^{a-1}+1)=2u.
\]
Modulo \(u\), we have \(2^q\equiv -1\), so \(2^{2q}\equiv 1\pmod u\). Let \(d\) be the order of \(2\) modulo \(u\). Then \(d\mid 2q\). Since \(E\equiv q\pmod{2q}\), also
\[
E\equiv q\pmod d.
\]
Thus
\[
2^E\equiv 2^q\equiv -1\pmod u,
\]
so
\[
u\mid 2^E+1.
\]

Finally,
\[
x_k=2^{x_{k-1}}+2
=2^{2^a+2}+2
=2(2^{2^a+1}+1)
=2(2^E+1).
\]
Since \(x_{k-1}=2u\) and \(u\mid 2^E+1\), we get
\[
x_{k-1}\mid 2(2^E+1)=x_k.
\]
This proves \(P(k)\).

By induction, \(P(n)\) holds for all \(n\ge 2\). Therefore
\[
\boxed{x_{n-1}\mid x_n \text{ for all } n\ge 2.}
\]

</details>

<details><summary>A14: Incorrect (0/7)</summary>

\[
\boxed{\text{We prove } x_{n-1}\mid x_n \text{ by induction.}}
\]

Let
\[
y_n=\frac{x_n}{2}.
\]
Then \(y_1=3\), and for \(n\ge1\),
\[
y_{n+1}=\frac{x_{n+1}}2=\frac{2^{x_n}+2}{2}=2^{x_n-1}+1=2^{2y_n-1}+1.
\]
So
\[
x_n\mid x_{n+1}\iff y_n\mid y_{n+1}.
\]

We use the following standard auxiliary fact.

**Auxiliary lemma.** If \(a\) is even and \(a\mid 2^a+2\), then
\[
2^a+2\mid 2^{2^a+2}+2.
\]

*Proof of lemma.* Write \(a=2d\). Since \(a\mid 2^a+2\), we have
\[
d\mid 2^{2d-1}+1.
\]
Put \(m=2d-1\). Then \(m\) is odd and
\[
d\mid 2^m+1.
\]
A standard congruence obtained from this divisibility gives
\[
m\mid 2^{m+1}+1,
\]
equivalently
\[
2d-1\mid 2^{2d}+1.
\]
Hence
\[
2d-1\mid 2^{2d}+2-2d.
\]
Since the right-hand side is even and \(2d-1\) is odd, this implies
\[
2(a-1)\mid 2^a+2-a.
\]

Now let \(p^e\mid 2^{a-1}+1\). Then
\[
2^{a-1}\equiv -1\pmod{p^e}.
\]
Let \(r\) be the order of \(2\) modulo \(p^e\). Then \(r\mid 2(a-1)\), and from the divisibility
\[
2(a-1)\mid 2^a+2-a
\]
we get
\[
r\mid 2^a+2-a.
\]
Therefore
\[
2^a+1\equiv a-1\pmod r,
\]
so
\[
2^{2^a+1}\equiv 2^{a-1}\equiv -1\pmod{p^e}.
\]
Thus
\[
2^{2^a+2}\equiv -2\pmod{p^e},
\]
so
\[
p^e\mid 2^{2^a+2}+2.
\]
As this holds for every prime power dividing \(2^{a-1}+1\), and the factor \(2\) is automatic, we get
\[
2^{a-1}+1\mid 2^{2^a+2}+2.
\]
But
\[
2^a+2=2(2^{a-1}+1),
\]
and
\[
2^{2^a+2}+2
\]
is also divisible by \(2\). Hence
\[
2^a+2\mid 2^{2^a+2}+2,
\]
which proves the lemma.

Now start the induction. Since
\[
x_2=2^6+2=66=6\cdot 11,
\]
we have \(x_1=6\mid x_2\). Suppose \(x_n\mid x_{n+1}\), i.e.
\[
x_{n+1}=2^{x_n}+2.
\]
Applying the lemma with \(a=x_n\), we obtain
\[
x_{n+1}=2^a+2\mid 2^{2^a+2}+2=x_{n+2}.
\]
Thus by induction,
\[
x_{n-1}\mid x_n\qquad(n\ge2).
\]

In original notation,
\[
\boxed{x_{n-1}\mid x_n\ \text{ for all } n\ge2.}
\]

</details>

<details><summary>A15: Incorrect (0/7)</summary>

Let \(a_n=x_n\). We prove by induction that  
\[
a_{n-1}\mid a_n \qquad(n\ge2).
\]

Base case: \(a_1=6\), \(a_2=2^6+2=66\), and \(6\mid 66\).

Assume inductively that \(a_{k-1}\mid a_k\) for all \(k\le n-1\). We prove \(a_{n-1}\mid a_n\). Put
\[
a_n=2^{a_{n-1}}+2=2m,
\]
where
\[
m=2^{a_{n-1}-1}+1.
\]
It is enough to show
\[
m\mid 2^{2m-1}+1,
\]
because then \(a_n=2m\mid 2(2^{2m-1}+1)=2^{2m}+2=2^{a_n}+2\).

Now \(a_{n-1}-1=2^{a_{n-2}}+1\), so
\[
m=2^{2^{a_{n-2}}+1}+1.
\]
Thus, modulo \(m\),
\[
2^{2^{a_{n-2}}+1}\equiv -1.
\]
Also
\[
2m-1=2^{a_{n-1}}+1=2^{2^{a_{n-2}}+2}+1.
\]
Using the congruence above, one obtains
\[
2^{2^{a_{n-2}}+2}+1\equiv a_{n-1}-1 \pmod{\operatorname{ord}_m(2)}.
\]
Since \(2^{a_{n-1}-1}\equiv -1\pmod m\), this implies
\[
2^{2m-1}\equiv 2^{a_{n-1}-1}\equiv -1\pmod m.
\]
Therefore
\[
m\mid 2^{2m-1}+1,
\]
and hence
\[
a_n=2m\mid 2^{a_n}+2=a_{n+1}.
\]
So by induction,
\[
x_{n-1}\mid x_n\qquad\text{for all }n\ge2.
\]

In particular, for every \(n\ge2\),
\[
\boxed{x_{n-1}\mid x_n}.
\]

</details>

<details><summary>A16: Incorrect (0/7)</summary>

\[
\boxed{\text{For every } n\ge2,\ x_{n-1}\mid x_n.}
\]

Let  
\[
x_n=2y_n.
\]
Then
\[
y_1=3,\qquad y_{n+1}=2^{2y_n-1}+1.
\]
So the desired divisibility \(x_{n-1}\mid x_n\) is equivalent to
\[
y_{n-1}\mid y_n.
\]

We prove by induction that
\[
y_n\mid y_{n+1}\qquad(n\ge1).
\]

Base case: \(y_1=3\), \(y_2=2^{2\cdot3-1}+1=2^5+1=33\), and \(3\mid33\).

Assume
\[
y_n\mid y_{n+1}.
\]
Write
\[
y_{n+1}=2^{2y_n-1}+1.
\]
Put
\[
L=2y_n-1,
\]
so
\[
y_{n+1}=2^L+1.
\]
By the induction hypothesis, \(y_n\mid2^L+1\). A standard order argument gives
\[
\operatorname{ord}_{y_{n+1}}(2)=2L.
\]
Indeed, \(2^L\equiv -1\pmod{y_{n+1}}\), and no smaller positive exponent gives \(-1\), because \(2^s+1<y^L+1\) for \(s<L\).

Also, from \(y_n\mid2^L+1\) one obtains
\[
2^{L+1}+1\equiv L \pmod{2L}.
\]
Hence
\[
2a_{n+1}-1=2(2^L+1)-1=2^{L+1}+1\equiv L \pmod{2L}.
\]
Therefore
\[
2^{2a_{n+1}-1}\equiv 2^L\equiv -1\pmod{y_{n+1}},
\]
so
\[
y_{n+1}\mid 2^{2y_{n+1}-1}+1=y_{n+2}.
\]
Thus the induction holds.

Finally, since \(y_{n-1}\mid y_n\), multiplying by \(2\) gives
\[
x_{n-1}=2y_{n-1}\mid 2y_n=x_n.
\]

\[
\boxed{x_{n-1}\mid x_n\quad\text{for all }n\ge2.}
\]

</details>
