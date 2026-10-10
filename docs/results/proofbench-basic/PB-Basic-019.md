# PB-Basic-019

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

For any positive integer $n$, let $\delta(n)$ be the largest odd divisor of $n$. Prove for any $N>0$ that we have
 \[
 \left| \sum_{n=1}^N \frac{\delta(n)}{n}- \frac{2}{3}N \right| <1.
 \]

## Swarm: accepted (best candidate `P4`; self-verification grades [7, 7, 7]; 346,748 tokens in 48 calls)

**Blind grade: Correct (7/7).** Valid derivation of E_{2m}=E_m/2 and E_{2m+1}=E_m/2+1/3 followed by a correct strong induction from E_1=1/3 showing |E_N|<5/6<1 for all N>=1; complete and rigorous.

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}{n},\qquad E_N=S_N-\frac23N.
\]
We prove \(|E_N|<1\) for every \(N\ge 1\).

First observe that if \(m=2^a u\) with \(u\) odd, then \(\delta(m)=u\). Hence
\[
\delta(2m)=\delta(m),
\]
so
\[
\frac{\delta(2m)}{2m}=\frac12\frac{\delta(m)}{m}.
\]
Also every odd \(n\le N\) contributes \(\delta(n)/n=1\), and there are \(\lceil N/2\rceil\) such integers. Therefore
\[
S_N=\left\lceil \frac N2\right\rceil+\frac12 S_{\lfloor N/2\rfloor}.
\]

Now derive recurrences for \(E_N\).

If \(N=2m\), then
\[
E_{2m}
= S_{2m}-\frac{4m}{3}
= m+\frac12S_m-\frac{4m}{3}
= \frac12\left(S_m-\frac{2m}{3}\right)
= \frac12E_m.
\]

If \(N=2m+1\), then
\[
E_{2m+1}
= S_{2m+1}-\frac{4m+2}{3}
= m+1+\frac12S_m-\frac{4m+2}{3}
= \frac12E_m+\frac13.
\]

We prove \(|E_N|<1\) by induction on \(N\).

For \(N=1\),
\[
E_1=1-\frac23=\frac13<1.
\]

Assume \(|E_k|<1\) for all \(k<N\).

- If \(N=2m\), then
\[
|E_N|=\frac12|E_m|<\frac12<1.
\]

- If \(N=2m+1\), then
\[
|E_N|=\left|\frac12E_m+\frac13\right|
\le \frac12|E_m|+\frac13
< \frac12+\frac13=\frac56<1.
\]

Thus by induction \(|E_N|<1\) for every \(N\ge 1\). Hence
\[
\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|<1.
\]

\[
\boxed{\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac{2}{3}N\right|<1}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 20,778 | Correct (7/7) | Derives A_{2M}=A_M/2 and A_{2M+1}=A_M/2+1/3, proves by induction the exact formula A_N=(1/3)sum b_i 2^{-i} (harmless typo A_1=F(1) for F(1)/3), and bounds it strictly between 0 and 2/3, which is complete. |
| A2 | stop | 17,033 | Correct (7/7) | Correctly derives E_{2M}=E_M/2 and E_{2M+1}=1/3+E_M/2, obtains E_N=(1/3)*sum eps_i 2^{-i} by a direct induction on binary digits, and bounds it strictly between 0 and 2/3, completing the proof. |
| A3 | stop | 10,636 | Correct (7/7) | Correctly derives E_{2N}=E_N/2 and E_{2K+1}=E_K/2+1/3 from delta(2m)=delta(m) and closes with a valid strong induction from E_0=0 giving \|E_N\|<5/6, a complete and rigorous alternative to the reference. |
| A4 | stop | 10,584 | Correct (7/7) | Correctly derives S_{2N}=S_N/2+N, S_{2N+1}=S_N/2+N+1, hence E_{2N}=E_N/2 and E_{2N+1}=E_N/2+1/3, and a valid strong induction from E_1=1/3 shows -1/6<E_N<5/6, which is complete. |
| A5 | stop | 11,458 | Correct (7/7) | Valid recurrence F(N)=ceil(N/2)+F(floor(N/2))/2 leading to E_{2q}=E_q/2, E_{2q+1}=E_q/2+1/3 with correct algebra and a clean strong induction from E_0=0 yielding \|E_N\|<5/6, which is complete. |
| A6 | stop | 19,834 | Correct (7/7) | Writes delta(n)/n=2^{-v_2(n)}, counts terms via floor(N/2^k), telescopes and evaluates the double sum through the binary digits to obtain the exact identity S_N-2N/3=(eps_0+B)/3 in [0,2/3), with every computation checking out. |
| A7 | stop | 21,652 | Correct (7/7) | Correctly derives E_{2q}=E_q/2 and E_{2q+1}=1/3+E_q/2, rigorously identifies E_N=F(N)/3 with F(N)=sum b_j 2^{-j} since both satisfy the same recurrence with value 0 at N=0, and concludes 0<E_N<2/3<1. |
| A8 | stop | 7,889 | Correct (7/7) | Correctly derives F_{2M}=F_M/2 and F_{2M+1}=F_M/2+1/3 with F_0=0 and gives a valid strong induction showing \|F_N\|<1 (indeed at most 5/6) for all N, a complete and rigorous proof. |
| A9 | stop | 18,314 | Correct (7/7) | Correctly derives E_{2q}=E_q/2 and E_{2q+1}=E_q/2+1/3 and the exact formula E_N=(1/3)*sum b_i 2^{-i}; the verbal description of the inductive step is slightly loose but the induction is routine and matches the correctly stated recurrence, giving 0<=E_N<2/3<1. |
| A10 | stop | 14,214 | Correct (7/7) | Correctly derives S_{2m}=m+S_m/2 and S_{2m+1}=m+1+S_m/2, hence A_{2m}=A_m/2 and A_{2m+1}=A_m/2+1/3, proves by induction the exact formula A_N=(1/3)*sum b_k 2^{-k} over the binary digits of N, and concludes 0<A_N<2/3<1. |
| A11 | stop | 15,932 | Correct (7/7) | Correct recurrences R(2q)=R(q)/2, R(2q+1)=1/3+R(q)/2 and a correct closed form R(N)=(1/3)sum b_i 2^{-i} checked against the recurrence (brief, with a harmless 'leading' vs trailing-digit wording slip), giving 0<=R(N)<2/3, which is complete. |
| A12 | stop | 8,932 | Correct (7/7) | Correct recurrences E_{2M}=E_M/2, E_{2M+1}=E_M/2+1/3 for M>=1 and a valid strong induction from E_1=1/3 proving 0<E_N<5/6 for all N>=1, which is complete. |
| A13 | stop | 17,780 | Correct (7/7) | Derives the correct recurrence A(N)=A(floor(N/2))/2+(N mod 2)/3 from delta(2m)=delta(m), unrolls it to the exact binary-digit formula A(N)=(1/3)*sum eps_j 2^{-j} with an adequate inductive justification, and bounds it in [0,2/3), giving a complete proof. |
| A14 | stop | 17,117 | Correct (7/7) | Correctly derives T_{2M}=T_M/2 and T_{2M+1}=T_M/2+1/3 and proves 0<=T_N<2/3 by a valid strong induction from T_0=0, which is complete and rigorous. |
| A15 | stop | 12,646 | Correct (7/7) | Correct recurrences E(2q)=E(q)/2 and E(2q+1)=1/3+E(q)/2 and a valid strong induction from E(1)=1/3 proving the sharper bound 0<E(N)<2/3, which yields the result. |
| A16 | stop | 16,413 | Correct (7/7) | Correct recurrences T_{2M}=T_M/2, T_{2M+1}=1/3+T_M/2 and the correct closed form T_N=(1/3)sum b_i/2^i (its induction only indicated but entirely routine from the recurrences), giving 0<T_N<2/3, which is complete. |

<details><summary>A1: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}n,\qquad A_N=S_N-\frac23N.
\]
We prove \(|A_N|<1\).

