# PB-Basic-004

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Find all strictly increasing functions $g:\mathbb{R} \to \mathbb{R}$ such that:
 (a) $g$ is surjective
 (b) $g(g(x))=g(x)+20x.$

## Swarm: accepted (best candidate `P6`; self-verification grades [7, 7, 7]; 621,010 tokens in 58 calls)

**Blind grade: Correct (7/7).** Complete solution: g(0)=0 from c=c+20c, iff-type sign preservation giving every orbit term the sign of x, B=0 from A(4/5)^m+B(-1)^m>0 as m grows, both signs handled, and the solution verified.

\[
\boxed{g(x)=5x}
\]

Proof:

Since \(g\) is strictly increasing and surjective, it is bijective. Let \(g^{-1}\) be its inverse.

First determine \(g(0)\). Put \(c=g(0)\). Then
\[
g(c)=g(g(0))=g(0)=c.
\]
Using the equation with \(x=c\),
\[
g(g(c))=g(c)+20c.
\]
But \(g(c)=c\), so the left side is \(c\). Hence
\[
c=c+20c \implies c=0.
\]
Thus
\[
g(0)=0.
\]

Now fix \(x\neq 0\) and define the orbit
\[
a_n=g^n(x)\qquad(n\in\mathbb Z),
\]
where \(g^0(x)=x\). Since \(g(0)=0\) and \(g\) is strictly increasing,
\[
g(t)>0 \iff t>0,\qquad g(t)<0 \iff t<0.
\]
Therefore all \(a_n\) have the same sign as \(x\).

The functional equation gives
\[
a_{n+2}=g^{n+2}(x)=g(g(g^n(x)))
=g(g^n(x))+20g^n(x),
\]
so
\[
a_{n+2}=a_{n+1}+20a_n.
\]
The characteristic equation is
\[
r^2-r-20=0 \implies r=5,-4.
\]
Thus
\[
a_n=A5^n+B(-4)^n
\]
for some real constants \(A,B\), valid for all \(n\in\mathbb Z\).

Assume first \(x>0\). Then \(a_n>0\) for all \(n\). In particular, for \(n=-m\),
\[
0<a_{-m}
=A5^{-m}+B(-4)^{-m}
=\frac{A}{5^m}+\frac{B(-1)^m}{4^m}.
\]
Multiplying by \(4^m\),
\[
0<A\left(\frac45\right)^m+B(-1)^m.
\]
If \(B\neq 0\), choosing the parity of \(m\) so that \(B(-1)^m<0\), the right-hand side tends to a negative number as \(m\to\infty\), contradiction. Hence \(B=0\).

Therefore
\[
a_n=A5^n.
\]
Since \(a_0=x\), we get \(A=x\), and hence
\[
g(x)=a_1=5x.
\]

For \(x<0\), the same argument gives \(a_n<0\) for all \(n\), and the inequality
\[
0>a_{-m}
\]
forces \(B=0\) as well. Thus again \(a_1=5a_0\), so
\[
g(x)=5x.
\]

Together with \(g(0)=0\), we obtain
\[
g(x)=5x\qquad \forall x\in\mathbb R.
\]

Finally, \(g(x)=5x\) indeed works:
- it is strictly increasing,
- it is surjective,
- and
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x.
\]

Thus the unique solution is

