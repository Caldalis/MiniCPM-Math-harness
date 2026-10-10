# PB-Basic-013

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Each of 8 boxes contains 6 balls. Each ball has been colored with one of 22 colors. If no two balls in the same box are the same color, prove that there are two colors that occur together in more than one box.

## Swarm: accepted (best candidate `P8`; self-verification grades [7, 7, 7]; 506,641 tokens in 51 calls)

**Blind grade: Correct (7/7).** Correct double counting sum C(r_i,2) = sum |B_j ∩ B_k| <= 28 under the assumption, contradicted by the Cauchy-Schwarz bound 312/11 > 28; the argument is complete and the arithmetic is right.

Let the boxes be \(B_1,\dots,B_8\), and let the colors be \(c_1,\dots,c_{22}\).  
For each color \(c_i\), define

\[
r_i=\#\{j: c_i\in B_j\},
\]

the number of boxes in which color \(c_i\) appears.

Since each box contains \(6\) balls, the total number of color-box incidences is

\[
\sum_{i=1}^{22} r_i = 8\cdot 6=48.
\]

Now consider pairs of boxes. For a fixed color \(c_i\), choosing any two boxes containing \(c_i\) gives a pair of boxes both containing \(c_i\). Hence

\[
\binom{r_i}{2}
\]

counts pairs of boxes sharing color \(c_i\). Therefore

\[
\sum_{i=1}^{22} \binom{r_i}{2}
=
\sum_{1\le j<k\le 8} |B_j\cap B_k|.
\]

The right-hand side counts, over all pairs of boxes, the number of common colors.

Assume for contradiction that no two colors occur together in more than one box. Then any two boxes can share at most one color; otherwise two common colors would form such a pair. Hence

\[
|B_j\cap B_k|\le 1
\]

for every \(j<k\). Therefore

\[
\sum_{i=1}^{22} \binom{r_i}{2}
=
\sum_{1\le j<k\le 8} |B_j\cap B_k|
\le \binom{8}{2}=28.
\]

On the other hand, by Cauchy-Schwarz,

\[
\sum_{i=1}^{22} r_i^2
\ge
\frac{\left(\sum_{i=1}^{22} r_i\right)^2}{22}
=
\frac{48^2}{22}
=
\frac{1152}{11}.
\]

Thus

\[
\sum_{i=1}^{22} \binom{r_i}{2}
=
\frac12\left(\sum_{i=1}^{22} r_i^2-\sum_{i=1}^{22} r_i\right)
\ge
\frac12\left(\frac{1152}{11}-48\right)
=
\frac{312}{11}>28.
\]

This contradicts the previous inequality \(\le 28\). Therefore the assumption is false, so there must exist two colors that occur together in more than one box.

