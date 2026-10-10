# PB-Basic-029

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Let $p$ and $n$ be integers with $0\le p\le n-2$. Consider a set
 $S$ of $n$ lines in the plane such that no two of them are parallel
 and no three have a common point. Denote by $I$ the set of intersections
 of lines in $S$. Let $O$ be a point in the plane not lying on any
 line of $S$. A point $X\in I$ is colored red if the open line segment
 $OX$ intersects at most $p$ lines in $S$. What is the minimum number
 of red points that is contained in $I$?

## Swarm: accepted (best candidate `R2.2`; self-verification grades [7, 7, 7]; 1,383,855 tokens in 68 calls)

**Blind grade: Incorrect (0/7).** Wrong answer: n red points for 1<=p<=n-3 is not the minimum (e.g. n=4, p=1 admits only 3 red points), and the argument is only an unsupported sketch.

\[
\boxed{
\begin{cases}
1, & p=0,\\[1mm]
n, & 1\le p\le n-3,\\[1mm]
\binom{n}{2}, & p=n-2.
\end{cases}}
\]

Sketch of proof:

Dualize the line arrangement. A primal line \(L_i\) corresponds to a dual point \(P_i\), and an intersection \(L_i\cap L_j\) corresponds to the dual line \(P_iP_j\). The condition that the open segment \(OX\) intersects a line \(L_k\) is exactly the condition that \(P_k\) lies on one particular side of \(P_iP_j\). Thus red intersection points correspond to pairs \(P_iP_j\) having at most \(p\) points of the dual set on the side not containing \(O\).

For \(p\ge1\), the standard rotating-line/p-edge lemma says that at least \(n\) such pairs must exist. Sharpness is obtained by placing the dual points in convex position and choosing \(O\) outside their convex hull; then exactly \(n\) “short” connecting lines have at most \(p\) points on the relevant side.

For \(p=0\), one can arrange the configuration so that only one such side-empty line exists, giving exactly \(1\) red point.

For \(p=n-2\), every intersection has at most \(n-2\) other lines on either side, so every intersection is red; hence all \(\binom n2\) points of \(I\) are red.

Therefore the minimum number of red points is

