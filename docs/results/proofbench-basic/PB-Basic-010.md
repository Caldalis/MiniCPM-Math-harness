# PB-Basic-010

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

The numbers $\{ 1, 2, 3, \ldots , 2022 \}$ are partitioned into two sets $A$ and $B$ of size $1011$ each. Let $S_{AB}$ denote the set of all pairs $(a, b) \in A \times B$ where $a < b$, and let $S_{BA}$ denote the set of all pairs $(a, b) \in A \times B$ where $b < a$.

 Prove that $\sum_{(a, b) \in S_{AB}} (b - a) \neq \sum_{(a, b) \in S_{BA}} (a - b)$.

## Swarm: accepted (best candidate `P1`; self-verification grades [7, 7, 7]; 337,683 tokens in 48 calls)

**Blind grade: Correct (7/7).** Cut-counting correctly gives D = m*sum_k(2x_k - k), and sum_k(2x_k - k) has the parity of sum_{k=1}^{2m-1} k = m(2m-1), which is odd, so D is nonzero; complete, with only a harmless reuse of the symbol S_AB for the sum.

Let \(n=2022=2m\), so \(m=1011\). For each \(k=1,\dots,n-1\), define
\[
x_k=|A\cap \{1,2,\dots,k\}|.
\]
Then \(|B\cap \{1,\dots,k\}|=k-x_k\), and \(|A\cap \{k+1,\dots,n\}|=m-x_k\).

For a pair \(a<b\) with \(a\in A,b\in B\), we have \(b-a\) equal to the number of cuts \(k\) such that \(a\le k<b\). Hence
\[
S_{AB}=\sum_{k=1}^{n-1} x_k(m-k+x_k).
\]
Similarly, for \(b<a\), the cut-counting gives
\[
S_{BA}=\sum_{k=1}^{n-1}(k-x_k)(m-x_k).
\]

Let \(D=S_{AB}-S_{BA}\). Then
\[
\begin{aligned}
D&=\sum_{k=1}^{n-1}\Big[x_k(m-k+x_k)-(k-x_k)(m-x_k)\Big]\\
&=\sum_{k=1}^{n-1} m(2x_k-k)\\
&=m\sum_{k=1}^{n-1}(2x_k-k).
\end{aligned}
\]
So it suffices to show
\[
T:=\sum_{k=1}^{n-1}(2x_k-k)\neq 0.
\]
Modulo \(2\),
\[
T\equiv \sum_{k=1}^{n-1} k \pmod 2.
\]
Since \(n=2m\),
\[
\sum_{k=1}^{n-1}k=\sum_{k=1}^{2m-1}k=m(2m-1)\equiv m \pmod 2.
\]
Here \(m=1011\) is odd, so \(T\) is odd. In particular, \(T\neq 0\). Therefore
\[
D=mT\neq 0,
\]
so
\[
S_{AB}\neq S_{BA}.
\]

