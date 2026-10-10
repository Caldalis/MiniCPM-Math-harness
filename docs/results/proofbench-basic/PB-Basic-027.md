# PB-Basic-027

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Given an acute triangle $ABC$, let $D$ and $E$ be the feet of
 the altitudes from $B$ to $AC$ and $C$ to $AB$, respectively.
 Let $E_{1}$ and $E_{2}$ be the reflections of $E$ with respect
 to $AC$ and $BC$, respectively. If $X$ (not equal to $C$) is an
 intersection point of the circumcircle of $\triangle CE_{1}E_{2}$
 and $AC$, and $O$ is the circumcenter of $\triangle CE_{1}E_{2}$,
 prove that $XO$ is perpendicular to $DE$.

## Swarm: accepted (best candidate `P6`; self-verification grades [7, 7, 7]; 716,049 tokens in 68 calls)

**Blind grade: Correct (7/7).** Complete coordinate proof with C at the origin and E=(0,-1) in which the circle coefficients, X, O and D are correct and XO=(1/(2k))(a+b,k) is orthogonal to DE's direction (k,-(a+b)).

\[
\boxed{\text{We prove the claim by coordinates.}}
\]

Place the origin at \(C\) and take the \(y\)-axis along \(CE\), with \(CE=1\). Since \(AB\perp CE\), write
\[
C=(0,0),\qquad E=(0,-1),
\]
and let
\[
A=(-a,-1),\qquad B=(b,-1),\qquad a,b>0.
\]
Because \(\angle C\) is acute,
\[
(-a,-1)\cdot(b,-1)=1-ab>0,
\]
so set
\[
k=1-ab>0.
\]

The lines \(AC\) and \(BC\) have equations
\[
AC:\ x-ay=0,\qquad BC:\ x+by=0.
\]

Reflecting \(E=(0,-1)\) across these two lines gives
\[
E_1=\left(-\frac{2a}{a^2+1},\frac{a^2-1}{a^2+1}\right),
\qquad
E_2=\left(\frac{2b}{b^2+1},\frac{b^2-1}{b^2+1}\right).
\]

Let the circumcircle of \(CE_1E_2\) be
\[
x^2+y^2+ux+vy=0,
\]
since it passes through \(C=(0,0)\). Using \(|E_1|=|E_2|=1\), substitution yields
\[
-2au+(a^2-1)v=-(a^2+1),
\]
\[
2bu+(b^2-1)v=-(b^2+1).
\]
Solving these two linear equations gives
\[
u=\frac{a-b}{k},\qquad v=\frac{1+ab}{k}.
\]
Hence the circumcenter is
\[
O=\left(-\frac u2,-\frac v2\right)
=\left(\frac{b-a}{2k},-\frac{1+ab}{2k}\right).
\]

Now \(X\neq C\) lies on \(AC\), so write \(X=(ay,y)\). Substituting into the circle equation:
\[
(a^2+1)y^2+(au+v)y=0.
\]
The root \(y=0\) gives \(C\). The other root is
\[
y=-\frac{au+v}{a^2+1}.
\]
But
\[
au+v=\frac{a(a-b)}{k}+\frac{1+ab}{k}
=\frac{a^2+1}{k},
\]
so
\[
y=-\frac1k,\qquad x=-\frac ak.
\]
Thus
\[
X=\left(-\frac ak,-\frac1k\right).
\]

Next, the foot \(D\) from \(B\) to \(AC\) is the projection of \(B=(b,-1)\) onto the direction \((a,1)\) of \(AC\):
\[
D=\frac{B\cdot(a,1)}{a^2+1}(a,1)
=\frac{ab-1}{a^2+1}(a,1)
=-\frac{k}{a^2+1}(a,1).
\]
Therefore
\[
\overrightarrow{DE}
=E-D
=(0,-1)+\frac{k}{a^2+1}(a,1)
=\frac{a}{a^2+1}\bigl(k,-(a+b)\bigr).
\]
So a direction vector of \(DE\) is
\[
q=(k,-(a+b)).
\]

