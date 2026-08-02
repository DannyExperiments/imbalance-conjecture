# A proof of the Imbalance Conjecture

Date: 2026-08-01  
Problem ID: `OPG-57613`

This is the corrected, self-contained presentation audited after the focused
post-Round-3 return.  It makes the empty-graph case explicit and consistently
uses “higher-degree endpoint” for the endpoint from which an edge is oriented.

## Theorem

Let (G) be a finite simple graph such that adjacent vertices have unequal
degrees.  Then the multiset

\[
\bigl\{|d_G(u)-d_G(v)|:uv\in E(G)\bigr\}
\]

is the degree multiset of a finite simple graph.

More strongly, if its elements are arranged as

\[
x_1\ge x_2\ge\cdots\ge x_m>0,
\]

then, for every (k\ge2), the condition (x_k\ge k) implies the (k)-th
Erdős--Gallai inequality.

## Proof

If (m=0), the empty sequence is graphic.  Assume (m>0).  Orient every edge
from its higher-degree endpoint to its lower-degree endpoint, and write

\[
w(uv)=|d_G(u)-d_G(v)|>0.
\]

The total weight is even, because modulo (2),

\[
\sum_{uv\in E(G)}|d(u)-d(v)|
\equiv \sum_{uv\in E(G)}(d(u)+d(v))
=\sum_v d(v)^2
\equiv\sum_vd(v)=2m\equiv0.
\]

Also (x_1\le m-1): if (u\to v), then

\[
w(uv)=d(u)-d(v)\le d(u)-1\le m-1.
\]

For (1\le j\le m), define the Erdős--Gallai deficit

\[
\Delta_j=j(j-1)+\sum_{i>j}\min(j,x_i)-\sum_{i\le j}x_i.
\]

Thus (Delta_1\ge0).  If some Erdős--Gallai inequality failed, let (k\ge2)
be the first failed index.  Necessarily

\[
x_k\ge k. \tag{1}
\]

Indeed, if (x_k\le k-1), then every (x_i) with (i\ge k) is at most
(k-1), and direct subtraction gives

\[
\Delta_k-\Delta_{k-1}=2(k-1-x_k)\ge0,
\]

contrary to (Delta_{k-1}\ge0>\Delta_k).

It therefore suffices to prove that (Delta_k\ge0) whenever (x_k\ge k).
Fix such a (k), and choose any set (S) of (k) edges of largest weight.
Every edge of (S) has weight at least (k).

For each vertex (v), let

\[
s_v=|\{v\to z\in S\}|,
\qquad
\ell_v=|\{z\to v\in S\}|.
\]

Put

\[
U=\{v:s_v>0\},\qquad h=|U|,
\]

and, for an edge (f=xy), put (p_f=s_x+s_y).  Finally define

\[
B=\sum_v\ell_v(d(v)-1)\ge0.
\]

### 1. Exact deficit identity

We claim

\[
\boxed{
\Delta_k=B+\sum_{f\in E(G)}\bigl(\min(k,w(f))-p_f\bigr).
} \tag{2}
\]

Since the (k) selected edges have truncated weight (k),

\[
\Delta_k=\sum_f\min(k,w(f))-k-\sum_{e\in S}w(e).
\]

Moreover,

\[
\sum_fp_f=\sum_vs_vd(v),
\]

while orientation gives

\[
\sum_{e\in S}w(e)
=\sum_vs_vd(v)-\sum_v\ell_vd(v),
\qquad
\sum_v\ell_v=k.
\]

Substituting these identities proves (2).

### 2. The head-side reserve

For the selected edges put

\[
P=\sum_{e\in S}(k-p_e)\ge0.
\]

Consider a selected oriented edge (u\to v), so (u) is its higher-degree
endpoint.  If (v\notin U), its contribution to (P) is (k-s_u).  If
(v\in U), then (v) is itself the higher-degree endpoint of a selected edge
of weight at least (k), and therefore (d(v)\ge k+1).  The copy
(d(v)-1\) of (B) associated with the selected edge entering (v), together
with that edge's (P)-term, is at least

\[
k+(k-s_u-s_v)\ge k-s_u.
\]

Summing over the selected edges yields

