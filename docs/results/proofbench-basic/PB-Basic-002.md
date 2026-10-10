# PB-Basic-002

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Show that $x^2 + y^2 + z^2 + t^2 \ge xyzt$ for any positive real numbers $x, y, z, t$ that satisfy $2(x + y + z + t) \ge xyzt$.

## Swarm: accepted (best candidate `P5`; self-verification grades [7, 7, 7]; 205,839 tokens in 48 calls)

**Blind grade: Correct (7/7).** Correct and complete case split on P<=16 (AM-GM) and P>=16 (Cauchy-Schwarz with S>=P/2 giving Q>=P^2/16>=P), with all inequalities valid.

Let  
\[
P=xyzt,\qquad S=x+y+z+t,\qquad Q=x^2+y^2+z^2+t^2.
\]
We are given \(2S\ge P\).

### Case 1: \(P\le 16\)
By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
Q=x^2+y^2+z^2+t^2\ge 4(x^2y^2z^2t^2)^{1/4}
=4\sqrt P.
\]
Since \(0<P\le 16\), we have \(\sqrt P\le 4\), so
\[
4\sqrt P\ge P.
\]
Hence \(Q\ge P\).

### Case 2: \(P\ge 16\)
From \(2S\ge P\), we get
\[
S\ge \frac P2.
\]
By Cauchy-Schwarz,
\[
S^2=(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2)=4Q,
\]
so
\[
Q\ge \frac{S^2}{4}\ge \frac{P^2}{16}\ge P,
\]
because \(P\ge 16\).

Thus in all cases,
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 12,287 | Correct (7/7) | Correct and complete: AM-GM gives S>=4sqrt(P)>=P when P<=16, and Cauchy-Schwarz with A>=P/2 gives S>=P^2/16>P when P>16. |
| A2 | stop | 8,000 | Correct (7/7) | Rigorous split on S: if S>=8 then Q>=S^2/4>=2S>=P, and if S<=8 then P<=2S<=16 so Q>=4sqrt(P)>=P; both cases are valid and exhaustive. |
| A3 | stop | 4,321 | Correct (7/7) | It correctly shows P<=S^2/4 in all cases (via P<=2S when S>=8 and P<=S^4/256<=S^2/4 when S<=8) and combines this with Q>=S^2/4, a complete proof whose omitted one-line algebraic checks are trivial. |
| A4 | stop | 5,828 | Correct (7/7) | Valid proof: Cauchy-Schwarz gives p<=2S<=4sqrt(Q), so Q>=p^2/16>=p when p>=16, and AM-GM gives Q>=4sqrt(p)>=p when p<=16. |
| A5 | stop | 12,439 | Correct (7/7) | Case S>=8 uses Q>=S^2/4>=2S>=p with S(S-8)>=0 justified, and case S<8 gives p<16 so AM-GM yields Q>=4sqrt(p)>p; complete, with a correct equality case. |
| A6 | stop | 14,229 | Correct (7/7) | Valid alternative proof: with u=x+y, v=z+t, A=u^2+v^2 it correctly shows min{2(u+v), u^2v^2/16} <= A/2 by contradiction (A<32 vs A>32), so xyzt <= A/2 <= x^2+y^2+z^2+t^2, with every step checked. |
| A7 | stop | 3,483 | Correct (7/7) | AM-GM gives Q>=4sqrt(p)>=p when p<=16, and for p>16 the hypothesis with Cauchy-Schwarz gives Q>=(p/2)^2/4=p^2/16>p, so both cases are fully and correctly handled. |
| A8 | stop | 7,868 | Correct (7/7) | Complete and rigorous: AM-GM handles p<=16, and Cauchy-Schwarz with S>=p/2 gives Q>=p^2/16>=p for p>=16, so all cases are covered. |
| A9 | stop | 8,325 | Correct (7/7) | AM-GM and Cauchy-Schwarz are derived correctly from elementary identities (including 4Q-S^2 as a sum of squared differences, verified), and the cases p<=16 and p>16 give a complete proof. |
| A10 | stop | 9,306 | Correct (7/7) | Splitting on S>=8 (Cauchy-Schwarz gives Q>=S^2/4>=2S>=p) and S<8 (then p<16 and AM-GM gives Q>=4sqrt(p)>=p) is a complete, rigorous proof with a correct equality case. |
| A11 | stop | 13,191 | Correct (7/7) | Case P<=16 is handled by AM-GM, and case P>16 forces S>8 so that Q>=S^2/4>2S>=P; this is the reference argument written directly and is complete. |
| A12 | stop | 9,873 | Correct (7/7) | Complete proof: AM-GM gives Q>=4sqrt(P)>=P when P<=16, and Cauchy-Schwarz with S>=P/2 gives Q>=P^2/16>P when P>16; the equality case is also identified correctly. |
| A13 | stop | 13,657 | Correct (7/7) | Correctly establishes both Q>=4sqrt(P) (AM-GM) and Q>=P^2/16 (Cauchy-Schwarz plus hypothesis) and notes that one of these bounds is at least P according to whether P<=16 or P>=16, which is a complete proof. |
| A14 | stop | 10,954 | Correct (7/7) | AM-GM handles P<=16, and for P>=16 the bound S>=P/2 with Cauchy-Schwarz gives Q>=P^2/16>=P, so the proof is complete and rigorous. |
| A15 | stop | 9,975 | Correct (7/7) | A valid alternative: for S>=8, Q>=S^2/4>=2S>=P, and for S<=8, S^2/4-(S/4)^4=S^2(64-S^2)/256>=0 with AM-GM gives Q>=P; all computations check out. |
| A16 | stop | 13,634 | Correct (7/7) | Complete case split: P<=16 handled by AM-GM Q>=4sqrt(P)>=P, and P>16 by Q>=S^2/4>=P^2/16>P using the correctly verified identity 4Q-S^2=sum (x_i-x_j)^2 and S>=P/2. |

