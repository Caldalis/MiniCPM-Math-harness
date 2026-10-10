# PB-Basic-008

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Let $a,b,c$ be positive reals such that $a+b+c = 1$, prove that $\sqrt{a}+\sqrt{b}+\sqrt{c} \geq 3\sqrt{3}(ab+bc+ca)$.

## Swarm: accepted (best candidate `P2`; self-verification grades [7, 7, 7]; 777,084 tokens in 65 calls)

**Blind grade: Correct (7/7).** Correct and complete: proves the homogenized bound 6*sum x^2y^2<=1+Q exactly, as fourth-degree Schur plus 2*sum xy(x-y)^2, then finishes with s^2+1<=4s/sqrt3 for 1<=s<=sqrt3; every identity checks.

Let  
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c .
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
The desired inequality becomes
\[
x+y+z\ge 3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2).
\]
Write
\[
s=x+y+z,\qquad Q=xy+yz+zx,\qquad P=x^2y^2+y^2z^2+z^2x^2.
\]
Since \(s^2=x^2+y^2+z^2+2Q=1+2Q\), we have
\[
s^2+1=2(1+Q).
\]
So it is enough to prove
\[
12P\le s^2+1. \tag{1}
\]

First prove \(6P\le 1+Q\). Let
\[
A=x^4+y^4+z^4,
\]
\[
B=xy(x^2+y^2)+yz(y^2+z^2)+zx(z^2+x^2),
\]
\[
C=xyz(x+y+z).
\]
Using \(x^2+y^2+z^2=1\),
\[
1+Q=(x^2+y^2+z^2)^2+(x^2+y^2+z^2)(xy+yz+zx).
\]
Expanding gives
\[
1+Q=A+B+C+2P.
\]
Hence
\[
1+Q-6P=A+B+C-4P.
\]
Now
\[
A+B+C-4P=(A+C-B)+2B-4P.
\]
By Schur’s inequality,
\[
A+C-B=\sum_{\text{cyc}}x^2(x-y)(x-z)\ge 0.
\]
Also,
\[
2B-4P=2\sum_{\text{cyc}}xy(x-y)^2\ge 0.
\]
Therefore
\[
1+Q-6P\ge 0,
\]
so
\[
6P\le 1+Q.
\]
Multiplying by \(2\),
\[
12P\le 2+2Q=s^2+1. \tag{2}
\]

It remains to use
\[
s\le \sqrt3
\]
by Cauchy, and \(s\ge 1\). Thus
\[
s^2+1-\frac{4s}{\sqrt3}
=(s-\sqrt3)\left(s-\frac1{\sqrt3}\right)\le 0,
\]
so
\[
s^2+1\le \frac{4s}{\sqrt3}. \tag{3}
\]
Combining (2) and (3),
\[
12P\le s^2+1\le \frac{4s}{\sqrt3}.
\]
Dividing by \(12\),
\[
P\le \frac{s}{3\sqrt3}.
\]
Thus
\[
s\ge 3\sqrt3\,P.
\]
Recalling \(s=\sqrt a+\sqrt b+\sqrt c\) and \(P=ab+bc+ca\), we get
\[
\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca).
\]

Equality occurs at \(a=b=c=\frac13\).

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 36,290 | Correct (7/7) | Complete pqr proof: the case p<=sqrt2 uses concavity of sqrt(1+2u)-3sqrt3*u^2 with positive endpoint values, and the case p>=sqrt2 uses Schur and the correct identity 48t-(t^2-2t+9)^2=w(48-40w+8w^2-w^3)>=0 with w=3-t. |
| A2 | stop | 36,368 | Correct (7/7) | Valid pqr/Schur proof: Case p<=sqrt2 via 27u^4<=16(1+u), Case p>=sqrt2 via substitution p=sqrt3 t and the correct factorization (t-1)(3t^3+3t^2+t-3), whose cubic factor is clearly positive for t>3/4. |
| A3 | stop | 37,194 | Correct (7/7) | Complete proof that even proves Schur's inequality via the SOS-type decomposition, then correctly handles t=p^2>=2 (Schur bound plus factorization) and t<=2 (Q<=q^2 and 27v^2<=16(1+v)). |
| A4 | stop | 33,334 | Correct (7/7) | Complete pqr proof: the case p<=sqrt2 uses concavity of 4p-3sqrt3(p^2-1)^2 with positive endpoint values, and the case p>=sqrt2 uses Schur to get Q<=(p^4-2p^2+9)/36 plus convexity of p^4-2p^2-4sqrt3p+9, whose endpoint values are 9-4sqrt6<0 and 0. |
| A5 | stop | 31,337 | Correct (7/7) | Complete pqr proof: the case u=p^2<=2 uses r>=0 and 27w^4<=16(1+w), and the case u>=2 uses Schur and the correct factorization 48u-(u^2-2u+9)^2=(3-u)(u^3-u^2+19u-27)>=0; the only unstated facts (p<=sqrt3, positivity of the cubic on [2,3]) are trivial. |
| A6 | stop | 38,118 | Correct (7/7) | Complete pqr proof: Case p<=sqrt2 bounds Q by (p^2-1)/4 and uses concavity of 4p-3sqrt3(p^2-1), Case p>=sqrt2 uses Schur and the correct factorization (t-3)(t^3-t^2+19t-27)<=0. |
| A7 | stop | 41,757 | Correct (7/7) | Complete proof showing 27M^2<=p^2 in both cases q<=1/2 (via q^4<=q/8) and q>=1/2 (Schur gives M<=(q^2+2)/9 and the verified factorization (1-q)(q^3+q^2+5q-1)>=0). |
| A8 | stop | 41,945 | Correct (7/7) | Complete pqr proof in R=xy+yz+zx: the case R<=1/2 uses Q<=R^2<=R/2 and 27R^2<=4(1+2R), and the case R>=1/2 uses Schur to get Q<=(R^2+2)/9 plus the correct factorization 3(1+2R)-(R^2+2)^2=(1-R)(R^3+R^2+5R-1)>=0. |
| A9 | stop | 44,677 | Correct (7/7) | Complete pqr argument: for u=p^2<=2 uses Q<=q^2 and 27v^4<=16u, for u>=2 uses Schur to get Q<=(u^2-2u+9)/36 and the verified factorization (u-3)(u^3-u^2+19u-27)<=0; all steps check out. |
| A10 | stop | 42,375 | Correct (7/7) | Complete pqr proof that also proves Schur: the case u<=2 uses 27v^4<=16(1+v), and the case u>=2 uses the correct factorization (u-3)(u^3-u^2+19u-27)<=0; a stray line ('M<=(u-1)/2?') is immediately replaced and does not affect the logic. |
| A11 | stop | 35,750 | Correct (7/7) | Complete pqr proof: with x=sqrt(a) etc. and sum x^2y^2 = q^2-2pr, the case p<=sqrt2 follows from r>=0 and 27q^4<=27q/8<=1+2q, and the case p>=sqrt2 follows from Schur (giving the bound (t^2-2t+9)/36) plus a valid concavity argument showing H(t)=4sqrt(3t)-t^2+2t-9>=0 on [2,3]; all computations check. |
| A12 | stop | 36,630 | Correct (7/7) | Valid pqr proof (x=sqrt a, Q=q^2-2pr, Schur 9r>=p(p^2-2)) with case split at p^2=2: concavity argument for p^2<=2 and the correct factorization (u-3)(u^3-u^2+19u-27) for p^2>=2; a stray self-corrected 'Wait, carefully' line is a presentation blemish that does not affect the logic. |
| A13 | stop | 42,820 | Correct (7/7) | Complete proof: Case p<=sqrt2 via a concave quadratic positive at endpoints, Case p>=sqrt2 via Schur and the correct factorization (w-sqrt3)(w^3+sqrt3w^2+w-3sqrt3) with an increasing, positive second factor. |
| A14 | stop | 33,122 | Correct (7/7) | Rigorous pqr/Schur proof with both cases fully verified, including derivation of Q=q^2-2pr and positivity of the cubic factor via C'(t)>0 and C(2)=15. |
| A15 | stop | 22,841 | Correct (7/7) | Correct and complete: the termwise bound sqrt(t)>=(3sqrt3/2)t(1-t) on (0,1) is proved rigorously from AM-GM (t(1-t)^2<=4/27), and summing it with sum a(1-a)=2(ab+bc+ca) gives the result. |
| A16 | stop | 47,458 | Correct (7/7) | Correct pqr proof parametrized by q: Schur gives 9rs>=4q^2-1, leading to Q<=(q^2+2)/9 for q>=1/2 with the verified factorization, and Q<=q^2<=s/(3sqrt3) for q<=1/2. |

