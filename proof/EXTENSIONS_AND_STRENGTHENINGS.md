# Further consequences of the Imbalance Conjecture proof

**Date:** 2026-08-01

This note assumes the notation and inequalities (2), (5), (13), and (16) from
`IMBALANCE_CONJECTURE_PROOF_2026-08-01.md`.

Let `G` be a finite simple locally irregular graph and put

\[
w(e)=|d_G(u)-d_G(v)|>0\qquad(e=uv\in E(G)).
\]

For an arbitrary edge set `S subseteq E(G)` of size `k`, define its subset
Erdős--Gallai deficit by

\[
D_G(S)=k(k-1)+\sum_{f\notin S}\min\{k,w(f)\}-\sum_{e\in S}w(e).
\tag{T}
\]

If `S` consists of the top `k` imbalances, then `D_G(S)` is the usual sorted
Erdős--Gallai deficit `Delta_k`.

## 0. Threshold-set theorem: a stronger form of the proof

### Theorem 0

For every `S subseteq E(G)` with `|S|=k>=1`, if

\[
w(e)\ge k\qquad\text{for every }e\in S,
\]

then

\[
\boxed{D_G(S)\ge0.}
\tag{TS}
\]

For `k>=2`, this is exactly what the main proof establishes. The word “top”
is used there only to guarantee that each selected edge has weight at least
`k`. Once that threshold condition holds, every later step remains valid:

- selected edges have truncated weight `k`;
- an active edge has `w<s_u<=k`, hence cannot be selected;
- all reserve, residual, parity, and multiplicity estimates depend only on
  the selected set and the threshold `w(e)>=k`, not on how its elements rank
  among the unselected edges.

For `k=1`, all unselected edges contribute one because `G` is locally
irregular, and

\[
D_G(\{e\})=|E(G)|-1-w(e)\ge0,
\]

since `w(e)<=|E(G)|-1`.

The sorted top-threshold theorem follows by taking `S` to be any top-`k` set.
The Imbalance Conjecture then follows from the standard first-failure fact:
if the first failed sorted Erdős--Gallai index were `k`, then `x_k>=k`.

## 1. Quantitative critical slack

Fix `k>=2`, a threshold set `S` as in Theorem 0, and orient every edge from
higher degree to lower degree. Let `s_u` be the number of selected edges
headed at `u`, and put

\[
U=\{u:s_u>0\},\qquad h=|U|,\qquad e_u=s_u-1,
\qquad p=k-h=\sum_ue_u.
\]

### Theorem 1

For every such threshold set `S`:

1. If `h=k`, then
   \[
   D_G(S)\ge \binom{k}{2}.
   \]
2. If `2<=h<k`, then
   \[
   D_G(S)\ge1.
   \]
   More precisely, with `p=k-h`,
   \[
   D_G(S)\ge
   \begin{cases}
   \left\lceil\dfrac{3p^2+(2h-4)p+h(h-2)}4\right\rceil,
       &2h\ge3p,\\[8pt]
   \left\lceil (h-1)p+\dfrac{h(h-2)}4\right\rceil,
       &2h<3p.
   \end{cases}
   \tag{PB}
   \]
3. If `h=1`, with unique head `u`, then
   \[
   D_G(S)=B+TV_k(G-u)-Q\ge B,
   \]
   where
   \[
   B=\sum_v\ell_v(d_G(v)-1)
   \]
   is the selected low-end contribution from the main proof.

### Proof

If `h=k`, then `p=0`, every `s_u=1`, all residual demands vanish, and the
head reserve is `Psi=binom(k,2)`. Inequality (5) gives the first claim.

Assume `2<=h<k`, so `p>0`. Let

\[
C=\sum_ue_u(k-e_u)^2.
\]

The main proof gives

\[
D_G(S)\ge \Psi-\frac{C}{4p}.
\]

With `S_2=sum e_u^2` and `S_3=sum e_u^3`, equation (16) and
`S_3<=pS_2` give

\[
4p\Psi-C\ge
p\bigl(3p^2+(2h-4)p+h(h-2)\bigr)+(2h-3p)S_2.
\tag{A}
\]

If `2h>=3p`, discard the nonnegative final term in (A) and divide by `4p`.
If `2h<3p`, use `S_2<=p^2` in the negative-coefficient term to obtain

\[
4p\Psi-C\ge
p\bigl(4(h-1)p+h(h-2)\bigr).
\]

This proves (PB). In particular, the right side is always at least one. A
convenient integral sharpening is