\[
\boxed{g(x)=5x}.
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 19,306 | Correct (7/7) | Rigorous solution: g(0)=0 from c=21c, g(t)>t with both subcases handled, positivity of the whole bi-infinite orbit, and the eventually alternating sign of A(4/5)^m+B(-1)^m forces B=0, so g(x)=5x, which is verified. |
| A2 | stop | 23,602 | Correct (7/7) | Complete: g(0)=0 by injectivity, g and its inverse preserve sign, closed form of the two-sided orbit, and the odd/even limits of A(4/5)^m+B(-1)^m rule out nonzero B, yielding g(x)=5x, which is verified. |
| A3 | stop | 20,443 | Correct (7/7) | Shows 0 is the only fixed point, derives g(y)-y=20g^{-1}(y) to get sign preservation in both directions, then dominance of the B-term in x_{-m} forces B=0, giving g(x)=5x on both half-lines, with verification. |
| A4 | stop | 27,840 | Correct (7/7) | Valid alternative route: for nonzero x the orbit is strictly monotone over all of Z, so (a_{n+1}-a_n)/5^n=4A-5B(-4/5)^n has constant sign, which forces B=0 because (-4/5)^n is unbounded above and below; g(0)=0 and verification are included. |
| A5 | stop | 25,329 | Correct (7/7) | Complete solution: g(0)=0 by injectivity, positivity of all iterates via g^{-1}, scaling by 4^m shows the alternating term gives a negative limit unless beta=0, so g(x)=5x for both signs, with verification. |
| A6 | stop | 20,906 | Correct (7/7) | Correct and complete chain (g(0)=0, sign-preserving bi-infinite orbit, closed form, sign changes of y_{-m} if B is nonzero, verification); invertibility of g and positivity of backward iterates are left implicit and the unused claim g(t)>t skips the equality case, but these are immediate and do not affect the logic. |
| A7 | stop | 34,278 | Correct (7/7) | Complete and rigorous: g(0)=0, sign-preserving orbit over all integers, closed form A5^n+B(-4)^n, B=0 since A+B(-1)^m(5/4)^m would tend to -infinity for the bad parity, both sign cases treated, and the converse checked. |
| A8 | stop | 12,811 | Correct (7/7) | Complete solution: g(0)=0 by injectivity, closed form with D=(5x-g(x))/9, dominance of the D(-4)^{-m} term forces D=0 for x>0 and x<0, giving g(x)=5x, which is checked to satisfy all conditions. |
| A9 | stop | 25,670 | Correct (7/7) | Proves bijectivity and g(0)=0, shows every orbit keeps the sign of x, solves the two-sided recurrence as C5^n+D(-4)^n, and uses the even/odd limits D and -D of 4^m x_{-m} to force D=0, giving g(x)=5x with verification. |
| A10 | stop | 26,224 | Correct (7/7) | Derives g(0)=0, g(t)>t for t>0 and positivity of g^{-1} via g^{-1}(y)=(g(y)-y)/20, then A(4/5)^k+B(-1)^k>0 for all k forces B=0 by parity, giving g(x)=5x on both half-lines, and verifies the answer. |
| A11 | stop | 23,683 | Correct (7/7) | Complete solution: g(0)=0 by injectivity, correct explicit A and B in terms of x and g(x), careful sign argument at large negative indices for both x>0 and x<0 forcing B=0, and verification of g(x)=5x. |
| A12 | stop | 23,519 | Correct (7/7) | Complete argument: g(0)=0 by injectivity, sign-preserving bi-infinite orbits, closed form A5^n+B(-4)^n, and positivity of A4^m+B(-1)^m5^m for all m excludes B>0 and B<0 by choosing m odd or even; both sign cases and verification are included. |
| A13 | stop | 24,070 | Correct (7/7) | Complete solution: proves g(0)=0 by injectivity, builds the bi-infinite orbit satisfying x_{n+2}=x_{n+1}+20x_n, shows the (-4)^n coefficient B=(5x-g(x))/9 must vanish because backward iterates keep the sign of x while the B term dominates, and verifies g(x)=5x. |
| A14 | stop | 28,510 | Correct (7/7) | Complete solution: derives g(0)=0 from c=c+20c, uses that g and g^{-1} preserve sign on the bi-infinite orbit, forces B=0 via A+B(-1)^m(5/4)^m>0 with a correct parity argument, handles x<0 by negation, and verifies g(x)=5x. |
| A15 | stop | 24,186 | Correct (7/7) | Correct: g(0)=0, g and its inverse preserve half-lines, closed form with B=(5x-g(x))/9, and the constant sign of 4^m x_{-m}=A(4/5)^m+B(-1)^m forces B=0 so g(x)=5x, with verification; a leftover scratch line is cosmetic only. |
| A16 | stop | 26,464 | Correct (7/7) | Complete solution: g(0)=0 directly by injectivity, sign-preserving bi-infinite orbit, beta=(5x-g(x))/9 forced to 0 by the dominant 4^{-m} term at negative indices for both x>0 and x<0, and g(x)=5x verified. |

<details><summary>A1: Correct (7/7)</summary>

\[
\boxed{g(x)=5x \text{ for all } x\in\mathbb R}
\]

Proof:

Since \(g\) is strictly increasing, it is injective; by condition (a), it is also surjective. Hence \(g\) is bijective, so \(g^{-1}\) exists.

First determine \(g(0)\). Let \(c=g(0)\). From \(x=0\),
\[
g(g(0))=g(0)\implies g(c)=c.
\]
Now apply the equation at \(x=c\):
\[
g(g(c))=g(c)+20c.
\]
Since \(g(c)=c\), the left side is \(g(c)=c\), so
\[
c=c+20c \implies c=0.
\]
Thus
\[
g(0)=0.
\]

Next, for \(t>0\), we claim \(g(t)>t\). Indeed, if \(g(t)\le t\), then:

- if \(g(t)=t\), then the equation gives \(t=t+20t\), impossible for \(t>0\);
- if \(g(t)<t\), strict monotonicity gives \(g(g(t))<g(t)\), but the equation gives \(g(g(t))=g(t)+20t>g(t)\), contradiction.

Hence \(g(t)>t\) for \(t>0\). Similarly,
\[
t<0 \implies g(t)<t.
\]
In particular, \(g\) maps positive numbers to positive numbers and negative numbers to negative numbers.

Now fix \(x>0\), and define the bi-infinite orbit
\[
x_n=g^n(x),\qquad n\in\mathbb Z,
\]
so \(x_0=x\) and \(x_{n+1}=g(x_n)\). Since \(g(t)>t>0\) for \(t>0\), and the preimage of a positive number is positive, we have
\[
x_n>0 \qquad \forall n\in\mathbb Z.
\]

Using the equation,
\[
x_{n+2}=g(g(x_n))=g(x_n)+20x_n=x_{n+1}+20x_n.
\]
The characteristic equation is
\[
r^2=r+20 \iff r^2-r-20=0 \iff (r-5)(r+4)=0,
\]
so
\[
x_n=A5^n+B(-4)^n
\]
for some constants \(A,B\in\mathbb R\). From \(n=0,1\),
\[
A+B=x,\qquad 5A-4B=g(x).
\]
Solving gives
\[
B=\frac{5x-g(x)}9.
\]

Now look at \(n=-m\), \(m\ge 0\):
\[
x_{-m}=A5^{-m}+B(-4)^{-m}
=\frac{A}{5^m}+\frac{B(-1)^m}{4^m}>0.
\]
Multiplying by \(4^m\),
\[
A\left(\frac45\right)^m+B(-1)^m>0 \qquad \forall m\ge 0.
\]
If \(B\neq 0\), then for large \(m\), the term \(A(4/5)^m\to 0\), so the sign of the expression is eventually the sign of \(B(-1)^m\), which alternates between positive and negative for consecutive integers \(m\). This contradicts positivity for all \(m\). Hence \(B=0\). Therefore
\[
g(x)=5x \qquad \forall x>0.
\]

The same argument for \(x<0\) (where all \(x_n<0\)) gives \(B=0\), hence
\[
g(x)=5x \qquad \forall x<0.
\]
Together with \(g(0)=0\), we obtain
\[
g(x)=5x \quad \forall x\in\mathbb R.
\]

Finally, check:
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x,
\]
\(g\) is strictly increasing, and it is surjective. Thus the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

Let \(g:\mathbb R\to\mathbb R\) be strictly increasing, surjective, and satisfy
\[
g(g(x))=g(x)+20x. \tag{1}
\]

Since \(g\) is strictly increasing, it is injective; together with surjectivity it is bijective. Let \(g^{-1}\) be its inverse.

First determine \(g(0)\). Putting \(x=0\) in (1),
\[
g(g(0))=g(0).
\]
Let \(a=g(0)\). Then \(g(a)=g(0)\), so injectivity gives \(a=0\). Hence
\[
g(0)=0. \tag{2}
\]

Now fix \(x>0\). From (1),
\[
g(g(x))=g(x)+20x>g(x).
\]
Since \(g\) is increasing, if \(g(x)\le x\), then \(g(g(x))\le g(x)\), contradiction. Hence
\[
g(x)>x>0.
\]
Similarly, for \(x<0\),
\[
g(x)<x<0.
\]
Also, because \(g(0)=0\) and \(g\) is increasing, \(g^{-1}(y)>0\) for \(y>0\) and \(g^{-1}(y)<0\) for \(y<0\).

Now fix \(x\neq 0\) and define the orbit
\[
a_n=g^n(x),\qquad n\in\mathbb Z,
\]
where \(g^0(x)=x\) and \(g^{-n}(x)=(g^{-1})^n(x)\). Applying (1) to \(g^n(x)\),
\[
g(g(g^n(x)))=g(g^n(x))+20g^n(x),
\]
so
\[
a_{n+2}=a_{n+1}+20a_n. \tag{3}
\]