<details><summary>A1: Correct (7/7)</summary>

Let  
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c.
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
We need to prove
\[
p:=x+y+z\ge 3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2),
\]
where
\[
Q=x^2y^2+y^2z^2+z^2x^2.
\]

Set also
\[
s=xy+yz+zx,\qquad r=xyz.
\]
Since \(x^2+y^2+z^2=1\),
\[
p^2=1+2s,\qquad Q=s^2-2pr.
\]
Also \(1\le p\le \sqrt3\).

### Case 1: \(p\le \sqrt2\)

Then
\[
s=\frac{p^2-1}{2}\le \frac12.
\]
Moreover,
\[
Q=s^2-2pr\le s^2.
\]
Thus it is enough to prove
\[
p=\sqrt{1+2s}\ge 3\sqrt3\,s^2.
\]
Let \(u=s\in[0,1/2]\) and define
\[
\phi(u)=\sqrt{1+2u}-3\sqrt3\,u^2.
\]
Since
\[
\phi''(u)=-(1+2u)^{-3/2}-6\sqrt3<0,
\]
\(\phi\) is concave, so its minimum on \([0,1/2]\) occurs at an endpoint. Now
\[
\phi(0)=1>0,
\]
and
\[
\phi\!\left(\frac12\right)=\sqrt2-\frac{3\sqrt3}{4}>0,
\]
because \(2>27/16\). Hence \(\phi(u)>0\), so
\[
p>3\sqrt3\,s^2\ge 3\sqrt3\,Q.
\]

### Case 2: \(p\ge \sqrt2\)

Let \(t=p^2\), so \(2\le t\le 3\). By Schur’s inequality,
\[
p^3+9r\ge 4ps.
\]
Since \(s=(t-1)/2\), this gives
\[
9r\ge p^3-2p=p(t-2),
\]
hence
\[
r\ge \frac{p(t-2)}9.
\]
Therefore
\[
Q=s^2-2pr
\le \frac{(t-1)^2}{4}-\frac{2t(t-2)}9
=\frac{t^2-2t+9}{36}.
\]
We claim
\[
\frac{t^2-2t+9}{36}\le \frac{\sqrt t}{3\sqrt3}.
\]
Indeed, after squaring, this is equivalent to
\[
(t^2-2t+9)^2\le 48t.
\]
Put \(w=3-t\in[0,1]\). Then \(t^2-2t+9=12-4w+w^2\), and
\[
48t-(t^2-2t+9)^2
= w(48-40w+8w^2-w^3)\ge0,
\]
because \(48-40w+8w^2-w^3\ge8>0\) on \([0,1]\). Thus
\[
Q\le \frac{\sqrt t}{3\sqrt3}=\frac{p}{3\sqrt3}.
\]
So
\[
3\sqrt3\,Q\le p.
\]

Combining both cases,
\[
\sqrt a+\sqrt b+\sqrt c=p\ge 3\sqrt3\,(ab+bc+ca).
\]

\[
\boxed{\sqrt{a}+\sqrt{b}+\sqrt{c}\ge 3\sqrt{3}(ab+bc+ca)}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

\[
\boxed{\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca)}
\]

Let
\[
x=\sqrt a,\qquad y=\sqrt b,\qquad z=\sqrt c .
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
We need to prove
\[
x+y+z\ge 3\sqrt3\bigl(x^2y^2+y^2z^2+z^2x^2\bigr).
\]

Set
\[
p=x+y+z,\qquad q=xy+yz+zx,\qquad r=xyz.
\]
Then
\[
p^2=1+2q \quad\Rightarrow\quad q=\frac{p^2-1}{2}.
\]
Also,
\[
x^2y^2+y^2z^2+z^2x^2=q^2-2pr.
\]
So the desired inequality becomes
\[
p\ge 3\sqrt3(q^2-2pr),
\]
or equivalently
\[
p+6\sqrt3\,pr\ge \frac{3\sqrt3}{4}(p^2-1)^2. \tag{1}
\]

Since \(x^2+y^2+z^2=1\), we have
\[
1\le p\le \sqrt3.
\]

### Case 1: \(p\le \sqrt2\)

Because \(r\ge0\), the left-hand side of (1) is at least \(p\). Thus it suffices to prove
\[
p\ge \frac{3\sqrt3}{4}(p^2-1)^2.
\]
Let \(u=p^2-1\in[0,1]\). Then \(p=\sqrt{1+u}\), and we need
\[
\sqrt{1+u}\ge \frac{3\sqrt3}{4}u^2.
\]
Squaring, this is equivalent to
\[
27u^4\le 16(1+u).
\]
Since \(0\le u\le1\),
\[
27u^4\le 27u^2\le 27u\le 16(1+u),
\]
because \(27u\le16(1+u)\iff 11u\le16\), which is true. Hence (1) holds in this case.

### Case 2: \(p\ge \sqrt2\)

By Schur’s inequality,
\[
p^3+9r\ge 4pq.
\]
Using \(q=\frac{p^2-1}{2}\), we get
\[
9r\ge p^3-2p=p(p^2-2),
\]
so
\[
r\ge \frac{p(p^2-2)}9.
\]
Therefore
\[
q^2-2pr
\le \frac{(p^2-1)^2}{4}-\frac{2p^2(p^2-2)}9
=\frac{p^4-2p^2+9}{36}.
\]
It remains to show
\[
\frac{p^4-2p^2+9}{36}\le \frac{p}{3\sqrt3}.
\]
Let \(p=\sqrt3\,t\), where \(t\in\left[\sqrt{\frac23},1\right]\). Then the inequality becomes
\[
3t^4-2t^2-4t+3\le0.
\]
But
\[
3t^4-2t^2-4t+3
=(t-1)(3t^3+3t^2+t-3).
\]
Here \(t-1\le0\), while
\[
3t^3+3t^2+t-3>0
\]
for \(t\ge \sqrt{\frac23}>\frac34\). Hence the product is nonpositive. Thus
\[
q^2-2pr\le \frac{p}{3\sqrt3},
\]
so (1) holds again.

Combining both cases proves
\[
x+y+z\ge 3\sqrt3(x^2y^2+y^2z^2+z^2x^2),
\]
i.e.
\[
\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca).
\]