First note that for every \(m\ge1\),
\[
\delta(2m)=\delta(m),
\]
because multiplying by \(2\) only adds one factor of \(2\) to the odd part. Also every odd \(n\le N\) contributes exactly \(1\), since \(\delta(n)=n\).

Thus, splitting the sum into odd and even \(n\)'s,
\[
S_N=O_N+\frac12S_{\lfloor N/2\rfloor},
\]
where \(O_N\) is the number of odd integers \(\le N\), namely
\[
O_{2M}=M,\qquad O_{2M+1}=M+1.
\]

Define \(S_0=0\). Then for \(M\ge1\),
\[
S_{2M}=M+\frac12S_M,\qquad S_{2M+1}=M+1+\frac12S_M.
\]
Subtracting \(\frac23N\) gives
\[
A_{2M}=\frac12A_M,
\]
and
\[
A_{2M+1}=\frac12A_M+\frac13.
\]

Now write \(N\) in binary:
\[
N=(b_\ell b_{\ell-1}\cdots b_0)_2,\qquad b_i\in\{0,1\},\ b_\ell=1.
\]
Set
\[
F(N)=\sum_{i=0}^\ell b_i2^{-i}.
\]
We claim that
\[
A_N=\frac{F(N)}3.
\]
Indeed, \(A_1=1-\frac23=\frac13=F(1)\). If \(N=2M\), then \(F(N)=\frac12F(M)\), and the recurrence gives \(A_N=\frac12A_M=\frac{F(M)}6=\frac{F(N)}3\). Similarly, if \(N=2M+1\), then \(F(N)=1+\frac12F(M)\), and
\[
A_N=\frac12A_M+\frac13
=\frac{F(M)}6+\frac13
=\frac{1+\frac12F(M)}3
=\frac{F(N)}3.
\]

Therefore
\[
0<A_N=\frac{F(N)}3.
\]
But
\[
F(N)=\sum_{i=0}^\ell b_i2^{-i}\le \sum_{i=0}^\ell 2^{-i}
=2-\frac1{2^\ell}<2.
\]
Hence
\[
0<A_N<\frac23<1.
\]

So
\[
\left|S_N-\frac23N\right|=|A_N|<1.
\]