\[
\boxed{4p\Psi-C\ge4p.}
\tag{B}
\]

For `h>=3` this follows immediately from the displayed bounds. For `h=2`,
the case `2h>=3p` forces `p=1`; the only profile is
`(e_1,e_2)=(1,0)`, and direct substitution gives
`4pPsi-C=4=4p`.

If `h=1`, write `U={u}`. Every selected edge is headed at `u`, so every
selected term in the exact deficit identity (2) is zero. Every unselected
edge incident with `u` contributes exactly the negative of its residual
demand, and every edge in `G-u` contributes its truncated imbalance.
Therefore

\[
D_G(S)=B+TV_k(G-u)-Q.
\]

The single-head boundary argument in the main proof gives `Q<=TV_k(G-u)`,
so `D_G(S)>=B`.

## 2. Complete classification of threshold equality

### Theorem 2

Let `S subseteq E(G)`, `|S|=k>=2`, and suppose every edge in `S` has
imbalance at least `k`. Then `D_G(S)=0` if and only if, after deleting
isolated vertices, one of the following holds:

1. `G=K_{1,t}` for some `t>=k+1`; in this case any `k` edges may form `S`;
2. `G` is obtained from `K_{1,k+1}` by subdividing exactly one edge once,
   and `S` is the set of the `k` unsubdivided leaf edges incident with the
   degree-`k+1` center.

For `k=1`, equality in (TS) holds if and only if, after deleting isolates,
`G` is a star.

### Proof for `k>=2`

Assume `D_G(S)=0`. Theorem 1 excludes every head profile except `h=1`.
Let `u` be the unique selected head. The exact single-head identity gives

\[
0=D_G(S)=B+TV_k(G-u)-Q,
\qquad Q\le TV_k(G-u).
\]

Hence `B=0` and `TV_k(G-u)=Q`. Since `B=0`, every selected low endpoint is
a leaf.

Write

\[
d_G(u)=k+1+a,\qquad a\ge0,
\]

and let

\[
A=\{z\in N_G(u): |d_G(u)-d_G(z)|<k\}
\]

be the active residual set. Put `n=|A|`. The proof's single-head estimate
has the exact form

\[
(k-1)(Q-W)\le(k-1)
\left(\left\lfloor\frac{n^2}{4}\right\rfloor-an\right),
\tag{C}
\]

where `W` is the total truncated imbalance of edges of `G-u` incident with
`A`, and `W<=TV_k(G-u)`. Also `n<=a+1`.

If `a>=1` and `n>0`, then

\[
\left\lfloor\frac{n^2}{4}\right\rfloor<an,
\]

because `1<=n<=a+1<4a`. Thus (C) gives
`Q<W<=TV_k(G-u)`, contradicting `Q=TV_k(G-u)`. Therefore `A` is empty.
It follows that `Q=0` and `TV_k(G-u)=0`. Every edge of `G-u` would have
positive imbalance, so `G-u` is edgeless. The only nontrivial component of
`G` is therefore a star.

Now suppose `a=0`. Then `d_G(u)=k+1` and `n<=1`. If `n=0`, the same
argument gives a star `K_{1,k+1}`. If `n=1`, write `A={z}`. Equality through

\[
TV_k(G-u)\ge W\ge d_{G-u}(z)\ge q_z=Q
\]

forces all four quantities to be equal. Consequently:

- `d_G(z)<d_G(u)`;
- every edge of `G-u` is incident with `z`;
- every such edge has imbalance one.

The `k` selected neighbors of `u` are leaves and, since `d_G(u)=k+1`, the
only remaining neighbor of `u` is `z`. Every neighbor of `z` in `G-u` has
no other incident edge and hence degree one in `G`. An imbalance-one edge
from `z` to a degree-one vertex forces `d_G(z)=2`; therefore there is exactly
one such vertex. This is precisely the once-subdivided star in case 2.

Conversely, for `K_{1,t}` every edge has imbalance `t-1`, and direct
substitution gives `D_G(S)=0` for every `k<=t-1` and every `k`-edge set `S`.
In the subdivided-star case the imbalance sequence is

\[
k^k,\quad k-1,\quad1,
\]

and the only `k` edges satisfying the threshold are the `k` direct leaf
edges; direct substitution gives `D_G(S)=0`.

For `k=1`, equality says `w(e)=|E(G)|-1`. If `e=uv` is oriented from `u` to
`v`, then `d(u)-d(v)=|E(G)|-1`, while `d(u)<=|E(G)|` and `d(v)>=1`. Hence
`d(u)=|E(G)|`, so every edge is incident with `u`; deleting isolates leaves
a star. The converse is immediate.