\[
\boxed{\sqrt a+\sqrt b+\sqrt c \ge 3\sqrt3(ab+bc+ca)}
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

\[
\boxed{\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca)}
\]

Let
\[
x=\sqrt a,\qquad y=\sqrt b,\qquad z=\sqrt c .
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
We need to prove
\[
x+y+z\ge 3\sqrt3(x^2y^2+y^2z^2+z^2x^2).
\]

Set
\[
p=x+y+z,\quad q=xy+yz+zx,\quad r=xyz,
\]
and
\[
R=x^2y^2+y^2z^2+z^2x^2.
\]
Since \(p^2=x^2+y^2+z^2+2q=1+2q\), if we put \(t=p^2\), then
\[
q=\frac{t-1}{2},\qquad t\in[1,3].
\]
Also,
\[
q^2=R+2pr \quad\Longrightarrow\quad R=q^2-2pr.
\]
So it suffices to prove
\[
R\le \frac{p}{3\sqrt3}=\frac{\sqrt t}{3\sqrt3}.
\]

We use Schur’s inequality:
\[
p^3+9r\ge 4pq.
\]
Indeed, assuming \(x\ge y\ge z\),
\[
p^3+9r-4pq
=\sum_{\rm cyc}x(x-y)(x-z)
=(x-y)^2(x+y-z)+z(x-z)(y-z)\ge0.
\]
Thus
\[
9r\ge 4pq-p^3=p(p^2-2)=p(t-2).
\]

### Case 1: \(t\ge2\)
Then
\[
r\ge \frac{p(t-2)}9,
\]
so
\[
R=q^2-2pr
\le \frac{(t-1)^2}{4}-2p\cdot \frac{p(t-2)}9
=\frac{t^2-2t+9}{36}.
\]
Now for \(2\le t\le3\),
\[
(t^2-2t+9)^2\le 48t,
\]
because
\[
48t-(t^2-2t+9)^2
=(3-t)(t^3-t^2+19t-27)\ge0.
\]
Hence
\[
\frac{t^2-2t+9}{36}\le \frac{\sqrt t}{3\sqrt3}.
\]
Therefore
\[
R\le \frac{\sqrt t}{3\sqrt3}.
\]

### Case 2: \(t\le2\)
Since \(r\ge0\),
\[
R=q^2-2pr\le q^2=\frac{(t-1)^2}{4}.
\]
Let \(v=t-1\in[0,1]\). Then \(t=1+v\), and we claim
\[
\frac{v^2}{4}\le \frac{\sqrt{1+v}}{3\sqrt3}.
\]
Indeed, this is equivalent to
\[
3\sqrt3\,v^2\le 4\sqrt{1+v}.
\]
Since \(v\in[0,1]\),
\[
27v^2\le 27v\le 16+16v=16(1+v),
\]
so taking square roots gives
\[
3\sqrt3\,v\le 4\sqrt{1+v},
\]
and therefore
\[
3\sqrt3\,v^2\le 3\sqrt3\,v\le 4\sqrt{1+v}.
\]
Thus
\[
R\le q^2=\frac{v^2}{4}\le \frac{\sqrt{1+v}}{3\sqrt3}
=\frac{\sqrt t}{3\sqrt3}.
\]

So in both cases,
\[
R\le \frac{\sqrt t}{3\sqrt3}=\frac{p}{3\sqrt3}.
\]
Hence
\[
p\ge 3\sqrt3\,R,
\]
i.e.
\[
\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca).
\]

Equality holds at \(a=b=c=\frac13\).

</details>

<details><summary>A4: Correct (7/7)</summary>

Let  
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c.
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
We need to prove
\[
x+y+z\ge 3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2).
\]

Set
\[
p=x+y+z,\quad s=xy+yz+zx,\quad r=xyz,
\]
and
\[
Q=x^2y^2+y^2z^2+z^2x^2.
\]
Since \(x^2+y^2+z^2=1\),
\[
p^2=1+2s \quad\Longrightarrow\quad s=\frac{p^2-1}{2}.
\]
Also \(1\le p\le \sqrt3\), by \(p^2\le 3(x^2+y^2+z^2)=3\).

Now
\[
Q=s^2-2pr.
\]

### Case 1: \(p\le \sqrt2\)

Because \(r>0\), we have
\[
Q=s^2-2pr\le s^2=\frac{(p^2-1)^2}{4}.
\]
We claim
\[
\frac{(p^2-1)^2}{4}\le \frac{p}{3\sqrt3}.
\]
Indeed, define
\[
\phi(p)=4p-3\sqrt3(p^2-1)^2.
\]
For \(1\le p\le \sqrt2\),
\[
\phi''(p)=12\sqrt3(1-3p^2)<0,
\]
so \(\phi\) is concave. Hence its values lie above the chord joining its endpoints:
\[
\phi(p)\ge (1-t)\phi(1)+t\phi(\sqrt2)>0,
\]
where \(p=t\sqrt2+(1-t)\). Since
\[
\phi(1)=4>0,\qquad \phi(\sqrt2)=4\sqrt2-3\sqrt3>0
\]
because \(32>27\), we get \(\phi(p)>0\). Therefore
\[
3\sqrt3(p^2-1)^2\le 4p,
\]
so
\[
Q\le \frac{p}{3\sqrt3}.
\]

### Case 2: \(p\ge \sqrt2\)

By Schur’s inequality,
\[
p^3+9r\ge 4ps.
\]
Thus
\[
9r\ge 4ps-p^3,
\]
and hence
\[
Q=s^2-2pr
\le s^2-\frac{2p(4ps-p^3)}9.
\]
Substituting \(s=\frac{p^2-1}{2}\), we obtain
\[
Q\le \frac{p^4-2p^2+9}{36}.
\]

It remains to show
\[
\frac{p^4-2p^2+9}{36}\le \frac{p}{3\sqrt3}.
\]
This is equivalent to
\[
P(p):=p^4-2p^2-4\sqrt3\,p+9\le 0.
\]
For \(p\in[\sqrt2,\sqrt3]\),
\[
P''(p)=12p^2-4>0,
\]
so \(P\) is convex. Also
\[
P(\sqrt3)=0,\qquad P(\sqrt2)=9-4\sqrt6<0.
\]
Since a convex function lies below its chord, we get \(P(p)\le 0\) for all \(p\in[\sqrt2,\sqrt3]\). Therefore
\[
Q\le \frac{p}{3\sqrt3}.
\]

Combining both cases, we have always
\[
Q\le \frac{p}{3\sqrt3}.
\]
Multiplying by \(3\sqrt3\),
\[
3\sqrt3\,Q\le p,
\]
i.e.
\[
3\sqrt3\,(ab+bc+ca)\le \sqrt a+\sqrt b+\sqrt c.
\]

Equality holds at \(a=b=c=\frac13\).

\[
\boxed{\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca)}
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

