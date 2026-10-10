# PB-Basic-025

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Given a triangle $XYZ$ with circumcenter $O$, the incircle of triangle
 $XYZ$ has center $I$. Let $M,N$ on the sides $XY,XZ$
 respectively such that $YM=ZN=YZ$. If $\gamma$ is the angle created
 by two lines $MN,OI$, what is $\frac{\gamma}{2}$ in terms of degree?

## Swarm: accepted (best candidate `P3`; self-verification grades [7, 7, 7]; 679,297 tokens in 65 calls)

**Blind grade: Correct (7/7).** With X at the origin and the bisector as x-axis, M, N, O=((b+c)/(4q),(b-c)/(4s)) and I=(2bcq/p,0) are computed correctly and MN.(O-I)=Delta((S-a)/2-qd)=0 via S^2-a^2=4bcq^2, a complete rigorous proof of perpendicularity.

Let \(a=YZ,\ b=ZX,\ c=XY\), and let \(\theta=\frac12\angle X\). Put  
\[
q=\cos\theta,\qquad s=\sin\theta.
\]
Place \(X\) at the origin and the internal angle bisector of \(\angle X\) along the \(x\)-axis. Then we may take
\[
Y=(cq,-cs),\qquad Z=(bq,bs).
\]

Since \(YM=ZN=a\), we have
\[
XM=c-a,\qquad XN=b-a,
\]
so
\[
M=((c-a)q,-(c-a)s),\qquad N=((b-a)q,(b-a)s).
\]
Hence
\[
\overrightarrow{MN}
=\big((b-c)q,\,(b+c-2a)s\big).
\]

The circumcenter \(O\) satisfies
\[
O\cdot Y=\frac{c^2}{2},\qquad O\cdot Z=\frac{b^2}{2},
\]
which gives
\[
O=\left(\frac{b+c}{4q},\frac{b-c}{4s}\right).
\]

Let \(I=(d,0)\) be the incenter. Since the distance from \(I\) to either side through \(X\) is \(ds\), we have \(r=ds\). Also
\[
[XYZ]=\frac12bc\sin 2\theta=bcsq=\frac{rs_p}{2}=\frac{dsp}{2},
\]
where \(p=a+b+c\). Thus
\[
d=\frac{2bcq}{p}.
\]

Now set \(S=b+c\), \(\Delta=b-c\). A direct computation gives
\[
\overrightarrow{MN}\cdot(O-I)=0.
\]
Indeed,
\[
\overrightarrow{MN}\cdot(O-I)
=\Delta\left(\frac{S-a}{2}-qd\right).
\]
But
\[
S^2-a^2=4bcq^2,
\]
so
\[
\frac{S-a}{2}=\frac{S^2-a^2}{2(S+a)}
=\frac{4bcq^2}{2p}=qd.
\]
Therefore
\[
\overrightarrow{MN}\cdot(O-I)=0,
\]
so \(MN\perp OI\).

Thus \(\gamma=90^\circ\), and therefore
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 6.94/7; graded Correct: 15 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 41,007 | Correct (7/7) | Trigonometric coordinates using the standard facts I = (s-a, r) and r/R = cos A + cos B + cos C - 1 give explicit OI and MN, and the dot product correctly reduces to sin(A+B) - sin C = 0, so gamma/2 = 45 degrees. |
| A2 | stop | 14,303 | Correct (7/7) | Vector computation from X correctly shows d.o = d.i = (b-c)(b+c-a)/2 using incenter barycentrics and the law of cosines, so MN is perpendicular to OI and gamma/2 = 45 degrees. |
| A3 | stop | 29,247 | Correct (7/7) | Trig-coordinate bash with Y=(0,0), Z=(1,0) correctly gets MN=(d_x,d_y), OI=(u/2, -d_x/(2 sin A)) with d_y=u sin A (all stated identities, incl. I_x=(1+c-b)/2 and r-(1/2)cot A=-d_x/(2 sin A), verify), so MN.OI=0 and gamma/2=45 degrees. |
| A4 | stop | 13,007 | Correct (7/7) | Vector proof with X at origin correctly reduces (o-i).MN to (b-c)((b+c-a)/2-T/s) and uses T/s=(b+c-a)/2 to get zero, a complete and rigorous proof that OI is perpendicular to MN. |
| A5 | stop | 20,712 | Correct (7/7) | Clean vector argument showing I.u = I.v = s-a and O.u = c/2, O.v = b/2, hence MN.OI = qp/2 - pq/2 = 0, a complete and correct proof that gamma/2 = 45 degrees. |
| A6 | stop | 30,902 | Correct (7/7) | Trig-coordinate proof with MN=(1-2pC,2pV) and OI=(V/(2q),-(1-2pC)/(4pq)); the incenter coordinates are stated tersely but are correct (I_x=(1+c-b)/2, I_y=r), and the dot product vanishes, so gamma/2=45 degrees. |
| A7 | stop | 28,694 | Correct (7/7) | Cartesian computation with YZ=1 is fully correct (w_x=(c-b)/2, the factorization (1+c-b)(c-u), and 2(c+u)=S(1+c-b) all check), proving MN.OI=0 and hence gamma/2=45 degrees. |
| A8 | stop | 32,975 | Correct (7/7) | Half-angle coordinate bash: the briefly stated identities xi=sin(s-q)/(2cos p), eta=-D_x/(2 sin 2p) and D_y=2 sin 2p xi are all correct on checking, so MN.(I-O)=0 and gamma/2=45 degrees. |
| A9 | stop | 35,702 | Correct (7/7) | Vector computation from Y with YZ = 1 correctly establishes 2 MN.i = (c+1-b)(alpha c + beta) = alpha c^2 + beta = 2 MN.o via verified factorizations, so MN is perpendicular to OI and gamma/2 = 45 degrees; only trivial substitutions are left implicit. |
| A10 | stop | 21,234 | Correct (7/7) | Unit-vector setup with I = (bc/p)(u+v), O.u = c/2, O.v = b/2 correctly reduces MN.OI to [(b-c)(b+c-a) - b(b-a) + c(c-a)]/2 = 0, proving MN is perpendicular to OI and gamma/2 = 45 degrees. |
| A11 | stop | 34,509 | Correct (7/7) | With YZ on the x-axis, MN = a(S,T) and, using I_x = s-b and r = R(cos alpha + cos beta + cos delta - 1), OI = R(T,-S) is a normal to MN, a correct and complete proof that gamma/2 = 45 degrees. |
| A12 | stop | 16,156 | Correct (7/7) | Vector proof with Y at origin shows O.E=I.E=(ac/2)(c-a)(a+c-b) for the direction E=a(c-b)x+c(b-a)z of MN, all computations verified, so OI is perpendicular to MN and gamma/2=45 degrees. |
| A13 | stop | 15,698 | Correct (7/7) | Coordinates along the bisector of angle X give MN, O and I = (d,0) with d cos(theta) = s-a, and MN.OI is correctly shown to vanish, giving gamma/2 = 45 degrees (the 'OA=OB=OC' typo is harmless). |
| A14 | stop | 15,077 | Correct (7/7) | Clean vector proof with X at origin: W=I-O satisfies W.y=c(b-a)/2 and W.z=b(c-a)/2 (verified), so W.MN=(b-a)(c-a)/2-(b-a)(c-a)/2=0, giving OI perpendicular to MN and gamma/2=45 degrees. |
| A15 | stop | 19,991 | Correct (7/7) | Complete vector computation from X (incenter barycentrics, o.y = c^2/2, o.z = b^2/2, law of cosines) correctly shows v.i = v.o = (b-c)(b+c-a)/2, so MN is perpendicular to OI and gamma/2 = 45 degrees. |
| A16 | stop | 39,315 | Almost (6/7) | Correct coordinate setup and correct conclusion, but the crucial simplification of OI to ((c-b)/2, -A/(2v)) is only asserted as a 'direct simplification' with no computation shown (it does check out), a minor gap in the key step. |

