# PB-Basic-030

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Given a trapezoid $ABCD$ with $AB,CD$ as the two legs. Circle $(W_{1})$ passes through $A,B$, and $(W_{2})$ passes through $C,D$ so that they are tangent to each other. The inscribed angle on circle $W_1$ corresponding to the arc AB on the side opposite to C and D is alpha, and the inscribed angle on circle $W_2$ corresponding to the arc CD on the side opposite to  A and B is beta. Construct $(W_{3})$ passing through $A,B$, $(W_{4})$ passing through $C,D$ such that the inscribed angle on circle W3 corresponding to the arc AB on the side opposite to C and D is $\beta$, and the inscribed angle on circle $W_4$ corresponding to the arc CD on the side opposite to  A and B is b $\alpha$. Prove that $(W_{3}),(W_{4})$ are tangent to each other.

## Swarm: accepted (best candidate `P4`; self-verification grades [7, 7, 7]; 993,590 tokens in 60 calls)

**Blind grade: Almost (6/7).** Clean, correct complex-number proof (w3 = w and R3R4 = R1R2 carry relation (1) over to W3, W4) for intersecting legs, but the case AB parallel to CD is not considered.

Let \(E=AB\cap CD\). Since \(AD\parallel BC\), the triangles \(EAD\) and \(EBC\) are similar, so, with \(E\) as origin and using unit vectors \(\mathbf u,\mathbf v\) along \(EA,ED\), we may write
\[
A=a\mathbf u,\quad B=\lambda a\mathbf u,\qquad 
D=d\mathbf v,\quad C=\lambda d\mathbf v
\]
for some \(\lambda>0,\lambda\ne1\). Put
\[
x=\frac{(\lambda-1)a}{2},\qquad y=\frac{(\lambda-1)d}{2},\qquad r=\frac{x}{y}=\frac ad.
\]
Let \(m_1=a+x,\ m_2=d+y\). Then \(m_1=rm_2\) and \(x=ry\).

Use the complex plane with \(\mathbf u=1\), \(\mathbf v=e^{i\theta}\). The center of \(W_1\) is
\[
O_1=m_1+ip,\qquad p=x\cot\alpha,
\]
and the center of \(W_2\) is
\[
O_2=(m_2-iq)v,\qquad q=y\cot\beta.
\]
Set
\[
z_1=m_1+ip,\qquad z_2=m_2-iq,\qquad w=z_1\overline{z_2}=(m_1+ip)(m_2+iq).
\]
The radii satisfy
\[
R_1^2=x^2+p^2,\qquad R_2^2=y^2+q^2,
\]
and the powers of \(E\) give
\[
|O_1|^2=R_1^2+U,\qquad |O_2|^2=R_2^2+V
\]
for some constants \(U,V\). Hence
\[
|O_1-O_2|^2
=R_1^2+R_2^2+U+V-2\Re(w\overline v).
\]
Since \(W_1,W_2\) are tangent, say with sign \(\sigma=\pm1\),
\[
|O_1-O_2|^2=R_1^2+R_2^2+2\sigma R_1R_2.
\]
Thus
\[
2\Re(w\overline v)+2\sigma R_1R_2=U+V. \tag{1}
\]

Now construct \(W_3,W_4\). By definition,
\[
p_3=x\cot\beta=rq,\qquad q_4=y\cot\alpha=\frac pr.
\]
So
\[
O_3=m_1+ip_3,\qquad O_4=(m_2-iq_4)v.
\]
Let
\[
w_3=(m_1+ip_3)(m_2+iq_4).
\]
Using \(m_1=rm_2\), \(x=ry\), \(p_3=rq\), \(q_4=p/r\), we get
\[
m_1m_2-p_3q_4=m_1m_2-pq,
\]
and
\[
m_2p_3+m_1q_4
=m_2rq+m_1\frac pr
=m_2rq+m_2p
=m_2p+m_1q.
\]
Therefore
\[
w_3=w.
\]
Also,
\[
R_3^2=x^2+p_3^2=r^2(y^2+q^2)=r^2R_2^2,
\]
and
\[
R_4^2=y^2+q_4^2=\frac{R_1^2}{r^2}.
\]
Hence
\[
R_3R_4=R_1R_2.
\]
Therefore equation (1) remains true for \(W_3,W_4\):
\[
2\Re(w_3\overline v)+2\sigma R_3R_4=U+V.
\]
But
\[
|O_3-O_4|^2
=R_3^2+R_4^2+U+V-2\Re(w_3\overline v)
=R_3^2+R_4^2+2\sigma R_3R_4.
\]
Thus
\[
|O_3-O_4|=R_3+R_4
\]
if \(\sigma=1\), or \(|R_3-R_4|\) if \(\sigma=-1\). In either case \(W_3\) and \(W_4\) are tangent.