\[
\boxed{\text{There are two colors that occur together in more than one box.}}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 14,624 | Correct (7/7) | Per-box counting shows the sum of r_c over colors in each box is at most 13, so sum r_c^2 <= 104, while Cauchy-Schwarz gives sum r_c^2 >= 1152/11 > 104, a correct and complete contradiction. |
| A2 | stop | 23,190 | Correct (7/7) | Substituting r_x = 2 + d_x gives the exact identity T = 28 + (1/2) sum d_x^2 (verified), and the integer bound d_x^2 >= d_x gives T >= 30 > 28, contradicting the at-most-one-shared-color bound; complete. |
| A3 | stop | 21,332 | Correct (7/7) | With r_c = 2 + t_c the identity S = 28 + (1/2) sum t_c^2 is correct, and integrality gives sum t_c^2 >= \|sum t_c\| = 4, so S >= 30 contradicts the double-counting bound S <= 28. |
| A4 | stop | 17,256 | Correct (7/7) | Correctly reduces to every pair of boxes sharing at most one color, double counts to get sum C(r_c,2) <= 28, and uses Cauchy-Schwarz to get sum C(r_c,2) >= 312/11 > 28 (computation verified), a valid contradiction. |
| A5 | stop | 12,962 | Correct (7/7) | Double counting gives sum C(r_c,2) <= 28, and the stated identity sum C(r_c,2) = 28 + (1/2) sum d_c^2 (verified) with integers d_c summing to 4 forces the sum above 28; the >= 30 step is terse but immediate, so the proof is complete. |
| A6 | stop | 21,319 | Correct (7/7) | Correct double counting plus the standard (true) fact that integers with fixed sum minimize their sum of squares when as equal as possible (four 3s, eighteen 2s, giving 108), so sum C(r_c,2) >= 30 > 28, a valid contradiction. |
| A7 | stop | 20,000 | Correct (7/7) | Rigorous argument: the contradiction hypothesis gives \|B_i ∩ B_j\| <= 1 so sum C(r_c,2) <= 28, and Cauchy-Schwarz gives sum r_c^2 >= 1152/11, hence sum C(r_c,2) >= 312/11 > 28; computations are correct. |
| A8 | stop | 27,103 | Correct (7/7) | Double counting gives T <= 28, and the substitution a_c = 3 - r_c with sum a_c = 18 and a^2 >= a for integers correctly yields T = 21 + (1/2) sum a_c^2 >= 30, a valid contradiction. |
| A9 | stop | 18,076 | Correct (7/7) | Valid double counting gives sum C(r_c,2) = sum \|B_i cap B_j\| <= 28 under the assumption, and the integer inequality C(r,2) >= 2r-3 (from (r-2)(r-3) >= 0) yields sum >= 2*48-66 = 30, a correct contradiction. |
| A10 | stop | 22,533 | Correct (7/7) | With y_c = r_c - 2 (sum 4) and the integer inequality y^2 >= y, it correctly shows sum C(r_c,2) >= 30 > 28 = C(8,2), so some pair of boxes shares two colors; complete and correct. |
| A11 | stop | 14,234 | Correct (7/7) | Complete double-counting proof: under the assumption each box pair shares at most one color so sum C(r_j,2) <= 28, while Cauchy-Schwarz with sum r_j = 48 gives sum C(r_j,2) >= 312/11 > 28, contradiction; all steps check out. |
| A12 | stop | 9,481 | Correct (7/7) | Correctly establishes T = sum C(r_c,2) = sum \|B_i cap B_j\| <= 28 and uses Cauchy-Schwarz to get T >= 312/11 > 28, with all computations verified. |
| A13 | stop | 19,738 | Correct (7/7) | Double counting shows N = sum C(r_c,2) <= 28 under the assumption, while Cauchy-Schwarz gives N >= (48^2/22 - 48)/2 = 312/11 > 28, a complete and rigorous contradiction. |
| A14 | stop | 13,849 | Correct (7/7) | Valid proof by contradiction: box pairs share at most one color, so S = sum C(r_x,2) <= 28, while Cauchy-Schwarz yields S >= 312/11 > 28; all steps verified. |
| A15 | stop | 15,949 | Correct (7/7) | Counting ordered box pairs gives sum r_c^2 <= 48 + 56 = 104, and with e_c = r_c - 2 the correct identity sum r_c^2 = 104 + sum e_c^2 together with e_c^2 >= e_c gives sum r_c^2 >= 108, a valid contradiction. |
| A16 | stop | 25,877 | Correct (7/7) | Uses (r-2)(r-3) >= 0 for integers to get sum r_x^2 >= 108 and hence T >= 30, contradicting the correctly derived double-counting bound T <= 28. |

<details><summary>A1: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\), and for box \(i\) let \(S_i\) be the set of colors in it. Since no two balls in the same box share a color, \(|S_i|=6\).

For a color \(c\), let \(r_c\) be the number of boxes containing color \(c\). Then
\[
\sum_{c=1}^{22} r_c = 8\cdot 6 = 48.
\]

Assume, for contradiction, that no two colors occur together in more than one box. Equivalently, any two boxes share at most one color. Thus for \(i\neq j\),
\[
|S_i\cap S_j|\le 1.
\]

Fix a box \(B_i\). For each color \(c\in S_i\), it appears in \(r_c-1\) other boxes, so
\[
\sum_{c\in S_i}(r_c-1)
=
\sum_{j\neq i}|S_i\cap S_j|
\le 7.
\]
Hence
\[
\sum_{c\in S_i} r_c
=
6+\sum_{c\in S_i}(r_c-1)
\le 6+7=13.
\]

Summing over all \(i=1,\dots,8\),
\[
\sum_{i=1}^8\sum_{c\in S_i} r_c \le 8\cdot 13=104.
\]
But the left-hand side counts each color \(c\) exactly \(r_c\) times in each of the \(r_c\) boxes containing it, so it equals
\[
\sum_{c=1}^{22} r_c^2.
\]
Thus
\[
\sum_{c=1}^{22} r_c^2 \le 104.
\]