\[
\boxed{\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca)}
\]

Proof. Put
\[
x=\sqrt a,\qquad y=\sqrt b,\qquad z=\sqrt c .
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
The desired inequality becomes
\[
x+y+z\ge 3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2).
\]

Let
\[
p=x+y+z,\qquad q=xy+yz+zx,\qquad r=xyz,
\]
and set \(u=p^2\). Since \(x^2+y^2+z^2=1\),
\[
p^2=1+2q \quad\Longrightarrow\quad q=\frac{u-1}{2}.
\]
Also \(1<u\le 3\). Let
\[
A=x^2y^2+y^2z^2+z^2x^2.
\]
Using
\[
q^2=(xy+yz+zx)^2=A+2pr,
\]
we get
\[
A=q^2-2pr.
\]

We prove \(A\le \frac{p}{3\sqrt3}\).

### Case 1: \(u\le 2\)

Since \(2pr\ge0\),
\[
A\le q^2=\frac{(u-1)^2}{4}.
\]
Put \(w=u-1\in[0,1]\). Then
\[
27w^4\le 27w\le 16+16w=16(1+w),
\]
so
\[
\frac{w^2}{4}\le \frac{\sqrt{1+w}}{3\sqrt3}.
\]
Therefore
\[
A\le \frac{(u-1)^2}{4}\le \frac{\sqrt u}{3\sqrt3}=\frac{p}{3\sqrt3}.
\]

### Case 2: \(2\le u\le 3\)

By Schur’s inequality,
\[
p^3+9r\ge 4pq.
\]
Since \(p=\sqrt u\) and \(q=\frac{u-1}{2}\),
\[
9r\ge 4p\cdot \frac{u-1}{2}-p^3
=p(u-2)=\sqrt u(u-2).
\]
Hence
\[
A=q^2-2pr
\le \frac{(u-1)^2}{4}-\frac{2u(u-2)}9
=\frac{u^2-2u+9}{36}.
\]
Now for \(2\le u\le 3\),
\[
48u-(u^2-2u+9)^2
=(3-u)(u^3-u^2+19u-27)\ge0,
\]
because \(3-u\ge0\) and \(u^3-u^2+19u-27>0\) on this interval. Thus
\[
\frac{u^2-2u+9}{36}\le \frac{\sqrt u}{3\sqrt3}
=\frac{p}{3\sqrt3}.
\]
So again \(A\le \frac{p}{3\sqrt3}\).

Therefore in all cases,
\[
A\le \frac{p}{3\sqrt3}
\quad\Longrightarrow\quad
p\ge 3\sqrt3\,A.
\]
Substituting back \(x=\sqrt a\), etc.,
\[
\sqrt a+\sqrt b+\sqrt c
\ge 3\sqrt3(ab+bc+ca).
\]

Equality holds at \(a=b=c=\frac13\).

</details>

<details><summary>A6: Correct (7/7)</summary>

Let  
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c.
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
We need to prove
\[
x+y+z\ge 3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2).
\]

Set
\[
p=x+y+z,\quad u=xy+yz+zx,\quad v=xyz,
\]
and
\[
T=x^2y^2+y^2z^2+z^2x^2.
\]
Since \(x^2+y^2+z^2=1\),
\[
p^2=1+2u \quad\Longrightarrow\quad u=\frac{p^2-1}{2}.
\]
Also
\[
T=u^2-2pv.
\]

We prove \(p\ge 3\sqrt3\,T\).

### Case 1: \(p\le \sqrt2\)

Since \(pv\ge0\),
\[
T=u^2-2pv\le u^2=\frac{(p^2-1)^2}{4}.
\]
Because \(p^2-1\le1\),
\[
u^2=\frac{(p^2-1)^2}{4}\le\frac{p^2-1}{4}.
\]
Now define
\[
g(p)=4p-3\sqrt3(p^2-1).
\]
Then \(g''(p)=-6\sqrt3<0\), so \(g\) is concave. Hence on \([1,\sqrt2]\) its minimum occurs at an endpoint. But
\[
g(1)=4>0,\qquad g(\sqrt2)=4\sqrt2-3\sqrt3>0
\]
since \(32>27\). Therefore \(g(p)\ge0\), i.e.
\[
\frac{p^2-1}{4}\le \frac{p}{3\sqrt3}.
\]
Thus
\[
T\le \frac{p}{3\sqrt3}.
\]

### Case 2: \(p\ge\sqrt2\)

By Schur’s inequality,
\[
p^3+9v\ge 4pu.
\]
Using \(u=\frac{p^2-1}{2}\),
\[
9v\ge p^3-2p=p(p^2-2),
\]
so
\[
v\ge \frac{p(p^2-2)}9.
\]
Hence
\[
T=u^2-2pv
\le \frac{(p^2-1)^2}{4}-\frac{2p^2(p^2-2)}9.
\]
Let \(t=p^2\), so \(2\le t\le3\). Then
\[
T\le \frac{t^2-2t+9}{36}.
\]
We claim
\[
\frac{t^2-2t+9}{36}\le \frac{\sqrt t}{3\sqrt3}.
\]
Indeed, this is equivalent to
\[
t^2-2t+9\le 4\sqrt{3t}.
\]
Squaring both sides gives
\[
(t^2-2t+9)^2-48t
=(t-3)(t^3-t^2+19t-27)\le0,
\]
because \(t-3\le0\) and
\[
t^3-t^2+19t-27\ge 15>0
\]
for \(2\le t\le3\). Therefore
\[
T\le \frac{p}{3\sqrt3}.
\]

Thus in all cases \(p\ge 3\sqrt3\,T\). Returning to \(x,y,z\),
\[
\sqrt a+\sqrt b+\sqrt c=x+y+z=p\ge 3\sqrt3\,T
=3\sqrt3(ab+bc+ca).
\]

Equality occurs at \(a=b=c=\frac13\).

\[
\boxed{\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca)}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

Let  
\[
x=\sqrt a,\qquad y=\sqrt b,\qquad z=\sqrt c .
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
Define
\[
p=x+y+z,\qquad q=xy+yz+zx,\qquad r=xyz,
\]
and
\[
M=x^2y^2+y^2z^2+z^2x^2=ab+bc+ca.
\]
We need to prove
\[
p\ge 3\sqrt3\,M.
\]

First note the identities
\[
p^2=x^2+y^2+z^2+2q=1+2q,
\]
and
\[
q^2=x^2y^2+y^2z^2+z^2x^2+2xyz(x+y+z)=M+2pr,
\]
so
\[
M=q^2-2pr.
\]

By Schur’s inequality,
\[
p^3+9r\ge 4pq.
\]
Using \(p^2=1+2q\), this gives
\[
9r\ge p(4q-p^2)=p(2q-1).
\]

### Case 1: \(q\le \frac12\)

Then \(M\le q^2\), so
\[
27M^2\le 27q^4.
\]
Since \(q\le \frac12\), we have \(q^3\le \frac18\), hence \(q^4\le q/8\). Therefore
\[
27q^4\le \frac{27q}{8}\le 1+2q=p^2.
\]
Thus
\[
27M^2\le p^2.
\]

### Case 2: \(q\ge \frac12\)

From Schur,
\[
r\ge \frac{p(2q-1)}9.
\]
Therefore
\[
M=q^2-2pr\le q^2-\frac{2p^2(2q-1)}9.
\]
Using \(p^2=1+2q\),
\[
M\le q^2-\frac{2(1+2q)(2q-1)}9
=\frac{q^2+2}{9}.
\]
Hence
\[
27M^2\le \frac{(q^2+2)^2}{3}.
\]
Now for \(q\in[\frac12,1]\),
\[
3(1+2q)-(q^2+2)^2
=(1-q)(q^3+q^2+5q-1)\ge0,
\]
so
\[
\frac{(q^2+2)^2}{3}\le 1+2q=p^2.
\]
Thus again
\[
27M^2\le p^2.
\]

In both cases,
\[
27M^2\le p^2.
\]
Since \(p,M>0\), taking square roots gives
\[
p\ge 3\sqrt3\,M.
\]
Recalling the definitions,
\[
\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca).
\]

