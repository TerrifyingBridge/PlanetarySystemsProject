# Section 1.2 - The Shape of the Kepler Orbit
This section, as you might have guessed, outlines what the different types of Kepler Orbits look like. The section starts off with using the acceleration derivative of $\mathbf{r}$ (or as it's more commonly seen, $\mathbf{\ddot{r}}$) in polar coordinates to derive some basic relations to energy and angular momentum. This then transitions into finding the periapsis and apoapsis. With all of this under our belt, the section transitions into solving the equation of motion that satisfy the differential equation, and ends the section talking about the different cases, and what they look like. The section ended with a discussion on the conditions (assuming a hyperbolic orbit) in order for the test partial to collide with the fixed mass it was orbiting.

As last time, I will first go through some self imposed exercises that I thought would be interesting / beneficial to work through, then later talk about the project I specifically worked on. On an unrelated note, you will notice that I'm using different vectors than for the previous section. This is because a friend of mine looked at the notation I was using and absolutely hated it. Thus, I have changed to the notation used in this file here. I am not going back to change the old file (something about seeing growth blah blah blah).

## Self Imposed Exercises
In my opinion, there is a lot less that this section jumps over, and when it does jump over something, it usually make sense. Most of the jumps over the non-obvious steps come from the derivation of the equation of motion. For this reason, I want to derive this equation of motion myself as an exercise. This cheating a bit, since the book technically does this already, but in my derivation, I'll go into more detail than the book does to make up for it. On top of this, another exercise I want to do is derive the second time derivative of $\mathbf{r}$ in terms of it's components. I think the book also shows this process in the appendix, but I'm not going to be looking there, and doing it myself (mostly for good practice).

### Derivation of $\mathbf{\ddot{r}}$
First thing I want to point out. For some reason the book uses $\psi$ for the angle in polar coordinates, but I will be using $\theta$ because it conforms to the convention I'm used to. Anyway, as you might imagine we're working in polar coordinates $(r, \theta)$. Alright to start, we're going to consider an object in an orbital plane. Since we're working with polar coordinates, our starting vector is $\mathbf{r} = r\mathbf{\hat{r}}$. Before we start, let's write our polar unit vectors in terms of cartesian unit vectors. 

$$ \mathbf{\hat{r}} = \cos (\theta) \mathbf{\hat{x}} + \sin (\theta) \mathbf{\hat{y}} $$
$$ \boldsymbol{\hat{\theta}} = -\sin (\theta) \mathbf{\hat{x}} + \cos (\theta) \mathbf{\hat{y}} $$

This is important to note, as because the polar unit vectors rely on $\theta$, it has a non-zero time derivative. Before we can derive our original derivative, we need to find these derivatives. Fortunately, since it's sines and cosines it isn't too bad.

$$ \frac{d \mathbf{\hat{r}}}{dt} = -\sin (\theta) \frac{d \theta}{dt} \mathbf{\hat{x}} + \cos (\theta) \frac{d \theta}{dt} \mathbf{\hat{y}}$$
$$ \frac{d \boldsymbol{\hat{\theta}}}{dt} = -\cos (\theta) \frac{d \theta}{dt} \mathbf{\hat{x}} - \sin (\theta) \frac{d \theta}{dt} \mathbf{\hat{y}}$$

Here we can factor out $\frac{d \theta}{dt}$ and re-write it as $\dot{\theta}$. 

$$ \frac{d \mathbf{\hat{r}}}{dt} = (-\sin (\theta) \mathbf{\hat{x}} + \cos (\theta) \mathbf{\hat{y}}) \frac{d \theta}{dt} = \dot{\theta} \boldsymbol{\hat{\theta}} $$
$$ \frac{d \boldsymbol{\hat{\theta}}}{dt} = (-\cos (\theta) \mathbf{\hat{x}} - \sin (\theta) \mathbf{\hat{y}}) \frac{d \theta}{dt} = -\dot{\theta} \mathbf{\hat{r}} $$

Now that we have these values, we can go back to our original problem. As a reminder, our position vector in polar coordinates is $\mathbf{r} = r\mathbf{\hat{r}}$. To start, we will find the first time derivative for this position. We can use the product rule to do this.

$$ \frac{d \mathbf{r}}{dt} = \frac{d}{dt} (r \mathbf{\hat{r}}) = \frac{d r}{dt} \mathbf{\hat{r}} + r \frac{d \mathbf{\hat{r}}}{dt} $$

We can substitute our time derivatives with the values found earlier, and use dot notation to clean up the rest.

$$ \mathbf{\dot{r}} = \dot{r} \mathbf{\hat{r}} + r \dot{\theta} \boldsymbol{\hat{\theta}} $$

Simple enough. We need to take another time derivative of this equation in order to find the second derivative (duh).

$$ \frac{d \mathbf{\dot{r}}}{dt} =  \frac{d}{dt} (\dot{r} \mathbf{\hat{r}} + r \dot{\theta} \boldsymbol{\hat{\theta}})$$

Alright, lots of product rule in this one.

$$ \mathbf{\ddot{r}} = \frac{d \dot{r}}{dt} \mathbf{\hat{r}} + \dot{r} \frac{d \mathbf{\hat{r}}}{dt} + \frac{dr}{dt} \dot{\theta} \boldsymbol{\hat{\theta}} + r \frac{d \dot{\theta}}{dt} \boldsymbol{\hat{\theta}} + r \dot{\theta} \frac{d \boldsymbol{\hat{\theta}}}{dt} $$

Before simplifying this down, let's substitue known values and clean up the equation.

$$ \mathbf{\ddot{r}} = \ddot{r}\mathbf{\hat{r}} + \dot{r}\dot{\theta}\boldsymbol{\hat{\theta}} + \dot{r}\dot{\theta}\boldsymbol{\hat{\theta}} + r\ddot{\theta}\boldsymbol{\hat{\theta}} - r\dot{\theta}^{2}\mathbf{\hat{r}} $$

Now this is a matter of rearranging terms and combining like terms, then we come to our final result.

$$ \mathbf{\ddot{r}} = (\ddot{r} - r\dot{\theta}^{2})\mathbf{\hat{r}} + (2\dot{r}\dot{\theta} + r\ddot{\theta})\boldsymbol{\hat{\theta}}$$

### Derivation of Equation of Motion
In order to derive the equation of motion, we first need to know what we're working with. As described back in the first section, we know the following relation for orbital motion.

$$ \mathbf{\ddot{r}} = -\nabla\Phi_{\text{K}} $$

Where $\Phi_{\text{K}}(r) = -\frac{GM}{r}$. Fortunately, since $\Phi_{\text{K}}$ only relies on $r$, $\frac{d \Phi_{\text{K}}}{d\theta} = 0$. To actually begin solving this, we will use the equation derived earlier for $\mathbf{\ddot{r}}$. This yields us two different equations.

$$ -\frac{d \Phi_{\text{K}}}{dt} = \ddot{r} - r\dot{\theta}^{2}, \quad 2\dot{r}\dot{\theta} + r\ddot{\theta} = 0 $$

Let's focus on that second equation. We can be a little tricky and multiply both sides by $r$. The right side stays 0, but the interesting part is the left side. Doing so allows us to rewrite it as a product rule.

$$ 2\dot{r}r\dot{\theta} + r^{2}\ddot{\theta} = \frac{d}{dt}(r^{2})\dot{\theta} + r^{2} \frac{d}{dt}(\dot{\theta}) = \frac{d}{dt} (r^{2}\dot{\theta}) = 0 $$

This is rather convient, as now we can just integrate both sides with respect to $t$. This leaves us with the following.

$$ r^{2}\dot{\theta} = C $$

Where $C$ is a constant. Now we're going to take a small detour to show something, namely that this constant is exactly equal to the magnitude of the angular momentum per unit mass. By definition the angular momentum per unit mass is the following.

$$ \mathbf{L} = \mathbf{r} \times \mathbf{\dot{r}} $$

Fortunately, as seen previouisly, we know what is $\mathbf{\dot{r}}$ is equal to. So let's replace it with what we found above.

$$ \mathbf{L} = r\mathbf{\hat{r}} \times (\dot{r} \mathbf{\hat{r}} + r \dot{\theta} \boldsymbol{\hat{\theta}}) $$

We can distribute the cross product to each one to evaluate this.

$$ \mathbf{L} = r\mathbf{\hat{r}} \times \dot{r} \mathbf{\hat{r}} + r\mathbf{\hat{r}} \times r \dot{\theta} \boldsymbol{\hat{\theta}} $$

The cross product of a vector against itself is 0, and the other terms are perpendicular so the magnitude is just the magnitudes of the vectors multiplied with each other.

$$ \mathbf{L} = r^{2}\dot{\theta}(\mathbf{\hat{r}} \times \boldsymbol{\hat{\theta}}), \quad L = r^{2}\dot{\theta} $$

Thus showing that the constant $C$ from earlier is just the magnitude of the angular momentum per unit mass. Having this equation let's us solve for $\dot{\theta}$ and gives us the following equation.

$$ \dot{\theta} = \frac{L}{r^{2}} $$

We do this as it'll be helpful later. Also, we can substitue this value into the other equation of the gradiate. This yields the following differntial equation.

$$ \ddot{r} - \frac{L^{2}}{r^{3}} = -\frac{d\Phi_{\text{K}}}{dt} $$

This is the differential equation we need to solve in order determine the equation of motion. Unfortunately, this is rather gross. However, we can simplify it down to a easier differential equation to solve. Before doing that, we need to some leg work to make it cleaner. The first step is using the transformation $u = 1/r$, where $u$ is just a temperary variable. Next, we can re-write the time derivative operator by changing the independant variable from $t$ to $\theta$.

$$ \frac{d}{dt} = \frac{d \theta}{dt} \frac{d}{d\theta} = \dot{\theta}\frac{d}{d\theta} = Lu^{2}\frac{d}{d\theta} $$

We will use this relation to re-write $\ddot{r}$ in terms of $u$ and the angle.

$$ \dot{r} = \frac{dr}{dt} = Lu^{2}\frac{du}{d\theta}\frac{dr}{du} = Lu^{2}\frac{du}{d\theta} (\frac{-1}{u^{2}}) = -L\frac{du}{d\theta}$$

We can repeat this process for $\ddot{r}$ and substitute what we found for $\dot{r}$.

$$ \ddot{r} = \frac{d\dot{r}}{dt} = \frac{d}{dt} (-L\frac{du}{d\theta}) = Lu^{2} \frac{d}{d\theta} (-L\frac{du}{d\theta}) = -L^{2}u^{2} \frac{d^{2}u}{d\theta^{2}} $$

This is helpful, as we can re-write the original differential equation using these terms. I am going to skip over the algebraic manipulation, as I don't think it is terribly productive. If you would like to see it, I will say just do it yourself, it's not particularly difficult. However, here is what it ends up becoming.

$$ \frac{d^{2}u}{d\theta^{2}} + u = \frac{-1}{L^{2}} \frac{d\Phi_{\text{K}}}{du} = \frac{GM}{L^{2}} $$

Now this is a differential equation I can solve (and much easier than what it was before). Working through this, the characteristic equation has imaginary roots thus the solution to this differential question will a combination of sines and cosines. Since the differential equation is equal to a constant, the particular solution will just be equal to that. Putting it together, the solution to this differential equation is as follows.

$$ u(\theta) = c_{1}\cos{\theta} + c_{2}\sin{\theta} + \frac{GM}{L^{2}} $$

Using the initial conditions, we can remove one of these trig functions. Being careful, we can set our starting position of the orbit to be at it's closest when $\theta = 0$. This means we want to minimize $r$ at this point, which is maximizing $u$. Similarly, since this is an orbit, we want $\theta = 2\pi$ to be the same point. Both of these conditions outline exactly what cosine does, and thus we can eliminate the sine term. Doing an extra bit of algebraic manipulation we get the following.

$$ \frac{1}{r} = \frac{GM}{L^{2}} (1 + e\cos(\theta)) $$

Where $e$ is just a constant (this will end up being the eccentricity). Before finally finishing, the book does this extra step and introduces a constant $a$ which is defined in the following way.

$$ a = \frac{L^{2}}{GM(1-e^{2})}, \quad L^{2} = GMa(1 - e^{2}) $$

Adding in this into our equation of motion, and using some algebraic manipulation to solve for $r$ we get the following.

$$ r(\theta) = \frac{a(1 - e^{2})}{1 + e\cos(\theta)} $$

This is our final result. Or at least my final result. This specific solution just works for where the starting condition of the orbit is at the periapsis. A more general solution would be to have another integration constant inside of the cosine part of the function. Regardless, this can be shown to be an elliptical orbit when $0 < e < 1$ and hyperbolic when $e > 1$ and parabolic when $e = 1$. This is the equation I will use in the program I made for this section.

## Description of Project
Alright, so I think I tried a little too hard on this one? Either that or it was just enough. Regardless, I am kinda happy with the end result.

Since this section was dedicated to describing and deriving Kepler Orbits, I figured that a good program to make would be one that actually showcases these orbits. After deriving the equations of motion, there ended up being three cases, namely energy less than zero, energy greater than zero, and energy equal to zero. The program I built showcases two of these cases, mainly because I forgot the last case (where the orbital path is parabolic).

My thought for direction on this was two parts: a plot that showed an animation of the orbital path, and a GUI interface that initializes the values for the plot. For the plot, I chose to use the library matplotlib with contributions from the numpy library. For the GUI interface, I used the library Tkinter, which also allowed for some compatibility with matplotlib so I could combine the two.

### Alpha Version
Going into this particular project, I knew nothing about Tkinter (besides its existence) and knew enough about matplotlib to make a plot, but not how to animate it. So this particular part needed a lot of learning. To do this, I created a test file (aptly named test.py). 

I'll go into the particulars of the manipulation of the equations of motion later, as for now I want to talk about what this file is. This file contains the animation of a specific Kepler orbit (I don't remember which one), which I used to learn how to animate in matplotlib without the worry about the GUI. I left this file in here mainly because I wanted to leave a breadcrumb trail as to how I went about creating the project overall. 

