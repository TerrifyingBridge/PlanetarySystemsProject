# Section 1.3 - Motion in the Kepler Orbit
This section compounds on the previous one by expanding on the ideas of Kepler orbit. The previous section talked about what the orbit looked like, but this section focused on how a particle actually moves inside this orbit. The section itself starts off with quickly mentioning Kepler's second and third law and using them to determine more properties about the orbit. We get a look into the period of an orbit, then get an earful of a lot of new definitions. We're introduced to the mean motion, mean anomaly, and eccentric anomaly. After this, the book does a lot of setting up equations and making relations for these new definitions (and introducing Kepler's equation) so that the fun part can happen. We take a brief aside to talk about the orbital averages and how to find them, and then transition into moving the equations of motion to a 2D plane and into a 3D coordinate system. A LOT of new terms are dropped here, but not used as the next section goes into solving equations for the position and velocity of a particle in orbit. The book mentions that you can do this the hard way with the 3D coordinate system, but the book uses Gauss's f and g functions to find these equations.

As per usual, I will first walk through any self imposed exercies I thought would be fun/benifical to me, talk about the coding project I made for this section, then end with my reflecting thoughts. More new to this section than the previous two is, I am going to add reflecting thoughts on the section itself as well as the project. My goal is to record my entire learning process thoughts and not just the coding part, as learning more astronomy is half of my goal for this. I will have to be careful, because there is a non-zero chance I'll just start complaining, but hey it's my project so my rules. That being said, I do want to try my best to keep this more centered around the learning part instead of the complaining part.

## Self Imposed Exercises
There is a lot this section leaves to the reader as an exercise, and because of this, it was hard to choose exactly I wanted to do for this section. I did end up trying a couple of different paths. The first part I tried doing was simplifying Gauss's $f$ and $g$ functions for hyperbolic orbits. I did end up re-writing them with these conditions in mind, but wasn't able to simplify them and it led to a gross mess of an equation (see Description of Project section). The next step was to mention the other route towards finding the equaiton of motion without using Gauss's functions and using the 3D equations for positioned outlined in 1.3.2. I worked on that for a bit, and realized that it was more of the same of the other exercise and was a lot of terms being thrown around and equation mangangement. I did kind of finish this one, but it's not the exercise I want to put here in this section. The one I want to spend my time on, is the orbital averages equation.

I know that this might seem silly, as the biggest reason I disliked the previous two exercises is that it was pretty much all trigonometry and hyperbolic trigonometry manipulation, and these equations are also a lot of that. However, these equations regard analytically solving integrals, which I found I am somewhat out of practice with. I figure, these exercises will give me a decent refresher on gross integers, even if they're all more or less the same type of integral with some variation. Some of these integrals are more gross than others, but I figure this is good practice. After all, these self imposed exercises are more so for me to refresh on material rather than learn new material (that's what the project is for). Without further ado, let's get into it.

## Description of Project
Since this section was about the motion in a Kepler orbit, I wanted to make an animation that showed the actual motion of a particle in an orbit given certain initial conditions, in this case, starting position and starting velocity. I wanted to make sure this program also showcased elliptical orbits as well as hyberolic orbits as well. This project is very similar to the project from Section 1.2, but slightly different. The project from the previous section showed an animation of a Kepler orbit using the true anomaly as the input variable, while this one would focus more on the input variable being time instead. Another addition I wanted to add was changing the representation from 2D to 3d. This section of the book had a subsection that talked about the representation of an orbit in 3D and I wanted to capture that in my project as well. It was also rather convenient that the final subsection generalized it so that the dimentions (or reference frame) didn't matter too much.

### Creating the GUI
I wanted to talk about this first, as it is the least interesting of the comments I have about the project. The GUI itself is modeled after the GUI from the project in Section 1.2. I used the Tkinter library to create it, and even kept most of the formating the same. There is a brief instruction set as well as text boxes to input the starting values for both position and velocity. I even kept the error handling the same just in case the user tries to give invalid inputs.

<p align="center">
<img src="assets/gui.png" alt="GUI Image" width="300">
</p>

### Vector3D
Since I wanted to make this project in a 3D coorindate system, I needed to update my vector class to the new dimention. Most of this method is exactly what you would expect, just adjusting for the $z$ term for 3D. However, there are a few interesting parts I wanted to discuss.

Later on I needed the magnitude of the cross product of two vectors, so I added a method to this class to do exactly that. However, this also required a method to determine the angle between two vectors as well. The method that calculates the magnitude of the cross product is done using the equation for the magnitude of the cross product, instead of calculating the cross product and taking the magnitude then.

