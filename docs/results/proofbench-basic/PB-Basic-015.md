# PB-Basic-015

Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.

## Problem

Adrian is lining up $n \geq 2$ toy cars in a row. Each car has a width and length, and no two cars have the same width or length. Initially, the cars are arranged in increasing order of length from left to right. Adrian repeatedly does the following: he chooses some two adjacent cars where the left car is shorter in length and greater in width than the right car, and he swaps them. He keeps doing this until no further moves are possible. Prove that no matter how Adrian chooses his swaps, the procedure will eventually terminate, and in the end, the cars will be sorted in increasing order of width from left to right.

## Swarm: accepted (best candidate `P2`; self-verification grades [7, 7, 7]; 900,581 tokens in 56 calls)

**Blind grade: Correct (7/7).** Proves that shorter-and-narrower pairs never reorder, that each move lowers the width-inversion count by one, and that a terminal adjacent width descent would be a reversed good pair, which is complete and rigorous.

Let each car be denoted by its length rank \(l(c)\) and width rank \(w(c)\).  
All \(l(c)\) are distinct, and all \(w(c)\) are distinct.

We prove two facts simultaneously.

### 1. A useful invariant

Call two cars \(x,y\) **good** if
\[
l(x)<l(y)\quad\text{and}\quad w(x)<w(y).
\]
Initially, the cars are arranged in increasing length, so every good pair \(x,y\) has \(x\) to the left of \(y\).

A good pair can never be swapped directly: to swap \(x\) and \(y\) while \(l(x)<l(y)\), they would have to become adjacent with \(x\) immediately left of \(y\). The swap rule would then require
\[
w(x)>w(y),
\]
contradicting \(w(x)<w(y)\). Since the relative order of two cars changes only by swapping them directly, every good pair \(x,y\) remains in the order \(x\) left of \(y\) forever.

### 2. Termination

Consider the number \(N\) of pairs \(x,y\) such that \(x\) is left of \(y\) and \(w(x)>w(y)\). This is the number of “width inversions” in the current row of cars.

A move swaps adjacent cars \(a,b\) with
\[
w(a)>w(b).
\]
For every other car \(c\), either \(c\) is entirely to the left of both \(a,b\), or entirely to the right of both; hence the relative order of \(c\) with each of \(a,b\) is unchanged. Therefore only the pair \((a,b)\) changes its inversion status: before the swap \(a\) is left of \(b\) and \(w(a)>w(b)\), so this pair is a width inversion; after the swap it is not.

Thus every move decreases \(N\) by exactly \(1\). Since \(N\ge 0\) and initially \(N\le \binom n2\), the procedure can have at most \(\binom n2\) moves. Hence it terminates.

### 3. The final order is by increasing width

At the end, no adjacent cars \(x,y\) satisfy both
\[
l(x)<l(y)\quad\text{and}\quad w(x)>w(y).
\]
Suppose the final widths were not increasing. Then there would be adjacent cars \(x,y\) with
\[
w(x)>w(y).
\]
Since no move is possible, we must have
\[
l(x)>l(y).
\]
Thus \(y\) is shorter and narrower than \(x\), so the pair \((y,x)\) is good. By the invariant, \(y\) must appear to the left of \(x\), contradicting that \(x\) is immediately to the left of \(y\).

Therefore no adjacent pair has \(w(x)>w(y)\), so the widths strictly increase from left to right.

\[
\boxed{\text{The procedure terminates, and the final order is sorted by increasing width.}}
\]

## Single calls (16 independent samples, up to 128K tokens each, no forced finish)

Mean blind grade 4.50/7; graded Correct: 7 of 16.

