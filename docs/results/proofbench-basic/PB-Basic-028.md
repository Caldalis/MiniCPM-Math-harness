# PB-Basic-028

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

In $\triangle ABC$ the altitudes $BE$ and $CF$ intersect at $H$. A circle $(W)$ is
 externally tangent to the Euler circle $(E)$ of $\triangle ABC$ and also tangent
 to the sides $AB$ and $AC$ at $X$ and $Y$, respectively, with
 $(W)$ being closer to $A$ than the Euler circle. Let $I'$ be the
 incenter of $\triangle AEF$. Prove that $AXI'Y$ is a rhombus.

## Swarm: accepted (best candidate `P2`; self-verification grades [7, 7, 7]; 829,929 tokens in 60 calls)

**Blind grade: Correct (7/7).** Derives the tangency quadratic correctly, justifies its factorization via P^2 - 2(b+c)P + 2(1+mu)bc = 0, takes the smaller root t = bc mu/P, computes AI' = 2t cos(theta) from the inradius, and checks that all four sides are equal.

Let \(A=2\theta\), and set
\[
p=\cos\theta,\qquad q=\sin\theta,\qquad \mu=\cos 2\theta=p^2-q^2.
\]
Let
\[
a=BC,\qquad b=CA,\qquad c=AB.
\]

Place \(A\) at the origin and the internal angle bisector of \(\angle A\) on the \(x\)-axis. Then we may write
\[
B=c(p,q),\qquad C=b(p,-q).
\]
The altitude feet are
\[
F=b\mu(p,q),\qquad E=c\mu(p,-q).
\]

The Euler circle is the nine-point circle of \(\triangle ABC\). It passes through \(F\), the midpoint of \(AB\), \(E\), and the midpoint of \(AC\). Writing its equation as
\[
x^2+y^2-2N_xx-2Ny_y+F_0=0,
\]
restricting to \(AB\) gives roots \(b\mu\) and \(c/2\), so
\[
F_0=\frac{bc\mu}{2},\qquad N_xp+N_yq=\frac{2b\mu+c}{4}.
\]
Similarly, using \(AC\), one gets
\[
N_xp-N_yq=\frac{2c\mu+b}{4}.
\]
Adding,
\[
N_x=\frac{(b+c)(1+2\mu)}{8p}.
\]
The nine-point radius is
\[
R_N=\frac{a}{8pq},
\]
so
\[
N_x+R_Nq=\frac{(b+c)(1+2\mu)+a}{8p}.
\]

Let \(t=AX=AY\). Since \(W\) is tangent to both sides of the angle, its center is \(O=(t/p,0)\) and its radius is \(tq/p\). The external tangency condition
\[
(O-N)^2=(R_N+\frac{tq}{p})^2
\]
simplifies, using \(F_0=N_x^2+N_y^2-R_N^2=\frac{bc\mu}{2}\), to
\[
4p^2t^2-St+2p^2bc\mu=0,
\]
where
\[
S=(b+c)(1+2\mu)+a.
\]

Set \(P=a+b+c\). From
\[
a^2=b^2+c^2-2bc\mu
\]
one obtains
\[
P^2-2(b+c)P+2(1+\mu)bc=0.
\]
Hence the quadratic factors as
\[
4p^2\left(t-\frac{bc\mu}{P}\right)\left(t-\frac P2\right)=0.
\]
The circle closer to \(A\) corresponds to the smaller root, so
\[
t=\frac{bc\mu}{P}.
\]

Now consider \(\triangle AEF\). Its side lengths are
\[
AE=c\mu,\qquad AF=b\mu,\qquad EF=a\mu.
\]
Thus its semiperimeter is
\[
s'=\frac{\mu(a+b+c)}2=\frac{\mu P}{2},
\]
and its area is
\[
[AEF]=bc\mu^2pq.
\]
Therefore its inradius is
\[
r'=\frac{[AEF]}{s'}
=\frac{2bc\mu pq}{P}.
\]
Since \(I'\) lies on the angle bisector of \(\angle A\),
\[
AI'=\frac{r'}{q}=\frac{2bc\mu p}{P}
=2p\cdot \frac{bc\mu}{P}
=2p\,AX.
\]

Finally, in the above coordinates,
\[
X=(tp,tq),\qquad Y=(tp,-tq),\qquad I'=(2tp,0),
\]
where \(t=AX=AY\). Hence
\[
AX^2=t^2,
\]
and
\[
XI'^2=I'Y^2=YA^2=t^2.
\]
Thus all four sides of \(AXI'Y\) are equal. Therefore \(AXI'Y\) is a rhombus.