The characteristic equation of (3) is
\[
r^2=r+20 \iff r^2-r-20=0,
\]
with roots \(5\) and \(-4\). Hence
\[
a_n=A5^n+B(-4)^n \qquad (n\in\mathbb Z)
\]
for some constants \(A,B\) depending on \(x\). Using \(a_0=x\) and \(a_1=g(x)\),
\[
A+B=x,\qquad 5A-4B=g(x).
\]

We now show \(B=0\). Since \(x>0\), every \(a_n>0\); in particular \(a_{-m}>0\) for all \(m\ge0\). Thus
\[
0<a_{-m}=A5^{-m}+B(-4)^{-m}
=\frac{A}{5^m}+\frac{B(-1)^m}{4^m}.
\]
Multiplying by \(4^m\),
\[
A\left(\frac45\right)^m+B(-1)^m>0. \tag{4}
\]
If \(B>0\), taking odd \(m\) gives the left side tending to \(-B<0\), impossible. If \(B<0\), taking even \(m\) gives the left side tending to \(B<0\), impossible. Therefore \(B=0\).

For \(x<0\), the same argument applied to the negative sign gives \(B=0\) as well. Hence for every \(x\neq0\),
\[
B=0.
\]
Then \(a_0=A+B=A=x\), so
\[
g(x)=a_1=5A=5x.
\]
Together with \(g(0)=0\), we get
\[
g(x)=5x\qquad \forall x\in\mathbb R.
\]

Finally, \(g(x)=5x\) is strictly increasing, surjective, and
\[
g(g(x))=g(5x)=25x=5x+20x.
\]
Thus the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

We prove this is the only possibility.

Let \(g:\mathbb R\to\mathbb R\) be strictly increasing and surjective. Then \(g\) is bijective, so \(g^{-1}\) exists.

### 1. Show \(g(0)=0\)
Putting \(x=0\) in  
\[
g(g(x))=g(x)+20x
\]
gives
\[
g(g(0))=g(0).
\]
Let \(c=g(0)\). Then \(g(c)=c\), so \(c\) is a fixed point of \(g\).

If \(g(t)=t\), then
\[
g(g(t))=g(t)=t,
\]
while the equation gives
\[
t=g(g(t))=g(t)+20t=t+20t.
\]
Hence \(20t=0\), so \(t=0\). Therefore every fixed point is \(0\), so \(c=0\). Thus
\[
g(0)=0.
\]

### 2. Obtain a relation for \(g^{-1}\)
For any \(y\in\mathbb R\), write \(y=g(x)\), i.e. \(x=g^{-1}(y)\). Then
\[
g(y)=g(g(x))=g(x)+20x=y+20g^{-1}(y).
\]
Hence
\[
g(y)-y=20g^{-1}(y). \tag{1}
\]

Since \(g(0)=0\) and \(g\) is strictly increasing:
- if \(y>0\), then \(g^{-1}(y)>0\), so \(g(y)>y>0\);
- if \(y<0\), then \(g^{-1}(y)<0\), so \(g(y)<y<0\).

### 3. Determine \(g\) on positive reals
Fix \(x>0\), and define the backward and forward orbit
\[
x_n=g^n(x)\qquad (n\in\mathbb Z),
\]
where \(g^0(x)=x\), \(g^{n+1}(x)=g(g^n(x))\), and negative powers are taken using \(g^{-1}\).

Because \(g(y)>y>0\) for \(y>0\), and \(g^{-1}(y)>0\) for \(y>0\), all \(x_n\) are positive.

Applying the equation to \(x_n\),
\[
x_{n+2}=g(g(x_n))=g(x_n)+20x_n=x_{n+1}+20x_n.
\]
Thus \((x_n)\) satisfies the linear recurrence
\[
x_{n+2}=x_{n+1}+20x_n.
\]
The characteristic equation is
\[
r^2-r-20=0=(r-5)(r+4),
\]
so
\[
x_n=A5^n+B(-4)^n.
\]

Since all \(x_n>0\), we must have \(B=0\). Indeed, if \(B\ne0\), then for \(n=-m\),
\[
x_{-m}=\frac{A}{5^m}+\frac{B(-1)^m}{4^m},
\]
and the \(B\)-term dominates as \(m\to\infty\), forcing \(x_{-m}\) to alternate in sign, contradicting \(x_{-m}>0\). Therefore \(B=0\).

Hence
\[
x_n=A5^n.
\]
At \(n=0\), \(A=x_0=x\). Therefore
\[
x_1=5x.
\]
But \(x_1=g(x)\), so
\[
g(x)=5x\qquad \forall x>0.
\]

### 4. Determine \(g\) on negative reals
The same argument applies to \(x<0\). For \(x<0\), all \(x_n<0\), and the recurrence gives
\[
x_n=A5^n+B(-4)^n.
\]
Since all \(x_n<0\), the term \(B(-4)^n\) cannot appear; hence \(B=0\). Thus
\[
x_n=A5^n,
\]
and with \(x_0=x\), we get
\[
g(x)=x_1=5x\qquad \forall x<0.
\]

Together with \(g(0)=0\), this gives
\[
g(x)=5x\qquad \forall x\in\mathbb R.
\]

### 5. Verification
The function \(g(x)=5x\) is strictly increasing, surjective, and
\[
g(g(x))=g(5x)=25x,
\]
while
\[
g(x)+20x=5x+20x=25x.
\]
So it satisfies both conditions.

Therefore the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

Let \(g:\mathbb R\to\mathbb R\) satisfy the conditions. Since \(g\) is strictly increasing and surjective, it is bijective. Put
\[
h=g^{-1}.
\]
The inverse of a strictly increasing function is strictly increasing.

First, determine \(g(0)\). Let \(c=g(0)\). Then
\[
g(c)=g(g(0))=g(0)=c,
\]
so \(c\) is a fixed point of \(g\). If \(c>0\), then \(0<c\) and strict increase gives
\[
g(0)<g(c)\implies c<c,
\]
a contradiction. Similarly \(c<0\) is impossible. Hence
\[
g(0)=0.
\]

Now fix \(x\neq 0\). Define the orbit
\[
a_n=g^n(x)\qquad(n\in\mathbb Z),
\]
where \(g^0(x)=x\), \(g^{n+1}(x)=g(g^n(x))\), and \(g^{-n}(x)=(g^{-1})^n(x)\). Thus
\[
a_0=x,\qquad a_1=g(x).
\]
From
\[
g(g(t))=g(t)+20t
\]
we get, for every \(n\in\mathbb Z\),
\[
a_{n+2}=a_{n+1}+20a_n. \tag{1}
\]