On the other hand, by Cauchy–Schwarz,
\[
48^2=\left(\sum_{c=1}^{22} r_c\right)^2
\le 22\sum_{c=1}^{22} r_c^2,
\]
so
\[
\sum_{c=1}^{22} r_c^2 \ge \frac{48^2}{22}
= \frac{2304}{22}
= \frac{1152}{11}
>104,
\]
a contradiction.

Therefore the assumption is false, so there must exist two colors that occur together in more than one box.

\[
\boxed{\text{There are two colors occurring together in more than one box.}}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\), and for each color \(x\), let \(r_x\) be the number of boxes containing color \(x\). Since each box has 6 distinct colors,
\[
\sum_x r_x = 8\cdot 6 = 48.
\]

Assume, for contradiction, that no two colors occur together in more than one box. Equivalently, every pair of colors appears together in at most one box.

For a fixed color \(x\), it appears in \(r_x\) boxes, so it contributes
\[
\binom{r_x}{2}
\]
pairs of boxes in which color \(x\) occurs in both boxes. Hence
\[
T:=\sum_x \binom{r_x}{2}
\]
counts all pairs \((\{i,j\},x)\) such that boxes \(B_i,B_j\) both contain color \(x\).

Now, if two boxes shared two different colors, then that pair of colors would occur together in both boxes, contradicting the assumption. Therefore any two boxes share at most one color. Since there are \(\binom{8}{2}=28\) pairs of boxes, we get
\[
T\le 28.
\]

On the other hand, write
\[
r_x=2+d_x.
\]
Then
\[
\sum_x d_x = \sum_x r_x - 2\cdot 22 = 48-44=4.
\]
Since each \(d_x\) is an integer, \(d_x^2\ge d_x\), so
\[
\sum_x d_x^2 \ge \sum_x d_x = 4.
\]
Therefore
\[
T=\sum_x \binom{r_x}{2}
=\sum_x \binom{2+d_x}{2}
=28+\frac12\sum_x d_x^2
\ge 28+\frac12\cdot 4=30.
\]
Thus \(T\ge 30\), contradicting \(T\le 28\).

Hence the assumption is false, so there must exist two colors that occur together in more than one box.

\[
\boxed{\text{Proved}}
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\), and for each color \(c\) let \(r_c\) be the number of boxes containing color \(c\).  
Since each box has \(6\) balls, the total number of color-box incidences is
\[
\sum_{c=1}^{22} r_c = 8\cdot 6 = 48.
\]

Define
\[
S=\sum_{c=1}^{22} \binom{r_c}{2}.
\]
For a fixed color \(c\), \(\binom{r_c}{2}\) counts pairs of boxes in which color \(c\) appears. Therefore \(S\) also equals the total number of pairs of boxes sharing a color:
\[
S=\sum_{1\le i<j\le 8} |B_i\cap B_j|.
\]

Now write \(r_c=2+t_c\). Then
\[
\sum_{c=1}^{22} t_c = \sum_{c=1}^{22} r_c - 2\cdot 22 = 48-44=4.
\]
For each color,
\[
\binom{r_c}{2}=\binom{t_c+2}{2}
=1+\frac{3t_c}{2}+\frac{t_c^2}{2}.
\]
Summing over all colors gives
\[
S=22+\frac32\sum t_c+\frac12\sum t_c^2
=22+\frac32\cdot 4+\frac12\sum t_c^2
=28+\frac12\sum t_c^2.
\]
Since the \(t_c\) are integers and \(\sum t_c=4\),
\[
\sum t_c^2\ge \sum |t_c|\ge \left|\sum t_c\right|=4.
\]
Hence
\[
S\ge 28+\frac12\cdot 4=30.
\]

On the other hand, if no two colors occur together in more than one box, then any two boxes can share at most one color, so
\[
|B_i\cap B_j|\le 1
\]
for every \(i<j\). Therefore
\[
S=\sum_{i<j}|B_i\cap B_j|\le \binom{8}{2}=28,
\]
contradicting \(S\ge 30\).

Thus the assumption is false, so there must exist two colors that occur together in more than one box.

</details>

<details><summary>A4: Correct (7/7)</summary>

Let \(B_1,\dots,B_8\) be the sets of colors in the 8 boxes. Since no two balls in the same box have the same color, \(|B_i|=6\) for each \(i\).

Assume, for contradiction, that no two colors occur together in more than one box. Then any two boxes can share at most one color; otherwise two shared colors would form a pair occurring together in both boxes.

