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

$$ E = \frac{-GM}{a} $$

Using some quick re-arranging, we can yield the following.

$$ a = \frac{-GM}{E} $$

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
In order to have the path show up on matplotlib, I first needed to create an array of values for my input. As mentioned before, I am using $f$ as my input variable and $f=0$ when starting at periapsis or $f=\pi$ when starting at apoapsis. For circular orbits, this range is $[0, 2 \pi)$, and for hyperbolic orbits, this range $(-f_{\infty}, f_{\infty})$, where $f_{\infty}$ is the asymptotic true anomaly. 

Once these arrays were created, I then created a new array which was to be the value for $r$. For each value in $f$, I used the equation of motion for $r$, and put the resulting value in its own array. Thus, I have created two arrays (in this case, of size 100) that will be used to make the plot. I also decided to have a single plot in the center of the screen which represented the fixed mass. Since these are in polar coordinates, an extra step was taken (during the animation function) to translate it into cartesian so it could be plotted.

In order to animate the path, I first created three different "lines" (as named by matplotlib) which represent the three different parts of the graph I wanted to see. These parts were the fixed mass in the center, the orbiting particle, and the path of the orbiting particle (the tracer). I used the FuncAnimation function from matplotlib, which takes in an update and init function. I am not sure if these functions need to return the lines that were plotted, but the examples did it, so I did it too. 

Regardless, The init function simply set up the bounds of the plot, in this case 500x500, which was chosen arbitrarily. The update function is where the animation actually happens. For each frame, I created two lists that were a chunk of the graph based on the current frame. This was then plotted using line1, which created the tracer of the orbit. The second line was a singular dot, which was just the last two data points of the segment obtained for line1, and this dot went in line2. The data for line3 was never changed as it was a fixed mass.

### Creating the GUI
This is the last part of the program, and took around half of the time to create. I wanted a GUI that took in starting values for my program. The library I chose to use was tkinter, because I saw that it had easy embeding of matplotlib figures. I didn't spend much time on design, as the space was cramped and I wasn't entirely sure what I was doing. I created some instruction labels at the top for people to read, and added in text boxes for people to put their starting values. Just for fun, I added in two radio buttons that determined the starting position of the particle as well. 

To make things just a bit spicier, I added a try/except block so that the program wouldn't crash if the user gave an incorrect response. If any error did show up, then a big red label appeared and told the user to try again. I also added a button at the bottom of the interface that started the simulation. All this did was remove all of the widgets on the screen and replaced it with the simulation I wanted to see (the orbit). I did not create a button to go back to the start however, so the user has to restart the program when the simulation starts.

## Reflecting Thoughts
As mentioned before, I think this project got a little too ambitious. It required I learn two new Python concepts that I have never used in my life (matplotlib animation and creating a GUI), and made the process of finishing it rather long. That being said, I think it was a good idea to go through with both of them. The animation adds a nice flavor where you can see the particle's actual path of orbit. I like the GUI too because it adds a nice bit of polish to everything and makes it feel more like a project than just some random program. 

For all of these reasons, I am happy with how the program turned out. There are a few things that could be upgraded or "fixed". The GUI could be fixed by adding a button or option to return to the main page. On top of not sure how to do that, I also didn't feel like figuring out how to do that, and I'm fine leaving it the way it is. In terms of plotting, I wanted to make the apoapsis button have the starting position be the apoapsis instead of the radius inputted always be the periapsis. However, I couldn't figure out how to do this with any reasonable accuracy. I did have a version where it kind of worked, but everything got janky with hyperbolic motion (as apoapsis doesn't exist in that case), so I just removed the feature.

Lastly, I am happy I chose this particular route for the program. The process helped me learn about the different processes described in the book, and made some lesser known parts more obvious. As an example, I wasn't sure why $f_{\infty}$ was defined as what it was at first. It was only when I went to fix the program for the hyperbolic orbit that I figured it out. When I tried to have an input range of $[0, 2 \pi)$ the program plotted the entire hyperbola, as it switched over to the other side when the bottom of the equation of motion flipped sign. I determined the $f$ value for when this happens and discovered that it was exactly $f_{infty}$. There were a number of moments like this throughout this project, and I ended up learning a lot.