### Corollary 2.1: uniqueness of the critical realization

The graphical sequences arising in the two `k>=2` equality cases have unique
simple realizations up to isomorphism:

- `(t-1)^t` is realized uniquely by `K_t`;
- `k^k,k-1,1` is realized uniquely by a `K_k` together with two independent
  vertices whose neighborhoods partition the clique into sets of sizes
  `k-1` and `1`.

For the second sequence, equality in its `k`th Erdős--Gallai inequality
forces the top `k` vertices to form a clique and the two tail vertices to be
independent with all their incident edges entering that clique. Their degree
sum is `k`, so those neighborhoods partition the clique; this determines the
graph up to isomorphism.

## 3. Edge-to-vertex realization and subset inequalities

The theorem can be stated in a labeled form. There exists a simple graph
`F` whose vertex set is `E(G)` such that

\[
d_F(e)=|d_G(u)-d_G(v)|\qquad(e=uv\in E(G)).
\]

Thus `|V(F)|=|E(G)|` and

\[
|E(F)|=\frac12\sum_{uv\in E(G)}|d_G(u)-d_G(v)|.
\]

For every edge subset `A subseteq E(G)`, `|A|=r`, the degree-sum bound in
`F` yields

\[
\sum_{e\in A}|d_G(u_e)-d_G(v_e)|
\le r(r-1)+
\sum_{f\in E(G)\setminus A}\min\{r,|d_G(u_f)-d_G(v_f)|\}.
\]

This is the full labeled Erdős--Gallai family, not only the inequalities for
an arbitrarily chosen ordering. Theorem 0 proves the potentially dangerous
part of this family directly, before invoking graphicality.

Equivalently, the imbalance vector is a feasible integral `b`-factor demand
on the complete graph whose vertices are the edges of `G`.

## 4. Incidence-matrix formulation

Orient every edge from higher degree to lower degree, let `D` be the
vertex-edge incidence matrix, and let `d` be the vertex-degree vector. The
imbalance vector is `|D^T d|`. The theorem is equivalent to the existence of
a symmetric zero-one matrix `A` with zero diagonal such that

\[
A\mathbf 1=|D^T d|.
\]

So the absolute discrete gradient of the degree signal on a locally
irregular graph is itself a simple-graph degree vector on the edge set.
Equivalently, it is a sum of distinct vectors `e_i+e_j`, one for each edge of
the realizing graph.

## 5. Algorithmic consequence

The proof gives a polynomial-time certificate. Compute the edge imbalances,
order them, and run Havel--Hakimi (or a simple-graph `b`-matching algorithm)
on vertices labeled by `E(G)`. The theorem guarantees success. The output is
an explicit graph `F` on the edge set of `G`, and ordinary degree checking is
a linear-time certificate once `F` is supplied.

## 6. Transfer of degree-sequence inequalities

Every universal inequality for degree sequences of simple graphs transfers
to edge imbalances. For example, let

\[
m=|E(G)|,\qquad
I(G)=\sum_{uv\in E(G)}|d_G(u)-d_G(v)|,
\]

and

\[
\Sigma(G)=\sum_{uv\in E(G)}(d_G(u)-d_G(v))^2.
\]

Applying de Caen's bound to the realization `F` on `m` vertices and
`I(G)/2` edges gives, for `m>=2`,

\[
\boxed{
\Sigma(G)\le
\frac{I(G)}2\left(\frac{I(G)}{m-1}+m-2\right).
}
\]

No claim of literature novelty for this transferred inequality is made here;
it is an immediate consequence once the imbalance sequence is known to be
graphical. More generally, every extremal, moment, majorization, and
forcibility theorem stated solely in terms of a simple graph's degree
sequence can be applied to the imbalance vector through `F`.

## 7. Locally irregular decompositions

If an arbitrary graph is edge-decomposed into locally irregular subgraphs
`G_1,...,G_r`, with degrees computed inside each color class, then the union
of all classwise imbalance multisets is graphical: realize each classwise
multiset separately and take the disjoint union of the realizations. This is
a direct bridge to locally irregular edge-coloring, though it does not by
itself bound the locally irregular chromatic index.

## 8. What is not implied