For each color \(c\), let \(r_c\) be the number of boxes containing \(c\). Since there are \(8\cdot 6=48\) total color occurrences,

\[
\sum_{c=1}^{22} r_c=48.
\]

Now count triples \((c,\{i,j\})\) where color \(c\) appears in both boxes \(B_i\) and \(B_j\). For each color \(c\), there are \(\binom{r_c}{2}\) such pairs of boxes, so

\[
S:=\sum_{i<j}|B_i\cap B_j|
=\sum_{c=1}^{22}\binom{r_c}{2}.
\]

Because any two boxes share at most one color,

\[
S\le \binom{8}{2}=28.
\]

On the other hand, by Cauchy-Schwarz,

\[
\sum_{c=1}^{22} r_c^2 \ge \frac{(\sum r_c)^2}{22}
=\frac{48^2}{22}
=\frac{2304}{22}.
\]

Thus

\[
S=\frac12\left(\sum_{c=1}^{22} r_c^2-\sum_{c=1}^{22}r_c\right)
\ge \frac12\left(\frac{2304}{22}-48\right)
=\frac{312}{11}
=28+\frac4{11}>28.
\]

Since \(S\) is an integer, \(S\ge 29\), contradicting \(S\le 28\).

Therefore the assumption is false, and there must be two colors that occur together in more than one box.

</details>

<details><summary>A5: Correct (7/7)</summary>

Assume for contradiction that no two colors occur together in more than one box.

Let the boxes be \(B_1,\dots,B_8\), and let the color set have size \(22\). For a color \(c\), let \(r_c\) be the number of boxes containing \(c\).

First, \(r_c\le 4\). Indeed, if color \(c\) appears in \(r_c\) boxes, then in each such box there are \(5\) other colors. If the same color \(d\neq c\) appeared with \(c\) in two different boxes, then the pair \(\{c,d\}\) would occur together in two boxes, contradicting the assumption. Hence all \(5r_c\) other colors paired with \(c\) must be distinct. There are only \(21\) other colors, so
\[
5r_c\le 21 \implies r_c\le 4.
\]

Now count box-color incidences:
\[
\sum_{c} r_c = 8\cdot 6=48.
\]

Next, count pairs of boxes that share a color. Since no two colors occur together in more than one box, any two boxes can share at most one color; otherwise two colors would occur together in two boxes. Therefore
\[
\sum_{c} \binom{r_c}{2}
= \sum_{1\le i<j\le 8} |B_i\cap B_j|
\le \binom{8}{2}=28.
\]

But the condition \(r_c\le 4\) and \(\sum_c r_c=48\) forces
\[
\sum_c \binom{r_c}{2}\ge 30.
\]
Indeed, write \(r_c=2+d_c\). Then \(\sum_c d_c=48-2\cdot 22=4\), and since \(r_c\le 4\), each \(d_c\in\{-2,-1,0,1,2\}\). A short calculation gives
\[
\sum_c \binom{r_c}{2}
=28+\frac12\sum_c d_c^2\ge 30.
\]

Thus
\[
30\le \sum_c \binom{r_c}{2}\le 28,
\]
a contradiction.

Therefore our assumption was false: there exist two colors that occur together in more than one box.

\[
\boxed{\text{Proof complete.}}
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\). For each color \(c\), let \(A_c\) be the set of boxes containing color \(c\), and write \(r_c=|A_c|\).

Because each box has 6 balls of distinct colors,

\[
\sum_{c=1}^{22} r_c = 8\cdot 6 = 48.
\]

Assume for contradiction that no two colors occur together in more than one box. Then any two boxes can share at most one color; otherwise two common colors would form such a pair. Hence

\[
\sum_{1\le i<j\le 8} |B_i\cap B_j|\le \binom{8}{2}=28. \tag{1}
\]

On the other hand, counting pairs of boxes sharing a color gives

\[
\sum_{1\le i<j\le 8} |B_i\cap B_j|
= \sum_{c=1}^{22} \binom{r_c}{2}. \tag{2}
\]

Now we lower-bound the right-hand side. Since \(\sum r_c=48\) over 22 nonnegative integers, \(\sum r_c^2\) is minimized when the \(r_c\)'s are as equal as possible: four of them are \(3\) and eighteen are \(2\). Thus

\[
\sum_{c=1}^{22} r_c^2 \ge 4\cdot 3^2+18\cdot 2^2=108.
\]