<details><summary>A1: Correct (7/7)</summary>

Let  
\[
P=xyzt,\qquad A=x+y+z+t,\qquad S=x^2+y^2+z^2+t^2.
\]
The hypothesis is
\[
P\le 2A.
\]

We prove \(S\ge P\) in two cases.

**Case 1: \(P\le 16\).**  
By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
S=x^2+y^2+z^2+t^2
\ge 4(x^2y^2z^2t^2)^{1/4}
=4\sqrt P.
\]
Since \(P\le 16\), we have \(\sqrt P\le 4\), hence
\[
4\sqrt P\ge P.
\]
Therefore
\[
S\ge 4\sqrt P\ge P.
\]

**Case 2: \(P>16\).**  
From \(P\le 2A\), we get
\[
A\ge \frac P2.
\]
By Cauchy-Schwarz,
\[
A^2=(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2)=4S,
\]
so
\[
S\ge \frac{A^2}{4}.
\]
Thus
\[
S\ge \frac{A^2}{4}\ge \frac{(P/2)^2}{4}
=\frac{P^2}{16}.
\]
Since \(P>16\), we have \(\frac{P^2}{16}>P\), so \(S>P\).

In both cases \(S\ge P\). Hence
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

Let  
\[
S=x+y+z+t,\qquad P=xyzt,\qquad Q=x^2+y^2+z^2+t^2.
\]
We need to prove \(Q\ge P\), given \(2S\ge P\).

By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
Q=x^2+y^2+z^2+t^2\ge 4\sqrt{P}.
\tag{1}
\]
By Cauchy-Schwarz,
\[
S^2=(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2)=4Q,
\]
so
\[
Q\ge \frac{S^2}{4}.
\tag{2}
\]

Now consider two cases.

### Case 1: \(S\ge 8\)
From (2),
\[
Q\ge \frac{S^2}{4}\ge 2S,
\]
because \(S\ge 8\). Using the hypothesis \(2S\ge P\), we get
\[
Q\ge 2S\ge P.
\]

### Case 2: \(S\le 8\)
Then
\[
P\le 2S\le 16.
\]
Let \(r=\sqrt P\). Then \(r\le 4\), and therefore
\[
P=r^2\le 4r=4\sqrt P.
\]
By (1),
\[
Q\ge 4\sqrt P\ge P.
\]

Thus in both cases \(Q\ge P\), i.e.
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

Let  
\[
S=x+y+z+t,\qquad P=xyzt.
\]
By AM-GM,
\[
P=xyzt\le \left(\frac{x+y+z+t}{4}\right)^4=\frac{S^4}{256}.
\]
Also the hypothesis gives
\[
P\le 2S.
\]

We now show that \(P\le S^2/4\). There are two cases.

- If \(S\ge 8\), then
\[
2S\le \frac{S^2}{4},
\]
so
\[
P\le 2S\le \frac{S^2}{4}.
\]

- If \(S\le 8\), then
\[
\frac{S^4}{256}\le \frac{S^2}{4},
\]
so
\[
P\le \frac{S^4}{256}\le \frac{S^2}{4}.
\]

