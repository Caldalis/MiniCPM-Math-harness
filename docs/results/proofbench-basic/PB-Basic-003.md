# PB-Basic-003

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Find all functions $f\colon \mathbb{R} \rightarrow \mathbb{R}$ such that for all $a,b \in \mathbb{R}$,
 \[ (b - a)f(f(a)) = a f(a + f(b)). \]"

## Swarm: accepted (best candidate `P2`; self-verification grades [7, 7, 7]; 483,254 tokens in 52 calls)

**Blind grade: Correct (7/7).** Shows two distinct zeros force f(f(a))=0 for all a and hence f=0, so any other solution has the single zero c=f(0), and f(a+f(a))=0 then gives f(a)=c-a for all a; concise, complete and verified.

Let  
\[
F(a)=f(f(a)).
\]
The equation is
\[
(b-a)F(a)=a f(a+f(b)) \qquad \forall a,b\in\mathbb R. \tag{1}
\]

Putting \(a=0\) gives
\[
bF(0)=0 \quad \forall b,
\]
so \(F(0)=0\). Let
\[
c=f(0).
\]
Then
\[
f(c)=f(f(0))=0,
\]
so \(c\) is a zero of \(f\).

Let \(Z=\{x:f(x)=0\}\). If \(z\in Z\), then \(f(z)=0\), and from (1) with \(b=z\),
\[
(z-a)F(a)=a f(a) \qquad \forall a\in\mathbb R. \tag{2}
\]

If \(z_1,z_2\in Z\) are distinct, subtract the two corresponding equations:
\[
(z_1-z_2)F(a)=0,
\]
hence \(F(a)=0\) for all \(a\). Then (2) gives \(a f(a)=0\), so \(f(a)=0\) for all \(a\neq 0\). Also \(F(a)=0\) and \(f(a)=0\) imply
\[
0=F(a)=f(f(a))=f(0),
\]
so \(f(0)=0\). Thus \(f\equiv 0\).

Therefore every nonzero solution has exactly one zero, namely \(c\):
\[
Z=\{c\}.
\]

Now for \(a\neq 0\), set \(b=a\) in the original equation:
\[
0=a f(a+f(a)).
\]
Since \(a\neq 0\),
\[
f(a+f(a))=0.
\]
Thus \(a+f(a)\in Z=\{c\}\), so
\[
a+f(a)=c.
\]
Hence for all \(a\neq 0\),
\[
f(a)=c-a.
\]
Also \(f(0)=c\), so the formula holds for all \(a\in\mathbb R\):
\[
f(x)=c-x.
\]

Finally, check both families.

- If \(f\equiv 0\), then both sides of (1) are \(0\).
- If \(f(x)=c-x\), then
\[
f(f(a))=a,\qquad f(a+f(b))=b-a,
\]
so
\[
(b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
\]

Thus the solutions are
\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x \text{ for some } c\in\mathbb R.}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 22,590 | Correct (7/7) | Case c=f(0) nonzero gives injectivity and f(x)=c-x; case c=0 reduces to af(a+f(b))=(a-b)f(a), giving injectivity for nonzero f and hence f(x)=-x; both families verified, complete. |
| A2 | stop | 22,317 | Correct (7/7) | Non-injective case forces f(f(a)) identically 0 and hence f identically 0; injective case uses the unique zero k=f(0) with f(a+f(a))=0 to get f(x)=k-x; both families verified, complete. |
| A3 | stop | 23,069 | Correct (7/7) | Proves injectivity in both cases (from f(p+f(b))=b-p when p!=0, and from P(a0,b) with f(f(a0))=-f(a0)!=0 when p=0 and f is not 0), then f(a+f(a))=0=f(p) gives f(x)=p-x; complete with verification. |
| A4 | stop | 13,349 | Correct (7/7) | For t=f(0)!=0, f(t+f(b))=b-t gives injectivity and then f(x)=t-x; for t=0 a nonzero zero forces f=0 and otherwise f(x)=-x; complete with verification. |
| A5 | stop | 14,361 | Correct (7/7) | Derives f(f(0))=0 and f(a+f(a))=0, shows f(f(a)) identically 0 forces f identically 0, proves injectivity for nonzero f to get a+f(a)=f(0), and verifies both families; the misprinted intermediate equations (F written for f) are typos that do not affect the valid logic. |
| A6 | stop | 13,166 | Correct (7/7) | Splits on c=f(0): c nonzero gives injectivity via f(c+f(b))=b-c and hence f(x)=c-x; c=0 shows a nonzero zero forces f identically 0 and otherwise f(x)=-x; all cases handled and verified. |
| A7 | stop | 9,760 | Correct (7/7) | Shows that any f other than 0 has some a0 with f(f(a0))!=0, gets injectivity from P(a0,b), and combines f(a+f(a))=0=f(f(0)) with injectivity to get f(x)=f(0)-x; complete, rigorous and verified. |
| A8 | stop | 20,285 | Correct (7/7) | Case f(0)=p nonzero gives f(p+f(b))=b-p, hence bijectivity and f(x)=p-x; case f(0)=0 uses f(f(a))=-f(a) and surjectivity to get f(x)=-x or f identically 0; all cases covered and verified. |
| A9 | stop | 44,127 | Correct (7/7) | Establishes bijectivity and f(f(a)) nonzero for a nonzero, derives f(z+t)=B_t f(z)+C_t, shows B_t=1 so f is affine and then f(x)=K-x, and verifies; the few routine steps left implicit (B_s nonzero, the excluded translation t=-1) follow directly from facts already proved. |
| A10 | stop | 13,551 | Correct (7/7) | Shows two distinct zeros force f(f(a)) identically 0 and then f identically 0, so for nonzero f the only zero is c=f(0) and f(a+f(a))=0 gives f(x)=c-x, with verification of both families. |
| A11 | stop | 19,230 | Correct (7/7) | Shows that two distinct zeros force f(f(a))=0 for all a and then f=0 through a valid image argument, so any other solution has the single zero c=f(0), and a+f(a) in Z gives f(a)=c-a; complete and verified. |
| A12 | stop | 10,425 | Correct (7/7) | Proves injectivity for nonzero f (since f(f(a)) identically 0 would force f identically 0), then f(a+f(a))=0=f(c) yields f(x)=c-x, and verifies both families; complete and rigorous. |
| A13 | stop | 18,755 | Correct (7/7) | Uses P(a,c) and P(a,a+f(a)) to get f(a)f(f(a))=af(a); for c!=0 it shows c is the only zero and f(a)=c-a, and for c=0 it avoids the pointwise trap f(a) in {0,-a} by showing a nonzero zero forces f=0, with verification. |
| A14 | stop | 25,444 | Correct (7/7) | For p=f(0)!=0 it proves bijectivity from f(p+f(b))=b-p and correctly derives f(t)=p-t, handling t=p and t=2p separately, and for p=0 it shows a nonzero zero forces f=0 and otherwise f(a)=-a; all steps check and the answers are verified. |
| A15 | stop | 21,245 | Correct (7/7) | Shows any zero other than t=f(0) forces f(f(a)) identically 0 and hence f identically 0, so for nonzero f the unique zero t together with f(a+f(a))=0 gives f(x)=t-x, with both families verified. |
| A16 | stop | 21,528 | Correct (7/7) | Derives f(f(a))=-f(a+c) and, for every zero x, (c-x)f(a+c)=0, which forces the zero set to be {c} unless f=0, then f(a+f(a))=0 gives f(a)=c-a in both cases c!=0 and c=0, with full verification. |