The theorem does not settle conjectures about arbitrary block graphs,
bicyclic graphs, or line graphs when zero-imbalance edges are allowed. A zero
in a graphical degree sequence is forced to be an isolated target vertex, so
zero imbalances cannot simply be ignored or used as extra capacity. The
realizing graph `F` is existential/algorithmic; it is not claimed to be a
subgraph of the line graph of `G`, connected, bipartite, locally irregular,
or unique outside the two critical equality families.

## 9. Robustness beyond local irregularity: one zero imbalance is allowed

The proof can be extended to graphs that are not locally irregular, provided
one keeps explicit correction terms for equal-degree edges.

Let `G` now be an arbitrary finite simple graph. Fix a threshold set
`S subseteq E(G)`, `|S|=k>=2`, with `w(e)>=k` for every `e in S`. Orient the
selected edges from higher degree to lower degree and define `U,H,h,p,e_u`,
`B,Q,TV_k(H),Psi`, and `C=sum e_u(k-e_u)^2` as before. Let

\[
Z_{UU}=|\{xy\in E(G[U]):d_G(x)=d_G(y)\}|,
\]

\[
Z_{UH}=|\{xy\in E_G(U,H):d_G(x)=d_G(y)\}|,
\]

and

\[
Z_H=|\{xy\in E(H):d_G(x)=d_G(y)\}|.
\]

### Lemma 3: zero-edge correction

The subset deficit satisfies:

1. If `h=k`, then
   \[
   D_G(S)\ge \binom{k}{2}-Z_{UU}-Z_{UH}. \tag{Z1}
   \]
2. If `2<=h<k`, then
   \[
   D_G(S)\ge L(h,p)-Z_{UU}-Z_{UH}-2Z_H, \tag{Z2}
   \]
   where `L(h,p)` is the integer profile bound in (PB).
3. If `h=1`, then
   \[
   D_G(S)\ge B-2Z_H. \tag{Z3}
   \]

### Proof

The exact deficit identity (2) is unchanged. In the head reserve, an
unselected positive-imbalance edge between two heads costs at most
`s_u+s_v-1`, while a zero-imbalance edge costs `s_u+s_v`. Therefore the
head-side reduction becomes

\[
D_G(S)\ge TV_k(H)-Q+\Psi-Z_{UU}. \tag{Z4}
\]

For a repeated head `u`, retain the active set `A_u` and put

\[
t_u=|\{z\in A_u:w(uz)=0\}|,
\]

\[
\zeta_u=
\sum_{xy\in E(H),\,w(xy)=0}|\{x,y\}\cap A_u|.
\]

A zero residual edge contributes no weight to `W_u`; consequently the
modified incidence count is

\[
W_u\ge
\sum_{z\in A_u}d_H(z)-E_1(A_u)-\zeta_u. \tag{Z5}
\]

For a positive active edge, `q_{u,z}<=e_u`, exactly as before. A zero
`U`--`H` edge has `q_{u,z}=e_u+1`; hence

\[
Q_u-e_un_u\le t_u. \tag{Z6}
\]

Combining (Z5), (Z6), the same degree estimate, and the parity/Mantel bound
gives

\[
pQ_u-e_uW_u
\le
\frac{e_u}{4}(k-e_u)^2+e_u\zeta_u+(p-e_u)t_u. \tag{Z7}
\]

On summing over `u`, each zero edge of `H` contributes at most `2p` to
`sum e_u zeta_u`, and each zero `U`--`H` edge contributes at most `p` to
`sum (p-e_u)t_u`. As before, `sum e_uW_u<=pTV_k(H)`. Thus, when `p>0`,

\[
p(Q-TV_k(H))
\le
\frac C4+2pZ_H+pZ_{UH}. \tag{Z8}
\]

Combining (Z4), (Z8), and (PB) proves (Z2).

If `p=0`, then every `s_u=1`; the only residual demands are the zero
`U`--`H` edges. Hence `Q=Z_{UH}`, and (Z1) follows from (Z4).

If `h=1`, write `U={u}`, `e_u=p=k-1`, and `d_G(u)=k+1+a`. Equation (Z7)
reduces more sharply to

\[
Q-W_u\le E_1(A_u)+\zeta_u-an_u.
\]

The old parity bound and `n_u<=a+1` imply `E_1(A_u)<=an_u`; hence
`Q-TV_k(H)<=\zeta_u<=2Z_H`. The exact single-head identity then gives
(Z3).

### Theorem 4: one-equal-edge extension

If a finite simple graph has at most one edge whose endpoints have equal
degrees, then its full imbalance sequence is graphical.

### Proof

The zero-edge-free case is the main theorem. Suppose that `G` has exactly
one zero-imbalance edge. The imbalance sum is even. Let