\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 5,840 | Correct (7/7) | Shows the sum of the two quantities equals sum \|a-b\| which is congruent mod 2 to 1011(s_A + s_B), i.e. to 1011*2023, odd, so the two quantities cannot be equal; correct and complete despite reusing S_AB, S_BA to denote the sums. |
| A2 | stop | 4,333 | Correct (7/7) | Shows X-Y = 1011(sum B - sum A) and that sum A = sum B is impossible because their total 1011*2023 is odd, so X-Y is nonzero; complete and rigorous. |
| A3 | stop | 19,102 | Correct (7/7) | Valid cut-counting argument with correct counts P_k = x_k(m-k+x_k), Q_k = (k-x_k)(m-x_k) giving D = m*sum(2x_k - k), which is shown to be odd; the phrase that summing P_k 'counts exactly the pairs' should say each pair is counted b-a times and the final box is mislabeled, but the identity used is correct and the proof is complete. |
| A4 | stop | 25,314 | Correct (7/7) | Gap-counting gives D = m*sum_k(p_k - q_k), correctly evaluated as m(sum B - sum A), and sum B - sum A = 1011*2023 - 2*sum A is odd, so D is nonzero; complete. |
| A5 | stop | 6,841 | Correct (7/7) | Shows D_+ + D_- = sum of \|a-b\| over A x B, which is congruent mod 2 to sum(a+b) = 1011^2*2023 (odd), so D_+ = D_- would make the total even, a contradiction; complete and correct. |
| A6 | stop | 20,606 | Correct (7/7) | Using +-1 signs and a unit-cut decomposition, correctly derives Delta = 1011*sum_{t=1}^{2021} X_t with X_t congruent to t mod 2, so Delta is odd and nonzero; all computations check out. |
| A7 | stop | 10,715 | Correct (7/7) | Observes the difference equals sum over all (a,b) in AxB of (b-a) = 1011(s_B - s_A), and since s_A + s_B = 1011*2023 is odd, s_B - s_A is odd hence nonzero; complete and correct. |
| A8 | stop | 10,189 | Correct (7/7) | Shows X+Y = sum \|a-b\| is congruent mod 2 to 1+2+...+2022 = 1011*2023, which is odd, so X = Y would force X+Y even, a contradiction; complete and rigorous. |
| A9 | stop | 20,897 | Correct (7/7) | Correct cut-counting derivation (each pair counted once per separating cut) of Delta = m*sum(A_k - B_k) = m(sum_B b - sum_A a), and since the total 1011*2023 is odd the two set sums differ, so Delta is nonzero; complete and rigorous. |
| A10 | stop | 12,773 | Correct (7/7) | Cut-by-cut counting correctly yields D = n*sum d_k with d_k = 2alpha_k - k congruent to k mod 2, so sum d_k has the parity of n(2n-1), which is odd, making D odd and nonzero; complete. |
| A11 | stop | 17,963 | Correct (7/7) | Correctly rewrites the difference with indicator variables and a unit-cut decomposition as D = 1011*sum_{k=1}^{2021}(2a_k - k), verifies the per-cut count, and shows the sum is odd so D is odd and nonzero; complete and rigorous. |
| A12 | stop | 8,075 | Correct (7/7) | Correctly shows the difference equals 1011(T_B - T_A) and that T_B - T_A is odd because T_A + T_B = 1011*2023 is odd, so the difference is nonzero; complete and rigorous. |
| A13 | stop | 6,339 | Correct (7/7) | Shows L-R equals the sum over all of A x B of (b-a) = 1011(sum B - sum A), and since sum A + sum B = 1011*2023 is odd the difference is odd, so L-R is odd and nonzero; complete and rigorous. |
| A14 | stop | 26,747 | Correct (7/7) | Gap-counting yields D = n*sum_t y_t with y_t = 2a_t - t congruent to t mod 2, and sum_{t=1}^{2n-1} t has the parity of n = 1011 (odd), so D is odd and nonzero; all steps verified. |
| A15 | stop | 8,754 | Correct (7/7) | Shows X-Y = 1011(sigma_B - sigma_A) and that sigma_A + sigma_B = 1011*2023 is odd, so sigma_A differs from sigma_B and X is not equal to Y; complete and rigorous. |
| A16 | stop | 19,536 | Correct (7/7) | Writes Delta = sum_{i<j}(j-i)(eps_i - eps_j), correctly computes the coefficient C_i - D_i = m(2m+1-2i), so Delta is 1011 times a sum of 1011 odd numbers, hence odd and nonzero; all algebra verified. |

<details><summary>A1: Correct (7/7)</summary>

Let \(m=1011\). For every pair \((a,b)\in A\times B\), the absolute difference \(|a-b|\) is counted exactly once in either \(S_{AB}\) or \(S_{BA}\). Hence

\[
T:=\sum_{a\in A,\ b\in B}|a-b|
= S_{AB}+S_{BA}.
\]

So if \(S_{AB}=S_{BA}\), then \(T=2S_{AB}\) would be even.

Now compute \(T\) modulo \(2\). For integers \(a,b\),

\[
|a-b|\equiv a+b \pmod 2.
\]

Therefore

\[
T \equiv \sum_{a\in A,\ b\in B}(a+b)\pmod 2.
\]

Since \(|A|=|B|=m=1011\),

\[
\sum_{a\in A,\ b\in B}(a+b)
= m\sum_{a\in A}a+m\sum_{b\in B}b
\equiv \sum_{k=1}^{2m}k \pmod 2.
\]

But

\[
\sum_{k=1}^{2m}k = m(2m+1)=1011\cdot 2023,
\]

which is odd because both \(1011\) and \(2023\) are odd. Thus \(T\) is odd.

So \(T\) cannot be even, while equality \(S_{AB}=S_{BA}\) would force \(T\) to be even. Contradiction.

Hence

\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}.
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

Let \(m=1011\), so \(2022=2m\). Let

\[
T=\sum_{(a,b)\in A\times B}(b-a).
\]

Split the cross pairs \(A\times B\) into the two given sets:

\[
A\times B=\bigl((a,b)\in A\times B:a<b\bigr)\cup\bigl((a,b)\in A\times B:b<a\bigr).
\]

For pairs with \(b<a\), we have \(b-a=-(a-b)\). Hence

\[
T=\sum_{(a,b)\in S_{AB}}(b-a)+\sum_{(a,b)\in S_{BA}}(b-a)
\]
\[
=\sum_{S_{AB}}(b-a)-\sum_{S_{BA}}(a-b).
\]

So the desired equality

\[
\sum_{S_{AB}}(b-a)=\sum_{S_{BA}}(a-b)
\]

would be equivalent to \(T=0\).

Now compute \(T\) directly:

\[
T=\sum_{a\in A}\sum_{b\in B}(b-a)
=|A|\sum_{b\in B}b-|B|\sum_{a\in A}a.
\]

Since \(|A|=|B|=1011=m\),

\[
T=m\left(\sum_{b\in B}b-\sum_{a\in A}a\right)
=1011\left(\sum_{b\in B}b-\sum_{a\in A}a\right).
\]

Thus \(T=0\) would imply

\[
\sum_{b\in B}b=\sum_{a\in A}a.
\]