<details><summary>A1: Correct (7/7)</summary>

\[
\boxed{f(x)\equiv 0 \quad \text{or} \quad f(x)=c-x\ \text{for some } c\in\mathbb R.}
\]

Proof:

Let \(P(a,b)\) denote the given equation:
\[
(b-a)f(f(a))=a f(a+f(b)).
\]

Set \(c=f(0)\). From \(P(0,b)\),
\[
b f(f(0))=0\quad \forall b\in\mathbb R,
\]
so \(f(f(0))=0\). Hence
\[
f(c)=0. \tag{1}
\]

Also \(P(a,a)\) gives
\[
a f(a+f(a))=0,
\]
so for \(a\neq 0\),
\[
f(a+f(a))=0. \tag{2}
\]

### Case 1: \(c\neq 0\)

Using \(P(c,b)\),
\[
(b-c)f(f(c))=c f(c+f(b)).
\]
Since \(f(c)=0\), we have \(f(f(c))=f(0)=c\). Thus
\[
c(b-c)=c f(c+f(b)).
\]
Because \(c\neq 0\),
\[
f(c+f(b))=b-c. \tag{3}
\]

If \(f(b)=f(b')\), then \(c+f(b)=c+f(b')\), so applying \(f\) and using (3),
\[
b-c=f(c+f(b))=f(c+f(b'))=b'-c,
\]
hence \(b=b'\). Therefore \(f\) is injective.

Now from (2), for \(a\neq 0\),
\[
f(a+f(a))=0=f(c).
\]
Injectivity gives
\[
a+f(a)=c,
\]
so
\[
f(a)=c-a.
\]
Also \(f(0)=c=c-0\), hence
\[
f(x)=c-x \qquad \forall x\in\mathbb R.
\]

### Case 2: \(c=0\)

Then \(f(0)=0\). From \(P(a,0)\),
\[
-a f(f(a))=a f(a),
\]
so for \(a\neq 0\),
\[
f(f(a))=-f(a).
\]
Thus the original equation becomes
\[
a f(a+f(b))=(a-b)f(a). \tag{4}
\]

If \(f\equiv 0\), this is a solution.

Otherwise, choose \(t\) with \(f(t)\neq 0\). If \(f(b)=f(b')\), then using (4) with \(a=t\),
\[
t f(t+f(b))=(t-b)f(t),\qquad t f(t+f(b'))=(t-b')f(t).
\]
The left-hand sides are equal, so
\[
(t-b)f(t)=(t-b')f(t).
\]
Since \(f(t)\neq 0\), we get \(b=b'\). Hence \(f\) is injective.

From (2), for \(a\neq 0\),
\[
f(a+f(a))=0=f(0).
\]
Injectivity gives
\[
a+f(a)=0,
\]
so
\[
f(a)=-a \qquad (a\neq 0),
\]
and since \(f(0)=0\), we get
\[
f(x)=-x.
\]

### Verification

- \(f\equiv 0\) clearly works.
- For \(f(x)=c-x\),
\[
f(f(a))=a,\qquad f(a+f(b))=b-a,
\]
so both sides equal \(a(b-a)\). Thus every such function works.

Therefore the complete set of solutions is
\[
\boxed{f(x)\equiv 0 \quad \text{or} \quad f(x)=c-x\ (c\in\mathbb R).}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

Let  
\[
P(a,b):\quad (b-a)f(f(a))=a f(a+f(b)).
\]

### 1. Basic consequences
Set \(a=0\). Then for all \(b\),
\[
b f(f(0))=0.
\]
Hence
\[
f(f(0))=0.
\]
Let
\[
k=f(0).
\]
Then
\[
f(k)=0. \tag{1}
\]

### 2. Non-injective case
Suppose \(f\) is not injective. Then there exist \(u\neq v\) with \(f(u)=f(v)\). Using \(P(a,u)\) and \(P(a,v)\),
\[
(u-a)f(f(a))=a f(a+f(u)),
\]
\[
(v-a)f(f(a))=a f(a+f(v)).
\]
Since \(f(u)=f(v)\), the right-hand sides are equal, so
\[
(u-v)f(f(a))=0.
\]
Because \(u\neq v\), we get
\[
f(f(a))=0 \qquad \forall a.
\]
Thus the original equation becomes
\[
a f(a+f(b))=0 \qquad \forall a,b.
\]
For \(a\neq 0\), this gives
\[
f(a+f(b))=0.
\]
Taking \(b=0\), and using \(f(0)=k\), we get
\[
f(a+k)=0 \qquad \forall a\neq 0.
\]
Together with \(f(k)=0\), this implies \(f\equiv 0\). So the zero function is one solution.

### 3. Injective case
Assume now \(f\) is injective. Since \(f(k)=0\), the preimage of \(0\) is unique, so
\[
f(x)=0 \iff x=k.
\]

Now use \(P(a,a)\):
\[
0=a f(a+f(a)).
\]
For \(a\neq 0\),
\[
f(a+f(a))=0.
\]
By uniqueness of the zero, we get
\[
a+f(a)=k,
\]
so
\[
f(a)=k-a \qquad (a\neq 0).
\]
Also \(f(0)=k\), so the formula holds for all \(a\in\mathbb R\):
\[
f(x)=k-x.
\]

### 4. Verification
Let \(f(x)=c-x\) for arbitrary \(c\in\mathbb R\). Then
\[
f(f(a))=a,
\]
and
\[
f(a+f(b))=f(a+c-b)=c-(a+c-b)=b-a.
\]
Therefore
\[
(b-a)f(f(a))=(b-a)a,
\]
while
\[
a f(a+f(b))=a(b-a).
\]
So every \(f(x)=c-x\) works. Also \(f\equiv 0\) works.

Hence all solutions are
\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x \text{ for some } c\in\mathbb R.}
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

Let  
\[
P(a,b):\quad (b-a)f(f(a))=a f(a+f(b)).
\]
Put \(p=f(0)\).

### 1. Basic consequences
Using \(P(0,b)\):
\[
b f(f(0))=0 \quad \forall b\in\mathbb R,
\]
so
\[
f(f(0))=0 \quad\Rightarrow\quad f(p)=0. \tag{1}
\]

Using \(P(a,a)\):
\[
a f(a+f(a))=0.
\]
For \(a\neq 0\), this gives \(f(a+f(a))=0\), and for \(a=0\) it also gives \(f(f(0))=0\), i.e. \(f(p)=0\). Hence
\[
f(a+f(a))=0 \quad \forall a\in\mathbb R. \tag{2}
\]

### 2. Case \(p\neq 0\)
Using \(P(p,b)\):
\[
(b-p)f(f(p))=p f(p+f(b)).
\]
Since \(f(p)=0\), we have \(f(f(p))=f(0)=p\). Thus
\[
(b-p)p=p f(p+f(b)).
\]
Because \(p\neq 0\),
\[
f(p+f(b))=b-p. \tag{3}
\]

From (3), \(f\) is injective: if \(f(b_1)=f(b_2)\), then
\[
b_1-p=f(p+f(b_1))=f(p+f(b_2))=b_2-p,
\]
so \(b_1=b_2\).

Also \(f\) is surjective: for any \(y\in\mathbb R\), taking \(b=y+p\) gives
\[
f(p+f(y+p))=y.
\]

Now from (2),
\[
f(a+f(a))=0=f(p).
\]
Since \(f\) is injective,
\[
a+f(a)=p,
\]
so
\[
f(a)=p-a.
\]
Thus every solution with \(p\neq 0\) has the form
\[
f(x)=p-x,\qquad p\neq 0.
\]

### 3. Case \(p=0\)
Then \(f(0)=0\). Using \(P(a,0)\):
\[
-a f(f(a))=a f(a).
\]
For \(a\neq 0\),
\[
f(f(a))=-f(a). \tag{4}
\]

If \(f\equiv 0\), this is a solution. Otherwise choose \(a_0\neq 0\) with \(f(a_0)\neq 0\). Then \(f(f(a_0))=-f(a_0)\neq 0\). Using \(P(a_0,b)\):
\[
(b-a_0)f(f(a_0))=a_0 f(a_0+f(b)).
\]
Hence
\[
f(a_0+f(b))=-\frac{f(a_0)}{a_0}(b-a_0),
\]
which, as \(b\) ranges over \(\mathbb R\), takes all real values. Thus \(f\) is surjective.

If \(f(b_1)=f(b_2)\), then \(f(a_0+f(b_1))=f(a_0+f(b_2))\), so
\[
(b_1-a_0)f(f(a_0))=(b_2-a_0)f(f(a_0)).
\]
Since \(f(f(a_0))\neq 0\), we get \(b_1=b_2\). Hence \(f\) is injective.

Finally, from (2),
\[
f(a+f(a))=0=f(0).
\]
Injectivity gives
\[
a+f(a)=0,
\]
so
\[
f(a)=-a.
\]

Thus the nonzero \(p=0\) solution is \(f(x)=-x\).

### 4. Verification
- \(f\equiv 0\) works.
- For \(f(x)=c-x\), \(c\in\mathbb R\):
  \[
  f(f(a))=a,\qquad f(a+f(b))=b-a.
  \]
  Hence
  \[
  (b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
  \]

Therefore all solutions are
\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=c-x \text{ for some } c\in\mathbb R.}
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x\ \text{for some }c\in\mathbb R.}
\]

Proof.

Let
\[
P(a,b):\quad (b-a)f(f(a))=a f(a+f(b)).
\]

### 1. Basic consequences

Taking \(a=b\),
\[
0=a f(a+f(a)),
\]
so for every \(a\ne0\),
\[
f(a+f(a))=0. \tag{1}
\]

Taking \(a=0\),
\[
b f(f(0))=0\quad \forall b\in\mathbb R,
\]
hence
\[
f(f(0))=0.
\]
Let
\[
t=f(0).
\]
Then
\[
f(t)=0. \tag{2}
\]

### 2. Case \(t\ne0\)

Using \(P(t,b)\),
\[
(b-t)f(f(t))=t f(t+f(b)).
\]
Since \(f(t)=0\), we have \(f(f(t))=f(0)=t\). Thus
\[
t(b-t)=t f(t+f(b)).
\]
Because \(t\ne0\),
\[
f(t+f(b))=b-t. \tag{3}
\]

Now if \(f(u)=f(v)\), then \(t+f(u)=t+f(v)\), so applying \(f\) and using (3),
\[
u-t=f(t+f(u))=f(t+f(v))=v-t,
\]
hence \(u=v\). Thus \(f\) is injective.

From (2), \(f(t)=0\), so by injectivity \(t\) is the unique zero of \(f\).

Using (1), for every \(a\ne0\),
\[
f(a+f(a))=0,
\]
so by uniqueness of the zero,
\[
a+f(a)=t.
\]
Therefore, for \(a\ne0\),
\[
f(a)=t-a.
\]
Also \(f(0)=t\), so the same formula holds for \(a=0\). Hence
\[
f(x)=t-x.
\]

### 3. Case \(t=0\)

Then \(f(0)=0\). Taking \(b=0\) in the original equation,
\[
-a f(f(a))=a f(a).
\]
For \(a\ne0\),
\[
f(f(a))=-f(a). \tag{4}
\]

Now suppose \(b\) is a zero of \(f\), i.e. \(f(b)=0\). Then
\[
(b-a)f(f(a))=a f(a+f(b))=a f(a).
\]
Using (4),
\[
-(b-a)f(a)=a f(a),
\]
so
\[
-b f(a)=0.
\]
Thus, for every zero \(b\),
\[
b f(a)=0\quad \forall a\in\mathbb R. \tag{5}
\]

If there exists a nonzero zero \(b\), then (5) gives \(f(a)=0\) for all \(a\), so
\[
f\equiv0.
\]

Otherwise, the only zero is \(0\). From (1), for every \(a\ne0\),
\[
f(a+f(a))=0,
\]
so
\[
a+f(a)=0.
\]
Hence
\[
f(a)=-a\quad (a\ne0),
\]
and since \(f(0)=0\),
\[
f(x)=-x.
\]

This is included in the family \(f(x)=c-x\) with \(c=0\).

### 4. Verification

First, \(f\equiv0\) works, since both sides are identically \(0\).

Second, let \(f(x)=c-x\) with \(c\in\mathbb R\). Then
\[
f(f(a))=f(c-a)=c-(c-a)=a,
\]
and
\[
f(a+f(b))=f(a+c-b)=c-(a+c-b)=b-a.
\]
Thus
\[
(b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
\]
So every such function works.

Therefore the complete list is

\[
\boxed{f\equiv0 \quad \text{or} \quad f(x)=c-x\ (c\in\mathbb R).}
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

Let  
\[
P(a,b):\quad (b-a)f(f(a))=a f(a+f(b)).
\]

We will prove that the only solutions are
\[
f\equiv 0
\]
and
\[
f(x)=c-x \qquad (c\in\mathbb R).
\]

Set \(t=f(0)\).

### 1. Basic consequences
Putting \(a=0\) in \(P(a,b)\),
\[
b f(f(0))=0 \qquad \forall b\in\mathbb R.
\]
Hence
\[
f(f(0))=0,
\]
so
\[
f(t)=0. \tag{1}
\]

Putting \(b=a\),
\[
aF(a)=aF(a+f(a)), \qquad F(a):=f(f(a)).
\]
For \(a\neq 0\), this gives
\[
f(a+f(a))=0. \tag{2}
\]
For \(a=0\), (1) already gives \(f(t)=0=f(0+f(0))\). Thus (2) holds for all \(a\in\mathbb R\).

### 2. The zero function is the only solution with \(F\equiv 0\)
Suppose \(F\equiv 0\). Using \(P(a,0)\),
\[
-aF(a)=aF(a+t).
\]
Since \(F\equiv 0\), we get
\[
aF(a+t)=0 \qquad \forall a\in\mathbb R.
\]
For \(a\neq 0\), this gives \(f(a+t)=0\). Since \(a+t\) ranges over all real numbers as \(a\) varies, \(f\equiv 0\). This function clearly works.

### 3. Every nonzero solution is injective
Assume now that \(f\not\equiv 0\). Then \(F\not\equiv 0\). Indeed, \(F\equiv 0\) would force \(f\equiv 0\).

Suppose \(f(u)=f(v)\). Applying \(P(a,u)\) and \(P(a,v)\),
\[
(u-a)F(a)=a f(a+f(u))=a f(a+f(v))=(v-a)F(a).
\]
Thus
\[
(u-v)F(a)=0 \qquad \forall a\in\mathbb R.
\]
Since \(F\not\equiv 0\), choose \(a_0\) with \(F(a_0)\neq 0\). Then \(u=v\). Hence \(f\) is injective.

### 4. Determine \(f\) from injectivity
From (2),
\[
f(a+f(a))=0.
\]
By (1), \(f(t)=0\). Since \(f\) is injective, the unique preimage of \(0\) is \(t\). Therefore
\[
a+f(a)=t,
\]
so
\[
f(a)=t-a.
\]
Thus every nonzero solution has the form
\[
f(x)=t-x
\]
for some \(t\in\mathbb R\).

### 5. Verification
- \(f\equiv 0\) works.
- For \(f(x)=t-x\),
  \[
  f(f(a))=f(t-a)=a,
  \]
  and
  \[
  f(a+f(b))=f(a+t-b)=t-(a+t-b)=b-a.
  \]
  Hence
  \[
  (b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
  \]
  So these functions work for every \(t\in\mathbb R\).

Therefore the complete set of solutions is
\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=c-x\ \text{for some }c\in\mathbb R.}
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x\ \text{for some } c\in\mathbb R.}
\]

Proof.

Let the given equation be \(P(a,b)\):
\[
(b-a)f(f(a))=a f(a+f(b)).
\]

Set \(c=f(0)\). Taking \(a=0\) in \(P(0,b)\),
\[
b f(f(0))=0 \qquad \forall b\in\mathbb R,
\]
so
\[
f(f(0))=0 \implies f(c)=0.
\]

Now use \(P(a,c)\):
\[
(c-a)f(f(a))=a f(a+f(c))=a f(a). \tag{1}
\]

### Case 1: \(c\neq 0\)

Using \(P(c,b)\),
\[
(b-c)f(f(c))=c f(c+f(b)).
\]
Since \(f(c)=0\), we have \(f(f(c))=f(0)=c\), hence
\[
(b-c)c=c f(c+f(b)).
\]
Because \(c\neq 0\),
\[
f(c+f(b))=b-c. \tag{2}
\]

From (2), \(f\) is injective: if \(f(u)=f(v)\), then
\[
u-c=f(c+f(u))=f(c+f(v))=v-c,
\]
so \(u=v\).

Now \(P(a,a)\) gives
\[
a f(a+f(a))=0.
\]
For \(a\neq 0\),
\[
f(a+f(a))=0.
\]
But \(f(c)=0\) and \(f\) is injective, so
\[
a+f(a)=c,
\]
hence
\[
f(a)=c-a \qquad (a\neq 0).
\]
Also \(f(0)=c\), so
\[
f(x)=c-x \qquad \forall x\in\mathbb R.
\]

### Case 2: \(c=0\)

Then \(f(0)=0\). From \(P(a,0)\),
\[
-a f(f(a))=a f(a),
\]
so for \(a\neq 0\),
\[
f(f(a))=-f(a). \tag{3}
\]
Also \(P(a,a)\) gives
\[
f(a+f(a))=0 \qquad (a\neq 0). \tag{4}
\]

If there exists \(b\neq 0\) with \(f(b)=0\), then using \(P(a,b)\) for \(a\neq 0\),
\[
(b-a)f(f(a))=a f(a).
\]
By (3),
\[
(b-a)(-f(a))=a f(a),
\]
so
\[
(a-b)f(a)=a f(a),
\]
hence
\[
-b f(a)=0.
\]
Since \(b\neq 0\), we get \(f(a)=0\) for all \(a\neq 0\), and \(f(0)=0\). Thus
\[
f\equiv 0.
\]

Otherwise, \(f\) has no nonzero zero. From (4), for every \(a\neq 0\), \(a+f(a)\) is a zero of \(f\), hence must be \(0\). Therefore
\[
f(a)=-a \qquad (a\neq 0),
\]
and since \(f(0)=0\),
\[
f(x)=-x.
\]
This is included in the family \(f(x)=c-x\) with \(c=0\).

### Verification

1. If \(f\equiv 0\), both sides are \(0\).

2. If \(f(x)=c-x\), then
\[
f(f(a))=a,
\]
and
\[
f(a+f(b))=f(a+c-b)=c-(a+c-b)=b-a.
\]
Therefore
\[
(b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
\]
So every such function works.

Hence the complete set of solutions is
\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x\ (c\in\mathbb R).}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=c-x\ \text{for some }c\in\mathbb R}
\]

Proof.

Let
\[
P(a,b):\quad (b-a)f(f(a))=a f(a+f(b)).
\]
Set \(c=f(0)\).

### 1. Basic facts
From \(P(0,b)\),
\[
b f(f(0))=0 \quad \forall b\in\mathbb R,
\]
so
\[
f(f(0))=0.
\]
Since \(f(0)=c\), this gives
\[
f(c)=0. \tag{1}
\]

Also, from \(P(a,a)\),
\[
0=a f(a+f(a)).
\]
Thus for every \(a\ne 0\),
\[
f(a+f(a))=0. \tag{2}
\]

### 2. The zero function
If \(f\equiv 0\), then both sides of the equation are \(0\), so \(f\equiv 0\) is a solution.

Now assume \(f\not\equiv 0\).

### 3. Nonzero solutions are injective
Suppose first that \(f(f(t))=0\) for all \(t\). Using \(P(t,0)\),
\[
-t f(f(t))=t f(t+f(0)).
\]
Since \(f(f(t))=0\), for \(t\ne 0\),
\[
f(t+c)=0.
\]
Hence \(f\) vanishes everywhere except possibly at \(c\). But \(f(c)=0\) by (1), so \(f\equiv 0\), contradiction.

Therefore there exists \(a_0\in\mathbb R\) such that
\[
f(f(a_0))\ne 0.
\]

Now take \(b,d\in\mathbb R\) with \(f(b)=f(d)\). Using \(P(a_0,b)\) and \(P(a_0,d)\),
\[
(b-a_0)f(f(a_0))=a_0 f(a_0+f(b)),
\]
\[
(d-a_0)f(f(a_0))=a_0 f(a_0+f(d)).
\]
Since \(f(b)=f(d)\), the right-hand sides are equal. Subtracting gives
\[
(b-d)f(f(a_0))=0.
\]
Because \(f(f(a_0))\ne 0\), we get \(b=d\). Hence \(f\) is injective.

### 4. Determine the form of \(f\)
From (2), for every \(a\ne 0\),
\[
f(a+f(a))=0=f(c).
\]
Since \(f\) is injective,
\[
a+f(a)=c.
\]
Thus for all \(a\ne 0\),
\[
f(a)=c-a.
\]
For \(a=0\), this also holds because \(f(0)=c\). Hence
\[
f(x)=c-x \quad \forall x\in\mathbb R.
\]

### 5. Verification
If \(f(x)=c-x\), then
\[
f(f(a))=a,
\]
and
\[
f(a+f(b))=f(a+c-b)=c-(a+c-b)=b-a.
\]
Therefore
\[
(b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
\]
So every \(f(x)=c-x\) works. The zero function also works.

Thus
\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=c-x\ \text{for some }c\in\mathbb R.}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x \ \ (c\in\mathbb R)}
\]

Proof:

Let \(p=f(0)\). Setting \(a=0\) in
\[
(b-a)f(f(a))=a f(a+f(b))
\]
gives
\[
b f(f(0))=0 \quad \forall b\in\mathbb R,
\]
so
\[
f(f(0))=0.
\]
Since \(f(0)=p\), this means
\[
f(p)=0. \tag{1}
\]

### Case 1: \(p\neq 0\)

Set \(a=p\) in the original equation:
\[
(b-p)f(f(p))=p f(p+f(b)).
\]
Using \(f(p)=0\), we have \(f(f(p))=f(0)=p\), hence
\[
p(b-p)=p f(p+f(b)).
\]
Since \(p\neq 0\),
\[
f(p+f(b))=b-p. \tag{2}
\]

From (2), \(f\) is surjective: for any \(y\in\mathbb R\), take \(b=y+p\), then
\[
f(p+f(y+p))=y.
\]
Also, if \(f(b_1)=f(b_2)\), then \(p+f(b_1)=p+f(b_2)\), so applying \(f\) gives
\[
b_1-p=b_2-p,
\]
hence \(b_1=b_2\). Thus \(f\) is injective, hence bijective.

Now for \(a\neq 0\), we claim \(f(f(a))\neq 0\). Indeed, since \(f^{-1}(0)=p\), if \(f(f(a))=0\), then \(f(a)=p=f(0)\), so \(a=0\), contradiction.

For \(a\neq 0\), choose \(b=f^{-1}(p-a)\). Then
\[
f(b)=p-a,
\]
so
\[
a+f(b)=p.
\]
Substituting into the original equation:
\[
(b-a)f(f(a))=a f(p)=0.
\]
Since \(a\neq 0\) and \(f(f(a))\neq 0\), we must have \(b=a\). Therefore
\[
f(a)=p-a.
\]
This also holds for \(a=0\), so
\[
f(x)=p-x.
\]
Thus every \(p\neq 0\) gives a solution
\[
f(x)=p-x.
\]

### Case 2: \(p=0\)

Then \(f(0)=0\). Setting \(b=0\) gives, for \(a\neq 0\),
\[
f(f(a))=-f(a). \tag{3}
\]
Also, for \(a\neq 0\), the original equation becomes
\[
f(a+f(b))=\frac{a-b}{a}f(a). \tag{4}
\]

If there exists \(a\neq 0\) with \(f(a)\neq 0\), then as \(b\) varies, the right-hand side of (4) takes all real values. Hence \(f\) is surjective. Now for any \(y\neq 0\), choose \(x\neq 0\) with \(f(x)=y\). By (3),
\[
f(y)=f(f(x))=-f(x)=-y.
\]
Also \(f(0)=0\), so
\[
f(y)=-y \quad \forall y\in\mathbb R.
\]
Thus
\[
f(x)=-x,
\]
which is the case \(c=0\) in \(f(x)=c-x\).

If no such \(a\neq 0\) exists, then \(f(a)=0\) for all \(a\neq 0\), and since \(f(0)=0\), we get
\[
f\equiv 0.
\]

### Verification

- \(f\equiv 0\) works: both sides are identically \(0\).
- For \(f(x)=c-x\), \(c\in\mathbb R\), we have
\[
f(f(a))=a,\qquad f(a+f(b))=b-a.
\]
Thus
\[
(b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
\]

Therefore the complete set of solutions is

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x,\ c\in\mathbb R.}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x \text{ for some } c\in\mathbb R.}
\]