Therefore

\[
\sum_{c=1}^{22}\binom{r_c}{2}
= \frac12\left(\sum r_c^2-\sum r_c\right)
\ge \frac12(108-48)=30. \tag{3}
\]

Combining (1), (2), and (3),

\[
28 \ge \sum_{i<j}|B_i\cap B_j|
= \sum_c \binom{r_c}{2}
\ge 30,
\]

a contradiction.

Hence the assumption is false, so there must exist two colors that occur together in more than one box.

\[
\boxed{\text{Such two colors exist.}}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\). Suppose, for contradiction, that no two colors occur together in more than one box.

For each color \(c\), let \(r_c\) be the number of boxes in which color \(c\) appears. Since each box contains 6 distinct colors, the total number of color-box incidences is

\[
\sum_{c} r_c = 8\cdot 6=48.
\]

Now consider two boxes \(B_i,B_j\). They cannot share two colors; otherwise those two colors would occur together in both boxes, contradicting the assumption. Hence

\[
|B_i\cap B_j|\le 1
\]

for every pair \(i<j\). Therefore

\[
\sum_{i<j}|B_i\cap B_j|\le \binom{8}{2}=28.
\]

On the other hand, a color \(c\) with \(r_c\) occurrences is counted in exactly \(\binom{r_c}{2}\) pairs of boxes, so

\[
\sum_c \binom{r_c}{2}
=
\sum_{i<j}|B_i\cap B_j|
\le 28.
\]

But by Cauchy-Schwarz,

\[
\sum_c r_c^2 \ge \frac{\left(\sum_c r_c\right)^2}{22}
=
\frac{48^2}{22}
=
\frac{1152}{11}.
\]

Thus

\[
\sum_c \binom{r_c}{2}
=
\frac12\left(\sum_c r_c^2-\sum_c r_c\right)
\ge
\frac12\left(\frac{1152}{11}-48\right)
=
\frac{312}{11}
>
28.
\]

This contradicts \(\sum_c \binom{r_c}{2}\le 28\). Hence our assumption was false.

Therefore, there exist two colors that occur together in more than one box.

</details>

<details><summary>A8: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\). Assume, for contradiction, that no two colors occur together in more than one box.

For each color \(c\), let \(r_c\) be the number of boxes containing \(c\). Since each box has 6 distinct colors,

\[
\sum_c r_c = 8\cdot 6 = 48.
\]

Define

\[
T=\sum_c \binom{r_c}{2}.
\]

This counts triples \((c,\{i,j\})\) where color \(c\) appears in both boxes \(B_i\) and \(B_j\).

If two boxes shared two colors, then those two colors would occur together in both boxes, contradicting the assumption. Hence every pair of boxes contributes at most one such triple, so

\[
T \le \binom{8}{2}=28.
\]

On the other hand, write \(a_c=3-r_c\). Then \(a_c\in\mathbb Z\) and

\[
\sum_c a_c = 3\cdot 22 - 48 = 66-48=18.
\]

For every integer \(a\), \(a^2\ge a\), so

\[
\sum_c a_c^2 \ge \sum_c a_c = 18.
\]

Now

\[
\binom{r_c}{2}=\binom{3-a_c}{2}
=\frac{(3-a_c)(2-a_c)}2
=3-\frac52a_c+\frac12a_c^2.
\]

Summing over all colors gives

\[
T
=66-\frac52\sum_c a_c+\frac12\sum_c a_c^2
=66-45+\frac12\sum_c a_c^2
=21+\frac12\sum_c a_c^2.
\]

Thus

\[
T \ge 21+\frac12\cdot 18 = 30,
\]

contradicting \(T\le 28\).

Therefore the assumption is false: there exist two colors that occur together in more than one box.

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

Assume, for contradiction, that no two colors occur together in more than one box.

For each color \(c\), let \(r_c\) be the number of boxes in which color \(c\) appears. Since there are \(8\cdot 6=48\) balls total,

\[
\sum_{c} r_c=48.
\]

Now consider two boxes \(B_i,B_j\). They cannot share two different colors: if they shared colors \(a\) and \(b\), then \(a\) and \(b\) would occur together in both boxes, contradicting the assumption. Hence

\[
|B_i\cap B_j|\le 1
\]

for every pair of boxes \(i<j\). Therefore

\[
\sum_{i<j} |B_i\cap B_j|\le \binom{8}{2}=28. \tag{1}
\]