| sample | finish | tokens | grade | reason |
|---|---|---:|---|---|
| A1 | stop | 93,394 | Partial (3/7) | Termination via the decreasing inversion count and the invariance of compatible (shorter-and-narrower) pairs are correct, but the crucial claim that no inverted pair remains at termination is justified by the invalid argument that 'one could bring them adjacent and swap them', so the core of the sortedness proof is missing. |
| A2 | stop | 37,561 | Correct (7/7) | Classifies each pair into four types and shows a move only turns a type-B pair into type C, so type D never appears and the number of B pairs drops; any final adjacent width descent would then be a legal B-type move, giving a complete proof. |
| A3 | stop | 60,799 | Partial (2/7) | Termination is correct and it notes that same-direction pairs (shorter and narrower) keep their order, but it argues B=0 at termination circularly, by assuming the width-sorted order is reached and by treating a possibly non-adjacent bad pair as an available swap, so the final order is not proved. |
| A4 | stop | 38,961 | Correct (7/7) | Width inversions drop by exactly one per move, and at a stable state an adjacent width descent is either a legal swap or a longer-and-wider pair whose relative order is invariant from the start, giving a complete and rigorous proof. |
| A5 | stop | 73,523 | Correct (7/7) | Termination follows since each move swaps a bad pair that can never be swapped again, and at a stable state any adjacent width descent is either a legal move or a shorter-and-narrower pair that can never be reordered, matching the reference argument. |
| A6 | stop | 85,113 | Partial (2/7) | Termination via the count N is correct and it notes that same-direction pairs (shorter and narrower) never change order, but it asserts N=0 at termination without proof (having no adjacent legal pair does not rule out non-adjacent counted pairs), so the final order is not proved. |
| A7 | stop | 18,276 | Partial (1/7) | Termination via counting width-inverted pairs is correct, but it simply asserts that no bad pairs remain at termination, without using the length condition or any invariant, so the main claim is unproved. |
| A8 | stop | 64,365 | Correct (7/7) | Proves that a car both shorter and narrower than another always stays to its left, proves termination by counting width-inverted pairs still in length order, and gets a valid contradiction from any final adjacent width descent; the only flaw is a letter mix-up in the last sentence that does not affect the logic. |
| A9 | stop | 72,677 | Correct (7/7) | Rigorous termination via the bad-pair count, plus a valid induction showing the narrowest car never passes a longer car and must be first in a stable row (its left neighbor would be shorter and wider, allowing a swap), after which the remaining cars form a legal (n-1)-car run. |
| A10 | stop | 87,545 | Partial (2/7) | Termination via a strictly decreasing inversion count is correct, but the sortedness part rests on a 'standard adjacent-inversion argument' that is false in general and wrongly treats P=0 as equivalent to width-sortedness, never proving that compatible pairs keep their order. |
| A11 | stop | 88,075 | Almost (5/7) | Termination and the key invariant (the narrowest car never passes a longer car) are correct, but it concludes the narrowest car must be first without ever invoking the stopping condition (its left neighbor would be shorter and wider, giving a legal move), and the 'and so on' induction is only sketched. |
| A12 | stop | 80,597 | Partial (3/7) | Termination and the invariance of compatible pairs are correct, but the crucial claim that the process cannot stop while a bad pair remains is attributed to a 'standard adjacent-pair argument' that is false for general configurations and needs the invariant, so the main step is unproven. |
| A13 | stop | 34,798 | Correct (7/7) | Proves termination because width inversions drop by exactly one per move, proves that a car both shorter and narrower than another is never swapped with it and so stays to its left, and gets a contradiction from any final adjacent width descent. |
| A14 | stop | 44,888 | Correct (7/7) | Shows every legal swap exchanges two adjacent cars that are incomparable in the both-smaller order, so the row stays a linear extension of that order; this forces any final adjacent width descent to be a legal move, and termination follows from width inversions dropping by one per move. |
| A15 | stop | 98,965 | Partial (4/7) | Termination is correct and it shows the narrowest car cannot be passed by longer cars and ends at the front, but the recursive step rests on the false claim that the other cars are still in length order when that car reaches the front (other swaps may happen first), so the proof does not cover every order of swaps. |
| A16 | stop | 96,130 | Partial (1/7) | Termination via width inversions is correct, but the final-order step ignores the length condition in the move rule and just asserts that no adjacent width descent can remain, which is the main thing the problem asks to prove. |

<details><summary>A1: Partial (3/7)</summary>

Let the cars be indexed by their length ranks: car \(i\) has length rank \(i\), with \(1<2<\cdots<n\).  
Let \(\pi(i)\) be the width rank of car \(i\). Thus \(1,2,\dots,n\) is the identity permutation, and width order is given by \(\pi\).

For \(i<j\), call the pair \(\{i,j\}\) an inversion if
\[
\pi(i)>\pi(j).
\]
There are finitely many such pairs, and initially every inversion has its smaller-length car \(i\) to the left of the larger-length car \(j\).

Define
\[
I=\#\{(i,j): i<j,\ \pi(i)>\pi(j),\ \text{and car }i\text{ is left of car }j\}.
\]
Initially \(I\) equals the total number of inversions of \(\pi\).

Now consider one swap Adrian makes. It swaps adjacent cars \(a<b\) with \(\pi(a)>\pi(b)\), i.e. an inversion \(\{a,b\}\). This swap changes only the relative order of cars \(a\) and \(b\): before the swap car \(a\) is left of car \(b\), and after the swap car \(b\) is left of car \(a\). No other pair changes its order, so \(I\) decreases by exactly \(1\).

Therefore each swap reduces \(I\) by \(1\), and since \(I\ge 0\), the procedure can have at most finitely many swaps. Hence it terminates.

At termination \(I=0\). Indeed, if some inversion \(\{i,j\}\) with \(i<j\) still had car \(i\) left of car \(j\), then one could bring them adjacent and swap them, giving another possible move; this contradicts termination. Thus every inversion \(\{i,j\}\) has car \(j\) left of car \(i\).

For non-inversions \(\pi(i)<\pi(j)\), car \(i\) is left of car \(j\) from the start, and they can never be swapped because a swap would require \(\pi(i)>\pi(j)\).

Hence for every pair of cars \(A,B\), the car with smaller width is placed to the left of the car with larger width. Therefore the cars are sorted by increasing width from left to right.

\[
\boxed{\text{The procedure terminates, and in the final order the cars are sorted in increasing order of width.}}
\]

</details>

<details><summary>A2: Correct (7/7)</summary>

Let the cars be labeled by increasing length: car \(1\) is the shortest, car \(2\) is next, etc.  
For two cars \(X,Y\), suppose \(X\) is currently to the left of \(Y\). Because all lengths and widths are distinct, we may classify their current relative order as one of four types:

\[
\begin{array}{c|cc}
 & L_X<L_Y & L_X>L_Y\\
\hline
W_X<W_Y & A & C\\
W_X>W_Y & B & D
\end{array}
\]

where \(A\) means both inequalities are increasing, \(B\) means length is increasing but width is decreasing, \(C\) means length is decreasing but width is increasing, and \(D\) means both are decreasing.

Initially the cars are in increasing length order, so for every \(X\) left of \(Y\), we have \(L_X<L_Y\). Hence there are no \(D\)-pairs.

A allowed move swaps adjacent cars \(X,Y\) with

\[
L_X<L_Y,\qquad W_X>W_Y,
\]

so this adjacent pair is type \(B\). After the swap, \(Y\) is left of \(X\), and now

\[
L_Y>L_X,\qquad W_Y<W_X,
\]

so this same pair becomes type \(C\). Every other pair of cars has unchanged relative order and unchanged length/width comparisons, so its type does not change.

Therefore the total number of type-\(B\) pairs strictly decreases by exactly \(1\) on every move. Since there are only \(\binom n2\) pairs of cars, the process cannot continue forever; it terminates after at most \(\binom n2\) moves.

At termination, there are no adjacent type-\(B\) pairs. Also, no type-\(D\) pair can ever appear, because type-\(D\) would have required \(L_X>L_Y\) and \(W_X>W_Y\), and the only type changes are \(B\to C\).

Now consider any adjacent pair \(X,Y\). If \(W_X>W_Y\), then type \(D\) is impossible, so we must have \(L_X<L_Y\); hence this adjacent pair would be type \(B\), contradicting termination. Thus \(W_X<W_Y\) for every adjacent pair. Therefore the widths strictly increase from left to right.

Hence the procedure terminates, and in the end the cars are sorted in increasing order of width from left to right.

\[
\boxed{\text{The cars are finally arranged by increasing width.}}
\]

</details>

<details><summary>A3: Partial (2/7)</summary>

Let the cars be labeled \(1,2,\dots,n\) in increasing order of length, so
\[
L_1<L_2<\cdots<L_n.
\]
Let \(W_i\) denote the width of car \(i\).

Define a **bad pair** as a pair \(i<j\) such that
\[
W_i>W_j
\]
and car \(i\) is currently to the left of car \(j\). Let \(B\) be the number of bad pairs.

Initially, for every \(i<j\), car \(i\) is left of car \(j\), so
\[
B=\#\{(i,j): i<j,\ W_i>W_j\},
\]
which is finite.

Now consider an allowed swap of adjacent cars \(a,b\) with
\[
a<b,\qquad W_a>W_b.
\]
Before the swap, \((a,b)\) is a bad pair. After the swap, car \(b\) is left of car \(a\), so \((a,b)\) is no longer bad. For any third car \(c\), the car \(c\) remains on the same side of both \(a\) and \(b\), so only the relative order of \(a\) and \(b\) changes. Hence exactly one bad pair is removed.

Therefore every move decreases \(B\) by exactly \(1\). Since \(B\ge 0\), the procedure must terminate after at most \(\binom n2\) moves.

At termination, \(B=0\): if any bad pair \(i<j\) with \(W_i>W_j\) remained with car \(i\) left of car \(j\), then car \(j\) would still have to pass car \(i\) to reach the width-sorted order, which would require an allowed adjacent swap of \(i,j\), contradicting that no further moves are possible.

Thus for every pair \(i<j\):

- if \(W_i<W_j\), then car \(i\) is left of car \(j\) because this order is invariant;
- if \(W_i>W_j\), then \(B=0\) implies car \(j\) is left of car \(i\).

So for every pair of cars, the one with smaller width is to the left. Hence the widths increase left to right.

\[
\boxed{\text{The procedure terminates and the final order is increasing in width.}}
\]

</details>

<details><summary>A4: Correct (7/7)</summary>

\[
\boxed{\text{The procedure terminates, and the final order is by increasing width.}}
\]

Let the cars be given width ranks \(1<2<\cdots<n\) from left to right in a configuration.  
At any moment write down the sequence of width ranks

\[
w_1,w_2,\dots,w_n.
\]

Because all widths are distinct, this is a permutation of \(\{1,\dots,n\}\). Define

\[
I=\#\{(i,j): i<j,\ w_i>w_j\},
\]

the number of width inversions.

### 1. Termination

Consider one move. Adrian swaps two adjacent cars whose widths are \(a>b\), i.e.

\[
w_i=a,\qquad w_{i+1}=b,\qquad a>b.
\]

After the swap, the entries \(a,b\) become \(b,a\). For every car to the left of the two swapped cars, the comparisons with \(a\) and \(b\) are unchanged; the same holds for cars to the right. The only change is the pair \((a,b)\), which changes from an inversion to a non-inversion. Hence

\[
I\mapsto I-1.
\]

Thus every move decreases \(I\) by exactly \(1\). Since \(I\ge 0\), only finitely many moves can occur. Therefore Adrian’s procedure terminates.

### 2. Final order is by increasing width

Suppose, for contradiction, that the final row is not sorted by increasing width. Then there are adjacent cars \(X,Y\) with

\[
w_X>w_Y.
\]

There are two possibilities.

#### Case 1: \(l_X<l_Y\)