\[
\boxed{\left| \sum_{n=1}^N \frac{\delta(n)}{n}-\frac{2}{3}N \right|<1}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

Let  
\[
a_n=\frac{\delta(n)}{n},\qquad S_N=\sum_{n=1}^N a_n.
\]
We will prove that
\[
E_N:=S_N-\frac23N
\]
satisfies \(0<E_N<\frac23<1\).

First note that if \(n=2m\), then \(\delta(2m)=\delta(m)\), so
\[
a_{2m}=\frac{\delta(m)}{2m}=\frac12 a_m.
\]
Thus odd terms contribute \(1\) each, and even terms contribute half the corresponding previous term.

For \(M\ge 0\),
\[
S_{2M}=M+\frac12S_M,
\]
because among \(1,\dots,2M\) there are \(M\) odd numbers, each contributing \(1\), and the \(M\) even numbers \(2,4,\dots,2M\) contribute \(\frac12S_M\).

Similarly,
\[
S_{2M+1}=M+1+\frac12S_M.
\]

Now define \(E_N=S_N-\frac23N\). Then
\[
E_{2M}=S_{2M}-\frac43M
=M+\frac12S_M-\frac43M
=\frac12\left(S_M-\frac{2M}{3}\right)
=\frac12E_M.
\]
Also,
\[
E_{2M+1}=S_{2M+1}-\frac{4M+2}{3}
=M+1+\frac12S_M-\frac{4M+2}{3}
=\frac13+\frac12E_M.
\]

We now use binary expansions. Write
\[
N=\sum_{i=0}^L \varepsilon_i2^i,\qquad \varepsilon_i\in\{0,1\},\ \varepsilon_L=1.
\]
A direct induction from the recurrences above gives
\[
E_N=\frac13\sum_{i=0}^L \varepsilon_i2^{-i}.
\]
Indeed, shifting binary digits left corresponds to halving the sum, and adding a final \(1\) in the units place adds \(1/3\).

Since only finitely many \(\varepsilon_i\) are nonzero,
\[
\sum_{i=0}^L \varepsilon_i2^{-i}
\le \sum_{i=0}^L 2^{-i}
=2-2^{-L}<2.
\]
Therefore
\[
0<E_N=\frac13\sum_{i=0}^L \varepsilon_i2^{-i}<\frac23<1.
\]
Hence
\[
\left|S_N-\frac23N\right|=E_N<1.
\]

Thus
\[
\boxed{
\left| \sum_{n=1}^N \frac{\delta(n)}{n}-\frac{2}{3}N \right|<1
}
\]
for every positive integer \(N\).

</details>

<details><summary>A3: Correct (7/7)</summary>

Let  
\[
a_n=\frac{\delta(n)}{n}.
\]
For odd \(n\), \(\delta(n)=n\), so \(a_n=1\). Also, if \(n=2m\), then \(\delta(2m)=\delta(m)\), hence
\[
a_{2m}=\frac{\delta(2m)}{2m}=\frac{\delta(m)}{2m}=\frac12 a_m.
\]

Define
\[
S_N=\sum_{n=1}^N a_n,\qquad E_N=S_N-\frac23N.
\]
We prove by induction that \(|E_N|<1\) for every \(N\ge 0\).

First,
\[
S_{2N}
=\sum_{m=1}^N a_{2m-1}+\sum_{m=1}^N a_{2m}
=N+\frac12\sum_{m=1}^N a_m
=N+\frac12S_N.
\]
Therefore
\[
E_{2N}=S_{2N}-\frac43N
=N+\frac12S_N-\frac43N
=\frac12S_N-\frac13N
=\frac12E_N.
\]

Now if \(N=2K+1\), then \(a_{2K+1}=1\), so
\[
E_{2K+1}=S_{2K+1}-\frac{2(2K+1)}3
=S_{2K}+1-\frac{4K+2}{3}.
\]
Using \(S_{2K}=E_{2K}+\frac{4K}{3}=\frac12E_K+\frac{4K}{3}\), we get
\[
E_{2K+1}
=\frac12E_K+\frac13.
\]

We now prove \(|E_N|<1\) by strong induction. For \(N=0\), \(E_0=0\). Assume \(|E_j|<1\) for all \(j<N\).

- If \(N=2K\), then
\[
|E_N|=\frac12|E_K|<\frac12<1.
\]
- If \(N=2K+1\), then
\[
|E_N|=\left|\frac12E_K+\frac13\right|
\leq \frac12|E_K|+\frac13
<\frac12+\frac13=\frac56<1.
\]

Thus \(|E_N|<1\) for all \(N\ge 0\). In particular, for every positive integer \(N\),
\[
\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|
=|E_N|<1.
\]

\[
\boxed{\left| \sum_{n=1}^N \frac{\delta(n)}{n}-\frac{2}{3}N \right|<1}
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}{n},\qquad E_N=S_N-\frac23N.
\]
We need to prove \(|E_N|<1\) for every \(N\ge1\).

For every positive integer \(k\), multiplying by \(2\) does not change the odd part of \(k\), so
\[
\delta(2k)=\delta(k).
\]
Hence
\[
\frac{\delta(2k)}{2k}=\frac{\delta(k)}{2k}.
\]
Also, for every odd \(2k-1\),
\[
\delta(2k-1)=2k-1,
\]
so
\[
\frac{\delta(2k-1)}{2k-1}=1.
\]

Now split \(S_{2N}\) into even and odd terms:
\[
S_{2N}
=\sum_{k=1}^N \frac{\delta(2k)}{2k}
+\sum_{k=1}^N \frac{\delta(2k-1)}{2k-1}.
\]
The first sum is \(\frac12S_N\), and the second sum is \(N\). Therefore
\[
S_{2N}=\frac12S_N+N.
\]
Similarly,
\[
S_{2N+1}=S_{2N}+1=\frac12S_N+N+1.
\]

Define \(E_N=S_N-\frac23N\). Using the recurrences above,
\[
E_{2N}
=\frac12S_N+N-\frac43N
=\frac12S_N-\frac N3
=\frac12\left(S_N-\frac23N\right)
=\frac12E_N.
\]
Also,
\[
E_{2N+1}
=\frac12S_N+N+1-\frac{2(2N+1)}3
=\frac12S_N-\frac N3+\frac13
=\frac12E_N+\frac13.
\]

Now we prove by strong induction that \(|E_N|<1\).

For \(N=1\),
\[
E_1=\frac{\delta(1)}1-\frac23=1-\frac23=\frac13,
\]
so \(|E_1|<1\).

Assume \(|E_k|<1\) for all \(k<N\). If \(N=2M\), then \(M<N\), and
\[
|E_N|=|E_{2M}|=\frac12|E_M|<\frac12<1.
\]
If \(N=2M+1\), then by the induction hypothesis \(-1<E_M<1\), so
\[
E_N=E_{2M+1}=\frac12E_M+\frac13.
\]
Thus
\[
-\frac16<\frac12E_M+\frac13<\frac56,
\]
so certainly
\[
-1<E_N<1.
\]