Proof.

Let
\[
F(x)=f(f(x)).
\]
The equation is
\[
(b-a)F(a)=a f(a+f(b)). \tag{1}
\]

### 1. The zero function works
If \(f\equiv 0\), then both sides are \(0\).

Now assume \(f\not\equiv 0\).

### 2. \(f\) is bijective

Putting \(a=0\) in (1),
\[
bF(0)=0 \quad \forall b,
\]
so \(F(0)=0\). In particular,
\[
F(0)=f(f(0))=0.
\]

Suppose \(F(a)=0\) for every \(a\neq 0\). Then from (1), for every \(a\neq 0\),
\[
f(a+f(b))=0.
\]
This forces \(f\equiv 0\), contradiction. Hence there exists \(a_0\neq 0\) with \(F(a_0)\neq 0\).

From (1) with \(a=a_0\),
\[
f(a_0+f(b))=\frac{F(a_0)}{a_0}(b-a_0).
\]
Since the coefficient of \(b\) is nonzero, \(f\) is both injective and surjective. Thus \(f\) is bijective.

Let \(p=f(0)\). From \(F(0)=0\), we get
\[
f(p)=0.
\]
Because \(f\) is injective, \(p\) is the unique preimage of \(0\). If \(F(a)=0\) for some \(a\neq 0\), then \(f(f(a))=0\), so \(f(a)=p=f(0)\), hence \(a=0\), contradiction. Therefore
\[
F(a)\neq 0 \quad \forall a\neq 0.
\]
In particular,
\[
M:=F(1)\neq 0.
\]