Then the shorter car \(X\) is left of the longer car \(Y\), but \(X\) is wider than \(Y\). Thus \(X\) is shorter in length and greater in width than \(Y\), so this adjacent pair is a legal swap. This contradicts termination. Hence this case cannot occur.

#### Case 2: \(l_X>l_Y\)

Then \(X\) is longer than \(Y\) and wider than \(Y\). To swap \(X\) and \(Y\) directly, one of the two possible orders would have to satisfy the swap rule:

- if \(X\) is left of \(Y\), then \(l_X<l_Y\) is false;
- if \(Y\) is left of \(X\), then \(w_Y>w_X\) is false.

So \(X\) and \(Y\) can never be swapped with each other; their relative order is invariant. Initially, because the cars were lined up in increasing length order, the shorter car \(Y\) was to the left of the longer car \(X\). Therefore in every reachable configuration \(Y\) is still left of \(X\). But in the final adjacent descent \(X,Y\), we have \(X\) left of \(Y\), contradiction.

Thus no adjacent pair with \(w_i>w_{i+1}\) can exist in the final row. Hence

\[
w_1<w_2<\cdots<w_n,
\]

so the cars are sorted in increasing order of width.

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A5: Correct (7/7)</summary>

Let \(L(a)\) and \(W(a)\) denote the length and width of car \(a\).

Call two cars \(a,b\) a **bad pair** if  
\[
L(a)<L(b)\quad\text{and}\quad W(a)>W(b).
\]
So \(a\) has smaller length but larger width than \(b\). Initially, because cars are lined up by increasing length, \(a\) is to the left of \(b\). But in a width-increasing final order, the smaller-width car \(b\) must be to the left of \(a\). Thus each bad pair must be swapped at least once.

A legal swap exchanges adjacent cars \(a,b\) with
\[
L(a)<L(b),\quad W(a)>W(b),
\]
i.e. exactly a bad pair. After swapping them, we have \(W(b)<W(a)\), so their width order is correct. Moreover, those two cars can never be swapped again: reversing their order would require swapping them in the order \(b,a\), but then we would need \(L(b)<L(a)\) and \(W(b)>W(a)\), which is false. Hence each bad pair can be swapped at most once. Since there are only finitely many pairs of cars, the procedure terminates.

Now we prove the final order is sorted by width. Suppose, for contradiction, that the widths are not increasing. Then there are adjacent cars \(x,y\) with
\[
W(x)>W(y).
\]
Consider their lengths.

- If \(L(x)<L(y)\), then \(\{x,y\}\) is a bad pair, and the left car \(x\) is shorter in length but wider than the right car \(y\). This is exactly a legal swap condition, so Adrian could still swap them, contradicting that no further moves are possible.

- If \(L(x)>L(y)\), then \(y\) has both smaller length and smaller width than \(x\). Such a compatible pair already has the correct relative order and can never be changed, so \(x\) before \(y\) is impossible.

Thus no adjacent pair with \(W(x)>W(y)\) can exist. Therefore the widths are strictly increasing from left to right.

\[
\boxed{\text{The procedure terminates, and the final order is increasing in width.}}
\]

</details>

<details><summary>A6: Partial (2/7)</summary>

Let \(l(C)\) and \(w(C)\) denote the length and width of car \(C\).

Consider the quantity

\[
N=\#\{(A,B): A \text{ is left of } B,\ l(A)<l(B),\ w(A)>w(B)\}.
\]

This counts pairs of cars that are “inverted” with respect to both the length order and the width order.

Initially \(N\) is finite, say \(N_0\).  
Now suppose Adrian swaps adjacent cars \(A,B\) with

\[
l(A)<l(B)\quad\text{and}\quad w(A)>w(B).
\]

Before the swap, this pair contributes \(1\) to \(N\). After the swap, \(B\) is left of \(A\), so this same unordered pair contributes \(0\) to \(N\).  
Because \(A\) and \(B\) are adjacent, every other car is either to the left of both or to the right of both, so the relative order of any other car with \(A\) or \(B\) is unchanged. Hence only the pair \(A,B\) changes its contribution to \(N\), and it decreases \(N\) by exactly \(1\).

Therefore every move reduces \(N\) by \(1\). Since \(N\ge 0\), the procedure can have at most \(N_0\) moves, so it terminates.

At termination \(N=0\). Thus there is no pair \(A,B\) with \(A\) left of \(B\), \(l(A)<l(B)\), and \(w(A)>w(B)\). Equivalently, whenever the smaller length is to the left of the larger length, the smaller width must also be to the left. For pairs with \(w(A)<w(B)\) and \(l(A)<l(B)\), their relative order was already correct and cannot be changed. Hence all cars are ordered by increasing width from left to right.

\[
\boxed{\text{The procedure terminates, and the cars are sorted by increasing width.}}
\]

</details>

<details><summary>A7: Partial (1/7)</summary>

Let us define a “bad pair” of cars as a pair \(\{A,B\}\) for which the car with larger width is to the left of the car with smaller width.  
Equivalently, if \(W_A<W_B\), then a pair is bad exactly when \(B\) is left of \(A\).