Thus in all cases,
\[
xyzt=P\le \frac{S^2}{4}.
\]

On the other hand, by Cauchy-Schwarz,
\[
(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2),
\]
so
\[
x^2+y^2+z^2+t^2\ge \frac{S^2}{4}.
\]

Therefore,
\[
x^2+y^2+z^2+t^2\ge \frac{S^2}{4}\ge P=xyzt.
\]

Hence
\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}.
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

Let  
\[
Q=x^2+y^2+z^2+t^2,\qquad p=xyzt,\qquad S=x+y+z+t.
\]
We are given \(2S\ge p\).

First, by Cauchy-Schwarz,
\[
S^2=(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2)=4Q,
\]
so
\[
S\le 2\sqrt Q.
\]
Hence
\[
p\le 2S\le 4\sqrt Q. \tag{1}
\]

Now we prove \(Q\ge p\).

### Case 1: \(p\le 16\)
By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
Q=x^2+y^2+z^2+t^2\ge 4(x^2y^2z^2t^2)^{1/4}
=4\sqrt p.
\]
Since \(p\le 16\), we have \(\sqrt p\le 4\), so
\[
4\sqrt p\ge p.
\]
Thus
\[
Q\ge 4\sqrt p\ge p.
\]

### Case 2: \(p\ge 16\)
From (1),
\[
p\le 4\sqrt Q.
\]
Squaring both sides gives
\[
p^2\le 16Q,
\]
so
\[
Q\ge \frac{p^2}{16}.
\]
Since \(p\ge 16\),
\[
\frac{p^2}{16}\ge p.
\]
Therefore
\[
Q\ge p.
\]

In both cases \(Q\ge p\). Since \(Q=x^2+y^2+z^2+t^2\) and \(p=xyzt\), we conclude
\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}.
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

Let  
\[
S=x+y+z+t,\qquad p=xyzt,\qquad Q=x^2+y^2+z^2+t^2.
\]
The hypothesis is \(p\le 2S\).

By Cauchy-Schwarz,
\[
S^2=(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2)=4Q,
\]
so
\[
Q\ge \frac{S^2}{4}.
\]

### Case 1: \(S\ge 8\)
Then
\[
Q\ge \frac{S^2}{4}\ge 2S\ge p.
\]
The middle inequality holds because
\[
\frac{S^2}{4}\ge 2S \iff S(S-8)\ge 0,
\]
which is true for \(S\ge 8\).

### Case 2: \(S<8\)
From \(p\le 2S\) and \(S<8\), we get
\[
p<16.
\]
By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
Q=x^2+y^2+z^2+t^2
\ge 4\sqrt[4]{x^2y^2z^2t^2}
=4\sqrt{p}.
\]
Since \(p<16\), we have \(\sqrt{p}<4\), hence
\[
4\sqrt{p}>p.
\]
Therefore
\[
Q\ge 4\sqrt{p}>p,
\]
so in particular \(Q\ge p\).

Both cases cover all positive reals, so
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

Equality occurs at \(x=y=z=t=2\).

</details>

<details><summary>A6: Correct (7/7)</summary>

Let  
\[
u=x+y,\qquad v=z+t,\qquad A=u^2+v^2.
\]

By AM-GM, for positive \(x,y\),
\[
xy\le \frac{(x+y)^2}{4}=\frac{u^2}{4},
\]
and similarly
\[
zt\le \frac{v^2}{4}.
\]
Multiplying,
\[
xyzt\le \frac{u^2v^2}{16}. \tag{1}
\]
Also the hypothesis gives
\[
xyzt\le 2(x+y+z+t)=2(u+v). \tag{2}
\]

We now show
\[
\min\left\{2(u+v),\frac{u^2v^2}{16}\right\}\le \frac{A}{2}.
\]
Assume, for contradiction, that both inequalities above are strict:
\[
2(u+v)>\frac A2,\qquad \frac{u^2v^2}{16}>\frac A2.
\]
Then
\[
A<4(u+v).
\]
But
\[
(u+v)^2\le 2(u^2+v^2)=2A,
\]
so \(u+v\le \sqrt{2A}\). Hence
\[
A<4\sqrt{2A},
\]
which implies \(A<32\).