The other method I added was the copy method. As someone who teaches a computer science class, I should have been able to determine this was needed much earlier. Many times in my code, I was accidently creating variables to were all assigned to the same object. When I changed what I thought was a temporary variable was actually the original vector I was using. The copy method just creates a new vector with the same coordinates as the parent, but allows me to modify it without changing the original.

### Plotting Elliptical Orbits
I started by first making sure that I was able to plot elliptical orbits before getting too deep into the project. I did this by using Gauss's $f$ and $g$ functions, which are defined using the following equation.

$$ \mathbf{r} (t) = f(t,t_{0})\mathbf{r_{0}} + g(t,t_{0})\mathbf{v_{0}} $$

Where $\mathbf{r_{0}}$ is the initial position of the partical and $\mathbf{v_{0}}$ is the initial velocity of the particle. Using this definition, many other relations found earlier in the book, and a lot of algebraic manipulation, one can find Gauss's functions in terms of the true anomaly and eccentric anomaly. Since the eccentric anomaly (designated using the letter $u$) is the easiest one that directly corrilates to time, this is the variation I used. The book gives us this equation, but just to be certain I understood what was happening, I made sure to do it myself as well (for my worked out solution to this, see Problem 12 in the Chapter Problems file). These equations ended up being the following.

$$ f(t, t_{0}) = \frac{\cos(u - u_{0}) - e\cos(u_{0})}{1 - e\cos(u_{0})} $$
$$ g(t, t_{0}) = \frac{1}{n} [\sin(u - u_{0}) - e\sin(u) + e\sin(u - u_{0})] $$

Now that we have this, we can find the motion of a particle around a mass, as the variable $u$ relates to the mean anomaly, which relates to time. Before actually getting into things, we need one more relation, which relates the semi-major axis ($a$) with the magnitudes of the starting positions. This relation is seen below.

$$ \frac{1}{a} = \frac{2}{r} - \frac{v^{2}}{GM} $$

Now we have everything we need to actually plot the equation of motion. It just needs to be broken down into a couple of steps.

1. First, compute $r_{0} = |\mathbf{r_{0}}|$ and $v_{0} = |\mathbf{v_{0}}|$
2. Use the relation mentioned above the find the semi-major axis $a$
3. Use the semi-major axis to find the mean motion using Kepler's Law
4. Use the initial conditions to determine the magnitude of the angular momentum $L = |\mathbf{r_{0}} \times \mathbf{v_{0}}|$
5. Use the magnitude of the angular momentum and the semi-major axis to find the eccentricity $e$
6. Use the semi-major axis, eccentricity, and $r_{0}$ to determine $\cos(u_{0})$ then take the inverse cosine function to determine $u_{0}$
7. Use Kepler's Equaiton to determine the initial mean anomaly $l_{0}$
8. Use the equation with respect to time to determine $l$ at a given time $t$
9. Use Kepler's equation to determine $u$ for a time $t$
10. Use $u$ to find the values for Gauss's functions $f$ and $g$
11. Use Gauss's functions to find the position of the particle for the given time.

Simple stuff. With all of these steps, I was able to plot an elliptical orbit for a particle mass. However, before jumping into the final result, there are a couple of points I want to talk about first.

#### Solution to Kepler's Equation
The book mentioned that Kepler's equation cannot be solved analytically, and needs to be done numerically. The solution I ended up using was fixed-point iteration. I saw that technically Newton's method converged faster, but wikipedia said that fixed-point interation was identical to Kepler's solution, so I stuck with that. Here is the code for it.

```python
def calc_u(l, ecc, accuracy):
  E = l
  err = E
  while (err > accuracy):
    temp = l + ecc * np.sin(E)
    err = np.abs(E - temp)
    E = temp
  return E
```
It is a little robust, and the accuracy term isn't entirely reliable due to floating point error, but this is what I used to find $u$ from the mean anomaly.

#### Temporary Confusion
So, I used all of these steps, and set up the program so that it could take in a starting position and velocity and then plot the resulting elliptical orbit. I chose some random numbers for these values that kept the eccentricity below 1, and I obtained the following result.

<p align="center">
<img src="assets/wrong_orbit.png" alt="GUI Image" width="300">
</p>

This... wasn't correct. And for a long time, I was confused on what was happening. Eventually, the error I made was in step 6 when taking the inverse cosine to determine $u_{0}$. The inverse cosine function is only defined for angles between $0$ and $\pi$, so when we reach a point where $u_{0}$ is greater than $\pi$, the program freaks out and plots a very incorrect graph.