Also \(g(x)\neq x\) for \(x\neq 0\), because if \(g(x)=x\), then
\[
x=g(g(x))=g(x)+20x=x+20x,
\]
forcing \(x=0\). Hence either \(a_1>a_0\) or \(a_1<a_0\).

If \(a_1>a_0\), then applying \(h=g^{-1}\) repeatedly gives
\[
a_0>a_{-1}>a_{-2}>\cdots,
\]
and applying \(g\) gives
\[
a_1>a_0>a_{-1}>\cdots.
\]
Thus \(a_n\) is strictly increasing in \(n\). Similarly, if \(a_1<a_0\), then \(a_n\) is strictly decreasing in \(n\). Therefore \(a_{n+1}-a_n\) has a fixed nonzero sign for all \(n\in\mathbb Z\).

The recurrence (1) has characteristic roots
\[
5,\ -4,
\]
so
\[
a_n=A5^n+B(-4)^n
\]
for some constants \(A,B\). Hence
\[
a_{n+1}-a_n=4A5^n-5B(-4)^n. \tag{2}
\]
Dividing by \(5^n>0\),
\[
4A-5B\left(-\frac45\right)^n=\frac{a_{n+1}-a_n}{5^n}.
\]
Since \((a_n)\) is strictly monotone, the left-hand side has a fixed sign for all \(n\in\mathbb Z\). But \(\left(-\frac45\right)^n\) is unbounded both above and below as \(n\) ranges over \(\mathbb Z\). Therefore the only possible way for the inequality
\[
4A>5B\left(-\frac45\right)^n
\quad\text{or}\quad
4A<5B\left(-\frac45\right)^n
\]
to hold for all \(n\in\mathbb Z\) is
\[
B=0.
\]
Thus
\[
a_n=A5^n.
\]
Since \(a_0=x\), we have \(A=x\). Therefore
\[
g(x)=a_1=5A=5x.
\]

So for every \(x\neq 0\), \(g(x)=5x\), and we already know \(g(0)=0\). Hence
\[
g(x)=5x\qquad\forall x\in\mathbb R.
\]

Finally, \(g(x)=5x\) is strictly increasing, surjective, and satisfies
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x.
\]

Thus the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

Let \(g:\mathbb R\to\mathbb R\) be a strictly increasing surjective solution.

First, set \(x=0\):
\[
g(g(0))=g(0).
\]
Let \(c=g(0)\). Then \(g(c)=c=g(0)\). Since \(g\) is injective, \(c=0\). Hence
\[
g(0)=0.
\]
Therefore \(g\) maps positive numbers to positive numbers and negative numbers to negative numbers.

Since \(g\) is bijective, write \(g^n\) for all \(n\in\mathbb Z\).

Fix \(x>0\), and define
\[
a_n=g^n(x)\qquad(n\in\mathbb Z).
\]
Because \(g^{-1}\) preserves positivity, we have \(a_n>0\) for every \(n\in\mathbb Z\). Also,
\[
a_{n+2}=g(g(a_n))=g(a_n)+20a_n=a_{n+1}+20a_n.
\]
Thus \((a_n)\) satisfies
\[
a_{n+2}=a_{n+1}+20a_n.
\]
The characteristic equation is
\[
r^2-r-20=0=(r-5)(r+4),
\]
so
\[
a_n=\alpha 5^n+\beta(-4)^n
\]
for some constants \(\alpha,\beta\).

For \(n=-m\),
\[
a_{-m}=\frac{\alpha}{5^m}+\frac{\beta(-1)^m}{4^m}>0.
\]
Multiplying by \(4^m\),
\[
\alpha\left(\frac45\right)^m+\beta(-1)^m>0
\]
for all \(m\). As \(m\to\infty\), \(\alpha(4/5)^m\to0\). If \(\beta>0\), then for large odd \(m\) the expression tends to \(-\beta<0\), contradiction. If \(\beta<0\), then for large even \(m\) it tends to \(\beta<0\), contradiction. Hence \(\beta=0\).

Therefore
\[
a_n=\alpha 5^n.
\]
In particular,
\[
g(x)=a_1=5a_0=5x.
\]

The same argument for \(x<0\) gives \(g(x)=5x\), since then \(a_n<0\) for all \(n\in\mathbb Z\), forcing \(\beta=0\) as well.

Thus \(g(x)=5x\) for all \(x\in\mathbb R\). Conversely,
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x,
\]
and \(g(x)=5x\) is strictly increasing and surjective.

Hence the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

First, \(g(0)=0\). Let \(c=g(0)\). Then
\[
g(g(0))=g(0)+0 \implies g(c)=c.
\]
Applying the equation at \(x=c\),
\[
g(g(c))=g(c)+20c.
\]
Since \(g(c)=c\), this gives
\[
c=c+20c,
\]
so \(c=0\). Hence \(g(0)=0\).

Because \(g\) is strictly increasing and \(g(0)=0\), for \(t>0\) we must have \(g(t)>0\), and for \(t<0\), \(g(t)<0\). Also, if \(t>0\) and \(g(t)<t\), then
\[
g(g(t))<g(t),
\]
but the equation gives
\[
g(g(t))=g(t)+20t>g(t),
\]
a contradiction. Thus \(g(t)>t\) for \(t>0\), and similarly \(g(t)<t\) for \(t<0\).

Now fix \(a>0\), and define
\[
y_n=g^n(a)\qquad (n\in\mathbb Z).
\]
Then \(y_n>0\) for every \(n\). From the equation,
\[
y_{n+2}=g(g(y_n))=g(y_n)+20y_n=y_{n+1}+20y_n.
\]
The characteristic equation is
\[
r^2-r-20=0 \implies r=5,-4.
\]
Hence
\[
y_n=A5^n+B(-4)^n
\]
for some constants \(A,B\). If \(B\neq 0\), then for \(n=-m\),
\[
y_{-m}=5^{-m}\left(A+B(-1)^m\left(\frac54\right)^m\right),
\]
which changes sign infinitely often as \(m\to\infty\), contradicting \(y_{-m}>0\). Therefore \(B=0\), so
\[
y_n=A5^n.
\]
Since \(y_0=a\), we have \(A=a\), and therefore
\[
g(a)=y_1=5a.
\]
Thus \(g(x)=5x\) for every \(x>0\).

The same argument for \(a<0\) gives \(g(a)=5a\) for every \(a<0\), and we already know \(g(0)=0\). Hence
\[
g(x)=5x\qquad \forall x\in\mathbb R.
\]

