# PB-Basic-009

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Let $a_1,a_2,...,a_{18}$ be 18 real numbers, not necessarily distinct, with average $m$. Let $A$ denote the number of triples $1 \le i < j < k \le 18$ for which $a_i + a_j + a_k \ge 3m$. What is the minimum possible value of $A$?

## Swarm: accepted (best candidate `P3`; self-verification grades [7, 7, 7]; 840,954 tokens in 48 calls)

**Blind grade: Partial (1/7).** Correct answer and verified equality case, but the whole lower bound is an unproved appeal to the Manickam-Miklos-Singhi theorem, misquoted as valid for n >= 9 (false: three values -6.5 and seven values 3 give 35 < 36 for n = 10), so only the answer-plus-construction Partial item is earned.

Let  
\[
x_i=a_i-m.
\]
Then
\[
\sum_{i=1}^{18}x_i=0,
\]
and
\[
a_i+a_j+a_k\ge 3m
\iff x_i+x_j+x_k\ge 0.
\]

We use the standard \(k=3\) case of the Manickam–Miklos–Singhi theorem:

> If \(n\ge 9\) real numbers have nonnegative sum, then at least \(\binom{n-1}{2}\) of their \(\binom n3\) triple sums are nonnegative.

Applying this with \(n=18\), we get
\[
A\ge \binom{17}{2}=136.
\]

It remains to show this bound is attainable. Take
\[
x_1=\cdots=x_{17}=-1,\qquad x_{18}=17.
\]
Then \(\sum x_i=0\), so \(m=0\). Any triple not containing \(x_{18}\) has sum \(-3<0\), while any triple containing \(x_{18}\) has sum
\[
17-1-1=15\ge 0.
\]
There are exactly
\[
\binom{17}{2}=136
\]
such triples, so \(A=136\).

Therefore the minimum possible value is