On the other hand,
\[
\frac{u^2v^2}{16}>\frac A2
\]
gives
\[
u^2v^2>8A.
\]
Since \(uv\le \frac{A}{2}\), we have
\[
u^2v^2\le \frac{A^2}{4}.
\]
Thus
\[
\frac{A^2}{4}>8A,
\]
so \(A>32\), a contradiction. Therefore
\[
\min\left\{2(u+v),\frac{u^2v^2}{16}\right\}\le \frac A2. \tag{3}
\]

Combining (1), (2), and (3),
\[
xyzt\le \min\left\{2(u+v),\frac{u^2v^2}{16}\right\}\le \frac A2.
\]

Finally, by \((x-y)^2\ge0\),
\[
x^2+y^2\ge \frac{(x+y)^2}{2}=\frac{u^2}{2},
\]
and similarly
\[
z^2+t^2\ge \frac{v^2}{2}.
\]
Therefore
\[
x^2+y^2+z^2+t^2\ge \frac{u^2+v^2}{2}=\frac A2.
\]

Hence
\[
x^2+y^2+z^2+t^2\ge \frac A2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

Let  
\[
p=xyzt>0,\qquad S=x^2+y^2+z^2+t^2.
\]
We want to prove \(S\ge p\) under the assumption
\[
2(x+y+z+t)\ge p.
\]

By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
\frac{x^2+y^2+z^2+t^2}{4}\ge \sqrt{p},
\]
so
\[
S\ge 4\sqrt p. \tag{1}
\]

Now consider two cases.

### Case 1: \(p\le 16\)
Then \(\sqrt p\le 4\), hence
\[
4\sqrt p\ge p.
\]
Using (1),
\[
S\ge 4\sqrt p\ge p.
\]

### Case 2: \(p>16\)
From \(2(x+y+z+t)\ge p\), we get
\[
x+y+z+t\ge \frac p2.
\]
By Cauchy-Schwarz,
\[
(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2)=4S.
\]
Therefore
\[
S\ge \frac{(x+y+z+t)^2}{4}\ge \frac{(p/2)^2}{4}
=\frac{p^2}{16}.
\]
Since \(p>16\), we have
\[
\frac{p^2}{16}>p,
\]
so \(S>p\). In particular \(S\ge p\).

Thus in all cases,
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

Let  
\[
p=xyzt,\qquad S=x+y+z+t,\qquad Q=x^2+y^2+z^2+t^2.
\]
The hypothesis is \(p\le 2S\).

We split into two cases.

### Case 1: \(p\le 16\)
By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
Q=x^2+y^2+z^2+t^2
\ge 4(x^2y^2z^2t^2)^{1/4}
=4\sqrt p.
\]
Since \(p\le 16\), we have \(\sqrt p\le 4\), so
\[
4\sqrt p\ge p.
\]
Hence
\[
Q\ge p=xyzt.
\]

### Case 2: \(p\ge 16\)
By Cauchy-Schwarz,
\[
(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2)=4Q,
\]
so
\[
Q\ge \frac{S^2}{4}.
\]
From \(p\le 2S\), we get \(S\ge p/2\). Therefore
\[
Q\ge \frac{S^2}{4}\ge \frac{(p/2)^2}{4}=\frac{p^2}{16}.
\]
Since \(p\ge 16\),
\[
\frac{p^2}{16}\ge p.
\]
Thus again \(Q\ge p=xyzt\).

Both cases cover all possible values of \(p>0\), so in all cases
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

Let  
\[
Q=x^2+y^2+z^2+t^2,\qquad S=x+y+z+t,\qquad p=xyzt.
\]
The hypothesis is \(p\le 2S\).

First, by \((a-b)^2\ge0\),
\[
x^2+y^2\ge2xy,\qquad z^2+t^2\ge2zt.
\]
Thus
\[
Q\ge2xy+2zt=2(xy+zt)\ge4\sqrt{xyzt}=4\sqrt p,
\]
using \(xy+zt\ge2\sqrt{xyzt}\).

Also,
\[
4Q-S^2=\sum_{1\le i<j\le4}(x_i-x_j)^2\ge0,
\]
so
\[
Q\ge \frac{S^2}{4}.
\]

Now consider two cases.

### Case 1: \(p\le 16\)
Then \(\sqrt p\le4\), so
\[
Q\ge4\sqrt p\ge p.
\]

### Case 2: \(p>16\)
From \(p\le2S\), we get \(S\ge p/2\). Hence
\[
Q\ge \frac{S^2}{4}\ge \frac{(p/2)^2}{4}=\frac{p^2}{16}>p.
\]

Therefore in all cases,
\[
Q\ge p,
\]
i.e.
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