Consider one Adrian swap of adjacent cars \(X\) and \(Y\), with
\[
L_X<L_Y \quad\text{and}\quad W_X>W_Y.
\]
Thus \(X\) is the wider car and \(Y\) is the narrower car, and before the swap \(X\) is left of \(Y\). Hence \(\{X,Y\}\) is a bad pair.

After swapping, \(Y\) is left of \(X\), so this particular pair is no longer bad. Also, since \(X\) and \(Y\) are adjacent, any other car \(Z\) is either to the left of both or to the right of both. Therefore the relative order of \(Z\) with \(X\) and with \(Y\) is unchanged by the swap. Consequently, no other pair becomes or ceases to be bad.

So every move decreases the total number of bad pairs by exactly \(1\). There are only finitely many pairs of cars, so this cannot continue forever. Hence the procedure terminates.

At termination, there are no bad pairs: for any two cars \(A,B\) with \(W_A<W_B\), the smaller-width car \(A\) must lie to the left of the larger-width car \(B\). Therefore the cars, read from left to right, have their widths strictly increasing.

\[
\boxed{\text{The procedure terminates, and the final order is sorted by increasing width.}}
\]

</details>

<details><summary>A8: Correct (7/7)</summary>

Let the cars be numbered \(1,2,\dots,n\) so that car \(i\) has length \(i\).  
Let \(w_i\) denote the rank of car \(i\)'s width among all widths: \(w_i<w_j\) means car \(i\) is narrower than car \(j\). All \(w_i\) are distinct.

### 1. A useful invariant
For every pair \(i<j\) with \(w_i<w_j\), car \(i\) is always to the left of car \(j\).

Initially this is true, since cars are ordered by increasing length.  
A move swaps adjacent cars \(a,b\) with
\[
a<b,\qquad w_a>w_b.
\]
This swap changes only the relative order of \(a\) and \(b\); every other car is either to the left of both or to the right of both, so its order with \(a\) and \(b\) is unchanged. Hence the invariant is preserved.

### 2. Termination
Consider the discordant pairs
\[
a<b,\qquad w_a>w_b.
\]
Initially, for each such pair, car \(a\) is left of car \(b\).  
A move swaps exactly one such adjacent pair \(a,b\), and after the swap they become \(b,a\). No other pair’s relative order changes, so the number of discordant pairs still having car \(a\) before car \(b\) decreases by exactly \(1\). There are only finitely many pairs, so the process must terminate.

### 3. Final order
Suppose, for contradiction, that in the final row there are adjacent cars \(A,B\) with
\[
w_A>w_B.
\]
Since no move is possible, we cannot have \(L_A<L_B\); otherwise the move condition would be satisfied. Hence \(L_A>L_B\).

Let \(a\) be the shorter of \(A,B\) and \(b\) the taller one. Then \(a<b\) and \(w_a<w_b\), so by the invariant car \(a\) must appear before car \(b\). But in the adjacent pair \(A,B\), the taller car \(B=b\) is on the left and the shorter car \(A=a\) is on the right, i.e. \(b\) before \(a\), a contradiction.

Therefore no adjacent pair has decreasing width, so the widths strictly increase from left to right. Hence the cars are sorted in increasing order of width.

\[
\boxed{\text{The procedure terminates, and in the final row the widths are increasing.}}
\]

</details>

<details><summary>A9: Correct (7/7)</summary>

Let the cars be labeled by their increasing length: car \(i\) has length \(L_i\), with  
\[
L_1<L_2<\cdots<L_n,
\]
and let its width be \(W_i\).

We prove two facts simultaneously.

---

### 1. The procedure terminates

Call a pair of cars \(\{A,B\}\) bad if
\[
L_A<L_B \quad\text{and}\quad W_A>W_B.
\]
Let \(N\) be the number of unordered bad pairs \(\{A,B\}\) such that \(A\) is to the left of \(B\) in the current row.

Initially the cars are in increasing length order, so every bad pair appears in the correct left-right order. Hence
\[
0\le N\le \binom n2.
\]

Now consider a legal swap of adjacent cars \(A,B\) with
\[
L_A<L_B,\qquad W_A>W_B.
\]
Before the swap, \(\{A,B\}\) contributes \(1\) to \(N\). After the swap, \(B\) is left of \(A\), so that pair contributes \(0\).

For any third car \(C\), its position relative to both \(A\) and \(B\) is unchanged: if \(C\) was left of both, it is still left of both after the swap; if \(C\) was right of both, both are still left of \(C\). Thus the contributions involving \(C\) do not change.

Therefore every legal swap reduces \(N\) by exactly \(1\). Since \(N\) is a nonnegative integer bounded by \(\binom n2\), at most \(\binom n2\) swaps can occur. Hence the procedure terminates.

---

### 2. The final order is sorted by width

Let \(m\) be the car with minimum width:
\[
W_m<\min_{i\ne m}W_i.
\]

For any car \(j>m\), we have
\[
L_j>L_m,\qquad W_j>W_m.
\]
The two cars \(m\) and \(j\) can never be swapped: to swap them would require either
\[
L_m<L_j \quad\text{and}\quad W_m>W_j,
\]
which is false, or
\[
L_j<L_m,
\]
which is also false. Hence \(m\) always stays to the left of every car with larger length.

Thus, in the final stable row, all cars with larger length are to the right of \(m\). Therefore any car to the left of \(m\) must have smaller length, hence must be wider than \(m\).