\[
B+P\ge\sum_{u\in U}s_u(k-s_u)
=2\sum_{\{u,v\}\subset U}s_us_v. \tag{3}
\]

An unselected edge joining (u,v\in U) has contribution

\[
\min(k,w)-s_u-s_v\ge-(s_u+s_v-1),
\]

because every physical edge has positive weight.  Simplicity permits at most
one such edge for each unordered pair.  After every possible negative
unselected (U)-(U) edge is paid, the reserve left by (3) is

\[
\boxed{
\Psi(s)=\sum_{\{u,v\}\subset U}
\bigl(2s_us_v-s_u-s_v+1\bigr).
} \tag{4}
\]

Let (H=G-U).  For (z\in V(H)), define

\[
q_z=\sum_{u\in N_G(z)\cap U}
\bigl(s_u-|d_G(u)-d_G(z)|\bigr)_+,
\qquad
Q=\sum_zq_z,
\]

and put

\[
TV_k(H)=\sum_{xy\in E(H)}\min\{k,|d_G(x)-d_G(y)|\}.
\]

Every unselected (U)-(H) edge (uz) contributes at least the negative of
its corresponding demand.  A selected (U)-(H) edge has weight at least
(k\ge s_u) and hence has no demand.  Every (H)-edge contributes its full
truncated weight.  Splitting (2) by edge type therefore gives

\[
\boxed{
\Delta_k\ge TV_k(H)-Q+\Psi(s).
} \tag{5}
\]

### 3. A weighted global bound on the residual shortfall

For (u\in U), put

\[
e_u=s_u-1,
\qquad
p=k-h=\sum_{u\in U}e_u.
\]

Define

\[
q_{u,z}=(s_u-|d_G(u)-d_G(z)|)_+
\]

and

\[
A_u=\{z\in V(H):uz\in E(G),\ q_{u,z}>0\},
\qquad
Q_u=\sum_{z\in A_u}q_{u,z}.
\]

Let (W_u) be the total truncated weight of the (H)-edges incident with
(A_u), with each edge counted once:

\[
W_u=\sum_{\substack{xy\in E(H)\\\{x,y\}\cap A_u\ne\varnothing}}
\min\{k,|d_G(x)-d_G(y)|\}.
\]

If (e_u=0), then (A_u=\varnothing).  Suppose (e_u>0).  Since (u)
is the higher-degree endpoint of a selected edge of weight at least (k),
write

\[
d_G(u)=k+1+a_u,\qquad a_u\ge0. \tag{6}
\]

Every active edge (uz) has weight strictly less than
(s_u=e_u+1\le k), and hence is not selected.  With (n_u=|A_u|),

\[
n_u\le d_G(u)-s_u=k-e_u+a_u. \tag{7}
\]

For (z\in A_u), set (j=|d_G(u)-d_G(z)|).  Then

\[
1\le j\le e_u,
\qquad
q_{u,z}=e_u+1-j.
\]

Deleting the (h) vertices of (U) removes at most (h) edges incident
with (z).  If (d_G(z)=d_G(u)-j), then

\[
d_H(z)\ge d_G(u)-j-h
=q_{u,z}+p-e_u+a_u. \tag{8}
\]

If (d_G(z)=d_G(u)+j), the lower bound is larger by (2j).

Let (E_1(A_u)) denote the number of (H)-edges of imbalance one with both
endpoints in (A_u).  The sum of the (H)-degrees over (A_u) counts a
boundary edge once and an internal edge twice; (W_u) counts either edge
once with truncated weight at least one.  The only possible loss is one unit
for an internal edge of weight one.  Hence

\[
W_u\ge\sum_{z\in A_u}d_H(z)-E_1(A_u). \tag{9}
\]

The unit-edge graph induced by (A_u) is bipartite under the coloring
(z\mapsto d_G(z)\pmod2).  Consequently,

\[
E_1(A_u)\le\left\lfloor\frac{n_u^2}{4}\right\rfloor. \tag{10}
\]

Equations (8)--(10), together with

\[
Q_u=e_un_u-\sum_{z\in A_u}(e_u-q_{u,z}),
\]

give