Equality occurs at \(a=b=c=\frac13\).

</details>

<details><summary>A8: Correct (7/7)</summary>

\[
\boxed{\sqrt a+\sqrt b+\sqrt c \ge 3\sqrt3(ab+bc+ca)}
\]

Let
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c .
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
Define
\[
P=x+y+z,\qquad R=xy+yz+zx,\qquad Q=x^2y^2+y^2z^2+z^2x^2.
\]
We need to prove \(P\ge 3\sqrt3\,Q\). Note that
\[
Q=ab+bc+ca.
\]

We have
\[
P^2=x^2+y^2+z^2+2R=1+2R,
\]
so \(P=\sqrt{1+2R}\). Also \(R\le 1\), and
\[
Q=R^2-2xyz(x+y+z)=R^2-2PT,
\]
where \(T=xyz\).

By Schur’s inequality,
\[
P^3+9T\ge 4PR.
\]
Since \(P^2=1+2R\), dividing by \(P>0\) gives
\[
9T\ge P(2R-1). \tag{1}
\]

### Case 1: \(R\le \frac12\)
Then \(Q=R^2-2PT\le R^2\). Also \(R\le \frac12\) implies
\[
R^2\le \frac R2.
\]
Moreover,
\[
27R^2-8R-4\le 0 \quad \text{for }0\le R\le \frac12,
\]
because the convex function \(27R^2-8R-4\) is negative at both endpoints \(R=0\) and \(R=\frac12\). Hence
\[
27R^2\le 4+8R=4(1+2R).
\]
Taking square roots,
\[
\frac R2\le \frac{\sqrt{1+2R}}{3\sqrt3}=\frac{P}{3\sqrt3}.
\]
Therefore
\[
Q\le R^2\le \frac R2\le \frac{P}{3\sqrt3},
\]
so \(P\ge 3\sqrt3\,Q\).

### Case 2: \(R\ge \frac12\)
From (1),
\[
T\ge \frac{P(2R-1)}9.
\]
Thus
\[
Q=R^2-2PT
\le R^2-\frac{2P^2(2R-1)}9.
\]
Using \(P^2=1+2R\),
\[
Q\le R^2-\frac{2(1+2R)(2R-1)}9
=R^2-\frac{2(4R^2-1)}9
=\frac{R^2+2}{9}.
\]
Now for \(R\in\left[\frac12,1\right]\),
\[
3(1+2R)-(R^2+2)^2
=(1-R)(R^3+R^2+5R-1)\ge 0.
\]
Hence
\[
\frac{R^2+2}{9}\le \frac{\sqrt{3(1+2R)}}9
=\frac{P}{3\sqrt3}.
\]
So again
\[
Q\le \frac{P}{3\sqrt3},
\]
which gives \(P\ge 3\sqrt3\,Q\).

Both cases cover all possible \(R\), so
\[
\sqrt a+\sqrt b+\sqrt c=P\ge 3\sqrt3\,Q=3\sqrt3(ab+bc+ca).
\]

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

Let  
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c.
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
We need to prove
\[
x+y+z\ge 3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2).
\]

Define
\[
s=x+y+z,\qquad t=xy+yz+zx,\qquad r=xyz,
\]
and put \(u=s^2\). Since
\[
u=s^2=x^2+y^2+z^2+2t=1+2t,
\]
we have
\[
t=\frac{u-1}{2},\qquad 1\le u\le 3.
\]
Also
\[
Q:=x^2y^2+y^2z^2+z^2x^2=t^2-2sr.
\]

### Case 1: \(1\le u\le 2\)

Since \(r\ge0\),
\[
Q\le t^2=\frac{(u-1)^2}{4}.
\]
Let \(v=u-1\in[0,1]\). Then
\[
27v^4\le 27v^2\le 27v\le 16+16v=16u.
\]
Taking square roots gives
\[
\frac{v^2}{4}\le \frac{\sqrt u}{3\sqrt3},
\]
so
\[
Q\le \frac{(u-1)^2}{4}\le \frac{\sqrt u}{3\sqrt3}=\frac{s}{3\sqrt3}.
\]

### Case 2: \(2\le u\le 3\)

By Schur’s inequality,
\[
s^3+9r\ge 4st.
\]
Using \(t=(u-1)/2\), this gives
\[
9r\ge s(u-2),
\]
hence
\[
r\ge \frac{s(u-2)}9.
\]
Therefore
\[
Q=t^2-2sr
\le t^2-\frac{2u(u-2)}9
=\frac{u^2-2u+9}{36}.
\]
Now for \(2\le u\le 3\),
\[
(u^2-2u+9)^2-48u
=(u-3)(u^3-u^2+19u-27)\le0,
\]
because \(u-3\le0\) and \(u^3-u^2+19u-27>0\). Hence
\[
\frac{u^2-2u+9}{36}\le \frac{\sqrt u}{3\sqrt3}
=\frac{s}{3\sqrt3}.
\]
So again \(Q\le s/(3\sqrt3)\).

Thus in all cases,
\[
Q\le \frac{s}{3\sqrt3},
\]
or equivalently
\[
3\sqrt3\,Q\le s.
\]
Returning to \(a,b,c\),
\[
3\sqrt3(ab+bc+ca)\le \sqrt a+\sqrt b+\sqrt c.
\]

\[
\boxed{\sqrt a+\sqrt b+\sqrt c \ge 3\sqrt3(ab+bc+ca)}
\]

Equality holds at \(a=b=c=\frac13\).

</details>

<details><summary>A10: Correct (7/7)</summary>

Let  
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c .
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
We need to prove
\[
ab+bc+ca=x^2y^2+y^2z^2+z^2x^2\le \frac{x+y+z}{3\sqrt3}.
\]

Set
\[
p=x+y+z,\quad q=xy+yz+zx,\quad r=xyz,
\]
and let
\[
M=x^2y^2+y^2z^2+z^2x^2.
\]
Since
\[
q^2=M+2pr,
\]
we have
\[
M=q^2-2pr.
\]
Also
\[
p^2=x^2+y^2+z^2+2q=1+2q,
\]
so if \(u=p^2\), then
\[
q=\frac{u-1}{2},\qquad 1\le u\le 3.
\]