But if \(m\) were not at the very left, the car immediately to its left would be wider than \(m\) and have smaller length, giving an allowed adjacent swap. This is impossible in a stable row. Hence \(m\) must be the first car.

Now remove \(m\). The remaining \(n-1\) cars initially form an increasing-length row:
\[
1,2,\ldots,m-1,m+1,\ldots,n.
\]
Moves involving \(m\) do not change the relative order of the remaining cars; they only temporarily move shorter cars across \(m\). Therefore the remaining cars evolve exactly like the original problem with \(n-1\) cars, starting from increasing length order.

By induction on \(n\), the remaining cars end sorted by width. Since \(m\) is first and has minimum width, the entire row is sorted by increasing width.

---

\[
\boxed{\text{The procedure terminates, and the final order is sorted by increasing width.}}
\]

</details>

<details><summary>A10: Partial (2/7)</summary>

\[
\boxed{\text{The procedure always terminates, and the final order is increasing in width.}}
\]

Let the cars be labelled \(1,2,\dots,n\) in increasing order of length. Thus car \(i\) is shorter than car \(j\) exactly when \(i<j\). Let \(w_i\) denote the rank of car \(i\) in width order: \(w_i<w_j\) means car \(i\) is narrower than car \(j\).

Define
\[
P=\#\{(i,j): i<j,\ w_i>w_j,\ \text{and car }i\text{ appears before car }j\}.
\]
So \(P\) counts pairs of cars that are “wrongly ordered” with respect to width: the shorter car is wider than the longer car, and the shorter car is to the left.

Initially, all cars are in increasing length order, so every pair \(i<j\) with \(w_i>w_j\) contributes to \(P\). Hence \(P\) is finite.

Now suppose Adrian swaps adjacent cars \(a,b\) with
\[
a<b,\qquad w_a>w_b.
\]
Before the swap, car \(a\) is immediately before car \(b\), so the pair \((a,b)\) is counted in \(P\). After the swap, car \(b\) is before car \(a\), so \((a,b)\) is no longer counted.

The swap changes only the relative order of these two cars; every other car is either to the left of both or to the right of both, so the relative order of every other car with \(a\) or \(b\) remains unchanged. Therefore the number of counted pairs decreases by exactly \(1\):
\[
P\longrightarrow P-1.
\]
Since \(P\) is a nonnegative integer, after at most its initial value many swaps the process must stop.

It remains to see what happens at termination. Suppose there is no possible swap. Then no adjacent cars \(x,y\) satisfy
\[
x<y,\qquad w_x>w_y.
\]
Equivalently, whenever two adjacent cars have increasing length, their widths must also be increasing. A standard adjacent-inversion argument then shows that this forces every pair \(i<j\) with \(w_i>w_j\) to appear with car \(j\) before car \(i\); otherwise there would be a forbidden adjacent pair and Adrian could swap them. Hence
\[
P=0.
\]
So for every pair \(i<j\) with \(w_i>w_j\), car \(j\) appears to the left of car \(i\). This is exactly the condition that the cars are sorted by increasing width.

Thus the procedure terminates, and in the final arrangement the cars are sorted in increasing order of width.

\[
\boxed{\text{Proved.}}
\]

</details>

<details><summary>A11: Almost (5/7)</summary>

\[
\boxed{\text{The procedure always terminates, and the final order is by increasing width.}}
\]

Label the cars by their initial increasing lengths: \(1,2,\dots,n\). Let \(\sigma(i)\) be the width rank of the car of length \(i\), so \(\sigma\) is a permutation of \(\{1,\dots,n\}\).

### 1. Termination

Consider the sequence
\[
S=(S_1,S_2,\dots,S_n),
\]
where \(S_j\) is the length label of the car in position \(j\). Initially,
\[
S=(1,2,\dots,n).
\]
A swap exchanges adjacent entries \(a<b\) with \(\sigma(a)>\sigma(b)\). For every car other than \(a,b\), their positions relative to both \(a\) and \(b\) do not change; only the relative order of \(a\) and \(b\) changes. Before the swap, \(a\) is before \(b\), so after the swap \(b\) is before \(a\). Hence the number of inversions of the length-label sequence increases by exactly \(1\).

Since there are at most \(\binom n2\) inversions, the process can have at most \(\binom n2\) moves. Therefore it terminates.

### 2. Final order by increasing width

Let \(m\) be the car of minimum width. For any car \(B\) with larger length than \(m\), their relative order is invariant: if they were adjacent, swapping them would require either \(w_m>w_B\) or \(l_B<l_m\), both false. Thus \(m\) remains to the left of every longer-length car. Initially it is already to the left of all longer-length cars, so finally \(m\) must be first.

Now remove \(m\). The remaining cars again have distinct widths, and the same argument applies to the car of second-smallest width: it must end up immediately after \(m\), then the car of third-smallest width immediately after it, and so on. Hence the final order is
\[
C_1,C_2,\dots,C_n,
\]
where \(C_k\) has the \(k\)-th smallest width. Therefore the cars are lined up in increasing order of width.

\[
\boxed{\text{Thus every possible sequence of swaps terminates, and the final order is by increasing width.}}
\]

</details>