Finally, \(g(x)=5x\) indeed satisfies
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x,
\]
and it is strictly increasing and surjective. Therefore the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

Let \(g:\mathbb R\to\mathbb R\) be strictly increasing, surjective, and satisfy
\[
g(g(x))=g(x)+20x.
\]

First, setting \(x=0\) gives
\[
g(g(0))=g(0).
\]
Let \(c=g(0)\). Then \(g(c)=c\). Applying the equation at \(x=c\),
\[
g(g(c))=g(c)+20c.
\]
Since \(g(c)=c\), this becomes
\[
c=c+20c,
\]
so \(c=0\). Hence
\[
g(0)=0.
\]

Because \(g\) is strictly increasing, it maps positive numbers to positive numbers and negative numbers to negative numbers. Thus for any \(x>0\), the whole backward and forward orbit
\[
x_n=g^n(x),\qquad n\in\mathbb Z,
\]
remains positive; for \(x<0\), all \(x_n\) remain negative.

Fix \(x>0\), and define \(x_n=g^n(x)\) for \(n\in\mathbb Z\). Then
\[
x_{n+2}=g(g(x_n))=g(x_n)+20x_n=x_{n+1}+20x_n.
\]
So \((x_n)\) satisfies the linear recurrence
\[
x_{n+2}=x_{n+1}+20x_n.
\]
Its characteristic equation is
\[
r^2-r-20=0,
\]
so
\[
r=5,\ -4.
\]
Hence
\[
x_n=A5^n+B(-4)^n
\]
for some real constants \(A,B\). Since \(x_0=x\), we have
\[
A+B=x>0.
\]

Now look at negative indices. For \(m\ge 0\),
\[
x_{-m}=A5^{-m}+B(-4)^{-m}
=\frac{A}{5^m}+B\frac{(-1)^m}{4^m}>0.
\]
Multiplying by \(5^m\),
\[
A+B(-1)^m\left(\frac54\right)^m>0.
\]
If \(B\neq 0\), choosing the parity of \(m\) that makes \(B(-1)^m<0\) forces the left-hand side to tend to \(-\infty\), contradiction. Therefore \(B=0\).

Thus
\[
x_n=A5^n.
\]
Since \(x_0=A=x>0\), we get
\[
g(x)=x_1=5x.
\]

The same argument for \(x<0\) gives \(B=0\) as well, so again
\[
g(x)=5x.
\]
Finally, \(g(0)=0=5\cdot 0\).

So every solution must be \(g(x)=5x\).

Conversely, \(g(x)=5x\) is strictly increasing, surjective, and
\[
g(g(x))=g(5x)=25x,
\]
while
\[
g(x)+20x=5x+20x=25x.
\]
Thus it satisfies the equation.