Let  
\[
Q=x^2+y^2+z^2+t^2,\qquad S=x+y+z+t,\qquad p=xyzt.
\]
The hypothesis is \(p\le 2S\).

We prove \(Q\ge p\) by considering two cases.

**Case 1: \(S\ge 8\).**  
By Cauchy-Schwarz,
\[
S^2=(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2)=4Q.
\]
Hence
\[
Q\ge \frac{S^2}{4}\ge 2S,
\]
because \(S\ge 8\). Since \(p\le 2S\), we get
\[
Q\ge 2S\ge p.
\]

**Case 2: \(S<8\).**  
Then from \(p\le 2S\),
\[
p<16.
\]
By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
Q=x^2+y^2+z^2+t^2
\ge 4(x^2y^2z^2t^2)^{1/4}
=4\sqrt{xyzt}
=4\sqrt p.
\]
Since \(p<16\), we have \(\sqrt p<4\), so
\[
4\sqrt p\ge p.
\]
Therefore
\[
Q\ge 4\sqrt p\ge p.
\]

In both cases, \(Q\ge p\). Thus
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

Equality is attained at \(x=y=z=t=2\).

</details>

<details><summary>A11: Correct (7/7)</summary>

Let  
\[
Q=x^2+y^2+z^2+t^2,\qquad P=xyzt,\qquad S=x+y+z+t.
\]
We must show \(Q\ge P\).

First, by AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
Q=x^2+y^2+z^2+t^2\ge 4\sqrt{P}.
\]
Also, by Cauchy-Schwarz,
\[
S^2=(x+y+z+t)^2\le 4Q,
\]
so
\[
Q\ge \frac{S^2}{4}.
\]

Now consider two cases.

**Case 1: \(P\le 16\).**  
Then \(\sqrt P\le 4\), hence
\[
4\sqrt P\ge P.
\]
Therefore
\[
Q\ge 4\sqrt P\ge P.
\]

**Case 2: \(P>16\).**  
From the hypothesis
\[
2S\ge P>16,
\]
so \(S>8\). Hence
\[
\frac{S^2}{4}>2S\ge P.
\]
Using \(Q\ge S^2/4\), we get
\[
Q>2S\ge P,
\]
so again \(Q\ge P\).

Both cases cover all possibilities, so
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

Let  
\[
Q=x^2+y^2+z^2+t^2,\qquad P=xyzt,\qquad S=x+y+z+t.
\]
The hypothesis is \(P\le 2S\).

By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
\frac{Q}{4}\ge \sqrt[4]{x^2y^2z^2t^2}=\sqrt P,
\]
so
\[
Q\ge 4\sqrt P. \tag{1}
\]

Now split into two cases.

### Case 1: \(P\le 16\)
Then \(\sqrt P\le 4\), so
\[
4\sqrt P\ge P.
\]
Using (1),
\[
Q\ge 4\sqrt P\ge P.
\]

### Case 2: \(P>16\)
From \(P\le 2S\), we get
\[
S\ge \frac P2.
\]
By Cauchy-Schwarz,
\[
S^2=(x+y+z+t)^2\le 4Q,
\]
so
\[
Q\ge \frac{S^2}{4}\ge \frac{P^2}{16}.
\]
Since \(P>16\),
\[
\frac{P^2}{16}>P.
\]
Hence
\[
Q>P,
\]
so in particular \(Q\ge P\).

Both cases cover all possible \(P>0\), so
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

Equality occurs at \(x=y=z=t=2\), where both sides equal \(16\).

</details>

<details><summary>A13: Correct (7/7)</summary>

Let  
\[
P=xyzt,\qquad Q=x^2+y^2+z^2+t^2,\qquad S=x+y+z+t.
\]
We prove \(Q\ge P\).

By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
\frac{Q}{4}\ge (x^2y^2z^2t^2)^{1/4}=\sqrt P,
\]
so
\[
Q\ge 4\sqrt P. \tag{1}
\]

By Cauchy-Schwarz,
\[
S^2=(x+y+z+t)^2\le 4Q,
\]
hence
\[
Q\ge \frac{S^2}{4}.
\]
The hypothesis gives \(2S\ge P\), so \(S\ge P/2\). Therefore
\[
Q\ge \frac{S^2}{4}\ge \frac{(P/2)^2}{4}=\frac{P^2}{16}. \tag{2}
\]

Now \(P>0\), so either \(P\le 16\) or \(P\ge 16\).  
If \(P\le 16\), then \(\sqrt P\le 4\), hence \(4\sqrt P\ge P\).  
If \(P\ge 16\), then \(P^2/16\ge P\).

