# PB-Basic-001

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Determine all functions $f: \mathbb{Z} \rightarrow \mathbb{Z}$ such that, for all $x, y \in \mathbb{Z}$, we have \[ f(2x)+2f(y)=f(f(x+y)).\]

## Swarm: accepted (best candidate `P5`; self-verification grades [7, 7, 7]; 292,190 tokens in 47 calls)

**Blind grade: Correct (7/7).** Correctly obtains f(2x)=2f(x)-a from P(x,x) and f(f(t))=a+2f(t), reduces to Cauchy's equation on Z to get f affine, solves c^2=2c and a(c-2)=0 correctly, and verifies both f=0 and f(x)=2x+a.

\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=2x+a \text{ for some } a\in \mathbb Z}
\]

Proof:

Let \(a=f(0)\). The given equation is
\[
f(2x)+2f(y)=f(f(x+y)). \tag{P}
\]

Putting \(x=0\) in (P),
\[
f(0)+2f(y)=f(f(y)).
\]
Thus for every \(t\in\mathbb Z\),
\[
f(f(t))=a+2f(t). \tag{1}
\]

Using (1) with \(t=x+y\) in the original equation gives
\[
f(2x)+2f(y)=a+2f(x+y). \tag{2}
\]

Now put \(y=x\) in the original equation:
\[
f(2x)+2f(x)=f(f(2x)).
\]
By (1) with \(t=2x\),
\[
f(2x)+2f(x)=a+2f(2x).
\]
Hence
\[
f(2x)=2f(x)-a. \tag{3}
\]

Substitute (3) into (2):
\[
2f(x)-a+2f(y)=a+2f(x+y),
\]
so
\[
f(x+y)=f(x)+f(y)-a. \tag{4}
\]

Define \(g(x)=f(x)-a\). Then (4) becomes
\[
g(x+y)=g(x)+g(y).
\]
Since \(g:\mathbb Z\to\mathbb Z\), this additive Cauchy equation implies
\[
g(n)=cn
\]
for some \(c\in\mathbb Z\). Therefore
\[
f(n)=cn+a. \tag{5}
\]

Substitute \(f(n)=cn+a\) into the original equation. The left side is
\[
f(2x)+2f(y)=2cx+a+2cy+2a=2c(x+y)+3a.
\]
The right side is
\[
f(f(x+y))=f(c(x+y)+a)=c^2(x+y)+ca+a.
\]
Thus for all \(n=x+y\in\mathbb Z\),
\[
2cn+3a=c^2n+ca+a.
\]
Equivalently,
\[
(c^2-2c)n+a(c-2)=0.
\]
Since this holds for all \(n\in\mathbb Z\), we must have
\[
c^2-2c=0,\qquad a(c-2)=0.
\]
So \(c=0\) or \(c=2\).

- If \(c=0\), then \(a(c-2)=-2a=0\), so \(a=0\). This gives \(f\equiv 0\).
- If \(c=2\), then \(a(c-2)=0\) is automatic, so \(a\in\mathbb Z\) is arbitrary. This gives \(f(x)=2x+a\).

Finally, both families work:

- If \(f\equiv 0\), both sides are \(0\).
- If \(f(x)=2x+a\), then
\[
f(2x)+2f(y)=4x+a+4y+2a=4(x+y)+3a,
\]
and
\[
f(f(x+y))=f(2(x+y)+a)=2(2(x+y)+a)+a=4(x+y)+3a.
\]