Now compute
\[
\overrightarrow{XO}=O-X.
\]
We have
\[
\overrightarrow{XO}
=
\left(
\frac{b-a}{2k}+\frac{a}{k},
-\frac{1+ab}{2k}+\frac1k
\right)
=
\left(
\frac{a+b}{2k},\frac12
\right).
\]
Hence
\[
\overrightarrow{XO}
=
\frac1{2k}(a+b,k).
\]
Taking the dot product with \(q=(k,-(a+b))\),
\[
\overrightarrow{XO}\cdot q
=
\frac{a+b}{2k}k+\frac12\bigl(-(a+b)\bigr)
=
\frac{a+b}{2}-\frac{a+b}{2}=0.
\]
Thus \(XO\perp q\), and since \(q\parallel DE\), we conclude
\[
\boxed{XO\perp DE}.
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 6.94/7; graded Correct: 15 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 34,513 | Correct (7/7) | Complete coordinate proof with C at the origin and AC as the x-axis: the circumcenter conditions give px - qy = R/2 and, via the verified identity R(xv+yu) - sxy = uvR, pu = R/2, so XO.DE = pu - (px - qy) = 0. |
| A2 | stop | 23,955 | Correct (7/7) | Complete coordinate proof with C=(0,0), E=(1,0) in which the circle coefficients, X=(1/T,p/T), O and D are all correct (verified), and (T,S).(S,-T)=0 gives the perpendicularity rigorously. |
| A3 | stop | 22,794 | Correct (7/7) | Complete coordinate proof (C=(0,0), A=(1,0)) that derives ta+mb=a and tu=a from E1, E2 lying on the circle, so OX.DE=(ta+mb-tu)/2=0; all the algebra checks out. |
| A4 | stop | 37,061 | Correct (7/7) | Rigorous coordinate proof with AC on the x-axis: T=a^2v^2/L, the bracket simplification to uL and alpha=-T/u are all correct, giving X=(T/u,0), and using beta k = T(u-h)/u the dot product XO.DE vanishes. |
| A5 | stop | 39,579 | Correct (7/7) | Complete coordinate proof using the circle kappa - L/k through C, E1, E2, in which O, the factorization giving X=(-a/k,-ab/k), D, and XO parallel to (a+b,k) perpendicular to (k,-(a+b)) are all correct. |
| A6 | stop | 24,678 | Correct (7/7) | Coordinate proof with C=(0,0), E=(0,-1); the reflections, circle coefficients u=(a-b)/s and v=(1+ab)/s, X=(-a/s,-1/s), O and D all check out, and XO is shown orthogonal to the direction (s,-(a+b)) of DE. |
| A7 | stop | 31,316 | Almost (6/7) | The approach and main computations are correct (alpha=-e/u, X=(e/u,0), gamma f = e(u-e)/u, final dot product zero), but the write-up miswrites the circumcenter as (e/u,-gamma/2) and XO as (-e/u,-gamma/2) amid leftover 'Wait... ?' scratch work before reaching the correct direction (e/u,gamma), so the verification contains minor mistakes. |
| A8 | stop | 30,921 | Correct (7/7) | Complete coordinate proof with E at the origin in which the linear system, u, v, w, X=(-ac^2/d,-abc/d), D and O-X are all correct and the dot product with DE's direction vanishes. |
| A9 | stop | 32,464 | Correct (7/7) | Complete coordinate proof using the pencil s*Omega - L through C, E1, E2 (non-collinearity justified), with O, X, D and the slopes s/(a+b) and -(a+b)/s all computed correctly. |
| A10 | stop | 41,238 | Correct (7/7) | Coordinate proof with A=(1,0): writing B=A+t(E-A) gives the verified results x0=p/u and k=p(p-u)/(2qu), and XO.DE = -p(p-u)/(2u) + kq = 0; D=(u,0) is left implicit but is obvious. |
| A11 | stop | 25,182 | Correct (7/7) | Coordinate proof with C=(0,0), E=(0,1); O=((b-a)/2q,(1+ab)/2q), X=(-a/q,1/q) and D are computed correctly, and XO, parallel to (a+b,-q), is orthogonal to DE, parallel to (q,a+b). |
| A12 | stop | 37,664 | Correct (7/7) | Complete vector proof with C at the origin that derives mu=-s/m from E1, E2 lying on the circle, gets X=-mu*a and D=(m/alpha)a, and obtains XO.DE=-(s+mu*m)/2=0, with every step correct. |
| A13 | stop | 38,479 | Correct (7/7) | Complete coordinate proof (A=(0,0), C=(1,0)) that derives t*R^2 = beta*pq/L and beta*q = K(t-1) from E1, E2 lying on the circle, giving slope(XO) = K/q against slope(DE) = -q/K; every step checks out and the nondegeneracy conditions (p>0, K>0, t!=1) hold. |
| A14 | stop | 30,256 | Correct (7/7) | Coordinate proof with C=(0,0), A=(1,0): lambda=-v^2/(uR) and mu=-vH/(uR) are derived correctly, the identity lambda H = mu v gives (lambda,-mu) orthogonal to DE=(mH/R,mv/R), and XO is parallel to (lambda,-mu). |
| A15 | stop | 32,800 | Correct (7/7) | Coordinate proof with E at the origin and C=(0,1); the reflections, circle coefficients, t_X=1/h, X, O=((b-a)/2h,(3h-2)/2h) and D are all verified, and XO=((a+b)/2h,1/2) is orthogonal to DE's direction (-h,a+b). |
| A16 | stop | 19,926 | Correct (7/7) | Complete coordinate proof with C at the origin and AB horizontal in which the circle coefficients, X=(-a/k,-1/k), O and D are all correct and the direction vectors (a+b,k) and (k,-(a+b)) are orthogonal. |

<details><summary>A1: Correct (7/7)</summary>

\[
\boxed{\text{We prove } XO\perp DE.}
\]

Place \(C\) at the origin and \(AC\) on the \(x\)-axis. Write
\[
B=(u,v),\qquad E=(x,y),\qquad v>0,
\]
and set
\[
\mathbf e=(x,y),\qquad \mathbf b=(u,v),\qquad R=|\mathbf e|^2=x^2+y^2.
\]
Since \(CE\perp AB\) and \(E\in AB\), we have
\[
\mathbf e\cdot(\mathbf b-\mathbf e)=0
\]
so
\[
\mathbf e\cdot\mathbf b=R.
\]
Also \(D=(u,0)\).

Let
\[
s=u^2+v^2.
\]
The reflection of \(\mathbf e\) in \(BC\) is
\[
\mathbf e_2=\frac{2R}{s}\mathbf b-\mathbf e,
\]
while the reflection in \(AC\) is
\[
\mathbf e_1=(x,-y).
\]

Let \(O=(p,q)\) be the circumcenter of \(\triangle CE_1E_2\). Since \(C=0\) lies on the circle,
\[
|O|^2=|O-\mathbf e_1|^2=|O-\mathbf e_2|^2.
\]
Using \(|\mathbf e_1|^2=|\mathbf e_2|^2=R\), this gives
\[
O\cdot\mathbf e_1=O\cdot\mathbf e_2=\frac R2.
\]
Subtracting,
\[
O\cdot(\mathbf e_1-\mathbf e_2)=0.
\]
Now
\[
\mathbf e_1-\mathbf e_2=(2x,0)-\frac{2R}{s}(u,v),
\]
so
\[
xp=\frac{R}{s}(up+vq). \tag{1}
\]
Also from \(O\cdot\mathbf e_1=R/2\),
\[
xp-yq=\frac R2. \tag{2}
\]

From (1),
\[
up+vq=\frac{sxp}{R},
\]
hence
\[
q=\frac{p}{v}\left(\frac{sx}{R}-u\right).
\]
Substitute this into (2):
\[
p\left(x-\frac{y}{v}\left(\frac{sx}{R}-u\right)\right)=\frac R2.
\]
Using
\[
R=xu+yv,\qquad R=x^2+y^2,
\]
the bracket simplifies:
\[
x-\frac{y}{v}\left(\frac{sx}{R}-u\right)
=\frac{R(xv+yu)-sxy}{vR}
=\frac{uvR}{vR}=u.
\]
Therefore
\[
pu=\frac R2. \tag{3}
\]

Now \(X\in AC\), so \(X=(t,0)\). Since \(X\) lies on the circle centered at \(O\) through the origin,
\[
(t-p)^2+q^2=p^2+q^2,
\]
so
\[
t(t-2p)=0.
\]
The point \(t=0\) is \(C\), hence
\[
X=(2p,0).
\]
Thus
\[
\overrightarrow{XO}=O-X=(-p,q).
\]
Also
\[
\overrightarrow{DE}=E-D=(x-u,y).
\]
Therefore
\[
\overrightarrow{XO}\cdot\overrightarrow{DE}
=(-p,q)\cdot(x-u,y)
=pu-(px-yq).
\]
By (2), \(px-yq=R/2\), and by (3), \(pu=R/2\). Hence
\[
\overrightarrow{XO}\cdot\overrightarrow{DE}=0.
\]
So \(XO\perp DE\).

\[
\boxed{XO\perp DE}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

\[
\boxed{\text{We prove } XO\perp DE.}
\]

Let us use coordinates. Since the statement is invariant under similarities, put

\[
C=(0,0),\qquad E=(1,0).
\]

Because \(CE\perp AB\), the line \(AB\) is vertical, say \(x=1\). Since the triangle is acute, \(E\) lies between \(A\) and \(B\), so write

\[
A=(1,p),\qquad B=(1,-q),\qquad p,q>0.
\]

Set

\[
T=1-pq>0,\qquad S=p+q.
\]

The lines \(AC\) and \(BC\) are

\[
AC:\ y=px,\qquad BC:\ y=-qx.
\]

Reflecting \(E=(1,0)\) in these two lines gives

\[
E_1=\left(\frac{1-p^2}{1+p^2},\frac{2p}{1+p^2}\right),
\qquad
E_2=\left(\frac{1-q^2}{1+q^2},-\frac{2q}{1+q^2}\right).
\]

Let \(\Gamma\) be the circumcircle of \(\triangle CE_1E_2\). Since it passes through \(C=(0,0)\), its equation has the form

\[
x^2+y^2+ux+vy=0.
\]

Using the coordinates of \(E_1,E_2\) and simplifying gives

\[
u=-\frac{1+pq}{T},\qquad v=\frac{q-p}{T}.
\]

Thus

\[
\Gamma:\quad x^2+y^2-\frac{1+pq}{T}x+\frac{q-p}{T}y=0.
\]

Now intersect \(\Gamma\) with \(AC:y=px\). A point on \(AC\) has form \((t,pt)\). Substituting,

\[
(1+p^2)t^2+\left(u+pv\right)t=0.
\]

But

\[
u+pv=-\frac{1+pq}{T}+\frac{p(q-p)}{T}
=-\frac{1+p^2}{T}.
\]

Hence

\[
(1+p^2)t\left(t-\frac1T\right)=0.
\]

The point \(t=0\) is \(C\), so the other intersection is

\[
X=\left(\frac1T,\frac pT\right).
\]

The circumcenter \(O\) of \(\Gamma\) is

\[
O=\left(\frac{1+pq}{2T},\frac{p-q}{2T}\right).
\]

Therefore

\[
X-O
=
\left(\frac12,\frac{p+q}{2T}\right)
=
\frac1{2T}(T,S).
\]

So the direction of \(XO\) is \((T,S)\).

Now compute \(D\). Since \(D\) is the foot from \(B\) to \(AC\), projecting \(B=(1,-q)\) onto the direction \((1,p)\) of \(AC\),

\[
D=\frac{B\cdot(1,p)}{1+p^2}(1,p)
=
\frac{1-pq}{1+p^2}(1,p)
=
\frac{T}{1+p^2}(1,p).
\]

Thus

\[
\overrightarrow{DE}
=
E-D
=
\left(1-\frac{T}{1+p^2},-\frac{pT}{1+p^2}\right)
=
\frac{p}{1+p^2}(S,-T).
\]

So \(DE\) has direction \((S,-T)\). Finally,

\[
(T,S)\cdot(S,-T)=TS-ST=0.
\]

Hence \(XO\perp DE\).

\[
\boxed{XO\perp DE}
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

\[
\boxed{\text{Prove } XO\perp DE.}
\]

By a similarity, place
\[
C=(0,0),\qquad A=(1,0),\qquad B=(u,v),\quad v>0.
\]
Since \(ABC\) is acute, \(0<u<1\). Put
\[
r=1-u,\qquad s=r^2+v^2.
\]

The foot from \(B\) to \(AC\) is
\[
D=(u,0).
\]
The foot from \(C\) to \(AB\) can be written as
\[
E=(a,b),\qquad 
a=\frac{v^2}{s},\quad b=\frac{vr}{s}.
\]
Indeed, if \(E=A+\lambda(-r,v)\), then \(CE\perp AB\) gives \(\lambda=r/s\).

Now
\[
a^2+b^2=a,\qquad E\cdot B=a.
\]

Reflect \(E\) across \(AC\), so
\[
E_1=(a,-b).
\]
Reflecting \(E\) across \(BC\), with \(h=u^2+v^2\), gives
\[
E_2=\frac{2(E\cdot B)}{h}B-E=\frac{2a}{h}B-E,
\]
hence
\[
E_2=\left(\frac{2au}{h}-a,\frac{2av}{h}-b\right).
\]

Let \(\Gamma\) be the circumcircle of \(CE_1E_2\). Since it passes through \(C=(0,0)\), write
\[
\Gamma:\ x^2+y^2-tx+my=0.
\]
Its intersections with \(AC\), i.e. with \(y=0\), satisfy
\[
x(x-t)=0,
\]
so the second intersection is
\[
X=(t,0).
\]

Substituting \(E_1=(a,-b)\) into \(\Gamma\), and using \(a^2+b^2=a\), gives
\[
a-ta-mb=0
\]
or
\[
ta+mb=a. \tag{1}
\]

Substituting \(E_2=(X_2,Y_2)\) and using \(|E_2|^2=a\), we get
\[
a-tX_2+mY_2=0,
\]
so
\[
tX_2-mY_2=a.
\]
But
\[
tX_2-mY_2
=\frac{2a}{h}(tu-mv)-at+mb.
\]
Using \(mb=a-at\) from (1), this becomes
\[
a=\frac{2a}{h}(tu-mv)-at+a-at.
\]
Canceling \(a\) and dividing by \(2a\),
\[
tu-mv=ht.
\]
Thus
\[
mv=t(u-h). \tag{2}
\]

From (2),
\[
m=\frac{t(u-h)}{v}.
\]
Substituting into (1),
\[
ta+\frac{t r}{s}(u-h)=a,
\]
because \(b/v=r/s\). Multiplying by \(s\),
\[
t v^2+t r(u-h)=v^2.
\]
But
\[
u-h=ur-v^2,
\]
so
\[
v^2+r(u-h)=v^2+r(ur-v^2)=ur^2+v^2(1-r)=u(r^2+v^2)=us.
\]
Therefore
\[
t u s=v^2,
\]
and since \(a=v^2/s\),
\[
tu=a. \tag{3}
\]

The center of \(\Gamma\) is
\[
O=\left(\frac t2,-\frac m2\right).
\]
Hence
\[
\overrightarrow{OX}=\left(\frac t2,\frac m2\right),
\qquad
\overrightarrow{DE}=(a-u,b).
\]
Their dot product is
\[
\overrightarrow{OX}\cdot\overrightarrow{DE}
=\frac{t(a-u)+mb}{2}
=\frac{ta-tu+mb}{2}.
\]
Using \(ta+mb=a\) and \(tu=a\),
\[
ta-tu+mb=(ta+mb)-tu=a-tu=0.
\]
Thus
\[
\overrightarrow{OX}\cdot\overrightarrow{DE}=0,
\]
so \(XO\perp DE\).

\[
\boxed{XO\perp DE}
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Place coordinates with
\[
C=(0,0),\qquad A=(a,0),\qquad B=(u,v),
\]
where \(a,u,v>0\) and, since the triangle is acute, \(0<u<a\). Then
\[
D=(u,0).
\]
Write
\[
E=(h,k),\qquad k>0,
\]
and set
\[
T=CE^2=h^2+k^2.
\]

Because \(CE\perp AE\), we have
\[
(h,k)\cdot(h-a,k)=0 \implies h^2+k^2=ah,
\]
so
\[
T=ah \quad\Longrightarrow\quad h=\frac Ta.
\]
Also \(CE\perp AB\) gives
\[
E\cdot(B-A)=0 \implies uh+vk=ah=T.
\]
Hence
\[
vk=T-uh=T-\frac{Tu}{a}=\frac{T(a-u)}a,
\]
so
\[
\frac kT=\frac{a-u}{av}.
\]
The line \(AB\) has equation
\[
vh+(a-u)k=av.
\]
Substituting \(h=T/a\) and \(k=T(a-u)/(av)\) gives
\[
T\bigl((a-u)^2+v^2\bigr)=a^2v^2.
\]
Denote
\[
L=(a-u)^2+v^2.
\]
Then
\[
T=\frac{a^2v^2}{L}.
\]

Let the circumcircle of \(CE_1E_2\) have equation
\[
x^2+y^2+\alpha x+\beta y=0.
\]
This is valid because it passes through \(C=(0,0)\).

The reflection of \(E\) across \(AC\) is
\[
E_1=(h,-k).
\]
Also, since \(E\cdot B=T\),
\[
E_2=\frac{2T}{u^2+v^2}(u,v)-(h,k).
\]
Let \(c_2=u^2+v^2\). Substituting \(E_1,E_2\) into the circle equation gives
\[
T+\alpha h-\beta k=0, \tag{1}
\]
and
\[
T+\frac{2T}{c_2}(\alpha u+\beta v)-\alpha h-\beta k=0. \tag{2}
\]
From (1), \(\alpha h-\beta k=-T\). Substituting this into (2) yields
\[
1+\frac{\alpha u+\beta v}{c_2}-\frac{\beta k}{T}=0. \tag{3}
\]
Dividing (1) by \(T\) gives
\[
1+\frac{\alpha}{a}-\frac{\beta k}{T}=0. \tag{4}
\]
Subtracting (4) from (3),
\[
\frac{\alpha u+\beta v}{c_2}=\frac{\alpha}{a}.
\]
Thus
\[
a\beta v=\alpha(c_2-au).
\]
Using \(\frac kT=\frac{a-u}{av}\), we obtain
\[
\frac{\beta k}{T}
=\frac{\alpha(c_2-au)}{a v}\cdot\frac{a-u}{a v}.
\]
But from (4),
\[
\frac{\beta k}{T}=1+\frac{\alpha}{a}.
\]
Hence
\[
1+\frac{\alpha}{a}
=\alpha\frac{(c_2-au)(a-u)}{a^2v^2}.
\]
Solving,
\[
\alpha\Bigl(a v^2-(c_2-au)(a-u)\Bigr)=-a^2v^2.
\]
The bracket simplifies to
\[
a v^2-(c_2-au)(a-u)=u\bigl((a-u)^2+v^2\bigr)=uL.
\]
Therefore
\[
\alpha=-\frac{a^2v^2}{uL}=-\frac Tu.
\]

So the circle meets \(AC\), i.e. \(y=0\), at
\[
x^2+\alpha x=0,
\]
whose roots are \(x=0\) and \(x=-\alpha=\frac Tu\). Hence
\[
X=\left(\frac Tu,0\right).
\]
The circumcenter is
\[
O=\left(-\frac\alpha2,-\frac\beta2\right)
=\left(\frac{T}{2u},-\frac\beta2\right).
\]
Thus
\[
\overrightarrow{XO}
=
\left(-\frac{T}{2u},-\frac\beta2\right).
\]
Also
\[
\overrightarrow{DE}=E-D=(h-u,k).
\]
Therefore
\[
\overrightarrow{XO}\cdot \overrightarrow{DE}
=
-\frac{T}{2u}(h-u)-\frac{\beta k}{2}
=
\frac{T(u-h)}{2u}-\frac{\beta k}{2}.
\]
From (1), with \(\alpha=-T/u\),
\[
T-\frac{Th}{u}-\beta k=0,
\]
so
\[
\beta k=T-\frac{Th}{u}=\frac{T(u-h)}{u}.
\]
Substituting this into the dot product gives
\[
\overrightarrow{XO}\cdot \overrightarrow{DE}
=
\frac{T(u-h)}{2u}-\frac{T(u-h)}{2u}=0.
\]
Hence
\[
XO\perp DE.
\]

\[
\boxed{\text{Therefore } XO\perp DE.}
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

By a similarity, place
\[
E=(0,0),\qquad C=(0,1),
\]
and let
\[
A=(-a,0),\qquad B=(b,0)\qquad (a,b>0).
\]
Since \(\triangle ABC\) is acute, \(\angle C<90^\circ\), so
\[
ab<1.
\]
Put
\[
k=1-ab>0.
\]

The line \(AC\) is
\[
x-ay+a=0,
\]
and the line \(BC\) is
\[
x+by-b=0.
\]
Reflecting \(E=(0,0)\) in these two lines gives
\[
E_1=\left(-\frac{2a}{1+a^2},\frac{2a^2}{1+a^2}\right),\qquad
E_2=\left(\frac{2b}{1+b^2},\frac{2b^2}{1+b^2}\right).
\]
Both \(E_1,E_2\) satisfy
\[
\kappa(x,y):=x^2+y^2-2y=0.
\]
A direct substitution shows that the line \(E_1E_2\) is
\[
L(x,y):=(b-a)x-(1+ab)y+2ab=0.
\]
Since
\[
\kappa(C)=-1,\qquad L(C)=-k,
\]
the circle through \(C,E_1,E_2\) is
\[
\Omega:\quad \kappa-\frac{L}{k}=0.
\]
Equivalently,
\[
\Omega:\quad x^2+y^2-\frac{b-a}{k}x+\left(\frac{1+ab}{k}-2\right)y-\frac{2ab}{k}=0.
\]
Thus its center is
\[
O=\left(\frac{b-a}{2k},\frac{1-3ab}{2k}\right).
\]

Now parametrize \(AC\) by
\[
P(y)=(a(y-1),y).
\]
For \(P(y)\in AC\), one computes
\[
k\Omega(P(y))=(1+a^2)(y-1)(ky+ab).
\]
Hence the intersections with \(AC\) correspond to
\[
y=1 \quad\text{or}\quad y=-\frac{ab}{k}.
\]
The point \(y=1\) is \(C\), so the other intersection is
\[
X=\left(-\frac{a}{k},-\frac{ab}{k}\right).
\]

Next compute \(D\), the foot from \(B\) to \(AC\). Since \(AC: x-ay+a=0\),
\[
D=\left(-\frac{ak}{1+a^2},\frac{a(a+b)}{1+a^2}\right).
\]
Therefore
\[
\overrightarrow{DE}=E-D
=\frac{a}{1+a^2}\bigl(k,-(a+b)\bigr),
\]
so \(DE\) is parallel to \((k,-(a+b))\).

On the other hand,
\[
\overrightarrow{XO}=O-X
=\left(\frac{b-a}{2k}+\frac{a}{k},\frac{1-3ab}{2k}+\frac{ab}{k}\right)
=\frac1{2k}(a+b,k).
\]
Thus \(XO\) is parallel to \((a+b,k)\). Now
\[
(a+b,k)\cdot \bigl(k,-(a+b)\bigr)
=k(a+b)-k(a+b)=0.
\]
Hence
\[
XO\perp DE.
\]

\[
\boxed{\text{Therefore } XO \perp DE.}
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

\[
\boxed{\text{Proof}}
\]

Apply a similarity transformation so that
\[
C=(0,0),\qquad E=(0,-1).
\]
Since \(CE\perp AB\), the line \(AB\) is horizontal. Write
\[
A=(-a,-1),\qquad B=(b,-1),\qquad a,b>0.
\]
Because \(\angle C\) is acute,
\[
CA\cdot CB=(-a,-1)\cdot(b,-1)=1-ab>0,
\]
so put
\[
s=1-ab>0,\qquad p=a^2+1.
\]

The lines are
\[
AC:\ x-ay=0,\qquad BC:\ x+by=0.
\]

Reflecting \(E=(0,-1)\) across \(AC\) and \(BC\) gives
\[
E_1=\left(-\frac{2a}{p},\frac{a^2-1}{p}\right),\qquad
E_2=\left(\frac{2b}{q},\frac{b^2-1}{q}\right),
\]
where \(q=b^2+1\). Both \(E_1,E_2\) lie on the unit circle.

Let the circumcircle of \(\triangle CE_1E_2\) be
\[
\Gamma:\ x^2+y^2+ux+vy=0,
\]
since it passes through \(C=(0,0)\). Substituting \(E_1,E_2\) gives
\[
-2au+(a^2-1)v=-(a^2+1),
\]
\[
2bu+(b^2-1)v=-(b^2+1).
\]
Solving,
\[
u=\frac{a-b}{s},\qquad v=\frac{1+ab}{s}.
\]

Parametrize \(AC\) by
\[
P(\lambda)=(\lambda a,\lambda).
\]
Substituting into \(\Gamma\):
\[
p\lambda^2+\lambda(au+v)=0.
\]
Now
\[
au+v=\frac{a(a-b)}{s}+\frac{1+ab}{s}
=\frac{a^2+1}{s}=\frac ps.
\]
Thus
\[
p\lambda^2+\frac p s\lambda=0
\iff p\lambda\left(\lambda+\frac1s\right)=0.
\]
The root \(\lambda=0\) gives \(C\), so the other intersection is
\[
X=P\!\left(-\frac1s\right)=\left(-\frac as,-\frac1s\right).
\]

The circumcenter \(O\) of \(\Gamma\) is
\[
O=\left(-\frac u2,-\frac v2\right).
\]
Therefore
\[
\overrightarrow{XO}=O-X
=\left(\frac{a+b}{2s},\frac12\right).
\]

Next compute \(D\), the foot from \(B\) to \(AC\). Since a direction vector of \(AC\) is \((a,1)\),
\[
D=\frac{B\cdot(a,1)}{p}(a,1)
=\frac{ab-1}{p}(a,1)
=-\frac{s}{p}(a,1).
\]
Hence
\[
\overrightarrow{DE}=E-D
=\left(\frac{as}{p},-1+\frac{s}{p}\right)
=\frac{a}{p}\bigl(s,-(a+b)\bigr).
\]
So a direction vector of \(DE\) is
\[
(s,-(a+b)).
\]

Now take the dot product:
\[
\overrightarrow{XO}\cdot (s,-(a+b))
=
\frac{a+b}{2s}\cdot s+\frac12\bigl(-(a+b)\bigr)
=
\frac{a+b}{2}-\frac{a+b}{2}=0.
\]
Thus \(XO\) is perpendicular to \(DE\).

\[
\boxed{XO\perp DE}
\]

</details>

<details><summary>A7: Almost (6/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Apply a similarity transformation so that
\[
C=(0,0),\qquad A=(1,0),\qquad B=(u,v),\quad v>0.
\]
Since the triangle is acute, \(0<u<1\). Put \(p=1-u\), and write
\[
S=p^2+v^2.
\]

The foot \(E\) from \(C\) to \(AB\) is
\[
E=(e,f)=\left(\frac{v^2}{S},\frac{vp}{S}\right).
\]
Indeed, parametrizing \(AB\) gives \(E=(1-pt,vt)\), and the condition \(CE\perp AB\) yields \(t=p/S\). Then
\[
e^2+f^2=e.
\]
Also \(D=(u,0)\), and since \(AC\) is the \(x\)-axis,
\[
E_1=(e,-f).
\]

Let \(T=u^2+v^2\). Since \(E\cdot B=e\), the reflection of \(E\) across \(BC\) is
\[
E_2=\frac{2e}{T}(u,v)-(e,f).
\]
Hence
\[
E_2-E_1=\frac{2e}{T}(u-T,v).
\]
Write \(N=E_2-E_1=(N_x,N_y)\). Let the circumcircle \(\Gamma\) of \(CE_1E_2\) have equation
\[
x^2+y^2+\alpha x+\gamma y=0,
\]
because it passes through \(C=(0,0)\). Since \(|E_1|^2=|E_2|^2=e\), substituting \(E_1,E_2\) gives
\[
\alpha e-\gamma f=-e,\qquad \alpha x_2+\gamma y_2=-e.
\]
Subtracting,
\[
\alpha N_x+\gamma N_y=0.
\]
Thus \((\alpha,\gamma)\) is perpendicular to \(N\), so
\[
(\alpha,\gamma)=\lambda(-N_y,N_x).
\]
Using \(\alpha e-\gamma f=-e\),
\[
-\lambda(eN_y+fN_x)=-e.
\]
Now
\[
eN_y+fN_x=\frac{2e}{T}\bigl(ev+f(u-T)\bigr).
\]
But
\[
ev+f(u-T)=\frac{v}{S}\bigl(v^2+p(u-T)\bigr)=uv,
\]
because \(u-T=pu-v^2\). Therefore
\[
eN_y+fN_x=\frac{2euv}{T},
\]
so
\[
\lambda=\frac{T}{2uv}.
\]
Hence
\[
\alpha=-\lambda N_y=-\frac{T}{2uv}\cdot \frac{2ev}{T}=-\frac eu.
\]

The circle therefore meets the \(x\)-axis \(AC\) where
\[
x^2+\alpha x=x\left(x-\frac eu\right)=0.
\]
Since \(X\neq C\), we get
\[
X=\left(\frac eu,0\right).
\]

The circumcenter is
\[
O=\left(-\frac{\alpha}{2},-\frac{\gamma}{2}\right)
=\left(\frac eu,2\right),\? 
\]
Wait, more precisely,
\[
O=\left(\frac eu,2\right)? 
\]
No, \(\gamma\) is not necessarily 0. Let us write correctly:
\[
O=\left(\frac eu,-\frac{\gamma}{2}\right).
\]
Thus
\[
\overrightarrow{XO}
=\left(-\frac eu,-\frac{\gamma}{2}\right)
=-\frac12\left(\frac eu,\gamma\right).
\]
So \(XO\) is parallel to
\[
w=\left(\frac eu,\gamma\right).
\]

Now
\[
E-D=(e-u,f).
\]
Using \(\alpha e-\gamma f=-e\) and \(\alpha=-e/u\),
\[
-\frac{e^2}{u}-\gamma f=-e,
\]
so
\[
\gamma f=e-\frac{e^2}{u}=\frac{e(u-e)}{u}.
\]
Therefore
\[
w\cdot(E-D)
=\frac eu(e-u)+\gamma f
=\frac{e(e-u)}{u}+\frac{e(u-e)}{u}=0.
\]
Hence \(w\perp DE\), and since \(XO\parallel w\), we conclude
\[
XO\perp DE.
\]

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Let \(E=(0,0)\), let \(AB\) be the \(x\)-axis, and let \(CE\) be the \(y\)-axis. Write
\[
A=(-a,0),\qquad B=(b,0),\qquad C=(0,c),
\]
where \(a,b,c>0\). Since \(\angle C\) is acute,
\[
d:=c^2-ab>0.
\]

The line \(AC\) has equation
\[
cx-ay+ac=0,
\]
and \(BC\) has equation
\[
cx+by-bc=0.
\]

Reflecting \(E=(0,0)\) in these two lines gives
\[
E_1=\left(-\frac{2ac^2}{a^2+c^2},\frac{2a^2c}{a^2+c^2}\right),
\qquad
E_2=\left(\frac{2bc^2}{b^2+c^2},\frac{2b^2c}{b^2+c^2}\right).
\]
In particular \(CE_1=CE_2=CE=c\), so \(E_1,E_2\) satisfy
\[
x^2+y^2=2cy.
\]

Let the circumcircle of \(\triangle CE_1E_2\) be
\[
\Gamma:\ x^2+y^2+ux+vy+w=0.
\]
Put \(s=v+2c\). Substituting \(C,E_1,E_2\) into \(\Gamma\) and using \(x_i^2+y_i^2=2cy_i\) gives the two linear equations
\[
-2acu+(a^2-c^2)s=-c(a^2+c^2),
\]
\[
2bcu+(b^2-c^2)s=-c(b^2+c^2).
\]
Solving this system, with \(d=c^2-ab\), yields
\[
u=\frac{c^2(a-b)}{d},\qquad
s=\frac{c(ab+c^2)}{d}.
\]
Hence
\[
v=s-2c=\frac{c(3ab-c^2)}{d},
\]
and from \(C\in\Gamma\),
\[
w=c^2-cs=-\frac{2ab c^2}{d}.
\]
Therefore the circumcenter \(O\) of \(\triangle CE_1E_2\) is
\[
O=\left(-\frac u2,-\frac v2\right)
=
\left(
-\frac{c^2(a-b)}{2d},
\frac{c(c^2-3ab)}{2d}
\right).
\]

Now parametrize \(AC\) by
\[
P(t)=(-a+at,ct).
\]
Substituting \(P(t)\) into \(\Gamma\), the roots are \(t=1\), corresponding to \(C\), and
\[
t_X=-\frac{ab}{d},
\]
corresponding to \(X\). Thus
\[
X=P\!\left(-\frac{ab}{d}\right)
=
\left(-\frac{ac^2}{d},-\frac{abc}{d}\right).
\]

Next, the foot \(D\) from \(B\) to \(AC\) is
\[
D=\left(-\frac{ad}{a^2+c^2},\frac{ac(a+b)}{a^2+c^2}\right).
\]
Since \(E=(0,0)\), the line \(DE\) has direction vector
\[
(-d,\ c(a+b)).
\]

Finally,
\[
O-X
=
\left(
\frac{c^2(a+b)}{2d},\frac c2
\right).
\]
Taking the dot product with \((-d,\ c(a+b))\),
\[
(O-X)\cdot (-d,c(a+b))
=
-\frac{c^2(a+b)}2+\frac{c^2(a+b)}2=0.
\]
Hence \(XO\perp DE\).

\[
\boxed{\text{Therefore } XO \perp DE.}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Place coordinates so that  
\[
E=(0,0),\qquad C=(0,1),
\]
and \(AB\) is the \(x\)-axis. Since \(ABC\) is acute, \(E\) lies between \(A\) and \(B\), so write
\[
A=(-a,0),\qquad B=(b,0),\qquad a,b>0.
\]
Also the angle at \(C\) being acute gives
\[
s:=1-ab>0.
\]

The lines \(AC\) and \(BC\) are
\[
AC:\ x-ay+a=0,\qquad BC:\ x+by-b=0.
\]
Reflecting \(E=(0,0)\) in these two lines gives
\[
E_1=\left(-\frac{2a}{1+a^2},\frac{2a^2}{1+a^2}\right),\qquad
E_2=\left(\frac{2b}{1+b^2},\frac{2b^2}{1+b^2}\right).
\]

Let
\[
\Omega:\ x^2+y^2-2y=0.
\]
This is the circle centered at \(C\) with radius \(CE=1\), hence \(E_1,E_2\in\Omega\). A direct substitution shows that the line \(E_1E_2\) is
\[
L:(b-a)x-(ab+1)y+2ab=0.
\]
Now define
\[
\Gamma:s\Omega-L=0,\qquad s=1-ab.
\]
Since \(E_1,E_2\in\Omega\cap L\) and
\[
\Omega(C)=-1,\qquad L(C)=ab-1=-s,
\]
we get
\[
s\Omega(C)-L(C)=s(-1)-(-s)=0.
\]
Thus \(\Gamma\) passes through \(C,E_1,E_2\). Since \(s>0\), \(C\notin E_1E_2\), so these three points are noncollinear and \(\Gamma\) is their circumcircle. Expanding,
\[
\Gamma:s(x^2+y^2)-(b-a)x+(3ab-1)y-2ab=0.
\]
Hence its center is
\[
O=\left(\frac{b-a}{2s},\frac{1-3ab}{2s}\right).
\]

Now parametrize \(AC\) by
\[
P(t)=(-at,1-t).
\]
On this line,
\[
\Omega(P(t))=(1+a^2)t^2-1,\qquad L(P(t))=(1+a^2)t-s.
\]
Substituting into \(\Gamma=s\Omega-L\) gives
\[
(1+a^2)t(st-1)=0.
\]
The root \(t=0\) gives \(C\), and the other intersection with \(AC\) is obtained from \(t=1/s\). Therefore
\[
X=P(1/s)=\left(-\frac{a}{s},-\frac{ab}{s}\right).
\]

Next compute \(D\), the foot from \(B\) to \(AC\). Using the projection formula on \(AC\),
\[
D=\left(b,0\right)-\frac{a+b}{1+a^2}(1,-a)
=\left(-\frac{as}{1+a^2},\frac{a(a+b)}{1+a^2}\right).
\]
Since \(E=(0,0)\),
\[
m_{DE}=\frac{\frac{a(a+b)}{1+a^2}}{-\frac{as}{1+a^2}}
=-\frac{a+b}{s}.
\]

Finally,
\[
m_{XO}
=\frac{y_O-y_X}{x_O-x_X}
=\frac{\frac{1-3ab}{2s}+\frac{ab}{s}}
        {\frac{b-a}{2s}+\frac{a}{s}}
=\frac{s}{a+b}.
\]
Thus
\[
m_{DE}\cdot m_{XO}
=
-\frac{a+b}{s}\cdot \frac{s}{a+b}
=-1.
\]
Therefore \(XO\perp DE\).

\[
\boxed{XO\perp DE}
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

\[
\boxed{
\begin{aligned}
&\text{By a similarity, set } C=(0,0),\ A=(1,0),\ B=(u,v),\ v>0.\\
&\text{Since }ABC\text{ is acute, }0<u<1. \text{ Let }E=(p,q),\ q>0.
\end{aligned}
}
\]

\[
\boxed{
\begin{aligned}
&CE\perp AB \implies E\cdot(A-E)=0 \implies p^2+q^2=p.\\
&\text{Since }E\in AB,\text{ write }B=A+t(E-A)\text{ for some }t>1.\\
&\text{Then }u=1+t(p-1),\ v=tq,\text{ and }E\cdot B=p.
\end{aligned}
}
\]

\[
\boxed{
\begin{aligned}
&\text{Let }n=B\cdot B=u^2+v^2.\\
&\text{Reflecting }E\text{ in }BC\text{ gives }E_2=\frac{2(E\cdot B)}{n}B-E=\frac{2p}{n}B-E.\\
&\text{Thus }E_2=(x_2,y_2)=\left(\frac{2pu}{n}-p,\frac{2pv}{n}-q\right),
\end{aligned}
}
\]
and \(E_1=(p,-q)\).

Let \(X=(x_0,0)\) and let \(O=(h,k)\). Since the circumcircle passes through \(C=(0,0)\), its equation is
\[
x^2+y^2-x_0x-2ky=0,
\]
because \(x_0=2h\). Substituting \(E_1\) and \(E_2\) gives
\[
p-x_0p+2kq=0, \tag{1}
\]
\[
p-x_0x_2-2ky_2=0. \tag{2}
\]
From (1), \(2kq=p(x_0-1)\). Substituting into (2) yields
\[
x_0=\frac{p(q+y_2)}{qx_2+py_2}.
\]
Now
\[
q+y_2=\frac{2pv}{n},
\]
and
\[
qx_2+py_2=\frac{2pq}{n}(u+pt-n).
\]
Also
\[
n=B\cdot B=B\cdot A+t(B\cdot E-B\cdot A)=u+t(p-u),
\]
so
\[
u+pt-n=tu.
\]
Therefore
\[
x_0=\frac{p\cdot \frac{2pv}{n}}{\frac{2pq}{n}tu}=\frac pu.
\]
Hence
\[
h=\frac{x_0}{2}=\frac{p}{2u}.
\]

Using (1) again,
\[
2kq=p\left(\frac pu-1\right)=\frac{p(p-u)}{u},
\]
so
\[
k=\frac{p(p-u)}{2qu}.
\]

Finally,
\[
\overrightarrow{XO}=O-X=\left(-\frac{p}{2u},k\right),
\]
while
\[
\overrightarrow{DE}=E-D=(p-u,q).
\]
Thus
\[
\overrightarrow{XO}\cdot \overrightarrow{DE}
=
-\frac{p(p-u)}{2u}+kq
=
-\frac{p(p-u)}{2u}+\frac{p(p-u)}{2u}
=0.
\]
Therefore \(XO\perp DE\).

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A11: Correct (7/7)</summary>

\[
\boxed{XO\perp DE}
\]

Proof.

By a similarity, place
\[
C=(0,0),\qquad E=(0,1).
\]
Since \(CE\perp AB\), take \(AB\) as the line \(y=1\). Because \(ABC\) is acute, \(E\) lies between \(A\) and \(B\), so write
\[
A=(-a,1),\qquad B=(b,1)
\]
with \(a,b>0\). Also \(\angle C\) is acute, so
\[
\vec{CA}\cdot \vec{CB}=(-a,1)\cdot(b,1)=1-ab>0.
\]
Set
\[
q=1-ab>0.
\]

The lines are
\[
AC:\ x+ay=0,\qquad BC:\ x-by=0.
\]

Using the reflection formula for a line through the origin, the reflections of \(E=(0,1)\) give
\[
E_1=\left(-\frac{2a}{1+a^2},\frac{1-a^2}{1+a^2}\right),
\qquad
E_2=\left(\frac{2b}{1+b^2},\frac{1-b^2}{1+b^2}\right).
\]

Let \(O=(u,v)\) be the circumcenter of \(\triangle CE_1E_2\). Since \(|E_1|=|E_2|=1\), the equalities \(OC=OE_1=OE_2\) give
\[
ux_1+vy_1=\frac12,\qquad ux_2+vy_2=\frac12,
\]
where \((x_1,y_1)=(E_1)\), \((x_2,y_2)=(E_2)\). Solving these two linear equations yields
\[
u=\frac{b-a}{2q},\qquad v=\frac{1+ab}{2q}.
\]

Thus the circumcircle of \(\triangle CE_1E_2\) has equation
\[
x^2+y^2-2ux-2vy=0.
\]
Parametrize \(AC\) by
\[
P=t(a,-1).
\]
Substituting into the circle equation gives
\[
t\big((1+a^2)t+2(v-au)\big)=0.
\]
The root \(t=0\) corresponds to \(C\). The other root is
\[
t_X=\frac{2(au-v)}{1+a^2}.
\]
Now
\[
au-v
=\frac{a(b-a)}{2q}-\frac{1+ab}{2q}
=-\frac{1+a^2}{2q},
\]
so
\[
t_X=-\frac1q.
\]
Hence
\[
X=\left(-\frac aq,\frac1q\right).
\]

Therefore
\[
\overrightarrow{XO}=O-X
=\left(\frac{a+b}{2q},-\frac12\right)
=\frac1{2q}(a+b,-q).
\]
So \(XO\) is parallel to \((a+b,-q)\).

Next compute \(D\), the foot from \(B\) to \(AC\). Since \(AC\) has normal vector \((1,a)\),
\[
D=B-\frac{a+b}{1+a^2}(1,a)
=\left(-\frac{aq}{1+a^2},\frac{q}{1+a^2}\right).
\]
Thus
\[
\overrightarrow{DE}=E-D
=\left(\frac{aq}{1+a^2},\frac{a(a+b)}{1+a^2}\right)
=\frac{a}{1+a^2}(q,a+b).
\]
Now dot with \((a+b,-q)\):
\[
\overrightarrow{DE}\cdot (a+b,-q)
=\frac{a}{1+a^2}\big(q(a+b)-(a+b)q\big)=0.
\]
Hence \(DE\perp (a+b,-q)\). Since \(XO\parallel(a+b,-q)\), we conclude
\[
XO\perp DE.
\]

\[
\boxed{XO\perp DE}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Let \(C\) be the origin. Since \(CE\perp AB\), choose coordinates so that  
\[
E=(0,-q),\qquad A=(-p,-q),\qquad B=(r,-q)
\]
with \(p,q,r>0\). Put
\[
a=(-p,-q),\quad b=(r,-q),\quad e=(0,-q).
\]
Write
\[
s=q^2,\qquad \alpha=|a|^2=p^2+q^2,\qquad \beta=|b|^2=r^2+q^2,
\]
and
\[
m=a\cdot b=q^2-pr>0
\]
because the triangle is acute.

The reflection of \(e\) across the line \(CA\) is
\[
E_1=\frac{2s}{\alpha}a-e,
\]
and the reflection across \(CB\) is
\[
E_2=\frac{2s}{\beta}b-e.
\]

Let \(\Gamma\) be the circumcircle of \(\triangle CE_1E_2\). Since it passes through the origin, its equation has the form
\[
x\cdot x+u\cdot x=0,
\]
with center
\[
O=-\frac u2.
\]
Because \(E_1,E_2\in\Gamma\),
\[
s+u\cdot E_1=0,\qquad s+u\cdot E_2=0.
\]
Substituting the expressions for \(E_1,E_2\) gives
\[
\frac{2s}{\alpha}u\cdot a-u\cdot e=-s,\qquad
\frac{2s}{\beta}u\cdot b-u\cdot e=-s.
\]
Subtracting, we get
\[
\frac{u\cdot a}{\alpha}=\frac{u\cdot b}{\beta}=\mu
\]
for some scalar \(\mu\). Hence
\[
u\cdot a=\mu\alpha,\qquad u\cdot b=\mu\beta,
\]
and from the first equation,
\[
u\cdot e=s(2\mu+1). \tag{1}
\]

Now write \(u=(U,V)\). Using
\[
u\cdot a=\mu\alpha,\qquad u\cdot b=\mu\beta,\qquad u\cdot e=-qV=s(2\mu+1),
\]
one obtains
\[
pU=q^2+\mu(q^2-p^2),
\]
\[
rU=\mu(r^2-q^2)-q^2.
\]
Eliminating \(U\),
\[
r\bigl(q^2+\mu(q^2-p^2)\bigr)
=
p\bigl(\mu(r^2-q^2)-q^2\bigr).
\]
After expanding,
\[
\mu\bigl(r(q^2-p^2)-p(r^2-q^2)\bigr)
=-q^2(p+r).
\]
But
\[
r(q^2-p^2)-p(r^2-q^2)
=(p+r)(q^2-pr).
\]
Therefore
\[
\mu=-\frac{q^2}{q^2-pr}=-\frac{s}{m},
\]
so
\[
s+\mu m=0. \tag{2}
\]

Now parametrize a point of \(AC\) by \(ta\). Substituting into the circle equation gives
\[
\alpha t^2+t u\cdot a=\alpha t(t+\mu).
\]
Thus the second intersection with \(AC\) is
\[
X=-\mu a.
\]
Therefore
\[
\overrightarrow{XO}=O-X=-\frac u2+\mu a
=\mu a-\frac u2.
\]

The foot \(D\) from \(B\) to \(AC\) is the projection of \(b\) onto \(a\), so
\[
D=\frac{b\cdot a}{\alpha}a=\frac{m}{\alpha}a.
\]
Hence a direction vector of \(DE\) is
\[
e-D=e-\frac{m}{\alpha}a.
\]

Now compute the dot product:
\[
\begin{aligned}
\overrightarrow{XO}\cdot(e-D)
&=\left(\mu a-\frac u2\right)\cdot
\left(e-\frac{m}{\alpha}a\right)\\
&=\mu a\cdot e-\frac{u\cdot e}{2}
-\frac{m}{\alpha}\left(\mu a-\frac u2\right)\cdot a.
\end{aligned}
\]
Using \(a\cdot e=s\), \(u\cdot e=s(2\mu+1)\), and \(u\cdot a=\mu\alpha\),
\[
\begin{aligned}
\left(\mu a-\frac u2\right)\cdot e
&=\mu s-\frac{s(2\mu+1)}2
=-\frac s2,
\end{aligned}
\]
and
\[
\frac{m}{\alpha}\left(\mu a-\frac u2\right)\cdot a
=\frac{m}{\alpha}\left(\mu\alpha-\frac{\mu\alpha}{2}\right)
=\frac{\mu m}{2}.
\]
Thus
\[
\overrightarrow{XO}\cdot(e-D)
=-\frac s2-\frac{\mu m}{2}
=-\frac{s+\mu m}{2}=0
\]
by (2). Hence \(XO\perp DE\).

\[
\boxed{\text{Thus } XO\perp DE.}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

\[
\boxed{\text{We prove } XO\perp DE.}
\]

By a similarity, set
\[
A=(0,0),\qquad C=(1,0),\qquad B=(p,q),\quad q>0.
\]
Since \(ABC\) is acute, \(0<p<1\), and
\[
K=p^2+q^2-p=q^2-p(1-p)>0.
\]
Let
\[
L=p^2+q^2.
\]

The foot \(D\) from \(B\) to \(AC\) is
\[
D=(p,0).
\]
The foot \(E\) from \(C\) to \(AB\) is the projection of \(C\) onto \(AB\), hence
\[
E=\frac{p}{L}(p,q)=\left(\frac{p^2}{L},\frac{pq}{L}\right).
\]
Thus
\[
E-D=\left(\frac{p^2}{L}-p,\frac{pq}{L}\right)
=\left(-\frac{pK}{L},\frac{pq}{L}\right),
\]
so the slope of \(DE\) is
\[
m_{DE}=-\frac qK.
\]
Hence \(DE\) has direction vector \((-K,q)\), and a perpendicular direction is \((q,K)\).

Now let \(\omega\) be the circumcircle of \(\triangle CE_1E_2\). It meets the \(x\)-axis \(AC\) at \(C=(1,0)\) and at \(X=(t,0)\), with \(t\ne 1\). Therefore its equation has the form
\[
x^2+y^2-(1+t)x+t+\beta y=0. \tag{1}
\]
Equivalently, in coordinates centered at \(C\),
\[
u^2+v^2+(1-t)u+\beta v=0. \tag{2}
\]

Set
\[
e=E-C=\left(-\frac{q^2}{L},\frac{pq}{L}\right),\qquad R^2=|e|^2=\frac{q^2}{L}.
\]
Since
\[
E_1-C=\left(-R^2,-\frac{pq}{L}\right),
\]
substituting \(E_1\) into (2) gives
\[
R^2-(1-t)R^2-\beta\frac{pq}{L}=0,
\]
so
\[
tR^2=\beta\frac{pq}{L}. \tag{3}
\]

Now let
\[
w=(p-1,q),\qquad M=w\cdot w.
\]
Because \(E_2\) is the reflection of \(E\) across \(BC\), in coordinates centered at \(C\),
\[
e_2=E_2-C=\frac{2(e\cdot w)}{M}w-e.
\]
A direct computation gives
\[
e\cdot w=\frac{q^2}{L}=R^2,
\]
so
\[
e_2=\lambda w-e,\qquad \lambda=\frac{2R^2}{M}.
\]
Substituting \(e_2\) into (2) and using (3), we obtain
\[
2(1-t)R^2+\lambda\bigl((1-t)(p-1)+\beta q\bigr)=0.
\]
Since \(\lambda=2R^2/M\), this simplifies to
\[
(1-t)\bigl(M+p-1\bigr)+\beta q=0.
\]
But
\[
M+p-1=(p-1)^2+q^2+p-1=p^2+q^2-p=K.
\]
Hence
\[
(1-t)K+\beta q=0,
\]
or
\[
\beta q=K(t-1). \tag{4}
\]

The center \(O\) of \(\omega\) is
\[
O=\left(\frac{1+t}{2},-\frac{\beta}{2}\right).
\]
Therefore the slope of \(XO\) is
\[
m_{XO}
=\frac{-\beta/2}{(1+t)/2-t}
=\frac{\beta}{t-1}
=\frac{K}{q}
\]
by (4). But
\[
m_{DE}=-\frac qK.
\]
Thus
\[
m_{XO}m_{DE}=\frac{K}{q}\left(-\frac qK\right)=-1.
\]
So \(XO\perp DE\).

\[
\boxed{XO\perp DE}
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

\[
\boxed{\textbf{Proof.}}
\]

Apply a similarity transformation so that
\[
C=(0,0),\qquad A=(1,0),\qquad B=(u,v),\quad v>0,\quad 0<u<1.
\]
Put
\[
m=1-u,\qquad R=m^2+v^2,\qquad L=u^2+v^2,\qquad H=v^2-um.
\]
Since \(D\) is the foot from \(B\) to \(AC\), we have
\[
D=(u,0).
\]
Let
\[
E=(e,f).
\]
A direct projection computation gives
\[
E=\left(\frac{v^2}{R},\frac{mv}{R}\right).
\]
Thus
\[
e=\frac{v^2}{R},\qquad f=\frac{mv}{R},
\]
and
\[
f=\frac{m}{v}e,\qquad e^2+f^2=e,\qquad E\cdot B=e.
\]

Let the circumcircle of \(\triangle CE_1E_2\) be
\[
\Gamma:\ x^2+y^2+\lambda x+\mu y=0.
\]
It passes through \(C=(0,0)\), so this form is valid.

Since
\[
E_1=(e,-f),
\]
substituting \(E_1\) into \(\Gamma\) gives
\[
e+\lambda e-\mu f=0.
\]
Using \(f=\frac{m}{v}e\), this becomes
\[
v\lambda-m\mu=-v. \tag{1}
\]

Now \(E_2\) is the reflection of \(E\) across \(BC\). Since \(BC\) is the line through the origin in direction \(B=(u,v)\),
\[
E_2=\frac{2e}{L}(u,v)-(e,f).
\]
Substituting \(E_2\) into \(\Gamma\) and using (1) yields
\[
L+\lambda u+\mu v=\frac{m}{v}\mu L. \tag{2}
\]
From (1), \(\lambda=\frac{m\mu}{v}-1\). Substituting this into (2),
\[
L-u+\mu\left(\frac{um}{v}+v-\frac{mL}{v}\right)=0.
\]
But
\[
L-u=H,\qquad \frac{um}{v}+v-\frac{mL}{v}=\frac{uR}{v}.
\]
Hence
\[
H+\frac{uR}{v}\mu=0,
\]
so
\[
\mu=-\frac{vH}{uR}. \tag{3}
\]
Using (1) again,
\[
v\lambda=m\mu-v
=-\frac{v(uR+mH)}{uR}.
\]
Since
\[
uR+mH=u(m^2+v^2)+m(v^2-um)=v^2,
\]
we get
\[
\lambda=-\frac{v^2}{uR}. \tag{4}
\]
Therefore
\[
\lambda H=\mu v. \tag{5}
\]

Now
\[
\overrightarrow{DE}=E-D=\left(\frac{v^2}{R}-u,\frac{mv}{R}\right).
\]
But
\[
\frac{v^2}{R}-u=\frac{v^2-uR}{R}=\frac{mH}{R},
\]
so
\[
\overrightarrow{DE}=\left(\frac{mH}{R},\frac{mv}{R}\right).
\]
Then
\[
(\lambda,-\mu)\cdot \overrightarrow{DE}
=\frac{m}{R}(\lambda H-\mu v)=0
\]
by (5). Hence
\[
(\lambda,-\mu)\perp DE.
\]

Finally, the circle \(\Gamma\) meets \(AC\), i.e. the \(x\)-axis, at
\[
x^2+\lambda x=x(x+\lambda)=0.
\]
Thus the second intersection is
\[
X=(-\lambda,0).
\]
The center of \(\Gamma\) is
\[
O=\left(-\frac{\lambda}{2},-\frac{\mu}{2}\right).
\]
Therefore
\[
\overrightarrow{XO}
=\left(\frac{\lambda}{2},-\frac{\mu}{2}\right)
\parallel (\lambda,-\mu).
\]
So \(XO\perp DE\).

\[
\boxed{\text{Thus } XO\perp DE.}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

\[
\boxed{\text{Proof}}
\]

Place \(E\) at the origin and \(AB\) on the \(x\)-axis. Scale so that \(C=(0,1)\). Since \(ABC\) is acute, \(E\) lies between \(A\) and \(B\), so write

\[
A=(-a,0),\qquad B=(b,0),\qquad a,b>0.
\]

Let

\[
h=1-ab>0.
\]

The line \(AC\) has equation \(x-ay+a=0\), and \(BC\) has equation \(x+by-b=0\). Reflecting \(E=(0,0)\) in these two lines gives

\[
E_1=\left(-\frac{2a}{1+a^2},\frac{2a^2}{1+a^2}\right),\qquad
E_2=\left(\frac{2b}{1+b^2},\frac{2b^2}{1+b^2}\right).
\]

Let \(\Omega\) be the circumcircle of \(\triangle CE_1E_2\). Write

\[
\Omega:\ x^2+y^2+ux+vy+w=0.
\]

Since \(C=(0,1)\in\Omega\), we have \(w=-1-v\). Hence for a point \((x,y)\),

\[
\Omega((x,y))=x^2+y^2-1+ux+v(y-1)=0.
\]

Using \(E_1,E_2\) and the fact that they lie on \(x^2+y^2=2y\), we obtain

\[
-2au+(a^2-1)v=1-3a^2,
\]
\[
2bu+(b^2-1)v=1-3b^2.
\]

Solving these two linear equations gives

\[
u=\frac{a-b}{h},\qquad v=\frac{2-3h}{h}.
\]

Now parametrize \(AC\) by

\[
P(t)=(-at,1-t),\qquad t\in\mathbb R.
\]

Here \(P(0)=C\) and \(P(1)=A\). Substituting \(P(t)\) into \(\Omega\) gives

\[
\Omega(P(t))
=t\left((a^2+1)t-2-au-v\right).
\]

Thus the second intersection with \(AC\) corresponds to

\[
t_X=\frac{2+au+v}{a^2+1}.
\]

Since

\[
au+v=\frac{a(a-b)+2-3h}{h}
=\frac{a^2+1-2h}{h},
\]

we get

\[
2+au+v=\frac{a^2+1}{h},
\]

so

\[
t_X=\frac1h.
\]

Therefore

\[
X=\left(-\frac a h,-\frac{ab}{h}\right).
\]

The circumcenter of \(\Omega\) is

\[
O=\left(-\frac u2,-\frac v2\right)
=
\left(\frac{b-a}{2h},\frac{3h-2}{2h}\right).
\]

Hence

\[
\overrightarrow{XO}=O-X
=
\left(\frac{a+b}{2h},\frac12\right).
\]

Next, \(D\) is the foot from \(B=(b,0)\) to \(AC\). A direct projection gives

\[
D=\left(-\frac{ah}{1+a^2},\frac{a(a+b)}{1+a^2}\right)
=
\frac{a}{1+a^2}(-h,a+b).
\]

Thus \(DE\) has direction \((-h,a+b)\). Now

\[
\overrightarrow{XO}\cdot(-h,a+b)
=
\frac{a+b}{2h}(-h)+\frac12(a+b)
=
-\frac{a+b}{2}+\frac{a+b}{2}
=0.
\]

Therefore \(XO\perp DE\).

\[
\boxed{XO\perp DE}
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

\[
\boxed{
\text{We prove }XO\perp DE.
}
\]

Place coordinates so that  
\[
C=(0,0),\qquad E=(0,-1),
\]
and since \(CE\perp AB\), we may write
\[
A=(-a,-1),\qquad B=(b,-1),\qquad a,b>0.
\]
Let
\[
k=1-ab>0,
\]
which follows from \(\angle C<90^\circ\). Then
\[
AC:\ x-ay=0,\qquad BC:\ x+by=0.
\]

Reflecting \(E=(0,-1)\) across \(AC\) and \(BC\) gives
\[
E_1=\left(-\frac{2a}{1+a^2},\frac{a^2-1}{1+a^2}\right),
\]
\[
E_2=\left(\frac{2b}{1+b^2},\frac{b^2-1}{1+b^2}\right).
\]

Let the circumcircle of \(\triangle CE_1E_2\) have equation
\[
x^2+y^2+\alpha x+\beta y=0,
\]
since it passes through \(C=(0,0)\). Substituting \(E_1,E_2\) and using \(E_1^2=E_2^2=1\), we get
\[
-2a\alpha+(a^2-1)\beta=-(1+a^2),
\]
\[
2b\alpha+(b^2-1)\beta=-(1+b^2).
\]
Solving gives
\[
\alpha=\frac{a-b}{k},\qquad \beta=\frac{1+ab}{k}.
\]
Thus the circumcenter is
\[
O=\left(-\frac{\alpha}{2},-\frac{\beta}{2}\right)
=\left(\frac{b-a}{2k},-\frac{1+ab}{2k}\right).
\]

Now parametrize points on \(AC\) by \((at,t)\). Substituting into the circle equation:
\[
(1+a^2)t^2+(\alpha a+\beta)t=0.
\]
The nonzero solution is
\[
t=-\frac{\alpha a+\beta}{1+a^2}
=-\frac1k.
\]
Hence
\[
X=\left(-\frac a k,-\frac1k\right).
\]

Therefore
\[
\overrightarrow{OX}=X-O
=\left(-\frac{a+b}{2k},-\frac12\right)
=-\frac1{2k}(a+b,k).
\]
So a direction vector of \(OX\) is
\[
(a+b,k).
\]

Next compute \(D\), the foot from \(B\) to \(AC\). Since \(AC\) has direction \((a,1)\),
\[
D=\frac{B\cdot(a,1)}{(a,1)\cdot(a,1)}(a,1)
=\frac{ab-1}{a^2+1}(a,1)
=-\frac{k}{a^2+1}(a,1).
\]
Thus
\[
\overrightarrow{DE}=E-D
=\left(\frac{ak}{a^2+1},-1+\frac{k}{a^2+1}\right)
=\frac{a}{a^2+1}(k,-(a+b)).
\]
So a direction vector of \(DE\) is
\[
(k,-(a+b)).
\]

Now dot product:
\[
(a+b,k)\cdot\bigl(k,-(a+b)\bigr)
=(a+b)k-k(a+b)=0.
\]
Hence \(OX\perp DE\).

\[
\boxed{XO\perp DE}
\]

</details>