Therefore \(|E_N|<1\) for every \(N\ge1\). Since \(E_N\) is exactly
\[
\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N,
\]
we obtain
\[
\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|<1.
\]

\[
\boxed{\text{Proved}}
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

Let  
\[
F(N)=\sum_{n=1}^N \frac{\delta(n)}{n},\qquad F(0)=0.
\]
We will prove the stronger statement
\[
|F(N)-\tfrac23N|<1 \qquad (N\ge 0).
\]

For every \(m\ge 1\), \(\delta(2m)=\delta(m)\), since removing a factor of \(2\) does not change the largest odd divisor. Hence for even \(n=2m\),
\[
\frac{\delta(2m)}{2m}=\frac{\delta(m)}{2m}
=\frac12\frac{\delta(m)}{m}.
\]
Also, if \(n\) is odd, then \(\delta(n)=n\), so \(\delta(n)/n=1\).

Therefore
\[
F(N)=\#\{1\le n\le N:n\text{ odd}\}+\frac12F\!\left(\left\lfloor \frac N2\right\rfloor\right)
=\left\lceil \frac N2\right\rceil+\frac12F\!\left(\left\lfloor \frac N2\right\rfloor\right).
\]

Define
\[
E_N=F(N)-\frac23N.
\]
We will show \(|E_N|<1\).

If \(N=2q\), then \(\lceil N/2\rceil=q\), and
\[
E_{2q}=q+\frac12F(q)-\frac{4q}{3}
=\frac12F(q)-\frac q3
=\frac12\left(F(q)-\frac{2q}{3}\right)
=\frac12E_q.
\]
If \(N=2q+1\), then \(\lceil N/2\rceil=q+1\), and
\[
E_{2q+1}=q+1+\frac12F(q)-\frac{4q+2}{3}
=\frac12E_q+\frac13.
\]

Now prove by strong induction that \(|E_N|<1\) for all \(N\ge 0\). The case \(N=0\) is clear since \(E_0=0\).

Assume \(|E_k|<1\) for all \(k<N\).

- If \(N=2q\), then
\[
|E_N|=\frac12|E_q|<\frac12<1.
\]
- If \(N=2q+1\), then
\[
|E_N|=\left|\frac12E_q+\frac13\right|
\le \frac12|E_q|+\frac13
< \frac12+\frac13=\frac56<1.
\]

Thus \(|E_N|<1\) for every \(N\ge 0\). In particular,
\[
\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|
=|E_N|<1.
\]

\[
\boxed{\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|<1}
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}{n}.
\]
For each \(n\), write uniquely \(n=2^{v_2(n)}q\) with \(q\) odd. Then \(\delta(n)=q\), so
\[
\frac{\delta(n)}n=\frac1{2^{v_2(n)}}.
\]

Set \(c_k=\left\lfloor \frac N{2^k}\right\rfloor\). The integers \(n\le N\) with \(v_2(n)=k\) are exactly those divisible by \(2^k\) but not by \(2^{k+1}\), so their number is \(c_k-c_{k+1}\). Hence
\[
S_N=\sum_{k=0}^m 2^{-k}(c_k-c_{k+1}),
\]
where \(m\) is such that \(2^m\le N<2^{m+1}\). Telescoping gives
\[
S_N=N-\sum_{k=1}^m \frac{c_k}{2^k}.
\]

Now write the binary expansion
\[
N=\sum_{i=0}^m \varepsilon_i2^i,\qquad \varepsilon_i\in\{0,1\}.
\]
For \(k\ge1\),
\[
c_k=\left\lfloor \frac N{2^k}\right\rfloor
=\sum_{i=k}^m \varepsilon_i2^{i-k}.
\]
Therefore
\[
\sum_{k=1}^m \frac{c_k}{2^k}
=\sum_{i=1}^m \varepsilon_i\sum_{k=1}^i2^{i-2k}.
\]
The inner sum is geometric:
\[
\sum_{k=1}^i2^{i-2k}
=2^i\sum_{k=1}^i4^{-k}
=\frac{2^i}{3}-\frac{2^{-i}}{3}.
\]
Thus
\[
\sum_{k=1}^m \frac{c_k}{2^k}
=\frac13\sum_{i=1}^m\varepsilon_i2^i-\frac13\sum_{i=1}^m\varepsilon_i2^{-i}.
\]
Since \(\sum_{i=1}^m\varepsilon_i2^i=N-\varepsilon_0\), where \(\varepsilon_0\in\{0,1\}\), we get
\[
\sum_{k=1}^m \frac{c_k}{2^k}
=\frac{N-\varepsilon_0}{3}-\frac{B}{3},
\]
where
\[
B=\sum_{i=1}^m\varepsilon_i2^{-i}.
\]
Hence
\[
S_N=N-\frac{N-\varepsilon_0}{3}+\frac{B}{3}
=\frac{2N+\varepsilon_0}{3}+\frac{B}{3}.
\]
So
\[
S_N-\frac{2N}{3}
=\frac{\varepsilon_0+B}{3}\ge 0.
\]

Now bound \(\varepsilon_0+B\). Since \(\varepsilon_0\le1\) and
\[
B=\sum_{i=1}^m\varepsilon_i2^{-i}
\le \sum_{i=1}^m2^{-i}<1,
\]
we have
\[
\varepsilon_0+B<2.
\]
Therefore
\[
0\le S_N-\frac{2N}{3}<\frac23<1.
\]
Taking absolute values gives
\[
\left|S_N-\frac{2N}{3}\right|<1.
\]

Thus
\[
\boxed{\left| \sum_{n=1}^N \frac{\delta(n)}{n}-\frac{2}{3}N\right|<1}
\]
for every positive integer \(N\).

</details>

<details><summary>A7: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}{n}.
\]