Thus at least one of the two quantities \(4\sqrt P\) or \(P^2/16\) is \(\ge P\). Since \(Q\) is at least both, by (1) and (2),
\[
Q\ge P.
\]
Therefore
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

Let  
\[
P=xyzt,\qquad Q=x^2+y^2+z^2+t^2,\qquad S=x+y+z+t.
\]
The hypothesis is
\[
P\le 2S.
\]

We prove \(Q\ge P\).

### Case 1: \(P\le 16\)
By AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
Q=x^2+y^2+z^2+t^2
\ge 4(x^2y^2z^2t^2)^{1/4}
=4\sqrt P.
\]
Since \(P\le 16\), we have \(\sqrt P\le 4\), hence
\[
4\sqrt P\ge P.
\]
Therefore
\[
Q\ge 4\sqrt P\ge P.
\]

### Case 2: \(P\ge 16\)
From \(P\le 2S\), we get
\[
S\ge \frac P2.
\]
By Cauchy-Schwarz,
\[
S^2=(x+y+z+t)^2\le 4(x^2+y^2+z^2+t^2)=4Q.
\]
Thus
\[
Q\ge \frac{S^2}{4}\ge \frac{P^2}{16}.
\]
Since \(P\ge 16\),
\[
\frac{P^2}{16}\ge P.
\]
Hence
\[
Q\ge P.
\]

Both cases cover all positive \(P>0\), so in all cases
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

Let  
\[
S=x+y+z+t,\qquad P=xyzt.
\]
The hypothesis is \(2S\ge P\).

By Cauchy-Schwarz,
\[
x^2+y^2+z^2+t^2 \ge \frac{(x+y+z+t)^2}{4}=\frac{S^2}{4}.
\]
By AM-GM,
\[
\frac S4=\frac{x+y+z+t}{4}\ge (xyzt)^{1/4}=P^{1/4},
\]
so
\[
P\le \left(\frac S4\right)^4.
\]

Now consider two cases.

### Case 1: \(S\ge 8\)
Then
\[
\frac{S^2}{4}-2S=\frac{S(S-8)}4\ge 0,
\]
so
\[
\frac{S^2}{4}\ge 2S.
\]
Using the hypothesis \(P\le 2S\), we get
\[
x^2+y^2+z^2+t^2\ge \frac{S^2}{4}\ge 2S\ge P.
\]

### Case 2: \(0<S\le 8\)
Since \(S\le 8\),
\[
\frac{S^2}{4}-\left(\frac S4\right)^4
=\frac{S^2(64-S^2)}{256}\ge 0,
\]
hence
\[
\frac{S^2}{4}\ge \left(\frac S4\right)^4\ge P.
\]
Therefore
\[
x^2+y^2+z^2+t^2\ge P=xyzt.
\]

Combining both cases, for all positive \(x,y,z,t\) satisfying
\[
2(x+y+z+t)\ge xyzt,
\]
we have
\[
\boxed{x^2+y^2+z^2+t^2\ge xyzt}.
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

Let  
\[
P=xyzt,\qquad S=x+y+z+t,\qquad Q=x^2+y^2+z^2+t^2.
\]
We prove \(Q\ge P\).

First, by AM-GM applied to \(x^2,y^2,z^2,t^2\),
\[
Q\ge 4(x^2y^2z^2t^2)^{1/4}=4\sqrt P.
\]

### Case 1: \(P\le 16\)
Then \(\sqrt P\le 4\), so
\[
4\sqrt P\ge P.
\]
Hence
\[
Q\ge 4\sqrt P\ge P.
\]

### Case 2: \(P>16\)
From the hypothesis,
\[
2S\ge P \implies S\ge \frac P2.
\]
Also,
\[
4Q-S^2=\sum_{1\le i<j\le 4}(x_i-x_j)^2\ge 0,
\]
where \(x_1=x,x_2=y,x_3=z,x_4=t\). Therefore
\[
Q\ge \frac{S^2}{4}.
\]
Using \(S\ge P/2\),
\[
Q\ge \frac{S^2}{4}\ge \frac{P^2}{16}.
\]
Since \(P>16\),
\[
\frac{P^2}{16}>P.
\]
Thus \(Q>P\).

In both cases \(Q\ge P\), so
\[
x^2+y^2+z^2+t^2\ge xyzt.
\]

Equality occurs at \(x=y=z=t=2\).

</details>