Anyway, let's talk about what the program actually contains.

### Plotting Kepler Orbits in Matplotlib
The set up for this program is rather simple. We consider an object with fixed mass $M$ which sits at the origin of our plot. We want to consider the path of a test partial with negligible mass when it is dropped on a specific point around this fixed mass. 

#### Set Up

Setting up the constants are easy, as I just choose a mass of $10^{16}kg$ to sit in the center and used the gravitational constant $G$ to keep things nice and neat. However, we need the equation of motion of a particle in orbit before we can move on. Since around half of this section is dedicated to deriving the equation of motion for a Kepler orbit, it also happens to have the orbit itself neatly outlined, which for clarity can be seen below.

$$ r = \frac{a(1-e^{2})}{1 + e \cos{f}} $$

We can be a bit tricky and have $r$ be a function of $f$ (where $r$ is the distance from the fixed mass and $f$ is true anomaly). I create the graph where the periapsis was always to the right of the fixed mass ($\cos(0) = 1$). However, there are a few unknowns that we have to solve in order to actually start plotting. These unknowns are $a$ and $e$ from the equation of motion (semimajor axis and eccentricity respectfully). 

To combat this, I gave the program two initial values: the energy of the system and the starting distance of the periapsis from the origin. Using these two starting values, we can find the values for this unknowns. The first we will look for is $a$. The book derives the following relation between $a$ and $E$.