For odd \(n\), \(\delta(n)=n\), so \(\delta(n)/n=1\).  
For even \(n=2m\), we have \(\delta(2m)=\delta(m)\), hence
\[
\frac{\delta(2m)}{2m}=\frac12\frac{\delta(m)}{m}.
\]
Therefore
\[
S_N=\left\lceil \frac N2\right\rceil+\frac12 S_{\lfloor N/2\rfloor}.
\]

Define
\[
E_N=S_N-\frac23N,\qquad E_0=0.
\]
Using the recurrence above,
\[
E_N=\left\lceil \frac N2\right\rceil+\frac13\left\lfloor \frac N2\right\rfloor-\frac{2N}{3}
+\frac12 E_{\lfloor N/2\rfloor}.
\]
If \(N=2q\), this gives
\[
E_{2q}=\frac12 E_q.
\]
If \(N=2q+1\), it gives
\[
E_{2q+1}=\frac13+\frac12 E_q.
\]

Now write the binary expansion
\[
N=\sum_{j=0}^L b_j2^j,\qquad b_j\in\{0,1\},
\]
and define
\[
F(N)=\sum_{j=0}^L b_j2^{-j}.
\]
Then \(F(0)=0\), and shifting binary digits gives
\[
F(2q)=\frac12F(q),\qquad F(2q+1)=1+\frac12F(q).
\]
Thus \(G_N=F(N)/3\) satisfies exactly the same recurrences as \(E_N\), with \(G_0=0\). By induction on \(N\),
\[
E_N=\frac{F(N)}3.
\]

For \(N\ge1\), \(F(N)>0\), and
\[
F(N)=\sum_{j=0}^L b_j2^{-j}
\le \sum_{j=0}^L 2^{-j}
<2.
\]
Hence
\[
0<E_N=\frac{F(N)}3<\frac23<1.
\]
Therefore
\[
\left|S_N-\frac23N\right|=E_N<1.
\]

\[
\boxed{\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|<1}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}{n},\qquad S_0=0,
\]
and define
\[
F_N=S_N-\frac23N.
\]
We prove \(|F_N|<1\) for every \(N\ge 0\).

First note that if \(m=2^r q\) with \(q\) odd, then \(2m=2^{r+1}q\), so
\[
\delta(2m)=\delta(m)=q.
\]
Hence
\[
\frac{\delta(2m)}{2m}=\frac12\frac{\delta(m)}{m}.
\]

Now split \(S_N\) into odd and even terms. For \(N=2M\), the odd numbers are \(1,3,\dots,2M-1\), so there are \(M\) of them, each contributing \(1\). The even terms give
\[
\sum_{m=1}^M \frac{\delta(2m)}{2m}
=\frac12\sum_{m=1}^M \frac{\delta(m)}{m}
=\frac12 S_M.
\]
Thus
\[
S_{2M}=M+\frac12S_M.
\]
Similarly,
\[
S_{2M+1}=M+1+\frac12S_M.
\]

Now compute \(F_N\). For \(N=2M\),
\[
F_{2M}=S_{2M}-\frac23(2M)
=M+\frac12S_M-\frac43M
=\frac12S_M-\frac M3
=\frac12F_M.
\]
For \(N=2M+1\),
\[
F_{2M+1}=M+1+\frac12S_M-\frac23(2M+1)
=\frac12S_M-\frac M3+\frac13
=\frac12F_M+\frac13.
\]

We now prove by induction on \(N\ge 0\) that \(|F_N|<1\). The base case \(N=0\) gives \(F_0=0\). Suppose \(|F_M|<1\) for all \(M<N\). If \(N=2M\), then
\[
|F_N|=\frac12|F_M|<\frac12<1.
\]
If \(N=2M+1\), then
\[
|F_N|=\left|\frac12F_M+\frac13\right|
\le \frac12|F_M|+\frac13
< \frac12+\frac13=\frac56<1.
\]
Therefore \(|F_N|<1\) for all \(N\ge 0\), in particular for all \(N>0\).

Since
\[
F_N=S_N-\frac23N,
\]
we obtain
\[
\left|S_N-\frac23N\right|<1,
\]
as required.

\[
\boxed{\left| \sum_{n=1}^N \frac{\delta(n)}{n}- \frac{2}{3}N \right|<1}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}{n},\qquad S_0=0,
\]
and define
\[
E_N=S_N-\frac{2N}{3}.
\]
We will prove \(0\le E_N<1\), which gives the desired inequality.

For odd \(n\), \(\delta(n)=n\), so \(\delta(n)/n=1\). Also \(\delta(2m)=\delta(m)\). Hence
\[
S_N=\#\{1\le n\le N:n\text{ odd}\}+\frac12S_{\lfloor N/2\rfloor}
=\left\lceil \frac N2\right\rceil+\frac12S_{\lfloor N/2\rfloor}.
\]

Now compute \(E_N\) according as \(N\) is even or odd.

If \(N=2q\), then
\[
E_{2q}=S_{2q}-\frac{4q}{3}
=q+\frac12S_q-\frac{4q}{3}
=\frac12\left(S_q-\frac{2q}{3}\right)
=\frac12E_q.
\]

If \(N=2q+1\), then
\[
E_{2q+1}=S_{2q+1}-\frac{4q+2}{3}
=q+1+\frac12S_q-\frac{4q+2}{3}
=\frac12E_q+\frac13.
\]

Now write \(N\) in binary:
\[
N=\sum_{i=0}^r b_i2^i,\qquad b_i\in\{0,1\}.
\]
The recurrence above shows by induction that
\[
E_N=\frac13\sum_{i=0}^r b_i2^{-i}.
\]
Indeed, appending a binary digit \(0\) corresponds to halving, and appending a binary digit \(1\) adds \(1/3\), exactly matching the recurrence.