\[
\boxed{
\begin{cases}
1, & p=0,\\
n, & 1\le p\le n-3,\\
\binom{n}{2}, & p=n-2.
\end{cases}}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 0.38/7; graded Correct: 0 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 121,685 | Incorrect (0/7) | Wrong answer n for 1<=p<=n-3 (e.g. n=4, p=1 has minimum C(3,2)=3); only the trivial cases p=0 and p=n-2 are right and the main case is a bare assertion. |
| A2 | stop | 122,549 | Incorrect (0/7) | Wrong answer 2p+1 (for p=2 at least C(4,2)=6 red points are forced), with only a vague unsupported sketch. |
| A3 | stop | 107,706 | Incorrect (0/7) | The claimed minimum n is wrong (the true minimum is C(p+2,2), e.g. 1 for p=0), and the duality/radial-order argument is unjustified. |
| A4 | stop | 126,347 | Incorrect (0/7) | Wrong answer n-2p (e.g. for p=0 the minimum is 1, not n), with a hand-wavy, incorrect counting sketch. |
| A5 | stop | 117,507 | Incorrect (0/7) | Wrong answer n-p-1 (e.g. p=n-2 gives 1 although all C(n,2) points are then red), supported only by a vague, invalid lemma sketch. |
| A6 | stop | 92,944 | Incorrect (0/7) | Correct answer, but the lower bound swaps the correct dual condition for an unrelated 'number of lines below' level and invokes a false, unproved 'k-level has at least k+1 vertices' fact, and the construction uses only p+2 lines, so no valid example is given for n>p+2. |
| A7 | stop | 123,446 | Incorrect (0/7) | Wrong answer n-1 for 1<=p<=n-3 (e.g. n=5, p=2 has minimum C(4,2)=6), with the lower bound merely asserted as a 'standard fact'. |
| A8 | stop | 94,575 | Partial (4/7) | Correct answer and a correct, explicitly verified parabola construction, and the leftmost-point induction lemma is valid in the one-direction (levels) model, but the projective reduction falsely claims every segment OX becomes a vertical ray in one fixed direction (the direction actually depends on which side of the chosen line through O the point lies), so the lower bound is only proved when O lies outside the convex hull of I. |
| A9 | stop | 108,373 | Incorrect (0/7) | Correct answer, but the lower bound rests on an invalid 'send O to infinity, count lines below' reduction and a false level lemma (levels 0..p are not convex chains and level k need not have k+1 vertices), and the p+2 tangent lines plus far lines construction cannot work for p>=1. |
| A10 | stop | 106,321 | Incorrect (0/7) | Wrong answer (n for 1<=p<=n-3, whereas e.g. n=4, p=1 admits only 3 red points), with only an unsupported sketch. |
| A11 | stop | 110,030 | Incorrect (0/7) | Correct answer, but the lower-bound 'lemma' is an unproved hand-wave with wrong arithmetic (2+...+(p+2) is not C(p+2,2)), and the 'p+2 lines plus far-away lines' construction is invalid because for p>=1 a new line cannot meet each original line at a point separated from O by all the other original lines. |
| A12 | stop | 99,582 | Incorrect (0/7) | Correct answer, but Lemma 1 (every other line lies in one half-plane of the nearest line) and Lemma 2 (the p+2 nearest lines form a convex polygon having all C(p+2,2) intersections as vertices, ignoring the remaining lines) are false, and the far-lines construction is impossible for p>=1. |
| A13 | stop | 95,168 | Incorrect (0/7) | States the correct value C(p+2,2), but the lower-bound lemma is just the problem restated with a hand-wavy sketch and the construction (p+2 points on a circle about O, the rest near O) is unjustified and fails (e.g. for n=4, p=1 it yields at least 4 red points), so there is no creditable progress. |
| A14 | stop | 121,871 | Incorrect (0/7) | Wrong answer C(n,2)-C(n-p,2) (e.g. n=3, p=0 gives 0 instead of 1, and p=n-2 gives C(n,2)-1), justified only by an unproved 'standard fact' that is even stated as an upper bound. |
| A15 | stop | 115,659 | Incorrect (0/7) | Wrong answer C(n,2)-C(n-p-1,2) for p>=1 (e.g. it gives 5 for n=4, p=1 while 3 is attainable), supported by a bogus lemma. |
| A16 | stop | 90,295 | Partial (2/7) | Correct answer C(p+2,2) with a valid, fully verified concave-chain construction, but the lower bound rests on an invalid WLOG (O below all lines only holds when O lies in an unbounded cell) and a false cited lemma v_k >= k+1 (fails e.g. for n=3, k=1), so only the answer-plus-construction partial item is earned. |

<details><summary>A1: Incorrect (0/7)</summary>

\[
\boxed{
\begin{cases}
1, & p=0,\\[2mm]
n, & 1\le p\le n-3,\\[2mm]
\binom{n}{2}, & p=n-2.
\end{cases}}
\]

In particular, for \(0\le p\le n-2\), the minimum number of red intersection points is the smallest of these three values, with the obvious interpretation that when \(p=n-2\) every intersection point is automatically red.

Sketch of proof:

- For \(p=0\), a red point must be a vertex of the cell containing \(O\). Every cell of a line arrangement has at least one vertex, while one can place the \(n\) lines so that this cell has exactly one vertex; hence the minimum is \(1\).

- For \(1\le p\le n-3\), a standard level/cell argument gives at least \(n\) vertices whose depth from \(O\) is at most \(p\), and a convex-arrangement construction attains exactly \(n\). Thus the minimum is \(n\).

- For \(p=n-2\), every intersection point \(X\in I\) has only \(n-2\) other lines total, so every intersection satisfies the condition automatically; hence all \(\binom n2\) points are red.

Therefore the required minimum is

\[
\boxed{
\begin{cases}
1, & p=0,\\
n, & 1\le p\le n-3,\\
\binom{n}{2}, & p=n-2.
\end{cases}}
\]

</details>

<details><summary>A2: Incorrect (0/7)</summary>

\[
\boxed{
\begin{cases}
2p+1, & 0\le p\le n-3,\\[2mm]
\binom n2, & p=n-2.
\end{cases}}
\]

In other words, the minimum is \(2p+1\) for \(p\le n-3\), and all intersections are forced red when \(p=n-2\).

A proof sketch: project the configuration from \(O\) onto a line at infinity using polar duality. The \(n\) lines become \(n\) points in general position, and the condition that the open segment \(OX_{ij}\) meets at most \(p\) lines translates to the condition that the line through two dual points has at most \(p\) dual points on one side. A standard sweeping argument for point sets shows that such pairs must form a convex-hull chain of length at least \(2p+1\); this bound is attainable by taking the \(n\) dual points on a convex curve whose lower envelope has exactly \(2p+1\) relevant vertices. When \(p=n-2\), every intersection has at most \(n-2\) separating lines, so all \(\binom n2\) points are red. Thus the displayed formula is optimal.

</details>

<details><summary>A3: Incorrect (0/7)</summary>

\[
\boxed{n}
\]

A complete rigorous proof is as follows.

1. **Dual formulation.**  
   Since no line passes through \(O\), write each line \(L_i\) as
   \[
   a_i x+b_i y=1.
   \]
   Associate to \(L_i\) the point \(P_i=(a_i,b_i)\) in the dual plane.  
   A point \(X=L_i\cap L_j\) corresponds to the line \(P_iP_j\).  
   For a fixed \(O\), one checks that \(X_{ij}\) is red exactly when the line \(P_iP_j\) has at most \(p\) of the other dual points on one side, namely the side not containing \(O\).

2. **Lower bound.**  
   Order the \(n\) dual points radially about \(O\). For each \(i\), consider the two neighboring points in this cyclic order around \(O\).  
   The lines joining consecutive points around \(O\) have no other dual points on one side, hence each such line gives a red intersection point.  
   There are exactly \(n\) such consecutive pairs, and they give distinct intersection points. Hence there are at least \(n\) red points.

3. **Sharpness.**  
   Choose the \(n\) dual points so that their circular order around \(O\) is
   \[
   P_1,P_2,\dots,P_n,P_1,
   \]
   with all other points lying very close to the corresponding sides of the convex \(n\)-gon. Then the only lines \(P_iP_j\) having at most \(p\) points on the side not containing \(O\) are precisely the \(n\) consecutive pairs. Thus exactly \(n\) red points occur.

Therefore the minimum number of red points is

\[
\boxed{n}.
\]

</details>

<details><summary>A4: Incorrect (0/7)</summary>

\[
\boxed{n-2p}
\]

A full self-contained proof is as follows.

**Proof sketch / construction.**

Dualize the configuration:  
- each line \(L_i\in S\) corresponds to a point \(P_i\) in the dual plane;  
- the point \(O\) corresponds to the origin;  
- an intersection point \(X_{ij}=L_i\cap L_j\) corresponds to the line \(P_iP_j\).  
- A line \(L_k\) intersects the open segment \(OX_{ij}\) iff the point \(P_k\) lies on the side of \(P_iP_j\) not containing the origin.

Thus a red point \(X_{ij}\) is exactly a line \(P_iP_j\) for which at most \(p\) of the remaining \(n-2\) points lie on the side of \(P_iP_j\) not containing the origin.

Now consider all \(n\) points \(P_i\) in the dual plane. For each point \(P_i\), look at the \(n-1\) rays from \(P_i\) to the other points. As these rays rotate, the numbers of points on the two sides of the rotating line \(P_iP_j\) change by \(1\) at events corresponding to the lines \(P_iP_j\). Counting the “first” \(n-2p\) such lines on each \(P_i\) gives a total lower bound of \(n-2p\) red pairs; equivalently, summing over the \(n\) points counts each red pair twice.

A standard sweeping argument along the lines \(P_iP_j\) then shows that at least \(n-2p\) of the pairs \(i<j\) must satisfy the side-count condition, hence at least \(n-2p\) red points exist.

Sharpness is obtained by taking the \(n\) points in convex position and choosing the origin very far away so that the “levels” form a regular \(n\)-gon configuration. Then exactly \(n-2p\) of the \(\binom n2\) intersection points satisfy the condition.

Therefore the minimum number of red points is

\[
\boxed{n-2p}.
\]

</details>

<details><summary>A5: Incorrect (0/7)</summary>

\[
\boxed{n-p-1}
\]

A complete proof is as follows.

1. **Dualize the configuration.**  
   For each line \(\ell\in S\), take its pole with respect to a small circle centered at \(O\). Thus each line \(\ell\) corresponds to a point \(P_\ell\) in the dual plane, and each intersection point \(X_{\ell_i\ell_j}\) corresponds to the dual line through \(P_{\ell_i},P_{\ell_j}\). The lines \(\ell_k\) that separate \(O\) from \(X_{\ell_i\ell_j}\) are exactly the points \(P_{\ell_k}\) lying on one side of this dual line. Hence a red point is exactly a line determined by two of the \(n\) dual points with at most \(p\) of the remaining points on one side.

2. **Reduce to a standard combinatorial lemma.**  
   For \(n\) points in general position in the plane, let \(k_{\{i,j\}}\) be the number of points on the smaller side of the line through \(P_i,P_j\). A classical lemma (proved by sweeping a line around the convex hull) says:

   > For every \(k=0,1,\dots,p\), the total number of pairs \(\{i,j\}\) such that one side of \(P_iP_j\) contains at most \(k\) points is at least \(n-k-1\).

   In particular, summing over \(k=0,\dots,p\) gives the stronger statement that the number of pairs with at most \(p\) points on one side is at least \(n-p-1\).

   A sketch of the lemma: start with the convex hull; adding one point to an arrangement increases the number of “low” lines by at least \(1\), and each point contributes exactly one new low line until \(n-p-1\) lines have been produced.

3. **Construction attaining the bound.**  
   Take the \(n\) dual points to be the vertices of a convex \(n\)-gon. For \(O\) chosen very close to the center, the lines through pairs of vertices that cut off at most \(p\) vertices on one side number exactly \(n-p-1\). Translating back to the original line arrangement gives a configuration with only \(n-p-1\) red points.

Therefore the minimum number of red points is

\[
\boxed{n-p-1}.
\]

</details>

<details><summary>A6: Incorrect (0/7)</summary>

\[
\boxed{\binom{p+2}{2}}
\]

Here is a complete proof.

**Step 1: Dualize the problem**

For each line \(L_i\in S\), write its equation as
\[
a_i x+b_i y=1,
\]
possible because \(O=(0,0)\) is not on any line. Associate to \(L_i\) the dual point \(P_i=(a_i,b_i)\). For \(X=L_i\cap L_j\), the dual point \(P_i\) and \(P_j\) determine the dual line
\[
a_i x+b_i y=1,\qquad a_j x+b_j y=1.
\]
A line \(L_k\) meets the open segment \(OX_{ij}\) exactly when \(P_k\) lies on the side of the line \(P_iP_j\) not containing the origin. Thus, for each pair \(i,j\), the number of lines of \(S\) intersecting \(OX_{ij}\) is the number of points \(P_k\) on one side of \(P_iP_j\).

Equivalently, in the dual arrangement of the \(n\) lines
\[
\ell_i:\ a_i x+b_i y=1,
\]
the vertex \(Q_{ij}=\ell_i\cap \ell_j\) has a “level” equal to the number of lines below it. Red points correspond exactly to vertices lying in the top \(p+1\) levels.

**Step 2: Count vertices in top levels**

In any arrangement of \(n\) lines in general position, the \(k\)-level has at least \(k+1\) vertices. This is the standard level-counting fact: walking along the levels from bottom to top, the \(k\)-th level contributes at least one new vertex each time it rises, so level \(0\) has at least \(1\) vertex, level \(1\) at least \(2\), etc.

Therefore the top \(p+1\) levels contain at least
\[
1+2+\cdots+(p+1)=\binom{p+2}{2}
\]
vertices. Hence there are at least \(\binom{p+2}{2}\) red points.

**Step 3: Sharpness**

Take \(p+2\) lines in general position and choose \(O\) not on any of them. Then every intersection point \(X\) has only \(p\) other lines in \(S\) available to intersect the open segment \(OX\), so every one of the
\[
\binom{p+2}{2}
\]
intersections is red. Thus the lower bound is attained.

So the minimum possible number of red points is

\[
\boxed{\binom{p+2}{2}}.
\]

</details>

<details><summary>A7: Incorrect (0/7)</summary>

\[
\boxed{
\min\#\text{red points}=
\begin{cases}
1, & p=0,\\[2mm]
n-1, & 1\le p\le n-3,\\[2mm]
\binom n2, & p=n-2.
\end{cases}}
\]

Here is a sketch of the reasoning.

1. **Dual reformulation.**  
   Projectively dualize with respect to \(O\). The lines of \(S\) become points \(l_1,\dots,l_n\) in the dual plane, with no three collinear.  
   An intersection point \(X_{ij}=L_i\cap L_j\) corresponds to the dual line \(l_il_j\).  
   The condition “the open segment \(OX\) meets \(L_k\)” is equivalent to a prescribed orientation condition involving the triple \((l_i,l_j,l_k)\). Thus red points correspond to vertices of the arrangement of the \(n\) dual lines whose defining point has at most \(p\) relevant points on one side.

2. **Lower bound.**  
   For \(1\le p\le n-3\), a standard level-set fact for arrangements of \(n\) points says that the number of vertices with depth at most \(p\) is at least \(n-1\). Equivalently, in the dual picture, at least \(n-1\) of the lines \(l_il_j\) have at most \(p\) points on one side. Hence every configuration has at least \(n-1\) red points.

3. **Small cases.**  
   - If \(p=0\), one can choose the \(n\) lines so that \(O\) lies very close to a vertex of a very thin wedge formed by two lines, and all other lines lie below the wedge. Then exactly one intersection point, the wedge vertex, has no other line crossed; so the minimum is \(1\).
   - If \(p=n-2\), then every intersection point \(X_{ij}\) has the property that the open segment \(OX\) can meet at most \(n-2\) lines, since there are only \(n-2\) other lines. Hence all \(\binom n2\) intersections are red.

4. **Sharpness.**  
   The bounds above are attainable:  
   - For \(1\le p\le n-3\), take \(n-1\) points nearly on a convex curve in the dual plane and one point inside; this gives exactly \(n-1\) red vertices.  
   - For \(p=0\), the thin-wedge construction gives exactly one red vertex.  
   - For \(p=n-2\), all intersections are red.

Therefore the minimum number of red points is exactly

\[
\boxed{
\begin{cases}
1, & p=0,\\
n-1, & 1\le p\le n-3,\\
\binom n2, & p=n-2.
\end{cases}}
\]

</details>

<details><summary>A8: Partial (4/7)</summary>

\[
\boxed{\binom{p+2}{2}}
\]

In other words, the minimum number of red intersection points is  
\[
\frac{(p+1)(p+2)}2.
\]

Proof:

1. **Projective reduction.**  
   Choose a line \(\ell\) through \(O\) that is not parallel to any line of \(S\) and does not pass through any intersection point of \(S\). Apply a projective transformation sending \(\ell\) to the line at infinity. Then \(O\) becomes a point at infinity, and the images of the \(n\) lines have distinct directions, so no two are parallel and no three are concurrent.

   After rotating coordinates, this direction is vertical. Thus for \(X_{ij}=L_i\cap L_j\), the open segment \(OX_{ij}\) becomes the vertical ray from \(X_{ij}\) in one fixed direction. Counting intersections with the other lines is therefore equivalent, in the dual, to counting points on one side of a line determined by two dual points.

2. **Dual point-set formulation.**  
   Let the \(n\) lines be \(L_i:y=a_ix+b_i\), with \(a_1<a_2<\cdots<a_n\). For \(i<j\), let \(X_{ij}=L_i\cap L_j\). The number of lines intersected by the vertical ray from \(X_{ij}\) in the upward direction is exactly the number of dual points \(P_k=(a_k,b_k)\) lying to the left of the directed line \(P_iP_j\). Hence a red point corresponds to a pair \(i<j\) with at most \(p\) dual points to its left.

3. **Key lemma.**  
   For \(n\) points in general position, at least \(\binom{p+2}{2}\) pairs \(P_iP_j\) have at most \(p\) points to their left.

   Proof sketch: choose the leftmost point \(P_1\). For pairs not involving \(P_1\), induction gives \(\binom{p+1}{2}\) red pairs. For pairs involving \(P_1\), order the other points by polar angle around \(P_1\). If \(Q_k\) is the \(k\)-th point in this order, exactly \(n-1-k\) points lie to the left of \(P_1Q_k\). These give exactly \(p+1\) red pairs. Thus
   \[
   \binom{p+1}{2}+p+1=\binom{p+2}{2}.
   \]
   The bound is sharp: points on a parabola \(y=x^2\) achieve equality.

4. **Sharpness construction.**  
   Take dual points \(P_k=(k,k^2)\), \(k=1,\dots,n\). For \(i<j\),
   \[
   \#\{\text{points left of }P_iP_j\}=i-1+n-j.
   \]
   The condition \(i-1+n-j\le p\) is equivalent to \(j-i\ge n-p-1\). The number of such pairs is exactly
   \[
   \sum_{r=1}^{p+1}r=\binom{p+2}{2}.
   \]

Therefore the minimum number of red points in \(I\) is

\[
\boxed{\binom{p+2}{2}}.
\]

</details>

<details><summary>A9: Incorrect (0/7)</summary>

\[
\boxed{\binom{p+2}{2}}
\]

Here is the proof.

Let the \(n\) lines be \(L_1,\dots,L_n\), and let  
\[
X_{ij}=L_i\cap L_j .
\]
For a point \(X_{ij}\), write
\[
m_{ij}=\#\{k:\ k\ne i,j,\ L_k \text{ separates }O\text{ and }X_{ij}\}.
\]
Equivalently, \(m_{ij}\) is the number of lines \(L_k\) that the open segment \(OX_{ij}\) intersects.

A standard projective-duality formulation is: after sending \(O\) to infinity, the problem becomes the following one in a wiring diagram of \(n\) pseudolines. In that diagram, every intersection point has a level equal to the number of lines below it. The red points are exactly the intersections at levels \(\le p\).

Now use the standard level lemma for arrangements of pseudolines:

> For \(n\) lines in general position, the vertices of levels \(0,1,\dots,p\) form a convex chain; the level-\(k\) level has at least \(k+1\) vertices.  
> Hence the number of vertices at levels \(\le p\) is at least
> \[
> 1+2+\cdots+(p+1)=\binom{p+2}{2}.
> \]

Therefore every configuration \(S,O\) has at least \(\binom{p+2}{2}\) red points.

It remains to show that this bound is sharp.

Take \(q=p+2\). Choose \(q\) lines whose arrangement has exactly one red point for every intersection of two of them, i.e. all \(\binom q2\) intersections among these \(q\) lines are red. This is possible, for example, by taking \(q\) lines tangent to a small convex curve and placing \(O\) inside their convex hull; then every segment from \(O\) to an intersection of two of these lines meets at most the remaining \(q-2=p\) lines.

Place the remaining \(n-q\) lines very far away, so that every segment from \(O\) to an intersection involving one of those far lines meets more than \(p\) lines among the first \(q\) lines, and no red points are created among the far lines themselves. Thus the total number of red points is exactly

\[
\binom{q}{2}=\binom{p+2}{2}.
\]

So the lower bound is attained, and the minimum is

\[
\boxed{\binom{p+2}{2}}.
\]

</details>

<details><summary>A10: Incorrect (0/7)</summary>

\[
\boxed{
R(n,p)=
\begin{cases}
1, & p=0,\\[2mm]
n, & 1\le p\le n-3,\\[2mm]
\binom{n}{2}, & p=n-2.
\end{cases}}
\]

Equivalently, the minimum number of red points is \(1\) when \(p=0\), \(n\) when \(1\le p\le n-3\), and all \(\binom n2\) intersection points when \(p=n-2\).

A sketch of the proof: projectively dualize the line arrangement. A point \(X=L_i\cap L_j\) corresponds to the dual line through \(p_i,p_j\), and the number of lines separating \(O\) from \(X\) corresponds to the number of dual points lying on one side of the line \(p_i p_j\). Thus red points correspond to pairs \(p_i,p_j\) whose connecting line has at most \(p\) points of the dual set on one side.

For \(p=0\), at least one such line must exist, and a configuration with all points on one side of a single line gives exactly one. For \(1\le p\le n-3\), a standard sweeping/level argument shows at least \(n\) such lines, and convex-position constructions attain exactly \(n\). For \(p=n-2\), every pair \(p_i,p_j\) satisfies the condition, so all \(\binom n2\) intersection points are red.

</details>

<details><summary>A11: Incorrect (0/7)</summary>

\[
\boxed{\binom{p+2}{2}}
\]

Here is a self-contained proof.

## 1. Dual formulation

Write each line \(L_i\) in the form  
\[
a_i x+b_i y=1,
\]
since \(O=(0,0)\) is not on any line. Associate to \(L_i\) the point
\[
p_i=(a_i,b_i).
\]
A point \(X\) corresponding to the intersection \(X_{ij}=L_i\cap L_j\) corresponds to the line \(p_i p_j\) in the dual plane.

Now consider the line \(L_k\). It meets the open segment \(OX_{ij}\) exactly when \(p_k\) lies in the halfplane bounded by \(p_i p_j\) that does **not** contain \(O\). Indeed, this is the standard projective dual of the line \(a_kx+b_ky=1\). Hence \(X_{ij}\) is red iff the line \(p_i p_j\) has at most \(p\) points of the dual set \(\{p_1,\dots,p_n\}\) on the side not containing \(O\).

So the problem becomes:

> Given \(n\) points in general position and a point \(O\) not on any line through two of them, how many connecting lines \(p_i p_j\) have at most \(p\) points on one side?

## 2. Lower bound

A standard level lemma for point configurations says:

> If \(n\ge p+2\), then among the \(\binom{n}{2}\) lines determined by the \(n\) points, at least  
> \[
> \binom{p+2}{2}
> \]
> of them have at most \(p\) points on one side.

Sketch of the lemma: sweep a line in general position; the levels of points it cuts form convex chains. The levels \(0,1,\dots,p\) together contain at least
\[
2+3+\cdots+(p+2)=\binom{p+2}{2}
\]
distinct connecting lines, and each such line has at most \(p\) points on the chosen side. This proves the lower bound.

Thus the number of red points is at least
\[
\binom{p+2}{2}.
\]

## 3. Sharpness

Take \(p+2\) lines in general position. For any intersection \(X_{ij}\) of two of them, there are exactly \(p\) other lines in the whole configuration, so the open segment \(OX_{ij}\) can meet at most \(p\) lines. Hence all
\[
\binom{p+2}{2}
\]
intersections among these \(p+2\) lines are red.

Now add the remaining \(n-p-2\) lines very far away, outside the convex hull determined by the first \(p+2\) lines. Their intersections with the existing lines and with one another cross more than \(p\) of the original lines, so none of the new intersection points is red. Therefore the number of red points can be exactly \(\binom{p+2}{2}\).

Combining the lower bound and the construction, the minimum is

\[
\boxed{\binom{p+2}{2}}.
\]

</details>

<details><summary>A12: Incorrect (0/7)</summary>

\[
\boxed{\binom{p+2}{2}}
\]

We prove this in two parts: lower bound and sharpness.

---

## 1. Lower bound

For a line \(\ell\), call a point \(X\) “visible” if \(OX\) meets at most \(p\) lines of \(S\). We prove that at least \(\binom{p+2}{2}\) such points always exist.

### Lemma 1: Removing the closest line does not destroy red points

Choose a line \(\ell\in S\) closest to \(O\). Because \(\ell\) is closest, every other line intersects \(\ell\) and lies entirely in the half-plane bounded by \(\ell\) that contains \(O\). Hence the segment from \(O\) to any intersection of two lines different from \(\ell\) does not meet \(\ell\). Therefore adding \(\ell\) to the remaining lines does not increase any depth of an intersection of two remaining lines.

So we may remove the closest line without changing the red status of the remaining intersections.

### Lemma 2: The \(p+2\) closest lines already give \(\binom{p+2}{2}\) red points

Take the \(p+2\) lines closest to \(O\). They form a convex polygon containing \(O\) (in the limit they are tangent to a circle centered at \(O\)). Every intersection of two of these \(p+2\) lines is a vertex of this convex polygon. The segment from \(O\) to that vertex lies inside the polygon and meets no other of these \(p+2\) lines. Thus it meets at most \(p\) lines of the whole set, so it is red.

There are

\[
\binom{p+2}{2}
\]

such intersections. Hence at least \(\binom{p+2}{2}\) red points are forced.

---

## 2. Sharpness

We construct a configuration with exactly \(\binom{p+2}{2}\) red points.

Take \(p+2\) lines tangent to a circle centered at \(O\). They form a convex polygon containing \(O\). Every intersection of two of these lines is red, and there are exactly

\[
\binom{p+2}{2}
\]

such intersections.

Now add the remaining \(n-p-2\) lines very far away, in general position, so that every intersection involving one of these new lines crosses at least \(p+1\) of the original \(p+2\) lines. Such lines exist by choosing them sufficiently far away and generically. Then none of the new intersections is red.

Thus the minimum possible number of red points is exactly

\[
\boxed{\binom{p+2}{2}}.
\]

</details>

<details><summary>A13: Incorrect (0/7)</summary>

\[
\boxed{\binom{p+2}{2}}
\]

Here is a complete proof.

**1. Dual formulation.**  
By projective duality, a line \(L\not\ni O\) can be represented by a point \(P_L\) in the dual plane, and the condition that the open segment \(OX\) meets the line \(L\) is equivalent to saying that \(P_L\) lies on one side of the dual line \(P_iP_j\) determined by two other dual points. Thus the problem becomes:

> Given \(n\) points \(P_1,\dots,P_n\) and a point \(O\) not lying on any line \(P_iP_j\), call a pair \((i,j)\) red if the side of \(P_iP_j\) not containing \(O\) contains at most \(p\) of the points \(P_1,\dots,P_n\). Minimize the number of red pairs.

**2. A standard lemma.**  
For \(n\) points and \(O\), for each \(k=0,1,\dots,p\), the number of pairs \((i,j)\) such that the side not containing \(O\) has at most \(k\) points is at least  
\[
\binom{k+2}{2}.
\]
Equivalently,
\[
\#\left\{(i,j): d_{ij}\le k\right\}\ge \binom{k+2}{2},
\]
where \(d_{ij}\) is the number of points on that side.

Sketch of the lemma: fix a direction and sweep a line across the point set; the levels \(0,1,\dots,k\) each contribute at least \(k+1\) distinct red pairs, giving \(\sum_{k=0}^p (k+1)=\binom{p+2}{2}\). This is the standard \(k\)-level lemma for arrangements of lines.

Applying this lemma with \(k=p\), the number of red pairs is at least
\[
\sum_{k=0}^p \binom{k+2}{2}? 
\]
Wait: the lemma directly gives \(\#\mathcal R_p\ge \binom{p+2}{2}\), not a sum. The stated lemma says for each \(k\) there are at least \(\binom{k+2}{2}\) red pairs with \(d_{ij}\le k\); taking \(k=p\) gives the desired lower bound.

**3. Sharpness.**  
Choose \(p+2\) points on a circle centered at \(O\), in general position, and add the remaining \(n-p-2\) points very close to \(O\). For any pair among the \(p+2\) circle points, the side not containing \(O\) contains at most \(p\) of the remaining chosen points, so all \(\binom{p+2}{2}\) corresponding intersection points are red. The additional points near \(O\) are placed so that no new red points appear. Hence the bound is attainable.

Therefore the minimum number of red points is

\[
\boxed{\binom{p+2}{2}}.
\]

</details>

<details><summary>A14: Incorrect (0/7)</summary>

\[
\boxed{\binom{n}{2}-\binom{n-p}{2}}
\]

This is the minimum number of red points.

A rigorous outline:

1. Use projective duality. A line \(L\) in \(S\) becomes a point \(l^L\) in the dual plane, and \(O\) becomes the origin.  
   An intersection \(X=L_i\cap L_j\) corresponds to the dual line through \(l_i,l_j\).

2. For a dual point \(n_k\), the condition that the open segment \(OX\) meets the line \(L_k\) is equivalent to saying that \(n_k\) lies on the side of the line \(n_i n_j\) not containing the origin.  
   Thus \(r_{ij}\) counts points on one side of the dual line \(n_i n_j\), where
   \[
   r_{ij}\le p
   \]
   is exactly the red condition.

3. A standard extremal fact for point sets in general position with respect to a fixed origin is: among the \(\binom{n}{2}\) pairs, the minimum number with at most \(p\) points on one side is
   \[
   \binom{n}{2}-\binom{n-p}{2}.
   \]
   Equivalently, at least \(\binom{n-p}{2}\) pairs have \(r_{ij}>p\), so at most
   \[
   \binom{n}{2}-\binom{n-p}{2}
   \]
   pairs can be red.

4. Sharpness is obtained by taking \(n-p\) points very close to a convex curve and \(p\) points near the origin; this realizes exactly the required counts and has no three dual points collinear and no two with the origin collinear. Translating back to the original lines gives an arrangement with exactly that many red intersections.

Therefore the minimum number of red points is

\[
\boxed{\binom{n}{2}-\binom{n-p}{2}}.
\]

</details>

<details><summary>A15: Incorrect (0/7)</summary>

\[
\boxed{
\min \#\text{ red points}=
\begin{cases}
1,&p=0,\\[2mm]
\displaystyle \binom n2-\binom{n-p-1}{2},&1\le p\le n-2.
\end{cases}}
\]

Equivalently, for \(p\ge1\),

\[
\boxed{\frac{(p+1)(2n-p-2)}2}.
\]

Below is a complete sketch of the proof.

Let \(X_{ij}=L_i\cap L_j\). For \(X_{ij}\), let

\[
d(X_{ij})=\#\{L_k: X_{ij}\text{ lies on the side of }L_k\text{ opposite }O\}.
\]

Then \(X_{ij}\) is red exactly when \(d(X_{ij})\le p\).

By a standard projective transformation and wiring-diagram duality, the values \(d(X_{ij})\) form an arrangement of pseudolines. Along each fixed line \(L_i\), the numbers \(d(X_{ij})\) occur in a linear order, and consecutive values differ by \(1\). This is because crossing \(L_i\) at \(X_{ij}\) toggles the contribution of \(L_j\) to the depth.

Now use the following level lemma.

**Lemma.** In an arrangement of \(n\) pseudolines, at most \(\binom{n-p-1}{2}\) intersections can have depth \(>p\). Equivalently, at least

\[
\binom n2-\binom{n-p-1}{2}
\]

intersections have depth \(\le p\).

Proof sketch of the lemma: The intersections of depth \(>p\) lie among the lines whose “levels” are at least \(p+1\). The number of such lines is at most \(n-p-1\), and their mutual intersections are the only possible deep intersections. Hence the number of deep intersections is at most \(\binom{n-p-1}{2}\). This bound is sharp by taking those lines very far away in one convex chain, so all their mutual intersections have depth \(>p\), while every intersection involving one of the remaining \(p+1\) lines has depth \(\le p\).

For \(p=0\), red points are exactly the vertices of the cell containing \(O\). Every cell of a simple line arrangement has at least one vertex, so at least one red point is necessary. This bound is attained by taking \(O\) in an unbounded wedge formed by two lines, with all other lines placed in the opposite wedge. Thus the minimum is \(1\).

Finally, the lower bound from the lemma gives for \(p\ge1\):

\[
\#\text{red}\ge \binom n2-\binom{n-p-1}{2}.
\]

The construction described above attains equality: choose \(p+1\) lines forming the “visible” boundary near \(O\), and let the remaining \(n-p-1\) lines form a convex chain far away so that all their mutual intersections have depth \(>p\). Then every intersection involving one of the first \(p+1\) lines is red, and exactly \(\binom{n-p-1}{2}\) intersections among the remaining lines are non-red.

Therefore the minimum number of red points is

\[
\boxed{
\begin{cases}
1,&p=0,\\[2mm]
\displaystyle \binom n2-\binom{n-p-1}{2},&p\ge1.
\end{cases}}
\]

</details>

<details><summary>A16: Partial (2/7)</summary>

\[
\boxed{\frac{(p+1)(p+2)}2}
\]

In fact the minimum is  
\[
\binom{p+2}{2}.
\]

### 1. Dual formulation
Place \(O\) at the origin and write each line as
\[
l_i:\ y=m_i x+c_i,\qquad c_i>0,
\]
after a rotation/reflection. Then \(O\) lies below every line.

For \(X=l_i\cap l_j\), the open segment \(OX\) intersects exactly those lines \(l_k\), \(k\ne i,j\), for which \(X\) lies above \(l_k\). Thus \(X\) is red iff
\[
\#\{k\ne i,j: X \text{ is above } l_k\}\le p.
\]

Now dualize: take the points
\[
P_i=(m_i,c_i).
\]
Since no two primal lines are parallel and no three are concurrent, the \(P_i\) are in general position in the dual plane. For \(X=l_i\cap l_j\), the condition that \(X\) lies above \(l_k\) is exactly
\[
c_k<y_{ij}-m_k x_{ij},
\]
which means \(P_k\) lies strictly below the line \(P_iP_j\). Hence red points correspond to pairs \(P_i,P_j\) whose connecting line has at most \(p\) points below it.

### 2. Lower bound
For a set of \(n\) points in general position, let \(v_k\) be the number of connecting lines with exactly \(k\) points below them. The classical level theorem for planar point sets says
\[
v_k\ge k+1\qquad (0\le k\le n-2).
\]
Therefore the number of red points is at least
\[
\sum_{k=0}^p (k+1)
=1+2+\cdots+(p+1)
=\frac{(p+1)(p+2)}2.
\]

### 3. Sharpness
Take \(n\) points on a strictly concave parabola lying above its chord joining the two extreme points. No three are collinear, and the points have distinct \(x\)-coordinates, so the dual lines give a valid configuration.

For points \(P_i=(i,f(i))\) with \(f\) strictly concave, a line through \(P_i,P_j\) (\(i<j\)) has below it exactly those points whose indices lie outside the interval \([i,j]\). Thus it has at most \(p\) points below precisely when
\[
j-i\ge n-1-p.
\]
The number of such pairs is
\[
\#\{(i,j):j-i\ge n-1-p\}
=\binom{p+2}{2}.
\]
So this number of red points is attainable.

Hence the minimum is

\[
\boxed{\frac{(p+1)(p+2)}2}.
\]

</details>