\[
\boxed{g(x)=5x}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

Let \(g:\mathbb R\to\mathbb R\) be strictly increasing and surjective, so bijective.

First, put \(x=0\):
\[
g(g(0))=g(0).
\]
Since \(g\) is injective, this forces \(g(0)=0\). Hence \(g\) preserves sign:
\[
x>0 \implies g(x)>0,\qquad x<0 \implies g(x)<0.
\]

Fix \(x\in\mathbb R\), and for \(n\in\mathbb Z\) define
\[
a_n=g^n(x),
\]
where \(g^n\) denotes the \(n\)-fold iterate, with \(g^{-1}\) used for negative integers. Then
\[
a_{n+2}=g^2(a_n)=g(a_n)+20a_n=a_{n+1}+20a_n.
\]
So \((a_n)\) satisfies the linear recurrence
\[
a_{n+2}=a_{n+1}+20a_n.
\]
Its characteristic equation is
\[
r^2-r-20=0=(r-5)(r+4),
\]
so
\[
a_n=C5^n+D(-4)^n.
\]
Using \(a_0=x\) and \(a_1=g(x)\), we get
\[
C+D=x,\qquad 5C-4D=g(x),
\]
hence
\[
C=\frac{g(x)+4x}{9},\qquad D=\frac{5x-g(x)}{9}.
\]

Now take \(x>0\). Since \(g(0)=0\) and \(g\) is increasing, every forward and every backward iterate of \(x\) remains positive:
\[
a_n>0\qquad \forall n\in\mathbb Z.
\]
In particular, for \(m\ge 1\),
\[
a_{-m}=C5^{-m}+D(-4)^{-m}
=\frac{C}{5^m}+\frac{D(-1)^m}{4^m}.
\]
As \(m\to\infty\), the term \(D/4^m\) dominates \(C/5^m\), so for large \(m\), the sign of \(a_{-m}\) is determined by \(D(-1)^m\). If \(D\neq 0\), one of the even/odd \(m\) would make \(a_{-m}<0\), contradicting \(a_{-m}>0\). Thus \(D=0\) for \(x>0\).

Similarly, taking \(x<0\) shows \(D=0\). Therefore for every \(x\neq 0\),
\[
D=0,\qquad C=x,
\]
so
\[
g(x)=a_1=5C=5x.
\]
Since \(g(0)=0=5\cdot 0\), we obtain
\[
g(x)=5x\qquad \forall x\in\mathbb R.
\]

Finally, check:
\[
g(g(x))=g(5x)=25x,
\]
while
\[
g(x)+20x=5x+20x=25x.
\]
Also \(g(x)=5x\) is strictly increasing and surjective. Hence the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

Let \(g:\mathbb R\to\mathbb R\) be strictly increasing, surjective, and satisfy
\[
g(g(x))=g(x)+20x.
\]

Since \(g\) is strictly increasing, it is injective; together with surjectivity, \(g\) is bijective. Also, from \(x=0\),
\[
g(g(0))=g(0).
\]
Writing \(u=g(0)\), this gives \(g(u)=u=g(0)\), so by injectivity \(u=0\). Hence
\[
g(0)=0.
\]

Now fix \(x\neq 0\), and define its orbit
\[
x_n=g^n(x)\qquad(n\in\mathbb Z),
\]
where \(g^0(x)=x\) and \(g^{-1}\) exists. Then \(x_n\) has the same sign as \(x\) for every \(n\in\mathbb Z\). Indeed, for \(x>0\), the equation gives
\[
g(g(x))=g(x)+20x>g(x),
\]
forcing \(g(x)>x>0\); similarly for negative \(x\). Thus the orbit never crosses \(0\).

From the functional equation,
\[
x_{n+2}=g^2(x_n)=g(x_n)+20x_n=x_{n+1}+20x_n.
\]
So \((x_n)\) satisfies the linear recurrence
\[
x_{n+2}=x_{n+1}+20x_n.
\]
Its characteristic equation is
\[
r^2-r-20=0=(r-5)(r+4),
\]
so
\[
x_n=C5^n+D(-4)^n
\]
for some constants \(C,D\).

For \(n=-m\),
\[
x_{-m}=C5^{-m}+D(-4)^{-m}.
\]
Multiplying by \(4^m\),
\[
4^m x_{-m}=C\left(\frac45\right)^m+D(-1)^m.
\]
The left-hand side has constant sign equal to the sign of \(x\). Taking even and odd \(m\to\infty\), the even subsequence tends to \(D\) and the odd subsequence tends to \(-D\). Hence both \(D\) and \(-D\) must have the same sign, forcing
\[
D=0.
\]
Therefore
\[
x_n=C5^n.
\]
In particular, using \(x_0=x\), we get \(C=x\), and then
\[
g(x)=x_1=5x_0=5x.
\]
This holds for every \(x\neq 0\), and we already know \(g(0)=0\). Hence
\[
g(x)=5x\qquad\forall x\in\mathbb R.
\]

Finally, \(g(x)=5x\) indeed works:
\[
g(g(x))=g(5x)=25x=5x+20x,
\]
it is strictly increasing, and it is surjective. Therefore the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

\[
\boxed{g(x)=5x \text{ for all } x\in\mathbb R}
\]

Proof:

Let \(g:\mathbb R\to\mathbb R\) be strictly increasing and surjective, so bijective.

First determine \(g(0)\). From
\[
g(g(x))=g(x)+20x
\]
with \(x=0\),
\[
g(g(0))=g(0).
\]
Let \(c=g(0)\). Then \(g(c)=c=g(0)\), so by injectivity \(c=0\). Hence
\[
g(0)=0.
\]

Also, if \(x>0\), then
\[
g(g(x))=g(x)+20x>g(x).
\]
Since \(g\) is strictly increasing, \(g(g(x))>g(x)\) implies
\[
g(x)>x.
\]
Similarly, if \(x<0\), then \(g(x)<x\).

Now replace \(x\) by \(g^{-1}(y)\) in the functional equation:
\[
g(y)=y+20g^{-1}(y),
\]
so
\[
g^{-1}(y)=\frac{g(y)-y}{20}. \tag{1}
\]
Thus for \(y>0\), \(g^{-1}(y)>0\).

Fix \(x>0\), and define the orbit
\[
a_n=g^n(x),\qquad n\in\mathbb Z.
\]
Then
\[
a_{n+2}=g(g(g^n(x)))=g(g^n(x))+20g^n(x),
\]
so
\[
a_{n+2}=a_{n+1}+20a_n.
\]
The characteristic equation is
\[
r^2-r-20=0,
\]
so \(r=5,-4\). Hence for some constants \(A,B\),
\[
a_n=A5^n+B(-4)^n. \tag{2}
\]

Because \(g(t)>t\) for \(t>0\), the orbit \(a_n=g^n(x)\) stays positive for all \(n\in\mathbb Z\). In particular,
\[
a_{-k}=A5^{-k}+B(-4)^{-k}>0.
\]
Multiplying by \(4^k\),
\[
A\left(\frac45\right)^k+B(-1)^k>0. \tag{3}
\]
Taking \(k=2m\) even in (3) and letting \(m\to\infty\) gives \(B\ge 0\). Taking \(k=2m+1\) odd in (3) and letting \(m\to\infty\) gives \(B\le 0\). Therefore \(B=0\).

Then
\[
a_n=A5^n.
\]
Since \(a_0=x\), we have \(A=x\), and hence
\[
g(x)=a_1=5x.
\]

The same argument works for \(x<0\): there \(a_n<0\) for all \(n\in\mathbb Z\), and the inequalities in (3) force \(B=0\) again, giving \(g(x)=5x\). Also \(g(0)=0=5\cdot 0\).

Finally, \(g(x)=5x\) indeed satisfies all conditions:
\[
g(g(x))=g(5x)=25x,\qquad g(x)+20x=5x+20x=25x,
\]
and it is strictly increasing and surjective.

Thus the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

\[
\boxed{g(x)=5x \text{ for all } x\in\mathbb R}
\]

Proof:

Since \(g\) is strictly increasing and surjective, it is bijective. Let \(g^n\) denote the \(n\)-fold iterate for \(n\in\mathbb Z\), with \(g^0=\mathrm{id}\) and \(g^{-n}=(g^n)^{-1}\).

First, setting \(x=0\) gives
\[
g(g(0))=g(0).
\]
By injectivity of \(g\), this implies \(g(0)=0\). Hence \(g\) sends positive numbers to positive numbers and negative numbers to negative numbers. Therefore, for any fixed \(x\ne 0\), all iterates \(g^n(x)\) have the same sign as \(x\).

Fix \(x>0\), and write \(a_n=g^n(x)\). Then \(a_n>0\) for every \(n\in\mathbb Z\). The functional equation gives
\[
a_{n+2}=a_{n+1}+20a_n.
\]
The characteristic equation is
\[
r^2-r-20=0,
\]
with roots \(5\) and \(-4\). Thus
\[
a_n=A5^n+B(-4)^n.
\]
Using \(a_0=x\) and \(a_1=g(x)\), we get
\[
A=\frac{g(x)+4x}{9},\qquad B=\frac{5x-g(x)}{9}.
\]
For \(x>0\), \(A>0\). Now take \(n=-m\):
\[
a_{-m}=\frac{A}{5^m}+\frac{B(-1)^m}{4^m}.
\]
If \(B\ne0\), choose infinitely many \(m\) with \(B(-1)^m<0\). Then for those \(m\),
\[
a_{-m}=\frac{A}{5^m}-\frac{|B|}{4^m}<0
\]
for all sufficiently large such \(m\), contradicting \(a_{-m}>0\). Hence \(B=0\), so
\[
5x-g(x)=0 \quad\Longrightarrow\quad g(x)=5x.
\]

Similarly, for \(x<0\), we have \(A<0\) and \(a_n<0\) for all \(n\). If \(B\ne0\), choose \(m\) with \(B(-1)^m>0\). Then
\[
a_{-m}=-\frac{|A|}{5^m}+\frac{|B|}{4^m}>0
\]
for all sufficiently large such \(m\), again a contradiction. Thus \(B=0\), so \(g(x)=5x\) as well.

Since \(g(0)=0=5\cdot0\), we have
\[
g(x)=5x\qquad \forall x\in\mathbb R.
\]

Finally, this function works:
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x,
\]
and it is strictly increasing and surjective.