Therefore
\[
0\le E_N
=\frac13\sum_{i=0}^r b_i2^{-i}
\le \frac13\sum_{i=0}^r2^{-i}
< \frac13\sum_{i=0}^{\infty}2^{-i}
=\frac13\cdot 2
=\frac23<1.
\]

Thus for every \(N>0\),
\[
\left|S_N-\frac{2N}{3}\right|=E_N<1.
\]

So
\[
\boxed{\left| \sum_{n=1}^N \frac{\delta(n)}{n}-\frac{2}{3}N\right|<1}
\]
holds for all positive integers \(N\).

</details>

<details><summary>A10: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}{n},\qquad A_N=S_N-\frac23N.
\]
We will prove \(0<A_N<\frac23\), hence \(|A_N|<1\).

For \(m\ge 1\), write \(m=2^a q\) with \(q\) odd. Then \(\delta(m)=q\) and \(\delta(2m)=q\), so
\[
\frac{\delta(2m)}{2m}=\frac{\delta(m)}{2m}
=\frac12\frac{\delta(m)}m.
\]

Now split the sum according to parity. There are exactly \(m\) odd numbers among \(1,\dots,2m\), each contributing \(1\), and
\[
\sum_{j=1}^m \frac{\delta(2j)}{2j}
=\frac12\sum_{j=1}^m \frac{\delta(j)}j
=\frac12 S_m.
\]
Thus
\[
S_{2m}=m+\frac12 S_m.
\]
Also, since \(2m+1\) is odd,
\[
S_{2m+1}=S_{2m}+1=m+1+\frac12S_m.
\]

Define \(A_N=S_N-\frac23N\). Then
\[
A_{2m}=m+\frac12S_m-\frac43m
=\frac12S_m-\frac m3
=\frac12\left(S_m-\frac{2m}{3}\right)
=\frac12A_m,
\]
and
\[
A_{2m+1}=m+1+\frac12S_m-\frac{2(2m+1)}3
=\frac12S_m-\frac m3+\frac13
=\frac12A_m+\frac13.
\]

Now write \(N\) in binary:
\[
N=\sum_{k=0}^L b_k2^k,\qquad b_k\in\{0,1\}.
\]
We claim
\[
A_N=\frac13\sum_{k=0}^L b_k2^{-k}.
\]
It is true for \(N=1\), where \(A_1=1-\frac23=\frac13\). For \(N=2m\), the binary digits of \(N\) are the digits of \(m\) shifted left, so the formula gives \(A_N=A_m/2\), matching the recurrence. For \(N=2m+1\), the least significant bit is \(1\), and again the formula reduces to the same recurrence. Hence the claim follows by induction on \(N\).

Therefore, with \(B_N=\sum_{k=0}^L b_k2^{-k}\),
\[
A_N=\frac{B_N}{3}.
\]
Since \(B_N>0\) and
\[
B_N\le \sum_{k=0}^L2^{-k}<2,
\]
we get
\[
0<A_N<\frac23<1.
\]
Thus
\[
|A_N|<1,
\]
which is exactly
\[
\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|<1.
\]

\[
\boxed{\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|<1}
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

Let  
\[
S(N)=\sum_{n=1}^N \frac{\delta(n)}n,\qquad S(0)=0.
\]
We prove
\[
\left|S(N)-\frac23N\right|<1.
\]

First note that if \(m=2^a u\) with \(u\) odd, then \(\delta(m)=u\). Hence
\[
\delta(2m)=\delta(m),
\]
so for even \(n=2m\),
\[
\frac{\delta(2m)}{2m}=\frac12\frac{\delta(m)}m.
\]
Also every odd \(n\) contributes \(1\). Therefore
\[
S(N)=\left\lceil \frac N2\right\rceil+\frac12 S\left(\left\lfloor \frac N2\right\rfloor\right). \tag{1}
\]

Define
\[
R(N)=S(N)-\frac23N.
\]
Then \(R(0)=0\). Using (1),

- if \(N=2q\),
\[
R(2q)=q+\frac12S(q)-\frac{4q}{3}
=\frac12\left(S(q)-\frac{2q}{3}\right)
=\frac12R(q),
\]
- if \(N=2q+1\),
\[
R(2q+1)=q+1+\frac12S(q)-\frac{4q+2}{3}
=\frac13+\frac12R(q).
\]
Thus
\[
R(2q)=\frac12R(q),\qquad R(2q+1)=\frac13+\frac12R(q). \tag{2}
\]

Now write the binary expansion
\[
N=\sum_{i=0}^r b_i2^i,\qquad b_i\in\{0,1\}.
\]
Using (2), each time a binary digit \(1\) is removed, it contributes \(1/3\), and every later contribution is divided by \(2\) for each subsequent digit. Hence
\[
R(N)=\frac13\sum_{i=0}^r b_i2^{-i}. \tag{3}
\]
Indeed, for \(N=2q\), the binary digits of \(N\) are those of \(q\) shifted left, so (2) matches the formula; for \(N=2q+1\), an extra leading \(1\) appears, giving the extra \(1/3\).

Now
\[
0\le \sum_{i=0}^r b_i2^{-i}
\le \sum_{i=0}^r 2^{-i}
=2-2^{-r}<2.
\]
Therefore, from (3),
\[
0\le R(N)<\frac23<1.
\]
So
\[
\left|S(N)-\frac23N\right|=|R(N)|=R(N)<1.
\]

\[
\boxed{\left|\sum_{n=1}^N \frac{\delta(n)}n-\frac23N\right|<1}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}{n}.
\]
We want to show
\[
\left|S_N-\frac23N\right|<1.
\]

Define
\[
E_N=S_N-\frac23N.
\]
We will prove \(0<E_N<1\) for every \(N\ge 1\).