On the other hand, the left-hand side counts, for each pair of boxes, how many colors they share. This is the same as counting, for each color \(c\), the number of pairs of boxes containing \(c\), namely \(\binom{r_c}{2}\). Thus

\[
\sum_{i<j} |B_i\cap B_j|=\sum_c \binom{r_c}{2}. \tag{2}
\]

For every integer \(r\ge 0\),

\[
\binom{r}{2}\ge 2r-3,
\]

because

\[
\binom{r}{2}-(2r-3)=\frac{(r-2)(r-3)}2\ge 0.
\]

Summing over all \(22\) colors gives

\[
\sum_c \binom{r_c}{2}
\ge \sum_c (2r_c-3)
=2\sum_c r_c-3\cdot 22
=2\cdot 48-66
=30. \tag{3}
\]

But (1) and (3) contradict each other. Therefore the assumption is false, so there exist two colors that occur together in more than one box.

\[
\boxed{\text{Proved}}
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\). For each color \(c\), let \(r_c\) be the number of boxes in which color \(c\) appears.

Since each box contains 6 balls of distinct colors,
\[
\sum_{c=1}^{22} r_c = 8\cdot 6 = 48.
\]

Now count pairs of boxes in which some color appears together. For a fixed color \(c\), it appears together in \(\binom{r_c}{2}\) pairs of boxes. Therefore
\[
N:=\sum_{1\le i<j\le 8} |B_i\cap B_j|
= \sum_{c=1}^{22} \binom{r_c}{2}.
\]

We estimate \(\sum \binom{r_c}{2}\). Put \(y_c=r_c-2\). Then
\[
\sum_{c=1}^{22} y_c = 48-2\cdot 22 = 4.
\]
For every integer \(y\),
\[
y^2-y=y(y-1)\ge 0,
\]
so \(y^2\ge y\). Hence
\[
\sum_{c=1}^{22} y_c^2 \ge \sum_{c=1}^{22} y_c = 4.
\]
Now
\[
\binom{r_c}{2}=\binom{y_c+2}{2}
=\frac{y_c^2+3y_c+2}{2}.
\]
Thus
\[
\sum_{c=1}^{22}\binom{r_c}{2}
= \frac12\sum y_c^2+\frac32\sum y_c+22
\ge \frac12\cdot 4+6+22=30.
\]
So
\[
N\ge 30.
\]

But there are only
\[
\binom{8}{2}=28
\]
pairs of boxes. If every pair of boxes had at most one common color, then \(N\le 28\), contradiction. Therefore some pair of boxes shares at least two colors. Those two colors occur together in more than one box.

