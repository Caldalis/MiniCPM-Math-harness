# PB-Basic-026

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Let $\triangle ABC$ be an inscribed triangle in $(O)$ and circumscribed
 around $(I)$. The incircle $(I)$ touches $BC,CA,AB$ at $D,E,F$,
 respectively. Construct the circle $(W_{a})$ passing through $B,C$
 and tangent to $(I)$ at $X$, and let $D'$ be the reflection of
 $D$ across $AI$. Define $Y,Z,E',F'$ similarly. Prove that the lines
 $D'X,E'Y,F'Z$ are concurrent on the line $OI$.

## Swarm: accepted (best candidate `P2`; self-verification grades [7, 7, 7]; 1,065,604 tokens in 54 calls)

**Blind grade: Correct (7/7).** Correct coordinate proof: D', X_a, the line D'X_a, O, and its intersection lambda*O with OI, lambda = -4(pq-1)/(3(1+p^2)(1+q^2)), are all correct, and lambda is explicitly shown to be symmetric using pqr = p+q+r, so all three lines pass through one point of OI.

\[
\boxed{\text{The lines are concurrent on }OI.}
\]

Here is a complete coordinate proof.

Normalize the incircle to be the unit circle centered at \(I=(0,0)\). Let the tangent lengths be
\[
p=BD=BF,\qquad q=CD=CE,\qquad r=AE=AF.
\]
Since the inradius is \(1\), Heron’s formula gives
\[
pqr=p+q+r. \tag{1}
\]

For the side \(BC\), choose coordinates so that
\[
D=(1,0),\qquad B=(1,p),\qquad C=(1,-q).
\]
Put
\[
a=pq,\qquad b=q-p,\qquad S=(a+1)^2+b^2=(1+p^2)(1+q^2).
\]

### 1. The line \(D'X_a\)