But

\[
\sum_{k=1}^{2022}k=\frac{2022\cdot 2023}{2}=1011\cdot 2023,
\]

which is odd. If the two sums in \(A\) and \(B\) were equal, their total would be twice an integer, hence even. Contradiction. Therefore

\[
\sum_{b\in B}b-\sum_{a\in A}a\neq 0,
\]

so

\[
T=1011\left(\sum_{b\in B}b-\sum_{a\in A}a\right)\neq 0.
\]

Hence

\[
\sum_{S_{AB}}(b-a)\neq \sum_{S_{BA}}(a-b).
\]

\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

Let \(n=2022=2m\), so \(m=1011\). Define

\[
D=\sum_{(a,b)\in S_{AB}}(b-a)-\sum_{(a,b)\in S_{BA}}(a-b).
\]

We will prove \(D\neq 0\).

For \(0\le k\le 2m\), let

\[
x_k=\bigl|A\cap \{1,\dots,k\}\bigr|.
\]

Thus \(x_0=0,\ x_{2m}=m\), and for \(1\le k\le 2m-1\),

\[
c_k=2x_k-k
=|A\cap\{1,\dots,k\}|-|B\cap\{1,\dots,k\}|.
\]

Now fix \(k\). Let

\[
P_k=\#\{(a,b)\in A\times B: a\le k<b\},
\]

and

\[
Q_k=\#\{(a,b)\in A\times B: b\le k<a\}.
\]

Then

\[
P_k=x_k(m-k+x_k),
\]

because there are \(x_k\) choices for \(a\le k\) and \(m-k+x_k\) choices for \(b>k\). Similarly,

\[
Q_k=(k-x_k)(m-x_k),
\]

because there are \(k-x_k\) choices for \(b\le k\) and \(m-x_k\) choices for \(a>k\).

Hence

\[
\begin{aligned}
P_k-Q_k
&=x_k(m-k+x_k)-(k-x_k)(m-x_k)\\
&=2mx_k-km\\
&=m(2x_k-k)\\
&=m c_k.
\end{aligned}
\]

On the other hand, summing \(P_k\) over all cuts counts exactly the pairs in \(S_{AB}\), and summing \(Q_k\) counts exactly the pairs in \(S_{BA}\). Therefore

\[
\begin{aligned}
D&=\sum_{k=1}^{2m-1}(P_k-Q_k)\\
&=m\sum_{k=1}^{2m-1} c_k.
\end{aligned}
\]

Now \(c_k=2x_k-k\equiv k\pmod 2\), so

\[
\sum_{k=1}^{2m-1} c_k
\equiv \sum_{k=1}^{2m-1} k
=\frac{2m(2m-1)}2
=m(2m-1)\pmod 2.
\]

Since \(m=1011\) is odd and \(2m-1=2021\) is odd, \(m(2m-1)\) is odd. Thus

\[
\sum_{k=1}^{2m-1} c_k
\]

is odd. Therefore \(D=m\sum_{k=1}^{2m-1}c_k\) is odd, in particular \(D\neq 0\).

Hence

\[
\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b).
\]

\[
\boxed{S_{AB}\neq S_{BA}}
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

Let  
\[
X=\sum_{(a,b)\in S_{AB}}(b-a),\qquad Y=\sum_{(a,b)\in S_{BA}}(a-b),
\]
and put \(D=X-Y\). We prove \(D\neq 0\).

Write \(m=1011\), so the ground set is \(\{1,\dots,2m\}\) with \(2m=2022\).

For each gap \(k=1,\dots,2m-1\), define
\[
p_k=|A\cap\{1,\dots,k\}|,\qquad q_k=|B\cap\{1,\dots,k\}|.
\]
Thus \(p_k+q_k=k\), and there are \(m-p_k\) elements of \(A\) greater than \(k\), and \(m-q_k\) elements of \(B\) greater than \(k\).

Now count contributions of each gap \(k\) to \(D=X-Y\).

- Pairs \((a,b)\in A\times B\) with \(a\le k<b\) cross the gap from \(A\)-side to \(B\)-side. There are
  \[
  p_k(m-q_k)
  \]
  such pairs, and each contributes \(+1\) to the gap-count for \(X\).

- Pairs \((a,b)\in A\times B\) with \(b\le k<a\) cross the gap from \(B\)-side to \(A\)-side. There are
  \[
  q_k(m-p_k)
  \]
  such pairs, and each contributes \(-1\) to the gap-count for \(D\).

Hence the total contribution of gap \(k\) to \(D\) is
\[
p_k(m-q_k)-q_k(m-p_k)=m(p_k-q_k).
\]
Therefore
\[
D=\sum_{k=1}^{2m-1} m(p_k-q_k)
=m\sum_{k=1}^{2m-1}(p_k-q_k).
\]

Now compute the sum. Each \(a\in A\) appears in \(p_k\) exactly for \(k=a,a+1,\dots,2m-1\), i.e. \(2m-a\) times. Similarly each \(b\in B\) appears in \(q_k\) exactly \(2m-b\) times. Thus
\[
\sum_{k=1}^{2m-1}(p_k-q_k)
=
\sum_{a\in A}(2m-a)-\sum_{b\in B}(2m-b)
=
\sum_{b\in B}b-\sum_{a\in A}a.
\]
So
\[
D=m\left(\sum_{b\in B}b-\sum_{a\in A}a\right).
\]

Now
\[
\sum_{i=1}^{2022}i=\frac{2022\cdot 2023}{2}=1011\cdot 2023,
\]
which is odd. Hence
\[
\sum_{b\in B}b-\sum_{a\in A}a
=
1011\cdot 2023-2\sum_{a\in A}a
\]
is odd, in particular nonzero. Since \(m=1011\neq 0\), we get
\[
D=m\left(\sum_{b\in B}b-\sum_{a\in A}a\right)\neq 0.
\]
Thus \(X-Y\neq 0\), so
\[
\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b).
\]