<details><summary>A1: Correct (7/7)</summary>

Let  
\[
A=\angle YXZ,\quad B=\angle XYZ,\quad C=\angle XZY,
\]
and let \(R\) be the circumradius. Then
\[
YZ=2R\sin A,\quad ZX=2R\sin B,\quad XY=2R\sin C.
\]

Place \(X=(0,0)\), \(Y=(2R\sin C,0)\). Then the circumcenter is
\[
O=(R\sin C,R\cos C).
\]
Also, if \(r\) is the inradius and \(s\) the semiperimeter, then
\[
I=(s-a,r)
\]
where \(a=YZ\). Since \(s=R(\sin A+\sin B+\sin C)\),
\[
I_x-O_x=R(\sin B-\sin A).
\]
Using the standard identity
\[
\frac rR=\cos A+\cos B+\cos C-1,
\]
we get
\[
I_y-O_y=r-R\cos C=R(\cos A+\cos B-1).
\]
Thus
\[
\overrightarrow{OI}
=R\bigl(\sin B-\sin A,\ \cos A+\cos B-1\bigr).
\]

Now
\[
XM=XY-YZ=2R(\sin C-\sin A),
\]
so
\[
M=\bigl(2R(\sin C-\sin A),0\bigr).
\]
Also
\[
XN=XZ-YZ=2R(\sin B-\sin A),
\]
so
\[
N=2R(\sin B-\sin A)(\cos A,\sin A).
\]
Hence
\[
\overrightarrow{MN}
=2R\bigl((\sin B-\sin A)\cos A-(\sin C-\sin A),\ 
(\sin B-\sin A)\sin A\bigr).
\]

Let \(p=\sin B-\sin A\). Then
\[
\overrightarrow{MN}=2R(p\cos A-\sin C+\sin A,\ p\sin A),
\]
while
\[
\overrightarrow{OI}=R(p,\ \cos A+\cos B-1).
\]
Therefore
\[
\frac{\overrightarrow{MN}\cdot \overrightarrow{OI}}{2R^2}
=p\Bigl(p\cos A-\sin C+\sin A+\sin A(\cos A+\cos B-1)\Bigr).
\]
But
\[
p\cos A-\sin C+\sin A+\sin A(\cos A+\cos B-1)
\]
\[
=(\sin B-\sin A)\cos A-\sin C+\sin A+\sin A\cos A+\sin A\cos B-\sin A
\]
\[
=\sin B\cos A-\sin C+\sin A\cos B
=\sin(A+B)-\sin C=0.
\]
Thus
\[
\overrightarrow{MN}\cdot \overrightarrow{OI}=0,
\]
so \(MN\perp OI\). Hence the angle between the two lines is
\[
\gamma=90^\circ.
\]
Therefore
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

Let  
\[
a=YZ,\qquad b=ZX,\qquad c=XY,
\]
and put the origin at \(X\). Write
\[
\vec Y=\mathbf y,\qquad \vec Z=\mathbf z,
\]
so
\[
|\mathbf y|=c,\qquad |\mathbf z|=b,\qquad |\mathbf y-\mathbf z|=a.
\]

Since \(YM=a\), along \(XY\) we have
\[
\overrightarrow{XM}=\frac{c-a}{c}\mathbf y=\alpha \mathbf y,\qquad 
\alpha=\frac{c-a}{c}.
\]
Similarly,
\[
\overrightarrow{XN}=\frac{b-a}{b}\mathbf z=\beta \mathbf z,\qquad 
\beta=\frac{b-a}{b}.
\]
Thus a direction vector of \(MN\) is
\[
\mathbf d=\overrightarrow{MN}=\beta \mathbf z-\alpha \mathbf y.
\]

Let \(O\) and \(I\) have position vectors \(\mathbf o\) and \(\mathbf i\), respectively. Since \(O\) is equidistant from \(X,Y,Z\),
\[
\mathbf o\cdot \mathbf y=\frac{c^2}{2},\qquad 
\mathbf o\cdot \mathbf z=\frac{b^2}{2}.
\]
Also, using the standard barycentric form of the incenter,
\[
\mathbf i=\frac{b\mathbf y+c\mathbf z}{a+b+c}.
\]
Let \(p=a+b+c\) and \(q=\mathbf y\cdot \mathbf z\). By the law of cosines,
\[
q=\frac{b^2+c^2-a^2}{2}.
\]

Now
\[
\mathbf d\cdot \mathbf o
=\frac12(\beta b^2-\alpha c^2)
=\frac12\bigl[b(b-a)-c(c-a)\bigr]
=\frac12(b-c)(b+c-a).
\]