Fortunately, this is an easy fix, as we just need to know the sign of the radial velocity $\dot{r}$. When $\dot{r}$ is positive, $0 < u_{0} < \pi$, and when $\dot{r}$ is negative, $\pi < u_{0} < 2\pi$. Honestly, I wasn't able to figure this out analytically that didn't involve a bunch of extra math that I didn't really want to do. The book only has a couple relations that involve the radial velocity that depends on other variables. The first one involves $\dot{r}$ being squared, which doesn't tell us the sign, and the other depends on $u$, which is what we're trying to solve for. 

I solved this problem numerically. Since we start with a starting position AND velocity, what I did was add the starting velocity to the starting position, then checked to see if the magnitude was greater or smaller than the starting position. If it was greater, than the radial velocity was increasing, if it was lesser, then the radial velocity was decreasing. Adding in this fix was able to make sure all orbits were plotted correctly.

<p align="center">
<img src="assets/good_orbit.png" alt="GUI Image" width="300">
</p>

### Plotting Hyperbolic Orbits
The biggest reason I wanted to implement this orbit was because it's rather difficult to tell whether a certain orbit will be an ellipse or hyperbola when supplying the starting position and velocity. On top of this, I think a pass-by hyperbolic orbit would be fun to witness. However, we need to know how to code this, which theoretically, shouldn't be that bad. We just need to determine the equations for Gauss's $f$ and $g$ functions when eccentricity is greater than 1.

Fortunately, the book gives relations for the true anomaly to the hyperbolic eccentric anomaly. These relations are shown below.

$$ \cos(f) = \frac{e - \cosh(u)}{e\cosh(u) - 1}, \quad \sin(f) = \frac{(e^{2}-1)^{\frac{1}{2}}\sinh{u}}{e\cosh{u} - 1} $$

The book also provides equations for Gauss's functions in terms of the true anomaly, also given below. So it should be a matter of using the relations mentioned earlier to find Gauss's functions in terms of the hyperbolic eccentric anomaly.

$$ f(t, t_{0}) = \frac{\cos(f - f_{0}) + e\cos(f)}{1 + e\cos(f)} $$
$$ g(t, t_{0}) = \frac{(e^{2} - 1)^{\frac{3}{2}} \sin(f - f_{0})}{n(1 + e\cos(f))(1 + e\cos(f_{0}))} $$

Now, I wasn't able to simplify this analytically. Creating the functions is easy enough as it is just a matter of substitution, but it looks gross and I feel like it could be simplified. I tried for a while, but I wasn't able to figure that part out, so I stuck with the gross looking. 

I used this method to calculate the hyperbolic orbit for a particle when the eccentricity was greater than 1. However, whenever I used starting conditions for the program, I saw an orbital path that, seemingly, just traced a straight line. This remained true even for eccentricities really close to 1 (such as 1.0003). To verify that anything was happening, I then oriented the graph so that I was witnessing a head-on path of the particle. And what I saw was the particle genuinely curving.

## Reflecting Thoughts
Alright, so this first paragraph will center around my thoughts about reading through/learning the chapter and the next few will be about my project and other general ideas. Because of this, I am writing this as soon as I am done reading the section (and understanding it) so there will be a large break between this one and the next one. I am not entirely sure how this will work, but if I don't like it, I'll change it for next time.

I found this section to be significally more digestable than the previous section. In the previous seciton, I really felt like the jumps in the steps were a lot harder to grasp. However, this section connceted a lot better in terms of what was being demonstrated. I imagine this is one of three things: the book is getting better at representing its material, I'm getting less rusty at the physics behind the skips so it's easier to follow, or the book is building on itself rather than assumed knowledge so there are less gaps for me to need to fill in. I believe it's probably the latter 2, but I wouldn't call this book perfect either. There are many times where the book mentions "this is the case" for certain explanations, and I'm sure this is because the book is advertised for "advanced undergrads, graduate students, and researchers new to the field" (as per the back of the book), but it still annoys me. The other thing I want to point out is the notation, as I don't exactly know how standard it is. Whenever I am confused on a topic, I look up reference material to help work me through it, and when doing so, the notation is always different. For example, in the book, Kepler's equation is $\ell = u - e\sin(u)$ while in most resources online I found it was written as $M = E - e\sin(E)$. I suppose this isn't a huge deal, but something I've notived. Anyway, into the coding project.