First note that if \(n=2m\), then the odd part of \(2m\) is the same as the odd part of \(m\), so
\[
\delta(2m)=\delta(m).
\]
Hence
\[
\frac{\delta(2m)}{2m}=\frac12\cdot \frac{\delta(m)}m.
\]
Also, if \(n\) is odd, then \(\delta(n)=n\), so \(\delta(n)/n=1\).

Now split \(S_N\) into odd and even terms.

For \(M\ge 1\),
\[
S_{2M}
=\sum_{\substack{1\le n\le 2M\\ n\text{ odd}}}1
+\sum_{m=1}^M \frac{\delta(2m)}{2m}
=M+\frac12 S_M.
\]
Similarly,
\[
S_{2M+1}=S_{2M}+1=M+1+\frac12 S_M.
\]

Now compute \(E_N\) from these recurrences.

For \(N=2M\),
\[
E_{2M}
=S_{2M}-\frac{4M}{3}
=M+\frac12S_M-\frac{4M}{3}
=\frac12S_M-\frac M3.
\]
Since \(S_M=E_M+\frac23M\),
\[
E_{2M}
=\frac12\left(E_M+\frac23M\right)-\frac M3
=\frac12E_M.
\]

For \(N=2M+1\),
\[
E_{2M+1}
=S_{2M+1}-\frac{2(2M+1)}3
=M+1+\frac12S_M-\frac{4M+2}{3}.
\]
Again using \(S_M=E_M+\frac23M\),
\[
E_{2M+1}
=\frac12E_M+\frac13.
\]

We now prove by induction that \(0<E_N<1\) for all \(N\ge 1\).

Base case: \(N=1\),
\[
E_1=S_1-\frac23=1-\frac23=\frac13,
\]
so \(0<E_1<1\).

Inductive step: assume \(0<E_k<1\) for all \(k<N\). If \(N=2M\), then
\[
0<E_N=\frac12E_M<\frac12<1.
\]
If \(N=2M+1\), then
\[
0<E_N=\frac12E_M+\frac13<\frac12+\frac13=\frac56<1.
\]
Thus by induction \(0<E_N<1\) for all \(N\ge 1\).

Therefore
\[
\left|S_N-\frac23N\right|=E_N<1.
\]

\[
\boxed{\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|<1}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

Let  
\[
S(N)=\sum_{n=1}^N \frac{\delta(n)}{n},\qquad S(0)=0,
\]
and define
\[
A(N)=S(N)-\frac23N.
\]
We will prove \(0\le A(N)<1\).

First observe that for even \(n=2m\),
\[
\delta(2m)=\delta(m),
\]
so
\[
\frac{\delta(2m)}{2m}=\frac12\frac{\delta(m)}{m}.
\]
For odd \(n\), \(\delta(n)=n\), hence \(\delta(n)/n=1\). Therefore
\[
S(N)=\#\{n\le N:n\text{ odd}\}+\frac12S(\lfloor N/2\rfloor)
=\left\lceil \frac N2\right\rceil+\frac12S(\lfloor N/2\rfloor).
\]

Now let \(A(N)=S(N)-2N/3\). Writing \(N=2q\) or \(N=2q+1\), we get
\[
A(2q)=q+\frac12S(q)-\frac{4q}{3}
=\frac12A(q),
\]
and
\[
A(2q+1)=q+1+\frac12S(q)-\frac{2(2q+1)}3
=\frac12A(q)+\frac13.
\]
Thus, equivalently,
\[
A(N)=\frac12A(\lfloor N/2\rfloor)+\frac{N\bmod 2}{3}.
\]

Write the binary expansion of \(N\) as
\[
N=\sum_{j=0}^k \varepsilon_j2^j,\qquad \varepsilon_j\in\{0,1\}.
\]
Iterating the recurrence above gives
\[
A(N)=\frac13\sum_{j=0}^k \frac{\varepsilon_j}{2^j}.
\]
Indeed, this is true for \(k=0\), and each binary digit contributes \(\varepsilon_j/(3\cdot 2^j)\) after being halved at each subsequent step.

Hence \(A(N)\ge 0\), and since only finitely many \(\varepsilon_j\) are nonzero,
\[
0\le A(N)
=\frac13\sum_{j=0}^k \frac{\varepsilon_j}{2^j}
\le \frac13\sum_{j=0}^k \frac1{2^j}
=\frac13\left(2-2^{-k}\right)
<\frac23<1.
\]
Therefore
\[
\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|
=|A(N)|
=A(N)
<1.
\]

This proves the required inequality.

</details>

<details><summary>A14: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}n,\qquad T_N=S_N-\frac23N.
\]
We will prove the stronger bound \(0\le T_N<\frac23<1\).

For \(j\ge1\), write \(j=2^r u\) with \(u\) odd. Then \(2j=2^{r+1}u\), so
\[
\delta(2j)=u=\delta(j).
\]
Hence
\[
\frac{\delta(2j)}{2j}=\frac12\frac{\delta(j)}j.
\]

Now for \(M\ge0\), among \(1,2,\dots,2M\) there are exactly \(M\) odd numbers, each contributing \(1\), and the even terms contribute \(\frac12S_M\). Thus
\[
S_{2M}=M+\frac12S_M.
\]
Also,
\[
S_{2M+1}=S_{2M}+1=M+1+\frac12S_M.
\]

Define \(T_N=S_N-\frac23N\), with \(T_0=0\). Then
\[
T_{2M}=S_{2M}-\frac43M
=M+\frac12S_M-\frac43M
=\frac12S_M-\frac M3
=\frac12T_M,
\]
and
\[
\begin{aligned}
T_{2M+1}
&=M+1+\frac12S_M-\frac{2(2M+1)}3\\
&=\frac12S_M+\frac{1-M}{3}\\
&=\frac12\left(T_M+\frac23M\right)+\frac{1-M}{3}\\
&=\frac12T_M+\frac13.
\end{aligned}
\]