### 3. Deriving the affine form

Put \(g=f^{-1}\). From (1) with \(a=1\),
\[
f(1+f(b))=M(b-1).
\]
Writing \(y=f(b)\), so \(b=g(y)\), gives
\[
f(1+y)=M(g(y)-1),
\]
hence
\[
g(y)=1+\frac{f(1+y)}M. \tag{2}
\]

Now for \(a\neq 0\), using (1) again,
\[
f(a+y)=\frac{F(a)}a\bigl(g(y)-a\bigr).
\]
Using (2), with \(t=a-1\),
\[
f(z+t)=B_t f(z)+C_t, \tag{3}
\]
where \(t\neq -1\) and
\[
B_t=\frac{F(t+1)}{(t+1)M},\qquad C_t=-t F(t+1)/(t+1).
\]

Apply (3) twice:
\[
f(z+t+s)=B_s f(z+t)+C_s
=B_sB_t f(z)+B_sC_t+C_s.
\]
Comparing with (3) for \(t+s\), we get
\[
B_{t+s}=B_sB_t,\qquad C_{t+s}=B_sC_t+C_s.
\]
But
\[
C_t=-tB_tM,
\]
so
\[
C_{t+s}=-(t+s)M B_sB_t,
\]
while
\[
B_sC_t+C_s=-MB_s(tB_t+s).
\]
Thus
\[
(t+s)B_t=tB_t+s,
\]
so
\[
sB_t=s.
\]
For every fixed \(t\neq -1\), we may choose \(s\neq 0\) with \(t+s\neq -1\), hence \(B_t=1\). Therefore
\[
B_t=1 \quad (t\neq -1),
\]
so
\[
F(a)=Ma \quad (a\neq 0).
\]
Then (3) becomes
\[
f(z+t)=f(z)-Mt \quad (t\neq -1).
\]
Thus
\[
h(x):=f(x)+Mx
\]
is invariant under all translations, so \(h\) is constant. Hence
\[
f(x)=K-Mx.
\]