\[
\boxed{\text{The two sums are unequal.}}
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

Let  
\[
D_+=\sum_{(a,b)\in S_{AB}}(b-a),\qquad 
D_-=\sum_{(a,b)\in S_{BA}}(a-b).
\]
For every cross pair \((a,b)\in A\times B\), since \(A\cap B=\varnothing\), we have \(a\ne b\). Hence exactly one of \(a<b\) or \(b<a\) holds, so
\[
D_++D_-=\sum_{a\in A,\ b\in B}|a-b|.
\]

Now work modulo \(2\). Since \(|x|\equiv x\pmod 2\),
\[
\sum_{a\in A,\ b\in B}|a-b|
\equiv \sum_{a\in A,\ b\in B}(a+b)\pmod 2.
\]
But
\[
\sum_{a\in A,\ b\in B}(a+b)
=|B|\sum_{a\in A}a+|A|\sum_{b\in B}b.
\]
Here \(|A|=|B|=1011\), so
\[
\sum_{a\in A,\ b\in B}(a+b)
\equiv 1011\sum_{k=1}^{2022}k \pmod 2.
\]
Now
\[
\sum_{k=1}^{2022}k=\frac{2022\cdot 2023}{2}=1011\cdot 2023,
\]
so
\[
1011\sum_{k=1}^{2022}k
=1011^2\cdot 2023,
\]
which is odd. Therefore
\[
D_++D_-\equiv 1\pmod 2,
\]
so \(D_++D_-\) is odd.

If \(D_+=D_-\), then \(D_++D_-=2D_+\) would be even, contradiction. Hence
\[
D_+\neq D_-.
\]

\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

Let  
\[
\Delta=\sum_{(a,b)\in S_{AB}}(b-a)-\sum_{(a,b)\in S_{BA}}(a-b).
\]
It suffices to prove \(\Delta\ne 0\).

Write \(2022=2m\) with \(m=1011\). For each \(i\), define
\[
\varepsilon_i=\begin{cases}
1,& i\in A,\\
-1,& i\in B,
\end{cases}
\qquad X_k=\sum_{i=1}^k \varepsilon_i.
\]
Since \(|A|=|B|\), we have \(X_0=X_{2022}=0\).

For \(i<j\), the pair \((i,j)\) contributes only when \(\varepsilon_i=-\varepsilon_j\). If \(\varepsilon_i=1,\varepsilon_j=-1\), it contributes \(j-i\) to \(\Delta\); if \(\varepsilon_i=-1,\varepsilon_j=1\), it contributes \(-(j-i)\). Hence
\[
\Delta=\sum_{1\le i<j\le 2022}\frac{(j-i)(\varepsilon_i-\varepsilon_j)}2.
\]
Using \(j-i=\#\{t:i\le t<j\}\),
\[
\Delta=\sum_{t=1}^{2021}\sum_{i\le t<j}\frac{\varepsilon_i-\varepsilon_j}{2}.
\]
For fixed \(t\),
\[
\sum_{i\le t<j}\varepsilon_i=X_t(2022-t),
\qquad
\sum_{i\le t<j}\varepsilon_j=t\sum_{j>t}\varepsilon_j=-tX_t.
\]
Therefore
\[
\sum_{i\le t<j}\frac{\varepsilon_i-\varepsilon_j}{2}
=\frac{X_t(2022-t)+tX_t}{2}
=\frac{2022X_t}{2}=1011X_t.
\]
Summing over \(t=1,\dots,2021\),
\[
\Delta=1011\sum_{t=1}^{2021}X_t.
\]

Now \(X_t=2|A\cap[1,t]|-t\), so \(X_t\equiv t\pmod 2\). Hence
\[
\sum_{t=1}^{2021}X_t\equiv \sum_{t=1}^{2021}t
=\frac{2021\cdot 2022}{2}
=1011\cdot 2021\equiv 1\pmod 2.
\]
Thus \(\sum_{t=1}^{2021}X_t\) is odd. Since \(1011\) is also odd,
\[
\Delta=1011\sum_{t=1}^{2021}X_t
\]
is odd. In particular \(\Delta\ne 0\). Therefore the two sums cannot be equal.

\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

Let  
\[
P=\sum_{(a,b)\in S_{AB}}(b-a),\qquad 
Q=\sum_{(a,b)\in S_{BA}}(a-b),
\]
and define
\[
\Delta=P-Q.
\]
We will show \(\Delta\neq 0\).

Let \(m=1011\). Since \(|A|=|B|=m\), for every \(a\in A\) and \(b\in B\), the ordered pair \((a,b)\) contributes \(b-a\) to \(\Delta\):

- If \(a<b\), then \((a,b)\in S_{AB}\), contributing \(b-a\).
- If \(b<a\), then \((a,b)\in S_{BA}\), and the contribution to \(\Delta=P-Q\) is \(-(a-b)=b-a\).

Hence
\[
\Delta=\sum_{a\in A}\sum_{b\in B}(b-a).
\]
Expanding,
\[
\Delta=\sum_{a\in A}\sum_{b\in B}b-\sum_{a\in A}\sum_{b\in B}a
= m\sum_{b\in B}b-m\sum_{a\in A}a.
\]
Let
\[
s_A=\sum_{a\in A}a,\qquad s_B=\sum_{b\in B}b.
\]
Then
\[
\Delta=m(s_B-s_A).
\]

Now
\[
s_A+s_B=1+2+\cdots+2022=\frac{2022\cdot 2023}{2}=1011\cdot 2023.
\]
The number \(1011\cdot 2023\) is odd, so
\[
s_B-s_A=(s_A+s_B)-2s_A
\]
is odd. In particular \(s_B-s_A\neq 0\). Since \(m=1011\neq 0\), we get
\[
\Delta=m(s_B-s_A)\neq 0.
\]
Therefore
\[
P-Q\neq 0,
\]
so
\[
\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b).
\]

\[
\boxed{\text{The two sums are unequal.}}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

Let  
\[
X=\sum_{(a,b)\in S_{AB}}(b-a),\qquad 
Y=\sum_{(a,b)\in S_{BA}}(a-b).
\]
For every pair \((a,b)\in A\times B\), the contribution to \(X+Y\) is exactly \(|a-b|\). Indeed, if \(a<b\), then \((a,b)\in S_{AB}\) and contributes \(b-a=|a-b|\); if \(b<a\), then \((a,b)\in S_{BA}\) and contributes \(a-b=|a-b|\). Hence
\[
X+Y=\sum_{a\in A,\ b\in B}|a-b|.
\]

Now work modulo \(2\). Since \(|a-b|\equiv a+b\pmod 2\),
\[
X+Y\equiv \sum_{a\in A,\ b\in B}(a+b)\pmod 2.
\]
But
\[
\sum_{a\in A,\ b\in B}(a+b)
=|B|\sum_{a\in A}a+|A|\sum_{b\in B}b.
\]
Here \(|A|=|B|=1011\), so modulo \(2\),
\[
X+Y\equiv \sum_{a\in A}a+\sum_{b\in B}b
=1+2+\cdots+2022.
\]
Thus
\[
X+Y\equiv \frac{2022\cdot 2023}{2}
=1011\cdot 2023\equiv 1\pmod 2,
\]
because \(1011\) and \(2023\) are both odd. Therefore \(X+Y\) is odd.

If \(X=Y\), then \(X+Y=2X\) would be even, contradiction. Hence
\[
X\ne Y.
\]

\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\ne \sum_{(a,b)\in S_{BA}}(a-b)}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

Let \(n=2022\) and \(m=1011\). Define
\[
\Delta=\sum_{(a,b)\in S_{AB}}(b-a)-\sum_{(a,b)\in S_{BA}}(a-b).
\]
We will show \(\Delta\neq 0\).

For \(1\le k\le n-1\), let
\[
A_k=|A\cap\{1,\dots,k\}|,\qquad B_k=|B\cap\{1,\dots,k\}|=k-A_k.
\]

For a fixed cut between \(k\) and \(k+1\), the pairs counted by
\[
A_k(m-B_k)
\]
are exactly those \((a,b)\in A\times B\) with \(a\le k<b\). Each such pair has distance \(b-a\), and it is counted once for each cut between \(a\) and \(b\). Hence
\[
\sum_{(a,b)\in S_{AB}}(b-a)=\sum_{k=1}^{n-1} A_k(m-B_k).
\]
Similarly,
\[
\sum_{(a,b)\in S_{BA}}(a-b)=\sum_{k=1}^{n-1} B_k(m-A_k).
\]
Therefore
\[
\Delta=\sum_{k=1}^{n-1}\bigl(A_k(m-B_k)-B_k(m-A_k)\bigr)
=m\sum_{k=1}^{n-1}(A_k-B_k).
\]

Now
\[
\sum_{k=1}^{n-1}A_k=\sum_{a\in A}(n-a),\qquad
\sum_{k=1}^{n-1}B_k=\sum_{b\in B}(n-b),
\]
so
\[
\sum_{k=1}^{n-1}(A_k-B_k)
=\sum_{a\in A}(n-a)-\sum_{b\in B}(n-b)
=\sum_{b\in B}b-\sum_{a\in A}a.
\]
Thus
\[
\Delta=m\left(\sum_{b\in B}b-\sum_{a\in A}a\right).
\]

But
\[
\sum_{i=1}^{2022}i=\frac{2022\cdot 2023}{2}=1011\cdot 2023,
\]
which is odd because \(1011\) and \(2023\) are both odd. Hence \(\sum_{a\in A}a\) and \(\sum_{b\in B}b\) cannot be equal; otherwise their total sum would be even. Therefore
\[
\sum_{b\in B}b-\sum_{a\in A}a\neq 0.
\]
Since \(m=1011\neq 0\), it follows that
\[
\Delta\neq 0.
\]

So
\[
\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b).
\]

