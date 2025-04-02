# Section 1.8 - Nearly Circular Orbits
This section of the book focuses on orbits that have an eccentricity that is just slightly larger than 0, or (as the title suggests) a nearly circular orbit. The first part of this section focuses on putting the various anomalies (true, eccentric, mean) and the radius in terms of each other by using a Taylor expansion around the eccentricity, as it is close to 0. From here, the d'Alembert property is found. The next part of this section focuses on finding how the different dimensions of the orbit oscillate by finding the epicycle approximations. Each of the variables in cylindrical coordinates are found to have different oscillations that depend on the given gravitational potential. Other oscillations are also found for the argument of periapsis and the ascending node, but the book mentions / shows that for a standard Kepler potential, these do not change. The last part of the book is considering the gravitational potential due to the Kepler potential and the multipoles as well. The book shows how each of the epicycles are approximated from the expanded gravitational potential and shows that the argument of periapsis and the ascending node each have a non-zero derivative with respect to time as well (both change over time). The book ends this section by briefly talking about how we can use this idea of wobbling orbits to define the osculating elements of a system, which are used to help characterize these orbits.

| Subsection of Document                            | Description of Subsection                                                                                                                                     |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Self Imposed Exercises](#self-imposed-exercises) | An outline of any exercises I thought would be beneficial or fun to work through that relate to the section of the book, usually exercises I make for myself. |
| [Project Description](#project-description)       | A description of the coding project I designed for this section of the book, as well as any relevant information I used.                                      |
| [Reflecting Thoughts](#reflecting-thoughts)       | Reflective thoughts about the chapter itself, the self imposed exercises I worked through, and the coding project I made for the section.                     |

## Self Imposed Exercises
text2

## Project Description
For this project, I thought it would be a fun idea to to and showcase off what some of these nearly circular orbits looked like. The last two subsections surround this idea just in different ways, namely where the second subsection deals with the general epicycle approximation, and the last subsection deals with specifically the effect of multipole expansion on the potential. Since I wanted to showcase both of these, I figured I could split my own project into these two parts as well. As always, there is also a GUI that goes along with this project so that the program is more easily accessible.

### Epicycle Approximation
The book goes into great detail on how the approximations are found, but another method for modeling the two body system can be determined using a Taylor series approximation on the potential. Only looking at the first order equations for these provides us with the following approximations for the path of an orbiting body.

$$
z(t) = z_{0}\cos(\kappa_{z}t + \zeta), \quad \quad x(t) = x_{0}\cos(\kappa_{R}t + \eta), \quad \quad \phi(t) = \kappa_{\phi}t + \phi_{0} - \frac{2x_{0}\kappa_{\phi}}{R_{g}\kappa_{R}}\sin(\kappa_{R}t + \eta)
$$

Where $x$ is the deviation from the orbital radius $R_{g}$, $z$ is the altitude of the orbit, $\kappa$ is the frequency of the respective variable, and $\eta$ and $\zeta$ are integration constants. There is another form to write these in that the book outlines as well. Using just the linear part of the azimuth angle equation, we can re-write both $z$ and $x$ in terms of just $\phi$.

$$
x = x_{0} \cos \left[\frac{\kappa_{R}}{\kappa_{\phi}} (\phi - \phi_{R})\right], \quad \quad z = z_{0} \cos\left[\frac{\kappa_{z}}{\kappa_{\phi}}(\phi - \phi_{z})\right]
$$

This looks a bit nicer and is a tad easier to work with when actually making the code for the program itself. Doing it this way, means that I can use $\phi$ as an independent variable instead of relying on time (which can get a bit funky when coding).  

## Reflecting Thoughts
### Section Thoughts
This section was alright. Like many of those in the past, I think it got more interesting the more I ended up reading, but compared to the previous two sections, I think I just enjoyed it enough. The most difficult part to wrap my head around in this section was probably the jump in the various equations that happened at the beginning. The text undersells just how much work is required to create those Taylor expansions. I did them to make sure I understood where they were coming from, but there was a ton of leg work. I ended up having to do two Taylor expansions, and both required using limits as the derivatives weren't defined at that point.

The most interesting, and rather straight forward part of the section was the middle and last. I am sure that those Taylor expansions are similarly hard, but they're easier to conceptualize. Plus, this part was a bit more interesting as we got to actually explore how the multipole moments affect orbits. I was curious how they would be used when they were introduced in the previous section, and I am glad I have a change to see them now.

### Self Imposed Exercise Thoughts
text5

### Project Thoughts
text6

### Concluding Thoughts
text7