\[
\boxed{\text{There exist two colors that occur together in more than one box.}}
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

Let the colors be \(1,2,\dots,22\). For color \(j\), let \(r_j\) be the number of boxes in which color \(j\) appears.

Each box contains 6 balls of distinct colors, so there are \(8\cdot 6=48\) color-box incidences:

\[
\sum_{j=1}^{22} r_j=48.
\]

Assume, for contradiction, that no two colors occur together in more than one box. Then any two boxes can share at most one color; otherwise, if two boxes shared two colors \(a,b\), those two colors would occur together in both boxes, contradicting the assumption.

Now count pairs \((\{B_i,B_j\},c)\) where \(c\) is a color appearing in both boxes \(B_i\) and \(B_j\). For a fixed color \(c\), it appears in \(r_c\) boxes, hence contributes \(\binom{r_c}{2}\) such pairs of boxes. Therefore the total number \(T\) of such pairs is

\[
T=\sum_{j=1}^{22}\binom{r_j}{2}.
\]

Since each pair of boxes shares at most one color, and there are \(\binom{8}{2}=28\) pairs of boxes,

\[
T\le \binom{8}{2}=28.
\]

On the other hand, by Cauchy’s inequality,

\[
\sum_{j=1}^{22} r_j^2 \ge \frac{\left(\sum_{j=1}^{22} r_j\right)^2}{22}
= \frac{48^2}{22}.
\]

Thus

\[
T=\frac12\left(\sum r_j^2-\sum r_j\right)
\ge \frac12\left(\frac{48^2}{22}-48\right)
= \frac{312}{11}>28.
\]

Since \(T\) is an integer, this gives \(T\ge 29\), contradicting \(T\le 28\).

Therefore the assumption is false, so there must exist two colors that occur together in more than one box.

\[
\boxed{\text{Two such colors exist.}}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\). For each color \(c\), let \(r_c\) be the number of boxes containing color \(c\).

Since each box contains 6 distinct colors,
\[
\sum_{c=1}^{22} r_c = 8\cdot 6=48.
\]

Assume for contradiction that no pair of colors occurs together in more than one box.  
Equivalently, every pair of colors appears together in at most one box.

For a fixed color \(c\), it appears in \(r_c\) boxes, so it contributes \(\binom{r_c}{2}\) pairs of boxes both containing \(c\). Thus the total number
\[
T=\sum_{c=1}^{22}\binom{r_c}{2}
\]
counts triples \((c,\{i,j\})\) with \(c\in B_i\cap B_j\).

Now, if two boxes \(B_i,B_j\) shared two colors, say \(a,b\), then the pair \(\{a,b\}\) would occur together in both boxes, contradicting the assumption. Hence any two boxes share at most one color, so
\[
T=\sum_{1\le i<j\le 8} |B_i\cap B_j|
\le \binom{8}{2}=28.
\]

On the other hand, by Cauchy-Schwarz,
\[
\sum_{c=1}^{22} r_c^2 \ge \frac{\left(\sum_{c=1}^{22} r_c\right)^2}{22}
=\frac{48^2}{22}
=\frac{1152}{11}.
\]
Therefore
\[
T=\frac12\sum_{c=1}^{22} r_c(r_c-1)
=\frac12\left(\sum_{c=1}^{22}r_c^2-\sum_{c=1}^{22}r_c\right)
\ge \frac12\left(\frac{1152}{11}-48\right)
=\frac{312}{11}>28.
\]
This contradicts \(T\le 28\). Therefore our assumption was false.

Hence there exist two colors that occur together in more than one box.

</details>

<details><summary>A13: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\), and let the color set be \(C\), with \(|C|=22\).  
For a color \(c\in C\), let \(r_c\) be the number of boxes containing \(c\).

Since each box has 6 balls,
\[
\sum_{c\in C} r_c = 8\cdot 6 = 48.
\]

Assume for contradiction that no two colors occur together in more than one box. Then any two boxes can share at most one color; otherwise two shared colors would occur together in both boxes.

Let
\[
N=\sum_{1\le i<j\le 8} |B_i\cap B_j|.
\]
Because each intersection has size at most \(1\),
\[
N\le \binom{8}{2}=28.
\]

On the other hand, counting pairs \((c,\{i,j\})\) where color \(c\) appears in both boxes \(B_i\) and \(B_j\), we get
\[
N=\sum_{c\in C}\binom{r_c}{2}.
\]
Thus
\[
2N=\sum_{c\in C} r_c(r_c-1)
=\sum_{c\in C} r_c^2-\sum_{c\in C}r_c
=\sum_{c\in C} r_c^2-48.
\]
By Cauchy-Schwarz,
\[
\sum_{c\in C} r_c^2 \ge \frac{\left(\sum_{c\in C} r_c\right)^2}{22}
=\frac{48^2}{22}.
\]
Therefore
\[
N\ge \frac12\left(\frac{48^2}{22}-48\right)
=\frac{312}{11}>28.
\]
Since \(N\) is an integer, this gives \(N\ge 29\), contradicting \(N\le 28\).

Hence the assumption is false. Therefore some two boxes share at least two colors; those two colors occur together in more than one box.

\[
\boxed{\text{There exist two colors that occur together in more than one box.}}
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\), viewed as sets of colors. Since no two balls in the same box share a color, each \(B_i\) has exactly 6 colors.

For each color \(x\), define
\[
r_x=\#\{i: x\in B_i\}.
\]
Because each box has 6 colors,
\[
\sum_x r_x = 8\cdot 6=48.
\]

Assume for contradiction that no two colors occur together in more than one box. Then any two boxes can share at most one color: if \(B_i\) and \(B_j\) shared two colors \(a,b\), then the pair \(\{a,b\}\) would occur in both boxes, contradicting the assumption.

Now count pairs \((\{i,j\},x)\) where boxes \(B_i,B_j\) and color \(x\) are such that \(x\in B_i\cap B_j\). For a fixed color \(x\), there are \(\binom{r_x}{2}\) such box-pairs. Hence
\[
S:=\sum_x \binom{r_x}{2}
=\sum_{1\le i<j\le 8} |B_i\cap B_j|.
\]
Since every intersection has size at most \(1\),
\[
S\le \binom{8}{2}=28.
\]