\[
\boxed{\text{Proved}}
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

Let  
\[
n=1011,\qquad m=2n=2022,
\]
and define
\[
T_+=\sum_{(a,b)\in S_{AB}}(b-a),\qquad 
T_-=\sum_{(a,b)\in S_{BA}}(a-b).
\]
We prove that \(T_+\neq T_-\).

Set
\[
D=T_+-T_-.
\]
If \(T_+=T_-\), then \(D=0\), impossible if we show \(D\) is always odd.

For each \(k=1,\dots,m-1\), let
\[
\alpha_k=\#(A\cap\{1,\dots,k\}),\qquad 
\beta_k=\#(B\cap\{1,\dots,k\}).
\]
Then \(\alpha_k+\beta_k=k\), and define
\[
d_k=\alpha_k-\beta_k=2\alpha_k-k.
\]

Now consider the cut between \(k\) and \(k+1\). Pairs \((i,j)\) with \(i\le k<j\) and \(i\in A,j\in B\) contribute \(+1\) to \(D\) for every such cut, while pairs \(i\le k<j\) with \(i\in B,j\in A\) contribute \(-1\). The numbers of such pairs are
\[
\alpha_k(n-\beta_k)\quad\text{and}\quad \beta_k(n-\alpha_k),
\]
respectively. Hence the cut \(k\) contributes
\[
\alpha_k(n-\beta_k)-\beta_k(n-\alpha_k)
= n(\alpha_k-\beta_k)=n d_k.
\]
Summing over all cuts gives
\[
D=\sum_{k=1}^{m-1} n d_k
= n\sum_{k=1}^{2n-1} d_k.
\]

But
\[
d_k=2\alpha_k-k\equiv k \pmod 2.
\]
Therefore
\[
\sum_{k=1}^{2n-1} d_k
\equiv \sum_{k=1}^{2n-1} k
= n(2n-1)
\equiv n \pmod 2.
\]
Since \(n=1011\) is odd, \(\sum_{k=1}^{2n-1} d_k\) is odd. Also \(n\) is odd, so
\[
D=n\sum_{k=1}^{2n-1} d_k
\]
is odd.

Thus \(D\) cannot be \(0\), because \(0\) is even. Hence
\[
T_+-T_-\neq 0,
\]
so
\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}.
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}
\]