\[
\boxed{AXI'Y\text{ is a rhombus}}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 7.00/7; graded Correct: 16 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 58,263 | Correct (7/7) | Clean and complete oblique-coordinate proof: the external tangency condition reduces to (t-rho)(t-L/2)=0 with rho=bc cosA/(a+b+c), and the incenter formula gives I'=X+Y, so all four sides equal rho. |
| A2 | stop | 43,273 | Correct (7/7) | Correct coordinate proof: AI' from the inradius, correct nine-point center/radius/power, explicit verification that t0=bcu/(pT) solves the tangency equation (that it is the smaller root, the other being T/(2p), is immediate), and diagonals that bisect each other perpendicularly. |
| A3 | stop | 52,994 | Correct (7/7) | Correct coordinate proof: power of A, nine-point center via chord bisectors, tangency quadratic with roots bcm/(2 sigma k) and sigma/k (verified via bc k^2 = sigma(sigma-a)), AI'=2dk^2 from the inradius of AEF, and a parallelogram with equal sides. |
| A4 | stop | 61,466 | Correct (7/7) | Correct nine-point circle data (apart from a mislabeled point list that does not affect the formulas), a correct quadratic with u0 verified as a root, and a correct incenter computation giving four equal sides; choosing u0 as the closer root is asserted but true (the other root is (a+b+c)/(2cos(theta))). |
| A5 | stop | 56,657 | Correct (7/7) | Complete coordinate proof: AI' from the inradius of AEF, correct nine-point center/radius/power, the tangency quadratic is explicitly factored as (l-t)(l-sigma)=0 with all identities shown, the smaller root is taken, and the four sides are shown equal. |
| A6 | stop | 47,076 | Correct (7/7) | Shows in full that d0 = k(b+c-a)/(4cos^3(theta)) satisfies the external tangency quadratic, picks it as the smaller root (asserted but true; the other root is (a+b+c)/(2cos(theta))), and AI' = 2d cos^2(theta) gives four equal sides. |
| A7 | stop | 50,482 | Correct (7/7) | Complete coordinate proof: external tangency gives t^2 - T t/(4cos^2(theta)) + kmn/2 = 0, whose stated factorization (t - mnk/q)(t - q/2) is correct, the excircle root q/2 is properly excluded, and I' = X + Y with \|X\| = \|Y\| gives the rhombus. |
| A8 | stop | 56,871 | Correct (7/7) | Correct coordinate proof: AI' via the similarity AEF~ABC, correct nine-point data and tangency quadratic (2), and the omitted routine checks that p0=qbc/(sqrt(k)M) is a root and that the other root M/(2sqrt(k)) is larger hold, giving AI'=2kp and four equal sides. |
| A9 | stop | 48,529 | Correct (7/7) | The tangency quadratic is correct, and the verified identity shows d0 = bc cosA/(P cos(A/2)) is a root, the other root P/(2cos(A/2)) being larger; AI' is computed correctly from the inradius and the diagonals bisect each other at right angles. |
| A10 | stop | 53,025 | Correct (7/7) | Correct coordinate proof in terms of AF, AE, EF: nine-point data and tangency equation (1) are right, u0=(P-l)/(4t^3) is indeed the smaller root (checked, other root (P+l)/(2td)), and AI'=2t*AX yields the rhombus. |
| A11 | stop | 43,015 | Correct (7/7) | Correct coordinate proof: AI', the nine-point center x-coordinate and radius, the power bck/2, and the tangency quadratic with roots bck/(pT) and T/(2p) all check out, and perpendicular mutually bisecting diagonals give the rhombus; the stated y-coordinate of H is missing a factor k but is never used. |
| A12 | stop | 47,420 | Correct (7/7) | Correct setup and tangency quadratic with roots bc cosA/S and S/2 (the claimed identity checks out), correctly chooses the smaller root, and AI' = 2t cos(A/2) gives diagonals that bisect each other at right angles; one intermediate line has a harmless typo. |
| A13 | stop | 57,869 | Correct (7/7) | Correct coordinates, tangency equation and substitution identity (verified), identifies the other root S/(2cos(theta)) as larger, and I' = X + Y with AX = AY gives the rhombus. |
| A14 | stop | 54,899 | Correct (7/7) | Defines X, Y so that I' = X + Y and verifies by explicit, correct algebra (power of the center equals 2Rr + r^2) that this circle is externally tangent to the nine-point circle, then identifies it with (W) the same way the reference does (the 'closer to A' step is asserted but true). |
| A15 | stop | 51,813 | Correct (7/7) | Correct coordinate proof: tangency quadratic correctly derived and factored with roots P*mu/(a+S) and (a+S)/2 (factorization verified), I' located via the similarity ABC to AEF, giving AX=XI'=I'Y=YA; the m/mu mix-up is a harmless typo. |
| A16 | stop | 58,047 | Correct (7/7) | Complete coordinate bash: correct incenter of AEF, nine-point data and tangency equation, explicit verification that d0=Pk/(cL) is the smaller root (other root L/(2c)), giving I'=X+Y and hence a rhombus. |

<details><summary>A1: Correct (7/7)</summary>

Let \(p=\cos A\). Work in oblique coordinates with origin \(A\), axes \(AB,AC\). If \(\mathbf e_1,\mathbf e_2\) are unit vectors along \(AB,AC\), then
\[
\overrightarrow{AP}=x\mathbf e_1+y\mathbf e_2,\qquad 
|AP|^2=x^2+y^2+2pxy=:Q(x,y).
\]

Set
\[
a=BC,\quad b=CA,\quad c=AB,\quad L=a+b+c,\quad K=1+p.
\]

Since \(E,F\) are altitude feet,
\[
AF=bp,\qquad AE=cp,
\]
so
\[
F=(bp,0),\qquad E=(0,cp).
\]
The nine-point circle also passes through the side midpoints \((c/2,0),(0,b/2)\). Hence its equation is
\[
\Gamma:\quad Q-(bp+c/2)x-(cp+b/2)y+\frac{bcp}{2}=0. \tag{1}
\]

Let \(W\) touch \(AB,AC\) at \(X=(t,0)\), \(Y=(0,t)\). Then
\[
W:\quad Q-2t(x+y)+t^2=0. \tag{2}
\]
Indeed, on the axes this gives \((x-t)^2=0\), so the tangency points are exactly \(X,Y\).

Now let \(C=(x_0,y_0)\) be the center of \(\Gamma\), and let its radius be \(R\). Comparing the linear terms in (1),
\[
x_0+py_0=\frac{bp+c/2}{2},\qquad y_0+px_0=\frac{cp+b/2}{2}.
\]
Adding,
\[
x_0+y_0=\frac{(b+c)(K-\frac12)}{2K}. \tag{3}
\]

The center of \(W\) is \(O_t=\frac{t}{K}(\mathbf e_1+\mathbf e_2)\), and its radius is
\[
R_t=t\sqrt{\frac{1-p}{K}}.
\]
Because \(W\) and \(\Gamma\) are externally tangent,
\[
|O_t-C|^2=(R_t+R)^2.
\]
Expanding this using (1) and (2) gives
\[
t^2-2t(x_0+y_0)+\frac{bcp}{2}
=2tR\sqrt{\frac{1-p}{K}}. \tag{4}
\]
Thus
\[
t^2-2\bigl((x_0+y_0)+R\sqrt{\frac{1-p}{K}}\bigr)t+\frac{bcp}{2}=0.
\]
Using (3) and
\[
R\sqrt{\frac{1-p}{K}}=\frac{a}{4K},
\]
we get
\[
2\bigl((x_0+y_0)+R\sqrt{\frac{1-p}{K}}\bigr)
=
\frac{(b+c)(K-\frac12)}{K}+\frac{a}{2K}.
\]
But
\[
\frac{(b+c)(K-\frac12)}{K}+\frac{a}{2K}
=
\frac{bcp}{L}+\frac L2,
\]
where the last equality follows from \(a^2=(b+c)^2-2bcK\). Therefore (4) becomes
\[
t^2-\left(\frac{bcp}{L}+\frac L2\right)t+\frac{bcp}{2}=0.
\]
Let
\[
\rho=\frac{bcp}{L}.
\]
Then
\[
t^2-\left(\rho+\frac L2\right)t+\rho\frac L2=0,
\]
so
\[
(t-\rho)\left(t-\frac L2\right)=0.
\]
The circle closer to \(A\) is the one with smaller \(t\), hence
\[
t=\rho.
\]

Now consider triangle \(AEF\). Its side lengths are
\[
EF=ap,\qquad AF=bp,\qquad AE=cp.
\]
Using the standard incenter coordinate formula,
\[
I'=\frac{apA+cpF+bpE}{ap+cp+bp}
=\left(\frac{bcp}{L},\frac{bcp}{L}\right)=(\rho,\rho).
\]
But \(X=(\rho,0)\), \(Y=(0,\rho)\), so in vector form
\[
I'=X+Y.
\]
Therefore
\[
\overrightarrow{XI'}=Y,\qquad \overrightarrow{I'Y}=-X,
\]
and all four sides have length \(\rho\):
\[
AX=XI'=I'Y=YA=\rho.
\]
Hence \(AXI'Y\) is a rhombus.

\[
\boxed{AXI'Y\text{ is a rhombus}}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

\[
\boxed{\text{ }AXI'Y\text{ is a rhombus.}}
\]

Proof.

Let \(\angle BAC=2\theta\), and set
\[
p=\cos\theta,\qquad q=\sin\theta,\qquad u=\cos A=p^2-q^2.
\]
Place \(A\) at the origin and the internal bisector of \(\angle A\) on the \(x\)-axis. Write
\[
AB=c,\qquad AC=b,\qquad BC=a,
\]
and put \(S=b+c\), \(T=a+b+c\).

Then
\[
B=(cp,cq),\qquad C=(bp,-bq).
\]
Since \(E,F\) are the altitude feet,
\[
E=(cu\,p,-cu\,q),\qquad F=(bu\,p,bu\,q).
\]
Thus the side lengths of \(\triangle AEF\) are
\[
AE=cu,\quad AF=bu,\quad EF=au.
\]

Let \(I'=(i,0)\) be the incenter of \(\triangle AEF\). Its area is
\[
[ AEF]=\frac12 (cu)(bu)\sin A=bc\,u^2pq,
\]
and its semiperimeter is
\[
s'=\frac{uT}{2}.
\]
Hence its inradius is
\[
r'=\frac{[AEF]}{s'}
=\frac{2bc\,u\,pq}{T}.
\]
Since the distance from \(I'=(i,0)\) to \(AB\) is \(iq\), we get
\[
iq=r',
\]
so
\[
i=\frac{2bc\,u\,p}{T}. \tag{1}
\]

Now let the center of \((W)\) be \(O=(t,0)\). Because \((W)\) is tangent to both sides \(AB,AC\), its radius is \(tq\), and the tangency points are
\[
X=(tp^2,tpq),\qquad Y=(tp^2,-tpq).
\]
Thus \(AX=AY=tp\).

We now determine \(t\) from tangency to the Euler circle. The nine-point center is
\[
N=\left(\frac{S(1+2u)}{8p},\frac{(c-b)(1-2u)}{8q}\right),
\]
and its radius is
\[
R_N=\frac{a}{8pq}.
\]
The power of \(A\) with respect to the Euler circle is
\[
\operatorname{Pow}(A)=AF\cdot AM_c=(bu)\left(\frac c2\right)=\frac{bc\,u}{2}.
\]
Since \((W)\) and the Euler circle are externally tangent,
\[
ON=tq+R_N.
\]
Squaring and expanding gives
\[
p^2t^2-2t(x_N+qR_N)+\frac{bc\,u}{2}=0.
\]
Now
\[
x_N+qR_N
=\frac{S(1+2u)+a}{8p}
=\frac{T+2Su}{8p}.
\]
So
\[
p^2t^2-\frac{T+2Su}{4p}t+\frac{bc\,u}{2}=0. \tag{2}
\]

We claim the smaller positive root of (2) is
\[
t_0=\frac{bc\,u}{pT}.
\]
Indeed, substituting \(t_0\) into (2) gives
\[
bc u\left(\frac{bc u}{T^2}-\frac{T+2Su}{4p^2T}+\frac12\right)=0,
\]
because
\[
2p^2T^2-(T+2Su)T+4p^2bc\,u
=u(T^2-2ST+4p^2bc)=0.
\]
The last equality follows from
\[
T^2-2ST=a^2-S^2
\]
and
\[
a^2-S^2+4p^2bc=0.
\]
Thus the circle closer to \(A\), hence the given \((W)\), satisfies
\[
t=t_0=\frac{bc\,u}{pT}. \tag{3}
\]

Using (1) and (3),
\[
i=\frac{2bc\,u\,p}{T}
=2p^2\cdot \frac{bc\,u}{pT}
=2p^2t.
\]
Therefore
\[
i=2tp^2.
\]

Now
\[
X=(tp^2,tpq),\qquad Y=(tp^2,-tpq),\qquad I'=(2tp^2,0).
\]
The midpoint of \(XY\) is
\[
M=(tp^2,0),
\]
and the midpoint of \(AI'\) is also
\[
\left(\frac{0+2tp^2}{2},0\right)=(tp^2,0)=M.
\]
Hence the diagonals \(AI'\) and \(XY\) bisect each other at \(M\). They are perpendicular because one is horizontal and the other vertical. Therefore \(AXI'Y\) is a rhombus.

\[
\boxed{AXI'Y\text{ is a rhombus.}}
\]

</details>

<details><summary>A3: Correct (7/7)</summary>

\[
\boxed{AXI'Y\text{ is a rhombus}}
\]

Assume \(ABC\) is acute; the other cases follow by directed lengths. Let
\[
\angle A=2\theta,\qquad k=\cos\theta,\quad s=\sin\theta,\quad m=\cos A=2k^2-1.
\]
Put
\[
a=BC,\quad b=CA,\quad c=AB,\quad \sigma=\frac{a+b+c}{2}.
\]
Place \(A\) at the origin and the internal angle bisector of \(\angle A\) on the \(x\)-axis:
\[
B=(ck,cs),\qquad C=(bk,-bs).
\]

Let \(\Gamma\) be the Euler circle. The nine-point circle cuts \(AB\) at \(F\) and at the midpoint \(M_c\) of \(AB\). Since
\[
AF=bm,\qquad AM_c=\frac c2,
\]
the power of \(A\) with respect to \(\Gamma\) is
\[
\operatorname{Pow}_\Gamma(A)=AF\cdot AM_c=\frac{bc\,m}{2}.
\]
Let \(N=(u,v)\) be the center of \(\Gamma\), and let its radius be \(\rho\). Then
\[
u^2+v^2-\rho^2=\frac{bc\,m}{2}. \tag{1}
\]
Also, using the perpendicular bisectors of the chords \(FM_c\) and \(EM_b\),
\[
N\cdot(k,s)=\frac{bm+c/2}{2},\qquad
N\cdot(k,-s)=\frac{cm+b/2}{2}.
\]
Adding,
\[
2ku=\frac{(b+c)(2m+1)}4,
\]
so
\[
u=\frac{(b+c)(2m+1)}{8k}. \tag{2}
\]
The nine-point radius is
\[
\rho=\frac a{8ks}.
\]

Let \(O=(d,0)\) be the center of \((W)\). Since \((W)\) is tangent to \(AB\) and \(AC\), its radius is \(ds\). External tangency to \(\Gamma\) gives
\[
|O-N|^2=(\rho+ds)^2.
\]
Expanding and using (1), (2), and \(a=2\sigma-(b+c)\), we get
\[
k^2d^2-\frac{d(\sigma+(b+c)m)}{2k}+\frac{bc\,m}{2}=0. \tag{3}
\]
Factoring (3) using \(m=2k^2-1\) and \(bc k^2=\sigma(\sigma-a)\), the two roots are
\[
d=\frac{bc\,m}{2\sigma k},\qquad d=\frac{\sigma}{k}.
\]
The circle closer to \(A\) is the smaller one, so
\[
d=\frac{bc\,m}{2\sigma k}. \tag{4}
\]

Now consider \(\triangle AEF\). We have
\[
AE=cm,\quad AF=bm,\quad EF=am.
\]
Thus its semiperimeter is \(m\sigma\), and its area is \(m^2[ABC]\). If \(r'\) is its inradius, then
\[
r'=\frac{m[ABC]}{\sigma}.
\]
Since \(AI'\) lies on the angle bisector and the distance from \(I'\) to either side of \(\angle A\) is \(r'\),
\[
AI'=\frac{r'}{s}=\frac{m[ABC]}{\sigma s}
=\frac{bc\,k\,m}{\sigma}.
\]
Using (4),
\[
AI'=2dk^2. \tag{5}
\]

Therefore, with \(O=(d,0)\), the tangency points are
\[
X=(dk^2,dks),\qquad Y=(dk^2,-dks),
\]
and
\[
I'=(2dk^2,0).
\]
Now
\[
AX^2=d^2k^4+d^2k^2s^2=d^2k^2,
\]
and
\[
XI'^2=(2dk^2-dk^2)^2+(dks)^2=d^2k^2.
\]
Similarly,
\[
AY^2=d^2k^2,\qquad I'Y^2=d^2k^2.
\]
Also
\[
\vec{I'Y}=-\vec{AX},\qquad \vec{YA}=-\vec{XI'},
\]
so \(AXI'Y\) is a parallelogram. All four sides are equal, hence it is a rhombus.

\[
\boxed{AXI'Y\text{ is a rhombus}}
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Let \(A=2\theta\), and set
\[
q=\cos\theta,\qquad p=\sin\theta,\qquad m=\cos 2\theta=q^2-p^2.
\]
Place \(A\) at the origin and the internal angle bisector of \(\angle A\) on the \(x\)-axis. Write
\[
\vec{AB}=c(q,p),\qquad \vec{AC}=b(q,-p),
\]
so \(AB=c,\ AC=b\). Put \(a=BC\), \(s=\frac{a+b+c}{2}\), and \(P=b+c\).

The feet of the altitudes are
\[
F=(bm,0),\qquad E=(0,cm)
\]
in the oblique coordinate system with basis \((q,p),(q,-p)\). The nine-point circle \(\mathcal N\) of \(\triangle ABC\) therefore passes through
\[
(0,cm),(0,bm),\left(\frac c2,0\right),\left(\frac b2,0\right).
\]
A direct computation gives its center \(N=(N_x,N_y)\) and radius \(r_N\) by
\[
N=\left(\frac{P(1+2m)}{8q},\frac{(c-b)(1-2m)}{8p}\right),\qquad r_N=\frac{a}{8pq}.
\]
Also
\[
N_x^2+N_y^2-r_N^2=\frac{bc\,m}{2}. \tag{1}
\]

Let the circle \((W)\) have center \(O=(u,0)\) on the angle bisector. Since it is tangent to \(AB,AC\), its radius is
\[
r_W=up.
\]
Its tangency points are
\[
X=(u q^2,u p q),\qquad Y=(u q^2,-u p q),
\]
so
\[
AX=AY=uq.
\]

Because \((W)\) is externally tangent to \(\mathcal N\),
\[
ON=r_N+r_W.
\]
Thus
\[
(N_x-u)^2+N_y^2=(r_N+up)^2.
\]
Using the formulas for \(N_x,r_N\) and (1), this simplifies to
\[
4q^3u^2-\bigl(a+P(1+2m)\bigr)u+2qbc\,m=0. \tag{2}
\]

Now consider
\[
u_0=\frac{bc\,m}{2sq}=\frac{bc\,m}{(a+b+c)q}.
\]
Substituting into (2) gives, after multiplying by \((a+b+c)^2q\),
\[
bc\,m^2\bigl(a^2-P^2+4bc\,q^2\bigr)=0.
\]
But
\[
a^2=b^2+c^2-2bc\,m=P^2-2bc(1+m)
\]
and \(4q^2=2(1+m)\), so
\[
a^2-P^2+4bc\,q^2=0.
\]
Hence \(u_0\) satisfies the tangency equation. Since \(W\) is the circle closer to \(A\) than \(\mathcal N\), we have
\[
u=u_0.
\]

It remains to identify \(I'\). In \(\triangle AEF\),
\[
AE=cm,\qquad AF=bm,\qquad EF=ma.
\]
Its inradius is
\[
r_{AEF}=\frac{\text{area}_{AEF}}{\text{semiperimeter}_{AEF}}
=\frac{m^2[ABC]}{ms}=m\frac{[ABC]}s=m r_{ABC}.
\]
If \(I'=(d,0)\), then its distance to \(AB\) is \(dp\), so
\[
dp=m\frac{bc\,pq}{s}
\quad\Longrightarrow\quad
d=\frac{bc\,mq}{s}.
\]
Since \(s=(a+b+c)/2=T/2\), with \(T=a+P\),
\[
d=\frac{2bc\,mq}{T}=2q^2u_0.
\]
Therefore
\[
d-u_0q^2=u_0q^2.
\]

Now
\[
X=(u_0q^2,u_0pq),\qquad Y=(u_0q^2,-u_0pq),\qquad I'=(d,0).
\]
Hence
\[
XI'^2=(d-u_0q^2)^2+(u_0pq)^2
=u_0^2q^4+u_0^2p^2q^2
=u_0^2q^2.
\]
Thus
\[
XI'=u_0q=AX.
\]
Similarly,
\[
I'Y=u_0q=AY.
\]
Therefore
\[
AX=XI'=I'Y=AY,
\]
so \(AXI'Y\) is a rhombus.

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

\[
\boxed{\text{We prove }AXI'Y\text{ is a rhombus.}}
\]

Let \(a=BC,\ b=CA,\ c=AB\), and let \(\sigma=\frac{a+b+c}{2}\). Write
\[
\angle BAC=2\alpha,\qquad p=\cos\alpha,\quad q=\sin\alpha,\quad m=\cos2\alpha.
\]
Use unit vectors
\[
u=(p,q),\qquad v=(p,-q),
\]
so \(u+v\) is the internal angle bisector of \(\angle A\). Put
\[
B=cu,\qquad C=bv.
\]
Since \(E,F\) are altitude feet,
\[
E=cmv,\qquad F=bmu.
\]

Let \(I'=t(u+v)\). The inradius of \(\triangle AEF\) is
\[
r'=\frac{m[ABC]}{\sigma},
\]
while its distance to \(AB\) is \(t\sin2\alpha\). Hence
\[
t=\frac{r'}{\sin2\alpha}
=\frac{bc m}{2\sigma}. \tag{1}
\]

Now consider the Euler circle \(\Gamma\). It cuts \(AB\) at \(F\) and at the midpoint of \(AB\), so on the line \(AB\) its intersection parameters are \(bm\) and \(c/2\). Thus, if \(\Gamma\) has equation
\[
x^2+y^2+Ux+Vy+\frac{bc m}{2}=0,
\]
then adding the two restrictions on \(AB\) and \(AC\) gives
\[
N_x=\frac{(b+c)(1+2m)}{8p},
\]
where \(N\) is the center of \(\Gamma\). Its radius is
\[
R=\frac{a}{8pq}.
\]

Let the circle tangent to \(AB,AC\) have tangency points \(X=t_0u,\ Y=t_0v\); write \(l=t_0\). Its center is \(O_l=(l/p,0)\) and radius \(r_l=lq/p\). External tangency to \(\Gamma\) gives
\[
|O_lN|^2=(R+r_l)^2.
\]
Expanding,
\[
l^2-2\frac{N_x+Rq}{p}l+\frac{bc m}{2}=0. \tag{2}
\]

Now
\[
\frac{N_x+Rq}{p}
=\frac{(b+c)(1+2m)+a}{4(1+m)}.
\]
Let \(S=b+c\). From the law of cosines,
\[
a^2=S^2-2bc(1+m),
\]
so
\[
bc(1+m)=2\sigma(\sigma-a).
\]
Using this,
\[
2\frac{N_x+Rq}{p}
=\frac{S(1+2m)+a}{2(1+m)}
=\frac{\sigma+mS}{1+m}.
\]
On the other hand, by (1),
\[
t+\sigma
=\frac{bc m}{2\sigma}+\sigma
=\frac{m(\sigma-a)}{1+m}+\sigma
=\frac{\sigma+mS}{1+m}.
\]
Hence
\[
2\frac{N_x+Rq}{p}=t+\sigma.
\]
Substituting into (2),
\[
l^2-(t+\sigma)l+\frac{bc m}{2}=0.
\]
But
\[
\frac{bc m}{2}=t\sigma,
\]
so
\[
(l-t)(l-\sigma)=0.
\]
The circle closer to \(A\) has the smaller value of \(l\), hence
\[
l=t.
\]

Therefore
\[
X=tu,\qquad Y=tv,\qquad I'=t(u+v).
\]
Thus
\[
AX=AY=t,
\]
and
\[
XI'=|tu-t(u+v)|=t,\qquad I'Y=|tv-t(u+v)|=t.
\]
So all four sides of \(AXI'Y\) are equal to \(t\). Hence \(AXI'Y\) is a rhombus.

\[
\boxed{\text{Therefore }AXI'Y\text{ is a rhombus.}}
\]

</details>

<details><summary>A6: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Let \(\angle A=2\theta\), and set
\[
p=\cos\theta,\qquad q=\sin\theta,\qquad k=\cos A=2p^2-1.
\]
Place \(A=(0,0)\), with the internal angle bisector of \(\angle A\) as the \(x\)-axis. Write
\[
AB=c,\qquad AC=b,\qquad BC=a.
\]
Then
\[
B=(cp,-cq),\qquad C=(bp,bq).
\]

Let
\[
S=b+c,\qquad t=S-a.
\]

The altitude feet are
\[
E=(c kp,ckq),\qquad F=(bkp,-bkq).
\]
Thus
\[
AE=ck,\quad AF=bk,\quad EF=ka.
\]
If \(I'\) is the incenter of \(\triangle AEF\), then \(AI'\) bisects \(\angle A\), and
\[
AI'=\frac{AE+AF-EF}{2p}
=\frac{k(S-a)}{2p}.
\tag{1}
\]

Now let \(\Gamma\) be the Euler circle. A direct substitution of the three side midpoints \(B/2,C/2,(B+C)/2\) gives the equation
\[
\Gamma:\quad x^2+y^2-\frac{S(2k+1)}{4p}x+\frac{(b-c)(2k-1)}{4q}y+\frac{bc k}{2}=0.
\]
Hence
\[
N_x=\frac{S(2k+1)}{8p},\qquad w=\frac{bc k}{2},
\]
and the nine-point radius is
\[
R=\frac{a}{8pq}.
\]

Let the center of \((W)\) be \(O=(d,0)\). Since \((W)\) is tangent to both sides \(AB,AC\), its radius is \(dq\), and its equation is
\[
x^2+y^2-2dx+d^2p^2=0.
\]
External tangency to \(\Gamma\) gives
\[
(d-N_x)^2+N_y^2=(R+dq)^2.
\]
Using \(N_x^2+N_y^2=R^2+w\), this simplifies to
\[
p^2d^2-2(N_x+Rq)d+w=0.
\tag{2}
\]
Since
\[
N_x+Rq=\frac{S(2k+1)+a}{8p},
\]
equation (2) becomes
\[
p^2d^2-\frac{S(2k+1)+a}{4p}d+\frac{bc k}{2}=0.
\tag{3}
\]

Now set
\[
d_0=\frac{k(S-a)}{4p^3}=\frac{kt}{4p^3}.
\]
Using
\[
bc=\frac{S^2-a^2}{4p^2}=\frac{t(S+a)}{4p^2},
\]
one checks that \(d_0\) satisfies (3). Indeed,
\[
\begin{aligned}
p^2d_0^2-\frac{S(2k+1)+a}{4p}d_0+\frac{bc k}{2}
&=\frac{k^2t^2}{16p^4}
-\frac{(4p^2S-t)}{4p}\frac{kt}{4p^3}
+\frac{kt(S+a)}{8p^2}\\
&=\frac{kt^2}{8p^2}-\frac{kSt}{4p^2}+\frac{kt(S+a)}{8p^2}\\
&=-\frac{kt(S+a)}{8p^2}+\frac{kt(S+a)}{8p^2}=0.
\end{aligned}
\]
Thus \(d=d_0\), because \(d_0\) is the smaller positive root of (3). Therefore
\[
AI'=2dp^2.
\]

The tangency points on \(AB,AC\) are
\[
X=(dp^2,-dpq),\qquad Y=(dp^2,dpq).
\]
Hence
\[
AX=AY=dp.
\]
Also
\[
I'X^2=(2dp^2-dp^2)^2+(dpq)^2
=d^2p^4+d^2p^2q^2
=d^2p^2
=(dp)^2.
\]
So \(XI'=AX\). By symmetry, \(I'Y=AX\). Therefore
\[
AX=XI'=I'Y=AY.
\]
Thus \(AXI'Y\) is a rhombus.

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A7: Correct (7/7)</summary>

\[
\boxed{AXI'Y\text{ is a rhombus}}
\]

Let \(\angle A=2\theta\), and set
\[
c=\cos\theta,\qquad s=\sin\theta,\qquad k=\cos2\theta=\cos A.
\]
Let
\[
AB=m,\qquad AC=n,\qquad BC=a,
\]
so by the cosine rule
\[
a^2=m^2+n^2-2mnk.
\]

Place \(A=(0,0)\) and the internal angle bisector of \(\angle A\) on the \(x\)-axis. Write
\[
B=(mc,ms),\qquad C=(nc,-ns).
\]
The feet of the altitudes are
\[
E=(kmc,-kms),\qquad F=(knc,kns).
\]
Thus in triangle \(AEF\),
\[
AE=km,\quad AF=kn,\quad EF=ka.
\]
Let \(q=m+n+a\). The incenter \(I'\) lies on the \(x\)-axis, and using the standard formula for the distance from the incenter to the vertex \(A\),
\[
AI'=\frac{2(km)(kn)c}{km+kn+ka}
=\frac{2mnkc}{q}.
\]
So
\[
I'=\left(\frac{2mnkc}{q},0\right). \tag{1}
\]

Now let the center of \((W)\) be \(O=(d,0)\), with radius \(ds\), since it is tangent to both sides of the angle. Put
\[
t=dc.
\]
Then the tangency points are
\[
X=(tc,ts),\qquad Y=(tc,-ts),
\]
and
\[
X+Y=(2tc,0). \tag{2}
\]
It remains to show that the tangency condition to the Euler circle gives
\[
2tc=\frac{2mnkc}{q},
\]
i.e. \(t=\frac{mnk}{q}\).

Let \(\mathcal E\) be the Euler circle, with center \(N\) and radius \(\rho\). The circumcenter and orthocenter of \(ABC\) are respectively
\[
O_c=\left(\frac{m+n}{4c},\frac{m-n}{4s}\right),\qquad
H=\left(\frac{k(m+n)}{2c},-\frac{k(m-n)}{2s}\right).
\]
Hence, since \(N\) is the midpoint of \(O_cH\),
\[
N_x=\frac{(m+n)(1+2k)}{8c}.
\]
Also
\[
\rho=\frac{a}{8sc}.
\]
Therefore
\[
N_x+\rho s=\frac{(m+n)(1+2k)+a}{8c}.
\]

The Euler circle meets \(AB\) at \(F\) and at the midpoint of \(AB\), so the power of \(A\) with respect to \(\mathcal E\) is
\[
AN^2-\rho^2=AF\cdot \frac m2
=kn\cdot \frac m2=\frac{k mn}{2}.
\]

Since \((W)\) is externally tangent to \(\mathcal E\),
\[
ON=\rho+ds.
\]
Squaring and expanding,
\[
(N_x^2+N_y^2-\rho^2)-2d(N_x+\rho s)+c^2d^2=0.
\]
Substituting the values above gives
\[
c^2d^2-\frac{(m+n)(1+2k)+a}{4c}d+\frac{k mn}{2}=0.
\]
Let
\[
T=(m+n)(1+2k)+a.
\]
Using \(t=dc\), this becomes
\[
t^2-\frac{T}{4c^2}t+\frac{k mn}{2}=0.
\]
A direct factorization using \(a^2=m^2+n^2-2mnk\) gives
\[
t^2-\frac{T}{4c^2}t+\frac{k mn}{2}
=
\left(t-\frac{mnk}{q}\right)\left(t-\frac q2\right).
\]
Thus the two possible values of \(t\) are
\[
t=\frac{mnk}{q}\quad\text{or}\quad t=\frac q2.
\]
The second root is larger than both \(m\) and \(n\), so it gives tangency points beyond \(B,C\), not on the sides themselves. Hence the circle closer to \(A\) corresponds to
\[
t=\frac{mnk}{q}.
\]
Therefore, by (2),
\[
X+Y=\left(2t c,0\right)
=\left(\frac{2mnkc}{q},0\right)=I'.
\]

So
\[
I'=X+Y.
\]
Hence
\[
\overrightarrow{XI'}=Y=\overrightarrow{AY},
\]
and
\[
\overrightarrow{I'Y}=-X=-\overrightarrow{AX}.
\]
Also
\[
|AX|=|X|=t,\qquad |AY|=|Y|=t.
\]
Therefore
\[
AX=XI'=I'Y=YA=t,
\]
and \(AXI'Y\) is a parallelogram with all sides equal. Hence it is a rhombus.

\[
\boxed{\text{AXI'}Y\text{ is a rhombus}}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

\[
\boxed{\text{Proof}}
\]

Let
\[
\angle BAC=2\alpha,\qquad k=\cos^2\alpha,\qquad h=\sin^2\alpha,\qquad q=\cos 2\alpha=2k-1.
\]
Write
\[
a=BC,\qquad b=CA,\qquad c=AB,\qquad M=a+b+c.
\]
Since \(E,F\) lie on the sides, the triangle is acute and \(q>0\).

---

### 1. Position of \(I'\)

In \(\triangle ABC\),
\[
AF=bq,\qquad AE=cq,
\]
and also
\[
EF=aq.
\]
Thus \(\triangle AEF\sim \triangle ABC\) with ratio \(q\). Hence its incenter \(I'\) lies on the angle bisector of \(\angle A\), and
\[
AI'=q\cdot AI.
\]
Using
\[
AI=\frac{bc\cos\alpha}{s}=\frac{bc\sqrt k}{T},\qquad T=\frac M2,
\]
we get
\[
AI'=\frac{2qbc\sqrt k}{M}. \tag{1}
\]

---

### 2. Determine the center \(O\) of \((W)\)

Let \(O=(p,0)\) be the center of \((W)\), where the angle bisector of \(\angle A\) is the \(x\)-axis. Since \((W)\) is tangent to \(AB,AC\), its radius is
\[
\rho=p\sin\alpha=p\sqrt h.
\]

The Euler circle passes through the feet \(E,F\) and the midpoints of the sides. Therefore its intersections with \(AB\) have distances
\[
bq,\quad \frac c2
\]
from \(A\), and with \(AC\) have distances
\[
cq,\quad \frac b2.
\]
If the Euler circle has equation
\[
x^2+y^2+ux+vy+\Pi=0,
\]
then comparing roots on the two sides gives
\[
\Pi=\frac{bcq}{2},
\]
and, with \(N=(N_x,N_y)\) its center,
\[
N_x=\frac{(b+c)(4k-1)}{8\sqrt k}.
\]
Its radius is the nine-point radius
\[
R_e=\frac{a}{8\sqrt{k}\sqrt h}.
\]

Since \((W)\) and the Euler circle are externally tangent,
\[
ON=R_e+\rho.
\]
Squaring and using \(AN^2-R_e^2=\Pi\), we get
\[
kp^2-2pN_x+\Pi=2R_e p\sqrt h.
\]
Substituting the above expressions for \(N_x,R_e,\Pi\) yields
\[
4k^{3/2}p^2-\bigl[(b+c)(4k-1)+a\bigr]p+2bcq\sqrt k=0. \tag{2}
\]

Now set
\[
p_0=\frac{qbc}{\sqrt k\,M}.
\]
Using
\[
a^2=(b+c)^2-4kbc,
\]
one checks directly that \(p_0\) satisfies (2). The other root is larger, so the smaller positive root, i.e. the center of \((W)\) closer to \(A\), is
\[
p=p_0=\frac{qbc}{\sqrt k\,M}.
\]
Therefore
\[
p=\frac{qbc}{\sqrt k\,M}. \tag{3}
\]

From (1) and (3),
\[
AI'=2kp. \tag{4}
\]

---

### 3. Show \(AXI'Y\) is a rhombus

Place the angle bisector on the \(x\)-axis. Then
\[
I'=(2kp,0),
\]
and the tangency points are
\[
X=(pk,p\sqrt{kh}),\qquad Y=(pk,-p\sqrt{kh}).
\]
Hence
\[
AX=AY=p\sqrt k.
\]
Also
\[
XI'^2=(pk-2kp)^2+(p\sqrt{kh})^2
=k^2p^2+kp^2h
=kp^2.
\]
Thus
\[
XI'=p\sqrt k=AX.
\]
By symmetry,
\[
I'Y=AX.
\]
Therefore
\[
AX=XI'=I'Y=AY.
\]
So \(AXI'Y\) is a rhombus.

\[
\boxed{\text{AXI}'\!\!\!\!Y\text{ is a rhombus.}}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

\[
\boxed{\text{ }AXI'Y\text{ is a rhombus.}}
\]

Let  
\[
a=BC,\qquad b=CA,\qquad c=AB,\qquad P=a+b+c,
\]
and write
\[
\alpha=\frac A2,\qquad u=\cos\alpha,\qquad v=\sin\alpha,\qquad k=\cos A=2u^2-1.
\]

Place \(A=(0,0)\), with the internal angle bisector of \(\angle A\) as the \(x\)-axis. Then we may take
\[
B=c(u,v),\qquad C=b(u,-v).
\]
The altitude feet are
\[
F=bk(u,v),\qquad E=ck(u,-v).
\]

The Euler circle is the nine-point circle of \(\triangle ABC\). It meets \(AB\) at \(F\) and at the midpoint of \(AB\), so on the line \(AB\) its equation
\[
x^2+y^2+Dx+Ey+F_0=0
\]
gives roots \(bk\) and \(c/2\) along the direction \((u,v)\). Similarly on \(AC\) the roots are \(ck\) and \(b/2\). Hence
\[
F_0=\frac{bc k}{2},\qquad 
D=-\frac{(b+c)(2k+1)}{4u}.
\]
The nine-point radius is
\[
R_N=\frac{a}{8uv},\qquad 2R_Nv=\frac{a}{4u}.
\]

Let \((W)\) have center \(O=(d,0)\) and radius \(dv\), since it is tangent to the two sides. External tangency with the Euler circle gives
\[
u^2d^2-\frac{(b+c)(2k+1)+a}{4u}d+\frac{bc k}{2}=0. \tag{1}
\]

Now consider \(\triangle AEF\). Its side lengths are \(AE=ck\), \(AF=bk\), \(EF=ak\), so its semiperimeter is \(\frac{kP}{2}\), and its area is \(k^2[ABC]\). Therefore its inradius \(r'\) satisfies
\[
r'=k r,
\]
where \(r\) is the inradius of \(\triangle ABC\). Since \(r=\frac{2[ABC]}{P}= \frac{2bcu v}{P}\), we get
\[
AI'=\frac{r'}{v}=\frac{2bcu k}{P}.
\]
Thus
\[
I'=\left(\frac{2bcu k}{P},0\right).
\]

Set
\[
m=\frac{bc k}{P},\qquad d_0=\frac{m}{u}.
\]
Using \(a^2=p^2-4bcu^2\), where \(p=b+c\), one verifies the identity
\[
p(2k+1)+a=2u^2P+\frac{4bc k u^2}{P}.
\]
Substituting \(d_0=m/u\) into (1) gives
\[
m^2-\left(\frac{mP}{2}+m^2\right)+\frac{Pm}{2}=0.
\]
Hence \(d_0\) is a root of the tangency equation. The other root is
\[
\frac{P}{2u}>d_0,
\]
so the circle closer to \(A\) is precisely the one with center \(O=(d_0,0)\). Therefore
\[
d=d_0=\frac{m}{u}=\frac{bc k}{Pu}.
\]

The tangency points on \(AB,AC\) are
\[
X=(mu,mv),\qquad Y=(mu,-mv),
\]
so \(M=(mu,0)\) is the midpoint of \(XY\). But
\[
AM=mu=\frac{bcu k}{P}=\frac{AI'}2,
\]
so \(M\) is also the midpoint of \(AI'\). Thus the diagonals \(AI'\) and \(XY\) bisect each other and are perpendicular. Therefore \(AXI'Y\) is a rhombus.

\[
\boxed{AXI'Y\text{ is a rhombus}.}
\]

</details>

<details><summary>A10: Correct (7/7)</summary>

\[
\boxed{\text{AXI'}Y\text{ is a rhombus.}}
\]

Let \(\angle BAC=2\theta\), and put  
\[
t=\cos\theta,\qquad s=\sin\theta,\qquad d=\cos 2\theta=2t^2-1.
\]
Place \(A=(0,0)\) and the internal angle bisector of \(\angle A\) on the \(x\)-axis. Write
\[
p=(t,s),\qquad q=(t,-s).
\]
Then \(AB\) has direction \(p\), \(AC\) has direction \(q\). Let
\[
F=m p,\qquad E=n q,
\]
so \(m=AF,\ n=AE\). Put
\[
P=m+n,\qquad \ell=EF=\sqrt{m^2+n^2-2mn d}.
\]

The nine-point circle \(\Gamma\) passes through \(E,F\) and the midpoints \(U=\frac n{2d}p\), \(V=\frac m{2d}q\). Write its equation as
\[
x^2+y^2-2hx-2ky+\lambda=0.
\]
On \(AB\), substituting \(\lambda p\) gives roots \(m\) and \(\frac n{2d}\), hence
\[
\lambda=\frac{mn}{2d},\qquad ht+ks=\frac m2+\frac n{4d}.
\]
Similarly on \(AC\),
\[
ht-ks=\frac n2+\frac m{4d}.
\]
Adding,
\[
h=\frac{P(2d+1)}{8dt}.
\]
The nine-point radius is
\[
R=\frac{\ell}{8sdt},
\]
so
\[
Rs=\frac{\ell}{8td}.
\]
Thus
\[
h+Rs=\frac{P(2d+1)+\ell}{8td}.
\]

Let \(W\) have center \(O=(u,0)\) and radius \(us\), since it is tangent to both sides. External tangency to \(\Gamma\) gives
\[
T u^2-2u(h+Rs)+\lambda=0,\qquad T=t^2.
\]
Substituting the expressions for \(h+Rs\) and \(\lambda=\frac{P^2-\ell^2}{8t^2d}\), we get
\[
8t^4d u^2-2tu\bigl(P(2d+1)+\ell\bigr)+P^2-\ell^2=0. \tag{1}
\]
One checks that
\[
u_0=\frac{P-\ell}{4t^3}
\]
is a root of (1). The other root is
\[
\frac{P+\ell}{2td}>u_0,
\]
so the circle closer to \(A\) corresponds to
\[
u=u_0=\frac{P-\ell}{4t^3}.
\]
Since \(AX=ut\),
\[
AX=\frac{P-\ell}{4t^2}. \tag{2}
\]

Now compute \(I'\), the incenter of \(\triangle AEF\). Using side-length weights,
\[
I'=\frac{mE+nF}{P+\ell}
=\left(\frac{2mn t}{P+\ell},0\right).
\]
Therefore
\[
AI'=\frac{2mn t}{P+\ell}.
\]
But
\[
P^2-\ell^2=2mn(1+d)=4mn t^2,
\]
so
\[
AI'=\frac{P-\ell}{2t}. \tag{3}
\]
Comparing (2) and (3),
\[
AI'=2t\,AX. \tag{4}
\]

Now \(X\) lies on \(AB\), so
\[
X=(AX\,t,AX\,s),\qquad I'=(AI',0).
\]
Let \(i=AI'\). Then
\[
XI'^2=(i-AXt)^2+(AXs)^2
=i^2-2i\,AX\,t+AX^2.
\]
Using \(i=2t\,AX\), we get \(i^2=2i\,AX\,t\), hence
\[
XI'^2=AX^2,
\]
so \(XI'=AX\). By symmetry about the \(x\)-axis,
\[
AY=AX,\qquad I'Y=XI'.
\]
Thus
\[
AX=AY=XI'=I'Y,
\]
so \(AXI'Y\) is a rhombus.

</details>

<details><summary>A11: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Let  
\[
A=2\theta,\qquad p=\cos\theta,\quad s=\sin\theta,\quad k=\cos 2\theta=2p^2-1,
\]
and set
\[
a=BC,\quad b=CA,\quad c=AB,\quad T=a+b+c.
\]

Place \(A=(0,0)\) and the internal angle bisector of \(\angle A\) on the \(x\)-axis. Then we may write
\[
B=(cp,cs),\qquad C=(bp,-bs).
\]
Since \(E,F\) are altitude feet,
\[
AE=ck,\qquad AF=bk,
\]
and by the cosine rule in \(\triangle AEF\),
\[
EF=ka.
\]
Thus the side lengths of \(\triangle AEF\) are \(ck,bk,ka\). If \(I'=(q,0)\), then using its inradius one obtains
\[
q=\frac{2bc kp}{T}. \tag{1}
\]

Now consider the Euler (nine-point) circle of \(\triangle ABC\). Let its center be \(N=(u,v)\) and radius \(\rho\). From the standard formulas for the circumcenter \(O\) and orthocenter \(H\),
\[
O=\left(\frac{b+c}{4p},\frac{c-b}{4s}\right),\qquad
H=\left(\frac{(b+c)k}{2p},\frac{b-c}{2s}\right),
\]
and since the nine-point center is \(N=(O+H)/2\),
\[
u=\frac{(b+c)(1+2k)}{8p},\qquad \rho=\frac{a}{8sp}.
\]
The equation of the Euler circle can be written
\[
x^2+y^2-2ux-2vy+\frac{bc k}{2}=0.
\]
Hence
\[
u+\rho s=\frac{(b+c)(1+2k)+a}{8p}. \tag{2}
\]

Let the center of \((W)\) be \(O_W=(d,0)\), so its radius is \(ds\). Since \((W)\) is externally tangent to the Euler circle,
\[
(d-u)^2+v^2=(\rho+ds)^2.
\]
Expanding and using (2),
\[
p^2d^2-\frac{d\big((b+c)(1+2k)+a\big)}{4p}+\frac{bc k}{2}=0. \tag{3}
\]

Put \(d_0=\dfrac{bc k}{pT}\). Substituting \(d=d_0\) into (3) and using
\[
a^2=b^2+c^2-2bc k
\]
shows the left-hand side is \(0\). Thus \(d_0\) is one root. The other root is \(\dfrac{T}{2p}\), which is larger than \(d_0\). Since \((W)\) is closer to \(A\) than the Euler circle, we must have
\[
d=d_0=\frac{bc k}{pT}. \tag{4}
\]

Using (1) and (4),
\[
q=AI'=\frac{2bc kp}{T}=2p^2d. \tag{5}
\]

Now the tangency points on \(AB,AC\) are
\[
X=(dp^2,dps),\qquad Y=(dp^2,-dps),
\]
while
\[
I'=(q,0)=(2dp^2,0).
\]
Therefore the diagonals of quadrilateral \(AXI'Y\) are
\[
AI':\ y=0,\qquad XY:\ x=dp^2.
\]
They are perpendicular and intersect at
\[
P=(dp^2,0),
\]
which is the midpoint of both \(AI'\) and \(XY\). Hence the diagonals bisect each other at right angles, so \(AXI'Y\) is a rhombus.

\[
\boxed{\text{Therefore } AXI'Y \text{ is a rhombus.}}
\]

</details>

<details><summary>A12: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Let  
\[
a=BC,\quad b=CA,\quad c=AB,\quad S=a+b+c,
\]
and write
\[
q=\cos A,\qquad m=\cos\frac A2,\qquad n=\sin\frac A2 .
\]
Place \(A=(0,0)\), with the internal angle bisector of \(\angle A\) as the \(x\)-axis. Then
\[
B=(cm,cn),\qquad C=(bm,-bn).
\]

The altitude feet are
\[
E=(cq m,-cq n),\qquad F=(bq m,bq n).
\]
Indeed \(AE=cq\), \(AF=bq\), and \(EF=aq\). Hence, in triangle \(AEF\), the side lengths opposite \(A,E,F\) are \(aq,bq,cq\), respectively. Therefore
\[
I'=\frac{bqE+cqF}{q(a+b+c)}
=\left(\frac{2bcmq}{S},0\right).
\]
So
\[
AI'=\frac{2bcmq}{S}. \tag{1}
\]

Now let \((W)\) have tangency length
\[
t=AX=AY.
\]
Since \(W\) is tangent to \(AB\) and \(AC\), its center lies on the \(x\)-axis. Write its center as \(O=(p,0)\). Then
\[
p=\frac{t}{m},\qquad \rho=\frac{tn}{m},
\]
where \(\rho\) is the radius of \((W)\). The tangency points are
\[
X=(tm,tn),\qquad Y=(tm,-tn).
\]

Let \(\Gamma\) be the Euler circle of \(\triangle ABC\), with center \(N=(u,v)\) and radius \(r\). A standard computation from the circumcenter and orthocenter gives
\[
u=\frac{(b+c)(1+2q)}{8m},\qquad r=\frac{a}{8mn}.
\]
Also, since \(\Gamma\) cuts \(AB\) at \(F\) and the midpoint of \(AB\),
\[
AN^2-r^2=AF\cdot AM_{AB}=bcq/2.
\]

Because \((W)\) and \(\Gamma\) are externally tangent,
\[
ON=\rho+r.
\]
Squaring and simplifying gives
\[
t^2-\frac{2t}{m}(u+nr)+\frac{bcq}{2}=0. \tag{2}
\]
Now
\[
u+nr=\frac{(b+c)(1+2q)+a}{8m}+\frac{a}{8m}
=\frac{(b+c)(1+2q)+a}{8m}.
\]
Hence
\[
\frac{2(u+nr)}{m}
=\frac{(b+c)(1+2q)+a}{2(1+q)}.
\]
Using \(a^2=b^2+c^2-2bcq\), one checks
\[
\frac{(b+c)(1+2q)+a}{2(1+q)}
=\frac S2+\frac{bcq}{S}.
\]
Thus (2) becomes
\[
t^2-\left(\frac S2+\frac{bcq}{S}\right)t+\frac{bcq}{2}=0. \tag{3}
\]
One root of this quadratic is
\[
t_0=\frac{bcq}{S}.
\]
The other root is \(S/2\), so the circle closer to \(A\) corresponds to
\[
t=\frac{bcq}{S}. \tag{4}
\]
Therefore
\[
2mt=\frac{2bcmq}{S}=AI' \qquad\text{by (1)}.
\]

Now \(X=(tm,tn)\) and \(Y=(tm,-tn)\), so the midpoint of \(XY\) is
\[
(tm,0).
\]
But \(I'=(d,0)\) with \(d=AI'=2tm\), so the midpoint of \(AI'\) is also \((tm,0)\). Hence the diagonals \(AI'\) and \(XY\) bisect each other. They are perpendicular because \(AI'\) is the \(x\)-axis and \(XY\) is vertical.

Therefore \(AXI'Y\) is a parallelogram with perpendicular diagonals, hence a rhombus.

\[
\boxed{AXI'Y\text{ is a rhombus.}}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

\[
\boxed{\text{We prove that } A,X,I',Y \text{ is a rhombus.}}
\]

Assume \(ABC\) is acute; the usual directed-length argument covers the other cases.

Let
\[
a=BC,\qquad b=CA,\qquad c=AB,
\]
and write
\[
\angle BAC=2\theta,\qquad m=\cos\theta,\qquad n=\sin\theta,\qquad t=\cos2\theta=m^2-n^2.
\]
Place \(A=(0,0)\) and take the internal angle bisector of \(\angle A\) as the \(x\)-axis. Then
\[
B=(cm,cn),\qquad C=(bm,-bn).
\]

The altitude feet are
\[
F=(btm,btn),\qquad E=(ctm,-ctn).
\]
Thus
\[
AF=bt,\quad AE=ct,\quad EF=at.
\]
Using the incenter formula in \(\triangle AEF\),
\[
I'=\frac{btE+ctF}{t(a+b+c)}
=\frac{bc t(u+v)}{a+b+c},
\]
where \(u=(\cos\theta,\sin\theta)\), \(v=(\cos\theta,-\sin\theta)\). Since \(u+v=(2m,0)\),
\[
I'=\left(\frac{2bc t m}{a+b+c},0\right).
\]

Let the Euler circle \(\Gamma\) have equation
\[
x^2+y^2+Dx+\lambda y+\gamma=0.
\]
Since \(\Gamma\) cuts \(AB\) at \(F\) and \(B/2\), and \(AC\) at \(E\) and \(C/2\), comparing the roots on \(AB\) and \(AC\) gives
\[
D=-\frac{(b+c)(2t+1)}{4m},\qquad \gamma=\frac{bc t}{2}.
\]
Also \(\Gamma\) is the nine-point circle, so its radius is
\[
\rho=\frac{R}{2}=\frac{a}{8mn}.
\]

Let \((W)\) have center \(O=(u,0)\). Since it is tangent to both sides \(AB,AC\), its radius is \(un\). The tangency points are
\[
X=(um^2,umn),\qquad Y=(um^2,-umn).
\]
Thus
\[
X+Y=(2um^2,0).
\]
So it suffices to show
\[
u=\frac{bc t}{m(a+b+c)}.
\]

The nine-point circle has center \(N=(-D/2,-\lambda/2)\), and using
\[
ON^2=u^2+Du+\rho^2+\gamma,
\]
the external tangency \(ON=\rho+un\) gives
\[
m^2u^2+Du+\gamma=2\rho n u.
\]
Since \(2\rho n=\dfrac{a}{4m}\), this is
\[
m^2u^2+Du+\gamma=\frac{a u}{4m}. \tag{1}
\]

Set
\[
u_0=\frac{bc t}{m(a+b+c)}.
\]
A direct substitution using
\[
4m^2bc=b^2+2bc+c^2-a^2=(b+c)^2-a^2
\]
and \(a+b+c=S\) verifies (1) for \(u=u_0\). Indeed,
\[
\frac{m^2u_0^2+Du_0+\gamma}{bc t}
=\frac{bc t}{S^2}-\frac{(b+c)(2t+1)}{4m^2S}+\frac12
=\frac{a}{4m^2S},
\]
which is exactly (1) divided by \(bc t\). Hence \(u_0\) is one root of the quadratic obtained from (1).

The other root is \(\dfrac{S}{2m}>u_0\), so the circle closer to \(A\) has
\[
u=u_0=\frac{bc t}{m(a+b+c)}.
\]
Therefore
\[
I'=\left(\frac{2bc t m}{a+b+c},0\right)
=(2u_0m^2,0)=X+Y.
\]

Thus \(I'=X+Y\), so \(AXI'Y\) is a parallelogram. Also
\[
AX=AY,
\]
because \(X\) and \(Y\) are symmetric about the \(x\)-axis. Hence a parallelogram with equal adjacent sides is a rhombus.

\[
\boxed{AXI'Y\text{ is a rhombus}.}
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

\[
\boxed{\text{Proof}}
\]

Let \(\angle A=2\theta\), and write
\[
q=\cos\theta,\qquad s=\sin\theta,\qquad \gamma=\cos A=q^2-s^2.
\]
Assume \(ABC\) is acute, so all the lengths below are ordinary positive lengths. Put
\[
a=BC,\qquad b=CA,\qquad c=AB,
\]
and set
\[
u=b+c,\qquad v=b-c.
\]
Then
\[
a^2=u^2-4bcq^2. \tag{1}
\]

Place \(A\) at the origin and the internal angle bisector of \(\angle A\) on the \(x\)-axis:
\[
B=(cq,-cs),\qquad C=(bq,bs).
\]
The altitude feet are
\[
F=(b\gamma q,-b\gamma s),\qquad E=(c\gamma q,c\gamma s).
\]
One checks that
\[
EF=a\gamma,\qquad AE=c\gamma,\qquad AF=b\gamma.
\]
Thus triangle \(AEF\) is similar to triangle \(ABC\) with scale factor \(\gamma\). Hence its tangent length from \(A\) is
\[
\gamma\frac{b+c-a}{2}=\frac{\gamma(u-a)}2.
\]
Therefore, if \(I'\) is the incenter of \(AEF\), then
\[
AI'=\frac{\gamma(u-a)}{2q}. \tag{2}
\]

Now define
\[
t=\frac{\gamma(u-a)}{4q^2}.
\]
Then
\[
2qt=\frac{\gamma(u-a)}{2q},
\]
so by (2),
\[
AI'=2qt.
\]
Let
\[
e_1=(q,-s),\qquad e_2=(q,s),
\]
the unit vectors along \(AB\) and \(AC\). Put
\[
X=t e_1,\qquad Y=t e_2.
\]
Then
\[
X+Y=t(e_1+e_2)=(2tq,0),
\]
which is exactly the point \(I'\) on the angle bisector. Hence
\[
I'=X+Y.
\]
Consequently,
\[
AX=AY=t,\qquad XI'=I'Y=t,
\]
so \(AXI'Y\) is a rhombus once we identify these \(X,Y\) with the tangency points of the given circle \((W)\).

It remains to show that this circle is indeed \((W)\).

Consider the circle centered at \(O=(o,0)\) with
\[
o=\frac{t}{q}=\frac{\gamma(u-a)}{4q^3},\qquad r=os.
\]
Its tangency points with \(AB\) and \(AC\) are precisely \(X=t e_1\) and \(Y=t e_2\). We show this circle is tangent to the Euler circle.

The Euler circle has equation
\[
x^2+y^2-\frac{u(1+2\gamma)}{4q}x-\frac{v(1-2\gamma)}{4s}y+\frac{\gamma bc}{2}=0.
\]
Its center \(N\) and radius \(R\) satisfy
\[
R=\frac{a}{8sq}.
\]
For \(O=(o,0)\), the power of \(O\) with respect to the Euler circle is
\[
\Pi=o^2-\frac{u(1+2\gamma)o}{4q}+\frac{\gamma bc}{2}.
\]
Using \(r=os\), we have
\[
2Rr+r^2=\frac{ao}{4q}+o^2s^2.
\]
Thus
\[
\Pi-(2Rr+r^2)
=o^2q^2-\frac{o(u(1+2\gamma)+a)}{4q}+\frac{\gamma bc}{2}.
\]
Put \(L=u-a\). Since \(o=\gamma L/(4q^3)\), multiplying the above expression by \(16q^4/\gamma\) gives
\[
\gamma L^2-L\bigl(u(1+2\gamma)+a\bigr)+8bcq^4.
\]
But
\[
L\bigl(u(1+2\gamma)+a\bigr)-\gamma L^2
=L\bigl((1+\gamma)(u+a)\bigr)
=2q^2L(u+a)
=2q^2(u^2-a^2)
=8bcq^4.
\]
Hence the expression is \(0\), so
\[
\Pi=2Rr+r^2.
\]
Therefore
\[
ON^2=R^2+\Pi=(R+r)^2,
\]
so
\[
ON=R+r.
\]
Thus the circle centered at \(O\) with radius \(r\) is externally tangent to the Euler circle. It is the circle closer to \(A\) than the Euler circle, hence it is exactly \((W)\).

Therefore the tangency points of \((W)\) with \(AB,AC\) are \(X,Y\) defined above, and we already proved
\[
AX=XI'=I'Y=AY.
\]
So \(AXI'Y\) is a rhombus.

\[
\boxed{\text{Thus } AXI'Y \text{ is a rhombus.}}
\]

</details>

<details><summary>A15: Correct (7/7)</summary>

Let  
\[
a=BC,\qquad b=CA,\qquad c=AB,\qquad S=b+c,\qquad P=bc,
\]
and write
\[
\mu=\cos A,\qquad p=\cos\frac A2,\qquad q=\sin\frac A2 .
\]
Then \(\mu=p^2-q^2\), so
\[
a^2=S^2-2P(1+\mu). \tag{1}
\]

Place \(A=(0,0)\) and the internal angle bisector of \(\angle A\) on the \(x\)-axis. Then
\[
B=(cp,cq),\qquad C=(bp,-bq).
\]
The altitude feet are
\[
F=bm(p,q),\qquad E=cm(p,-q).
\]

Let \(\Gamma\) be the Euler circle (nine-point circle). Since it passes through \(F\) and the midpoint of \(AB\), its equation
\[
x^2+y^2+Ux+Vy+K=0
\]
has, on the line \(AB\), intersection parameters \(\lambda=bm\) and \(\lambda=c/2\). Hence
\[
K=\frac{P\mu}{2}.
\]
Similarly, on \(AC\), the same \(K\) is obtained. Adding the two linear equations gives
\[
U=-\frac{S(2\mu+1)}{4p}.
\]
Thus the center \(N\) of \(\Gamma\) has
\[
N_x=\frac{S(2\mu+1)}{8p},
\]
and its radius is
\[
\rho=\frac{a}{8pq}.
\]

Now let the circle \(\omega=(W)\) have center \(O=(d,0)\) on the angle bisector. Since it is tangent to both sides, its radius is \(dq\). Put
\[
t=AX=AY=dp,
\]
so \(d=t/p\). The equation of \(\omega\) is
\[
x^2+y^2-\frac{2t}{p}x+t^2=0.
\]

External tangency to \(\Gamma\) gives
\[
(d-N_x)^2+N_y^2=(dq+\rho)^2.
\]
Using \(N_x^2+N_y^2-\rho^2=K\) and \(N_x+q\rho=\frac{S(2\mu+1)+a}{8p}\), this simplifies to
\[
t^2-\frac{t\bigl(S(2\mu+1)+a\bigr)}{2(1+\mu)}+\frac{P\mu}{2}=0. \tag{2}
\]
Multiplying by \(2(1+\mu)\), equation (2) becomes
\[
2(1+\mu)t^2-\bigl(S(2\mu+1)+a\bigr)t+P\mu(1+\mu)=0.
\]
Using (1), one checks that
\[
2(1+\mu)t^2-\bigl(S(2\mu+1)+a\bigr)t+P\mu(1+\mu)
=2(1+\mu)\left(t-\frac{P\mu}{a+S}\right)\left(t-\frac{a+S}{2}\right).
\]
Therefore the two possible values of \(t\) are
\[
t_0=\frac{P\mu}{a+S},\qquad t_1=\frac{a+S}{2}.
\]
The circle \(W\) closer to \(A\) is the smaller one, so
\[
t=t_0=\frac{P\mu}{a+S}. \tag{3}
\]

Now consider triangle \(AEF\). The reflection in the angle bisector followed by the homothety of ratio \(\mu=\cos A\) sends
\[
B\mapsto E,\qquad C\mapsto F.
\]
Hence it sends the incenter \(I\) of \(ABC\) to the incenter \(I'\) of \(AEF\). Since
\[
I=\left(\frac{2Pp}{a+S},0\right),
\]
we get
\[
AI'=\mu\cdot \frac{2Pp}{a+S}=2p\cdot \frac{P\mu}{a+S}=2pt. \tag{4}
\]

In coordinates,
\[
X=t(p,q),\qquad Y=t(p,-q),\qquad I'=(2pt,0).
\]
Therefore
\[
AX=AY=t,
\]
and
\[
XI'^2=(tp-2pt)^2+(tq)^2=t^2(p^2+q^2)=t^2,
\]
so \(XI'=t\). Similarly \(YI'=t\). Hence
\[
AX=XI'=I'Y=YA,
\]
so \(AXI'Y\) is a rhombus.

\[
\boxed{AXI'Y\text{ is a rhombus}}
\]

</details>

<details><summary>A16: Correct (7/7)</summary>

\[
\boxed{\text{Proof.}}
\]

Let \(\theta=\frac A2\), \(c=\cos\theta\), \(s=\sin\theta\), and
\[
k=\cos 2\theta=c^2-s^2.
\]
Place \(A=(0,0)\), with the internal angle bisector of \(\angle A\) as the \(x\)-axis. Write
\[
B=(pc,ps),\qquad C=(qc,-qs),
\]
where \(p=AB,\ q=AC\), and let \(a=BC\). Put
\[
P=pq,\qquad S=p+q,\qquad L=S+a.
\]

Since \(E,F\) are the altitude feet,
\[
E=(pkc,-pks),\qquad F=(qkc,qk s).
\]
Thus
\[
AE=pk,\qquad AF=qk,\qquad EF=ka.
\]
Using the standard incenter coordinate formula in triangle \(AEF\),
\[
I'=\frac{qkE+pkF}{kL}
=\frac{Pk}{L}(u+v)
=\left(\frac{2Pkc}{L},0\right).
\]

Now let the circle \((W)\) have center \(O=(d,0)\). Because it is tangent to \(AB,AC\), its radius is \(\rho=ds\), and its tangency points are
\[
X=dc\,u=(dc^2,dcs),\qquad Y=dc\,v=(dc^2,-dcs).
\]
Hence
\[
X+Y=(2dc^2,0).
\]
We will show that \(I'=X+Y\), i.e.
\[
d=\frac{Pk}{cL}.
\]

Let \(\Gamma\) be the Euler circle of \(\triangle ABC\), i.e. the nine-point circle. It passes through \(E,F\) and the midpoints of \(AB,AC\). If
\[
\Gamma:x^2+y^2+\alpha x+\beta y+\gamma=0,
\]
then on \(AB\) the circle meets the line at distances \(qk\) and \(p/2\), and on \(AC\) at distances \(pk\) and \(q/2\). Therefore
\[
\alpha c+\beta s=-\left(qk+\frac p2\right),\qquad
\alpha c-\beta s=-\left(pk+\frac q2\right),\qquad
\gamma=\frac{Pk}{2}.
\]
Solving,
\[
\alpha=-\frac{S(2k+1)}{4c},\qquad
\beta=\frac{(p-q)(2k-1)}{4s}.
\]
The center of \(\Gamma\) is \(N=(-\alpha/2,-\beta/2)\), so
\[
N_x=\frac{S(2k+1)}{8c}.
\]
Its radius is the nine-point radius:
\[
r_9=\frac{a}{8sc}.
\]

Since \((W)\) and \(\Gamma\) are externally tangent,
\[
|O-N|=ds+r_9.
\]
Squaring and expanding gives
\[
d c^2-2N_x+\frac{\gamma}{d}=2sr_9.
\]
Substituting \(N_x\) and \(r_9\),
\[
dc^2-\frac{S(2k+1)}{4c}+\frac{Pk}{2d}=\frac{a}{4c}.
\]
Multiplying by \(4c\),
\[
4dc^3+\frac{2cPk}{d}=S(2k+1)+a. \tag{1}
\]

Now set
\[
d_0=\frac{Pk}{cL}.
\]
Using \(a^2=S^2-4Pc^2\), one checks
\[
4Pc^2+L^2=2SL.
\]
Therefore
\[
4c^3d_0+\frac{2cPk}{d_0}
=\frac{4Pkc^2}{L}+2c^2L
=2Sk+L
=S(2k+1)+a,
\]
so \(d_0\) satisfies (1). The other root of the resulting quadratic is \(L/(2c)\), hence \(d_0\) is the smaller positive root. Since the circle closer to \(A\) corresponds to the smaller \(d\), we have
\[
d=d_0=\frac{Pk}{cL}.
\]

Thus
\[
I'=\left(\frac{2Pkc}{L},0\right)
=(2d_0c^2,0)=X+Y.
\]

Finally, the quadrilateral \(AXI'Y\) has vertices
\[
0,\quad X,\quad X+Y,\quad Y.
\]
Its side vectors are
\[
\vec{AX}=X,\qquad \vec{XI'}=Y,\qquad \vec{I'Y}=-X,\qquad \vec{YA}=-Y.
\]
Since \(|X|=|Y|=dc\), all four sides have the same length. Hence \(AXI'Y\) is a rhombus.

\[
\boxed{\text{Therefore } AXI'Y \text{ is a rhombus.}}
\]

</details>
