# Section 1.4 - Canonical Orbital Elements
This section introduces the Hamiltonian for Kepler orbits and talks about the results of doing so. Since many standard coordinate systems aren't the best when dealing with the average orbit, this section focuses on using the hamiltonian to use other canoical coordinates to work with that make understanding certain asepcts of orbits much simplier. Most of this section talks about the different types of canoical coordinates that can be used and their different generating functions. However, there are only two different named canoical coordinate pairs, and they are the Delaunay variables and the Poincaré variables. This book goes into a bit more detail surrounding some of these canonical coordinates (such as their consequence on the hamiltonian and some extra definitions for new terms), but for the most part, this is majority of the section.

| Subsection of Document | Description of Subsection |
| -----------------------|---------------------------|
| [Self Imposed Exercises](#self-imposed-exercises) | An outline of any exercises I thought would be beneifical or fun to work through that relate to the section of the book, usually exercises I make for myself. |
| [Project Description](#project-description) | A description of the coding project I designed for this section of the book, as well as any relevant information I used. |
| [Concluding Thoughts](#concluding-thoughts) | Reflective thoughts about the chapter itself, the self imposed exercises I worked through, and the coding project I made for the section. |

## Self Imposed Exercises
Since most of this section was focusing on canonical coordinates using the orbital elements and what they are, there wasn't too much that was left as an exercise to the reader. However, there is an extra little bit of work I wanted to get some practice in for this section. During this section, the book gives 5 different sets of canonical coordinates, as well as their generating function. I thought it would be fun to derive them and get some practice working with generating functions (since I am fairly certain I never saw them during my undergraduate studies). However, I am ***not*** going to be deriving the first set of canonical coordiates, which are the Delauney variables. This is mostly because I don't entirely understand their derivation, and the book just states what they are at the beginning. Regardless, to make sure we're on the same page, here are the Delauney variables.

$$ 
\begin{aligned}
\ell, & \qquad \qquad \Lambda \equiv (GMa)^{1/2}, \\
\omega, & \qquad \qquad L = [GMa(1-e^{2}]^{1/2}, \\
\Omega, & \qquad \qquad L_{z} = L\cos(I)
\end{aligned}
$$

Before getting into the derivations, I would like to state a fact that is derived in the appendex about generating functions. If we have a generating function $S_{2}(\textbf{q}, \textbf{P})$, (where $(\textbf{q}, \textbf{p})$ are our initial coordinates and $(\textbf{Q}, \textbf{P})$ are the coordinates we're transforming to), then we have the following relation.

$$ \textbf{p} = \frac{\partial S_{2}}{\partial \textbf{q}}, \qquad \textbf{Q} = \frac{\partial S_{2}}{\partial \textbf{P}} $$

Now we can start deriving these sets of coordinates. First, each set has their own generating function and they are all derived from the Delauney variables. So for this case, we have $\textbf{q} = (\ell, \omega, \Omega)$ and $\textbf{p} = (\Lambda, L, L_{z})$. Now we just need a generating function.

### 1st Coordinate Set
For this one, we will use the generating function $S_{2}(\textbf{q}, \textbf{P}) = (\ell + \omega + \Omega)P_{1} + (\omega + \Omega)P_{2} + \Omega P_{3}$. It is rather straightforward to get $\textbf{Q}$, as the $\textbf{P}$ simplify nicely.

$$
\begin{aligned}
Q_{1} = & \frac{\partial S_{2}}{\partial P_{1}}  = \ell + \omega + \Omega \\
Q_{2} = & \frac{\partial S_{2}}{\partial P_{2}} = \omega + \Omega \\
Q_{3} = & \frac{\partial S_{2}}{\partial P_{3}} = \Omega
\end{aligned}
$$

The momenta have slightly more work, but nothing too bad either.

$$
\begin{aligned}
p_{1} = & \Lambda = \frac{\partial S_{2}}{\partial \ell} = P_{1} \\
p_{2} = & L = \frac{\partial S_{2}}{\partial \omega} = P_{1} + P_{2} \\
p_{3} = & L_{z} = \frac{\partial S_{2}}{\partial \Omega} = P_{1} + P_{2} + P_{3}
\end{aligned}
$$

From the first equation we have the following.

$$ P_{1} = \Lambda $$

Here we can substitue in this value into the second equation to solve for $P_{2}$.

$$ L = \Lambda + P_{2} \Rightarrow P_{2} = L - \Lambda $$

In the last one, we can substitue $L = P_{1} + P_{2}$ to solve for $P_{3}$

$$ L_{z} = L + P_{3} \Rightarrow P_{3} = L - L_{z} $$

Thus, are final canonical coordinate set is the following.

$$
\begin{aligned}
\lambda &= \ell + \omega + \Omega, \qquad \qquad \Lambda, \\
\varpi &= \omega + \Omega, \qquad \qquad L - \Lambda, \\
\Omega, & \qquad \qquad \qquad \qquad L - L_{z}.
\end{aligned}
$$

## Project Description
More text!

## Reflecting Thoughts
### Section 1.4 Thoughts
Overall, this section was both rather easy and very difficult to get through. The section started off with talking about the Hamiltonian equation of motion, which was rather straight forward and then went into talking about canonical coordinates for the orbital elements. I didn't remember a lot of the hamiltonian, so I went to the appendix for a refresher. Most of this was fine, until I got to the "propegator" section, where I am very certain I did not learn that in my undergraduate studies. This is where the book tended to lose me, especially when it came to deriving the Delauney variables. I read through that section, and truthfully only kind of understood it. After getting to the end, I figured that this was just background context should I want it, and went back to reading the actual chapter (especially since I was spending *a lot* of time in the appendix and trying and failing to look stuff up).

However, the rest of the chapter was rather straightforward, and a lot simpler to get through. Once you have the Delauney variales, the rest comes rather easy. The book gives you the generating function for each coordinate set, and it is pretty straightforward how to get these coordinates from the generating functions. Speaking of the generating functions, I am still a bit unsure where they specficially come from. I know that they have to be a function of some combination of the canonical pairs, but it looks like you can make the function itself whatever you want as long as it's well defined? Truthfuylly, I am not sure, and I am fairly certain that there is more reason behind it, but I failed at finding one. Overall though, the section itself (and only the section), was rather easy to get through.

### Project Thoughts

### Concluding Thoughts
