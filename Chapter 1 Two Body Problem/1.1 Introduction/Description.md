# Section 1.1 - Introduction
This particular section focuses on a basic outline of celestial mechanics. Like very basic. The extent of this section talks about the acceleration for a simple 2-body problem and looks at the immediate consequence of this. They mention conversation of energy and momentum, and simplifies it down to a 1-body problem. Outside of that, there isn't too much going on.

I will first go over the self imposed exercise I thought would be beneficial and then move onto a description of the coding project.
## Self Imposed Exercises
Since this is the first description, I'll explain what I plan on doing here. This book jumps over a couple of concepts it deems as too simple to emphasize (at least I think, it's not an intro book, so I don't blame Scott for not focusing on stuff like conversation of energy), so it skips them. Part of this project is to re-learn these concepts (and learn some LaTeX), so I'll choose a couple derivations or explanations to get practice with this.

Onto the general description of what I am going to do, of which there are two: conservation of angular momentum and conservation of energy. None of these should be too difficult, just a lot of grinding algebra and vector operations. However, before we get into actually showing these, we need to make sure we have our basics outlined. For a 2-body system, our equations of motions are as follows.

$$ \frac{d^{2} \vec{r_{0}}}{d t^{2}} =  \frac{Gm_{1}(\vec{r_{1}} - \vec{r_{0}})}{|\vec{r_{1}} - \vec{r_{0}}|^{3}}, 
\quad \frac{d^{2} \vec{r_{1}}}{d t^{2}} =  \frac{Gm_{0}(\vec{r_{0}} - \vec{r_{1}})}{|\vec{r_{0}} - \vec{r_{1}}|^{3}}$$

Where $m_{0}$ and $m_{1}$ are the masses of the objects, $G$ is the gravitational constant, and $\vec{r_{0}}$ and $\vec{r_{1}}$ are the position vectors of the objects. These two definitions will be helpful in showing the following exercises.

### Conversation of Angular Momentum
Honestly, this one is kind of cheating, since *technically* the section shows conversation of the relative angular momentum. But I'm going to show it for the 2-body system. To start off, let's get some basic definitions. The book gives us the following equation.

$$ L_{tot}  = m_{0} \vec{r_{0}} \times \dot{\vec{r_{0}}} + m_{1} \vec{r_{1}} \times \dot{\vec{r_{1}}}$$

Where $L_{tot}$ is the total angular momentum of the system, $m_{0}$ and $m_{1}$ are the masses of the two objects, $r_{0}$ and $r_{1}$ are the position vectors of the two objects, and $\dot{\vec{r_{0}}}$ and $\dot{\vec{r_{1}}}$ are the velocity vectors of the two objects.

Alright, now to show that the angular momentum is conserved, we need to show that the time derivative is equal to 0. Using a little bit of product rule gets us the following.

$$ \frac{dL_{tot}}{dt} = m_{0} (\frac{d \vec{r_{0}}}{dt} \times \dot{\vec{r_{0}}} + \vec{r_{0}} \times \frac{d \dot{\vec{r_{0}}}}{dt}) + m_{1} (\frac{d \vec{r_{1}}}{dt} \times \dot{\vec{r_{1}}} + \vec{r_{1}} \times \frac{d \dot{\vec{r_{1}}}}{dt})$$

Gross. Trust me, it looks gross in LaTeX too. Let's use dot notation to make this look nicer.

$$ \frac{dL_{tot}}{dt} = m_{0} (\dot{\vec{r_{0}}} \times \dot{\vec{r_{0}}} + \vec{r_{0}} \times \ddot{\vec{r_{0}}}) + m_{1} (\dot{\vec{r_{1}}} \times \dot{\vec{r_{1}}} + \vec{r_{1}} \times \ddot{\vec{r_{1}}}) $$

We can simplify this further. Any vector crossed with itself is simply equal to 0, so we can eliminate two terms.