Now
\[
F(x)=f(f(x))=K(1-M)+M^2x.
\]
But we already know \(F(x)=Mx\), so
\[
K(1-M)+M^2x=Mx.
\]
Comparing coefficients gives \(M^2=M\) and \(K(1-M)=0\). Since \(M\neq 0\), we get \(M=1\). Therefore
\[
f(x)=K-x.
\]

### 4. Verification

- \(f\equiv 0\) clearly works.
- For \(f(x)=c-x\),
\[
f(f(a))=a,
\]
and
\[
f(a+f(b))=f(a+c-b)=b-a.
\]
Thus
\[
(b-a)f(f(a))=a(b-a)=a f(a+f(b)).
\]

Hence all solutions are
\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x\ \forall x\in\mathbb R,\ c\in\mathbb R.}
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

Let  
\[
P(a,b):\quad (b-a)f(f(a))=a f(a+f(b)).
\]

Set \(c=f(0)\). Taking \(a=0\) in \(P(a,b)\),
\[
b f(f(0))=0 \quad \forall b\in\mathbb R,
\]
so \(f(f(0))=0\). Hence
\[
f(c)=0. \tag{1}
\]

Now take \(b=a\). Then
\[
a f(a+f(a))=0.
\]
For every \(a\ne 0\),
\[
f(a+f(a))=0. \tag{2}
\]