\[
\boxed{g(x)=5x}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

Since \(g\) is strictly increasing and surjective, it is bijective. Denote iterates by \(g^n\), with \(g^0(x)=x\) and \(g^{-n}\) the inverse.

First, \(g(0)=0\). Indeed, at \(x=0\),
\[
g(g(0))=g(0).
\]
Let \(a=g(0)\). Then \(g(a)=a=g(0)\), so by injectivity \(a=0\).

Now fix \(x>0\). Since \(g\) is increasing and \(g(0)=0\), we have \(g(x)>0\). If \(g(x)<x\), then applying \(g\) gives
\[
g(g(x))<g(x),
\]
but the equation gives
\[
g(g(x))=g(x)+20x>g(x),
\]
a contradiction. Also \(g(x)=x\) would force \(x=0\). Hence
\[
g(x)>x.
\]
Therefore all iterates \(g^n(x)\) remain positive for \(x>0\). Similarly, for \(x<0\), all iterates remain negative.

Now fix \(x>0\) and define \(x_n=g^n(x)\) for \(n\in\mathbb Z\). From the equation,
\[
x_{n+2}=g(g(x_n))=g(x_n)+20x_n=x_{n+1}+20x_n.
\]
The characteristic equation is
\[
r^2-r-20=0,
\]
so \(r=5\) or \(r=-4\). Hence
\[
x_n=A5^n+B(-4)^n
\]
for some real constants \(A,B\).

Because \(x_{-m}>0\) for all \(m\ge0\),
\[
0<x_{-m}=A5^{-m}+B(-4)^{-m}.
\]
Multiplying by \(5^m4^m>0\), we get
\[
0<A4^m+B(-1)^m5^m.
\]
If \(B>0\), taking large odd \(m\) makes the right-hand side negative; if \(B<0\), taking large even \(m\) makes it negative. Thus necessarily \(B=0\).

Therefore
\[
x_n=A5^n.
\]
Since \(x_0=x\), we have \(A=x\), and hence
\[
g(x)=x_1=5x.
\]
The same argument for \(x<0\) gives \(g(x)=5x\) there as well, and \(g(0)=0\). Thus
\[
g(x)=5x\qquad \forall x\in\mathbb R.
\]

Finally, \(g(x)=5x\) indeed works:
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x,
\]
and it is strictly increasing and surjective.

\[
\boxed{g(x)=5x}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

Let \(g:\mathbb R\to\mathbb R\) be strictly increasing and surjective, satisfying  
\[
g(g(x))=g(x)+20x. \tag{1}
\]

Since \(g\) is strictly increasing, it is injective, and surjectivity gives that \(g\) is bijective. Let \(g^{-1}\) be its inverse.

First, put \(c=g(0)\). From (1) with \(x=0\),
\[
g(g(0))=g(0)\implies g(c)=c.
\]
But \(g(c)=g(0)\), so by injectivity \(c=0\). Hence
\[
g(0)=0.
\]

Now fix \(x\neq 0\), and define the bi-infinite orbit
\[
x_n=g^n(x)\qquad(n\in\mathbb Z),
\]
where \(g^0(x)=x\), \(g^{n+1}(x)=g(g^n(x))\), and \(g^{-n}(x)=(g^{-1})^n(x)\).

Applying (1) to \(x_n\), we get
\[
x_{n+2}=g(g(x_n))=g(x_n)+20x_n=x_{n+1}+20x_n.
\]
Thus
\[
x_{n+2}=x_{n+1}+20x_n \qquad(n\in\mathbb Z).
\]
The characteristic equation is
\[
r^2-r-20=0,
\]
so
\[
r=5 \quad\text{or}\quad r=-4.
\]
Hence
\[
x_n=A5^n+B(-4)^n
\]
for some constants \(A,B\) depending on \(x\). In particular,
\[
x_0=x,\qquad x_1=g(x),
\]
so
\[
A+B=x,\qquad 5A-4B=g(x).
\]
Solving gives
\[
B=\frac{5x-g(x)}9. \tag{2}
\]

Now consider \(x>0\). Since \(g(0)=0\) and \(g\) is increasing, all backward iterates of \(x\) remain positive:
\[
x_{-m}>0\qquad\forall m\ge0.
\]
But from the formula,
\[
x_{-m}=A5^{-m}+B(-4)^{-m}
=\frac{A}{5^m}+\frac{B(-1)^m}{4^m}.
\]
If \(B\neq0\), then \(\frac{B(-1)^m}{4^m}\) dominates \(\frac{A}{5^m}\) as \(m\to\infty\), so \(x_{-m}\) would have alternating signs for large \(m\), contradicting \(x_{-m}>0\). Therefore \(B=0\).

The same argument for \(x<0\), where all \(x_{-m}<0\), again forces \(B=0\). Thus for every \(x\neq0\),
\[
\frac{5x-g(x)}9=0,
\]
so
\[
g(x)=5x.
\]
Since \(g(0)=0=5\cdot0\), we have
\[
g(x)=5x\qquad\forall x\in\mathbb R.
\]

Finally, \(g(x)=5x\) indeed works:
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x,
\]
and \(g\) is strictly increasing and surjective.

Therefore the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof.

Since \(g\) is strictly increasing and surjective, it is bijective. Let \(g^{-1}\) be its inverse.

First determine \(g(0)\). Put \(c=g(0)\). From the equation at \(x=0\),
\[
g(g(0))=g(0),
\]
so \(g(c)=c\). Using the equation at \(x=c\),
\[
g(g(c))=g(c)+20c.
\]
But \(g(c)=c\), hence \(g(g(c))=c\). Therefore
\[
c=c+20c,
\]
so \(c=0\). Thus
\[
g(0)=0.
\]

Because \(g\) is strictly increasing and \(g(0)=0\), we have
\[
x>0 \implies g(x)>0,\qquad x<0 \implies g(x)<0.
\]
Thus \(g\) and \(g^{-1}\) both preserve the positive/negative half-lines.

Fix \(x>0\), and define
\[
a_n=g^{\circ n}(x)
\]
for \(n\in\mathbb Z\), where \(g^{\circ 0}(x)=x\) and \(g^{\circ(n+1)}=g\circ g^{\circ n}\). Since \(g\) preserves positivity, all \(a_n>0\).

The functional equation gives
\[
a_{n+2}=g^{\circ 2}(a_n)=g^{\circ1}(a_n)+20a_n=a_{n+1}+20a_n.
\]
So
\[
a_{n+2}=a_{n+1}+20a_n.
\]
The characteristic equation is
\[
r^2-r-20=0,
\]
with roots \(5\) and \(-4\). Hence
\[
a_n=A5^n+B(-4)^n
\]
for some real constants \(A,B\).