On the other hand,
\[
\mathbf d\cdot \mathbf i
=\frac{(\beta b-\alpha c)(q+bc)}{p}.
\]
Since \(\beta b-\alpha c=(b-a)-(c-a)=b-c\), and
\[
q+bc=\frac{b^2+c^2-a^2+2bc}{2}
=\frac{(b+c)^2-a^2}{2}
=\frac{(b+c-a)(a+b+c)}2,
\]
we get
\[
\mathbf d\cdot \mathbf i
=\frac{(b-c)(b+c-a)}2.
\]
Therefore
\[
\mathbf d\cdot \mathbf o=\mathbf d\cdot \mathbf i,
\]
so
\[
\mathbf d\cdot(\mathbf i-\mathbf o)=0.
\]
Hence
\[
MN\perp OI.
\]

Thus the angle between \(MN\) and \(OI\) is
\[
\gamma=90^\circ,
\]
and therefore
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

\[
\boxed{\frac{\gamma}{2}=45^\circ}
\]

Below is a self-contained proof.

Let  
\[
A=\angle X,\quad B=\angle Y,\quad C=\angle Z,
\]
and scale the triangle so that
\[
YZ=1.
\]
Place
\[
Y=(0,0),\qquad Z=(1,0).
\]

Since \(YM=YZ=1\), the point \(M\) lies on the unit circle centered at \(Y\) along ray \(YX\), so
\[
M=(\cos B,\sin B).
\]
Similarly,
\[
N=(1-\cos C,\sin C).
\]
Thus
\[
\overrightarrow{MN}
=
(d_x,d_y),
\]
where
\[
d_x=1-\cos B-\cos C,\qquad d_y=\sin C-\sin B.
\]

Now the circumcenter \(O\) lies on the perpendicular bisector of \(YZ\), so \(O=(1/2,O_y)\). Since \(YZ=1\),
\[
R=\frac1{2\sin A},
\]
and therefore
\[
O_y=\frac12\cot A.
\]
Hence
\[
O=\left(\frac12,\frac12\cot A\right).
\]

For the incenter, write \(b=ZX,\ c=XY\). By the sine rule,
\[
b=\frac{\sin B}{\sin A},\qquad c=\frac{\sin C}{\sin A}.
\]
Using barycentric coordinates for the incenter,
\[
I=\frac{X+cZ}{1+b+c}.
\]
A direct simplification gives
\[
I_x=\frac{c+1-b}{2},
\]
while \(I_y=r\), the inradius. Therefore
\[
\overrightarrow{OI}
=
\left(\frac{c-b}{2},\ r-\frac12\cot A\right).
\]

Let \(u=c-b\). Since
\[
u=\frac{\sin C-\sin B}{\sin A}=\frac{d_y}{\sin A},
\]
we have \(d_y=u\sin A\).

It remains to simplify the vertical component of \(\overrightarrow{OI}\). Put
\[
p=\sin\frac A2,\qquad q=\cos\frac A2,\qquad t=\frac{C-B}{2}.
\]
Then
\[
d_x=1-\cos B-\cos C=1-2p\cos t,
\]
and using
\[
r=4R\sin\frac A2\sin\frac B2\sin\frac C2
=\frac{\cos t-p}{2q},
\]
we get
\[
r-\frac12\cot A
=
-\frac{d_x}{2\sin A}.
\]
Thus
\[
\overrightarrow{OI}
=
\left(\frac u2,\ -\frac{d_x}{2\sin A}\right).
\]