We next show that a nonzero solution has only one zero.

Suppose \(u,v\) are two distinct zeros of \(f\), i.e. \(f(u)=f(v)=0\). Using the original equation with \(b=u\) and \(b=v\),
\[
(u-a)f(f(a))=a f(a+f(u))=a f(a),
\]
and similarly
\[
(v-a)f(f(a))=a f(a).
\]
Subtracting gives
\[
(u-v)f(f(a))=0.
\]
Since \(u\ne v\), we get
\[
f(f(a))=0 \quad \forall a.
\]
Now use \(b=0\) in the original equation:
\[
-a f(f(a))=a f(a+c).
\]
Since \(f(f(a))=0\), for \(a\ne 0\),
\[
f(a+c)=0.
\]
Together with \(f(c)=0\), this gives \(f\equiv 0\). Therefore, if \(f\not\equiv 0\), it has at most one zero. But from (1), \(c\) is a zero, so the only zero is \(c\).

Thus for every \(a\ne 0\), by (2),
\[
a+f(a)=c,
\]
so
\[
f(a)=c-a \quad (a\ne 0).
\]
Also \(f(0)=c\), hence
\[
f(x)=c-x \quad \forall x\in\mathbb R.
\]

It remains to check these functions work.

1. \(f\equiv 0\) clearly works.

2. For \(f(x)=c-x\), we have
\[
f(f(a))=f(c-a)=a,
\]
and
\[
f(a+f(b))=f(a+c-b)=c-(a+c-b)=b-a.
\]
Therefore
\[
(b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
\]
So every \(f(x)=c-x\) with \(c\in\mathbb R\) works.

Hence the solutions are
\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x \text{ for some } c\in\mathbb R.}
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=c-x\ \text{for some }c\in\mathbb R}
\]

Proof:

Let
\[
Z=\{x\in\mathbb R:f(x)=0\}.
\]

Putting \(a=0\) in the given equation gives
\[
b f(f(0))=0 \qquad \forall b\in\mathbb R,
\]
so
\[
f(f(0))=0.
\]
Set
\[
c=f(0).
\]
Then \(f(c)=0\), hence \(c\in Z\).

Now put \(b=a\):
\[
0=a f(a+f(a)).
\]
For \(a\ne 0\), this gives \(f(a+f(a))=0\). For \(a=0\), we already have \(f(c)=0\). Hence for every \(a\in\mathbb R\),
\[
a+f(a)\in Z. \tag{1}
\]

We next show that if \(Z\) has two distinct elements, then \(f\equiv 0\). Suppose \(z_1,z_2\in Z\), \(z_1\ne z_2\). Since \(f(z_i)=0\), using the original equation with \(b=z_i\) gives
\[
(z_i-a)f(f(a))=a f(a) \qquad \forall a\in\mathbb R.
\]
Subtracting the two equations for \(i=1,2\),
\[
(z_1-z_2)f(f(a))=0,
\]
so
\[
f(f(a))=0 \qquad \forall a\in\mathbb R. \tag{2}
\]
Then the original equation becomes
\[
a f(a+f(b))=0 \qquad \forall a,b\in\mathbb R.
\]
In particular, for \(a\ne 0\),
\[
f(a+f(b))=0. \tag{3}
\]

Now (2) implies that every value in the image of \(f\) is a zero of \(f\): if \(y=f(a)\), then \(f(y)=0\).

If the image of \(f\) has at least two elements, then for any \(x\in\mathbb R\):
- if \(x\) is in the image, then \(f(x)=0\);
- if \(x\) is not in the image, choose \(y\in f(\mathbb R)\) with \(y\ne x\), say \(y=f(b)\). Then \(a=x-y\ne 0\), so by (3),
  \[
  f(x)=f(a+f(b))=0.
  \]
Thus \(f\equiv 0\).

If the image is a singleton, say \(f\equiv y_0\), then \(f(y_0)=y_0\), but also \(y_0\) is in the image, so \(f(y_0)=0\), forcing \(y_0=0\), hence \(f\equiv 0\).

Therefore, if \(f\not\equiv 0\), then \(Z\) has exactly one element. Since \(c\in Z\), we have
\[
Z=\{c\}.
\]
By (1), for every \(a\),
\[
a+f(a)=c,
\]
so
\[
f(a)=c-a.
\]

Thus every nonzero solution has the form \(f(x)=c-x\).

Finally, verify:

- \(f\equiv 0\) clearly works.
- If \(f(x)=c-x\), then
  \[
  f(f(a))=a,
  \]
  and
  \[
  f(a+f(b))=f(a+c-b)=c-(a+c-b)=b-a.
  \]
  Hence
  \[
  (b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
  \]

So the complete set of solutions is

\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=c-x\ (c\in\mathbb R).}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

Let  
\[
P(a,b):\quad (b-a)f(f(a))=a f(a+f(b)).
\]

Set \(c=f(0)\).