Hence exactly
\[
\boxed{f\equiv 0 \quad\text{or}\quad f(x)=2x+a\ (a\in\mathbb Z)}.
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 8,202 | Correct (7/7) | Complete and rigorous: obtains f(2x)=2f(x)-c from P(0,y) and P(x,0), reduces to additivity so f is linear, correctly solves for a and c, and checks both families in the original equation. |
| A2 | stop | 5,203 | Correct (7/7) | Correctly derives f(f(t))=c+2f(t), f(2x)=2f(x)-c and the shifted Cauchy equation, gets f(n)=an+c by induction, solves a(a-2)=0 and c(a-2)=0 correctly, and verifies both solution families. |
| A3 | stop | 6,027 | Correct (7/7) | Derives f(2x)=2f(x)-a and f(f(x))=a+2f(x), reduces to Cauchy's equation to get f(n)=cn+a, uses the necessary condition to get c(c-2)=0 and a(c-2)=0, and properly verifies both candidates in the original equation. |
| A4 | stop | 10,258 | Correct (7/7) | Via P(x,0) obtains f(2x)+2f(y)=f(2x+2y)+2a and f(2y)=2f(y)-a, deduces f(x+y)=f(x)+f(y)-a so f is affine, correctly solves the coefficient conditions, and verifies both solution families. |
| A5 | stop | 5,993 | Correct (7/7) | Complete and rigorous: derives f(f(y))=c+2f(y) and f(2x)=2f(x)-c, shows f is affine via additivity of f-c, correctly solves the coefficient equations to get a=0,c=0 or a=2 with c arbitrary, and verifies both families. |
| A6 | stop | 7,289 | Correct (7/7) | Combines P(0,y) and P(x,0) to get f(2t)=2f(t)-b, deduces f(x+y)=f(x)+f(y)-b so f is linear, correctly solves the coefficient conditions, and verifies f identically 0 and f(n)=2n+b. |
| A7 | stop | 6,467 | Correct (7/7) | Derives f(f(y))=c+2f(y) and f(2y)=2f(y)-c, reduces to additivity of g=f-c so f(n)=an+c, correctly solves a(a-2)=0 and c(2-a)=0 from the original equation, and verifies both f=0 and f(n)=2n+c, giving a complete solution. |
| A8 | stop | 6,296 | Correct (7/7) | Derives f(2y)=2f(y)-f(0) from P(x+y,0) and x=0, reduces to Cauchy's equation for g=f-f(0) on Z so f is linear, correctly solves the coefficient conditions to get f identically 0 or f(x)=2x+a, and verifies both families. |
| A9 | stop | 7,523 | Correct (7/7) | Combines P(x,0) and P(0,x) to get f(2t)=2f(t)-c, reduces to additivity of f-c so f(n)=an+c, correctly solves a(a-2)=0 and c(a-2)=0, and verifies f=0 and f(n)=2n+c, giving a complete solution. |
| A10 | stop | 7,021 | Correct (7/7) | Correctly derives f(x+y)=f(x)+f(y)-c so f is affine, reduces the original equation to (2-a)(at+c)=0 for all t which yields exactly a=2 with any c or f=0, and verifies both families. |
| A11 | stop | 11,869 | Correct (7/7) | Correctly reduces to f(x+y)=f(x)+f(y)-c so f(n)=an+c, uses f(f(y))=c+2f(y) to force a(a-2)=0 and c(a-2)=0, and then verifies both candidate families in the original equation, so the solution is complete. |
| A12 | stop | 10,421 | Correct (7/7) | Compares P(0,y) and P(1,y-1) to show f has constant differences and is therefore linear (the reference approach), correctly solves the coefficient conditions, and verifies both solution families. |
| A13 | stop | 5,884 | Correct (7/7) | Complete and correct: obtains f(x+y)=f(x)+f(y)-c so f is affine, correctly solves a^2=2a and ac+c=3c, and verifies f=0 and f(n)=2n+c; one stray miscalculated line is explicitly retracted and redone correctly, so the logic is unaffected. |
| A14 | stop | 7,789 | Correct (7/7) | Derives f(2x)=2f(x)-c and f(x+y)=f(x)+f(y)-c, concludes f(n)=an+c, extracts the conditions via s=0 and s=1 to get f identically 0 or f(n)=2n+c, and verifies both. |
| A15 | stop | 10,149 | Correct (7/7) | Correctly reduces the equation to f(x+y)=f(x)+f(y)-c, hence f(n)=an+c, solves 2a=a^2 and c(2-a)=0 to get f identically 0 or f(n)=2n+c, and verifies both families. |
| A16 | stop | 7,741 | Correct (7/7) | Derives f(f(y))=2f(y)+c and f(2x)=2f(x)-c, reduces to additivity of f-c on Z so f(n)=an+c, correctly obtains a=2 with c arbitrary or a=c=0, and verifies both families in the original equation. |

<details><summary>A1: Correct (7/7)</summary>

Let \(P(x,y)\) denote the given equation:
\[
f(2x)+2f(y)=f(f(x+y)).
\]
Let \(c=f(0)\).

From \(P(0,y)\),
\[
f(0)+2f(y)=f(f(y)),
\]
so
\[
f(f(y))=c+2f(y). \tag{1}
\]

From \(P(x,0)\),
\[
f(2x)+2c=f(f(x)).
\]
Using (1) with \(y=x\), we get
\[
f(2x)+2c=c+2f(x),
\]
hence
\[
f(2x)=2f(x)-c. \tag{2}
\]

Now use the original equation. By (1),
\[
f(f(x+y))=c+2f(x+y).
\]
Thus
\[
f(2x)+2f(y)=c+2f(x+y).
\]
Using (2),
\[
2f(x)-c+2f(y)=c+2f(x+y),
\]
so
\[
f(x+y)=f(x)+f(y)-c. \tag{3}
\]

Define
\[
g(x)=f(x)-c.
\]
Then (3) gives
\[
g(x+y)=g(x)+g(y).
\]
Since \(g:\mathbb Z\to\mathbb Z\) is additive, \(g(n)=an\) for some \(a=g(1)\in\mathbb Z\). Hence
\[
f(n)=an+c \qquad \forall n\in\mathbb Z.
\]

Substitute \(f(n)=an+c\) into the original equation. For \(t=x+y\),
\[
f(2x)+2f(y)=2a(x+y)+3c,
\]
while
\[
f(f(x+y))=f(at+c)=a(at+c)+c=a^2t+ac+c.
\]
Thus
\[
2at+3c=a^2t+ac+c \qquad \forall t\in\mathbb Z.
\]
Comparing coefficients gives
\[
2a=a^2,\qquad 3c=ac+c.
\]
So
\[
a(a-2)=0,\qquad c(a-2)=0.
\]

If \(a=0\), then \(c=0\), giving
\[
f(x)\equiv 0.
\]

If \(a=2\), then \(c\) is arbitrary, giving
\[
f(x)=2x+c,\qquad c\in\mathbb Z.
\]

Both families are directly checked:

- If \(f\equiv 0\), both sides are \(0\).
- If \(f(x)=2x+c\), then
\[
f(2x)+2f(y)=4x+c+4y+2c=4(x+y)+3c,
\]
and
\[
f(f(x+y))=f(2(x+y)+c)=4(x+y)+3c.
\]

Therefore all solutions are
\[
\boxed{f(x)\equiv 0 \quad\text{or}\quad f(x)=2x+c\ \text{for some }c\in\mathbb Z.}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

Let \(c=f(0)\).

Putting \(x=0\) in the given equation gives
\[
f(0)+2f(y)=f(f(y)),
\]
so for every \(t\in\mathbb Z\),
\[
f(f(t))=c+2f(t). \tag{1}
\]
Using (1) in the original equation,
\[
f(2x)+2f(y)=c+2f(x+y). \tag{2}
\]

Now set \(y=0\) in (2):
\[
f(2x)+2c=c+2f(x),
\]
hence
\[
f(2x)=2f(x)-c. \tag{3}
\]
Substitute (3) into (2):
\[
2f(x)-c+2f(y)=c+2f(x+y),
\]
so
\[
f(x+y)=f(x)+f(y)-c. \tag{4}
\]

Define \(g(x)=f(x)-c\). Then (4) becomes
\[
g(x+y)=g(x)+g(y).
\]
Thus \(g\) is additive on \(\mathbb Z\). Let \(a=g(1)\). Then by induction,
\[
g(n)=an \quad \forall n\in\mathbb Z,
\]
so
\[
f(n)=an+c \quad \forall n\in\mathbb Z.
\]

Now use (1):
\[
f(f(n))=c+2f(n).
\]
Since \(f(n)=an+c\),
\[
a(an+c)+c=2an+3c.
\]
Thus
\[
a^2n+ac+c=2an+3c,
\]
or
\[
(a^2-2a)n+c(a-2)=0 \quad \forall n\in\mathbb Z.
\]
Therefore
\[
a(a-2)=0,\qquad c(a-2)=0.
\]

If \(a=0\), then \(c=0\), giving \(f\equiv 0\).

If \(a=2\), then \(c\) is arbitrary, giving
\[
f(x)=2x+c,\qquad c\in\mathbb Z.
\]

Finally, verify both families:

- If \(f\equiv 0\), then both sides are \(0\).
- If \(f(x)=2x+c\), then
\[
f(2x)+2f(y)=4x+c+4y+2c=4x+4y+3c,
\]
and
\[
f(f(x+y))=f(2x+2y+c)=4x+4y+3c.
\]

Hence the solutions are exactly

\[
\boxed{f(x)=0\ \forall x\in\mathbb Z}
\]
and
\[
\boxed{f(x)=2x+c\ \forall x\in\mathbb Z,\quad c\in\mathbb Z.}
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

\[
\boxed{f(x)=2x+c\ (c\in\mathbb Z)\quad\text{or}\quad f\equiv 0}
\]

Proof:

Let \(a=f(0)\). For all \(x,y\in\mathbb Z\), write the equation as
\[
P(x,y):\quad f(2x)+2f(y)=f(f(x+y)).
\]

Using \(P(x,0)\),
\[
f(2x)+2a=f(f(x)).
\]
Using \(P(0,x)\),
\[
a+2f(x)=f(f(x)).
\]
Hence
\[
f(2x)+2a=a+2f(x),
\]
so
\[
f(2x)=2f(x)-a. \tag{1}
\]
Also, from \(P(0,x)\),
\[
f(f(x))=a+2f(x). \tag{2}
\]

Now substitute (1) and (2) into the original equation:
\[
f(2x)+2f(y)=f(f(x+y)).
\]
Using (1) and (2),
\[
2f(x)-a+2f(y)=a+2f(x+y).
\]
Thus
\[
f(x+y)=f(x)+f(y)-a. \tag{3}
\]

Define
\[
g(x)=f(x)-a.
\]
Then (3) becomes
\[
g(x+y)=g(x)+g(y),
\]
so \(g:\mathbb Z\to\mathbb Z\) is additive. Therefore \(g(n)=cn\) for some \(c\in\mathbb Z\), where \(c=g(1)\). Hence
\[
f(n)=cn+a. \tag{4}
\]

Now use (2):
\[
f(f(x))=a+2f(x).
\]
By (4),
\[
f(f(x))=c(cx+a)+a=c^2x+ca+a,
\]
while
\[
a+2f(x)=a+2(cx+a)=2cx+3a.
\]
Thus
\[
c^2x+ca+a=2cx+3a
\]
for all \(x\in\mathbb Z\). Comparing coefficients gives
\[
c^2=2c,\qquad ca+a=3a.
\]
So
\[
c(c-2)=0,\qquad a(c-2)=0.
\]

If \(c=0\), then \(-2a=0\), so \(a=0\). This gives
\[
f(x)\equiv 0.
\]

If \(c=2\), then \(a\) is arbitrary, giving
\[
f(x)=2x+a,\qquad a\in\mathbb Z.
\]

Now verify both families.

1. \(f(x)\equiv 0\):  
   \[
   f(2x)+2f(y)=0,
   \]
   and
   \[
   f(f(x+y))=f(0)=0.
   \]
   So this works.

2. \(f(x)=2x+a\), \(a\in\mathbb Z\):  
   \[
   f(2x)+2f(y)=(4x+a)+2(2y+a)=4x+4y+3a.
   \]
   Also,
   \[
   f(f(x+y))=f(2(x+y)+a)=2(2x+2y+a)+a=4x+4y+3a.
   \]
   Thus the equation holds.

Therefore the complete set of solutions is
\[
\boxed{f(x)=2x+c\ (c\in\mathbb Z)\quad\text{or}\quad f\equiv 0.}
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(n)=2n+a \text{ for some } a\in\mathbb Z}
\]

Proof:

Let \(a=f(0)\). The given equation is
\[
f(2x)+2f(y)=f(f(x+y)). \tag{P}
\]

Putting \(y=0\) in (P), we get
\[
f(2x)+2a=f(f(x)). \tag{1}
\]
Hence, replacing \(x\) by \(x+y\),
\[
f(f(x+y))=f(2(x+y))+2a.
\]
Therefore (P) becomes
\[
f(2x)+2f(y)=f(2x+2y)+2a. \tag{2}
\]

Now set \(x=0\) in (2):
\[
a+2f(y)=f(2y)+2a,
\]
so
\[
f(2y)=2f(y)-a. \tag{3}
\]

Using (3) in (2), we get
\[
2f(x)-a+2f(y)=2f(x+y)+a,
\]
hence
\[
f(x+y)=f(x)+f(y)-a. \tag{4}
\]

Define
\[
g(x)=f(x)-a.
\]
Then (4) becomes
\[
g(x+y)=g(x)+g(y).
\]
So \(g:\mathbb Z\to\mathbb Z\) is additive. Thus for some \(c\in\mathbb Z\),
\[
g(n)=cn,
\]
and therefore
\[
f(n)=cn+a. \tag{5}
\]

Substitute \(f(n)=cn+a\) into the original equation. The left side is
\[
f(2x)+2f(y)=2cx+a+2cy+2a=2c(x+y)+3a.
\]
The right side is
\[
f(f(x+y))=c(c(x+y)+a)+a=c^2(x+y)+ca+a.
\]
Thus for all \(s=x+y\in\mathbb Z\),
\[
2cs+3a=c^2s+ca+a.
\]
So
\[
(2c-c^2)s+(2a-ca)=0
\]
for all \(s\in\mathbb Z\). Hence
\[
2c-c^2=0,\qquad 2a-ca=0.
\]
Thus \(c=0\) or \(c=2\).

- If \(c=0\), then \(2a=0\), so \(a=0\), giving \(f\equiv 0\).
- If \(c=2\), then \(2a-2a=0\) holds for every \(a\in\mathbb Z\), giving \(f(n)=2n+a\).

Finally, both families work:

- For \(f\equiv 0\), both sides are \(0\).
- For \(f(n)=2n+a\),
\[
f(2x)+2f(y)=4x+a+4y+2a=4(x+y)+3a,
\]
while
\[
f(f(x+y))=f(2(x+y)+a)=4(x+y)+3a.
\]

Therefore
\[
\boxed{f\equiv 0 \quad \text{or} \quad f(n)=2n+a,\ a\in\mathbb Z.}
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

Let \(c=f(0)\). The equation is
\[
f(2x)+2f(y)=f(f(x+y)) \qquad \forall x,y\in\mathbb Z.
\]

### Step 1: Derive basic identities
Putting \(x=0\),
\[
f(0)+2f(y)=f(f(y)),
\]
so
\[
f(f(y))=c+2f(y). \tag{1}
\]

Putting \(y=0\),
\[
f(2x)+2c=f(f(x)).
\]
Using (1) with \(y=x\), we get \(f(f(x))=c+2f(x)\), hence
\[
f(2x)+2c=c+2f(x),
\]
so
\[
f(2x)=2f(x)-c. \tag{2}
\]

### Step 2: Show \(f\) is affine linear
Using (2), the original equation becomes
\[
2f(x)-c+2f(y)=c+2f(x+y),
\]
because by (1),
\[
f(f(x+y))=c+2f(x+y).
\]
Thus
\[
2f(x)+2f(y)-c=c+2f(x+y),
\]
so
\[
f(x+y)=f(x)+f(y)-c. \tag{3}
\]
Define
\[
g(x)=f(x)-c.
\]
Then
\[
g(x+y)=g(x)+g(y),
\]
so \(g:\mathbb Z\to\mathbb Z\) is additive. Therefore \(g(x)=ax\) for some \(a\in\mathbb Z\), where \(a=g(1)\). Hence
\[
f(x)=ax+c. \tag{4}
\]

### Step 3: Substitute into the original equation
Substitute \(f(x)=ax+c\) into the original equation. For \(x+y=t\),
\[
f(2x)+2f(y)=2at+3c,
\]
while
\[
f(f(x+y))=f(at+c)=a(at+c)+c=a^2t+ac+c.
\]
Thus for all \(t\in\mathbb Z\),
\[
2at+3c=a^2t+ac+c.
\]
So
\[
(a^2-2a)t+ac-2c=0.
\]
Since this holds for all \(t\), we must have
\[
a^2-2a=0,\qquad ac-2c=0.
\]
Hence
\[
a=0 \quad \text{or} \quad a=2.
\]

- If \(a=0\), then \(-2c=0\), so \(c=0\). This gives
\[
f(x)=0.
\]
- If \(a=2\), then \(2c-2c=0\), so \(c\) is arbitrary. This gives
\[
f(x)=2x+c.
\]

### Step 4: Verify the candidates
1. If \(f(x)=0\), then both sides are \(0\).

2. If \(f(x)=2x+c\), then
\[
f(2x)+2f(y)=(4x+c)+2(2y+c)=4x+4y+3c,
\]
and
\[
f(f(x+y))=f(2(x+y)+c)=2(2x+2y+c)+c=4x+4y+3c.
\]
So the equation holds for every \(c\in\mathbb Z\).

Therefore the solutions are
\[
\boxed{f(x)=0 \quad \forall x\in\mathbb Z}
\]
and
\[
\boxed{f(x)=2x+c \quad \forall x\in\mathbb Z,\ c\in\mathbb Z.}
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

Let  
\[
P(x,y):\quad f(2x)+2f(y)=f(f(x+y)).
\]
Set \(b=f(0)\).

From \(P(0,y)\),
\[
b+2f(y)=f(f(y)) \qquad \forall y\in\mathbb Z.
\]
From \(P(x,0)\),
\[
f(2x)+2b=f(f(x)) \qquad \forall x\in\mathbb Z.
\]
Taking \(x=y=t\) in both gives
\[
f(2t)+2b=b+2f(t),
\]
so
\[
f(2t)=2f(t)-b. \tag{1}
\]

Now in the original equation, using \(f(f(x+y))=b+2f(x+y)\), we get
\[
f(2x)+2f(y)=b+2f(x+y).
\]
By (1),
\[
2f(x)-b+2f(y)=b+2f(x+y),
\]
hence
\[
f(x+y)=f(x)+f(y)-b. \tag{2}
\]

Define \(g(x)=f(x)-b\). Then (2) becomes
\[
g(x+y)=g(x)+g(y).
\]
Thus \(g\) is additive on \(\mathbb Z\), so there exists \(a\in\mathbb Z\) such that
\[
g(n)=an.
\]
Therefore
\[
f(n)=an+b. \tag{3}
\]

Substitute \(f(n)=an+b\) into the original equation. Let \(n=x+y\). Then
\[
f(2x)+2f(y)=2ax+b+2(ay+b)=2an+3b,
\]
while
\[
f(f(n))=f(an+b)=a(an+b)+b=a^2n+ab+b.
\]
Thus for all \(n\in\mathbb Z\),
\[
2an+3b=a^2n+ab+b.
\]
So
\[
(2a-a^2)n+(2b-ab)=0 \qquad \forall n\in\mathbb Z.
\]
Hence
\[
2a-a^2=0,\qquad 2b-ab=0.
\]
The first equation gives \(a=0\) or \(a=2\).

- If \(a=0\), then \(2b=0\), so \(b=0\). This gives \(f\equiv 0\).
- If \(a=2\), then \(2b-ab=b(2-a)=0\) is automatic, so \(b\in\mathbb Z\) is arbitrary. This gives \(f(n)=2n+b\).

Now check both families:

1. \(f\equiv 0\):
\[
f(2x)+2f(y)=0,\qquad f(f(x+y))=f(0)=0.
\]

2. \(f(n)=2n+b\):
\[
f(2x)+2f(y)=(4x+b)+2(2y+b)=4(x+y)+3b,
\]
and
\[
f(f(x+y))=f(2(x+y)+b)=2(2(x+y)+b)+b=4(x+y)+3b.
\]

Therefore the solutions are exactly
\[
\boxed{f\equiv 0 \quad\text{or}\quad f(n)=2n+c \text{ for some } c\in\mathbb Z.}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad\text{or}\quad f(n)=2n+c\ \text{for some }c\in\mathbb Z}
\]

Proof:

Let \(c=f(0)\). For all \(x,y\in\mathbb Z\), write the given equation as
\[
P(x,y):\quad f(2x)+2f(y)=f(f(x+y)).
\]

From \(P(0,y)\),
\[
f(f(y))=c+2f(y). \tag{1}
\]
From \(P(y,0)\),
\[
f(f(y))=f(2y)+2c. \tag{2}
\]
Comparing (1) and (2),
\[
f(2y)=2f(y)-c. \tag{3}
\]

Now in the original equation, replace \(x+y\) by \(t\). Using (1),
\[
f(f(x+y))=c+2f(x+y).
\]
Thus
\[
f(2x)+2f(y)=c+2f(x+y).
\]
Using (3) for \(f(2x)\),
\[
2f(x)-c+2f(y)=c+2f(x+y),
\]
so
\[
f(x+y)=f(x)+f(y)-c. \tag{4}
\]

Define
\[
g(n)=f(n)-c.
\]
Then (4) becomes
\[
g(x+y)=g(x)+g(y).
\]
So \(g:\mathbb Z\to\mathbb Z\) is additive. Hence \(g(n)=ng(1)\) for all \(n\in\mathbb Z\). Let \(a=g(1)\in\mathbb Z\). Then
\[
f(n)=an+c.
\]

Substitute \(f(n)=an+c\) into the original equation. First,
\[
f(2x)+2f(y)=(2ax+c)+2(ay+c)=2a(x+y)+3c.
\]
Also,
\[
f(f(x+y))=f(a(x+y)+c)=a(a(x+y)+c)+c=a^2(x+y)+ac+c.
\]
Therefore, for all \(s=x+y\),
\[
2as+3c=a^2s+ac+c.
\]
So
\[
(2a-a^2)s+(3c-ac-c)=0
\]
for all \(s\in\mathbb Z\). Hence
\[
2a-a^2=0,\qquad 3c-ac-c=0.
\]
The first equation gives
\[
a(a-2)=0,
\]
so \(a=0\) or \(a=2\).

If \(a=0\), then
\[
3c-c=2c=0,
\]
so \(c=0\). Thus \(f(n)=0\).

If \(a=2\), then the constant condition gives no restriction on \(c\), so
\[
f(n)=2n+c
\]
for arbitrary \(c\in\mathbb Z\).

Finally, verify both families:

- If \(f(n)=0\), then both sides are \(0\).
- If \(f(n)=2n+c\), then
\[
f(2x)+2f(y)=4x+c+4y+2c=4(x+y)+3c,
\]
and
\[
f(f(x+y))=f(2x+2y+c)=2(2x+2y+c)+c=4(x+y)+3c.
\]

Thus the complete set of solutions is

\[
\boxed{f\equiv 0 \quad\text{or}\quad f(n)=2n+c\ (c\in\mathbb Z).}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

Let  
\[
P(x,y):\quad f(2x)+2f(y)=f(f(x+y)).
\]
Set \(a=f(0)\). Using \(P(x+y,0)\),
\[
f(2x+2y)+2a=f(f(x+y)).
\]
Comparing with \(P(x,y)\),
\[
f(2x)+2f(y)=f(2x+2y)+2a. \tag{1}
\]
Putting \(x=0\) in (1),
\[
a+2f(y)=f(2y)+2a,
\]
so
\[
f(2y)=2f(y)-a. \tag{2}
\]
Using (2) in (1),
\[
2f(x)+2f(y)-a=2f(x+y)+a,
\]
hence
\[
f(x+y)=f(x)+f(y)-a. \tag{3}
\]
Define \(g(x)=f(x)-a\). Then (3) gives
\[
g(x+y)=g(x)+g(y),
\]
so \(g:\mathbb Z\to\mathbb Z\) is additive. Therefore \(g(x)=cx\) for some \(c\in\mathbb Z\), and thus
\[
f(x)=cx+a.
\]

Substitute \(f(x)=cx+a\) into the original equation. For \(s=x+y\),
\[
f(2x)+2f(y)=2cs+3a,
\]
while
\[
f(f(x+y))=c(cs+a)+a=c^2s+ca+a.
\]
Thus
\[
c^2s+ca+a=2cs+3a
\]
for all \(s\in\mathbb Z\). Hence
\[
(c^2-2c)s+a(c-2)=0
\]
for all \(s\in\mathbb Z\), so
\[
c^2-2c=0,\qquad a(c-2)=0.
\]
Thus \(c=0\) or \(c=2\).

- If \(c=2\), then \(a(c-2)=0\) gives no restriction on \(a\), so \(f(x)=2x+a\) for any \(a\in\mathbb Z\).
- If \(c=0\), then \(a(0-2)=0\), so \(a=0\), giving \(f(x)=0\).

Both families work:
\[
f(x)=2x+a:\quad f(2x)+2f(y)=4x+4y+3a=f(f(x+y)).
\]
and
\[
f\equiv 0
\]
clearly works.

\[
\boxed{f(x)=2x+a\ (a\in\mathbb Z)\quad\text{or}\quad f(x)\equiv 0}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

Let \(P(x,y)\) denote the assertion
\[
f(2x)+2f(y)=f(f(x+y)).
\]
Set \(c=f(0)\).

From \(P(x,0)\):
\[
f(2x)+2c=f(f(x)).
\]
From \(P(0,x)\):
\[
c+2f(x)=f(f(x)).
\]
Hence for every \(t\in\mathbb Z\),
\[
f(f(t))=c+2f(t).
\]
In particular,
\[
f(2t)=2f(t)-c.
\]

Also, using \(P(0,x+y)\),
\[
f(f(x+y))=c+2f(x+y).
\]
So the original equation becomes
\[
f(2x)+2f(y)=c+2f(x+y).
\]
Substituting \(f(2x)=2f(x)-c\), we get
\[
2f(x)-c+2f(y)=c+2f(x+y),
\]
so
\[
f(x+y)=f(x)+f(y)-c.
\]

Define
\[
g(x)=f(x)-c.
\]
Then
\[
g(x+y)=g(x)+g(y),
\]
so \(g:\mathbb Z\to\mathbb Z\) is additive. Therefore \(g(n)=an\) for some \(a\in\mathbb Z\), where \(a=g(1)\). Hence
\[
f(n)=an+c
\]
for all \(n\in\mathbb Z\).

Now substitute \(f(n)=an+c\) into the original equation. We have
\[
f(2x)+2f(y)=2ax+c+2ay+2c=2a(x+y)+3c,
\]
while
\[
f(f(x+y))=f(a(x+y)+c)=a^2(x+y)+ac+c.
\]
Thus for all \(n=x+y\in\mathbb Z\),
\[
2an+3c=a^2n+ac+c.
\]
Comparing coefficients gives
\[
2a=a^2,\qquad 3c=ac+c.
\]
So
\[
a(a-2)=0,\qquad c(a-2)=0.
\]

If \(a=0\), then \(c=0\), giving \(f\equiv 0\).

If \(a=2\), then \(c\) is arbitrary, giving
\[
f(n)=2n+c,\qquad c\in\mathbb Z.
\]

Finally, both families work:
- If \(f\equiv 0\), both sides are \(0\).
- If \(f(n)=2n+c\), then
\[
f(2x)+2f(y)=4x+c+4y+2c=4(x+y)+3c,
\]
and
\[
f(f(x+y))=f(2(x+y)+c)=2(2(x+y)+c)+c=4(x+y)+3c.
\]

Therefore,
\[
\boxed{f(x)\equiv 0 \quad\text{or}\quad f(x)=2x+c\ \text{for some }c\in\mathbb Z.}
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

Let \(c=f(0)\). For all \(n\in\mathbb Z\), using the equation with \(x=0,y=n\),

\[
f(0)+2f(n)=f(f(n)),
\]

so

\[
f(f(n))=c+2f(n). \tag{1}
\]

Hence the original equation becomes

\[
f(2x)+2f(y)=c+2f(x+y). \tag{2}
\]

Putting \(y=0\) in (2),

\[
f(2x)+2c=c+2f(x),
\]

so

\[
f(2x)=2f(x)-c. \tag{3}
\]

Substitute (3) into (2):

\[
2f(x)-c+2f(y)=c+2f(x+y).
\]

Thus

\[
f(x+y)=f(x)+f(y)-c. \tag{4}
\]

Define \(g(x)=f(x)-c\). Then (4) gives

\[
g(x+y)=g(x)+g(y).
\]

So \(g:\mathbb Z\to\mathbb Z\) is additive. Therefore there exists \(a\in\mathbb Z\) such that

\[
g(n)=an,
\]

and hence

\[
f(n)=an+c. \tag{5}
\]

Now substitute \(f(n)=an+c\) into the original equation. Let \(t=x+y\). Then

\[
f(2x)+2f(y)=2at+3c,
\]

while

\[
f(f(x+y))=f(at+c)=a(at+c)+c=a^2t+ac+c.
\]

Therefore

\[
2at+3c=a^2t+ac+c,
\]

so

\[
(2-a)(at+c)=0 \qquad \forall t\in\mathbb Z. \tag{6}
\]

If \(a=2\), then every \(c\in\mathbb Z\) works, giving

\[
f(n)=2n+c.
\]

If \(a\neq 2\), then \(at+c=0\) for all \(t\in\mathbb Z\). Taking \(t=0\) gives \(c=0\), and taking \(t=1\) gives \(a=0\). Hence \(f(n)=0\).

Finally, both families work:

- If \(f(n)=0\), both sides are \(0\).
- If \(f(n)=2n+c\), then
  \[
  f(2x)+2f(y)=4(x+y)+3c
  \]
  and
  \[
  f(f(x+y))=4(x+y)+3c.
  \]

Therefore the solutions are

\[
\boxed{f(n)=0\ \forall n\in\mathbb Z}
\]

or

\[
\boxed{f(n)=2n+c\ \forall n\in\mathbb Z,\quad c\in\mathbb Z.}
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

Let \(c=f(0)\). The given equation is
\[
f(2x)+2f(y)=f(f(x+y)). \tag{1}
\]

Set \(x=0\) in (1):
\[
f(f(y))=c+2f(y) \qquad \forall y\in\mathbb Z. \tag{2}
\]
Using (2) in (1), with \(y\) replaced by \(x+y\), gives
\[
f(2x)+2f(y)=c+2f(x+y). \tag{3}
\]
Now put \(y=0\) in (3):
\[
f(2x)+2c=c+2f(x),
\]
so
\[
f(2x)=2f(x)-c. \tag{4}
\]
Substitute (4) into (3):
\[
2f(x)-c+2f(y)=c+2f(x+y),
\]
hence
\[
f(x+y)=f(x)+f(y)-c. \tag{5}
\]
Define \(g(x)=f(x)-c\). Then (5) becomes
\[
g(x+y)=g(x)+g(y),
\]
so \(g\) is additive on \(\mathbb Z\). Therefore \(g(n)=an\) for some \(a\in\mathbb Z\), where \(a=g(1)\). Thus
\[
f(n)=an+c. \tag{6}
\]

Now use (2):
\[
f(f(y))=c+2f(y).
\]
Substituting \(f(y)=ay+c\), we get
\[
a(ay+c)+c=c+2(ay+c),
\]
so
\[
a^2y+ac+c=2ay+3c.
\]
Thus
\[
(a^2-2a)y+c(a-2)=0 \qquad \forall y\in\mathbb Z.
\]
Hence
\[
a(a-2)=0,\qquad c(a-2)=0.
\]
So either:
- \(a=2\), with \(c\in\mathbb Z\) arbitrary; or
- \(a=0\), which forces \(c=0\), giving \(f\equiv 0\).

It remains to verify these work.

For \(f(n)=2n+c\):
\[
f(2x)+2f(y)=4x+c+4y+2c=4(x+y)+3c,
\]
and
\[
f(f(x+y))=f(2(x+y)+c)=2(2(x+y)+c)+c=4(x+y)+3c.
\]
So it works.

For \(f\equiv 0\), both sides are \(0\).

Therefore all solutions are
\[
\boxed{f(n)=2n+c\ (c\in\mathbb Z)\quad\text{or}\quad f\equiv 0.}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

Let \(P(x,y)\) denote the given assertion:
\[
f(2x)+2f(y)=f(f(x+y)).
\]

Using \(P(0,y)\) and \(P(1,y-1)\), the right-hand sides are equal because both have \(x+y=y\). Hence
\[
f(0)+2f(y)=f(2)+2f(y-1).
\]
So for every \(y\in\mathbb Z\),
\[
2(f(y)-f(y-1))=f(2)-f(0).
\]
Therefore \(f(y)-f(y-1)\) is constant. Let
\[
a=f(1)-f(0)\in\mathbb Z.
\]
Then
\[
f(y)=f(y-1)+a \qquad \forall y\in\mathbb Z.
\]
By induction,
\[
f(n)=an+b \qquad \forall n\in\mathbb Z,
\]
where \(b=f(0)\).

Now substitute \(f(n)=an+b\) into the original equation. For \(t=x+y\),
\[
f(2x)+2f(y)=a(2x)+b+2(ay+b)=2a(x+y)+3b=2at+3b,
\]
while
\[
f(f(x+y))=f(at+b)=a(at+b)+b=a^2t+ab+b.
\]
Thus for all \(t\in\mathbb Z\),
\[
2at+3b=a^2t+ab+b.
\]
Comparing coefficients gives
\[
2a=a^2,\qquad 3b=ab+b.
\]
So
\[
a(a-2)=0,\qquad b(a-2)=0.
\]
Hence either \(a=0\), which forces \(b=0\), giving \(f\equiv 0\), or \(a=2\), with \(b\) arbitrary.

Finally, check:
- If \(f\equiv 0\), both sides are \(0\).
- If \(f(n)=2n+c\), then
\[
f(2x)+2f(y)=4x+c+4y+2c=4(x+y)+3c,
\]
and
\[
f(f(x+y))=f(2(x+y)+c)=2(2(x+y)+c)+c=4(x+y)+3c.
\]

Therefore the solutions are
\[
\boxed{f\equiv 0 \quad\text{or}\quad f(n)=2n+c\ \text{for any }c\in\mathbb Z.}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

Let  
\[
P(x,y):\quad f(2x)+2f(y)=f(f(x+y)).
\]

Set \(c=f(0)\).

### 1. Derive a basic identity
From \(P(0,y)\),
\[
f(0)+2f(y)=f(f(y)),
\]
so
\[
f(f(y))=c+2f(y). \tag{1}
\]
Using \(P(x,0)\),
\[
f(2x)+2f(0)=f(f(x)).
\]
By (1), \(f(f(x))=c+2f(x)\), hence
\[
f(2x)+2c=c+2f(x),
\]
so
\[
f(2x)=2f(x)-c. \tag{2}
\]

Now apply (1) to \(y=x+y\):
\[
f(f(x+y))=c+2f(x+y).
\]
Thus the original equation becomes
\[
f(2x)+2f(y)=c+2f(x+y).
\]
Using (2),
\[
2f(x)-c+2f(y)=c+2f(x+y).
\]
Therefore
\[
f(x+y)=f(x)+f(y)-c. \tag{3}
\]

### 2. Reduce to an affine function
Define
\[
g(x)=f(x)-c.
\]
Then (3) gives
\[
g(x+y)=g(x)+g(y),
\]
so \(g:\mathbb Z\to\mathbb Z\) is additive. Hence for some integer \(a\),
\[
g(n)=an,
\]
and therefore
\[
f(n)=an+c. \tag{4}
\]

### 3. Substitute into the original equation
Let \(t=x+y\). From (4),
\[
f(2x)+2f(y)=2at+c+2ay+2c=2at+2at? 
\]
Wait carefully:
\[
f(2x)=2ax+c,\qquad 2f(y)=2ay+2c,
\]
so
\[
f(2x)+2f(y)=2a(x+y)+3c=2at+3c.
\]
Also,
\[
f(f(x+y))=f(at+c)=a(at+c)+c=a^2t+ac+c.
\]
Thus for all \(t\in\mathbb Z\),
\[
2at+3c=a^2t+ac+c.
\]
Comparing coefficients of \(t\) and constants:
\[
a^2=2a,\qquad ac+c=3c.
\]
So
\[
a(a-2)=0.
\]
If \(a=0\), then \(ac+c=3c\) gives \(c=0\).  
If \(a=2\), then \(ac+c=3c\) holds for every \(c\in\mathbb Z\).

Hence the only possibilities are
\[
f(n)=0
\]
or
\[
f(n)=2n+c,\qquad c\in\mathbb Z.
\]

### 4. Verify the candidates
- If \(f\equiv 0\), then both sides are \(0\).
- If \(f(n)=2n+c\), then
\[
f(2x)+2f(y)=4x+c+4y+2c=4(x+y)+3c,
\]
and
\[
f(f(x+y))=f(2(x+y)+c)=2(2(x+y)+c)+c=4(x+y)+3c.
\]
So the equation holds.

Therefore the solutions are
\[
\boxed{f(n)=0\ \text{for all }n\in\mathbb Z}
\]
and
\[
\boxed{f(n)=2n+c\ \text{for all }n\in\mathbb Z,\ c\in\mathbb Z.}
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(n)=2n+c\ \text{for some }c\in\mathbb Z}
\]

Proof:

Let \(c=f(0)\). For all \(x,y\in\mathbb Z\),

\[
f(2x)+2f(y)=f(f(x+y)). \tag{1}
\]

Putting \(x=0\) in (1),

\[
f(0)+2f(y)=f(f(y)),
\]

so

\[
f(f(y))=2f(y)+c. \tag{2}
\]

Putting \(y=0\) in (1),

\[
f(2x)+2f(0)=f(f(x)).
\]

Using (2) with \(y=x\), we get

\[
f(2x)+2c=2f(x)+c,
\]

hence

\[
f(2x)=2f(x)-c. \tag{3}
\]

Now the right-hand side of (1) can also be written using (2):

\[
f(f(x+y))=2f(x+y)+c.
\]

Thus (1) becomes

\[
f(2x)+2f(y)=2f(x+y)+c.
\]

Using (3),

\[
2f(x)-c+2f(y)=2f(x+y)+c,
\]

so

\[
f(x+y)=f(x)+f(y)-c. \tag{4}
\]

Define

\[
g(n)=f(n)-c.
\]

Then \(g(0)=0\), and from (4),

\[
g(x+y)=g(x)+g(y).
\]

So \(g:\mathbb Z\to\mathbb Z\) is additive. Therefore \(g(n)=an\) for some \(a\in\mathbb Z\), where \(a=g(1)\). Hence

\[
f(n)=an+c.
\]

Substitute \(f(n)=an+c\) into the original equation. For \(s=x+y\),

\[
f(2x)+2f(y)=2as+3c,
\]

while

\[
f(f(s))=f(as+c)=a(as+c)+c=a^2s+ac+c.
\]

Thus for all \(s\in\mathbb Z\),

\[
2as+3c=a^2s+ac+c.
\]

Equivalently,

\[
(2a-a^2)s+(2c-ac)=0.
\]

Taking \(s=0\) gives \(2c-ac=0\), and taking \(s=1\) gives \(2a-a^2=0\). Hence

\[
a(a-2)=0,
\]

so \(a=0\) or \(a=2\).

- If \(a=0\), then \(2c-ac=2c=0\), so \(c=0\). Thus \(f\equiv 0\).
- If \(a=2\), then \(2c-ac=0\) automatically, so \(c\in\mathbb Z\) is arbitrary. Thus \(f(n)=2n+c\).

Finally, both families work:

- \(f\equiv 0\) is immediate.
- If \(f(n)=2n+c\), then with \(s=x+y\),
  \[
  f(2x)+2f(y)=4x+c+4y+2c=4s+3c,
  \]
  and
  \[
  f(f(s))=f(2s+c)=2(2s+c)+c=4s+3c.
  \]

Therefore the complete set of solutions is

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(n)=2n+c\ (c\in\mathbb Z).}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(n)=2n+c \text{ for some } c\in \mathbb Z}
\]

Proof:

Let \(c=f(0)\). Putting \(x=0\) in
\[
f(2x)+2f(y)=f(f(x+y))
\]
gives
\[
f(f(y))=c+2f(y). \tag{1}
\]
Thus the original equation becomes
\[
f(2x)+2f(y)=c+2f(x+y). \tag{2}
\]

Now set \(y=0\) in (2):
\[
f(2x)+2c=c+2f(x),
\]
so
\[
f(2x)=2f(x)-c.
\]
Substitute this back into (2):
\[
2f(x)-c+2f(y)=c+2f(x+y),
\]
hence
\[
f(x+y)=f(x)+f(y)-c. \tag{3}
\]

Define
\[
g(x)=f(x)-c.
\]
Then (3) gives
\[
g(x+y)=g(x)+g(y).
\]
So \(g:\mathbb Z\to\mathbb Z\) is additive. Therefore there exists \(a\in\mathbb Z\) such that
\[
g(n)=an,
\]
and hence
\[
f(n)=an+c. \tag{4}
\]

Substitute (4) into the original equation. For \(s=x+y\),
\[
f(2x)+2f(y)=2as+3c,
\]
while
\[
f(f(x+y))=f(as+c)=a(as+c)+c=a^2s+ac+c.
\]
Thus for all \(s\in\mathbb Z\),
\[
2as+3c=a^2s+ac+c.
\]
Comparing coefficients gives
\[
2a=a^2,\qquad c(2-a)=0.
\]
So \(a=0\) or \(a=2\).

- If \(a=0\), then \(c(2)=0\), so \(c=0\). This gives \(f\equiv 0\).
- If \(a=2\), then \(c\) is arbitrary, giving \(f(n)=2n+c\).

Finally, both families work:

- If \(f\equiv 0\), both sides are \(0\).
- If \(f(n)=2n+c\), then
\[
f(2x)+2f(y)=4x+c+4y+2c=4x+4y+3c,
\]
and
\[
f(f(x+y))=f(2x+2y+c)=2(2x+2y+c)+c=4x+4y+3c.
\]

Therefore,
\[
\boxed{f\equiv 0 \quad \text{or} \quad f(n)=2n+c\ (c\in\mathbb Z).}
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(n)=2n+c \text{ for some } c\in\mathbb Z}
\]

Proof:

Let
\[
c=f(0).
\]
The given equation is
\[
f(2x)+2f(y)=f(f(x+y)). \tag{P}
\]

Putting \(x=0\) in (P), we get
\[
f(0)+2f(y)=f(f(y)),
\]
so
\[
f(f(y))=2f(y)+c. \tag{1}
\]

Using (1) in (P), the right-hand side becomes
\[
f(f(x+y))=2f(x+y)+c.
\]
Thus
\[
f(2x)+2f(y)=2f(x+y)+c. \tag{2}
\]

Now set \(y=0\) in (2):
\[
f(2x)+2c=2f(x)+c,
\]
hence
\[
f(2x)=2f(x)-c. \tag{3}
\]

Substitute (3) into (2):
\[
2f(x)-c+2f(y)=2f(x+y)+c,
\]
so
\[
f(x+y)=f(x)+f(y)-c. \tag{4}
\]

Define
\[
g(x)=f(x)-c.
\]
Then (4) gives
\[
g(x+y)=g(x)+g(y),
\]
so \(g:\mathbb Z\to\mathbb Z\) is additive. Therefore
\[
g(n)=ng(1)
\]
for all \(n\in\mathbb Z\). Writing \(a=g(1)\), we get
\[
f(n)=an+c.
\]

Now use (1):
\[
f(f(n))=2f(n)+c.
\]
Substituting \(f(n)=an+c\),
\[
a(an+c)+c=2(an+c)+c.
\]
Thus
\[
a^2n+ac+c=2an+3c.
\]
Comparing coefficients gives
\[
a^2=2a,\qquad ac=2c.
\]
Hence \(a=0\) or \(a=2\). If \(a=0\), then \(ac=2c\) gives \(c=0\), so
\[
f\equiv 0.
\]
If \(a=2\), then \(c\) is arbitrary, giving
\[
f(n)=2n+c.
\]

Finally, verify both families.

1. If \(f\equiv 0\), then both sides are \(0\).

2. If \(f(n)=2n+c\), then
\[
f(2x)+2f(y)=4x+c+4y+2c=4(x+y)+3c,
\]
and
\[
f(f(x+y))=f(2(x+y)+c)=2(2(x+y)+c)+c=4(x+y)+3c.
\]
So the equation holds.

Therefore the complete set of solutions is

\[
\boxed{f\equiv 0 \quad \text{or} \quad f(n)=2n+c,\ c\in\mathbb Z.}
\]

</details>