Let
\[
X=\sum_{(a,b)\in S_{AB}}(b-a),\qquad Y=\sum_{(a,b)\in S_{BA}}(a-b),
\]
and define
\[
D=X-Y.
\]
We prove \(D\neq 0\).

Write \(2022=2m\), so \(m=1011\). For each \(i\), let
\[
\varepsilon_i=
\begin{cases}
1,& i\in A,\\
0,& i\in B.
\end{cases}
\]
For \(i<j\), the pair \(\{i,j\}\) contributes \(+(j-i)\) to \(D\) if \(i\in A,j\in B\), and \(-(j-i)\) if \(i\in B,j\in A\). Hence
\[
D=\sum_{1\le i<j\le 2m}(j-i)(\varepsilon_i-\varepsilon_j).
\]
Using \(j-i=\sum_{k=i}^{j-1}1\), we get
\[
D=\sum_{k=1}^{2m-1}\sum_{i\le k<j}(\varepsilon_i-\varepsilon_j).
\]
For fixed \(k\), let \(a_k=\sum_{i=1}^k\varepsilon_i\) be the number of elements of \(A\) among \(1,\dots,k\). Then
\[
\sum_{i\le k<j}(\varepsilon_i-\varepsilon_j)
=a_k(2m-k)-(m-a_k)k
=m(2a_k-k).
\]
Therefore
\[
D=m\sum_{k=1}^{2m-1}(2a_k-k).
\]
Since \(m=1011\) is odd,
\[
D\equiv \sum_{k=1}^{2m-1}(2a_k-k)\pmod 2.
\]
But
\[
\sum_{k=1}^{2m-1}(2a_k-k)
\equiv \sum_{k=1}^{2m-1}k
= \frac{(2m-1)(2m)}2
=m(2m-1)\pmod 2.
\]
Now \(m=1011\) is odd and \(2m-1=2021\) is odd, so
\[
m(2m-1)
\]
is odd. Thus \(D\) is odd. In particular, \(D\neq 0\). Hence \(X-Y\neq 0\), so
\[
X\neq Y.
\]

\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