We first recall Schur’s inequality:
\[
p^3+9r\ge 4pq.
\]
For completeness, if \(x\ge y\ge z\), then
\[
p^3+9r-4pq
=\sum_{\rm cyc}x(x-y)(x-z)
=(x-y)^2(x+y-z)+z(x-z)(y-z)\ge0.
\]

Now split into two cases.

### Case 1: \(u\le 2\)
Since \(r>0\),
\[
M=q^2-2pr\le q^2=\frac{(u-1)^2}{4}.
\]
Put \(v=u-1\in[0,1]\). We claim
\[
\frac{v^2}{4}\le \frac{\sqrt{1+v}}{3\sqrt3}.
\]
Indeed,
\[
27v^4\le 27v^2\le 27v\le 16+16v=16(1+v),
\]
so taking square roots gives
\[
3\sqrt3\,v^2\le 4\sqrt{1+v},
\]
or equivalently
\[
\frac{v^2}{4}\le \frac{\sqrt{1+v}}{3\sqrt3}.
\]
Thus
\[
M\le \frac{u-1}{2}? 
\]
More precisely,
\[
M\le \frac{(u-1)^2}{4}\le \frac{\sqrt u}{3\sqrt3}=\frac{p}{3\sqrt3}.
\]

### Case 2: \(u\ge 2\)
Schur gives
\[
9r\ge 4pq-p^3=p(u-2).
\]
Therefore
\[
2pr\ge \frac{2u(u-2)}9,
\]
and hence
\[
M=q^2-2pr
\le \frac{(u-1)^2}{4}-\frac{2u(u-2)}9
=\frac{u^2-2u+9}{36}.
\]
Let \(A=u^2-2u+9\). For \(2\le u\le 3\),
\[
A^2-48u=(u-3)(u^3-u^2+19u-27)\le0,
\]
because \(u-3\le0\) and \(u^3-u^2+19u-27\ge0\). Hence
\[
A\le 4\sqrt{3u},
\]
so
\[
\frac{A}{36}\le \frac{\sqrt u}{3\sqrt3}=\frac{p}{3\sqrt3}.
\]
Thus again
\[
M\le \frac{p}{3\sqrt3}.
\]

In both cases,
\[
ab+bc+ca=M\le \frac{x+y+z}{3\sqrt3}
=\frac{\sqrt a+\sqrt b+\sqrt c}{3\sqrt3}.
\]
Multiplying by \(3\sqrt3\), we obtain
\[
3\sqrt3(ab+bc+ca)\le \sqrt a+\sqrt b+\sqrt c.
\]

Equality holds at \(x=y=z=\frac1{\sqrt3}\), i.e. \(a=b=c=\frac13\).

\[
\boxed{\sqrt a+\sqrt b+\sqrt c \ge 3\sqrt3(ab+bc+ca)}
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

\[
\boxed{\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca)}
\]

Let
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c.
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
The desired inequality becomes
\[
x+y+z\ge 3\sqrt3(x^2y^2+y^2z^2+z^2x^2).
\]

Set
\[
p=x+y+z,\quad q=xy+yz+zx,\quad r=xyz.
\]
Since \(x^2+y^2+z^2=1\),
\[
p^2=1+2q,\qquad p\in(1,\sqrt3].
\]
Also
\[
x^2y^2+y^2z^2+z^2x^2=q^2-2pr.
\]
So it remains to prove
\[
p\ge 3\sqrt3\,(q^2-2pr).
\]

We use Schur’s inequality:
\[
p^3+9r\ge 4pq.
\]
Since \(q=\frac{p^2-1}{2}\), this gives
\[
9r\ge p^3-2p=p(p^2-2).
\]

### Case 1: \(p\le \sqrt2\)

Then
\[
q=\frac{p^2-1}{2}\le \frac12.
\]
Because \(r\ge0\),
\[
q^2-2pr\le q^2.
\]
Also, for \(0\le q\le \frac12\),
\[
27q^4\le \frac{27q}{8}\le 1+2q=p^2.
\]
Hence
\[
3\sqrt3\,q^2\le p,
\]
so
\[
q^2\le \frac{p}{3\sqrt3}.
\]
Therefore
\[
q^2-2pr\le \frac{p}{3\sqrt3},
\]
which proves the desired inequality in this case.

### Case 2: \(p\ge \sqrt2\)

Let \(t=p^2\). Then \(t\in[2,3]\). From Schur,
\[
9r\ge p(p^2-2)=p(t-2),
\]
so
\[
r\ge \frac{p(t-2)}9.
\]
Thus
\[
q^2-2pr
\le q^2-\frac{2p^2(t-2)}9.
\]
Since \(q=\frac{t-1}{2}\),
\[
q^2-\frac{2t(t-2)}9
=\frac{(t-1)^2}{4}-\frac{2t(t-2)}9
=\frac{t^2-2t+9}{36}.
\]
So
\[
q^2-2pr\le \frac{t^2-2t+9}{36}.
\]

Now we show
\[
\frac{t^2-2t+9}{36}\le \frac{\sqrt t}{3\sqrt3}.
\]
This is equivalent to
\[
t^2-2t+9\le 4\sqrt{3t}.
\]
Define
\[
H(t)=4\sqrt{3t}-t^2+2t-9.
\]
For \(t\in[2,3]\),
\[
H''(t)=-\frac{\sqrt3}{t^{3/2}}-2<0,
\]
so \(H\) is concave. Also
\[
H(3)=0,\qquad H(2)=4\sqrt6-9>0.
\]
Therefore, by concavity,
\[
H(t)\ge (3-t)H(2)\ge0.
\]
Hence
\[
\frac{t^2-2t+9}{36}\le \frac{\sqrt t}{3\sqrt3}
=\frac{p}{3\sqrt3}.
\]
So again
\[
q^2-2pr\le \frac{p}{3\sqrt3},
\]
which gives
\[
p\ge 3\sqrt3\,(q^2-2pr).
\]

Thus in all cases,
\[
x+y+z\ge 3\sqrt3(x^2y^2+y^2z^2+z^2x^2).
\]
Substituting back \(x=\sqrt a\), \(y=\sqrt b\), \(z=\sqrt c\), we obtain
\[
\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca).
\]

\[
\boxed{\text{Proved}}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

Let  
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c .
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
We need to prove
\[
x+y+z\ge 3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2).
\]

Set
\[
p=x+y+z,\qquad t=xy+yz+zx,\qquad r=xyz,
\]
and
\[
Q=x^2y^2+y^2z^2+z^2x^2=ab+bc+ca.
\]
Since \(p^2=1+2t\),
\[
t=\frac{p^2-1}{2}.
\]
Also,
\[
t^2=Q+2pr,
\]
so
\[
Q=t^2-2pr. \tag{1}
\]

By Schur’s inequality,
\[
p^3+9r\ge 4pt.
\]
Using \(t=\frac{p^2-1}{2}\), this gives
\[
9r\ge p(p^2-2). \tag{2}
\]

Now consider two cases.

### Case 1: \(p^2\le 2\)