$$ \frac{dL_{tot}}{dt} = m_{0} \vec{r_{0}} \times \ddot{\vec{r_{0}}} + m_{1} \vec{r_{1}} \times \ddot{\vec{r_{1}}} $$

Now using the equations from earlier, we can replace the acceleration terms. I am going to skip a step and also move all scalar terms to the outside that can be factored out. Especially since I think that nothing will be learned from spending an entire step focusing on it.

$$ \frac{dL_{tot}}{dt} = \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} (\vec{r_{0}} \times (\vec{r_{1}} - \vec{r_{0}}) + \vec{r_{1}} \times (\vec{r_{0}} - \vec{r_{1}})) $$

Distributing these cross products around give us the following.

$$ \frac{dL_{tot}}{dt} = \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} (\vec{r_{0}} \times \vec{r_{1}} - \vec{r_{0}} \times \vec{r_{0}} + \vec{r_{1}} \times \vec{r_{0}} + \vec{r_{1}} \times \vec{r_{1}}) $$

An important note, swapping the order of the cross product will result in a change in sign. So $ \vec{r_{0}} \times \vec{r_{1}} = -\vec{r_{1}} \times \vec{r_{0}} $. Eliminating cross products that equate to 0 and using this property, we get the following.

$$ \frac{dL_{tot}}{dt} = \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} (\vec{r_{0}} \times \vec{r_{1}} - \vec{r_{0}} \times \vec{r_{1}}) $$

These two terms cancel, and give us the final result.

$$ \frac{dL_{tot}}{dt} = 0 $$

Thus, angular momentum is conserved.

### Conservation of Energy
Alright, so I'm really glad I did this one. This required me to brush up and re-learn some vector calculus that I forgot about. Before we start with showing how energy is conserved, I want to first showcase two different equations for vector derivation. One important equation we will use for this task is the derivative of the magnitude of a vector. To demonstrate this, I will use the vector $\vec{v}$. We will use the dot product definition for magnitude, namely:

$$ |\vec{v}|^2 = \vec{v} \cdot \vec{v}, \quad |\vec{v}| = \sqrt{\vec{v} \cdot \vec{v}} $$

#### Derivative of the Magnitude Squared of a Vector
Let's re-write our current derivative using the definition stated above, and then apply product rule.

$$ \frac{d |\vec{v}|^{2}}{dt} = \frac{d}{dt} (\vec{v} \cdot \vec{v}) $$
$$ = \frac{d \vec{v}}{dt} \cdot \vec{v} + \vec{v} \cdot \frac{d \vec{v}}{dt} $$
$$ = \dot{\vec{v}} \cdot \vec{v} + \vec{v} \cdot \dot{\vec{v}} $$
$$ = 2 \vec{v} \cdot \dot{\vec{v}} $$

#### Derivative of the Reciprocal of the Magnitude of a Vector
Similar to above, we will re-write our derivative using the definition stated earlier, and then apply a mix of product and chain rule.

$$ \frac{d}{dt} (\frac{1}{|\vec{v}|}) = \frac{-\frac{d |\vec{v}|}{dt}}{|\vec{v}|^{2}} $$
$$ = \frac{-1}{|\vec{v}|^{2}} \frac{d}{dt} (\sqrt{\vec{v} \cdot \vec{v}}) $$
$$ = \frac{-1}{|\vec{v}|^{2}} \Big[ \frac{1}{2} (\vec{v} \cdot \vec{v})^{\frac{-1}{2}} \frac{d}{dt} (\vec{v} \cdot \vec{v}) \Big] $$
$$ = \frac{-1}{|\vec{v}|^{2}} \Big[ \frac{1}{2} \frac{1}{\sqrt{\vec{v} \cdot \vec{v}}} (2 \vec{v} \cdot \dot{\vec{v}}) \Big] $$
$$ = \frac{-1}{|\vec{v}|^{2}} \frac{\vec{v} \cdot \dot{\vec{v}}}{|\vec{v}|} $$
$$ = \frac{-(\vec{v} \cdot \dot{\vec{v}})}{|\vec{v}|^{3}} $$