$$ E = \frac{-GM}{a} $$

Using some quick re-arranging, we can yield the following.

$$ a = \frac{-GM}{E} $$

With one unknown found, we can use its value to find the other. To solve for the eccentricity, we can plug in our initial conditions for simulation ($r=r_{0}$ and $f = 0$) into our equation of motion.

$$ r_{0} = \frac{a(1 - e^{2})}{1 + e \cos{0}} $$

Here is where our choice of having $f$ be 0 is helpful, as we can re-write this equation as follows.

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
This is the last part of the program, and took around half of the time to create. I wanted a GUI that took in starting values for my program. The library I chose to use was Tkinter, because I saw that it had easy embedding of matplotlib figures. I didn't spend much time on design, as the space was cramped and I wasn't entirely sure what I was doing. I created some instruction labels at the top for people to read, and added in text boxes for people to put their starting values. Just for fun, I added in two radio buttons that determined the starting position of the particle as well. 

To make things just a bit spicier, I added a try/except block so that the program wouldn't crash if the user gave an incorrect response. If any error did show up, then a big red label appeared and told the user to try again. I also added a button at the bottom of the interface that started the simulation. All this did was remove all of the widgets on the screen and replaced it with the simulation I wanted to see (the orbit). I did not create a button to go back to the start however, so the user has to restart the program when the simulation starts.