\[
\begin{aligned}
pQ_u-e_uW_u
&\le e_uE_1(A_u)-e_ua_un_u
 -(p-e_u)\sum_{z\in A_u}(e_u-q_{u,z})\\
&\le e_u\left(\left\lfloor\frac{n_u^2}{4}\right\rfloor-a_un_u\right).
\end{aligned} \tag{11}
\]

Here (p-e_u\ge0), because (p=\sum_ve_v).

Set (R=k-e_u).  By (7), (0\le n_u\le R+a_u).  The function

\[
f(n)=\frac{n^2}{4}-a_un
\]

is convex, so its maximum on this interval occurs at an endpoint.  At the
nonzero endpoint,

\[
f(R+a_u)=\frac{(R+a_u)(R-3a_u)}4\le\frac{R^2}{4}.
\]

It follows that, also for (e_u=0),

\[
\boxed{
pQ_u-e_uW_u\le\frac{e_u}{4}(k-e_u)^2.
} \tag{12}
\]

Now sum over (u\).  We have (Q=\sum_uQ_u).  Each (H)-edge is counted in
(\sum_ue_uW_u) with coefficient at most
(sum_ue_u=p), even if it is incident with several active regions.  Hence

\[
\sum_ue_uW_u\le p\,TV_k(H).
\]

For (p>0), summing (12) therefore yields

\[
\boxed{
p\bigl(Q-TV_k(H)\bigr)
\le\frac14\sum_{u\in U}e_u(k-e_u)^2.
} \tag{13}
\]

### 4. The reserve dominates the residual collision bound

Assume (h\ge2) and (p>0).  Put

\[
S_2=\sum_ue_u^2,
\qquad
S_3=\sum_ue_u^3,
\qquad
k=p+h.
\]

Since (s_u=e_u+1), equation (4) gives

\[
\Psi=p^2-S_2+(h-1)p+\binom h2. \tag{14}
\]

Let

\[
C=\sum_ue_u(k-e_u)^2
=k^2p-2kS_2+S_3. \tag{15}
\]

Direct expansion yields

\[
\begin{aligned}
4p\Psi-C={}&3p^3+(2h-4)p^2+h(h-2)p\\
&+(2h-2p)S_2-S_3. 
\end{aligned} \tag{16}
\]

Because (0\le e_u\le p),

\[
S_3\le pS_2.
\]

Thus (16) is at least

\[
B_0+(2h-3p)S_2,
\]

where

\[
B_0=p\bigl(3p^2+(2h-4)p+h(h-2)\bigr)>0. \tag{17}
\]

If (2h\ge3p), this is positive.  If (2h<3p), use (S_2\le p^2), with
the inequality direction reversed by the negative coefficient, to obtain

\[
B_0+(2h-3p)S_2
\ge p\bigl(4(h-1)p+h(h-2)\bigr)>0.
\]

Therefore

\[
\boxed{
\Psi>\frac1{4p}\sum_ue_u(k-e_u)^2.
} \tag{18}
\]

Combining (5), (13), and (18) gives

\[
\Delta_k
\ge TV_k(H)-Q+\Psi
\ge-\frac{C}{4p}+\Psi
>0.
\]

It remains to dispose of the two boundary head profiles.

If (p=0), then (h=k), every (s_u=1), and (Q=0), because all physical
edge weights are positive.  Also (Psi=\binom{k}{2}), so (5) gives

\[
\Delta_k\ge TV_k(H)+\binom{k}{2}\ge0.
\]

If (h=1), then (p=e_u=k-1>0).  In (13),

\[
\sum_ue_u(k-e_u)^2=p.
\]

Consequently (Q-TV_k(H)\le1/4).  Both quantities are integers, so
(Q\le TV_k(H)), and (5) again gives (Delta_k\ge0).

Thus the (k)-th Erdős--Gallai inequality holds whenever (x_k\ge k).
But every first failed index would have this property by (1), a contradiction.
All Erdős--Gallai inequalities hold; the total sum is even; hence the
Erdős--Gallai theorem shows that the imbalance multiset is graphic.  This
proves the theorem.  □

## Scope note

The unconditional residual inequality (TV_k(H)\ge Q) is not used and is
false.  The proof succeeds because the discarded reserve (Psi(s)), together
with the weighted collision estimate (13), pays the possible residual
shortfall.