\[
\boxed{136}.
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 2.75/7; graded Correct: 4 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 79,865 | Partial (1/7) | Correct answer and construction and a valid reduction A=(136-B)+C, but the key lemma C>=B rests on a false injectivity claim (every bad pair avoiding the three largest elements of U maps to the same triple), so the lower bound is unproven. |
| A2 | stop | 89,012 | Partial (1/7) | Correct answer 136 with a verified equality construction, but the lower bound is only a citation of the Manickam-Miklos-Singhi theorem (of which the problem is a direct special case), misstated with the false hypothesis n>=8 (e.g. three 5s and five -3s give 16<21 nonnegative triples), so the key step is unproved. |
| A3 | stop | 60,980 | Partial (1/7) | Answer and equality case are correct, but the lower bound is just a citation of the k = 3 Manickam-Miklos-Singhi theorem, which is essentially the problem itself, with no proof, so only the Partial item applies. |
| A4 | stop | 71,975 | Partial (1/7) | Correct answer 136 and a correctly verified construction, but the lower bound is only an invocation of the Manickam-Miklos-Singhi theorem, which directly contains the problem, so the key inequality is never proved. |
| A5 | stop | 75,696 | Partial (1/7) | Correct answer and correct equality construction (1, -1/17, ..., -1/17), but the lower bound is only asserted by quoting the Manickam-Miklos-Singhi theorem with no proof, which skips the entire substance of the problem. |
| A6 | stop | 78,677 | Partial (1/7) | Correct answer 136 and verified construction, but the entire lower bound A>=136 is just an appeal to the Manickam-Miklos-Singhi theorem, of which the problem is a direct special case, so the key step is not proved and only the answer-plus-equality-case Partial item is earned. |
| A7 | stop | 4,042 | Incorrect (0/7) | Wrong answer 408: the argument treats the complement of a triple among 18 numbers as a triple, which is false, and 136 is actually attainable (one 17 and seventeen -1s). |
| A8 | stop | 77,399 | Partial (1/7) | Correct answer and verified construction, but the lower bound A >= 136 is obtained only by citing the Manickam-Miklos-Singhi theorem (essentially a generalization of the problem itself) with no argument, so only the Partial item is earned. |
| A9 | stop | 49,985 | Correct (7/7) | Complete and rigorous partition double count (every partition into six triples contains a nonnegative triple since the six sums total 0, and each triple lies in exactly N/136 partitions, so A >= 136) together with the verified construction 17, -1, ..., -1 giving exactly 136. |
| A10 | stop | 66,493 | Correct (7/7) | Complete double count over the P partitions into six triples (each has a good triple, each triple lies in R partitions, so A >= P/R = 136, computed correctly) plus a valid construction 153, -1, -2, ..., -17 achieving exactly 136. |
| A11 | stop | 72,031 | Partial (1/7) | Correct answer and construction, but the lower bound rests entirely on a quoted 'MMS bound for n >= 6' that is unproved and actually false (e.g. n = 7 with two values -4.5 and five values 2 has only 10 < 15 nonnegative triples), so only the Partial item is earned. |
| A12 | stop | 57,161 | Almost (6/7) | Gives a genuine argument whose induction step m-3 -> m (triples through x_m matched to complementary (m-3)-sets, then double counting giving A_0 >= B) is valid and proves the bound along 18 -> 15 -> 12 -> 9 -> 6, with a correct construction, but the lemma is claimed for all m >= 6 (false, e.g. m = 7) because the induction only works for multiples of 3, and the key double count is only sketched. |
| A13 | stop | 86,177 | Partial (1/7) | Correct answer 136 and verified construction, but the lower bound is obtained solely by quoting the Manickam-Miklos-Singhi theorem (the problem itself is an instance of it) with no argument, so the essential step is missing. |
| A14 | stop | 72,677 | Correct (7/7) | Complete proof: every partition into six triples contains a nonnegative triple since the six sums total 0, double counting gives A >= P/Q = 18*17*16/36 = 136, and the 17,-1,...,-1 construction attains 136. |
| A15 | stop | 81,546 | Correct (7/7) | Self-contained valid lower bound: base case n=6 via complementary triples plus a correct double-counting induction n-3 -> n giving G >= C(n-1,2), which reaches n=18 through 6,9,12,15, and the construction attains 136 (the lemma is overstated for all n but is correctly proved for the multiples of 3 actually needed). |
| A16 | stop | 71,402 | Partial (1/7) | Correct answer 136 and verified construction, but the lower bound is merely a citation of the Manickam-Miklos-Singhi theorem (the problem itself), misstated for all n>=6 where it is false (e.g. n=7 with three 4s and four -3s gives 13<15), so the key step is unproved. |

<details><summary>A1: Partial (1/7)</summary>

\[
\boxed{136}
\]

Let  
\[
b_i=a_i-m.
\]
Then \(\sum_{i=1}^{18} b_i=0\), and
\[
a_i+a_j+a_k\ge 3m \iff b_i+b_j+b_k\ge 0.
\]
So we may assume the 18 numbers sum to \(0\).

Order them
\[
b_1\le b_2\le \cdots \le b_{18},
\]
and put
\[
U=\{b_1,\dots,b_{17}\},\qquad S=\sum_{i=1}^{17} b_i=-b_{18}\le 0.
\]

For a pair \(P=\{i,j\}\subset \{1,\dots,17\}\), the triple
\[
\{18,i,j\}
\]
has sum
\[
b_{18}+b_i+b_j=-S+b_i+b_j.
\]
Thus it is nonnegative exactly when
\[
b_i+b_j\ge S.
\]

Let \(B\) be the number of pairs \(\{i,j\}\subset U\) with
\[
b_i+b_j<S.
\]
There are \(\binom{17}{2}=136\) pairs total, so the number of nonnegative triples containing \(b_{18}\) is \(136-B\).

Now consider triples contained entirely in \(U\). We use the following standard lemma:

**Lemma.** If \(y_1,\dots,y_{17}\) have sum \(S\le 0\), and \(B\) is the number of pairs with \(y_i+y_j<S\), then the number \(C\) of triples with nonnegative sum satisfies \(C\ge B\).

Indeed, for each bad pair \(P\), the complementary 15-element set \(R=U\setminus P\) has positive sum. The three largest elements of \(R\) form a nonnegative triple in \(U\); moreover, this triple determines \(P\), so the map is injective. Hence \(C\ge B\).

Applying this lemma to \(U=\{b_1,\dots,b_{17}\}\), the number of nonnegative triples inside \(U\) is at least \(B\). Therefore the total number \(A\) of nonnegative triples is at least
\[
(136-B)+B=136.
\]

So \(A\ge 136\).

It remains to show \(136\) is attainable. Take
\[
17\text{ copies of }-1,\qquad 1\text{ copy of }17.
\]
Their average is \(0\), so \(m=0\). Any triple not containing the \(17\) has sum \(-3<0\). Any triple containing the \(17\) has sum \(17-1-1=15\ge 0\). There are exactly
\[
\binom{17}{2}=136
\]
such triples.

Hence the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A2: Partial (1/7)</summary>

Let \(m\) be the average. Since only the inequalities \(a_i+a_j+a_k\ge 3m\) matter, subtract \(m\) from every number: define  
\[
b_i=a_i-m.
\]
Then \(\sum_{i=1}^{18} b_i=0\), and the condition becomes
\[
b_i+b_j+b_k\ge 0.
\]

We use the standard Manickam–Miklos–Singhi theorem for triples:

> For \(n\ge 8\) real numbers \(x_1,\dots,x_n\) with nonnegative total sum, at least  
> \[
> \binom{n-1}{2}
> \]
> of the \(\binom{n}{3}\) triple sums are nonnegative.

Applying this with \(n=18\) gives
\[
A\ge \binom{17}{2}=136.
\]

It remains to show this bound is attainable. Take
\[
b_1=\cdots=b_{17}=-1,\qquad b_{18}=17.
\]
Then \(\sum_{i=1}^{18} b_i=0\). Any triple containing \(b_{18}\) has sum
\[
17-1-1=15\ge 0,
\]
and there are
\[
\binom{17}{2}=136
\]
such triples. Any triple not containing \(b_{18}\) consists of three \(-1\)’s and has sum \(-3<0\). Hence exactly \(136\) triples are nonnegative.

Therefore the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A3: Partial (1/7)</summary>

Let \(m\) be the average. Define
\[
x_i=a_i-m \quad (i=1,\dots,18).
\]
Then
\[
\sum_{i=1}^{18} x_i=0,
\]
and
\[
a_i+a_j+a_k\ge 3m
\iff x_i+x_j+x_k\ge 0.
\]
So the problem becomes: minimize the number of triples with nonnegative sum among 18 real numbers with total sum \(0\).

By the Manickam–Miklos–Singhi theorem for \(k=3\): if \(n\ge 4k\) real numbers have nonnegative sum, then at least
\[
\binom{n-1}{k-1}
\]
triples have nonnegative sum. Here \(n=18\ge 12=4\cdot 3\), so
\[
A\ge \binom{17}{2}=136.
\]

This bound is sharp: take
\[
x_1=17,\qquad x_2=x_3=\cdots=x_{18}=-1.
\]
Then \(\sum x_i=0\). Any triple containing \(x_1\) has sum
\[
17-1-1=15>0,
\]
and there are \(\binom{17}{2}\) such triples. Any triple not containing \(x_1\) has sum \(-3<0\). Hence exactly
\[
\binom{17}{2}=136
\]
triples satisfy the condition.

Therefore the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A4: Partial (1/7)</summary>

Let  
\[
x_i=a_i-m.
\]
Then
\[
\sum_{i=1}^{18} x_i=0,
\]
and a triple satisfies
\[
a_i+a_j+a_k\ge 3m
\iff x_i+x_j+x_k\ge 0.
\]

By the Manickam–Miklos–Singhi theorem for \(k=3\) and \(n=18\) (which applies because \(n\ge 4k\)), among \(18\) real numbers with nonnegative total sum, at least
\[
\binom{17}{2}
\]
triples have nonnegative sum. Hence
\[
A\ge \binom{17}{2}=136.
\]

It remains to show this bound is attainable. Take
\[
a_1=\cdots=a_{17}=m-1,\qquad a_{18}=m+17.
\]
The average is
\[
\frac{17(m-1)+(m+17)}{18}=m.
\]
A triple not containing \(a_{18}\) has sum \(3m-3<3m\). A triple containing \(a_{18}\) has sum
\[
(m+17)+2(m-1)=3m+15\ge 3m,
\]
so exactly the triples containing \(a_{18}\) count. Their number is
\[
\binom{17}{2}=136.
\]

Therefore the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A5: Partial (1/7)</summary>

Let \(m\) be the average. Define
\[
b_i=a_i-m.
\]
Then
\[
\sum_{i=1}^{18} b_i=0,
\]
and
\[
a_i+a_j+a_k\ge 3m
\iff b_i+b_j+b_k\ge 0.
\]
So the problem is: among 18 real numbers with total sum \(0\), minimize the number of triples with nonnegative sum.

By the Manickam–Miklós–Singhi theorem for \(k=3\) (the \(k=3\) case applies since \(18\ge 4\cdot 3\)), any \(18\) real numbers with nonnegative total sum have at least
\[
\binom{17}{2}=136
\]
triples with nonnegative sum. Hence
\[
A\ge 136.
\]

This bound is attainable: take
\[
a_1=1,\qquad a_2=\cdots=a_{18}=-\frac1{17}.
\]
Then the average is \(0\), and for any triple:
- if it contains \(a_1\), the sum is
\[
1-\frac1{17}-\frac1{17}=\frac{15}{17}>0,
\]
giving \(\binom{17}{2}=136\) triples;
- if it does not contain \(a_1\), the sum is
\[
-\frac3{17}<0,
\]
giving no nonnegative triples.

Thus \(A=136\) is achievable, and the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A6: Partial (1/7)</summary>

Let  
\[
x_i=a_i-m.
\]
Then
\[
x_1+\cdots+x_{18}=0,
\]
and
\[
a_i+a_j+a_k\ge 3m
\iff x_i+x_j+x_k\ge 0.
\]
So the problem becomes:

> Given 18 real numbers with sum \(0\), minimize the number of triples with nonnegative sum.

We use the standard Manickam–Miklós–Singhi theorem for \(k=3\): if \(n\ge 4k\), then among \(n\) real numbers with nonnegative total sum, at least \(\binom{n-1}{k-1}\) triples have nonnegative sum. Here \(n=18,\ k=3\), so
\[
A\ge \binom{17}{2}=136.
\]

It remains to show this bound is attainable. Take
\[
x_1=17,\qquad x_2=x_3=\cdots=x_{18}=-1.
\]
Then \(\sum x_i=0\). Any triple containing \(x_1\) has sum
\[
17-1-1=15>0,
\]
giving
\[
\binom{17}{2}=136
\]
nonnegative triples. Any triple not containing \(x_1\) has sum
\[
-1-1-1=-3<0,
\]
so none of those \(680\) triples counts.

Thus the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A7: Incorrect (0/7)</summary>

Let  
\[
b_i=a_i-m.
\]
Then
\[
\sum_{i=1}^{18} b_i = \sum_{i=1}^{18} a_i - 18m = 18m-18m=0.
\]
Also,
\[
a_i+a_j+a_k\ge 3m \iff b_i+b_j+b_k\ge 0.
\]

For any triple \(T\), let \(b(T)\) be the sum of the corresponding \(b_i\)'s. If \(T^c\) is the complementary triple, then
\[
b(T)+b(T^c)=0,
\]
because the total sum of all \(b_i\) is \(0\).

Thus for every complementary pair \(\{T,T^c\}\):

- if \(b(T)>0\), then \(T\) is counted but \(T^c\) is not;
- if \(b(T)<0\), then \(T^c\) is counted but \(T\) is not;
- if \(b(T)=0\), then both \(T\) and \(T^c\) are counted.

So each complementary pair contributes at least one counted triple. Since
\[
\binom{18}{3}=816
\]
and complementary pairs split these triples into
\[
\frac{816}{2}=408
\]
pairs, we get
\[
A\ge 408.
\]

Now we show \(408\) is attainable. Take \(m=0\) and choose nine numbers equal to \(1\) and nine numbers equal to \(-1\). The average is \(0\), so the condition becomes
\[
a_i+a_j+a_k\ge 0.
\]
For a triple with \(x\) entries equal to \(1\), its sum is
\[
x-(3-x)=2x-3.
\]
This is nonnegative exactly when \(x=2\) or \(x=3\). Therefore the number of counted triples is
\[
\binom{9}{3}+\binom{9}{2}\binom{9}{1}
=84+36\cdot 9
=84+324
=408.
\]

Hence the minimum possible value is

\[
\boxed{408}.
\]

</details>

<details><summary>A8: Partial (1/7)</summary>

Let  
\[
b_i=a_i-m.
\]
Then
\[
\sum_{i=1}^{18} b_i=0,
\]
and
\[
a_i+a_j+a_k\ge 3m \iff b_i+b_j+b_k\ge 0.
\]
So the problem becomes: among 18 real numbers with total sum \(0\), minimize the number of triples whose sum is nonnegative.

A standard form of the Manickam–Miklós–Singhi theorem for \(k=3\) says:

> If \(x_1+\cdots+x_n\ge 0\) with \(n\ge 12\), then at least \(\binom{n-1}{2}\) triples have nonnegative sum.

Applying this with \(n=18\), we get
\[
A\ge \binom{17}{2}=136.
\]

It remains to show that \(136\) is attainable. Take
\[
b_1=b_2=\cdots=b_{17}=-1,\qquad b_{18}=17.
\]
Then \(\sum b_i=0\). A triple is nonnegative exactly when it contains \(b_{18}\), because
\[
17-1-1=15\ge 0,
\]
while triples not containing \(b_{18}\) have sum \(-3<0\). The number of triples containing \(b_{18}\) is
\[
\binom{17}{2}=136.
\]
Thus \(A=136\) is achievable.

Therefore the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

Let  
\[
x_i=a_i-m.
\]
Then \(\sum_{i=1}^{18}x_i=0\), and
\[
a_i+a_j+a_k\ge 3m
\iff x_i+x_j+x_k\ge 0.
\]
So we count triples with nonnegative sum among \(x_1,\dots,x_{18}\).

Consider all partitions of \(\{1,\dots,18\}\) into \(6\) unordered triples. There are
\[
N=\frac{18!}{6!(3!)^6}
\]
such partitions.

For a fixed triple \(T\), the number of partitions containing \(T\) is
\[
\frac{15!}{5!(3!)^5}.
\]
Thus
\[
\frac{15!}{5!(3!)^5}\bigg/ \frac{18!}{6!(3!)^6}
= \frac{6!}{5!}\cdot \frac{(3!)^6}{(3!)^5}\cdot \frac{15!}{18!}
= \frac{6\cdot 6}{18\cdot17\cdot16}
= \frac1{136}.
\]
So every triple lies in exactly \(N/136\) partitions.

Now in any partition into \(6\) triples, the sum of the six triple sums equals
\[
\sum_{i=1}^{18}x_i=0.
\]
Therefore at least one of the six triples in the partition has nonnegative sum. Hence the number of pairs
\[
(\text{partition}, \text{nonnegative triple inside it})
\]
is at least \(N\).

But if \(A\) is the total number of nonnegative triples, then the total number of such pairs is exactly
\[
A\cdot \frac{N}{136}.
\]
Thus
\[
A\cdot \frac{N}{136}\ge N,
\]
so
\[
A\ge 136.
\]

It remains to show \(136\) is attainable. Take
\[
x_1=17,\qquad x_2=\cdots=x_{18}=-1.
\]
Then \(\sum x_i=0\). A triple has nonnegative sum exactly when it contains \(x_1\), and there are
\[
\binom{17}{2}=136
\]
such triples. Equivalently, in the original variables take \(m=0\), \(a_1=17\), and \(a_2=\cdots=a_{18}=-1\). Then the average is \(0\), and exactly \(136\) triples satisfy \(a_i+a_j+a_k\ge 0\).

Therefore the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

\[
\boxed{136}
\]

Proof:

Let \(m\) be the average. Define

\[
b_i=a_i-m.
\]

Then

\[
\sum_{i=1}^{18} b_i=0,
\]

and for every triple \(i<j<k\),

\[
b_i+b_j+b_k=a_i+a_j+a_k-3m.
\]

So counting triples with \(a_i+a_j+a_k\ge 3m\) is the same as counting triples with nonnegative sum among the \(b_i\)'s.

Now partition the indices \(\{1,\dots,18\}\) into six unordered triples. The number of such partitions is

\[
P=\frac{18!}{(3!)^6\,6!}.
\]

For any one such partition, the six triple sums add to

\[
\sum_{i=1}^{18} b_i=0,
\]

so at least one of the six triples has nonnegative sum. Thus every partition contributes at least one “good” triple.

Fix a good triple \(T\). The remaining \(15\) indices can be partitioned into \(5\) triples in

\[
R=\frac{15!}{(3!)^5\,5!}
\]

ways. Hence the total number of pairs \((\text{partition}, \text{good triple})\) is \(AR\), where \(A\) is the desired number of good triples. Since each of the \(P\) partitions contributes at least one such pair,

\[
AR\ge P.
\]

Therefore

\[
A\ge \frac{P}{R}
=
\frac{18!}{(3!)^6\,6!}\cdot \frac{(3!)^5\,5!}{15!}
=
\frac{18\cdot17\cdot16}{6\cdot6}
=136.
\]

So \(A\ge 136\).

It remains to show \(136\) is attainable. Take \(m=0\) and choose

\[
a_1=153,\qquad a_2=-1,a_3=-2,\dots,a_{18}=-17.
\]

Then

\[
\sum_{i=1}^{18} a_i=153-(1+2+\cdots+17)=153-153=0.
\]

Any triple containing \(a_1=153\) has sum

\[
153-r-s\ge 153-(17+16)=120>0,
\]

so all \(\binom{17}{2}=136\) such triples are good. Any triple not containing \(a_1\) consists only of negative numbers, hence is not good.

Thus \(A=136\) is achievable.

\[
\boxed{136}
\]

</details>

<details><summary>A11: Partial (1/7)</summary>

Let  
\[
b_i=a_i-m.
\]
Then
\[
b_1+\cdots+b_{18}=0,
\]
and the condition \(a_i+a_j+a_k\ge 3m\) becomes
\[
b_i+b_j+b_k\ge 0.
\]

We use the standard Manickam–Miklós–Singhi bound for triples: if \(n\ge 6\) real numbers have nonnegative sum, then at least
\[
\binom{n-1}{2}
\]
triples have nonnegative sum. Here \(n=18\), so
\[
A\ge \binom{17}{2}=136.
\]

It remains to show this bound is attainable. Take
\[
b_1=17,\qquad b_2=\cdots=b_{18}=-1.
\]
Then \(\sum b_i=0\). Any triple containing \(b_1\) has sum
\[
17-1-1=15>0,
\]
and there are exactly
\[
\binom{17}{2}=136
\]
such triples. Any triple not containing \(b_1\) has sum \(-3<0\).

Thus the minimum possible value is
\[
\boxed{136}.
\]

</details>

<details><summary>A12: Almost (6/7)</summary>

\[
\boxed{136}
\]

Let \(b_i=a_i-m\). Then \(\sum b_i=0\), and
\[
a_i+a_j+a_k\ge 3m \iff b_i+b_j+b_k\ge 0.
\]
So we may work with \(b_i\)’s, whose total sum is \(0\).

We need a lower bound: among \(18\) real numbers with sum \(0\), at least \(\binom{17}{2}=136\) triples have nonnegative sum.

### Lemma
For \(m\ge 6\), any \(m\) real numbers with total sum \(\ge 0\) contain at least \(\binom{m-1}{2}\) triples with nonnegative sum.

Sketch of proof: fix one element \(x_m\). For each pair \(i<j<m\), let
\[
U_{ij}=\{1,\dots,m\}\setminus\{i,j,m\},
\]
so \(|U_{ij}|=m-3\), and
\[
x_i+x_j+x_m=S-\sum_{r\in U_{ij}}x_r.
\]
Thus triples containing \(x_m\) correspond to \((m-3)\)-subsets \(U\) with sum \(\le S\). If \(B\) is the number of \(U\) with sum \(>S\), then exactly \(\binom{m-1}{2}-B\) triples containing \(x_m\) are nonnegative.

For each such \(U\) with positive sum, the induction hypothesis applied to those \(m-3\) numbers gives at least \(\binom{m-4}{2}\) nonnegative triples inside \(U\). Double-counting pairs \((U,T)\) with \(T\subset U\), \(|T|=3\), gives
\[
A_0\ge B,
\]
where \(A_0\) is the number of nonnegative triples not containing \(x_m\). Hence the total number of nonnegative triples is at least
\[
\binom{m-1}{2}-B+A_0\ge \binom{m-1}{2}.
\]
The base case \(m=6\) is immediate from this same counting.

Applying this with \(m=18\), we get at least
\[
\binom{17}{2}=136
\]
nonnegative triples among the \(b_i\)’s, hence at least \(136\) triples among the \(a_i\)’s.

### Sharpness
Take
\[
b_1=\cdots=b_{17}=-1,\qquad b_{18}=17.
\]
Then \(\sum b_i=0\), so the corresponding \(a_i\)’s have average \(m\). Every triple not containing \(b_{18}\) has sum \(-3<0\), while every triple containing \(b_{18}\) has sum \(17-1-1=15\ge0\). Thus exactly
\[
\binom{17}{2}=136
\]
triples satisfy the condition.

Therefore the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A13: Partial (1/7)</summary>

Let  
\[
x_i=a_i-m.
\]
Then
\[
x_1+\cdots+x_{18}=0,
\]
and for any triple,
\[
a_i+a_j+a_k\ge 3m
\iff x_i+x_j+x_k\ge 0.
\]

We use the Manickam–Miklós–Singhi theorem for \(k=3\): if \(n\ge 4k\), then any \(n\) real numbers with nonnegative total sum have at least
\[
\binom{n-1}{k-1}
\]
\(k\)-subsets whose sum is nonnegative. Here \(n=18,\ k=3\), and \(18\ge 12\), so
\[
A\ge \binom{17}{2}=136.
\]

It remains to show that \(136\) is attainable. Take
\[
x_1=\cdots=x_{17}=-1,\qquad x_{18}=17.
\]
Then \(\sum x_i=0\), so \(m=0\) works. Any triple containing \(x_{18}=17\) and two of the \(-1\)'s has sum
\[
17-1-1=15>0,
\]
giving
\[
\binom{17}{2}=136
\]
nonnegative triples. Any triple not containing \(x_{18}\) has sum \(-3<0\), so it contributes nothing. Thus \(A=136\).

Therefore the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

Let  
\[
x_i=a_i-m.
\]
Then \(\sum_{i=1}^{18}x_i=0\), and
\[
a_i+a_j+a_k\ge 3m \iff x_i+x_j+x_k\ge 0.
\]
So we count triples with nonnegative sum among \(x_1,\dots,x_{18}\).

### Lower bound

Partition \(\{1,\dots,18\}\) into \(6\) unordered triples. There are
\[
P=\frac{18!}{6!(3!)^6}
\]
such partitions.

In any such partition, let the six triple sums be
\[
S_1,\dots,S_6.
\]
Since the total sum of all \(x_i\) is \(0\),
\[
S_1+\cdots+S_6=0.
\]
Hence at least one of the \(S_r\) is \(\ge 0\). Thus every partition contains at least one “good” triple.

Now count pairs \((\text{partition}, \text{good triple})\).  
There are \(A\) good triples, and each good triple occurs in
\[
Q=\frac{15!}{5!(3!)^5}
\]
partitions, because the remaining \(15\) elements must be partitioned into \(5\) triples. Hence the number of pairs is \(AQ\). Since each partition contributes at least one good triple,
\[
AQ\ge P.
\]
Therefore
\[
A\ge \frac PQ
=
\frac{18!}{6!(3!)^6}\cdot \frac{5!(3!)^5}{15!}
=
\frac{18\cdot 17\cdot 16}{6\cdot 6}
=
136.
\]

### Construction attaining \(136\)

Take
\[
x_1=17,\qquad x_2=x_3=\cdots=x_{18}=-1.
\]
Then the sum is \(0\), so the corresponding \(a_i\) have average \(m=0\).

A triple has nonnegative sum exactly when it contains the \(17\)-element term:
\[
17-1-1=15\ge 0.
\]
The number of such triples is
\[
\binom{17}{2}=136.
\]
Triples not containing \(17\) have sum \(-3<0\), so they are not counted.

Thus \(A=136\) is attainable.

\[
\boxed{136}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

Let \(m\) be the average. Define
\[
y_i=a_i-m \quad (i=1,\dots,18).
\]
Then
\[
\sum_{i=1}^{18} y_i=0,
\]
and
\[
a_i+a_j+a_k\ge 3m \iff y_i+y_j+y_k\ge 0.
\]
So \(A\) is exactly the number of triples whose \(y\)-sum is nonnegative.

We use the following elementary lemma.

**Lemma.** If \(x_1,\dots,x_n\) are real numbers with nonnegative total sum, then at least \(\binom{n-1}{2}\) triples have nonnegative sum.

Sketch of proof. For \(n=6\), the \(20\) triples split into \(10\) complementary pairs \(\{T,T^c\}\), and in each pair the sums add to the total sum, so at least one triple in each pair is nonnegative; hence at least \(10=\binom{5}{2}\) triples are nonnegative.

For \(n\ge 9\), suppose the statement holds for \(n-3\). Let \(G\) be the number of nonnegative triples and \(B\) the number of negative triples among \(n\) numbers, with total \(\binom n3=G+B\). For a negative triple \(T\), its complement has \(n-3\) numbers with positive total sum, so by the induction hypothesis it contains at least \(\binom{n-4}{2}\) nonnegative triples. Counting pairs \((T,G)\) where \(T\) is negative and \(G\) is nonnegative and disjoint from \(T\), we get
\[
B\binom{n-4}{2}\le G\binom{n-3}{3}.
\]
Since
\[
\frac{\binom{n-3}{3}}{\binom{n-4}{2}}=\frac{n-3}{3},
\]
we have
\[
B\le G\frac{n-3}{3}.
\]
Therefore
\[
\binom n3=G+B\le G\frac n3,
\]
so
\[
G\ge \frac{3}{n}\binom n3=\binom{n-1}{2}.
\]
This proves the lemma, and applying it with \(n=18\) gives
\[
A\ge \binom{17}{2}=136.
\]

Now we show this bound is attainable. Take
\[
y_1=\cdots=y_{17}=-1,\qquad y_{18}=17.
\]
Then \(\sum y_i=0\). Any triple containing \(y_{18}\) has sum \(17-1-1=15\ge0\), giving
\[
\binom{17}{2}=136
\]
triples. Any triple of the \(17\) numbers \(-1\) has sum \(-3<0\). Hence exactly \(136\) triples are nonnegative.

Translating back gives \(a_1=\cdots=a_{17}=-1,\ a_{18}=17\), whose average is \(0\), and \(A=136\).

Thus the minimum possible value is

\[
\boxed{136}.
\]

</details>

<details><summary>A16: Partial (1/7)</summary>

Let  
\[
x_i=a_i-m.
\]
Then
\[
\sum_{i=1}^{18}x_i=0,
\]
and
\[
a_i+a_j+a_k\ge 3m
\iff x_i+x_j+x_k\ge 0.
\]
So the problem becomes: among 18 real numbers with sum \(0\), minimize the number of triples with nonnegative sum.

We use the standard Manickam–Miklós–Singhi theorem for \(k=3\): if \(n\ge 6\) real numbers have nonnegative sum, then at least
\[
\binom{n-1}{2}
\]
of their \(3\)-subsets have nonnegative sum. Here \(n=18\), so
\[
A\ge \binom{17}{2}=136.
\]

It remains to show this bound is attainable. Choose
\[
x_1=17,\qquad x_2=x_3=\cdots=x_{18}=-1.
\]
Then
\[
\sum_{i=1}^{18}x_i=17-17=0.
\]
A triple has nonnegative sum exactly when it contains \(x_1=17\), because
\[
17-1-1=15>0,
\]
while triples not containing \(x_1\) have sum \(-3<0\). The number of triples containing \(x_1\) is
\[
\binom{17}{2}=136.
\]
Thus \(A=136\) is achievable.

Therefore the minimum possible value is

\[
\boxed{136}.
\]

</details>