Let \(n=1011\), and write
\[
T_A=\sum_{a\in A}a,\qquad T_B=\sum_{b\in B}b.
\]

First observe that every cross pair \((a,b)\in A\times B\) contributes exactly once to the expression
\[
\sum_{a\in A,\ b\in B}(b-a).
\]
For \(a<b\), this contributes \(b-a\), which is precisely the contribution in \(S_{AB}\).  
For \(b<a\), this contributes \(b-a=-(a-b)\), so its negative contribution gives exactly \(-(a-b)\), the contribution in \(S_{BA}\). Hence
\[
\sum_{(a,b)\in S_{AB}}(b-a)-\sum_{(a,b)\in S_{BA}}(a-b)
=
\sum_{a\in A,\ b\in B}(b-a).
\]

Now compute the right-hand side:
\[
\sum_{a\in A,\ b\in B}(b-a)
=
\sum_{b\in B} b\,|A|-\sum_{a\in A}a\,|B|.
\]
Since \(|A|=|B|=1011\), this becomes
\[
1011T_B-1011T_A=1011(T_B-T_A).
\]

On the other hand,
\[
T_A+T_B=1+2+\cdots+2022=\frac{2022\cdot 2023}{2}=1011\cdot 2023.
\]
Both \(1011\) and \(2023\) are odd, so \(1011\cdot 2023\) is odd. Therefore
\[
T_B-T_A=(T_A+T_B)-2T_A
\]
is odd, hence in particular nonzero. Thus
\[
\sum_{(a,b)\in S_{AB}}(b-a)-\sum_{(a,b)\in S_{BA}}(a-b)
=1011(T_B-T_A)\neq 0.
\]

Therefore the two sums cannot be equal.

\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

Let  
\[
L=\sum_{(a,b)\in S_{AB}}(b-a),\qquad R=\sum_{(a,b)\in S_{BA}}(a-b).
\]

For every ordered pair \((a,b)\in A\times B\):

- if \(a<b\), it contributes \(b-a\) to \(L\);
- if \(b<a\), it contributes \(a-b\) to \(R\), so it contributes \(-(a-b)=b-a\) to \(L-R\).

Thus every cross pair \((a,b)\in A\times B\) contributes \(b-a\) to \(L-R\), so
\[
L-R=\sum_{a\in A,\ b\in B}(b-a).
\]
Since \(|A|=|B|=1011\),
\[
\sum_{a\in A,\ b\in B}(b-a)
= |A|\sum_{b\in B} b-|B|\sum_{a\in A}a
=1011\left(\sum_{b\in B}b-\sum_{a\in A}a\right).
\]

Now
\[
\sum_{a\in A}a+\sum_{b\in B}b
=1+2+\cdots+2022
=\frac{2022\cdot 2023}{2}
=1011\cdot 2023,
\]
which is odd because both \(1011\) and \(2023\) are odd. Hence
\[
\sum_{b\in B}b-\sum_{a\in A}a
\]
is odd, and therefore
\[
L-R=1011\left(\sum_{b\in B}b-\sum_{a\in A}a\right)
\]
is odd. In particular, \(L-R\neq 0\).

Therefore \(L\neq R\), i.e.
\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b)}.
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

Let  
\[
L=\sum_{(a,b)\in S_{AB}}(b-a),\qquad R=\sum_{(a,b)\in S_{BA}}(a-b),
\]
and define
\[
D=L-R.
\]
We will prove \(D\ne 0\).

Let \(n=1011\), so the numbers are \(1,\dots,2n\). For \(0\le k\le 2n\), define
\[
A_k=\{i\le k:i\in A\},\qquad B_k=\{i\le k:i\in B\},
\]
and let
\[
a_k=|A_k|,\qquad b_k=|B_k|,\qquad y_k=a_k-b_k.
\]
Then \(y_0=y_{2n}=0\), and
\[
y_k-y_{k-1}=
\begin{cases}
1,&k\in A,\\
-1,&k\in B.
\end{cases}
\]
In particular,
\[
y_k=2a_k-k,
\]
so
\[
y_k\equiv k \pmod 2.
\]

Now consider a cross pair \(i<j\). If \(i\in A,j\in B\), it contributes \(+(j-i)\) to \(L\); if \(i\in B,j\in A\), it contributes \(-(j-i)\) to \(D=L-R\). Thus
\[
D=\sum_{\substack{i<j\\ i\in A,\ j\in B}}(j-i)
-\sum_{\substack{i<j\\ i\in B,\ j\in A}}(j-i).
\]
Writing \(j-i=\sum_{t=i}^{j-1}1\) and summing over \(t=1,\dots,2n-1\), for each fixed \(t\) we get
\[
D=\sum_{t=1}^{2n-1}\Bigl(a_t(n-b_t)-b_t(n-a_t)\Bigr).
\]
But
\[
a_t(n-b_t)-b_t(n-a_t)
= n(a_t-b_t)=ny_t.
\]
Hence
\[
D=n\sum_{t=1}^{2n-1} y_t.
\]