### 1. First observations
Taking \(a=0\):
\[
b f(f(0))=0 \qquad \forall b\in\mathbb R.
\]
Hence
\[
f(f(0))=0,
\]
so
\[
f(c)=0.
\]

Now suppose \(f\not\equiv 0\). We show \(f\) is injective.  
If \(f(x)=f(y)\), then for every \(a\),
\[
(x-a)f(f(a))=a f(a+f(x))=a f(a+f(y))=(y-a)f(f(a)).
\]
Thus
\[
(x-y)f(f(a))=0 \qquad \forall a.
\]
If \(x\ne y\), then \(f(f(a))=0\) for all \(a\), so the original equation gives
\[
a f(a+f(b))=0.
\]
For \(a\ne 0\), this implies \(f(a+f(b))=0\). Taking \(b=0\), we get
\[
f(a+c)=0 \qquad \forall a,
\]
so \(f\equiv 0\), contradiction. Therefore \(x=y\), and \(f\) is injective.

### 2. Determine the form of a nonzero solution
Using \(P(a,a)\):
\[
0=a f(a+f(a)).
\]
For \(a\ne 0\),
\[
f(a+f(a))=0.
\]
But \(f(c)=0\), and \(f\) is injective, so
\[
a+f(a)=c.
\]
Thus for \(a\ne 0\),
\[
f(a)=c-a.
\]
This also holds at \(a=0\), since \(f(0)=c\). Hence
\[
f(x)=c-x \qquad \forall x\in\mathbb R.
\]

### 3. Verify the solutions

First, \(f\equiv 0\) works:
\[
(b-a)f(f(a))=0,\qquad a f(a+f(b))=0.
\]

Second, let \(f(x)=c-x\) for arbitrary \(c\in\mathbb R\). Then
\[
f(f(a))=a,
\]
and
\[
f(a+f(b))=f(a+c-b)=c-(a+c-b)=b-a.
\]
Therefore
\[
(b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
\]
So these functions work.

Hence all solutions are
\[
\boxed{f(x)\equiv 0 \quad \text{or} \quad f(x)=c-x \text{ for some } c\in\mathbb R.}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=C-x \text{ for some } C\in\mathbb R}
\]

Proof:

Let \(P(a,b)\) denote the given equation:
\[
(b-a)f(f(a))=a f(a+f(b)).
\]
Put \(c=f(0)\).

From \(P(0,b)\),
\[
b f(f(0))=0 \quad \forall b,
\]
so \(f(f(0))=0\). Hence
\[
f(c)=0. \tag{1}
\]

Using \(P(a,c)\), since \(f(c)=0\),
\[
(c-a)f(f(a))=a f(a). \tag{2}
\]

Also, from \(P(a,a)\),
\[
a f(a+f(a))=0.
\]
For \(a\neq 0\), this gives \(f(a+f(a))=0\); for \(a=0\) it also holds because \(f(c)=0\). Therefore applying \(P(a,a+f(a))\) gives
\[
f(a)f(f(a))=a f(a). \tag{3}
\]

### Case 1: \(c\neq 0\)

If \(f(a)=0\), then using (2),
\[
(c-a)c=0,
\]
so \(a=c\). Thus the only zero of \(f\) is \(a=c\).

Hence for \(a\neq c\), \(f(a)\neq 0\). From (3),
\[
f(f(a))=a.
\]
Substituting into (2),
\[
(c-a)a=a f(a).
\]
For \(a\neq 0\), this gives
\[
f(a)=c-a.
\]
Together with \(f(0)=c\) and \(f(c)=0\), we obtain
\[
f(x)=c-x \quad \forall x\in\mathbb R.
\]

### Case 2: \(c=0\)

Then \(f(0)=0\). From (2),
\[
-a f(f(a))=a f(a),
\]
so for all \(a\),
\[
f(f(a))=-f(a). \tag{4}
\]
Using (3) and (4),
\[
-f(a)^2=a f(a),
\]
hence
\[
f(a)(a+f(a))=0. \tag{5}
\]

If \(f\equiv 0\), this is a solution.

Otherwise, choose \(t\) with \(f(t)\neq 0\). Then by (5),
\[
f(t)=-t,
\]
so \(t\neq 0\). If \(z\neq 0\) and \(f(z)=0\), then using \(P(a,z)\),
\[
(z-a)f(f(a))=a f(a).
\]
By (4), this becomes
\[
(z-a)(-f(a))=a f(a),
\]
which simplifies to
\[
z f(a)=0.
\]
Since \(z\neq 0\), this forces \(f(a)=0\) for all \(a\), contradiction. Therefore \(f(a)\neq 0\) for all \(a\neq 0\). By (5),
\[
f(a)=-a \quad (a\neq 0),
\]
and \(f(0)=0\). Hence
\[
f(x)=-x.
\]

Finally, both families are checked:

- \(f\equiv 0\) works trivially.
- For \(f(x)=C-x\),
\[
f(f(a))=a,\qquad f(a+f(b))=b-a,
\]
so both sides equal \(a(b-a)\).

Thus the complete set of solutions is
\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=C-x\ (C\in\mathbb R).}
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=c-x\ \text{for some }c\in\mathbb R.}
\]

Proof.

Let \(p=f(0)\). Taking \(a=0\) in
\[
(b-a)f(f(a))=a f(a+f(b))
\]
gives
\[
b f(f(0))=0\quad\forall b,
\]
so
\[
f(p)=0.
\]

### Case 1: \(p\neq 0\)

Putting \(a=p\) gives, since \(f(p)=0\) and \(f(f(p))=f(0)=p\),
\[
f(p+f(b))=b-p. \tag{1}
\]
This implies \(f\) is bijective: surjectivity is clear by choosing \(b=y+p\), and injectivity follows because if \(f(b_1)=f(b_2)\), then
\[
b_1-p=f(p+f(b_1))=f(p+f(b_2))=b_2-p.
\]

Let \(F(a)=f(f(a))\). From \(b=p\) in the original equation,
\[
(p-a)F(a)=a f(a). \tag{2}
\]
Using \(b=f^{-1}(y)\) in the original equation,
\[
a f(a+y)=(f^{-1}(y)-a)F(a).
\]
From (1),
\[
f^{-1}(y)=f(p+y)+p.
\]
Substituting (2) into the previous identity, for \(a\neq 0,p\),
\[
f(a+y)=\frac{f(a)}{p-a}\bigl(f(p+y)+p-a\bigr). \tag{3}
\]
Set \(y=p-a\). Then
\[
0=f(p)=\frac{f(a)}{p-a}\bigl(f(2p-a)+p-a\bigr).
\]
Since \(f\) is injective and \(f(p)=0\), we have \(f(a)\neq 0\) for \(a\neq p\). Hence
\[
f(2p-a)=a-p.
\]
Letting \(t=2p-a\), this gives
\[
f(t)=p-t
\]
for all \(t\neq p,2p\). Also \(f(p)=0\) and from (1) with \(b=0\), \(f(2p)=-p\), so the formula holds for all \(t\). Thus
\[
f(x)=p-x.
\]

### Case 2: \(p=0\)

