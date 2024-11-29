# Section 1.2 - The Shape of the Kepler Orbit
This section, as you might have guessed, outlines what the different types of Kepler Orbits look like. The section starts off with using the acceleration derivative of $\mathbf{r}$ (or as it's more commonly seen, $\mathbf{\ddot{r}}$) in polar coordinates to derive some basic relations to energy and angular momentum. This then transitions into finding the periapsis and apoapsis. With all of this under our belt, the section transitions into solving the equation of motion that satisfy the differential equation, and ends the section talking about the different cases, and what they look like. The section ended with a discussion on the conditions (assuming a hyperbolic orbit) in order for the test partical to collide with the fixed mass it was orbiting.

As last time, I will first go through some self imposed exercises that I thought would be interesting / benifical to work through, then later talk about the project I specifically worked on. On an unrelated note, you will notice that I'm using different vectors than for the previous section. This is because a friend of mine looked at the notation I was using and absolutely hated it. Thus, I have changed to the notation used in this file here. I am not going back to change the old file (something about seeing growth blah blah blah).

## Self Imposed Exercises
Uhh

## Description of Project
Alright, so I think I tried a little too hard on this one? Either that or it was just enough. Regardless, I am kinda happy with the end result.

Since this section was dedicated to describing and deriving Kepler Orbits, I figured that a good program to make would be one that actually showcases these orbits. After deriving the equations of motion, there ended up being three cases, namely energy less than zero, energy greater than zero, and energy equal to zero. The program I built showcases two of these cases, mainly because I forogt the last case (where the orbital path is parabolic).

My thought for direction on this was two parts: a plot that showed an animation of the orbital path, and a GUI interface that initializes the values for the plot. For the plot, I chose to use the library matplotlib with contributions from the numpy library. For the GUI interface, I used the library tkinter, which also allowed for some compatibility with matplotlib so I could combine the two.

### Alpha Version
Going into this particular project, I knew nothing about tkinter (besides its existance) and knew enough about matplotlib to make a plot, but not how to animate it. So this particular part needed a lot of learning. To do this, I created a test file (aptly named test.py). 

I'll go into the particulars of the manipulation of the equations of motion later, as for now I want to talk about what this file is. This file contains the animation of a specific Kepler orbit (I don't remember which one), which I used to learn how to animate in matplotlib without the worry about the GUI. I left this file in here mainly because I wanted to leave a breadcrumb trail as to how I went about creating the project overall. 

Anyway, let's talk about what the program actually contains.

### Plotting Kepler Orbits in Matplotlib
The set up for this program is rather simple. We consider an object with fixed mass $M$ which sits at the origin of our plot. We want to consider the path of a test partical with negligable mass when it is dropped on a specific point around this fixed mass. 

#### Set Up

Setting up the constants are easy, as I just choose a mass of $10^{16}kg$ to sit in the center and used the gravitational constant $G$ to keep things nice and neat. However, we need the equation of motion of a particle in orbit before we can move on. Since around half of this section is dedicated to deriving the equation of motion for a Kepler orbit, it also happens to have the orbit itself neatly outlined, which for clarity can be seen below.

$$ r = \frac{a(1-e^{2})}{1 + e \cos{f}} $$

We can be a bit tricky and have $r$ be a function of $f$ (where $r$ is the distance from the fixed mass and $f$ is true anomoly). I create the graph where the periapsis was always to the right of the fixed mass ($\cos(0) = 1$). However, there are a few unknowns that we have to solve in order to actually start plotting. These unknowns are $a$ and $e$ from the equation of motion (semimajor axis and eccentricity respectfully). 

To combat this, I gave the program two initial values: the energy of the system and the starting distance of the periapsis from the origin. Using these two starting values, we can find the values for this unknowns. The first we will look for is $a$. The book derives the following relation between $a$ and $E$.

$$ E = -GM/a $$

Using some quick re-arranging, we can yield the following.

$$ a = -GM/E $$

With one unknown found, we can use its value to find the other. To solve for the eccentricity, we can plug in our initial conditions for simulation ($r=r_{0}$ and $f = 0$) into our equation of motion.

$$ r_{0} = \frac{a(1 - e^{2})}{1 + e \cos{0}} $$

Here is where our choice of having $f$ be 0 is helpful, as we can re-write this equaiton as follows.

$$ \frac{a(1 - e^{2})}{1 + e} = \frac{a(1 - e)(1 + e)}{1 + e} $$

One of these binomials cancel out, and we're left with the following relation to $r_{0}$

$$ r_{0} = a(1 - e) $$

From here it is just a simple re-arranging to find $e$

$$ e = 1 - \frac{r_{0}}{a} $$

Now with everything accounted for, we can actually plot the orbit.

#### Actually Plotting the Orbit
## Reflecting Thoughts