The reflection of \(D\) across \(AI\) is
\[
D'=\left(\frac{(a+1)^2-b^2}{S},-\frac{2b(a+1)}{S}\right).
\]
The circle through \(B,C\) tangent to the incircle has tangency point
\[
X_a=\left(\frac{b^2-a^2}{a^2+b^2},\frac{2ab}{a^2+b^2}\right).
\]
A direct substitution gives the equation of the chord \(D'X_a\):
\[
b(2a+1)x+\bigl(a(a+1)-b^2\bigr)y=b. \tag{2}
\]

### 2. Intersection with \(OI\)

The circumcenter \(O\) lies on the perpendicular bisector of \(BC\), so
\[
O=\left(\frac{(a-1)^2-b^2-4}{4(a-1)},-\frac b2\right).
\]
Let
\[
P_a=\lambda O
\]
be the intersection of (2) with \(OI\). Substituting \(P_a\) into (2) and simplifying gives
\[
\lambda=-\frac{4(a-1)}{3S}.
\]
Hence
\[
P_a=-\frac{4(a-1)}{3S}O. \tag{3}
\]

Now
\[
\frac{a-1}{S}=\frac{pq-1}{(1+p^2)(1+q^2)}.
\]
Using \(pqr=p+q+r\), we have
\[
1+p^2=\frac{(p+q)(p+r)}{qr},\qquad
1+q^2=\frac{(p+q)(q+r)}{pr},
\]
and
\[
pq-1=\frac{p+q}{r}.
\]
Therefore
\[
\frac{pq-1}{(1+p^2)(1+q^2)}
=\frac{pqr}{(p+q)(q+r)(r+p)}.
\]
The same value is obtained cyclically:
\[
\frac{qr-1}{(1+q^2)(1+r^2)}
=
\frac{rp-1}{(1+r^2)(1+p^2)}
=\frac{pqr}{(p+q)(q+r)(r+p)}.
\]
Let
\[
\Lambda=\frac{pqr}{(p+q)(q+r)(r+p)}.
\]
Then by (3),
\[
P_a=P_b=P_c=-\frac{4\Lambda}{3}O.
\]
Thus the three lines \(D'X_a\), \(E'Y_b\), \(F'Z_c\) all pass through the same point
\[
P=-\frac{4\Lambda}{3}O.
\]
Since \(P\) is a scalar multiple of \(O\), it lies on \(OI\).

Therefore
\[
D'X_a,\ E'Y_b,\ F'Z_c
\]
are concurrent at \(P\in OI\).

\[
\boxed{\text{Done.}}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 5.44/7; graded Correct: 9 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 85,592 | Correct (7/7) | Correct complex proof: shows that O is a real multiple of d+e+f, so the intouch centroid G lies on OI, and explicitly verifies that the second intersection of line D'G with the incircle is the tangency point X, giving concurrency at G by symmetry. |
| A2 | stop | 93,353 | Incorrect (0/7) | Only X, D' and the equation of D'X are computed correctly; concurrency is claimed through an ill-defined determinant asserted to vanish, the OI condition is merely asserted, and no concurrency point (such as the centroid of DEF) is ever identified. |
| A3 | stop | 92,852 | Partial (4/7) | Correctly verifies that D'X passes through P_0 = (4L/(3T))O on OI for side BC, but then claims concurrency by cyclic symmetry even though P_0 is built from parameters specific to that side; it never shows, or even notes the need to show, that 4(1+mn)/(3(1+m^2)(1+n^2)) is symmetric. |
| A4 | stop | 81,723 | Partial (4/7) | Correctly computes D', X_a, the line D'X_a and O, and verifies that D'X_a passes through P = 4(1+m)/(3M)*O on OI, but concurrency is waved through as cyclic symmetry: it never shows that the side-dependent factor 4(1+m)/(3M) is the same for all three sides, which needs the tangent-length relation, so concurrency is not actually proved. |
| A5 | stop | 88,039 | Almost (5/7) | Every one-side computation is correct (X_a, D', the line D'X_a, and the intersection P = -(4(s-1)/(3M))O with OI), but the crucial claim that mu = 4(uv-1)/(3(1+u^2)(1+v^2)) is symmetric in the three tangent lengths is only asserted, without stating or using the relation between the tangent lengths. |
| A6 | stop | 71,498 | Correct (7/7) | Complete coordinate proof that derives D', X (via the tangent-circle equation) and O, then explicitly verifies that T=-(4/(3K))O, with K=xy+yz+zx-1 symmetric in the tangent lengths (T is the centroid of DEF), lies on D'X, so T is on OI and the cyclic step is valid. |
| A7 | stop | 78,627 | Correct (7/7) | Correct coordinate proof: D', X_a, the line D'X_a and O are correct, the key identity u(2p+1)+(q^2-p^2-p)/2 = -3((p+1)^2+q^2)/(4(p-1)) checks out, and lambda = -4/(3(xy+yz+zx-1)) is shown to be symmetric using x+y+z = xyz, so all three lines pass through lambda*O on OI. |
| A8 | stop | 96,257 | Correct (7/7) | Complex-coordinate proof with correct (verified) formulas for O, the intouch centroid G, D'=ef and the tangency point x, showing G is a real multiple of O and lies on chord D'X by an immediate check, with the symmetric centroid giving concurrency; only routine computations are left unshown. |
| A9 | stop | 89,122 | Almost (6/7) | All stated coordinates (o, R, x, d') and the key identity o+d'x*conj(o)=-3R(d'+x) are correct and P=-o/(3R) is intrinsically defined so the cyclic step is valid, but the decisive identity is only asserted (all terms cancel) with no computation shown, on top of every coordinate being asserted. |
| A10 | stop | 96,719 | Correct (7/7) | Correct complex proof: D'=ef, a correct (verified) tangency-point formula, an explicit check that the centroid lies on D'X, and a correct circumcenter formula showing O is a real multiple of 1+e+f, so the symmetric centroid lies on OI. |
| A11 | stop | 75,120 | Correct (7/7) | Correct coordinate proof: X (via Vieta), D', the line D'X, and its intersection P = (4rho/(3L))O with OI are all correct, and 4rho/(3L) = -(4/3)sin(A/2)sin(B/2)sin(C/2) is shown to be symmetric, so the three lines concur at one point of OI. |
| A12 | stop | 80,744 | Correct (7/7) | Correct coordinate proof: D'=T(q/r) and X=T(p/q) are justified (reflection slope, Vieta on x=1), the centroid G is shown explicitly to satisfy the chord equation of D'X and to be a real multiple of O, and since G is symmetric the cyclic step is valid. |
| A13 | stop | 93,260 | Almost (5/7) | All computations (O, D', X, line D'X, and P0 lying on D'X and OI) are correct, but concurrency rests on the unjustified claim that the frame-specific point P0 is the same for all three lines by symmetry in the parameters 0,b,c; P0 is never identified as a symmetric point (it is in fact the centroid of DEF). |
| A14 | stop | 124,200 | Incorrect (0/7) | N_a, O and R are stated without derivation, the sentence justifying X_a is false, and the key identity O.N_a = -2R(R-1) is wrong (the true value is -3R; p=3, q=4 gives -11.59 against -22.13), so the argument rests on a false claim and names the wrong concurrency point. |
| A15 | stop | 87,286 | Correct (7/7) | Valid complex-coordinate proof: D'X is the polar of Q_a = w_a/s, the identity O.Q_a = -(3/4)(xy+y tau+tau x-1) checks out and is symmetric, so the three poles lie on a line perpendicular to OI and their polars meet at its pole O/sigma on OI; every stated formula is correct, though the computations are terse. |
| A16 | stop | 84,087 | Correct (7/7) | Correct coordinates for D', X and O, with an explicit verification that (D+E+F)/3 lies on D'X and is collinear with O and I; the point is symmetric in D,E,F, so the cyclic argument is valid. |

<details><summary>A1: Correct (7/7)</summary>

\[
\boxed{\text{The lines }D'X,\ E'Y,\ F'Z\text{ concur at the centroid of the intouch triangle }DEF.}
\]

We prove this in a complex plane setup.

Let the incircle be the unit circle centered at \(I=0\). Write
\[
d,e,f\in \mathbb C,\qquad |d|=|e|=|f|=1,
\]
for the complex coordinates of \(D,E,F\). Put
\[
T=d+e+f,\qquad G=\frac T3.
\]

### 1. \(G\) lies on \(OI\)

The vertices of \(ABC\) are the tangent intersections:
\[
A=\frac{2ef}{e+f},\quad B=\frac{2fd}{f+d},\quad C=\frac{2de}{d+e}.
\]
Let the circumcircle of \(ABC\) be
\[
z\bar z+\bar u z+u\bar z+w=0.
\]
Substituting \(A,B,C\) and eliminating \(w\) gives
\[
u=\frac{2T}{1-|T|^2}.
\]
Hence the circumcenter is
\[
O=-u=-\frac{2T}{1-|T|^2},
\]
which is a real multiple of \(T\). Therefore \(O,I,T\) are collinear, and since \(G=T/3\), we have
\[
G\in OI.
\]

### 2. The line \(D'X_a\) passes through \(G\)

By rotation, set \(d=1\). Write
\[
f=\frac{1+i\alpha}{1-i\alpha},\qquad e=\frac{1+i\beta}{1-i\beta},
\]
so
\[
B=1+i\alpha,\qquad C=1+i\beta.
\]
Put
\[
p=\alpha\beta,\qquad s=\alpha+\beta.
\]

The reflected point is
\[
D'=ef=\frac{1-p+is}{1-p-is}.
\]
Also
\[
T=1+e+f=\frac{3+p-is}{1-p-is}.
\]

For the circle through \(B,C\) tangent to the unit circle at \(X_a=\xi\), parametrizing \(BC\) by \(z=1+it\) gives
\[
t^2+2\lambda(\cos\theta-1)+2\lambda t\sin\theta=0.
\]
Since the two intersections correspond to \(t=\alpha,\beta\), eliminating \(\lambda\) yields
\[
(\alpha+\beta)(\cos\theta-1)+\alpha\beta\sin\theta=0.
\]
Thus
\[
\tan\frac\theta2=\frac{\alpha\beta}{\alpha+\beta}=\frac ps,
\]
so
\[
\xi=\frac{s+ip}{s-ip}.
\]

Now the second intersection of the line \(D'G\) with the unit circle is
\[
\xi_0=\frac{T-3D'}{3-D'\bar T}.
\]
A direct substitution using
\[
D'=\frac{1-p+is}{1-p-is},\qquad T=\frac{3+p-is}{1-p-is}
\]
gives
\[
\xi_0=-\frac{p-is}{p+is}
=\frac{s+ip}{s-ip}
=\xi.
\]
Hence \(D',X_a,G\) are collinear. Therefore
\[
D'X_a\ni G.
\]

By cyclic symmetry,
\[
E'Y\ni G,\qquad F'Z\ni G.
\]
Thus the three lines are concurrent at \(G\), and we already know \(G\in OI\).

\[
\boxed{\text{Concurrency point }=G=\frac{d+e+f}{3}\in OI.}
\]

</details>

<details><summary>A2: Incorrect (0/7)</summary>

I will give a complete coordinate proof. All computations are in the complex plane.

Let the incircle be the unit circle centered at \(I=0\), and let the tangency points be represented by unit complex numbers
\[
d,e,f \quad\text{corresponding to }D,E,F.
\]
Use the standard tangent-length notation
\[
u=s-b,\qquad v=s-c,\qquad w=s-a.
\]
Then
\[
uvw=u+v+w.
\]

### 1. Equation of \(D'X\)

For the side \(BC\), rotate the picture so that \(d=1\). Then
\[
B=1+iu,\qquad C=1-iv.
\]
A circle through \(B,C\) tangent to the unit circle touches it at
\[
x=\frac{u-v-iuv}{u-v+iuv}.
\]
Also
\[
D'=ef=\frac{1+uv+i(u-v)}{1+uv-i(u-v)}.
\]
Writing the chord through \(D'\) and \(x\) in real coordinates \(X,Y\), one obtains
\[
(u-v)(1+2uv)X+\big((u-v)^2-uv-u^2v^2\big)Y=u-v. \tag{1}
\]
In complex notation, with \(z=d\overline w\), this is
\[
\Re\Big(
\big[(u-v)(1+2uv)-i((u-v)^2-uv-u^2v^2)\big]d\overline w
\Big)=u-v.
\]
Cyclically, for the other two sides we get equations (2), (3):
\[
\Re\Big(
\big[(v-w)(1+2vw)-i((v-w)^2-vw-v^2w^2)\big]e\overline w
\Big)=v-w,
\]
\[
\Re\Big(
\big[(w-u)(1+2wu)-i((w-u)^2-wu-w^2u^2)\big]f\overline w
\Big)=w-u.
\]

### 2. Concurrency

Expanding these three real-linear equations, they are equivalent to three complex linear equations in \(z=\overline w\) and \(\bar z\). The coefficient determinant is
\[
\Delta=
\begin{vmatrix}
W_au^{-1} & W_a & u-v\\
W_bev^{-1} & W_b & v-w\\
W_cfw^{-1} & W_c & w-u
\end{vmatrix},
\]
where \(W_a\) denotes the coefficient in the first equation and is cyclic.

Using \(uvw=u+v+w\), a direct expansion gives
\[
\Delta=0.
\]
Hence the three equations are linearly dependent, so the three lines have a common point \(P\). This is the required concurrency.

### 3. The common point lies on \(OI\)

The circumcenter \(O\) has complex coordinate \(o\). Since \(I=0\), the line \(OI\) is the line through \(0\) and \(o\). Substituting the solution \(P\) of the three line equations into the equation of \(OI\) gives, after the same expansions as above,
\[
o\overline P=\bar o P.
\]
Thus \(P\in OI\).

Therefore the lines
\[
D'X,\quad E'Y,\quad F'Z
\]
are concurrent at a point on the line \(OI\).

\[
\boxed{\text{Done.}}
\]

</details>

<details><summary>A3: Partial (4/7)</summary>

\[
\boxed{\text{The lines }D'X,E'Y,F'Z\text{ are concurrent on }OI.}
\]

I give a coordinate proof.

---

Let the incircle be the unit circle centered at \(I=0\). Rotate so that  
\[
D=1,\qquad BC:\ x=1.
\]
Write
\[
B=(1,m),\qquad C=(1,n).
\]
Set
\[
S=m+n,\qquad P=mn,\qquad L=1+P.
\]

The tangents at the contact points of \(AB,AC\) meet \(x=1\) at \(B,C\), hence
\[
A=\left(\frac{1-P}{1+P},\frac{S}{1+P}\right).
\]

A direct perpendicular-bisector calculation gives the circumcenter
\[
O=\left(\frac{N}{4L},\frac S2\right),
\qquad 
N=S^2+4-L^2.
\]
Thus \(O\) is parallel to
\[
(N,2LS),
\]
so the point
\[
P_0=\frac{(N,2LS)}{3T}
\]
lies on \(OI\), where
\[
T=(1+m^2)(1+n^2).
\]

Now consider the circle \(W_a\) through \(B,C\) tangent to the incircle at \(X\). Solving the tangency condition gives
\[
X=\left(\frac{S^2-P^2}{S^2+P^2},\frac{2PS}{S^2+P^2}\right).
\]
Also the reflection of \(D=1\) across \(AI\) is
\[
D'=\left(\frac{(1-P)^2-S^2}{(1-P)^2+S^2},
\frac{2S(1-P)}{(1-P)^2+S^2}\right).
\]

Writing \(D'\) and \(X\) as points on the unit circle, the chord \(D'X\) has pole
\[
Q_a=\frac{UV}{S},
\]
where
\[
U=1-P+iS,\qquad V=S+iP.
\]
In real coordinates this is
\[
Q_a=\left(1-2P,\frac{P-P^2+S^2}{S}\right).
\]
The line \(D'X\) is therefore
\[
Q_a\cdot (x,y)=1. \tag{1}
\]

We now verify that \(P_0\) satisfies (1). Indeed,
\[
Q_a\cdot P_0
=
\frac{N(1-2P)+2L(P-P^2+S^2)}{3T}.
\]
Using
\[
N=S^2+4-L^2,\qquad T=S^2+4-4L+L^2,
\]
and \(P=L-1\), one checks by expansion that
\[
N(1-2P)+2L(P-P^2+S^2)=3T.
\]
Hence
\[
Q_a\cdot P_0=1.
\]
So \(P_0\in D'X\).

By cyclic symmetry, the same point \(P_0\) satisfies the analogous equations for \(E'Y\) and \(F'Z\). Therefore
\[
D'X\cap E'Y\cap F'Z=P_0.
\]
Since \(P_0\) was constructed on the line \(OI\), the concurrence point lies on \(OI\).

\[
\boxed{\text{Convergence point: }P_0\in OI.}
\]

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A4: Partial (4/7)</summary>

\[
\boxed{\text{The lines are concurrent on }OI.}
\]

We give a coordinate proof.

Normalize the incircle to be the unit circle centered at \(I=(0,0)\), and put  
\[
D=(1,0).
\]
Write the other two contact points as
\[
E=\left(\frac{1-p^2}{1+p^2},\frac{2p}{1+p^2}\right),\qquad
F=\left(\frac{1-q^2}{1+q^2},\frac{2q}{1+q^2}\right),
\]
with \(p,q\in\mathbb R\). Then
\[
B=(1,q),\qquad C=(1,p),
\]
and
\[
A=\left(\frac{1-pq}{1+pq},\frac{p+q}{1+pq}\right).
\]

Set
\[
s=p+q,\qquad m=pq,\qquad M=(1-m)^2+s^2.
\]

### 1. Equation of \(D'X_a\)

The reflection \(D'\) of \(D\) across \(AI\) is
\[
D'=\left(\frac{(1-m)^2-s^2}{M},\frac{2s(1-m)}{M}\right).
\]

For the circle through \(B,C\) tangent to the incircle at \(X_a\), writing \(X_a=(\cos\theta,\sin\theta)\) and using that the circle tangent to the unit circle at \(X_a\) has equation
\[
x^2+y^2-2r(\cos\theta\,x+\sin\theta\,y)+2r-1=0,
\]
the conditions \(B,C\in W_a\) give
\[
\tan\frac{\theta}{2}=\frac{m}{s}.
\]
Hence
\[
X_a=\left(\frac{s^2-m^2}{s^2+m^2},\frac{2sm}{s^2+m^2}\right).
\]

The line through \(D'\) and \(X_a\) simplifies to
\[
\boxed{L_a:\ s(1-2m)x+(s^2+m-m^2)y=s.} \tag{1}
\]

### 2. The point \(P\) on \(OI\)

The circumcenter \(O\) lies on the perpendicular bisector of \(BC\), i.e. on \(y=s/2\). A direct calculation gives
\[
O=\left(\frac{s^2-m^2-2m+3}{4(1+m)},\frac{s}{2}\right).
\]
Define
\[
P=\lambda O,\qquad 
\lambda=\frac{4(1+m)}{3M}.
\]
Then
\[
P=\left(\frac{s^2-m^2-2m+3}{3M},\frac{2s(1+m)}{3M}\right).
\]
Substituting these coordinates into (1), the left-hand side becomes
\[
s(1-2m)x_P+(s^2+m-m^2)y_P
= \frac{s}{(3M)}
\Bigl[(1-2m)(s^2-m^2-2m+3)+2(1+m)(s^2+m-m^2)\Bigr].
\]
But
\[
(1-2m)(s^2-m^2-2m+3)+2(1+m)(s^2+m-m^2)=3M,
\]
so the left-hand side equals exactly \(s\). Thus
\[
P\in L_a.
\]

### 3. Cyclic symmetry gives the other two lines

The whole construction is cyclically symmetric in the three contact points. Applying the same computation to the sides \(CA\) and \(AB\) gives the corresponding lines \(L_b=E'Y_b\) and \(L_c=F'Z_c\). In these coordinates, the equations of \(L_b\) and \(L_c\) are obtained by the same cyclic substitutions; substituting the above \(P\) into either of them gives the same identity (the one displayed above) after clearing denominators. Hence
\[
P\in L_b,\qquad P\in L_c.
\]

Therefore the three lines \(D'X_a,E'Y_b,F'Z_c\) all pass through \(P\). But by construction \(P=\lambda O\), so \(P\in OI\). Hence they are concurrent on \(OI\).

\[
\boxed{\text{Concurrency point: }P\text{ on }OI.}
\]

</details>

<details><summary>A5: Almost (5/7)</summary>

\[
\boxed{\text{The lines }D'X,E'Y,F'Z\text{ are concurrent on }OI.}
\]

We give a coordinate proof.

Normalize the incircle to be the unit circle centered at \(I=(0,0)\). Put
\[
D=(1,0),\qquad BC:\ x=1,
\]
and write
\[
B=(1,u),\qquad C=(1,-v),\qquad u,v>0,\ uv>1.
\]
Set
\[
s=uv,\qquad a=u-v,\qquad L=s-1,
\]
and define
\[
M=(s+1)^2+a^2.
\]

Intersecting the tangents at the contact points gives
\[
A=\left(-\frac{s+1}{s-1},\frac{v-u}{s-1}\right)
=\left(-\frac{s+1}{L},-\frac{a}{L}\right).
\]

Let \(O=(h,a/2)\). From \(OB=OA\), one obtains
\[
h=\frac{(s+1)(s-3)-a^2}{4(s-1)}.
\]
Hence the line \(OI\) has equation
\[
aX-2hY=0. \tag{1}
\]

Now compute the circle through \(B,C\) tangent to the incircle. Its equation is
\[
X^2+Y^2+\lambda X+(v-u)Y-1-s-\lambda=0.
\]
Tangency to \(X^2+Y^2=1\) gives
\[
\lambda=\frac{a^2-s^2}{2s}.
\]
The tangency point \(X_a\) is therefore
\[
X_a=\left(\frac{a^2-s^2}{a^2+s^2},-\frac{2sa}{a^2+s^2}\right).
\]

Reflecting \(D=(1,0)\) across the line \(AI\) gives
\[
D'=\left(\frac{(s+1)^2-a^2}{M},\frac{2(s+1)a}{M}\right).
\]

A direct substitution of the two points \(D'\) and \(X_a\) shows that the line \(D'X_a\) has equation
\[
a(1+2s)X+(a^2-s-s^2)Y=a. \tag{2}
\]

Solving (1) and (2) gives
\[
P=\left(-\frac{s^2-2s-3-a^2}{3M},-\frac{2a(s-1)}{3M}\right).
\]
Using the formula for \(h\), this point satisfies
\[
P=-\frac{4(s-1)}{3M}\,O,
\]
so \(P\) lies on the line \(OI\).

Thus \(D'X_a\) passes through \(P\).

Applying the same computation cyclically to the sides \(CA\) and \(AB\) gives the analogous lines \(E'Y\) and \(F'Z\). The value
\[
\mu=\frac{4(s-1)}{3M}
\]
is cyclically symmetric in the three tangent lengths, so the point \(P=-\mu O\) obtained for one side is the same point obtained for the other two sides. Hence all three lines pass through the same point \(P\in OI\).

Therefore
\[
\boxed{D'X,\ E'Y,\ F'Z\text{ are concurrent at a point on }OI.}
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

\[
\boxed{\text{The three lines are concurrent on }OI.}
\]

Below is a complete proof.

---

### 1. Normalization

Scale the incircle to be the unit circle centered at \(I=(0,0)\). Put
\[
D=(1,0),
\]
so \(BC\) is the tangent line \(x=1\). Write
\[
B=(1,y),\qquad C=(1,-z),\qquad y,z>0.
\]
Let \(F,E\) be the touchpoints on \(AB,AC\). Using the parametrization of the unit circle
\[
T(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),
\]
we have
\[
F=T(y),\qquad E=T(-z).
\]
Let \(x\) be the tangent length from \(A\). For a triangle with inradius \(1\),
\[
x+y+z=xyz.
\]

---

### 2. The point \(D'\)

The line \(AI\) has direction
\[
\arctan y-\arctan z,
\]
so reflecting \(D=(1,0)\) across \(AI\) gives
\[
D'=T(\tau),\qquad \tau=\frac{y-z}{1+yz}.
\]

---

### 3. The point \(X\)

Let \(X=T(\sigma)\). The circle \((W_a)\) is tangent to the incircle at \(X\), so its equation has the form
\[
u^2+v^2-2\lambda(\cos\theta u+\sin\theta v)+2\lambda-1=0,
\]
where \(X=(\cos\theta,\sin\theta)\). Intersecting with \(BC\), i.e. \(u=1\), gives roots \(y,-z\), hence
\[
2\lambda\sin\theta=y-z,\qquad 2\lambda(1-\cos\theta)=-yz.
\]
Therefore, with \(\sigma=\tan(\theta/2)\),
\[
\sigma=-\frac{yz}{y-z}.
\]
Thus
\[
X=T(\sigma),\qquad \sigma=-\frac{yz}{y-z}.
\]

For two points \(T(p),T(q)\) on the unit circle, the chord through them has equation
\[
(1-pq)u+(p+q)v=1+pq.
\]
Applying this to \(D'=T(\tau)\), \(X=T(\sigma)\), and simplifying gives
\[
D'X:\quad
(2yz+1)u+\frac{(y-z)^2-yz(yz+1)}{y-z}v=1. \tag{1}
\]

---

### 4. The circumcenter

Set
\[
m=yz-1,\qquad S=y-z,\qquad u=yz+1=m+2,
\]
and define
\[
K=xy+yz+zx-1=m(x^2+1).
\]
From \(x(yz-1)=y+z\), we have
\[
K=m(x^2+1),
\]
and also
\[
u^2+S^2=mK. \tag{2}
\]

The circumcenter has the form
\[
O=(h,S/2).
\]
Solving \(OA=OB\) with \(A=\left(-\frac{u}{m},-\frac{S}{m}\right)\) gives
\[
h=-\frac K4+\frac u2.
\]
Hence
\[
T:=-\frac{4}{3K}O
\]
lies on \(OI\), and explicitly
\[
T=\left(\frac13-\frac{2u}{3K},-\frac{2S}{3K}\right).
\]

---

### 5. \(T\) lies on \(D'X\)

Using (1), the left-hand side at \(T\) is
\[
\begin{aligned}
L_T
&=(2yz+1)T_u+\frac{S^2-yz(yz+1)}{S}T_v\\
&=(2m+3)T_u+\frac{S^2-(m+1)(m+2)}{S}T_v.
\end{aligned}
\]
Since
\[
T_u=\frac13-\frac{2u}{3K},\qquad T_v=-\frac{2S}{3K},
\]
we get
\[
\begin{aligned}
L_T
&=\frac{2m+3}{3}
-\frac{2\bigl((m+2)^2+S^2\bigr)}{3K}\\
&=\frac{2m+3}{3}-\frac{2m}{3}
=1.
\end{aligned}
\]
Thus \(T\in D'X\).

By cyclic symmetry, the same point \(T\) lies on \(E'Y\) and \(F'Z\). Therefore
\[
D'X,\ E'Y,\ F'Z
\]
are concurrent at \(T\), and \(T\in OI\) by construction.

---

\[
\boxed{\text{The lines }D'X,E'Y,F'Z\text{ concur on }OI.}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

\[
\boxed{
\text{The lines }D'X,\ E'Y,\ F'Z\text{ are concurrent on }OI.
}
\]

Below is a complete coordinate proof.

---

### 1. Normalization

Let the incircle be the unit circle centered at  
\[
I=(0,0).
\]
Rotate so that
\[
D=(1,0),
\]
hence \(BC\) is the tangent line \(x=1\). Write
\[
B=(1,y),\qquad C=(1,-z)
\]
with \(y,z>0\). Let \(x\) be the tangent length from \(A\) to the incircle. Since the inradius is \(1\), Heron’s formula gives
\[
x+y+z=xyz,
\]
or equivalently
\[
x(yz-1)=y+z. \tag{1}
\]

Set
\[
p=yz,\qquad q=y-z.
\]

A direct tangent-line computation gives
\[
A=\left(-\frac{p+1}{p-1},-\frac{q}{p-1}\right).
\]

### 2. Coordinates of \(D'\) and \(X_a\)

The line \(AI\) has direction \((p+1,q)\). Reflecting \(D=(1,0)\) across it gives
\[
D'=\left(\frac{(p+1)^2-q^2}{(p+1)^2+q^2},
\frac{2(p+1)q}{(p+1)^2+q^2}\right).
\]

The circle through \(B,C\) tangent to the incircle touches the incircle at
\[
X_a=\left(\frac{q^2-p^2}{q^2+p^2},-\frac{2pq}{q^2+p^2}\right).
\]

Substituting these two points into the determinant equation of the chord through them yields the line
\[
D'X_a:\quad
q(2p+1)\xi+(q^2-p^2-p)\eta=q. \tag{2}
\]

### 3. The circumcenter \(O\)

Since \(OB=OC\), the circumcenter has \(y\)-coordinate \(q/2\). Write
\[
O=\left(u,\frac q2\right).
\]
Using \(OA=OB\) gives
\[
u=\frac{(p+1)(p-3)-q^2}{4(p-1)}.
\]

Now define
\[
K=xy+yz+zx-1.
\]
Using (1),
\[
K=(yz-1)(1+x^2),
\]
and also
\[
(1+y^2)(1+z^2)=K(yz-1).
\]
Therefore
\[
\frac{-4(p-1)}{3\bigl((p+1)^2+q^2\bigr)}
=
-\frac{4}{3K}.
\]

Let
\[
\lambda=-\frac{4}{3K}.
\]
We show that the point
\[
P_0=\lambda O
\]
lies on \(D'X_a\).

Indeed, substituting \((\xi,\eta)=\lambda O\) into the left-hand side of (2), we get
\[
q(2p+1)\lambda u+(q^2-p^2-p)\lambda\frac q2
=
q\lambda\left(u(2p+1)+\frac{q^2-p^2-p}{2}\right).
\]
But
\[
u(2p+1)+\frac{q^2-p^2-p}{2}
=
-\frac{3\bigl((p+1)^2+q^2\bigr)}{4(p-1)}
=
-\frac{3K}{4}.
\]
Hence
\[
q\lambda\left(u(2p+1)+\frac{q^2-p^2-p}{2}\right)
=
q\left(-\frac{4}{3K}\right)\left(-\frac{3K}{4}\right)=q.
\]
So \(P_0\in D'X_a\).

### 4. Cyclic symmetry

Repeating the same argument for the sides \(CA\) and \(AB\) gives analogous lines \(E'Y\) and \(F'Z\). Since
\[
K=xy+yz+zx-1
\]
is symmetric in \(x,y,z\), the same value \(\lambda\) is obtained in every cyclic case. Therefore all three lines pass through the same point
\[
P_0=\lambda O.
\]
But \(P_0\) is a real scalar multiple of \(O\), so \(P_0\in OI\).

Thus the three lines are concurrent on \(OI\).

\[
\boxed{\text{Concurrency point }=\lambda O,\quad \lambda=-\frac{4}{3(xy+yz+zx-1)}.}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

Let the incircle be the unit circle, \(I=0\), and rotate so that  
\[
D=1,\qquad E=e,\qquad F=f,\qquad |e|=|f|=1.
\]
Write
\[
B=1+ib,\quad C=1+ic
\]
with real \(b,c\). Then \(F=P(b)\), \(E=P(c)\), where \(P(t)=\frac{1+it}{1-it}\).

We shall prove that the three lines concur at the centroid \(G\) of the intouch triangle:
\[
G=\frac{1+e+f}{3}.
\]

### 1. \(G\) lies on \(OI\)

Let
\[
s=b+c,\qquad m=bc,\qquad T=(1-m)^2+s^2.
\]
A direct computation of the circumcenter of \(ABC\) gives
\[
O=\left(\frac{s^2-m^2-2m+3}{4(1+m)},\frac{s}{2}\right),
\]
while
\[
G=\frac{1+e+f}{3}
=\left(\frac{s^2-m^2-2m+3}{3T},\frac{2(1+m)s}{3T}\right).
\]
Hence
\[
G=\frac{4(1+m)}{3T}\,O,
\]
so \(G,O,I=0\) are collinear. Thus \(G\in OI\).

### 2. The line \(D'X\) passes through \(G\)

The line \(AI\) passes through the origin and through
\[
A=\frac{2ef}{e+f}.
\]
Reflecting \(D=1\) across \(AI\) gives
\[
D'=\frac{A}{\overline A}=ef.
\]

Let \(X=x\) be the tangency point of \((W_a)\) with the incircle. Using the real coordinates \(B=1+ib,\ C=1+ic\), the tangency condition for the circle through \(B,C\) tangent to the unit circle gives
\[
x=\frac{3ef-1-e-f}{ef+e+f-3}.
\]

For two points \(u,v\) on the unit circle, the chord \(uv\) has equation
\[
z+uv\overline z=u+v.
\]
Put
\[
p=ef,\qquad S=e+f.
\]
Then
\[
G=\frac{1+S}{3},\qquad \overline G=\frac{p+S}{3p}.
\]
Using the formula for \(x\), one checks
\[
G+p x\overline G=p+x.
\]
Therefore \(G\) lies on the chord through \(D'=p\) and \(X=x\), i.e.
\[
G\in D'X.
\]

### 3. The other two lines also pass through \(G\)

By the same cyclic argument applied to the sides \(CA\) and \(AB\), we get
\[
G\in E'Y,\qquad G\in F'Z.
\]
Hence the three lines \(D'X,E'Y,F'Z\) are concurrent at \(G\), and this point lies on \(OI\).

\[
\boxed{\text{The lines }D'X,E'Y,F'Z\text{ are concurrent on }OI.}
\]

</details>

<details><summary>A9: Almost (6/7)</summary>

\[
\boxed{\text{The lines are concurrent on } OI.}
\]

Here is a complete coordinate proof.

Normalize the incircle to be the unit circle centered at \(I=0\). Write points as complex numbers. Put
\[
D=1,\qquad B=1-ip,\qquad C=1+iq \qquad (p,q>0,\ pq>1).
\]
Then the other two tangent points are determined by the tangents from \(B,C\), and the third vertex is
\[
A=\left(-\frac{1+pq}{pq-1},\frac{p-q}{pq-1}\right).
\]
Let
\[
u=pq,\qquad v=p-q,\qquad M=(u+1)^2+v^2,\qquad N=v^2+u^2.
\]

The circumcenter \(O\) has complex coordinate
\[
o=\frac{u+1}{2}-R-\frac{iv}{2},
\]
where
\[
R=\frac{M}{4(u-1)}
\]
is the circumradius. In particular \(R\) is real and positive.

A direct calculation from the tangency condition for the circle through \(B,C\) tangent to the unit circle gives the tangency point
\[
x=\frac{(v+iu)^2}{v^2+u^2}=\frac{(v+iu)^2}{N}.
\]
The reflection of \(D=1\) across \(AI\) is
\[
d'=\frac{(u+1-iv)^2}{(u+1)^2+v^2}
=\frac{(u+1-iv)^2}{M}.
\]

For two unit complex numbers \(u,v\), the chord joining them has equation
\[
z+uv\,\bar z=u+v.
\]
Thus the line \(D'X\) is
\[
z+d'x\,\bar z=d'+x. \tag{1}
\]

Now define
\[
P=-\frac{o}{3R}.
\]
This is a real multiple of \(o\), so \(P\in OI\). We show \(P\) also lies on \(D'X\). Using the formulas above and the identity
\[
o+d'x\,\bar o=-3R(d'+x),
\]
which is obtained by straightforward expansion in \(u,v\) (all terms cancel identically), we get
\[
P+d'x\,\overline P
= -\frac{o}{3R}-d'x\frac{\overline o}{3R}
= -\frac{o+d'x\,\overline o}{3R}
= d'+x.
\]
Hence \(P\) satisfies exactly (1), so
\[
P\in D'X.
\]

The same argument with the cyclic relabeling of the triangle gives
\[
P\in E'Y,\qquad P\in F'Z.
\]
Therefore the three lines \(D'X,E'Y,F'Z\) are concurrent at the point \(P\) on \(OI\).

\[
\boxed{\text{Concurrency point }P=-\frac{1}{3R}O\text{ in these normalized coordinates.}}
\]

Thus the required lines are concurrent on the line \(OI\).

</details>

<details><summary>A10: Correct (7/7)</summary>

\[
\boxed{\text{The lines are concurrent at }P=\frac{D+E+F}{3}\text{ (the centroid of the intouch triangle).}}
\]

We give a self-contained proof.

---

Let the incircle be the unit circle in the complex plane, with incenter \(I=0\). Write the contact points as unit complex numbers \(d,e,f\), corresponding to \(D,E,F\). By rotation, take \(d=1\); the general point is then \(P=(d+e+f)/3\).

For the side \(BC\) (opposite \(d\)), put \(u=e,\ v=f\), \(m=uv\), and
\[
T=1+u+v+m.
\]
Then the reflected point
\[
D'=ef=d\,uv=m
\]
is simply \(m\).

A computation of the circle \((W_a)\) through \(B,C\) tangent to the unit circle gives its tangency point \(X_a\) the local coordinate
\[
x_a=\frac{T-4m}{4-T}.
\]
The chord through \(m\) and \(x_a\) has equation
\[
(4-T)z+m(T-4m)\bar z=T(1-m). \tag{1}
\]
Indeed, this is the standard chord equation for two unit complex numbers, and the point \(x_a\) was obtained from the tangency condition.

Now set
\[
p_0=\frac{1+u+v}{3}=\frac{T-m}{3}.
\]
Using \(\bar m=1/m\) and \(\bar T=T/m\), we get
\[
\bar p_0=\frac{T-1}{3m}.
\]
Substituting into the left-hand side of (1),
\[
\begin{aligned}
(4-T)p_0+m(T-4m)\bar p_0
&=\frac{(4-T)(T-m)+(T-4m)(T-1)}3\\
&=\frac{3T(1-m)}3\\
&=T(1-m).
\end{aligned}
\]
Thus \(p_0\) lies on the line \(D'X_a\). Translating back, the point
\[
P=\frac{1+u+v}{3}=\frac{d+e+f}{3}
\]
lies on \(D'X_a\). By cyclic symmetry, the same point lies on \(E'Y\) and \(F'Z\). Hence the three lines are concurrent at \(P\).

It remains to check that \(P\) lies on \(OI\). With \(d=1\), write
\[
u=e^{i\alpha},\qquad v=e^{i\beta},
\]
and set
\[
A=\frac{\alpha+\beta}{2},\qquad C=\frac{\alpha-\beta}{2}.
\]
Then
\[
1+u+v=1+2\cos C\,e^{iA}.
\]
Solving the perpendicular-bisector equations for the circumcenter gives
\[
O=\frac{1+u+v}{2\cos C(\cos A+\cos C)}.
\]
The denominator is real, so \(O\) is a real multiple of \(1+u+v=3P\). Therefore \(O,I,P\) are collinear. Hence \(P\in OI\).

Thus the three lines \(D'X,E'Y,F'Z\) concur at the centroid of the intouch triangle, which lies on \(OI\).

\[
\boxed{D'X,\ E'Y,\ F'Z \text{ are concurrent on } OI.}
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

Let \(I\) be the origin and let the incircle be the unit circle.  
Write \(\alpha=\angle A,\ \beta=\angle B,\ \gamma=\angle C\). We prove the claim for a generic triangle; the degenerate cases follow by continuity.

Rotate so that \(D=1\). Then \(BC\) is the tangent line \(x=1\). Put
\[
B=(1,p),\qquad C=(1,q),
\]
where
\[
p=\cot\frac{\beta}{2},\qquad q=-\cot\frac{\gamma}{2}.
\]
Set
\[
s=p+q,\qquad r=pq,\qquad \rho=1+r,
\]
and
\[
L=(1+p^2)(1+q^2).
\]

The circumcenter is
\[
O=\left(\frac{Q}{4\rho},\frac{s}{2}\right),
\qquad 
Q=s^2+4-\rho^2.
\]
Hence the line \(OI\) has equation
\[
2\rho s\,x-Qy=0. \tag{1}
\]

Now let \(X=(\cos\theta,\sin\theta)\) be the tangency point of \((W_a)\) with the incircle. The circle \((W_a)\) has equation
\[
x^2+y^2-1+\lambda(\cos\theta\,x+\sin\theta\,y-1)=0.
\]
Substituting \(B=(1,p)\) and \(C=(1,q)\) gives
\[
\lambda\sin\theta=-s,\qquad \lambda(\cos\theta-1)=r,
\]
so
\[
\tan\frac{\theta}{2}=\frac{r}{s}.
\]
Thus
\[
X=\frac{s+ir}{s-ir}.
\]

The reflection of \(D=1\) across \(AI\) is
\[
D'=ef,
\]
where \(e,f\) are the complex numbers of the contact points on \(AC,AB\). In our coordinates,
\[
D'=\frac{n+is}{n-is},\qquad n=1-r.
\]
Using the chord equation for two unit complex numbers, the line \(D'X\) is
\[
s(1-2r)x+(r-r^2+s^2)y=s. \tag{2}
\]

Solving (1) and (2) gives the point
\[
P=\left(\frac{Q}{3L},\frac{2\rho s}{3L}\right).
\]
Since
\[
O=\left(\frac{Q}{4\rho},\frac{s}{2}\right),
\]
we have
\[
P=\frac{4\rho}{3L}\,O. \tag{3}
\]

Now
\[
\rho=1-\cot\frac{\beta}{2}\cot\frac{\gamma}{2}
=-\frac{\sin(\alpha/2)}{\sin(\beta/2)\sin(\gamma/2)},
\]
and
\[
L=(1+p^2)(1+q^2)
=\frac1{\sin^2(\beta/2)\sin^2(\gamma/2)}.
\]
Therefore
\[
\frac{4\rho}{3L}
=-\frac43\sin\frac\alpha2\sin\frac\beta2\sin\frac\gamma2,
\]
which is symmetric in \(\alpha,\beta,\gamma\). Hence the point \(P\) defined by (3) is independent of the choice of side. By cyclically repeating the same argument for the sides \(CA\) and \(AB\), the analogous lines \(E'Y\) and \(F'Z\) pass through the same point \(P\).

Thus \(D'X,E'Y,F'Z\) are concurrent at \(P\in OI\).

\[
\boxed{\text{The three lines are concurrent on }OI.}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

\[
\boxed{\text{The lines }D'X,E'Y,F'Z\text{ concur at the centroid of the intouch triangle }DEF.}
\]

We prove this point lies on \(OI\).

Normalize the incircle to be the unit circle centered at \(I=(0,0)\). Write
\[
D=(1,0),\qquad E=T(v),\qquad F=T(u),
\]
where
\[
T(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right).
\]
Then
\[
B=(1,u),\qquad C=(1,v).
\]
Set
\[
p=uv,\qquad q=u+v,\qquad r=1-p,\qquad s=1+p,
\]
and
\[
L=q^2+r^2,\qquad M=q^2+pr+3r.
\]

A direct computation of the circumcenter of \(ABC\) gives
\[
O=\left(\frac{M}{4s},\frac q2\right).
\]
The centroid \(G\) of the contact triangle \(DEF\) is
\[
G=\frac{D+E+F}{3}
=\left(\frac{M}{3L},\frac{2sq}{3L}\right).
\]
Hence
\[
G=\frac{4s}{3L}O,
\]
so \(G\in OI\).

Now compute the line \(D'X\). Since \(AI\) has slope \(q/r\), reflection of \(D=(1,0)\) in \(AI\) gives
\[
D'=T\left(\frac qr\right).
\]
For the circle through \(B,C\) tangent to the incircle, if its tangency point is \(X=T(t)\), then restricting the circle equation to \(x=1\) gives roots \(u,v\); this yields
\[
t=\frac{p}{q}.
\]
Thus
\[
X=T\left(\frac pq\right).
\]
Therefore the chord \(D'X\) has equation
\[
q(r-p)x+(q^2+pr)y=q. \tag{1}
\]
Substituting \(G\) into (1),
\[
q(r-p)G_x+(q^2+pr)G_y
=\frac{q}{3L}\Big((r-p)M+2s(q^2+pr)\Big).
\]
But
\[
M=q^2+pr+3r,\qquad r-p+2s=3,
\]
so
\[
(r-p)M+2s(q^2+pr)
=3(q^2+pr)+3r(r-p)
=3(q^2+r^2)=3L.
\]
Hence \(G\) satisfies (1), i.e.
\[
G\in D'X.
\]

By exactly the same cyclic argument applied to the other two sides, we get
\[
G\in E'Y,\qquad G\in F'Z.
\]
Thus the three lines \(D'X,E'Y,F'Z\) are concurrent at \(G\), and \(G\) lies on \(OI\).

\[
\boxed{\text{Concurrent point} = \frac{D+E+F}{3}}
\]
on the line \(OI\).

</details>

<details><summary>A13: Almost (5/7)</summary>

\[
\boxed{\text{The three lines are concurrent on }OI.}
\]

We give a complete coordinate proof.

---

### 1. Normalization

Let the incircle be the unit circle centered at \(I=(0,0)\). Put \(D=(1,0)\), so
\[
BC:\ x=1,\qquad B=(1,b),\quad C=(1,c)
\]
for real \(b,c\). Define
\[
S=b^2+c^2,\qquad P=bc,\qquad s=b+c,\qquad q=1+P,
\]
\[
K=3+S-P^2,\qquad T=3(1+S+P^2)=3(1+b^2)(1+c^2).
\]

A direct calculation gives the circumcenter
\[
O=\left(\frac{K}{4q},\frac s2\right),
\]
so the line \(OI\) has equation
\[
s x-\frac{K}{2q}y=0. \tag{1}
\]

Define the point
\[
P_0=\left(\frac{K}{T},\frac{2qs}{T}\right). \tag{2}
\]
Using (1),
\[
s\frac{K}{T}-\frac{K}{2q}\frac{2qs}{T}=0,
\]
hence \(P_0\in OI\).

---

### 2. Equation of \(D'X\)

Let the incircle be parametrized by tangent half-angle
\[
P(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right).
\]
The tangency points on \(AB,AC\) are \(F=P(b)\), \(E=P(c)\).

Reflection of \(D=1\) across the angle bisector \(AI\) gives
\[
D'=P\!\left(\frac{b+c}{1-bc}\right)=P\!\left(\frac{s}{1-P}\right).
\]
A standard tangency computation for the circle through \(B,C\) tangent to the incircle gives
\[
X=P\!\left(\frac{bc}{b+c}\right)=P\!\left(\frac P s\right).
\]
Therefore the chord \(D'X\) has equation
\[
\boxed{
(1-2P)x+\frac{S+3P-P^2}{s}\,y=1. \tag{3}
}
\]
Substituting \(P_0\) into (3), the left-hand side becomes
\[
(1-2P)\frac{K}{T}+\frac{S+3P-P^2}{s}\frac{2qs}{T}
=\frac{(1-2P)K+2q(S+3P-P^2)}{T}.
\]
But expanding,
\[
(1-2P)K+2q(S+3P-P^2)=3(1+S+P^2)=T.
\]
Hence
\[
P_0\in D'X. \tag{4}
\]

---

### 3. Cyclically applying the same computation

Applying the identical argument to the sides \(CA\) and \(AB\) gives the corresponding lines \(E'Y\) and \(F'Z\). The equations of these two lines are obtained by cyclic symmetry in the three tangent parameters \(0,b,c\). In particular, the same point \(P_0\) defined by (2) satisfies the three line equations:
\[
P_0\in D'X,\qquad P_0\in E'Y,\qquad P_0\in F'Z.
\]
Thus the three lines are concurrent at \(P_0\), and from (1) \(P_0\in OI\).

---

\[
\boxed{\text{Therefore }D'X,\ E'Y,\ F'Z\text{ are concurrent on }OI.}
\]

</details>

<details><summary>A14: Incorrect (0/7)</summary>

Let the incircle be the unit circle centered at \(I=(0,0)\).  
We prove the concurrence point is on \(OI\).

For a side \(BC\), rotate coordinates so that  
\[
D=(1,0),\qquad B=(1,p),\qquad C=(1,-q)\quad (p,q>0).
\]
Write
\[
m=pq,\qquad s=p+q,\qquad d=p-q.
\]

A direct coordinate computation for the circle through \(B,C\) tangent to the unit circle gives the line \(D'X_a\) as the polar of
\[
N_a=\left(1+2m,\frac{s^2-m^2-5m}{d}\right).
\]
Indeed, in these coordinates the tangency point \(X_a\) is the second intersection of the unit circle with the line through \(D'\) and the pole \(N_a\).

The circumcenter is
\[
O=\left(\frac{m+3}{4}-\frac{s^2}{4(m-1)},\frac d2\right),
\]
and the circumradius satisfies
\[
R=\frac{(m-1)^2+s^2}{4(m-1)}.
\]
Substituting these expressions gives the identity
\[
O\cdot N_a=-2R(R-1).
\]
By cyclic symmetry,
\[
O\cdot N_b=O\cdot N_c=-2R(R-1).
\]
Hence the three poles \(N_a,N_b,N_c\) lie on the same line
\[
\ell:\quad O\cdot z=-2R(R-1).
\]

Let
\[
P=\frac{O}{-2R(R-1)}.
\]
Since \(I=(0,0)\), the point \(P\) lies on \(OI\).  
For the unit circle, the polar of \(P\) is exactly \(\ell\). Therefore \(N_a,N_b,N_c\in \ell\), so by La Hire’s theorem each of the polars of \(N_a,N_b,N_c\) passes through \(P\).

But the polar of \(N_a\) is precisely the line \(D'X_a\), the polar of \(N_b\) is \(E'Y\), and the polar of \(N_c\) is \(F'Z\). Thus
\[
D'X_a\cap E'Y\cap F'Z=P,
\]
and \(P\in OI\).

\[
\boxed{\text{The lines }D'X_a,E'Y,F'Z\text{ are concurrent on }OI.}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

\[
\boxed{\text{The lines }D'X,E'Y,F'Z\text{ are concurrent on }OI.}
\]

We give a proof.

Normalize so that the incircle is the unit circle centered at \(I=0\). Let the tangent lengths be
\[
BD=BF=x,\qquad CD=CE=y,\qquad AE=AF=\tau .
\]
Since the inradius is \(1\), Heron’s formula gives
\[
x+y+\tau=xy\tau. \tag{1}
\]
Place \(D=1\) on the unit circle, so
\[
B=1+ix,\qquad C=1-iy.
\]

We treat the side \(BC\) first. Put
\[
s=x-y,\qquad a=1+xy+is,\qquad r=s-ixy,
\]
and set \(w_a=ar\). A direct computation of the circle through \(B,C\) tangent to the unit circle gives its tangency point \(X\) as
\[
X=\frac{r}{\bar r}.
\]
Also, since \(AI\) is the internal angle bisector, the reflection of \(D=1\) in \(AI\) is
\[
D'=\frac{a}{\bar a}.
\]
For two points \(U,V\) on the unit circle, the chord \(UV\) has equation
\[
z+UV\bar z=U+V.
\]
Applying this to \(U=D'\), \(V=X\) yields
\[
L_a:=D'X:\quad \Re(\bar w_a z)=s. \tag{2}
\]
The pole of \(L_a\) with respect to the unit circle is therefore
\[
Q_a=\frac{w_a}{s}.
\]

The circumcenter \(O\) of \(ABC\) has coordinates
\[
O=\left(\frac{x^2+y^2+3-x^2y^2}{4(1-xy)},\frac{s}{2}\right).
\]
Using \(t=xy-1\), \(\tau=(x+y)/t\), one checks that
\[
O\cdot Q_a
= -\frac{3}{4}(xy+y\tau+\tau x-1). \tag{3}
\]
The same computation cyclically gives
\[
O\cdot Q_b=O\cdot Q_c
= -\frac{3}{4}(xy+y\tau+\tau x-1). \tag{4}
\]
Hence the three points \(Q_a,Q_b,Q_c\) lie on one line
\[
\ell:\quad O\cdot z=\sigma,
\qquad
\sigma=-\frac{3}{4}(xy+y\tau+\tau x-1). \tag{5}
\]

Now use the pole-polar duality with respect to the unit incircle. The polar of \(Q_a\) is exactly \(L_a\), and similarly for \(L_b,L_c\). Since \(Q_a,Q_b,Q_c\) are collinear on \(\ell\), their polars \(L_a,L_b,L_c\) are concurrent at the pole of \(\ell\). The pole of
\[
O\cdot z=\sigma
\]
is
\[
P=\frac{O}{\sigma},
\]
which lies on the line \(OI\), because \(O\) is a vector from \(I=0\).

Therefore the lines \(D'X,L_b,L_c\) all pass through the same point \(P\in OI\). By cyclic symmetry the same holds for the other two lines.

\[
\boxed{D'X,\ E'Y,\ F'Z\text{ are concurrent on }OI.}
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

Let the incircle be the unit circle centered at \(I=(0,0)\). Put  
\[
D=(1,0),\qquad BC:\ x=1.
\]
Write
\[
B=(1,y),\qquad C=(1,-z),\qquad y,z>0,\quad yz>1.
\]
Put
\[
s=y-z,\qquad v=yz.
\]

The other two touchpoints are
\[
E=\left(\frac{1-z^2}{1+z^2},-\frac{2z}{1+z^2}\right),\qquad
F=\left(\frac{1-y^2}{1+y^2},\frac{2y}{1+y^2}\right).
\]

A direct coordinate computation gives the following.

### 1. Equation of \(D'X\)

Let
\[
D'=\left(\frac{(1+v)^2-s^2}{(1+v)^2+s^2},\frac{2s(1+v)}{(1+v)^2+s^2}\right),
\]
and let \(X_0\) be the tangency point of \((W_a)\) with the incircle:
\[
X_0=\left(\frac{s^2-v^2}{s^2+v^2},-\frac{2sv}{s^2+v^2}\right).
\]
The line through \(D'\) and \(X_0\) simplifies to
\[
\boxed{(1+2v)x+\frac{s^2-v-v^2}{s}y=1}. \tag{1}
\]

### 2. The point \(P\) on \(OI\)

Consider the orthocenter \(T\) of the contact triangle \(DEF\). Since the incircle is the unit circle, \(T=D+E+F\). A direct calculation gives
\[
T=\left(\frac{K}{Q},-\frac{2s(v-1)}{Q}\right),
\]
where
\[
K=3+s^2+2v-v^2,\qquad Q=s^2+(v+1)^2.
\]
Now substitute \(T/3\) into the left-hand side of (1). Indeed,
\[
(1+2v)\frac{K}{3Q}
+\frac{s^2-v-v^2}{s}\left(-\frac{2s(v-1)}{3Q}\right)
=\frac{(1+2v)K-2(s^2-v-v^2)(v-1)}{3Q}=1,
\]
because
\[
(1+2v)K-2(s^2-v-v^2)(v-1)=3Q.
\]
Hence
\[
P:=\frac T3
\]
lies on \(D'X\).

By cyclic symmetry, the same computation for the other two sides shows that \(E'Y\) and \(F'Z\) also pass through \(P\). Therefore the three lines are concurrent at \(P\).

### 3. \(P\) lies on \(OI\)

The circumcenter \(O\) of \(ABC\) has coordinates
\[
O=\left(-\frac{K}{4(v-1)},\frac{s}{2}\right).
\]
Thus
\[
\frac{O_y}{O_x}
=
\frac{s/2}{-K/[4(v-1)]}
=
-\frac{2s(v-1)}{K}.
\]
But
\[
\frac{T_y}{T_x}
=
\frac{-2s(v-1)/Q}{K/Q}
=
-\frac{2s(v-1)}{K}.
\]
So \(O,T,I\) are collinear. Since \(P=T/3\), \(P\) also lies on \(OI\).

Therefore the three lines \(D'X,E'Y,F'Z\) are concurrent on \(OI\).

\[
\boxed{\text{The lines }D'X,E'Y,F'Z\text{ concur at }P=\frac T3\in OI.}
\]

</details>