I promise this is important.

#### Actually Showing Energy Conservation
Alright, now that we have those equations under our belt, let's get the definition of total energy down.

$$ E_{tot} = \frac{1}{2} m_{0} |\dot{\vec{r_{0}}}|^{2} + \frac{1}{2} m_{1} |\dot{\vec{r_{1}}}|^{2}  - \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|}$$

Like last time, in order to determine if energy is conserved, we need to show that the derivative with respect to time for energy is equal to zero. So let's start.

$$ \frac{d E_{tot}}{dt} = \frac{1}{2} m_{0} \frac{d |\dot{\vec{r_{0}}}|^{2}}{dt} + \frac{1}{2} m_{1} \frac{d |\dot{\vec{r_{1}}}|^{2}}{dt} - \frac{d}{dt} \Big( \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|} \Big)$$

Neat. Fun long equation. Anyway, now we can use those derivations for the magnitudes of the vectors, just substituting our position / velocity vectors in for $\vec{v}$.

$$ \frac{d E_{tot}}{dt} = \frac{1}{2} m_{0} (2\dot{\vec{r_{0}}} \cdot \ddot{\vec{r_{0}}}) + \frac{1}{2} m_{1} (2\dot{\vec{r_{1}}} \cdot \ddot{\vec{r_{1}}}) - G m_{0} m_{1} \Big[ \frac{-1}{|\vec{r_{1}} - \vec{r_{0}}|^{2}} \frac{\vec{r_{1}} - \vec{r_{0}}}{|\vec{r_{1}} - \vec{r_{0}}|} \cdot \frac{d}{dt} \Big(\vec{r_{1}} - \vec{r_{0}} \Big) \Big] $$
$$ = m_{0} (\dot{\vec{r_{0}}} \cdot \ddot{\vec{r_{0}}}) + m_{1} (\dot{\vec{r_{1}}} \cdot \ddot{\vec{r_{1}}}) + G m_{0} m_{1} \Big[ \frac{1}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} (\vec{r_{1}} - \vec{r_{0}}) \cdot (\dot{\vec{r_{1}}} - \dot{\vec{r_{0}}}) \Big] $$

Not so bad, but here are where things get a big gross. Our next step is to substitute our acceleration vector with acceleration due to gravity. I am also going to move all constants that can be factors out to the front, as I don't believe spending the extra step to showcase it is really helpful or insightful.

$$ \frac{d E_{tot}}{dt} = \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} \Big[ \dot{\vec{r_{0}}} \cdot (\vec{r_{1}} - \vec{r_{0}}) + \dot{\vec{r_{1}}} \cdot (\vec{r_{0}} - \vec{r_{1}}) + (\vec{r_{1}} - \vec{r_{0}}) \cdot (\dot{\vec{r_{1}}} - \dot{\vec{r_{0}}}) \Big] $$
$$  = \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} \Big[ \dot{\vec{r_{0}}} \cdot (\vec{r_{1}} - \vec{r_{0}}) - \dot{\vec{r_{1}}} \cdot (\vec{r_{1}} - \vec{r_{0}}) + (\dot{\vec{r_{1}}} - \dot{\vec{r_{0}}}) \cdot (\vec{r_{1}} - \vec{r_{0}}) \Big] $$
$$  = \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} \Big[ \dot{\vec{r_{0}}} \cdot (\vec{r_{1}} - \vec{r_{0}}) - \dot{\vec{r_{1}}} \cdot (\vec{r_{1}} - \vec{r_{0}}) + \dot{\vec{r_{1}}} \cdot (\vec{r_{1}} - \vec{r_{0}}) - \dot{\vec{r_{0}}} \cdot (\vec{r_{1}} - \vec{r_{0}}) \Big] $$

All of these dot products end up canceling each other out. This leaves us with the following conclusion.

$$ \frac{d E_{tot}}{dt} = 0 $$

Thus, energy is conserved.