\[
\boxed{\text{Therefore }(W_3),(W_4)\text{ are tangent.}}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 4.75/7; graded Correct: 0 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 90,843 | Almost (5/7) | Right approach with a correct symmetric tangency equation, but s is misdefined as √(1-γ) instead of √(1-γ^2), the key dot products are asserted rather than computed, and the case AB ∥ CD is omitted. |
| A2 | stop | 76,060 | Almost (6/7) | Correct vector computation showing the tangency condition L_{x,y}^2 = 4p^2q^2(1+x^2)(1+y^2) is symmetric in cotα, cotβ (one garbled line is harmless), but it assumes AB and CD intersect and omits the parallel case. |
| A3 | stop | 65,403 | Almost (6/7) | Correct complex-coordinate verification that Re(O1·conj O2) = Re(O3·conj O4), \|O_i\|^2 - R_i^2 is angle-independent and R1R2 = R3R4, so tangency transfers, but the parallel case AB ∥ CD is not handled. |
| A4 | stop | 75,323 | Almost (6/7) | Correct complex-coordinate proof for intersecting legs (consistent center offsets, the quantity T is symmetric in u and v, and R2 = cR3, R4 = cR1 transfer the tangency condition exactly), but the case AB parallel to CD is never considered. |
| A5 | stop | 54,620 | Almost (6/7) | Correct vector proof using l1/m1 = l2/m2 to get O1·O2 = O3·O4 and R1R2 = R3R4, hence tangency of W3, W4 when AB and CD intersect, but the parallel case is omitted. |
| A6 | stop | 67,476 | Almost (6/7) | Correct analytic proof (with P = AB∩CD) that the tangency condition 2k(p^2+r^2) - pr S(α,β) = ±pr(k-1)^2 cscα cscβ is symmetric in α and β, but the case AB ∥ CD is never considered. |
| A7 | stop | 63,621 | Almost (5/7) | Correct dot-product and power-of-a-point approach with the right symmetric formula for O1.O2, but the normal v is said to point toward A,B while the dot products used require it to point away (two sign slips that cancel), the write-up keeps an unresolved 'wait careful' fragment, and the parallel case is omitted. |
| A8 | stop | 60,177 | Almost (6/7) | Correct complex-coordinate proof that \|O1O2\|^2-R1^2-R2^2 and \|O3O4\|^2-R3^2-R4^2 both equal r^2 L while R1R2 = R3R4, so tangency transfers, but the case AB ∥ CD is not addressed. |
| A9 | stop | 96,404 | Partial (1/7) | Sets up correct oblique-coordinate circle equations, but the decisive claim that the tangency condition is symmetric is only asserted, the displayed tangency equation is off by a factor of 2 (under which the claim fails), and the parallel case is omitted. |
| A10 | stop | 81,676 | Almost (6/7) | Correct complex-coordinate proof using the angle bisector as axis (z4 conj(z3) = z2 conj(z1), equal powers of P, R1R2 = R3R4) for intersecting legs, but the parallel-legs case is omitted. |
| A11 | stop | 104,367 | Incorrect (0/7) | The anti-similarity T gives T(W1) = W4 and T(W2) = r^{-2}W3, which only shows W4 is tangent to the rescaled circle r^{-2}W3; concluding that W4 is tangent to W3 is a non sequitur (no inversion is used), so the key step fails. |
| A12 | stop | 61,707 | Almost (6/7) | Correct analytic proof via powers of P and the alpha-beta symmetric quantity S together with R1R2 = R3R4, valid for intersecting legs, but the parallel-legs case is not considered. |
| A13 | stop | 69,480 | Almost (6/7) | Clean, correct complex-number proof that both pairs satisfy the same relation k(1+t^2) - 2t Re(u e^{-iθ} v) = ±2tRS, but it relies on P = AB∩CD and does not treat the case AB ∥ CD. |
| A14 | stop | 61,084 | Almost (6/7) | Correctly shows O1·O2 = O3·O4 (via Xq = Yp from the similarity), \|O_i\|^2 - R_i^2 independent of the angles, and R1R2 = R3R4, transferring tangency, but only treats the case where AB and CD meet. |
| A15 | stop | 98,790 | Incorrect (0/7) | Falsely claims a spiral similarity sends the alpha-circle through A,B to the beta-circle through C,D and then identifies W3 with W2 and W4 with W1, so there is no valid argument. |
| A16 | stop | 74,909 | Almost (5/7) | Correct power-of-a-point and dot-product framework with a valid symmetry argument, but the displayed expression for E is miscomputed (2am^2 gamma instead of 2a^2 m gamma, and the cot-cot term is off by a factor 2), the key expansion O3.O4 = O1.O2 is only asserted, and the parallel case is omitted. |

<details><summary>A1: Almost (5/7)</summary>

\[
\boxed{
\text{The two swapped circles }(W_3),(W_4)\text{ are tangent.}
}
\]

We give a rigorous proof.

Let \(P=AB\cap CD\). Since \(AD\parallel BC\), triangles \(PAD\) and \(PBC\) are similar, hence
\[
\frac{PA}{PB}=\frac{PD}{PC}=m.
\]
Choose coordinates with \(P\) as origin, and let \(\mathbf e_1,\mathbf e_2\) be unit vectors along \(AB,CD\). Write
\[
A=mx\mathbf e_1,\quad B=x\mathbf e_1,\quad D=my\mathbf e_2,\quad C=y\mathbf e_2
\]
for some \(x,y>0\). Put
\[
a=\frac{m-1}{2}x,\qquad b=\frac{m-1}{2}y,\qquad 
\lambda=\frac{m+1}{m-1}.
\]
Thus the midpoint of \(AB\) is \(a\lambda\mathbf e_1\), and the half-length of chord \(AB\) is \(a\). If \(O_1,R_1\) are the center and radius of \((W_1)\), then, because the arc \(AB\) on the side opposite \(C,D\) subtends angle \(\alpha\),
\[
O_1=a(\lambda\mathbf e_1+\cot\alpha\,\mathbf n_1),\qquad R_1=a\csc\alpha,
\]
where \(\mathbf n_1\) is the unit normal to \(AB\) pointing toward \(CD\). Similarly
\[
O_2=b(\lambda\mathbf e_2+\cot\beta\,\mathbf n_2),\qquad R_2=b\csc\beta.
\]

Let \(\gamma=\mathbf e_1\cdot\mathbf e_2\), \(s=\sqrt{1-\gamma}\), and define
\[
u_1=\lambda\mathbf e_1+\cot\alpha\,\mathbf n_1,\qquad 
u_2=\lambda\mathbf e_2+\cot\beta\,\mathbf n_2.
\]
Then
\[
O_1=a u_1,\qquad O_2=b u_2,\qquad R_1=a\csc\alpha,\qquad R_2=b\csc\beta.
\]

The tangency of \((W_1),(W_2)\) means
\[
\|b u_2-a u_1\|=R_1+R_2
\]
or the analogous internal tangency case. Squaring gives
\[
a^2(\lambda^2-1)+b^2(\lambda^2-1)
=2ab\bigl(u_1\cdot u_2\pm \csc\alpha\csc\beta\bigr). \tag{1}
\]

Now compute
\[
u_1\cdot u_2
=\lambda^2\gamma+\lambda s(\cot\alpha+\cot\beta)-\gamma\cot\alpha\cot\beta.
\]
This expression is symmetric in \(\alpha,\beta\). Hence equation (1) is unchanged if we interchange \(\alpha\) and \(\beta\).

Now consider the circles \((W_3),(W_4)\). They have centers
\[
O_3=a(\lambda\mathbf e_1+\cot\beta\,\mathbf n_1),\qquad
O_4=b(\lambda\mathbf e_2+\cot\alpha\,\mathbf n_2),
\]
and radii
\[
R_3=a\csc\beta,\qquad R_4=b\csc\alpha.
\]
Writing
\[
u_1'=\lambda\mathbf e_1+\cot\beta\,\mathbf n_1,\qquad
u_2'=\lambda\mathbf e_2+\cot\alpha\,\mathbf n_2,
\]
we have \(O_3=a u_1'\), \(O_4=b u_2'\). Moreover
\[
u_1'\cdot u_2'
=\lambda^2\gamma+\lambda s(\cot\alpha+\cot\beta)
-\gamma\cot\alpha\cot\beta
=u_1\cdot u_2.
\]
Therefore the tangency condition for \((W_3),(W_4)\) is exactly the same equation (1) with \(\alpha,\beta\) interchanged. Since the original tangency \((W_1),(W_2)\) gave equation (1), the same equation holds after swapping \(\alpha,\beta\). Hence \((W_3),(W_4)\) are tangent.

Thus the construction preserves tangency, completing the proof.

\[
\boxed{(W_3),(W_4)\text{ are tangent.}}
\]

</details>

<details><summary>A2: Almost (6/7)</summary>

\[
\boxed{
\begin{aligned}
&\text{Let }O=AB\cap CD. \text{ Since }AD\parallel BC,\text{ the rays }OA,OB\text{ and }OD,OC\\
&\text{are corresponding under a homothety. Hence we may write}\\
&A=a\mathbf u,\quad B=\lambda a\mathbf u,\quad D=d\mathbf v,\quad C=\lambda d\mathbf v\\
&\text{for some } \lambda>1 \text{ and unit vectors } \mathbf u,\mathbf v.
\end{aligned}
}
\]

Define
\[
p=AB=(\lambda-1)a,\qquad q=CD=(\lambda-1)d,
\]
and
\[
r=\frac{\lambda+1}{\lambda-1}>1.
\]
Then
\[
\frac{(\lambda+1)a}{2}=\frac{rp}{2},\qquad \frac{(\lambda+1)d}{2}=\frac{rq}{2}.
\]

Let \(\mathbf n\) and \(\mathbf m\) be the inward unit normals to \(AB\) and \(CD\), respectively. Put
\[
x=\cot\alpha,\qquad y=\cot\beta,
\]
and let
\[
C_0=\cos\angle(\mathbf u,\mathbf v),\qquad S_0=\sin\angle(\mathbf u,\mathbf v).
\]
From the tangent-chord theorem, the center of \((W_1)\) is
\[
O_1=\frac p2\bigl(r\mathbf u-x\mathbf n\bigr),
\]
and its radius is
\[
R_1=\frac p{2\sin\alpha}=\frac p2\sqrt{1+x^2}.
\]
Similarly,
\[
O_2=\frac q2\bigl(r\mathbf v-y\mathbf m\bigr),\qquad
R_2=\frac q{2\sin\beta}=\frac q2\sqrt{1+y^2}.
\]

Now
\[
|\mathbf u\mathbf?| \qquad 
\mathbf u\cdot\mathbf v=C_0,\quad
\mathbf u\cdot\mathbf m=S_0,\quad
\mathbf n\cdot\mathbf v=S_0,\quad
\mathbf n\cdot\mathbf m=-C_0.
\]
A direct expansion gives
\[
\begin{aligned}
|O_1-O_2|^2-R_1^2-R_2^2
&=\frac14\Bigl[(r^2-1)(p^2+q^2)\\
&\qquad -2pq\bigl(r^2C_0-rS_0(x+y)-C_0xy\bigr)\Bigr].
\end{aligned}
\]
Thus \(W_1\) and \(W_2\) are tangent iff
\[
\begin{aligned}
L_{x,y}^2
&=4p^2q^2(1+x^2)(1+y^2),
\end{aligned}
\]
where
\[
L_{x,y}
=(r^2-1)(p^2+q^2)
-2pq\bigl(r^2C_0-rS_0(x+y)-C_0xy\bigr).
\]
The left-hand side \(L_{x,y}\) is symmetric in \(x,y\), and so is \(4p^2q^2(1+x^2)(1+y^2)\). Therefore
\[
L_{x,y}=L_{y,x}.
\]

The given tangency of \(W_1,W_2\) means the equation above holds for \((x,y)\). Replacing \(x\) by \(y\) and \(y\) by \(x\) gives exactly the tangency condition for the circles through \(AB\) and \(CD\) with the swapped angles:
\[
W_3:\ \alpha\mapsto\beta,\qquad W_4:\beta\mapsto\alpha.
\]
Hence \(W_3\) and \(W_4\) satisfy the same equation, so they are tangent.

\[
\boxed{\text{Therefore }(W_3)\text{ and }(W_4)\text{ are tangent to each other.}}
\]

</details>

<details><summary>A3: Almost (6/7)</summary>

\[
\boxed{\text{The circles }(W_3),(W_4)\text{ are tangent.}}
\]

Let \(P=AB\cap CD\). Since \(AD\parallel BC\), triangles \(PAD\) and \(PBC\) are similar, so we may use complex coordinates with  
\[
P=0,\qquad AB\subset \mathbb R,\qquad CD\subset \{tz:t\in\mathbb R\},\quad z=e^{i\theta}.
\]
Write
\[
A=a,\quad B=\lambda a,\qquad D=dz,\quad C=\lambda dz
\]
for some \(\lambda>1\). Put
\[
u=\frac{(\lambda-1)a}{2},\qquad v=\frac{(\lambda-1)d}{2},\qquad 
T=\frac{\lambda+1}{\lambda-1},\qquad \rho=T^2-1.
\]
Then the midpoints of \(AB\) and \(CD\) have coordinates \(Tu\) and \(Tvz\), respectively.

For a chord of length \(2u\) whose subtended angle is \(\theta\), the circle has radius \(u/\sin\theta\), and its center is at distance \(u\cot\theta\) from the chord on the required side. Hence
\[
O_1=u(T+i\cot\alpha),\qquad R_1=\frac u{\sin\alpha},
\]
and
\[
O_2=vz(T-i\cot\beta),\qquad R_2=\frac v{\sin\beta}.
\]

Now expand the tangency condition for \(W_1,W_2\). Since
\[
|O_1|^2=R_1^2+\rho u^2,\qquad |O_2|^2=R_2^2+\rho v^2,
\]
we have
\[
|O_1-O_2|^2=(R_1\pm R_2)^2
\]
equivalent to
\[
\rho(u^2+v^2)-2\Re(O_1\overline{O_2})
=\pm 2R_1R_2.
\]
Let \(p=\cot\alpha\), \(q=\cot\beta\). Using \(z=k+is\), \(k^2+s^2=1\), one obtains
\[
O_1\overline{O_2}
=uv(k-is)(T+ip)(T+iq),
\]
so
\[
2\Re(O_1\overline{O_2})
=2uv\bigl(k(T^2-pq)+sT(p+q)\bigr).
\]
Thus \(W_1,W_2\) tangent is exactly
\[
\rho(u^2+v^2)-2uv\bigl(k(T^2-pq)+sT(p+q)\bigr)
=\pm \frac{2uv}{\sin\alpha\sin\beta}. \tag{1}
\]

Now construct \(W_3,W_4\) as in the problem:
\[
O_3=u(T+iq),\quad R_3=\frac u{\sin\beta},
\]
\[
O_4=vz(T-ip),\quad R_4=\frac v{\sin\alpha}.
\]
A direct computation gives
\[
O_3\overline{O_4}
=uv(k-is)(T+iq)(T+ip),
\]
whose real part is exactly the same expression as before. Therefore
\[
\rho(u^2+v^2)-2uv\bigl(k(T^2-pq)+sT(p+q)\bigr)
=\pm 2R_3R_4.
\]
Since \(2R_3R_4=\dfrac{2uv}{\sin\alpha\sin\beta}\), this is precisely equation (1) for \(W_3,W_4\). Hence
\[
|O_3-O_4|=R_3+R_4
\]
or
\[
|O_3-O_4|=|R_3-R_4|.
\]
Therefore \((W_3)\) and \((W_4)\) are tangent.

\[
\boxed{\text{Proved}}
\]

</details>

<details><summary>A4: Almost (6/7)</summary>

\[
\boxed{\text{The circles }(W_3)\text{ and }(W_4)\text{ are tangent.}}
\]

We give a complete analytic proof.

Let \(O=AB\cap CD\). Since \(AB,CD\) are the legs, the bases are parallel, so \(AD\parallel BC\). Apply a similarity so that \(O=0\), \(AB\) is the real axis, \(B=1\), and \(A=a\) with \(a>0,\ a\ne 1\). Write
\[
C=cz,\qquad D=acz,\qquad z=e^{i\theta},\ \sin\theta>0.
\]
This is valid because \(AD\parallel BC\) forces the same ratio \(OD/OC=OA/OB=a\).

Set
\[
p=\frac{a+1}{2},\qquad q=\frac{|a-1|}{2},
\]
so
\[
p^2-q^2=a.
\]

For a chord of length \(2q\) and an inscribed angle \(\alpha\) on one side, the center lies on the perpendicular bisector at signed distance \(q\cot\alpha\) from the chord. Define
\[
u=q\cot\alpha,\qquad v=q\cot\beta.
\]
Then the centers and radii of the relevant circles are
\[
o_1=p+iu,\qquad R_1=\sqrt{q^2+u^2},
\]
\[
o_3=p+iv,\qquad R_3=\sqrt{q^2+v^2},
\]
and, since \(CD\) has half-length \(cq\),
\[
o_2=cz(p-iv)=cz\overline{o_3},\qquad R_2=cR_3,
\]
\[
o_4=cz(p-iu)=cz\overline{o_1},\qquad R_4=cR_1.
\]

Now let \(d_{ij}\) denote the distance between the centers of the two circles \(W_i,W_j\). Expanding,
\[
d_{12}^2=|o_2-o_1|^2
=R_1^2+c^2R_3^2+T,
\]
where
\[
T=a(c^2+1)-2c\bigl[(p^2-uv)\cos\theta+p(u+v)\sin\theta\bigr].
\]
Similarly,
\[
d_{34}^2=|o_4-o_3|^2
=R_3^2+c^2R_1^2+T.
\]

Since \((W_1)\) and \((W_2)\) are tangent,
\[
d_{12}^2=R_1^2+R_2^2\pm 2R_1R_2
=R_1^2+c^2R_3^2\pm 2cR_1R_3.
\]
Comparing with the expression for \(d_{12}^2\), we get
\[
T=\pm 2cR_1R_3.
\]
Therefore
\[
d_{34}^2=R_3^2+c^2R_1^2+T
=R_3^2+c^2R_1^2\pm 2cR_1R_3
=(R_3\pm cR_1)^2.
\]
But \(R_4=cR_1\), so
\[
d_{34}=R_3+R_4
\]
or
\[
d_{34}=|R_3-R_4|.
\]
These are exactly the conditions for \((W_3)\) and \((W_4)\) to be tangent.

Hence \((W_3)\) and \((W_4)\) are tangent.

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A5: Almost (6/7)</summary>

\[
\boxed{\text{The proof is as follows.}}
\]

Let \(P=AB\cap CD\). Since \(AB\) and \(CD\) are the legs of the trapezoid, \(AD\parallel BC\). Put \(P\) at the origin, and take unit vectors \(\mathbf u,\mathbf v\) along \(PB,PC\). Write
\[
B=b\mathbf u,\quad C=c\mathbf v,\quad A=a\mathbf u,\quad D=d\mathbf v
\]
with \(a,b,c,d>0\). From \(AD\parallel BC\),
\[
d\mathbf v-a\mathbf u \parallel c\mathbf v-b\mathbf u,
\]
so \(a/b=d/c\). Hence, if
\[
m_1=\frac{a+b}{2},\quad l_1=\frac{|a-b|}{2},\qquad
m_2=\frac{c+d}{2},\quad l_2=\frac{|c-d|}{2},
\]
then
\[
\frac{l_1}{m_1}=\frac{l_2}{m_2}=r.
\]

Choose coordinates
\[
\mathbf u=(1,0),\qquad \mathbf v=(\cos\theta,\sin\theta),
\]
and let \(s=\sin\theta,\ t=\cos\theta\). Let
\[
n_1=(0,1),\qquad n_2=(s,-t).
\]
Then \(n_1\perp \mathbf u\), \(n_2\perp \mathbf v\), and
\[
\mathbf u\cdot \mathbf v=t,\quad \mathbf u\cdot n_2=s,\quad \mathbf v\cdot n_1=s,\quad n_1\cdot n_2=-t.
\]

The centers of \(W_1,W_2,W_3,W_4\) are respectively
\[
O_1=m_1\mathbf u+k_1n_1,\quad
O_2=m_2\mathbf v+k_2n_2,
\]
\[
O_3=m_1\mathbf u+k_3n_1,\quad
O_4=m_2\mathbf v+k_4n_2,
\]
where, by the given angle conditions,
\[
k_1=l_1\cot\alpha,\quad k_2=l_2\cot\beta,
\]
\[
k_3=l_1\cot\beta,\quad k_4=l_2\cot\alpha.
\]

The radii satisfy
\[
R_1^2=l_1^2+k_1^2,\quad R_2^2=l_2^2+k_2^2,
\]
\[
R_3^2=l_1^2+k_3^2,\quad R_4^2=l_2^2+k_4^2.
\]

Now compute
\[
O_1\cdot O_2
=m_1m_2t+s(m_1k_2+k_1m_2)-tk_1k_2.
\]
Using \(l_1=rm_1,\ l_2=rm_2\), this becomes
\[
O_1\cdot O_2
=m_1m_2\left[t+rs(\cot\alpha+\cot\beta)-r^2t\cot\alpha\cot\beta\right].
\]
For \(W_3,W_4\), the same substitution gives
\[
O_3\cdot O_4
=m_1m_2\left[t+rs(\cot\alpha+\cot\beta)-r^2t\cot\alpha\cot\beta\right].
\]
Hence
\[
O_3\cdot O_4=O_1\cdot O_2.
\]
Also
\[
R_3R_4=\frac{l_1l_2}{\sin\alpha\sin\beta}=R_1R_2.
\]

Let \(D_1=O_1O_2\) and \(D_2=O_3O_4\). Since \(W_1,W_2\) are tangent, for some \(\varepsilon=\pm1\),
\[
D_1^2=R_1^2+R_2^2+\varepsilon 2R_1R_2.
\]
Using \(|O_1|^2=m_1^2+k_1^2\), \(|O_2|^2=m_2^2+k_2^2\), we get
\[
D_1^2-(R_1^2+R_2^2)
=(1-r^2)(m_1^2+m_2^2)-2O_1\cdot O_2
=\varepsilon 2R_1R_2.
\]
For \(W_3,W_4\),
\[
D_2^2-(R_3^2+R_4^2)
=(1-r^2)(m_1^2+m_2^2)-2O_3\cdot O_4.
\]
But \(O_3\cdot O_4=O_1\cdot O_2\) and \(R_3R_4=R_1R_2\), so
\[
D_2^2=R_3^2+R_4^2+\varepsilon 2R_3R_4
=(R_3+\varepsilon R_4)^2.
\]
Thus
\[
D_2=R_3+R_4 \quad\text{or}\quad D_2=|R_3-R_4|,
\]
which is precisely the condition for two circles to be tangent. Therefore \(W_3\) and \(W_4\) are tangent.

\[
\boxed{\text{Therefore }(W_3)\text{ and }(W_4)\text{ are tangent.}}
\]

</details>

<details><summary>A6: Almost (6/7)</summary>

Let \(P=AB\cap CD\). Since \(AD\parallel BC\), the triangles \(PBC\) and \(PAD\) are similar, so we may write
\[
PA=kp,\quad PB=p,\qquad PD=kr,\quad PC=r
\]
with \(k>1\). Put \(P\) at the origin, let \(AB\) be the \(x\)-axis, and let
\[
B=(p,0),\quad A=(kp,0),
\]
\[
C=r(\cos\theta,\sin\theta),\quad D=kr(\cos\theta,\sin\theta).
\]
Write \(c=\cos\theta,\ s=\sin\theta\).

---

### 1. Equation of \((W_1)\)

A circle through \((p,0)\) and \((kp,0)\) has equation
\[
x^2+y^2-p(k+1)x+vy+kp^2=0.
\]
Its center has \(y\)-coordinate \(-v/2\). The half-chord is
\[
h=\frac{p(k-1)}2.
\]
For an inscribed angle \(\alpha\) subtending this chord on the side \(y>0\),
\[
\frac{h}{R}=\sin\alpha,\qquad \frac{\text{distance from center to chord}}{R}=\cos\alpha,
\]
so
\[
-\frac v2=h\cot\alpha=\frac{p(k-1)}2\cot\alpha.
\]
Hence
\[
W_1:\quad x^2+y^2-p(k+1)x-p(k-1)\cot\alpha\,y+kp^2=0.
\]

### 2. Equation of \((W_2)\)

In coordinates \((X,Y)\) with
\[
X=cx+sy,\qquad Y=sx-cy,
\]
the line \(CD\) is the \(X\)-axis, with endpoints \(X=r\) and \(X=kr\). Thus
\[
X^2+Y^2-(k+1)rX-(k-1)r\cot\beta\,Y+kr^2=0.
\]
Substituting back \(X=cx+sy,\ Y=sx-cy\) gives
\[
W_2:\quad x^2+y^2-Ux-Vy+kr^2=0,
\]
where
\[
U=r(k+1)c+r(k-1)\cot\beta\,s,
\]
\[
V=r(k+1)s-r(k-1)\cot\beta\,c.
\]

---

### 3. Tangency condition for two circles

For two circles
\[
S_i:\ x^2+y^2+u_ix+v_iy+w_i=0,
\]
their centers are \(O_i=(-u_i/2,-v_i/2)\), and
\[
|O_1O_2|^2-R_1^2-R_2^2
=w_1+w_2-\frac{u_1u_2+v_1v_2}{2}.
\]
Thus tangency is equivalent to
\[
2(w_1+w_2)-u_1u_2-v_1v_2=\pm 4R_1R_2. \tag{1}
\]

For \(W_1\) and \(W_2\),
\[
w_1+w_2=k(p^2+r^2),
\]
and a direct expansion gives
\[
u_1u_2+v_1v_2
=pr\,S(\alpha,\beta),
\]
where
\[
S(\alpha,\beta)
=c\bigl((k+1)^2-(k-1)^2\cot\alpha\cot\beta\bigr)
+s(k^2-1)(\cot\alpha+\cot\beta).
\]
Also
\[
4R_1R_2=pr(k-1)^2\csc\alpha\csc\beta.
\]
Therefore \(W_1\) and \(W_2\) are tangent iff
\[
2k(p^2+r^2)-pr\,S(\alpha,\beta)
=\pm pr(k-1)^2\csc\alpha\csc\beta. \tag{2}
\]

But \(S(\alpha,\beta)\) is symmetric in \(\alpha,\beta\), and the right-hand side is also symmetric in \(\alpha,\beta\). Hence (2) is unchanged if \(\alpha\) and \(\beta\) are interchanged.

---

### 4. The swapped circles

Now take \(W_3\) through \(A,B\) with angle \(\beta\), and \(W_4\) through \(C,D\) with angle \(\alpha\). These are obtained from \(W_1\) and \(W_2\) by replacing \(\alpha\) by \(\beta\) and \(\beta\) by \(\alpha\), respectively.

Applying the same computation, \(W_3\) and \(W_4\) are tangent iff
\[
2k(p^2+r^2)-pr\,S(\beta,\alpha)
=\pm pr(k-1)^2\csc\alpha\csc\beta.
\]
Since
\[
S(\beta,\alpha)=S(\alpha,\beta),
\]
this is exactly the same equation as (2). But (2) holds by the hypothesis that \(W_1\) and \(W_2\) are tangent.

Therefore \(W_3\) and \(W_4\) satisfy the same tangency condition, so they are tangent to each other.

\[
\boxed{(W_3)\text{ and }(W_4)\text{ are tangent.}}
\]

</details>

<details><summary>A7: Almost (5/7)</summary>

Let \(P=AB\cap CD\). Since \(AB\) and \(CD\) are the legs, the bases are \(AD\parallel BC\). Hence
\[
\frac{PA}{PB}=\frac{PD}{PC}=\lambda>1.
\]
Choose coordinates with \(P\) as origin, \(PB\) along the \(x\)-axis, and \(PC\) making angle \(\theta\) with it. Write
\[
B=b e_1,\quad A=\lambda b e_1,\qquad
C=c e_2,\quad D=\lambda c e_2,
\]
where \(e_1,e_2\) are unit vectors and \(\theta=\angle(e_1,e_2)\).

For a chord of length \(L\), if the arc on one side has measure \(2\theta\), then the distance from the center to the chord is \(\frac L2\cot\theta\), and the radius is \(\frac L2\csc\theta\). Applying this to the two given circles gives, with
\[
m=\lambda-1,\qquad n=\lambda+1,
\]
\[
O_1=\frac{nb}{2}e_1+\frac{mb}{2}\cot\alpha\,f_1,\qquad
R_1=\frac{mb}{2\sin\alpha},
\]
where \(f_1\) is the unit perpendicular to \(AB\) toward \(C,D\), and
\[
O_2=\frac{nc}{2}e_2-\frac{mc}{2}\cot\beta\,v,\qquad
R_2=\frac{mc}{2\sin\beta},
\]
where \(v\) is the unit perpendicular to \(CD\) toward \(A,B\).

Using \(e_1\cdot e_2=\cos\theta\), \(f_1\cdot e_2=\sin\theta\), \(e_1\cdot v=-\sin\theta\), \(f_1\cdot v=\cos\theta\), one obtains
\[
O_1\cdot O_2
=\frac{bc}{4}\Bigl(
n^2\cos\theta+mn\sin\theta(\cot\alpha+\cot\beta)
-m^2\cos\theta\cot\alpha\cot\beta\Bigr).
\]
Thus
\[
O_1\cdot O_2
\]
is symmetric in \(\alpha,\beta\).

Now define the swapped circles \(W_3,W_4\). Their centers and radii are
\[
O_3=\frac{nb}{2}e_1+\frac{mb}{2}\cot\beta\,f_1,\qquad
R_3=\frac{mb}{2\sin\beta},
\]
\[
O_4=\frac{nb?}{?}\text{ wait careful: }O_4=\frac{nc}{2}e_2-\frac{mc}{2}\cot\alpha\,v,\qquad
R_4=\frac{mc}{2\sin\alpha}.
\]
Then
\[
O_3\cdot O_4=O_1\cdot O_2.
\]
Also
\[
R_3R_4=R_1R_2=\frac{m^2bc}{4\sin\alpha\sin\beta}.
\]

For the two circles \(W_1,W_2\), the power identities give
\[
|O_1|^2-R_1^2=\lambda b^2,\qquad
|O_2|^2-R_2^2=\lambda c^2.
\]
Therefore
\[
|O_1O_2|^2-R_1^2-R_2^2
=\lambda(b^2+c^2)-2O_1\cdot O_2.
\]
Since \(W_1\) and \(W_2\) are tangent,
\[
|O_1O_2|^2=(R_1\pm R_2)^2,
\]
so
\[
\lambda(b^2+c^2)-2O_1\cdot O_2=\pm 2R_1R_2.
\]

For \(W_3,W_4\), using the same identities,
\[
|O_3O_4|^2-R_3^2-R_4^2
=\lambda(b^2+c^2)-2O_3\cdot O_4
=\lambda(b^2+c^2)-2O_1\cdot O_2.
\]
Hence
\[
|O_3O_4|^2-R_3^2-R_4^2
=\pm 2R_3R_4.
\]
Thus
\[
|O_3O_4|^2=R_3^2+R_4^2\pm 2R_3R_4
=(R_3\pm R_4)^2,
\]
so
\[
|O_3O_4|=R_3+R_4 \quad\text{or}\quad |R_3-R_4|.
\]
Therefore \(W_3\) and \(W_4\) are tangent to each other.

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A8: Almost (6/7)</summary>

Let \(P=AB\cap CD\). Since \(AD\parallel BC\), the triangles \(PAD\) and \(PBC\) are similar; write

\[
\frac{PA}{PB}=\frac{PD}{PC}=k \qquad (0<k<1).
\]

Let

\[
r=\frac{AB}{2},\qquad s=\frac{CD}{2},\qquad \lambda=\frac{1+k}{1-k},\qquad t=\frac{s}{r}.
\]

Use complex coordinates with \(P=0\), \(AB\) along the positive real axis, and let the direction of \(CD\) be \(e^{i\theta}\). Put

\[
p=\cot\alpha,\qquad q=\cot\beta,\qquad C_p=\sqrt{1+p^2},\qquad C_q=\sqrt{1+q^2}.
\]

The midpoint of \(AB\) is \(r\lambda\) on the real axis, and the center of \(W_1\) lies on the perpendicular bisector of \(AB\) at signed distance \(r\cot\alpha\). Hence

\[
O_1=r(\lambda+ip).
\]

Similarly, for \(CD\), whose midpoint is \(s\lambda e^{i\theta}\), the center of \(W_2\) is

\[
O_2=s e^{i\theta}(\lambda-iq)=rt e^{i\theta}(\lambda-iq).
\]

The radii are

\[
R_1=rC_p,\qquad R_2=rtC_q.
\]

Now compute the tangency condition for \(W_1,W_2\). Dividing by \(r\),

\[
\frac{|O_1-O_2|^2}{r^2}
=
|\lambda+ip-t e^{i\theta}(\lambda-iq)|^2.
\]

Expanding,

\[
\begin{aligned}
\frac{|O_1-O_2|^2}{r^2}
&=\lambda^2+p^2+t^2(\lambda^2+q^2)\\
&-2t\big((\lambda^2-pq)\cos\theta+\lambda(p+q)\sin\theta\big).
\end{aligned}
\]

Therefore

\[
\frac{|O_1-O_2|^2}{r^2}-C_p^2-t^2C_q^2
=
(1+t^2)(\lambda^2-1)
-2t\big((\lambda^2-pq)\cos\theta+\lambda(p+q)\sin\theta\big).
\]

Call the right-hand side \(L\). Since \(W_1,W_2\) are tangent,

\[
|O_1-O_2|^2=R_1^2+R_2^2\pm 2R_1R_2.
\]

Dividing by \(r^2\),

\[
L=\pm 2tC_pC_q. \tag{1}
\]

Now consider the circles \(W_3,W_4\). By definition, \(W_3\) has the same chord \(AB\) but the angle \(\beta\), so its center is

\[
O_3=r(\lambda+iq),
\]

and its radius is \(R_3=rC_q\). The circle \(W_4\) has chord \(CD\) and angle \(\alpha\), so its center and radius are

\[
O_4=rt e^{i\theta}(\lambda-ip),\qquad R_4=rtC_p.
\]

We compute

\[
\begin{aligned}
\frac{|O_3-O_4|^2}{r^2}
&=
|\lambda+iq-t e^{i\theta}(\lambda-ip)|^2\\
&=\lambda^2+q^2+t^2(\lambda^2+p^2)\\
&-2t\big((\lambda^2-pq)\cos\theta+\lambda(p+q)\sin\theta\big).
\end{aligned}
\]

Subtracting \(C_q^2+t^2C_p^2\), the cross terms remain exactly the same, so

\[
\frac{|O_3-O_4|^2}{r^2}
-C_q^2-t^2C_p^2
=
L.
\]

Thus

\[
|O_3-O_4|^2-R_3^2-R_4^2
=
r^2L
=
\pm 2R_3R_4.
\]

Hence

\[
|O_3O_4|^2
=
R_3^2+R_4^2\pm 2R_3R_4
=
(R_3\pm R_4)^2.
\]

Therefore

\[
O_3O_4=R_3+R_4 \quad\text{or}\quad O_3O_4=|R_3-R_4|,
\]

which is exactly the tangency condition for the two circles \((W_3)\) and \((W_4)\).

\[
\boxed{\text{Therefore }(W_3)\text{ and }(W_4)\text{ are tangent.}}
\]

</details>

<details><summary>A9: Partial (1/7)</summary>

Let \(P=AB\cap CD\). Work in oblique coordinates with origin \(P\), \(x\)-axis along \(AB\), and \(y\)-axis along \(CD\). Write
\[
A=(k,0),\quad B=(1,0),\quad D=(kt,0?).
\]
Actually, since \(AD\parallel BC\), the coordinates satisfy
\[
A=(k,0),\quad B=(1,0),\quad C=(0,t),\quad D=(0,kt).
\]
Set
\[
A_0=1+k,\qquad L=1-k,\qquad q=\cos\theta,\qquad s=\sin\theta,
\]
where \(\theta\) is the angle between the legs. In these coordinates the Euclidean quadratic form is
\[
Q(u,v)=u^2+v^2+2quv.
\]

The circle through \(A,B\) with inscribed angle \(\alpha\) has equation
\[
S_\alpha:Q(u,v)-A_0u-B_\alpha v+k=0,
\]
where
\[
B_\alpha=qA_0+Ls\cot\alpha.
\]
The circle through \(C,D\) with inscribed angle \(\beta\) has equation
\[
S_\beta:Q(u,v)-tB_\beta u-A_0t\,v+kt^2=0,
\]
with
\[
B_\beta=qA_0+Ls\cot\beta.
\]

Now use the standard center-radius formula for a circle
\[
Q(u,v)+lu+mv+n=0.
\]
Its center and radius satisfy
\[
O=-\frac12 G^{-1}\binom{l}{m},\qquad R^2=\frac14 l^2G^{-1}\binom{lm}{m^2}-n,
\]
where \(G=\begin{pmatrix}1&q\\q&1\end{pmatrix}\).

For \(S_\alpha\) and \(S_\beta\), the tangency condition \(d=R_\alpha\pm R_\beta\) is equivalent to
\[
(L_\alpha^T G^{-1}L_\alpha+L_\beta^T G^{-1}L_\beta)
-(L_\alpha^TG^{-1}L_\beta+L_\beta^TG^{-1}L_\alpha)
=2(R_\alpha^2+R_\beta^2)\pm 4R_\alpha R_\beta.
\]
After expanding, the only terms involving the two angles are symmetric polynomials in \(B_\alpha\) and \(B_\beta\), namely \(B_\alpha+B_\beta\) and \(B_\alpha B_\beta\). Hence the tangency condition can be written as
\[
\Phi(B_\alpha,B_\beta)=0,
\]
where \(\Phi(x,y)\) is symmetric:
\[
\Phi(x,y)=\Phi(y,x).
\]

But \(W_3\) corresponds to replacing \(B_\alpha\) by \(B_\beta\), while \(W_4\) corresponds to replacing \(B_\beta\) by \(B_\alpha\). Thus the tangency condition for \(W_3,W_4\) is exactly
\[
\Phi(B_\beta,B_\alpha)=0.
\]
Since \(\Phi\) is symmetric, this is the same as
\[
\Phi(B_\alpha,B_\beta)=0,
\]
which is precisely the hypothesis that \(W_1,W_2\) are tangent.

Therefore \(W_3\) and \(W_4\) must be tangent to each other.

\[
\boxed{(W_3)\text{ and }(W_4)\text{ are tangent.}}
\]

</details>

<details><summary>A10: Almost (6/7)</summary>

Let \(P=AB\cap CD\). Since \(AD\parallel BC\), the triangles \(PAD\) and \(PBC\) are similar; hence there exist \(a,d>0\) and \(\lambda>1\) such that, after placing \(P\) at the origin in the complex plane and taking the angle bisector of the legs as the real axis,

\[
A=a u,\quad B=\lambda a u,\quad D=d v,\quad C=\lambda d v,
\]
where \(u=e^{i\theta}\), \(v=e^{-i\theta}\), so \(v=\overline u\).

Define

\[
a_0=\frac{a(1+\lambda)}2,\quad b_0=\frac{a(\lambda-1)}2,
\]
\[
d_0=\frac{d(1+\lambda)}2,\quad e_0=\frac{d(\lambda-1)}2.
\]

Let

\[
q=\cot\alpha,\qquad r=\cot\beta.
\]

The circle \(W_1\) through \(A,B\) has center on the side of \(AB\) containing \(C,D\), so

\[
O_1=u(a_0-i b_0q)=u z_1,
\qquad
z_1=a_0-i b_0q.
\]

The circle \(W_2\) through \(C,D\) has center on the side of \(CD\) containing \(A,B\), so

\[
O_2=v(d_0+i e_0r)=v z_2,
\qquad
z_2=d_0+i e_0r.
\]

Similarly,

\[
O_3=u(a_0-i b_0r)=u z_3,
\qquad
O_4=v(d_0+i e_0q)=v z_4,
\]

where

\[
z_3=a_0-i b_0r,\qquad z_4=d_0+i e_0q.
\]

Let \(w=u^2\). The radii are

\[
R_1=b_0\sqrt{1+q^2},\quad
R_2=e_0\sqrt{1+r^2},
\]
\[
R_3=b_0\sqrt{1+r^2},\quad
R_4=e_0\sqrt{1+q^2}.
\]

Thus

\[
R_1R_2=R_3R_4.
\]

Also,

\[
|z_1|^2=R_1^2+a^2\lambda,\qquad
|z_2|^2=R_2^2+d^2\lambda,
\]
\[
|z_3|^2=R_3^2+a^2\lambda,\qquad
|z_4|^2=R_4^2+d^2\lambda.
\]

Now

\[
D_{12}^2=|O_2-O_1|^2
=|z_2-wz_1|^2
=R_1^2+R_2^2+\lambda(a^2+d^2)-2K,
\]

where

\[
K=\Re(z_2\overline w\,\overline{z_1}).
\]

Because \(W_1\) and \(W_2\) are tangent, there is a sign \(\varepsilon\in\{\pm1\}\) such that

\[
D_{12}^2=R_1^2+R_2^2+2\varepsilon R_1R_2.
\]

Hence

\[
\lambda(a^2+d^2)-2K=2\varepsilon R_1R_2. \tag{1}
\]

Now observe that

\[
z_2\overline z_1=(d_0+i e_0r)(a_0+i b_0q)
=d_0a_0-e_0b_0qr+iP(q+r),
\]

where

\[
P=d_0b_0=e_0a_0.
\]

Similarly,

\[
z_4\overline z_3=(d_0+i e_0q)(a_0+i b_0r)
=d_0a_0-e_0b_0qr+iP(q+r).
\]

Therefore

\[
z_4\overline z_3=z_2\overline z_1.
\]

Consequently, if we define

\[
K'=\Re(z_4\overline w\,\overline{z_3}),
\]

then

\[
K'=K.
\]

For the circles \(W_3,W_4\), we get

\[
D_{34}^2=|O_4-O_3|^2
=R_3^2+R_4^2+\lambda(a^2+d^2)-2K'
=R_3^2+R_4^2+\lambda(a^2+d^2)-2K.
\]

Using (1) and \(R_1R_2=R_3R_4\),

\[
D_{34}^2=R_3^2+R_4^2+2\varepsilon R_3R_4
=(R_3+\varepsilon R_4)^2.
\]

Thus the distance between the centers of \(W_3\) and \(W_4\) equals either the sum or the difference of their radii. Hence \(W_3\) and \(W_4\) are tangent.

\[
\boxed{\text{Therefore }(W_3)\text{ and }(W_4)\text{ are tangent.}}
\]

</details>

<details><summary>A11: Incorrect (0/7)</summary>

Let \(P=AB\cap CD\). Since \(AD\parallel BC\), the two legs \(AB\) and \(CD\) meet at \(P\), and the correspondence
\[
A\mapsto D,\qquad B\mapsto C
\]
is realized by an orientation-reversing similarity centered at \(P\).

Use complex coordinates with \(P=0\), \(AB\) as the real axis, and \(CD\) in direction \(z\), \(|z|=1\). Because \(AD\parallel BC\), there are constants \(r,k>0\) such that, after writing \(D=zd\), \(C=kdz\),
\[
A=rd,\qquad B=krd.
\]
Define the anti-linear similarity
\[
T(w)=\frac{z}{r}\overline w.
\]
Then
\[
T(A)=D,\qquad T(B)=C,
\]
and also
\[
r^2T(D)=A,\qquad r^2T(C)=B.
\]

Now \(T\) maps circles to circles and preserves angles, but reverses orientation. Hence it maps
\[
W_1 \quad\longmapsto\quad W_4,
\]
because \(W_1\) passes through \(A,B\) with angle \(\alpha\), while \(W_4\) is the circle through \(C,D\) with angle \(\alpha\).

Similarly, \(T\) maps \(W_2\) to a circle through points on \(AB\) whose image after the homothety of ratio \(r^2\) is exactly the circle through \(A,B\) with angle \(\beta\), namely \(W_3\). Thus
\[
W_3=r^2T(W_2).
\]

Since \(W_1\) and \(W_2\) are tangent, applying the similarity \(T\) gives tangency between their images:
\[
T(W_1)\text{ is tangent to }T(W_2).
\]
But
\[
T(W_1)=W_4,\qquad T(W_2)=r^{-2}W_3.
\]
Therefore \(W_4\) is tangent to \(W_3\), i.e. \(W_3\) and \(W_4\) are tangent.

\[
\boxed{(W_3),(W_4)\text{ are tangent.}}
\]

</details>

<details><summary>A12: Almost (6/7)</summary>

Let \(P=AB\cap CD\). Since \(AB\) and \(CD\) are the legs of the trapezoid, \(AD\parallel BC\). Put \(P\) at the origin, take \(AB\) as the real axis, and write  
\[
A=a,\qquad D=d e^{i\theta},\qquad B=\lambda a,\qquad C=\lambda d e^{i\theta}
\]
for some \(\lambda>0,\ \lambda\ne 1\). Indeed \(AD\parallel BC\) gives \(BC=\lambda AD\).

Define
\[
u=\frac{|\lambda-1|a}{2},\qquad v=\frac{|\lambda-1|d}{2},\qquad 
k=\frac{1+\lambda}{|1-\lambda|}>1.
\]
Then the midpoint of \(AB\) is \(ku\) on the real axis, and the midpoint of \(CD\) is \(kv e^{i\theta}\). Also
\[
AB=2u,\qquad CD=2v.
\]

For a chord of length \(2u\), the radius of the circle through \(A,B\) with inscribed angle \(\alpha\) on the side opposite \(C,D\) is
\[
R_1=\frac{u}{\sin\alpha}.
\]
Thus the center of \(W_1\) is
\[
O_1=ku+i u\cot\alpha=u(k+i\cot\alpha).
\]
Similarly, for \(W_2\) through \(C,D\) with angle \(\beta\),
\[
O_2=kv e^{i\theta}-i v\cot\beta\,e^{i\theta}
      =v e^{i\theta}(k-i\cot\beta),
\]
and
\[
R_2=\frac{v}{\sin\beta}.
\]

Now
\[
|O_1|^2-R_1^2=u^2(k^2-1),\qquad
|O_2|^2-R_2^2=v^2(k^2-1).
\]
Let \(d_{12}=|O_2-O_1|\). Then
\[
d_{12}^2=R_1^2+R_2^2+S,
\]
where
\[
\begin{aligned}
S&=(u^2+v^2)(k^2-1)
 -2uv\Big[(k^2-\cot\alpha\cot\beta)\cos\theta
 +k(\cot\alpha+\cot\beta)\sin\theta\Big].
\end{aligned}
\]
Since \(W_1\) and \(W_2\) are tangent,
\[
d_{12}=R_1+R_2 \quad\text{or}\quad d_{12}=|R_1-R_2|,
\]
so
\[
S=d_{12}^2-R_1^2-R_2^2=\pm 2R_1R_2
=\pm \frac{2uv}{\sin\alpha\sin\beta}.
\]

Now consider the circles \(W_3,W_4\). By the same chord-center formulas,
\[
O_3=u(k+i\cot\beta),\qquad R_3=\frac{u}{\sin\beta},
\]
and
\[
O_4=v e^{i\theta}(k-i\cot\alpha),\qquad R_4=\frac{v}{\sin\alpha}.
\]
For these two circles,
\[
d_{34}^2=|O_4-O_3|^2=R_3^2+R_4^2+S,
\]
because the expression for \(S\) is unchanged when \(\alpha\) and \(\beta\) are interchanged:
\[
S=(u^2+v^2)(k^2-1)
-2uv\Big[(k^2-\cot\beta\cot\alpha)\cos\theta
 +k(\cot\beta+\cot\alpha)\sin\theta\Big].
\]
Also
\[
R_3R_4=\frac{uv}{\sin\beta\sin\alpha}
        =\frac{uv}{\sin\alpha\sin\beta}
        =R_1R_2.
\]
Therefore
\[
d_{34}^2=R_3^2+R_4^2\pm 2R_3R_4
=(R_3+R_4)^2
\quad\text{or}\quad
(R_3-R_4)^2.
\]
Hence
\[
d_{34}=R_3+R_4
\quad\text{or}\quad
d_{34}=|R_3-R_4|,
\]
which is exactly the condition for two circles to be tangent.

Thus \((W_3)\) and \((W_4)\) are tangent. \(\square\)

</details>

<details><summary>A13: Almost (6/7)</summary>

\[
\boxed{\text{(W}_3\text{),(W}_4\text{) are tangent.}}
\]

Let \(P=AB\cap CD\). Since \(AD\parallel BC\), triangles \(PAD\) and \(PBC\) are similar, so after a similarity we may put
\[
P=0,\qquad B=1,\qquad A=k,\qquad C=t e^{i\theta},\qquad D=k t e^{i\theta}
\]
for some \(k>0,\ k\ne 1\), \(t>0\), \(\theta\in(0,\pi)\).

Set
\[
s=\frac{k+1}{2},\qquad r=\frac{|k-1|}{2},
\]
so that
\[
s^2-r^2=k.
\]
The chord \(AB\) has midpoint \(s\) and half-length \(r\). Hence the circle \(W_1\) through \(A,B\) has center
\[
u=s+i r\cot\alpha
\]
and radius
\[
R=\frac r{\sin\alpha}.
\]
Indeed,
\[
|u|^2=R^2+k.
\]

Similarly, for the chord \(CD\), the circle \(W_2\) has center
\[
t e^{i\theta}\overline v
\]
and radius
\[
tS=\frac{tr}{\sin\beta},
\]
where
\[
v=s+i r\cot\beta,\qquad S=\frac r{\sin\beta},
\]
and
\[
|v|^2=S^2+k.
\]

Because \(W_1\) and \(W_2\) are tangent, the distance between their centers satisfies
\[
|u-t e^{i\theta}\overline v|^2=(R\pm tS)^2.
\]
Expanding,
\[
|u|^2+t^2|v|^2-2t\Re(u e^{-i\theta}v)
=R^2+t^2S^2\pm 2tRS.
\]
Using \(|u|^2=R^2+k\) and \(|v|^2=S^2+k\), we get
\[
k(1+t^2)-2t\Re(u e^{-i\theta}v)=\pm 2tRS. \tag{1}
\]

Now consider the constructed circles:
\[
W_3:\ |z-v|^2=S^2,
\]
\[
W_4:\ |z-t e^{i\theta}\overline u|^2=t^2R^2.
\]
Their centers are \(v\) and \(t e^{i\theta}\overline u\), with radii \(S\) and \(tR\), respectively. The squared distance between their centers is
\[
\begin{aligned}
|v-t e^{i\theta}\overline u|^2
&=|v|^2+t^2|u|^2-2t\Re(v e^{-i\theta}u)\\
&=S^2+k+t^2R^2+t^2k-2t\Re(u e^{-i\theta}v)\\
&=S^2+t^2R^2+k(1+t^2)-2t\Re(u e^{-i\theta}v).
\end{aligned}
\]
By (1),
\[
k(1+t^2)-2t\Re(u e^{-i\theta}v)=\pm 2tRS.
\]
Therefore
\[
|v-t e^{i\theta}\overline u|^2
=S^2+t^2R^2\pm 2tRS
=(S\pm tR)^2.
\]
Thus the distance between the centers of \(W_3\) and \(W_4\) equals the sum or absolute difference of their radii \(S\) and \(tR\). Hence the two circles are tangent.

\[
\boxed{(W_3)\text{ and }(W_4)\text{ are tangent to each other.}}
\]

</details>

<details><summary>A14: Almost (6/7)</summary>

Let \(E=AB\cap CD\). Since \(AD\parallel BC\), triangles \(EAD\) and \(EBC\) are similar, so with \(E\) as origin we may write
\[
B=b\mathbf u,\quad A=\lambda b\mathbf u,\quad 
C=c\mathbf v,\quad D=\lambda c\mathbf v
\]
for some \(\lambda>1\) and unit vectors \(\mathbf u,\mathbf v\). Put \(\mathbf u=(1,0)\), \(\mathbf v=(\cos\theta,\sin\theta)\).

Let
\[
p=\frac{(\lambda-1)b}{2},\qquad q=\frac{(\lambda-1)c}{2},
\]
so \(AB=2p,\ CD=2q\). Also set
\[
X=\frac{(\lambda+1)b}{2},\qquad Y=\frac{(\lambda+1)c}{2}.
\]
Then
\[
X^2-p^2=\lambda b^2,\qquad Y^2-q^2=\lambda c^2.
\]

For a chord of length \(2p\) subtending angle \(\alpha\), the radius is \(p\csc\alpha\). Hence, with signed coordinates,
\[
O_1=(X,-p\cot\alpha),\qquad 
O_2=Y(\cos\theta,\sin\theta)+q\cot\beta(-\sin\theta,\cos\theta).
\]
Thus
\[
R_1=p\csc\alpha,\qquad R_2=q\csc\beta,
\]
and
\[
R_3=p\csc\beta,\qquad R_4=q\csc\alpha,
\]
so
\[
R_3R_4=R_1R_2.
\]

Now compute the dot product of the centers of \(W_1,W_2\):
\[
O_1\cdot O_2
=\cos\theta\,(XY-pq\cot\alpha\cot\beta)
-\sin\theta\,(Xq\cot\beta+Yp\cot\alpha).
\]
For the circles \(W_3,W_4\), their centers are
\[
O_3=(X,-p\cot\beta),\qquad 
O_4=Y(\cos\theta,\sin\theta)+q\cot\alpha(-\sin\theta,\cos\theta).
\]
Hence
\[
O_3\cdot O_4
=\cos\theta\,(XY-pq\cot\alpha\cot\beta)
-\sin\theta\,(Xq\cot\alpha+Yp\cot\beta).
\]
Since
\[
Xq=Yp=\frac{(\lambda^2-1)bc}{4},
\]
the two \(\sin\theta\)-terms are equal. Therefore
\[
O_3\cdot O_4=O_1\cdot O_2. \tag{1}
\]

Also,
\[
|O_1|^2=R_1^2+\lambda b^2,\qquad |O_2|^2=R_2^2+\lambda c^2.
\]
Thus
\[
|O_1O_2|^2=R_1^2+R_2^2+\lambda(b^2+c^2)-2O_1\cdot O_2.
\]
Because \(W_1,W_2\) are tangent,
\[
|O_1O_2|^2=R_1^2+R_2^2\pm 2R_1R_2.
\]
Therefore
\[
\lambda(b^2+c^2)-2O_1\cdot O_2=\pm 2R_1R_2. \tag{2}
\]

For \(W_3,W_4\), similarly,
\[
|O_3O_4|^2=R_3^2+R_4^2+\lambda(b^2+c^2)-2O_3\cdot O_4.
\]
Using (1) and (2),
\[
|O_3O_4|^2
=R_3^2+R_4^2\pm 2R_1R_2
=R_3^2+R_4^2\pm 2R_3R_4.
\]
Hence
\[
|O_3O_4|=R_3+R_4
\]
or
\[
|O_3O_4|=|R_3-R_4|.
\]
Thus \(W_3\) and \(W_4\) are tangent.

\[
\boxed{\text{Therefore }(W_3)\text{ and }(W_4)\text{ are tangent.}}
\]

</details>

<details><summary>A15: Incorrect (0/7)</summary>

Let \(P=AB\cap CD\). Since \(AD\parallel BC\), the triangles \(PAB\) and \(PDC\) are similar, so there is a direct spiral similarity \(T\) centered at \(P\) sending  
\[
A\mapsto D,\qquad B\mapsto C.
\]
In particular \(T\) sends the line \(AB\) to the line \(CD\), and it preserves angles.

For brevity denote:
\[
W_\alpha=(W_1),\qquad W_\beta=(W_2),
\]
where \(W_\alpha\) is the circle through \(A,B\) with angle \(\alpha\), and \(W_\beta\) is the circle through \(C,D\) with angle \(\beta\).

Because \(T\) is a similarity, it maps circles to circles and preserves angles. It sends the chord \(AB\) to the chord \(DC\) of \(W_\beta\), and it sends the arc \(AB\) on the side opposite \(C,D\) to the arc \(DC\) on the side opposite \(A,B\). Hence
\[
T(W_\alpha)=W_\beta,\qquad T^{-1}(W_\beta)=W_\alpha.
\]
Similarly,
\[
T^{-1}(W_\beta)=W_\alpha \quad\text{and}\quad T(W_\alpha)=W_\beta.
\]
Wait: more precisely, \(T\) swaps the two families:
\[
T(W_\alpha)=W_\beta,\qquad T(W_\beta)=W_\alpha.
\]
Thus
\[
T^{-1}(W_\alpha)=W_\beta,\qquad T^{-1}(W_\beta)=W_\alpha.
\]

Since \(W_1=W_\alpha\) is tangent to \(W_2=W_\beta\), applying the similarity \(T^{-1}\) gives
\[
W_\beta \text{ tangent } W_\alpha.
\]
But by definition, \(W_3=W_\beta\) and \(W_4=W_\alpha\). Therefore
\[
W_3 \text{ tangent } W_4.
\]

Hence the two constructed circles are tangent.

\[
\boxed{W_3\text{ and }W_4\text{ are tangent.}}
\]

</details>

<details><summary>A16: Almost (5/7)</summary>

\[
\boxed{\text{We prove the required tangency.}}
\]

Let \(P=AB\cap CD\). Since \(AD\parallel BC\), the triangles \(PAD\) and \(PBC\) are similar, so there is \(k>1\) and \(m>0\) such that
\[
A=kB,\qquad D=kC
\]
as vectors from \(P\). Choose coordinates with \(P=(0,0)\), \(B=(1,0)\), \(A=(k,0)\), and let the direction of \(CD\) be
\[
v=(\gamma,s),\qquad \gamma=\cos\theta,\quad s=\sin\theta .
\]
Then
\[
C=m v,\qquad D=kmv .
\]
Put
\[
L=k-1,\qquad a=\frac{k+1}{2},\qquad b=am.
\]
Thus \(AB=L\), \(CD=mL\), and
\[
AD=k\,BC .
\]

Let
\[
u=(1,0),\qquad v=(\gamma,s),\qquad n_1=(0,1),\qquad n_2=(s,-\gamma).
\]
Then \(n_1\perp u\), \(n_2\perp v\), \(u\cdot v=\gamma\), and \(n_1\cdot n_2=-\gamma\).

For \(W_1\), whose chord is \(AB\), write
\[
O_1=a u+Y n_1.
\]
Since \(AB=L\) and the angle subtended by the arc on the side opposite \(C,D\) is \(\alpha\),
\[
Y=\frac L2\cot\alpha,\qquad R_1=\frac L{2\sin\alpha}.
\]
Similarly, for \(W_2\),
\[
O_2=am\,v+H n_2,\qquad H=\frac{mL}{2}\cot\beta,\qquad R_2=\frac{mL}{2\sin\beta}.
\]

The power of \(P\) with respect to \(W_1\) is
\[
\Pi_1=O_1P^2-R_1^2=a^2+Y^2-\left(Y^2+\frac{L^2}{4}\right)
=a^2-\frac{L^2}{4}=k.
\]
Similarly,
\[
\Pi_2=O_2P^2-R_2^2=k m^2.
\]
Hence
\[
\Pi_1+\Pi_2=k(1+m^2).
\]

Now write
\[
E=2O_1\cdot O_2-2R_1R_2.
\]
Using \(O_1\cdot O_2=O_3\cdot O_4\) after swapping \(\alpha,\beta\), one obtains
\[
E=2am^2\gamma+amLs(\cot\alpha+\cot\beta)
-\gamma mL^2\cot\alpha\cot\beta
-\frac{mL^2}{2\sin\alpha\sin\beta}.
\]
This expression is symmetric in \(\alpha,\beta\).

The tangency condition between \(W_1,W_2\) is exactly
\[
E=k(1+m^2)
\quad\text{or}\quad
E=k(1+m^2)-4R_1R_2.
\]
Indeed, if \(OO'=R_1+R_2\) or \(OO'=|R_1-R_2|\), then
\[
OO'^2=R_1^2+R_2^2+\Pi_1+\Pi_2-2O_1\cdot O_2
\]
gives the displayed two possibilities for \(E\).

Now define \(W_3,W_4\) as in the problem. They have centers
\[
O_3=a u+\frac L2\cot\beta\,n_1,\qquad
O_4=am\,v+\frac{mL}{2}\cot\alpha\,n_2,
\]
and radii
\[
R_3=\frac L{2\sin\beta},\qquad R_4=\frac{mL}{2\sin\alpha}.
\]
A direct expansion gives
\[
O_3\cdot O_4=O_1\cdot O_2,\qquad R_3R_4=R_1R_2.
\]
Therefore
\[
E_{34}:=2O_3\cdot O_4-2R_3R_4=E_{12}.
\]
Also
\[
\Pi_3+\Pi_4=\Pi_1+\Pi_2=k(1+m^2),
\]
and
\[
4R_3R_4=4R_1R_2.
\]
Thus \(E_{34}\) is the same value satisfying one of the two tangency conditions for \(W_1,W_2\). Hence \(W_3,W_4\) are tangent to each other.

\[
\boxed{\text{Therefore }(W_3)\text{ and }(W_4)\text{ are tangent.}}
\]

</details>