\[
y_1\ge\cdots\ge y_r>0
\]

be the positive imbalances; here `r=|E(G)|-1`. Graphicality of the full
sequence is equivalent to graphicality of this positive subsequence.

The first Erdős--Gallai inequality holds. Indeed, if `y_1>=r`, then
`y_1=|E(G)|-1`. Equality in the elementary bound
`w(e)<=|E(G)|-1` forces the edge's high endpoint to have degree
`|E(G)|`, so every edge is incident with it and the nontrivial part of `G`
is a star. That graph has no zero-imbalance edge, a contradiction. Hence
`y_1<=r-1`.

Assume a first failed index `k>=2`. Then `y_k>=k`; choose a top-`k` set `S`.
We show that its deficit cannot be negative.

- If `h=k`, (Z1) gives
  \[
  D_G(S)\ge\binom{k}{2}-1\ge0.
  \]

- Suppose `2<=h<k`. If the unique zero edge is not contained in `H`, then
  (Z2) and `L(h,p)>=1` give `D_G(S)>=0`. If it lies in `H`, the same follows
  whenever `L(h,p)>=2`. The only profile with `L(h,p)=1` is
  \[
  h=2,\qquad p=1,\qquad k=3,
  \]
  with head multiplicities `(2,1)`. Let `u` be the repeated head and write
  `d_G(u)=4+a`, `n=|A_u|<=a+2`. Here `Psi=2`, and the exact residual estimate
  is
  \[
  Q-TV_3(H)\le E_1(A_u)+\zeta_u-an.
  \]
  If `a>=1`, then `E_1(A_u)<=floor(n^2/4)<=an`, so the right side is at most
  `zeta_u<=2`. If `a=0`, then `n<=2`; for `n<=1` the same conclusion is
  immediate, while for `n=2`, either both active vertices are the endpoints
  of the unique zero edge, in which case `E_1(A_u)=0`, or
  `zeta_u<=1` and `E_1(A_u)<=1`. Thus always
  `Q-TV_3(H)<=2=Psi`, and `D_G(S)>=0`.

- Finally suppose `h=1`, with unique head `u`, and write
  `d_G(u)=k+1+a`, `A=A_u`, and `n=|A|<=a+1`. If the unique zero edge is not
  in `H`, (Z3) gives `D_G(S)>=B>=0`. Assume it is in `H`. The exact estimate
  is
  \[
  D_G(S)\ge B+an-E_1(A)-\zeta_u. \tag{Z9}
  \]
  For `a>=1`, one has
  \[
  E_1(A)+\zeta_u\le an.
  \]
  For `a=1` this follows by checking `n<=2`, observing that if both active
  vertices are joined by the unique zero edge then they cannot also form a
  unit edge. For `a>=2`, use
  \[
  E_1(A)+\zeta_u
  \le\left\lfloor\frac{n^2}{4}\right\rfloor+\min\{2,n\}
  \le an
  \]
  with `n<=a+1`. Hence (Z9) is nonnegative.

  It remains to consider `a=0`. Then `n<=1`. The cases `n=0`, `B>=1`, or
  `zeta_u=0` are immediate, so assume `n=1`, `B=0`, and the active vertex
  `z` is incident with the unique zero edge `zx`. The `k` selected low
  endpoints are leaves, `u` has only one further neighbor `z`, and
  \[
  d_G(z)=d_G(x)=r_0\ge2.
  \]
  In `H=G-u`, the vertex `z` has `r_0-2` positive incident edges other than
  `zx`, while `x` has `r_0-1` positive incident edges other than `xz`.
  These are distinct edges, so
  \[
  TV_k(H)\ge2r_0-3.
  \]
  The sole demand is
  \[
  q_z=(k-|k+1-r_0|)_+\le2r_0-3:
  \]
  if `r_0<=k+1`, then `q_z=r_0-1`; if `r_0>=k+1`, then
  `q_z<=k<=2r_0-3`. Thus `TV_k(H)>=Q`, and again `D_G(S)>=0`.

Every possible first failed index is excluded. Therefore the positive
imbalance subsequence, and hence the full imbalance sequence, is graphical.

### Significance of Theorem 4

This shows that the result has a nonzero robustness radius: local
irregularity is not a knife-edge hypothesis. The correction lemma identifies
precisely where equal-degree edges damage the proof and supplies a concrete
route toward larger zero-edge domains. It does **not** yet prove graphicality
when two or more zero-imbalance edges are present.