Now compute the dot product:
\[
\overrightarrow{OI}\cdot \overrightarrow{MN}
=
\frac u2 d_x
-\frac{d_x}{2\sin A}\,d_y.
\]
Since \(d_y=u\sin A\),
\[
\overrightarrow{OI}\cdot \overrightarrow{MN}
=
\frac{u d_x}{2}-\frac{u d_x}{2}=0.
\]
Therefore
\[
OI\perp MN.
\]
So the angle between \(MN\) and \(OI\) is
\[
\gamma=90^\circ.
\]
Hence
\[
\frac{\gamma}{2}=\frac{90^\circ}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

Let  
\[
a=YZ,\qquad b=ZX,\qquad c=XY,
\]
and put \(X\) at the origin. Write
\[
\vec y=\overrightarrow{XY},\qquad \vec z=\overrightarrow{XZ}.
\]
Then
\[
|\vec y|=c,\qquad |\vec z|=b,\qquad |\vec z-\vec y|=a.
\]

Since \(YM=a\) and \(ZN=a\), we have
\[
M=\frac{c-a}{c}\vec y,\qquad N=\frac{b-a}{b}\vec z.
\]
Thus
\[
\overrightarrow{MN}=\frac{b-a}{b}\vec z-\frac{c-a}{c}\vec y. \tag{1}
\]

Let \(O\) and \(I\) have position vectors \(\vec o\) and \(\vec i\). The circumcenter satisfies
\[
\vec o\cdot \vec y=\frac{c^2}{2},\qquad 
\vec o\cdot \vec z=\frac{b^2}{2}. \tag{2}
\]
The incenter has barycentric coordinates \(a:b:c\), so with \(s=a+b+c\),
\[
\vec i=\frac{b\vec y+c\vec z}{s}. \tag{3}
\]

Now set
\[
q=\vec y\cdot \vec z=\frac{b^2+c^2-a^2}{2},\qquad T=q+bc.
\]
Then
\[
T=\frac{(b+c)^2-a^2}{2}=\frac{(b+c-a)s}{2},
\]
so
\[
\frac{T}{s}=\frac{b+c-a}{2}. \tag{4}
\]

Using (2) and (3),
\[
\vec i\cdot \vec y=\frac{cT}{s},\qquad 
\vec i\cdot \vec z=\frac{bT}{s}.
\]
Hence
\[
(\vec o-\vec i)\cdot \vec z
=\frac{b^2}{2}-\frac{bT}{s}
=b\left(\frac b2-\frac Ts\right),
\]
and similarly
\[
(\vec o-\vec i)\cdot \vec y
=c\left(\frac c2-\frac Ts\right).
\]

Now compute:
\[
\begin{aligned}
(\vec o-\vec i)\cdot \overrightarrow{MN}
&=\frac{b-a}{b}(\vec o-\vec i)\cdot \vec z
-\frac{c-a}{c}(\vec o-\vec i)\cdot \vec y\\
&=(b-a)\left(\frac b2-\frac Ts\right)
-(c-a)\left(\frac c2-\frac Ts\right)\\
&=(b-c)\left(\frac{b+c-a}{2}-\frac Ts\right)=0
\end{aligned}
\]
by (4). Therefore
\[
(\vec o-\vec i)\cdot \overrightarrow{MN}=0,
\]
so
\[
OI\perp MN.
\]

Thus the angle between \(MN\) and \(OI\) is \(90^\circ\), so
\[
\gamma=90^\circ,\qquad \frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

\[
\boxed{45^\circ}
\]

Proof:

Let
\[
a=YZ,\qquad b=ZX,\qquad c=XY,
\]
and put \(S=a+b+c\). Place \(X\) at the origin. Let \(\mathbf u,\mathbf v\) be unit vectors along \(XY,XZ\), respectively, so
\[
Y=c\mathbf u,\qquad Z=b\mathbf v,\qquad \mathbf u\cdot \mathbf v=\cos X.
\]

Since \(YM=YZ=a\), we have \(XM=c-a\), hence
\[
M=(c-a)\mathbf u.
\]
Similarly \(ZN=a\) gives
\[
N=(b-a)\mathbf v.
\]
Set
\[
p=c-a,\qquad q=b-a.
\]
Then a direction vector of \(MN\) is
\[
\vec{MN}=N-M=q\mathbf v-p\mathbf u.
\]

Now consider the incenter \(I\). Since \(I\) lies on the internal angle bisector of \(\angle X\), write
\[
I=\lambda(\mathbf u+\mathbf v).
\]
The distance from \(I\) to \(XY\) is \(r=\lambda\sin X\). Also
\[
r=\frac{\Delta}{s}=\frac{bc\sin X}{S},
\]
so \(\lambda=\frac{bc}{S}\). Thus
\[
I\cdot \mathbf u=I\cdot \mathbf v
=\frac{bc}{S}(1+\cos X).
\]
Using the law of cosines,
\[
1+\cos X=\frac{(b+c)^2-a^2}{2bc}
=\frac{(b+c-a)S}{2bc},
\]
so
\[
I\cdot \mathbf u=I\cdot \mathbf v=\frac{b+c-a}{2}=s-a.
\]

For the circumcenter \(O\), since \(O\) is on the perpendicular bisector of \(XY\) and \(XZ\),
\[
O\cdot \mathbf u=\frac c2,\qquad O\cdot \mathbf v=\frac b2.
\]
Therefore, for \(w=\overrightarrow{OI}=I-O\),
\[
w\cdot \mathbf u=(s-a)-\frac c2=\frac{b-a}{2}=\frac q2,
\]
and
\[
w\cdot \mathbf v=(s-a)-\frac b2=\frac{c-a}{2}=\frac p2.
\]

Now compute
\[
\vec{MN}\cdot w=(q\mathbf v-p\mathbf u)\cdot w
=q(w\cdot \mathbf v)-p(w\cdot \mathbf u).
\]
Substituting the values above,
\[
\vec{MN}\cdot w
=q\cdot \frac p2-p\cdot \frac q2=0.
\]
Hence
\[
MN\perp OI.
\]
Thus the angle between the two lines is
\[
\gamma=90^\circ,
\]
so
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45}
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

\[
\boxed{45^\circ}
\]

Here is a complete proof.

Scale the triangle so that \(YZ=1\). Put
\[
Y=(0,0),\qquad Z=(1,0),
\]
and let
\[
\alpha=\angle YXZ,\quad \beta=\angle XYZ,\quad \delta=\angle XZY.
\]
Set \(t=\alpha/2\), \(u=(\delta-\beta)/2\), and write
\[
p=\sin t,\quad q=\cos t,\quad C=\cos u,\quad V=\sin u.
\]

Since \(YM=ZN=YZ=1\), the unit vectors along \(YX\) and \(ZX\) give
\[
M=(\cos\beta,\sin\beta),\qquad N=(1-\cos\delta,\sin\delta).
\]
Thus
\[
\overrightarrow{MN}
=(1-\cos\beta-\cos\delta,\ \sin\delta-\sin\beta).
\]
Using \(\beta=\frac\pi2-t-u,\ \delta=\frac\pi2-t+u\), we get
\[
\cos\beta+\cos\delta=2pC,\qquad \sin\delta-\sin\beta=2pV,
\]
so
\[
\overrightarrow{MN}=(1-2pC,\;2pV). \tag{1}
\]

Now compute the direction of \(OI\). The circumcenter lies on \(x=\frac12\), and
\[
O=\left(\frac12,\frac12\cot\alpha\right)
=\left(\frac12,\frac{q^2-p^2}{4pq}\right).
\]

For the incenter, using barycentric coordinates
\[
I=\frac{X+XY\cdot Z}{1+XY+XZ},
\]
one obtains
\[
I=\left(\frac{q+V}{2q},\frac{C-p}{2q}\right).
\]
Therefore
\[
\overrightarrow{OI}
=
\left(\frac{V}{2q},\frac{C-p}{2q}-\frac{q^2-p^2}{4pq}\right).
\]
Simplifying the second coordinate,
\[
\frac{C-p}{2q}-\frac{q^2-p^2}{4pq}
=
\frac{2pC-1}{4pq}
=
-\frac{1-2pC}{4pq}.
\]
Hence
\[
\overrightarrow{OI}
=
\left(\frac{V}{2q},-\frac{1-2pC}{4pq}\right). \tag{2}
\]

Now dot the two vectors from (1) and (2):
\[
\overrightarrow{MN}\cdot \overrightarrow{OI}
=
(1-2pC)\frac{V}{2q}
+(2pV)\left(-\frac{1-2pC}{4pq}\right).
\]
But
\[
\frac{2pV}{4pq}=\frac{V}{2q},
\]
so the expression is \(0\). Hence
\[
\overrightarrow{MN}\cdot \overrightarrow{OI}=0,
\]
meaning \(MN\perp OI\).

Therefore the angle between the two lines is
\[
\gamma=90^\circ,
\]
so
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

\[
\boxed{45^\circ}
\]

Here is a rigorous proof.

Scale the triangle so that \(YZ=1\). Place
\[
Y=(0,0),\qquad Z=(1,0),\qquad X=(u,v),\quad v>0.
\]
Let
\[
b=ZX,\qquad c=XY,\qquad S=1+b+c.
\]
Then
\[
u^2+v^2=c^2,\qquad (u-1)^2+v^2=b^2,
\]
so
\[
2u=c^2-b^2+1. \tag{1}
\]

The circumcenter is
\[
O=\left(\frac12,\frac{c^2-u}{2v}\right),
\]
and the incenter, using barycentrics \((1:b:c)\), is
\[
I=\frac{X+cZ}{S}
=\left(\frac{u+c}{S},\frac vS\right).
\]

Since \(YM=ZN=1\),
\[
M=\left(\frac u c,\frac v c\right),
\qquad
N=\left(1+\frac{u-1}{b},\frac v b\right).
\]
Let
\[
\mathbf d=N-M=(d_x,d_y).
\]
Writing \(r=c-b\), we get
\[
d_y=\frac{vr}{bc},
\]
and from (1),
\[
bc\,d_x=c(b-1)+ur. \tag{2}
\]
Also
\[
\overrightarrow{OI}=I-O=(w_x,w_y),
\]
where
\[
w_x=\frac{u+c}{S}-\frac12
=\frac{2u+c-b-1}{2S}
=\frac{rS}{2S}
=\frac r2.
\]
Thus
\[
\overrightarrow{MN}\cdot \overrightarrow{OI}
=d_x\frac r2+d_yw_y
=\frac r{2bc}\bigl(bc\,d_x+2v w_y\bigr).
\]

Now
\[
2v w_y=2v\left(\frac vS-\frac{c^2-u}{2v}\right)
=\frac{2v^2}{S}-(c^2-u).
\]
Therefore
\[
bc\,d_x+2v w_y
=bc\,d_x+\frac{2v^2}{S}-(c^2-u).
\]
Using (2),
\[
bc\,d_x+\frac{2v^2}{S}-(c^2-u)
=\frac{2v^2}{S}-(c^2-u-c(b-1)-ur).
\]
But
\[
c^2-u-c(b-1)-ur=(1+c-b)(c-u).
\]
Hence
\[
bc\,d_x+2v w_y
=\frac{2v^2}{S}-(1+c-b)(c-u).
\]
Since \(v^2=c^2-u^2=(c-u)(c+u)\), this becomes
\[
(c-u)\left(\frac{2(c+u)}{S}-(1+c-b)\right).
\]
Finally,
\[
2(c+u)=2c+c^2-b^2+1=(1+c)^2-b^2
=(1+c-b)(1+b+c)=S(1+c-b),
\]
so the expression is \(0\). Thus
\[
\overrightarrow{MN}\cdot \overrightarrow{OI}=0.
\]

So \(MN\perp OI\). Therefore
\[
\gamma=90^\circ,
\qquad
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

\[
\boxed{45^\circ}
\]

Let  
\[
\angle X=2p,\qquad \angle Y=2q,\qquad \angle Z=2s,
\]
so \(p+q+s=\pi/2\). Scale so that \(YZ=1\), and place
\[
Y=(0,0),\qquad Z=(1,0).
\]

Since \(YM=YZ=1\), point \(M\) lies on the ray making angle \(2q\) with \(YZ\), so
\[
M=(\cos 2q,\sin 2q).
\]
Similarly, since \(ZN=YZ=1\), from \(Z\) toward \(X\),
\[
N=(1-\cos 2s,\sin 2s).
\]
Thus a direction vector of \(MN\) is
\[
\vec d=\overrightarrow{MN}
=(1-\cos2q-\cos2s,\ \sin2s-\sin2q)=(D_x,D_y).
\]

The circumcenter lies on the perpendicular bisector of \(YZ\), so
\[
O=\left(\frac12,\frac12\cot 2p\right).
\]
For the incenter, write \(I=(r\cot q,r)\), where \(r\) is the inradius. Using
\[
r=4R\sin p\sin q\sin s,\qquad R=\frac1{2\sin 2p},
\]
we get
\[
r=\frac{\sin q\sin s}{\cos p}
=\frac{\cos(q-s)-\sin p}{2\cos p}.
\]
Hence, with \(\xi=I_x-\frac12\),
\[
\xi=\frac{\sin(s-q)}{2\cos p},
\]
and with \(\eta=I_y-\frac12\cot2p\),
\[
\eta=-\frac{D_x}{2\sin 2p}.
\]

Also,
\[
D_y=\sin2s-\sin2q
=2\sin p\sin(s-q)
=2\sin 2p\,\xi.
\]
Therefore
\[
\vec d\cdot (I-O)
=D_x\xi+D_y\eta
=D_x\xi+(2\sin2p\,\xi)\left(-\frac{D_x}{2\sin2p}\right)=0.
\]
So
\[
MN\perp OI.
\]
Hence \(\gamma=90^\circ\), and therefore
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

Let \(YZ=1\) after a scaling (angles are unchanged). Set
\[
b=ZX,\qquad c=XY,\qquad P=1+b+c.
\]
Place \(Y\) at the origin, and write
\[
\mathbf x=\overrightarrow{YX},\qquad \mathbf z=\overrightarrow{YZ},
\]
so \(|\mathbf z|=1,\ |\mathbf x|=c,\ |\mathbf x-\mathbf z|=b\).

Since \(YM=ZN=1\),
\[
M=\frac1c\mathbf x,\qquad 
N=\frac1b\mathbf x+\left(1-\frac1b\right)\mathbf z.
\]
Thus
\[
\overrightarrow{MN}
=\left(\frac1b-\frac1c\right)\mathbf x+\left(1-\frac1b\right)\mathbf z
=\alpha \mathbf x+\beta \mathbf z,
\]
where
\[
\alpha=\frac1b-\frac1c,\qquad \beta=1-\frac1b.
\]

The incenter has position vector
\[
\mathbf i=\frac{\mathbf x+c\mathbf z}{P}.
\]
Let \(\mathbf o\) be the circumcenter. Since \(O\) is equidistant from \(Y,Z\) and from \(Y,X\),
\[
\mathbf o\cdot \mathbf z=\frac12,\qquad 
\mathbf o\cdot \mathbf x=\frac{c^2}{2}.
\]

Let \(q=\mathbf x\cdot \mathbf z\). From
\[
b^2=|\mathbf x-\mathbf z|^2=c^2+1-2q,
\]
we get
\[
q+c=\frac{P(c+1-b)}2,\qquad 
c^2+cq=\frac{Pc(c+1-b)}2.
\]
A direct expansion gives
\[
(c+1-b)(\alpha c+\beta)=\alpha c^2+\beta,
\]
because
\[
(c+1-b)(\alpha c+\beta)-(\alpha c^2+\beta)
=\alpha c(1-b)+\beta(c-b)=0.
\]
Therefore
\[
2\overrightarrow{MN}\cdot \mathbf i
=\alpha c^2+\beta
=2\overrightarrow{MN}\cdot \mathbf o.
\]
Hence
\[
\overrightarrow{MN}\cdot(\mathbf i-\mathbf o)=0.
\]
But \(\mathbf i-\mathbf o=\overrightarrow{OI}\), so
\[
MN\perp OI.
\]
Thus the angle between the two lines is
\[
\gamma=90^\circ,
\]
and therefore
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

\[
\boxed{45^\circ}
\]

Proof:

Let  
\[
a=YZ,\qquad b=ZX,\qquad c=XY,\qquad p=a+b+c.
\]
Place \(X\) at the origin. Let \(\mathbf u,\mathbf v\) be unit vectors along \(XY,XZ\), and write
\[
\mathbf u\cdot \mathbf v=\cos \angle YXZ=:q.
\]
Then
\[
Y=c\mathbf u,\qquad Z=b\mathbf v,
\]
and
\[
a^2=b^2+c^2-2bcq.
\]

Since \(YM=a\) on \(XY\), we have
\[
M=(c-a)\mathbf u.
\]
Similarly,
\[
N=(b-a)\mathbf v.
\]
Set
\[
A=c-a,\qquad B=b-a,
\]
so
\[
\overrightarrow{MN}=B\mathbf v-A\mathbf u.
\]

The incenter lies on the angle bisector of \(\angle X\), so
\[
I=t(\mathbf u+\mathbf v).
\]
Its distance to \(XY\) is \(t\sin\angle X\), while the inradius satisfies
\[
r=\frac{bc\sin\angle X}{p}.
\]
Hence
\[
t=\frac{bc}{p},
\]
so
\[
I=\frac{bc}{p}(\mathbf u+\mathbf v).
\]

Let \(O\) be the circumcenter. Since \(O\) is equidistant from \(X\) and \(Y\),
\[
O\cdot \mathbf u=\frac c2.
\]
Similarly,
\[
O\cdot \mathbf v=\frac b2.
\]

Now compute the dot product:
\[
\overrightarrow{MN}\cdot \overrightarrow{OI}
=(B\mathbf v-A\mathbf u)\cdot \left(\frac{bc}{p}(\mathbf u+\mathbf v)-O\right).
\]
Expanding,
\[
\overrightarrow{MN}\cdot \overrightarrow{OI}
=(B-A)\frac{bc(q+1)}p-\frac{Bb}{2}+\frac{Ac}{2}.
\]
Since \(A=c-a,\ B=b-a\), we have \(B-A=b-c\). Also, by the law of cosines,
\[
bc(q+1)=\frac{(b+c)^2-a^2}{2}
=\frac{(b+c-a)(a+b+c)}2,
\]
so
\[
\frac{bc(q+1)}p=\frac{b+c-a}{2}.
\]
Therefore
\[
\overrightarrow{MN}\cdot \overrightarrow{OI}
=
\frac{(b-c)(b+c-a)-b(b-a)+c(c-a)}2.
\]
But
\[
(b-c)(b+c-a)-b(b-a)+c(c-a)=0.
\]
Hence
\[
\overrightarrow{MN}\cdot \overrightarrow{OI}=0.
\]
Thus
\[
MN\perp OI.
\]

So the angle between \(MN\) and \(OI\) is
\[
\gamma=90^\circ.
\]
Therefore
\[
\frac{\gamma}{2}=\frac{90^\circ}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

\[
\boxed{45^\circ}
\]

Proof:

Let  
\[
a=YZ,\qquad \alpha=\angle X,\quad \beta=\angle Y,\quad \delta=\angle Z,
\]
and let \(R\) be the circumradius. Place
\[
Y=(0,0),\qquad Z=(a,0).
\]

Since \(YM=YZ=a\), the point \(M\) lies on \(XY\) at distance \(a\) from \(Y\). As \(XY\) makes angle \(\beta\) with \(YZ\),
\[
M=(a\cos\beta,a\sin\beta).
\]
Similarly, since \(ZN=a\),
\[
N=(a-a\cos\delta,a\sin\delta).
\]
Thus
\[
\overrightarrow{MN}
=a\bigl(1-\cos\beta-\cos\delta,\ \sin\delta-\sin\beta\bigr).
\]
Let
\[
S=1-\cos\beta-\cos\delta,\qquad T=\sin\delta-\sin\beta.
\]
Then \(\overrightarrow{MN}=a(S,T)\), so a normal vector to \(MN\) is
\[
\mathbf n=(T,-S)=\bigl(\sin\delta-\sin\beta,\ \cos\beta+\cos\delta-1\bigr).
\]

Now the circumcenter has coordinates
\[
O=(R\sin\alpha,R\cos\alpha).
\]
For the incenter, using \(I_x=s-b=R(\sin\alpha+\sin\delta-\sin\beta)\) and
\[
r=R(\cos\alpha+\cos\beta+\cos\delta-1),
\]
we get
\[
\overrightarrow{OI}
=
\bigl(I_x-O_x,I_y-O_y\bigr)
=
R\bigl(\sin\delta-\sin\beta,\ \cos\beta+\cos\delta-1\bigr)
=R\mathbf n.
\]
Hence \(OI\parallel \mathbf n\), while \(\mathbf n\perp MN\). Therefore
\[
MN\perp OI.
\]
So the angle between the two lines is
\[
\gamma=90^\circ.
\]
Hence
\[
\frac{\gamma}{2}=\frac{90^\circ}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

\[
\boxed{45^\circ}
\]

Proof:

Let \(Y\) be the origin, and write
\[
\mathbf x=\overrightarrow{YX},\qquad \mathbf z=\overrightarrow{YZ}.
\]
Set
\[
a=YZ,\quad b=ZX,\quad c=XY,\quad p=a+b+c.
\]
Then
\[
|\mathbf x|=c,\qquad |\mathbf z|=a,\qquad |\mathbf x-\mathbf z|=b,
\]
so
\[
\mathbf x\cdot \mathbf z=\frac{a^2+c^2-b^2}{2}.
\]

Since \(YM=YZ=a\), we have
\[
M=\frac{a}{c}\mathbf x.
\]
Since \(ZN=YZ=a\), along side \(ZX\),
\[
N=\mathbf z+\frac{a}{b}(\mathbf x-\mathbf z)
=\frac{a}{b}\mathbf x+\left(1-\frac ab\right)\mathbf z.
\]
Thus
\[
\overrightarrow{MN}
=N-M
=\frac{a(c-b)}{bc}\mathbf x+\frac{b-a}{b}\mathbf z.
\]
Multiplying by \(bc\), a direction vector for \(MN\) is
\[
E=a(c-b)\mathbf x+c(b-a)\mathbf z.
\]

Let \(\mathbf o,\mathbf i\) be the position vectors of \(O,I\). Because \(O\) is the circumcenter,
\[
2\mathbf o\cdot \mathbf x=c^2,\qquad 2\mathbf o\cdot \mathbf z=a^2.
\]
Also, using the standard incenter barycentric formula,
\[
\mathbf i=\frac{a\mathbf x+c\mathbf z}{p}.
\]

Now compute:
\[
O\cdot E
=\frac{a(c-b)c^2+c(b-a)a^2}{2}
=\frac{ac}{2}(c-a)(a+c-b).
\]

On the other hand,
\[
(a\mathbf x+c\mathbf z)\cdot E
=ac(c-a)(ac+\mathbf x\cdot \mathbf z).
\]
Therefore
\[
I\cdot E
=\frac{ac(c-a)(ac+q)}{p},
\]
where \(q=\mathbf x\cdot\mathbf z\). But
\[
ac+q=ac+\frac{a^2+c^2-b^2}{2}
=\frac{(a+c)^2-b^2}{2}
=\frac{p(a+c-b)}2.
\]
Hence
\[
I\cdot E=\frac{ac}{2}(c-a)(a+c-b)=O\cdot E.
\]
So
\[
(I-O)\cdot E=0.
\]
Thus \(OI\perp MN\). Therefore the angle between the two lines is
\[
\gamma=90^\circ,
\]
and consequently
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

Let  
\[
a=YZ,\qquad b=ZX,\qquad c=XY,\qquad s=\frac{a+b+c}{2}.
\]
Put \(\theta=\frac12\angle YXZ\). Place \(X\) at the origin and the internal angle bisector of \(\angle X\) on the \(x\)-axis, so
\[
Y=(c\cos\theta,c\sin\theta),\qquad Z=(b\cos\theta,-b\sin\theta).
\]

Since \(YM=ZN=a\), we have
\[
XM=c-a,\qquad XN=b-a,
\]
hence
\[
M=((c-a)\cos\theta,(c-a)\sin\theta),
\]
\[
N=((b-a)\cos\theta,-(b-a)\sin\theta).
\]
Therefore
\[
\overrightarrow{MN}
=\big((b-c)\cos\theta,\,(2a-b-c)\sin\theta\big). \tag{1}
\]

Let \(O=(u,v)\). From \(OA=OB=OC\),
\[
u\cos\theta+v\sin\theta=\frac c2,\qquad
u\cos\theta-v\sin\theta=\frac b2.
\]
Solving,
\[
u=\frac{b+c}{4\cos\theta},\qquad v=\frac{c-b}{4\sin\theta}. \tag{2}
\]

The incenter \(I\) lies on the \(x\)-axis, say \(I=(d,0)\). Since its distance to side \(XY\) equals the inradius \(r\),
\[
d\sin\theta=r=\frac{\Delta}{s}.
\]
Now \(\Delta=bc\sin\theta\cos\theta\), so
\[
d=\frac{bc\cos\theta}{s}.
\]
Using
\[
\cos^2\theta=\frac{s(s-a)}{bc},
\]
we get
\[
d\cos\theta=s-a. \tag{3}
\]

Now
\[
\overrightarrow{OI}=(d-u,-v).
\]
Using (1), (2), and (3),
\[
\begin{aligned}
\overrightarrow{MN}\cdot \overrightarrow{OI}
&=(b-c)\cos\theta(d-u)+(2a-b-c)\sin\theta(-v)\\
&=(b-c)\left((d-u)\cos\theta+\frac{2a-b-c}{4}\right)\\
&=(b-c)\left(d\cos\theta-\frac{b+c-a}{2}\right)\\
&=(b-c)\bigl((s-a)-(s-a)\bigr)=0.
\end{aligned}
\]
Thus \(\overrightarrow{MN}\perp \overrightarrow{OI}\), so the angle between the lines \(MN\) and \(OI\) is
\[
\gamma=90^\circ.
\]
Hence
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

Let  
\[
a=YZ,\qquad b=ZX,\qquad c=XY,
\]
and put \(X\) at the origin. Write
\[
\vec y=\overrightarrow{XY},\qquad \vec z=\overrightarrow{XZ},
\]
so \(|\vec y|=c,\ |\vec z|=b\).

Since \(YM=YZ=a\), the point \(M\) on \(XY\) satisfies
\[
\overrightarrow{XM}=\frac{c-a}{c}\vec y=:\alpha \vec y,\qquad 
\alpha=\frac{c-a}{c}.
\]
Similarly,
\[
\overrightarrow{XN}=\frac{b-a}{b}\vec z=:\beta \vec z,\qquad 
\beta=\frac{b-a}{b}.
\]
Thus
\[
\overrightarrow{MN}=\beta \vec z-\alpha \vec y.
\]

Let \(O\) be the circumcenter. Since \(O\) is equidistant from \(X\) and \(Y\),
\[
O\cdot \vec y=\frac{|\vec y|^2}{2}=\frac{c^2}{2},
\]
and similarly
\[
O\cdot \vec z=\frac{b^2}{2}.
\]

The incenter has barycentrics \((a:b:c)\), so with \(p=a+b+c\),
\[
I=\frac{b\vec y+c\vec z}{p}.
\]
Using \(\vec y\cdot \vec z=\frac{b^2+c^2-a^2}{2}\), one obtains
\[
I\cdot \vec y=\frac{c(b+c-a)}2,\qquad 
I\cdot \vec z=\frac{b(b+c-a)}2.
\]
Hence for \(W=I-O\),
\[
W\cdot \vec y=\frac{c(b-a)}2,\qquad 
W\cdot \vec z=\frac{b(c-a)}2.
\]

Now compute
\[
W\cdot \overrightarrow{MN}
=(\beta \vec z-\alpha \vec y)\cdot W
=\beta(W\cdot \vec z)-\alpha(W\cdot \vec y).
\]
Substitute \(\alpha,\beta\) and the above dot products:
\[
\beta(W\cdot \vec z)
=\frac{b-a}{b}\cdot \frac{b(c-a)}2
=\frac{(b-a)(c-a)}2,
\]
and
\[
\alpha(W\cdot \vec y)
=\frac{c-a}{c}\cdot \frac{c(b-a)}2
=\frac{(b-a)(c-a)}2.
\]
Therefore
\[
W\cdot \overrightarrow{MN}=0.
\]
So \(OI\perp MN\). Thus the angle between the two lines is
\[
\gamma=90^\circ.
\]
Consequently,
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

Let  
\[
a=YZ,\qquad b=ZX,\qquad c=XY,\qquad p=a+b+c.
\]
Place \(X\) at the origin, and write
\[
\mathbf y=\overrightarrow{XY},\qquad \mathbf z=\overrightarrow{XZ}.
\]
Then \(|\mathbf y|=c,\ |\mathbf z|=b\). Put \(\mathbf y\cdot \mathbf z=d\).

Since \(YM=a\), we have \(XM=c-a\), so
\[
M=\frac{c-a}{c}\mathbf y.
\]
Similarly, since \(ZN=a\),
\[
N=\frac{b-a}{b}\mathbf z.
\]
Thus a direction vector of \(MN\) is
\[
\mathbf v=\overrightarrow{MN}
=\frac{b-a}{b}\mathbf z-\frac{c-a}{c}\mathbf y.
\]

Let \(\mathbf i=\overrightarrow{XI}\). The incenter has barycentric coordinates \((a:b:c)\), hence
\[
\mathbf i=\frac{b\mathbf y+c\mathbf z}{p}.
\]
Using \(\mathbf y\cdot\mathbf z=d\), we get
\[
\mathbf i\cdot\mathbf y=\frac{c(bc+d)}p,\qquad 
\mathbf i\cdot\mathbf z=\frac{b(bc+d)}p.
\]

Let \(\mathbf o=\overrightarrow{XO}\). Since \(O\) is the circumcenter,
\[
\mathbf o\cdot\mathbf y=\frac{c^2}{2},\qquad 
\mathbf o\cdot\mathbf z=\frac{b^2}{2}.
\]

Now compute:
\[
\mathbf v\cdot\mathbf i
=\frac{b-a}{b}(\mathbf i\cdot\mathbf z)-\frac{c-a}{c}(\mathbf i\cdot\mathbf y)
=\frac{(b-a)-(c-a)}p(bc+d)
=\frac{(b-c)(bc+d)}p.
\]
On the other hand,
\[
\mathbf v\cdot\mathbf o
=\frac{b-a}{b}\frac{b^2}{2}-\frac{c-a}{c}\frac{c^2}{2}
=\frac{b(b-a)-c(c-a)}2
=\frac{(b-c)(b+c-a)}2.
\]

But
\[
bc+d=bc+\frac{b^2+c^2-a^2}{2}
=\frac{(b+c)^2-a^2}{2}
=\frac{(b+c-a)p}{2},
\]
so
\[
\frac{bc+d}{p}=\frac{b+c-a}{2}.
\]
Therefore
\[
\mathbf v\cdot\mathbf i
=(b-c)\frac{bc+d}{p}
=(b-c)\frac{b+c-a}{2}
=\mathbf v\cdot\mathbf o.
\]
Hence
\[
\mathbf v\cdot(\mathbf i-\mathbf o)=0.
\]
Since \(\mathbf i-\mathbf o=\overrightarrow{OI}\), the direction of \(OI\) is perpendicular to \(\mathbf v\), the direction of \(MN\). Thus
\[
MN\perp OI.
\]

So \(\gamma=90^\circ\), and therefore
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>

<details><summary>A16: Almost (6/7)</summary>

Let \(YZ=1\) by scaling. Place
\[
Y=(0,0),\qquad Z=(1,0),\qquad X=(u,v),\quad v>0.
\]
Set
\[
b=XZ,\qquad c=XY,\qquad P=1+b+c,
\]
so
\[
b^2=(u-1)^2+v^2,\qquad c^2=u^2+v^2.
\]

Since \(YM=ZN=YZ=1\),
\[
M=\left(\frac u c,\frac v c\right),\qquad 
N=\left(1+\frac{u-1}{b},\frac v b\right).
\]
Thus
\[
\vec{MN}
=
\left(
\frac{A}{bc},\frac{v(c-b)}{bc}
\right),
\qquad
A=c(b-1)+u(c-b).
\]

The circumcenter is
\[
O=\left(\frac12,\frac{c^2-u}{2v}\right),
\]
and the incenter, by the standard barycentric formula, is
\[
I=\left(\frac{u+c}{P},\frac vP\right).
\]
Therefore
\[
\vec{OI}
=
\left(
\frac{c-b}{2},
\frac vP-\frac{c^2-u}{2v}
\right).
\]

A direct simplification using \(b^2=c^2-2u+1\) gives
\[
\frac vP-\frac{c^2-u}{2v}
=
-\frac{A}{2v}.
\]
Hence
\[
\vec{OI}
=
\left(
\frac{c-b}{2},
-\frac{A}{2v}
\right).
\]

Now compute the dot product:
\[
\vec{MN}\cdot \vec{OI}
=
\frac{A}{bc}\cdot\frac{c-b}{2}
+
\frac{v(c-b)}{bc}\left(-\frac{A}{2v}\right)
=0.
\]
So
\[
MN\perp OI.
\]

Thus the angle between the two lines is
\[
\gamma=90^\circ,
\]
and therefore
\[
\frac{\gamma}{2}=45^\circ.
\]

\[
\boxed{45^\circ}
\]

</details>