Then \(f(0)=0\). Taking \(b=0\),
\[
-a f(f(a))=a f(a),
\]
so for \(a\neq 0\),
\[
f(f(a))=-f(a). \tag{4}
\]

If there exists \(b\neq 0\) with \(f(b)=0\), then comparing the original equation for \(b\) and for \(0\) gives
\[
b f(f(a))=0\quad\forall a.
\]
Since \(b\neq 0\), this implies \(f(f(a))=0\) for all \(a\), and then \(a f(a)=0\), so \(f\equiv 0\).

If \(f\not\equiv 0\), then the only zero of \(f\) is \(0\). Taking \(a=b\) in the original equation gives
\[
0=a f(a+f(a)).
\]
For \(a\neq 0\), this implies \(f(a+f(a))=0\), hence
\[
a+f(a)=0,
\]
so
\[
f(a)=-a.
\]
Thus \(f(x)=-x\).

Finally, direct verification:

- \(f\equiv 0\) works.
- For \(f(x)=c-x\),
\[
f(f(a))=a,\qquad f(a+f(b))=b-a,
\]
so both sides equal \(a(b-a)\).

Therefore the complete set of solutions is

\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=c-x\ (c\in\mathbb R).}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=c-x\ \text{for some }c\in\mathbb R.}
\]

Proof.

Let \(t=f(0)\). Denote \(F(a)=f(f(a))\). The equation is
\[
(b-a)F(a)=a f(a+f(b)). \tag{P(a,b)}
\]

From \(a=0\),
\[
b f(f(0))=0 \quad \forall b\in\mathbb R,
\]
so
\[
f(t)=0. \tag{1}
\]

Now let \(z\in\mathbb R\) be such that \(f(z)=0\). Using \(P(a,z)\) and \(P(a,t)\), both have right-hand side \(a f(a)\), hence
\[
(z-a)F(a)=(t-a)F(a),
\]
so
\[
(z-t)F(a)=0 \quad \forall a. \tag{2}
\]

If \(z\neq t\), then \(F(a)=0\) for all \(a\). Thus \(f(f(a))=0\) for all \(a\). From \(P(a,t)\),
\[
a f(a)=(t-a)F(a)=0,
\]
so \(f(a)=0\) for all \(a\neq 0\). In particular \(f(1)=0\), hence
\[
F(1)=f(f(1))=f(0)=t.
\]
But \(F(1)=0\), so \(t=0\), and therefore \(f(0)=0\). Thus \(f\equiv 0\).

Hence, if \(f\not\equiv 0\), the only zero of \(f\) is \(t\):
\[
f(x)=0 \iff x=t. \tag{3}
\]

Next, we show \(f\) is injective. Suppose \(f(u)=f(v)\). Then for all \(a\),
\[
(u-a)F(a)=a f(a+f(u))=a f(a+f(v))=(v-a)F(a),
\]
so
\[
(u-v)F(a)=0 \quad \forall a.
\]
If \(u\neq v\), then \(F(a)=0\) for all \(a\), forcing \(f\equiv 0\), contradiction. Thus \(u=v\). So \(f\) is injective.

Now put \(b=a\) in the original equation:
\[
0=a f(a+f(a)).
\]
For \(a\neq 0\), this gives
\[
f(a+f(a))=0.
\]
By (3), \(a+f(a)=t\). Thus
\[
f(a)=t-a \quad (a\neq 0).
\]
Also \(f(0)=t\), so the formula holds for all \(a\in\mathbb R\):
\[
f(x)=t-x.
\]
Letting \(c=t\), we get
\[
f(x)=c-x.
\]

Finally, check that these functions work. If \(f\equiv 0\), both sides are \(0\). If \(f(x)=c-x\), then
\[
f(f(a))=a,\qquad f(a+f(b))=b-a,
\]
so
\[
(b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
\]
Thus all such functions work.

\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=c-x\ (c\in\mathbb R).}
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=C-x \text{ for some } C\in\mathbb R.}
\]

Proof.

Let the given equation be
\[
(b-a)f(f(a))=a f(a+f(b)) \qquad \forall a,b\in\mathbb R.
\]
Put \(c=f(0)\).

### 1. Basic consequences
Taking \(a=0\),
\[
b f(f(0))=0 \quad \forall b\in\mathbb R,
\]
so
\[
f(f(0))=0 \implies f(c)=0.
\]
Taking \(b=0\),
\[
-a f(f(a))=a f(a+c).
\]
For \(a\ne 0\),
\[
f(f(a))=-f(a+c),
\]
and this also holds for \(a=0\). Thus
\[
f(f(a))=-f(a+c). \tag{1}
\]

Taking \(b=a\),
\[
0=a f(a+f(a)).
\]
Hence for \(a\ne 0\), \(f(a+f(a))=0\), and also for \(a=0\), \(f(f(0))=0\). Therefore
\[
f(a+f(a))=0 \quad \forall a\in\mathbb R. \tag{2}
\]

Let
\[
Z=\{x\in\mathbb R: f(x)=0\}.
\]
Then \(c\in Z\).

### 2. Structure of the zero set
If \(x\in Z\), then \(f(x)=0\). Using the original equation with \(b=x\),
\[
(x-a)f(f(a))=a f(a+f(x))=a f(a).
\]
By (1),
\[
(a-x)f(a+c)=a f(a). \tag{3}
\]
In particular, taking \(x=c\),
\[
(a-c)f(a+c)=a f(a). \tag{4}
\]
Subtracting (4) from (3),
\[
(c-x)f(a+c)=0 \quad \forall a\in\mathbb R. \tag{5}
\]

### 3. Case \(c\ne 0\)
If \(x\in Z\) and \(x\ne c\), then \(c-x\ne 0\), so (5) gives
\[
f(a+c)=0 \quad \forall a\in\mathbb R,
\]
hence \(f\equiv 0\), contradicting \(f(0)=c\ne 0\). Therefore the only zero is \(c\):
\[
Z=\{c\}.
\]
From (2),
\[
f(a+f(a))=0,
\]
so \(a+f(a)=c\). Hence
\[
f(a)=c-a \quad \forall a\in\mathbb R.
\]

### 4. Case \(c=0\)
Now \(f(0)=0\). If \(f\equiv 0\), this is one solution.

Assume \(f\not\equiv 0\). From (3) with \(c=0\), for every \(x\in Z\),
\[
(a-x)f(a)=a f(a),
\]
so
\[
-x f(a)=0 \quad \forall a\in\mathbb R.
\]
If \(x\ne 0\), then \(f\equiv 0\), contradiction. Hence \(Z=\{0\}\). By (2),
\[
a+f(a)=0 \quad \forall a\in\mathbb R,
\]
so
\[
f(a)=-a.
\]

### 5. Verification
- \(f\equiv 0\) clearly works.
- For \(f(x)=C-x\),
\[
f(f(a))=a,\qquad f(a+f(b))=b-a.
\]
Thus
\[
(b-a)f(f(a))=(b-a)a=a(b-a)=a f(a+f(b)).
\]
So these functions work.

Therefore the complete set of solutions is

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(x)=C-x\ \forall x\in\mathbb R,\ C\in\mathbb R.}
\]

</details>