## Reflecting Thoughts
As mentioned before, I think this project got a little too ambitious. It required I learn two new Python concepts that I have never used in my life (matplotlib animation and creating a GUI), and made the process of finishing it rather long. That being said, I think it was a good idea to go through with both of them. The animation adds a nice flavor where you can see the particle's actual path of orbit. I like the GUI too because it adds a nice bit of polish to everything and makes it feel more like a project than just some random program. 

For all of these reasons, I am happy with how the program turned out. There are a few things that could be upgraded or "fixed". The GUI could be fixed by adding a button or option to return to the main page. On top of not sure how to do that, I also didn't feel like figuring out how to do that, and I'm fine leaving it the way it is. In terms of plotting, I wanted to make the apoapsis button have the starting position be the apoapsis instead of the radius inputted always be the periapsis. However, I couldn't figure out how to do this with any reasonable accuracy. I did have a version where it kind of worked, but everything got janky with hyperbolic motion (as apoapsis doesn't exist in that case), so I just removed the feature.

I am a little disappointed I wasn't able to figure out how to implement the collision aspect that is talked about in the final pages of the book. I believe I could have thought of something, but I didn't want to think about the idea for too hard (especially since this is going to be a long ass project if I am able to go through with it). Similarly, I wasn't able to add the case where $e=1$. In the current program, everything just breaks when this specific case happens, but I think it would have been fun to implement a parabolic orbit. 

Lastly, I am happy I chose this particular route for the program. The process helped me learn about the different processes described in the book, and made some lesser known parts more obvious. As an example, I wasn't sure why $f_{\infty}$ was defined as what it was at first. It was only when I went to fix the program for the hyperbolic orbit that I figured it out. When I tried to have an input range of $[0, 2 \pi)$ the program plotted the entire hyperbola, as it switched over to the other side when the bottom of the equation of motion flipped sign. I determined the $f$ value for when this happens and discovered that it was exactly $f_{\infty}$. There were a number of moments like this throughout this project, and I ended up learning a lot.