From (1), since \(r>0\),
\[
Q\le t^2=\frac{(p^2-1)^2}{4}.
\]
Let \(u=p^2\), so \(1\le u\le 2\). We show
\[
\frac{(u-1)^2}{4}\le \frac{\sqrt u}{3\sqrt3}.
\]
Define
\[
g(u)=\frac{\sqrt u}{3\sqrt3}-\frac{(u-1)^2}{4}.
\]
A direct derivative check gives \(g''(u)<0\), so \(g\) is concave on \([1,2]\). Also
\[
g(1)=\frac1{3\sqrt3}>0,
\]
and
\[
g(2)=\frac{\sqrt2}{3\sqrt3}-\frac14>0
\]
because \(4\sqrt2>3\sqrt3\). Hence \(g(u)\ge 0\) for all \(u\in[1,2]\). Therefore
\[
Q\le \frac{p^2-1}{2?}
\]
Wait, carefully:
\[
Q\le \frac{(u-1)^2}{4}\le \frac{\sqrt u}{3\sqrt3}=\frac{p}{3\sqrt3}.
\]
Thus \(Q\le p/(3\sqrt3)\).

### Case 2: \(p^2\ge 2\)

Let \(u=p^2\). Then \(2\le u\le 3\). From (2),
\[
r\ge \frac{p(u-2)}9.
\]
Using this in (1),
\[
Q\le \frac{(u-1)^2}{4}-\frac{2u(u-2)}9
=\frac{u^2-2u+9}{36}.
\]
It remains to show
\[
\frac{u^2-2u+9}{36}\le \frac{\sqrt u}{3\sqrt3}.
\]
This is equivalent to
\[
u^2-2u+9\le 4\sqrt{3u}.
\]
Squaring both sides, it suffices to prove
\[
(u^2-2u+9)^2-48u\le 0.
\]
But
\[
(u^2-2u+9)^2-48u
=(u-3)(u^3-u^2+19u-27).
\]
For \(u\in[2,3]\), \(u-3\le 0\), and
\[
u^3-u^2+19u-27
=u^2(u-1)+19u-27>0.
\]
Hence the product is \(\le 0\), so the desired inequality follows.

Thus in both cases,
\[
Q\le \frac{p}{3\sqrt3}.
\]
Since \(Q=ab+bc+ca\) and \(p=\sqrt a+\sqrt b+\sqrt c\), we get
\[
\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca).
\]

Equality holds at \(a=b=c=\frac13\).

\[
\boxed{\sqrt a+\sqrt b+\sqrt c \ge 3\sqrt3(ab+bc+ca)}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

Let  
\[
x=\sqrt a,\qquad y=\sqrt b,\qquad z=\sqrt c.
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
The desired inequality becomes
\[
x+y+z\ge 3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2). \tag{1}
\]

Set
\[
p=x+y+z,\quad r=xy+yz+zx,\quad t=xyz,
\]
and denote
\[
Q=x^2y^2+y^2z^2+z^2x^2.
\]
Since \(x^2+y^2+z^2=1\),
\[
p^2=1+2r,\qquad Q=r^2-2pt. \tag{2}
\]
Also \(1\le p\le \sqrt3\).

We prove \(3\sqrt3\,Q\le p\).

### Case 1: \(p\le \sqrt2\)
Then \(r=(p^2-1)/2\le 1/2\). Since \(Q\le r^2\), it is enough to show \(3\sqrt3\,r^2\le p\). But \(r\le 1/2\) gives
\[
3\sqrt3\,r^2\le \frac{3\sqrt3}{2}r.
\]
Also \(p=\sqrt{1+2r}\), so we need
\[
\frac{3\sqrt3}{2}r\le \sqrt{1+2r}.
\]
Squaring, this is equivalent to
\[
1+2r-\frac{27}{4}r^2\ge 0.
\]
For \(0\le r\le 1/2\), the function \(h(r)=1+2r-\frac{27}{4}r^2\) is concave, with
\[
h(0)=1,\qquad h(1/2)=\frac5{16}>0.
\]
Hence \(h(r)>0\), so \(3\sqrt3\,Q\le p\).

### Case 2: \(p\ge \sqrt2\)
By Schur’s inequality,
\[
p^3+9t\ge 4pr.
\]
Using \(r=(p^2-1)/2\), this gives
\[
9t\ge p(p^2-2).
\]
Therefore
\[
Q=r^2-2pt
\le \frac{(p^2-1)^2}{4}-\frac{2p^2(p^2-2)}9.
\]
Put \(u=p^2\in[2,3]\). Then
\[
Q\le \frac{u^2-2u+9}{36}.
\]
We claim
\[
\frac{u^2-2u+9}{36}\le \frac{\sqrt u}{3\sqrt3}.
\]
Equivalently, with \(w=\sqrt u=p\),
\[
w^4-2w^2-4\sqrt3\,w+9\le 0.
\]
Factor:
\[
w^4-2w^2-4\sqrt3\,w+9
=(w-\sqrt3)(w^3+\sqrt3w^2+w-3\sqrt3).
\]
For \(w\in[\sqrt2,\sqrt3]\), the first factor is \(\le0\). The second factor is increasing and positive because at \(w=\sqrt2\) it equals \(3\sqrt2-\sqrt3>0\). Hence the product is \(\le0\). Thus
\[
Q\le \frac{p}{3\sqrt3},
\]
so \(3\sqrt3\,Q\le p\).

In both cases \(3\sqrt3\,Q\le p\), i.e.
\[
3\sqrt3(x^2y^2+y^2z^2+z^2x^2)\le x+y+z.
\]
Since \(x^2y^2+y^2z^2+z^2x^2=ab+bc+ca\), we obtain
\[
\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca).
\]

Equality holds at \(a=b=c=\frac13\).

</details>

<details><summary>A14: Correct (7/7)</summary>

\[
\boxed{\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca)}
\]