Now
\[
y_t\equiv t \pmod 2,
\]
so
\[
\sum_{t=1}^{2n-1} y_t
\equiv \sum_{t=1}^{2n-1} t
\equiv \#\{t\le 2n-1:t\text{ odd}\}
= n
\equiv 1 \pmod 2,
\]
because \(n=1011\) is odd. Therefore \(\sum_{t=1}^{2n-1} y_t\) is odd. Since \(n\) is also odd,
\[
D=n\sum_{t=1}^{2n-1} y_t
\]
is odd. In particular \(D\ne 0\).

Thus \(L-R\ne 0\), so
\[
\boxed{\sum_{(a,b)\in S_{AB}}(b-a)\ne \sum_{(a,b)\in S_{BA}}(a-b)}.
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

Let
\[
X=\sum_{(a,b)\in S_{AB}}(b-a),\qquad Y=\sum_{(a,b)\in S_{BA}}(a-b).
\]

For each ordered pair \((a,b)\in A\times B\):

- if \(a<b\), then \((a,b)\in S_{AB}\), so its contribution to \(X-Y\) is \(b-a\);
- if \(b<a\), then \((a,b)\in S_{BA}\), so its contribution to \(X-Y\) is \(-(a-b)=b-a\).

Thus every cross pair contributes \(b-a\) to \(X-Y\), so
\[
X-Y=\sum_{a\in A,\ b\in B}(b-a).
\]

Now compute:
\[
\sum_{a\in A,\ b\in B}(b-a)
= \sum_{b\in B}\sum_{a\in A} b-\sum_{a\in A}\sum_{b\in B} a
= |A|\sum_{b\in B}b-|B|\sum_{a\in A}a.
\]
Since \(|A|=|B|=1011\),
\[
X-Y=1011\left(\sum_{b\in B}b-\sum_{a\in A}a\right).
\]

Let
\[
\sigma_A=\sum_{a\in A}a,\qquad \sigma_B=\sum_{b\in B}b.
\]
Then
\[
X-Y=1011(\sigma_B-\sigma_A).
\]

But
\[
\sigma_A+\sigma_B=1+2+\cdots+2022=\frac{2022\cdot 2023}{2}=1011\cdot 2023,
\]
which is odd. Hence \(\sigma_A+\sigma_B\) is odd, so \(\sigma_A\neq \sigma_B\). Therefore
\[
X-Y=1011(\sigma_B-\sigma_A)\neq 0.
\]

Thus
\[
X\neq Y,
\]
which means
\[
\sum_{(a,b)\in S_{AB}}(b-a)\neq \sum_{(a,b)\in S_{BA}}(a-b).
\]

\[
\boxed{\text{Proved}}
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

Let  
\[
X=\sum_{(a,b)\in S_{AB}}(b-a),\qquad 
Y=\sum_{(a,b)\in S_{BA}}(a-b),
\]
and put \(\Delta=X-Y\). We will show \(\Delta\neq 0\).

Write \(n=2022=2m\), so \(m=1011\). For \(i=1,\dots,n\), define
\[
\varepsilon_i=
\begin{cases}
1,& i\in A,\\
0,& i\in B.
\end{cases}
\]
For \(i<j\), the contribution of the pair \((i,j)\) to \(\Delta\) is:
- \(j-i\) if \(i\in A,j\in B\);
- \(-(j-i)\) if \(i\in B,j\in A\);
- \(0\) otherwise.

Thus
\[
\Delta=\sum_{1\le i<j\le n}(j-i)(\varepsilon_i-\varepsilon_j).
\]

Now expand:
\[
\Delta=\sum_{i<j}(j-i)\varepsilon_i-\sum_{i<j}(j-i)\varepsilon_j.
\]
For fixed \(i\), the first sum contains \(\varepsilon_i\) with coefficient
\[
C_i=\sum_{j=i+1}^{2m}(j-i),
\]
while the second sum contains \(\varepsilon_i\) with coefficient
\[
D_i=\sum_{j=1}^{i-1}(i-j).
\]
Hence
\[
\Delta=\sum_{i=1}^{2m}\varepsilon_i(C_i-D_i).
\]
Since \(\varepsilon_i=1\) exactly for \(i\in A\),
\[
\Delta=\sum_{i\in A}(C_i-D_i).
\]

Now compute:
\[
C_i=\frac{(2m-i)(2m-i+1)}2,\qquad
D_i=\frac{i(i-1)}2.
\]
Therefore
\[
C_i-D_i
=\frac{(2m-i)(2m-i+1)-i(i-1)}2
=m(2m+1-2i).
\]
So
\[
\Delta=m\sum_{i\in A}(2m+1-2i).
\]

For every \(i\), the number \(2m+1-2i\) is odd. Since \(|A|=m=1011\) is odd, the sum
\[
R=\sum_{i\in A}(2m+1-2i)
\]
is a sum of an odd number of odd integers, hence \(R\) is odd. Therefore
\[
\Delta=1011R
\]
is odd. In particular \(\Delta\neq 0\), so \(X\neq Y\).

\[
\boxed{X\neq Y}
\]

</details>