We prove by strong induction that \(0\le T_N<\frac23\) for all \(N\ge0\). The base case \(T_0=0\) is clear. Assume the claim holds for all smaller indices.

If \(N=2M\), then
\[
T_N=T_M/2<\frac13<\frac23.
\]
If \(N=2M+1\), then
\[
T_N=T_M/2+\frac13<\frac13+\frac13=\frac23.
\]
Also the recurrences show \(T_N\ge0\). Hence \(0\le T_N<\frac23\) for all \(N\).

Therefore
\[
\left|S_N-\frac23N\right|=|T_N|=T_N<\frac23<1.
\]

\[
\boxed{\left|\sum_{n=1}^N \frac{\delta(n)}{n}-\frac23N\right|<1}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

Let  
\[
S(N)=\sum_{n=1}^N \frac{\delta(n)}{n},\qquad S(0)=0,
\]
and define
\[
E(N)=S(N)-\frac{2N}{3}.
\]
We will prove \(0<E(N)<1\), in fact \(0<E(N)<2/3\).

For odd \(n\), \(\delta(n)=n\), so \(\delta(n)/n=1\). There are \(\lceil N/2\rceil\) odd integers \(n\le N\). For even \(n=2m\),
\[
\delta(2m)=\delta(m),
\]
so
\[
\frac{\delta(2m)}{2m}=\frac12\frac{\delta(m)}{m}.
\]
Hence
\[
S(N)=\left\lceil \frac N2\right\rceil+\frac12 S(\lfloor N/2\rfloor).
\]

Now let \(E(N)=S(N)-2N/3\). We compute the recurrence.

If \(N=2q\), then
\[
S(2q)=q+\frac12S(q),
\]
so
\[
E(2q)=q+\frac12S(q)-\frac{4q}{3}
=\frac12\left(S(q)-\frac{2q}{3}\right)
=\frac12E(q).
\]

If \(N=2q+1\), then
\[
S(2q+1)=q+1+\frac12S(q),
\]
so
\[
\begin{aligned}
E(2q+1)
&=q+1+\frac12S(q)-\frac{4q+2}{3}\\
&=\frac13+\frac12S(q)-\frac q3\\
&=\frac13+\frac12\left(S(q)-\frac{2q}{3}\right)\\
&=\frac13+\frac12E(q).
\end{aligned}
\]

Base case:
\[
E(1)=S(1)-\frac23=1-\frac23=\frac13.
\]

We now prove by induction that \(0<E(N)<2/3\) for every \(N\ge1\).

If \(N=2q\), then \(q<N\), so by induction \(0<E(q)<2/3\). Hence
\[
0<E(N)=\frac12E(q)<\frac13<\frac23.
\]

If \(N=2q+1\), then \(q<N\), and for \(q\ge1\),
\[
0<E(N)=\frac13+\frac12E(q)
<\frac13+\frac12\cdot\frac23=\frac23.
\]
The case \(N=1\) is the base case.

Therefore, for every positive integer \(N\),
\[
0<E(N)<\frac23<1.
\]
Since \(E(N)>0\),
\[
\left|S(N)-\frac23N\right|=E(N)<1.
\]

\[
\boxed{\left| \sum_{n=1}^N \frac{\delta(n)}{n}-\frac{2}{3}N \right|<1}
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

Let  
\[
S_N=\sum_{n=1}^N \frac{\delta(n)}n,\qquad T_N=S_N-\frac23N.
\]
We prove \(|T_N|<1\).

First note that for \(n=2^a u\) with \(u\) odd, \(\delta(n)=u\), so
\[
\frac{\delta(n)}n=\frac1{2^a}.
\]
In particular, if \(n=2m\), then \(\delta(2m)=\delta(m)\), hence
\[
\frac{\delta(2m)}{2m}=\frac12\frac{\delta(m)}m.
\]
Also, for odd \(n\), \(\delta(n)/n=1\). Therefore
\[
S_N=\#\{n\le N:n\text{ odd}\}+\frac12S_{\lfloor N/2\rfloor}
=\left\lceil\frac N2\right\rceil+\frac12S_{\lfloor N/2\rfloor}.
\]

Set \(T_0=0\). Using the recurrence for \(S_N\), we get
\[
T_{2M}=T_M/2,\qquad T_{2M+1}=\frac13+\frac12T_M.
\]
Indeed, for \(N=2M\),
\[
T_{2M}=M+\frac12S_M-\frac43M
=\frac12T_M,
\]
and for \(N=2M+1\),
\[
T_{2M+1}=M+1+\frac12S_M-\frac{4M+2}{3}
=\frac13+\frac12T_M.
\]

Now write the binary expansion
\[
N=\sum_{i=0}^L b_i2^i,\qquad b_i\in\{0,1\},\ b_L=1.
\]
Applying the recurrence from the least significant bit upward gives
\[
T_N=\frac13\sum_{i=0}^L \frac{b_i}{2^i}.
\]
This is easily proved by induction on \(L\), using
\[
T_{2M}=\frac12T_M,\qquad T_{2M+1}=\frac13+\frac12T_M.
\]

Hence
\[
0<T_N
=\frac13\sum_{i=0}^L \frac{b_i}{2^i}
\le \frac13\sum_{i=0}^L \frac1{2^i}
=\frac13\left(2-\frac1{2^L}\right)
<\frac23<1.
\]
Therefore
\[
|T_N|<1.
\]
Since
\[
S_N-\frac23N=T_N,
\]
we conclude
\[
\left|\sum_{n=1}^N \frac{\delta(n)}n-\frac23N\right|<1.
\]

\[
\boxed{\text{Proved}}
\]

</details>