Let
\[
x=\sqrt a,\quad y=\sqrt b,\quad z=\sqrt c.
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
Also
\[
ab+bc+ca=x^2y^2+y^2z^2+z^2x^2.
\]

Define
\[
p=x+y+z,\qquad q=xy+yz+zx,\qquad r=xyz.
\]
Since
\[
p^2=x^2+y^2+z^2+2q=1+2q,
\]
we have
\[
q=\frac{p^2-1}{2}.
\]
Moreover,
\[
q^2=(xy+yz+zx)^2=x^2y^2+y^2z^2+z^2x^2+2xyz(x+y+z),
\]
so
\[
T:=x^2y^2+y^2z^2+z^2x^2=q^2-2pr. \tag{1}
\]

We will prove \(T\le \frac{p}{3\sqrt3}\), which is exactly the desired inequality.

---

### Case 1: \(p\le \sqrt2\)

Let \(t=p^2\), so \(1\le t\le2\). Put \(u=t-1\), hence \(0\le u\le1\). Since \(r\ge0\),
\[
T\le q^2=\frac{(p^2-1)^2}{4}=\frac{u^2}{4}.
\]
Now \(u\le1\), so \(u^4\le u\). Hence
\[
27u^4\le27u\le16u+16=16t.
\]
Taking square roots gives
\[
3\sqrt3\,u^2\le4\sqrt t.
\]
Dividing by \(12\sqrt3\),
\[
\frac{u^2}{4}\le\frac{\sqrt t}{3\sqrt3}.
\]
Thus
\[
T\le q^2=\frac{u^2}{4}\le \frac{\sqrt t}{3\sqrt3}=\frac{p}{3\sqrt3}.
\]

---

### Case 2: \(p\ge \sqrt2\)

Then \(2\le t=p^2\le3\). By Schur’s inequality,
\[
p^3+9r\ge4pq.
\]
Using \(q=\frac{p^2-1}{2}\),
\[
p^3+9r\ge2p(p^2-1),
\]
so
\[
9r\ge p^3-2p=p(p^2-2).
\]
Therefore, from (1),
\[
T=q^2-2pr
\le \frac{(p^2-1)^2}{4}-\frac{2p^2(p^2-2)}{9}.
\]
Let \(t=p^2\). Then
\[
T\le \frac{(t-1)^2}{4}-\frac{2t(t-2)}{9}
=\frac{t^2-2t+9}{36}. \tag{2}
\]

It remains to show
\[
\frac{t^2-2t+9}{36}\le \frac{\sqrt t}{3\sqrt3}.
\]
Equivalently,
\[
t^2-2t+9\le4\sqrt{3t}.
\]
Let \(P=t^2-2t+9\). Since both sides are nonnegative, it suffices to prove
\[
P^2\le48t.
\]
But
\[
P^2-48t=(t-3)(t^3-t^2+19t-27).
\]
For \(2\le t\le3\), we have \(t-3\le0\). Also
\[
C(t)=t^3-t^2+19t-27
\]
has
\[
C'(t)=3t^2-2t+19>0
\]
for all real \(t\), and
\[
C(2)=8-4+38-27=15>0.
\]
Hence \(C(t)>0\), so
\[
P^2-48t\le0.
\]
Thus
\[
T\le \frac{t^2-2t+9}{36}\le \frac{\sqrt t}{3\sqrt3}=\frac{p}{3\sqrt3}.
\]

---

In both cases we have proved
\[
T\le \frac{p}{3\sqrt3}.
\]
Multiplying by \(3\sqrt3\),
\[
3\sqrt3\,T\le p,
\]
i.e.
\[
3\sqrt3(ab+bc+ca)\le \sqrt a+\sqrt b+\sqrt c.
\]

Equality holds at \(a=b=c=\frac13\).

\[
\boxed{\sqrt a+\sqrt b+\sqrt c \ge 3\sqrt{3}(ab+bc+ca)}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

Let  
\[
q=ab+bc+ca.
\]

We prove the following simple termwise estimate. For \(0<t<1\),

\[
\sqrt t \ge \frac{3\sqrt3}{2}t(1-t).
\]

Indeed, by AM-GM,

\[
t(1-t)^2
=4t\left(\frac{1-t}{2}\right)\left(\frac{1-t}{2}\right)
\le 4\left(\frac{t+\frac{1-t}{2}+\frac{1-t}{2}}{3}\right)^3
=\frac4{27}.
\]

Thus

\[
\sqrt t(1-t)\le \frac{2}{3\sqrt3},
\]

and multiplying by \(\sqrt t\) gives

\[
t(1-t)\le \frac{2\sqrt t}{3\sqrt3},
\]

so

\[
\sqrt t \ge \frac{3\sqrt3}{2}t(1-t).
\]

Applying this to \(t=a,b,c\), we get

\[
\sqrt a+\sqrt b+\sqrt c
\ge \frac{3\sqrt3}{2}\bigl(a(1-a)+b(1-b)+c(1-c)\bigr).
\]

Now

\[
a(1-a)+b(1-b)+c(1-c)
=a+b+c-(a^2+b^2+c^2)
=1-(a^2+b^2+c^2).
\]

Since

\[
1=(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca),
\]

we have

\[
1-(a^2+b^2+c^2)=2(ab+bc+ca).
\]

Therefore

\[
\sqrt a+\sqrt b+\sqrt c
\ge \frac{3\sqrt3}{2}\cdot 2(ab+bc+ca)
=3\sqrt3(ab+bc+ca).
\]

Hence

\[
\boxed{\sqrt a+\sqrt b+\sqrt c \ge 3\sqrt3(ab+bc+ca)}.
\]

Equality holds at \(a=b=c=\frac13\).

</details>

<details><summary>A16: Correct (7/7)</summary>

Let  
\[
x=\sqrt a,\qquad y=\sqrt b,\qquad z=\sqrt c .
\]
Then \(x,y,z>0\) and
\[
x^2+y^2+z^2=1.
\]
We need to prove
\[
x+y+z\ge 3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2).
\]

Set
\[
s=x+y+z,\qquad t=xy+yz+zx,\qquad r=xyz.
\]
Then
\[
s^2=1+2t,
\]
and
\[
x^2y^2+y^2z^2+z^2x^2=t^2-2rs.
\]

By Schur’s inequality,
\[
s^3+9r\ge 4st.
\]
Since \(s^2=1+2t\), this gives
\[
9rs\ge s^2(2t-1)=(1+2t)(2t-1)=4t^2-1. \tag{1}
\]

We split into two cases.

### Case 1: \(t\le \frac12\)
Since \(rs\ge0\),
\[
x^2y^2+y^2z^2+z^2x^2=t^2-2rs\le t^2.
\]
Also \(t\le \frac12\) implies
\[
t^2\le \frac t2\le \frac{\sqrt{1+2t}}{3\sqrt3}=\frac{s}{3\sqrt3}.
\]
Indeed, squaring the last inequality gives
\[
27t^2\le 4+8t,
\]
which follows from \(t\le \frac12\) because
\[
27t^2\le \frac{27}{2}t\le 4+8t.
\]
Thus
\[
x^2y^2+y^2z^2+z^2x^2\le \frac{s}{3\sqrt3}.
\]

### Case 2: \(t\ge \frac12\)
From (1),
\[
x^2y^2+y^2z^2+z^2x^2
=t^2-2rs
\le t^2-\frac{2(4t^2-1)}9
=\frac{t^2+2}{9}.
\]
Let \(m=1+2t\). Then \(m\in[2,3]\), and
\[
\frac{t^2+2}{9}
=\frac{m^2-2m+9}{36}.
\]
So it remains to show
\[
\frac{m^2-2m+9}{36}\le \frac{\sqrt m}{3\sqrt3}.
\]
This is equivalent to
\[
m^2-2m+9\le 4\sqrt{3m}.
\]
Squaring both sides,
\[
(m^2-2m+9)^2\le 48m.
\]
But
\[
48m-(m^2-2m+9)^2
=(3-m)(m^3-m^2+19m-27)\ge0,
\]
because \(3-m\ge0\) and for \(m\ge2\),
\[
m^3-m^2+19m-27=m^2(m-1)+19m-27\ge4+38-27>0.
\]
Hence
\[
\frac{t^2+2}{9}\le \frac{s}{3\sqrt3}.
\]

Therefore in both cases,
\[
x^2y^2+y^2z^2+z^2x^2\le \frac{s}{3\sqrt3}.
\]
Multiplying by \(3\sqrt3\), we get
\[
3\sqrt3\,(x^2y^2+y^2z^2+z^2x^2)\le s.
\]
Since \(x^2y^2+y^2z^2+z^2x^2=ab+bc+ca\) and \(s=\sqrt a+\sqrt b+\sqrt c\), the desired inequality follows.

Equality holds at \(a=b=c=\frac13\).

\[
\boxed{\sqrt a+\sqrt b+\sqrt c\ge 3\sqrt3(ab+bc+ca)}
\]

</details>
