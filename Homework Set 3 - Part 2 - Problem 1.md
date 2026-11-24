## Problem 1. Trajectory Optimization as a Quadratic Program
Learning objective: Understand how to formulate a finite-horizon trajectory optimization problem as a
quadratic program (QP) with linear dynamics and constraints.
Consider the following finite-horizon, discrete-time trajectory optimization problem,

$$
\begin{aligned}
\underset{x_{0:N},\,u_{0:N-1}}{\operatorname{minimize}} \quad
& \sum_{k=0}^{N-1}
  \left(x_k^\top Q x_k + u_k^\top R u_k\right)
  + x_N^\top Q_N x_N \\
\text{subject to} \quad
& x_{k+1} = A_k x_k + B_k u_k,
&& k = 0,\ldots,N-1, \\
& x_0 = x_{\mathrm{init}}, \\
& G_k x_k + h_k \le 0,
&& k = 0,\ldots,N, \\
& u_{\min} \le u_k \le u_{\max},
&& k = 0,\ldots,N-1.
\end{aligned}
$$

Here $N ≥ 1$, $x_k ∈ R^n$, $uk ∈ R^m$, $A_k ∈ R^{n×n}$ , $B_k ∈ R^n×m$, $G_k ∈ R^q×n$, and $h_k ∈ R^q$. The
symmetric weights satisfy $Q$, $QN ⪰ 0$ and $R ≻ 0$. All inequalities are componentwise.
In this problem, you will be using the ordering

$$
z =
\begin{bmatrix}
x_0^\top & \cdots & x_N^\top & u_0^\top & \cdots & u_{N-1}^\top
\end{bmatrix}^{\top}
\in \mathbb{R}^{d},
\qquad
d = (N+1)n + Nm.
$$

to obtain the equivalent quadratic program (QP) of the following form,

$$
\underset{z}{\operatorname{minimize}} \quad
\frac{1}{2} z^\top P z + p^\top z + r
\qquad \text{subject to} \qquad
A_{\mathrm{eq}} z = b_{\mathrm{eq}}, \quad G z \le h.
$$

For each part, display the block structure and give all matrix and vector dimensions. Label zero and identity
blocks clearly.

**(a) [4 points] Construct A_{dyn}z = b_{dyn} for the dynamics. Identify the blocks associated with x_k, x_{k+1}, and u_k.**  

$$
\begin{bmatrix}
A_{dyn\_0.0}  & \cdots & A_{dyn\_0.N}   &  B_{dyn\_0.0}  & \cdots &  B_{dyn\_0N.-1}  \\
\vdots        & \ddots & \vdots         &  \vdots        & \ddots &  \vdots         \\
\vdots        & \ddots & \vdots         &  B_{dyn\_a.0}  & \ddots &  B_{dyn\_b.N-1}  \\
\vdots        & \ddots & \vdots         &  I_{0.0}       & \cdots &  I_{dyn\_0.N-1}  \\
\vdots        & \ddots & \vdots         &  \vdots        & \ddots &  \vdots         \\
A_{dyn\_a.0}  & \cdots & A_{dyn\_a.N}   &  I_{a-b.0}     & \cdots &  I_{a-b.N-1}
\end{bmatrix}

\begin{bmatrix}
x_{0.0}    & \cdots   & \cdots   & \cdots   & \cdots & x_{0.z}        \\
\vdots    & \ddots    & \ddots   & \ddots   & \ddots & \vdots         \\
x_{N.z}    & \cdots   & \cdots   & \cdots   & \cdots & x_{N.z}        \\
u_{0.0}    & \cdots   & u_{0.b}  & I_{00}   & \cdots & I_{dyn\_0.z-b} \\
\vdots    & \ddots    & \vdots   & \vdots   & \ddots & \vdots         \\
u_{N-1.b} & \cdots    & u_{N-1.b}& I_{N-1.0}& \cdots & I_{N-1.z-b}
\end{bmatrix}

=