## Description of Project
This section of the chapter was focused on the basics of equations of motion for a 2-body system. Because of this, I figured it would be fun to create a simulation of a two body system using the equations of motion outlined. As mentioned this was done through the Python programming language, which meant my knowledge of GUI interface and animation was limited. While this is probably far from ideal, I ended up using PyGame to simulate these physics, as it has a rather straightforward update loop, and it is easy to control the fps. My plan was to have two different bodies, modeled as circles on the screen, and each would act on each other through gravity. 

### Set Up
Before jumping into actually making the planets and the dynamics work, I first created two different types of classes to work with: 2D Vectors and Celestial Objects. This step is a big unneeded as given how small the program ended up being, but I wanted to get some practice in using Python classes.
#### 2D Vectors
This was done in another Python file for organization. A 2D vector is simply a vector object that stores two variables x and y. This object comes with a number of methods such as adding, subtracting, multiplying by a scalar, normalizing, and getting the magnitude. Doing it this way allowed me to write the parts of the vector as pos.x and pos.y instead of pos[0] and pos[1] (for a vector named pos). I believe this looks a lot cleaner, and the methods for the vectors were very helpful many times throughout this project. 

Also, I used 2D vectors as both objects will remain in the xy-plane. Technically they are 3D vectors, but with the z coordinate being 0. This is more relevant when finding the angular momentum, as this fact is rather implied, so I wanted to mention it now.
#### Objects
This was also done in another Python file that only contains class. The class does not contain much, simply just the position and velocity vectors for the object, along with its mass and color. There are only two methods for this, and these are just for PyGame to update them. The update method applies a gravitational force for each tick, and then uses that to update velocity and position. The draw method simply draws a circle where the object is. One design choice that should be noted is that the gravitational constant was increased by a factor of 10^4. My comment mentions that this is just increasing the units to a "tick" where one tick is equivalent to 600 seconds, which isn't entirely true, but close enough.

### Putting Everything Together
To start, I created two celestial objects, which I will refer from now on as planets, with coordinates near the center of the screen. One of the planets is 100 times larger than the other, while the smaller one has an initial velocity. This was because I wanted the program to showcase one planet orbiting around the other, while keeping the masses close enough that the other planet would wobble a little bit. Later in the loop, I put the update methods for each of the planets to apply their force. After this, the planets are drawn in the same draw loop. 

### Extra Functions
The last implementation I wanted to add was various functions for values I wanted to see updated as the program ran. These values are as follows: Total Energy, Total Angular Momentum, and Center of Mass. All of these values are calculated as stated above (except for the center of mass, which I'm not going to define as it's just the weighted average of the positions of the two planets) using functions created at the beginning of the program. Later on, during the draw loop, the program calculates these values for each tick and prints them to the screen. For simplicity, I tried to keep these values to around 3-4 significant figures.

## Reflecting Thoughts
Overall, I'm rather happy with how this turned out. The planets were able to orbit each other in the way I wanted them to, and nothing truly terrible happened. I had a bunch of other ideas to make the project longer (ex: having a prompted for the GUI that let the user pick the starting values for the planets), but I remembered that I'm trying to keep these projects small (since there will be a lot). There are a few things that don't work terribly well, such as collision as I didn't add any. When the planets get too close, their distrance goes to 0, which means their force blows up. I didn't really want to fix this (and it isn't really important), so for now it's a fun little feature. 

Some other problems come with the values being printed (energy, angular momentum, and CoM), as they vary more than they should. Theoretically, they should all remain constant but instead change by about a factor of 25% except for the CoM which slightly drifts. Part of this problem is of course floating point error, however, this wouldn't account for that large of a factor. I believe the rest is explained that the orientation of the planets and velocities creates a situation where the system itself is moving and has it's own energy. Thus this would be included in the calculations and cause extra variation. Either that or I implemented it incorrectly. Either could work.

All in all, I had a lot of fun with this, and hopefully will be able to move on without getting too distracted!