On the other hand, by Cauchy-Schwarz,
\[
\sum_x r_x^2 \ge \frac{(\sum_x r_x)^2}{22}
= \frac{48^2}{22}
= \frac{1152}{11}.
\]
Therefore
\[
S=\frac12\sum_x r_x^2-\frac12\sum_x r_x
\ge \frac12\left(\frac{1152}{11}-48\right)
= \frac{312}{11}
>28.
\]

This contradicts \(S\le 28\). Therefore the assumption is false, so there must exist two colors that occur together in more than one box.

\[
\boxed{\text{There are two colors that occur together in more than one box.}}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

\[
\boxed{\text{There must be two colors occurring together in more than one box.}}
\]

Proof:

Let the boxes be \(B_1,\dots,B_8\). Since no two balls in the same box have the same color, each \(B_i\) is a set of 6 colors:

\[
|B_i|=6.
\]

For each color \(c\), let \(r_c\) be the number of boxes containing color \(c\). Then

\[
\sum_{c} r_c = \sum_{i=1}^8 |B_i| = 8\cdot 6=48.
\]

Assume for contradiction that no two colors occur together in more than one box. Then any two boxes can share at most one color: if \(B_i\cap B_j\) contained two colors \(a,b\), then the pair \(\{a,b\}\) would occur together in both boxes, contradiction.

Now count \(\sum_c r_c^2\) in two ways. For a fixed color \(c\), \(r_c^2\) counts ordered pairs of boxes both containing \(c\). Hence

\[
\sum_c r_c^2=\sum_{i,j}|B_i\cap B_j|.
\]

The diagonal contribution is

\[
\sum_{i=1}^8 |B_i|=8\cdot 6=48.
\]

For \(i\ne j\), we know \(|B_i\cap B_j|\le 1\), so

\[
\sum_{i\ne j}|B_i\cap B_j|
=2\sum_{1\le i<j\le 8}|B_i\cap B_j|
\le 2\binom{8}{2}=56.
\]

Therefore

\[
\sum_c r_c^2 \le 48+56=104.
\]

On the other hand, write \(e_c=r_c-2\). Then

\[
\sum_c e_c=\sum_c r_c-2\cdot 22=48-44=4.
\]

Since each \(e_c\) is an integer, \(e_c^2\ge e_c\) for every \(c\). Thus

\[
\sum_c r_c^2
=104+\sum_c e_c^2
\ge 104+\sum_c e_c
=104+4
=108.
\]

This contradicts \(\sum_c r_c^2\le 104\). Hence our assumption was false, so there exist two colors that occur together in more than one box.

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

Let the boxes be \(B_1,\dots,B_8\), and let \(X\) be the set of the \(22\) colors. Since no two balls in a box have the same color,

\[
|B_i|=6 \qquad (i=1,\dots,8).
\]

For each color \(x\in X\), let \(r_x\) be the number of boxes in which color \(x\) appears. Then

\[
\sum_{x\in X} r_x=\sum_{i=1}^8 |B_i|=8\cdot 6=48.
\]

Assume, for contradiction, that no two colors occur together in more than one box. Then any two boxes can share at most one color; otherwise two shared colors would occur together in two boxes.

Now count pairs \((\{i,j\},x)\) where \(i<j\) and \(x\in B_i\cap B_j\). For a fixed color \(x\), there are \(\binom{r_x}{2}\) such pairs of boxes, so the total is

\[
T=\sum_{x\in X}\binom{r_x}{2}.
\]

On one hand, because each pair of boxes shares at most one color,

\[
T=\sum_{1\le i<j\le 8} |B_i\cap B_j|
\le \binom{8}{2}=28.
\]

On the other hand, for every integer \(r\ge 0\),

\[
r^2-5r+6=(r-2)(r-3)\ge 0,
\]

so \(r^2\ge 5r-6\). Therefore

\[
\sum_{x\in X} r_x^2
\ge 5\sum_{x\in X}r_x-6|X|
=5\cdot 48-6\cdot 22
=240-132=108.
\]

Hence

\[
T=\frac12\sum_{x\in X}(r_x^2-r_x)
\ge \frac12(108-48)=30.
\]

Thus \(T\ge 30\) and \(T\le 28\), a contradiction. Therefore our assumption was false, so some pair of colors occurs together in more than one box.

\[
\boxed{\text{There exist two colors that occur together in more than one box.}}
\]

</details>