Now use positivity for negative indices. For \(m\ge 0\),
\[
0<a_{-m}=A5^{-m}+B(-4)^{-m}.
\]
Multiplying by \(5^m\),
\[
0<A+B(-1)^m\left(\frac54\right)^m.
\]
If \(B>0\), taking odd \(m\) large makes the right-hand side negative; if \(B<0\), taking even \(m\) large makes it negative. Therefore \(B=0\). Hence
\[
a_n=A5^n.
\]
Since \(a_0=x\), we get \(A=x\), so
\[
g(x)=a_1=5x.
\]

For \(x<0\), the same argument applied to \(-g^{\circ n}(x)>0\) gives \(g(x)=5x\) as well. For \(x=0\), we already have \(g(0)=0=5\cdot 0\).

Finally, \(g(x)=5x\) indeed works:
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x,
\]
and \(g\) is strictly increasing and surjective.

\[
\boxed{g(x)=5x}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

is the unique solution.

Proof:

Since \(g\) is strictly increasing, it is injective. By (a), \(g\) is surjective, hence bijective. Let \(g^{-1}\) denote the inverse.

First, put \(x=0\) in
\[
g(g(x))=g(x)+20x.
\]
Then
\[
g(g(0))=g(0).
\]
Let \(a=g(0)\). Then \(g(a)=a=g(0)\). Since \(g\) is injective, \(a=0\). Hence
\[
g(0)=0.
\]

Because \(g\) is strictly increasing and \(g(0)=0\), we have
\[
x>0 \implies g(x)>0,\qquad x<0 \implies g(x)<0.
\]
Thus \(g\) and \(g^{-1}\) each preserve the positive and negative half-lines.

For fixed \(x\in\mathbb R\), define
\[
x_n=g^n(x)\qquad (n\in\mathbb Z),
\]
where \(g^0=\mathrm{id}\), \(g^{n+1}=g\circ g^n\), and \(g^{-n}=(g^{-1})^n\). Since \(g\) is bijective, these iterates are defined for all integers \(n\).

Applying the equation to \(x_n\),
\[
x_{n+2}=g^2(x_n)=g(x_n)+20x_n=x_{n+1}+20x_n.
\]
So
\[
x_{n+2}=x_{n+1}+20x_n\qquad(n\in\mathbb Z).
\]
The characteristic equation is
\[
r^2=r+20 \iff r^2-r-20=0 \iff (r-5)(r+4)=0,
\]
so
\[
x_n=A5^n+B(-4)^n
\]
for some constants \(A,B\) depending on \(x\). From \(x_0=x\) and \(x_1=g(x)\),
\[
A+B=x,\qquad 5A-4B=g(x).
\]
Subtracting \(4(A+B)=4x\) from the second equation gives
\[
A-8B? 
\]
Instead, directly:
\[
5A-4B=5(A+B)-9B=5x-9B,
\]
so
\[
B=\frac{5x-g(x)}9.
\]

Now take \(m\ge 0\). Since \(g\) preserves the half-line containing \(x\), the numbers \(x_{-m}=g^{-m}(x)\) all have the same sign. But from the formula,
\[
x_{-m}=A5^{-m}+B(-4)^{-m}
=\frac{A}{5^m}+\frac{B(-1)^m}{4^m}.
\]
Multiplying by \(4^m\),
\[
4^m x_{-m}=A\left(\frac45\right)^m+B(-1)^m.
\]
Since \(\left(\frac45\right)^m\to 0\), the term \(B(-1)^m\) dominates for large \(m\). If \(B\neq 0\), then \(x_{-m}\) would alternate in sign for large \(m\), contradicting the fact that \(x_{-m}\) has constant sign. Therefore \(B=0\), so
\[
g(x)=5x.
\]
This holds for every \(x\neq 0\), and \(g(0)=0\) as well.

Finally, check that \(g(x)=5x\) works:
\[
g(g(x))=g(5x)=25x,
\]
while
\[
g(x)+20x=5x+20x=25x.
\]
It is strictly increasing, surjective, and satisfies the equation.

Hence
\[
\boxed{g(x)=5x}.
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

\[
\boxed{g(x)=5x}
\]

Proof:

Let \(g\) be a strictly increasing surjective function satisfying
\[
g(g(x))=g(x)+20x.
\]

Since \(g\) is strictly increasing, it is injective. Taking \(x=0\),
\[
g(g(0))=g(0).
\]
If \(a=g(0)\), then \(g(a)=g(0)\), so injectivity gives \(a=0\). Hence
\[
g(0)=0.
\]

Thus
\[
x>0 \implies g(x)>0,\qquad x<0 \implies g(x)<0.
\]
Because \(g\) is bijective, its inverse preserves signs as well. Therefore, for each fixed \(x\neq 0\), every iterate \(g^n(x)\) has the same sign as \(x\).

For fixed \(x\), define
\[
x_n=g^n(x)\qquad (n\in\mathbb Z).
\]
Applying the functional equation to \(x_n\),
\[
x_{n+2}=x_{n+1}+20x_n.
\]
The characteristic equation is
\[
r^2-r-20=0=(r-5)(r+4),
\]
so
\[
x_n=\alpha 5^n+\beta(-4)^n
\]
for some constants \(\alpha,\beta\) depending on \(x\). From \(x_0=x\) and \(x_1=g(x)\),
\[
\alpha+\beta=x,\qquad 5\alpha-4\beta=g(x).
\]
Solving,
\[
\beta=\frac{5x-g(x)}9.
\]

Now consider \(x>0\). Then \(x_{-m}>0\) for all \(m\ge 0\). But
\[
x_{-m}=\frac{\alpha}{5^m}+\beta\frac{(-1)^m}{4^m}.
\]
If \(\beta>0\), taking odd \(m\) large makes this negative; if \(\beta<0\), taking even \(m\) large makes it negative. Hence \(\beta=0\).

Similarly, for \(x<0\), all \(x_{-m}<0\), and the same asymptotic argument forces \(\beta=0\). Therefore \(\beta=0\) for every \(x\neq 0\), so
\[
5x-g(x)=0 \implies g(x)=5x.
\]
Since \(g(0)=0\), this holds for all \(x\in\mathbb R\).

Finally, \(g(x)=5x\) is strictly increasing, surjective, and satisfies
\[
g(g(x))=g(5x)=25x=5x+20x=g(x)+20x.
\]

Thus the unique solution is

\[
\boxed{g(x)=5x}.
\]

</details>