\begin{bmatrix}
b_{dyn\_0,0} & \cdots  & b_{dyn\_0,z} \\
\vdots       & \ddots  & \vdots      \\
b_{dyn\_a,0} & \cdots  & b_{dyn\_a,z}
\end{bmatrix}
$$

- The entries in A_{dyn} named A_{dyn\_XX} are multiplied against the components of $z$ named x_{XX}
- The entries in A_{dyn} named B_{dyn\_XX} are multiplied against the components of $z$ named u_{XX}
- The column index of A_{dyn} block corresponds to k.
- The column index of B_{dyn} block corresponds to k.
- The row index of x_{XX} block corresponds to k.
- The row index of u_{XX} block corresponds to k.


- a: # states in a single x entry
- b: # inputs in a single u entry. In these matrices, I assumed that b < a, arbitrarily. I filled in 
identity matrix blocks to fill in the difference between a and b.
- z: # length of z block

// A_{dyn}:  (a)x(N + N-1)
// z:        (N + N-1)x(z)
// b_{dyn}:  (a)x(z)

TODO: Need to redo this question. I treated A and B as vectors, but they're matrices.

**(b) [2 points] Construct A_{init\_z} = b_{init} for the initial state.**  

$$
\begin{bmatrix}
A_{init\_00}  & \cdots & A_{init\_0,n}  \\
\vdots         & \cdots & \vdots         \\
A_{init\_n,n} & \cdots & A_{init\_n,n}
\end{bmatrix}

\begin{bmatrix}
x_{00}  \\
\vdots   \\
x_{n,0} 
\end{bmatrix}

=

\begin{bmatrix}
b_{00}  \\
\vdots  \\
b_{n,0} 
\end{bmatrix}

$$

A: nxn
x: nx1

 - n: number of entries in a single x state. Also the length and width of a single A matrix


**(c) [2 points] Combine (a)–(b) into Aeqz = beq.**  

TODO: do this after I redo (a)

**(d) [4 points] Construct $G_{state}z ≤ h_{state}$ for all state inequalities, including $k = N$.**  

\begin{bmatrix}
G_k_0.0 ... G_k_0.g
...
G_k_n.0 ... G_k_n.g
G_N_0.0 ... G_N_0.g
...
G_N_n.0 ... G_N_n.g
\end{bmatrix}

*

x_k_0,0 ... x_N_0,0
...
x_k_g,0 ... x_N_g,0

<=

h_k_0,0 ... h_k_0,g
...
h_N_0,0 ... h_N_0,g

TODO: come back and convert to markdown


each G block: gxn
each x block: nx1
each h block: gx1

g: # rows in G
n: # state variables per x state
N: # time steps

**(e) [4 points] Construct G_{uz} ≤ h_u for both input bounds at every control step.**  

\begin{bmatrix}
G_k_0.0 ... G_k_0.g
...
G_k_n.0 ... G_k_n.g
G_N_0.0 ... G_N_0.g
...
G_N_n.0 ... G_N_n.g
\end{bmatrix}

*

u_k_0,0 ... u_N_0,0
...
u_k_g,0 ... u_N_g,0

<=

h_k_0,0 ... h_k_0,g
...
h_N_0,0 ... h_N_0,g


N: # time steps
n: # state variables per x state
g: # columns in a G block


**(f) [2 points] Combine (d)–(e) into Gz ≤ h.**  

TODO: do this after I've filled out d and e

**(g) [6 points] Determine P, p, and r. Don’t forget to account for the factor 1/2 in the QP objective.**  

Calculating dimensions:

z^T : (2N-1) x (N)     <- dimensions given as part of HW
P   : (N)    x (N)     <- length N because length of z is N. square because it's between z^T and z
z   : (N)    x (2N-1)

p   : (2N-1) x (N)     <- 2N-1 rows because it must have that many rows to output a matrix that's the same size as previous term
z   : (N)    x (2N-1)

r   : (2N-1) x (2N-1)  <- Must be this size to get added to previous terms

Q: nxn  <- length n because length of x is n. square because it's between x^T and x
R: nxn  <- same dimensions as Q because they're added together

Calculating values:

P : \sum_{k=0}_{N-1} (((Q_k + Q_k^T) / 2) + ((R_k + R_k^T) / 2)) + ((Q_N + Q_N^T) / 2)  <- match coefficients w/original objective
p : 0                                                                                   <- no input parameters w/power 1
r : 0                                                                                   <- no constants in original objective

TODO: check this by a TA
TODO: write out the matrices

**(h) [6 points]** Suppose we soften the state inequalities by introducing slack vectors $s_k \in \mathbb{R}^q$ at every timestep:

$$
G_k x_k + h_k \le s_k, \qquad s_k \ge 0, \qquad k = 0,\ldots,N.
$$

Add the penalty $\rho \sum_{k=0}^{N} s_k^\top s_k$ to the original objective, where $\rho > 0$ is a given weight. Using the augmented decision vector

$$
\bar{z} =
\begin{bmatrix}
z^\top & s_0^\top & \cdots & s_N^\top
\end{bmatrix}^{\top},
$$

describe how the QP from parts (a)–(g) changes. Explicitly give the updated objective coefficients and equality and inequality constraint matrices and vectors, including their dimensions and the constraints enforcing nonnegative slack. Briefly explain how $\rho$ affects the tradeoff between the original objective and state-constraint violation.  

The QP from parts a-g changes:
 - Hard boundaries from $G_kx_k + h_k$ become soft inequalities. Where the program might fail before, it is now merely penalized.
 - Though slack allows the program to pass, it does introduce a penalty
 - The slack is appended to $z$. Every matrix that $z$ is a part of has to enlarge to accommodate the slack vector.

Coefficients change like so:
 - 1/2 P   ->   1/2 s^T s_k + 1/2 P
 - p      ->    p
 - r      ->  r

TODO: after I do f, redo the $Gz < h$ matrix, but with slack
TODO: describe constraint for non-negative slack

ρ affects the tradeoff between original objective and state-constraint violation:
 - As ρ increases, the program will focus more on minimizing slack. It could potentially detract from the program's
 ability to solve the original problem, but only when the program is already violating that softened constraint.

**(i) [Ungraded]** Now, consider a subproblem at one iteration of sequential quadratic programming (SQP). Recall that the dynamics are linearized about the current reference trajectory $(\tilde{x}_k, \tilde{u}_k)$ to obtain

$$
x_{k+1} = A_k x_k + B_k u_k + C_k, \qquad k = 0,\ldots,N-1,
$$

where $A_k$, $B_k$, and $C_k \in \mathbb{R}^n$ are fixed during this iteration. The objective now also includes a trust region penalty cost and a terminal state cost,

$$
\begin{aligned}
&\sum_{k=0}^{N-1} \Big[
  x_k^\top Q x_k + u_k^\top R u_k \\
&\qquad + (x_k - \tilde{x}_k)^\top Q_{\mathrm{trp}} (x_k - \tilde{x}_k)
        + (u_k - \tilde{u}_k)^\top R_{\mathrm{trp}} (u_k - \tilde{u}_k)
  \Big] \\
&\quad + (x_N - x_{\mathrm{goal}})^\top Q_N (x_N - x_{\mathrm{goal}})
       + \rho \sum_{k=0}^{N} s_k^\top s_k.
\end{aligned}
$$

Here $x_{\mathrm{goal}} \in \mathbb{R}^n$ is a prescribed target, and the symmetric matrices $Q_{\mathrm{trp}} \in \mathbb{R}^{n \times n}$ and $R_{\mathrm{trp}} \in \mathbb{R}^{m \times m}$ are positive semidefinite weights penalizing deviations from the reference trajectory. Retain the initial condition, input bounds, and softened state inequalities from part (h). Using $\bar{z}$ from part (h), derive all coefficients of the resulting QP: $\bar{P}$, $\bar{p}$, $\bar{r}$, $\bar{A}_{\mathrm{eq}}$, $\bar{b}_{\mathrm{eq}}$, $\bar{G}$, and $\bar{h}$. Give their block structures and dimensions.