<details><summary>A12: Partial (3/7)</summary>

Label the cars \(1,2,\dots,n\) in increasing order of length, so car \(i\) is shorter than car \(j\) exactly when \(i<j\). Let \(w_i\) denote the width rank of car \(i\), so \(w_i<w_j\) means car \(i\) is narrower than car \(j\).

Call a pair \((i,j)\) with \(i<j\) “bad” if  
\[
w_i>w_j \quad\text{and}\quad \text{car }i\text{ is to the left of car }j.
\]
Initially, for every \(i<j\) with \(w_i>w_j\), car \(i\) is certainly to the left of car \(j\), so the number \(B\) of bad pairs is finite, at most \(\binom n2\).

Now consider an allowed move: Adrian swaps adjacent cars \(a,b\) with
\[
a<b,\qquad w_a>w_b.
\]
This is exactly an adjacent bad pair \((a,b)\). Just before the swap, car \(a\) is left of car \(b\), so \((a,b)\) is bad; just after the swap, car \(b\) is left of car \(a\), so it is no longer bad. Since \(a,b\) are adjacent, every other car remains on the same side of both \(a\) and \(b\), so the relative order of \(a\) or \(b\) with any third car is unchanged. Hence only this pair changes status, and exactly one bad pair disappears.

Therefore each move decreases \(B\) by exactly \(1\). Since \(B\) is a nonnegative integer, the procedure cannot have more than \(B_0\) moves, where \(B_0=\#\{(i,j):i<j,\ w_i>w_j\}\). Thus it terminates.

If \(B>0\) at some point, a bad pair still exists, and the standard adjacent-pair argument shows that an adjacent bad pair must exist, so another allowed move is possible. Hence the procedure cannot stop while \(B>0\). Therefore it stops exactly when \(B=0\).

When \(B=0\), every pair \(i<j\) with \(w_i>w_j\) is corrected: car \(j\) is now to the left of car \(i\). For pairs \(i<j\) with \(w_i<w_j\), no swap involving them can occur, so their initial order remains correct. Thus for every pair of cars, the narrower one is left of the wider one. Consequently the cars are sorted by increasing width.

\[
\boxed{\text{The procedure terminates, and in the final order the cars are sorted by increasing width.}}
\]

</details>

<details><summary>A13: Correct (7/7)</summary>

Let \(L(c)\) and \(W(c)\) denote the length and width of car \(c\). All \(L(c)\) are distinct, and all \(W(c)\) are distinct.

## 1. Termination

Consider the sequence of widths from left to right. A move swaps two adjacent cars with

\[
W(\text{left})>W(\text{right}).
\]

So each move swaps an adjacent inverted pair in the width sequence. Swapping an adjacent inverted pair decreases the number of inversions of the width sequence by exactly \(1\): the swapped pair changes from inverted to non-inverted, and no other pair of cars changes its relative order because the two cars are adjacent.

Initially there are at most \(\binom n2\) inversions, so after at most \(\binom n2\) moves the number of inversions becomes \(0\). Hence the procedure terminates.

## 2. Final order

We now use a monotonicity fact.

**Claim.** If two cars \(p,q\) satisfy

\[
L(p)<L(q)\quad\text{and}\quad W(p)<W(q),
\]

then \(p\) remains to the left of \(q\) forever.

Initially this is true, because the cars are lined up in increasing order of length. A move swaps adjacent cars \(x,y\) satisfying

\[
L(x)<L(y)\quad\text{and}\quad W(x)>W(y).
\]

Thus the two cars swapped are “opposite” in both length and width, not “same” in both. In particular, the pair \(p,q\) above with both inequalities increasing is never directly swapped, so their relative order cannot change.

Now suppose, for contradiction, that the final arrangement is not sorted by width. Then there are adjacent cars \(a,b\) in the final row with

\[
W(a)>W(b).
\]

Since no move is possible, we cannot also have \(L(a)<L(b)\). Therefore

\[
L(a)>L(b).
\]

So \(a\) is longer and wider than \(b\). Equivalently,

\[
L(b)<L(a),\qquad W(b)<W(a),
\]

which means \(b\) and \(a\) are of the same type: \(b\) has both smaller length and smaller width than \(a\). By the claim, \(b\) must always be to the left of \(a\). But in the final adjacent pair \(a,b\), we have \(a\) to the left of \(b\), a contradiction.

Therefore no adjacent pair in the final arrangement can have \(W(\text{left})>W(\text{right})\). Hence the widths strictly increase from left to right.

\[
\boxed{\text{The procedure always terminates, and the final order is increasing by width.}}
\]

</details>

<details><summary>A14: Correct (7/7)</summary>

Let \(L(c)\) and \(W(c)\) denote the length rank and width rank of a car \(c\), chosen so that smaller ranks mean shorter widths/lengths.

Define a relation on cars:
\[
c\prec d \quad \Longleftrightarrow \quad L(c)<L(d)\ \text{and}\ W(c)<W(d).
\]
This is a strict partial order.

Initially the cars are in increasing length order, so every pair \(c\prec d\) has \(L(c)<L(d)\), hence \(c\) appears to the left of \(d\). Thus the initial row is a linear extension of \(\prec\).

Now consider any allowed swap: adjacent cars \(x,y\) with
\[
L(x)<L(y)\quad\text{and}\quad W(x)>W(y).
\]
These two cars are incomparable in \(\prec\): we cannot have \(x\prec y\) because \(W(x)>W(y)\), and we cannot have \(y\prec x\) because \(L(y)>L(x)\). Swapping adjacent incomparable elements in a linear extension preserves the linear-extension property. Hence after every allowed swap the row remains a linear extension of \(\prec\).

Now suppose the final row were not sorted by width. Then there would be adjacent cars \(x,y\) with \(W(x)>W(y)\). Since the row is a linear extension of \(\prec\), it cannot be the case that \(y\prec x\), i.e. cannot have \(L(y)<L(x)\). Therefore \(L(x)<L(y)\). But then \(x\) is shorter in length and wider in width than \(y\), so \(x,y\) would be a legal swap. This contradicts that no further moves are possible.

Thus the final row must have no adjacent width-descents, meaning the widths increase left to right.

Finally, termination is clear from the inversion count: each swap exchanges adjacent entries \(u>v\) in the width-rank sequence, decreasing the inversion count by exactly \(1\). Since there are only finitely many permutations, the process terminates.

Therefore, no matter how Adrian chooses his swaps, the procedure terminates, and the cars end up sorted in increasing order of width.

\[
\boxed{\text{The final order is }W(1),W(2),\dots,W(n).}
\]

</details>

<details><summary>A15: Partial (4/7)</summary>

\[
\boxed{\text{No matter how Adrian chooses the swaps, the procedure terminates, and the final order is increasing in width.}}
\]

Proof.

Label the cars \(1,2,\dots,n\) in increasing order of length, so car \(i\) has length \(i\). Let \(A\) be the car of minimum width, and let its length be \(r\).

### 1. The minimum-width car eventually reaches the front

No car of length \(>r\) can ever pass \(A\) to its left: initially every car of length \(>r\) is to the right of \(A\), and to swap \(A\) with such a car \(X\) would require either

\[
L_A<L_X,\quad W_A>W_X,
\]

which is false because \(W_A<W_X\), or

\[
L_X<L_A,\quad W_X>W_A,
\]

which is false because \(L_X>L_A\). Hence larger-length cars stay to the right of \(A\).

Therefore, until \(A\) is at the first position, every car immediately to its left has length \(<r\). For such a car \(B\),

\[
L_B<L_A,\qquad W_B>W_A,
\]

so the adjacent pair \((B,A)\) is exactly the kind of pair Adrian may swap. Swapping \(B,A\) moves \(A\) one step left. Repeating this, \(A\) can move left through all cars of length \(<r\), so after at most \(r-1\le n-1\) moves \(A\) reaches the first position.

### 2. Termination

Each allowed swap exchanges adjacent cars \(X,Y\) with

\[
L_X<L_Y.
\]

This increases the number of pairs \((X,Y)\) with \(L_X<L_Y\) but with \(Y\) before \(X\) by exactly \(1\). There are only \(\binom n2\) such pairs, so the number of swaps is finite. Hence the whole procedure terminates.

### 3. Final order is by increasing width

Once \(A\) has reached the first position, it can never move again: as the left car, \(A\) would need to be wider than the right car, but \(A\) has minimum width.

The relative order of the remaining \(n-1\) cars is unchanged while \(A\) moves, because \(A\) only swaps with smaller-length cars. Thus the remaining cars are still ordered by increasing length. Applying the same argument recursively to the remaining cars shows that they are sorted by increasing width.

Since \(A\) has the smallest width and is placed first, the whole row is sorted by increasing width.

\[
\boxed{\text{Thus the procedure terminates, and the final order is increasing in width.}}
\]

</details>

<details><summary>A16: Partial (1/7)</summary>

Let the cars be labeled \(1,2,\dots,n\) in increasing order of length, so car \(i\) has length \(i\).  
Write the widths of the cars as \(w_1,w_2,\dots,w_n\), where the labels are now just their length ranks.

Consider the sequence of widths read from left to right:

\[
w_{a_1},w_{a_2},\dots,w_{a_n}.
\]

Call a pair of cars \(X,Y\) an **inversion** if \(X\) is to the left of \(Y\) but \(w_X>w_Y\). Equivalently, this is an adjacent inversion in the width sequence.

Initially there are finitely many such inversions; let their number be \(I\).

Now look at one allowed swap: adjacent cars \(A,B\) with \(w_A>w_B\).  
In the width sequence, \(w_A>w_B\) is a descent, so \(A,B\) form an inversion. After swapping them, \(B\) is to the left of \(A\), so that particular pair no longer is an inversion. For every other pair, their relative order in the row does not change, so no new inversion is created.

Thus every swap decreases the number \(I\) of inversions by exactly \(1\). Since \(I\) is a nonnegative integer, the process can continue only finitely many times. Hence it terminates.

At termination there can be no adjacent pair with larger width on the left and smaller width on the right. Therefore the width sequence is strictly increasing from left to right; otherwise an adjacent inversion would remain, contradicting the fact that the process has no possible moves.

Hence, in the end, the cars are lined up in increasing order of width.

\[
\boxed{\text{The procedure terminates, and the final order is by increasing width.}}
\]

</details>
