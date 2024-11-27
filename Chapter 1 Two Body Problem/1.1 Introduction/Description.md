# Section 1.1 - Introduction
This particular section focuses on a basic outline of celestial mechanics. Like very basic. The extent of this section talks about the acceleration for a simple 2-body problem and looks at the immediate consequence of this. They mention conversation of energy and momentum, and simplifies it down to a 1-body problem. Outside of that, there isn't too much going on.

I will first go over the self imposed exerices I thought would be benifical and then move onto a description of the coding project.
## Self Imposed Exercises
Since this is the first descriptiong, I'll explain what I plan on doing here. This book jumps over a couple of concepts it deems as too simple to emphasize (at least I think, it's not an intro book, so I don't blame Scott for not focusing on stuff like conversation of energy), so it skips them. Part of this project is to re-learn these concepts (and learn some LaTeX), so I'll choose a couple derivations or explanations to get practice with this.

Onto the general description of what I am going to do, of which there are two: conservation of angular momentum and conservation of energy. None of these should be too difficult, just a lot of grinding algebra and vector operations. However, before we get into actually showing these, we need to make sure we have our basics outlined. For a 2-body system, our equations of motions are as follows.

$$ \frac{d^{2} \vec{r_{0}}}{d t^{2}} =  \frac{Gm_{1}(\vec{r_{1}} - \vec{r_{0}})}{|\vec{r_{1}} - \vec{r_{0}}|^{3}}, 
\quad \frac{d^{2} \vec{r_{1}}}{d t^{2}} =  \frac{Gm_{0}(\vec{r_{0}} - \vec{r_{1}})}{|\vec{r_{0}} - \vec{r_{1}}|^{3}}$$

Where $m_{0}$ and $m_{1}$ are the masses of the objects, $G$ is the graviational constant, and $\vec{r_{0}}$ and $\vec{r_{1}}$ are the position vectors of the objects. These two definitions will be helpful in showing the following exercises.

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

Now using the equations from earlier, we can replace the accerlation terms. I am going to skip a step and also move all scalar terms to the outside that can be factored out. Especially since I think that nothing will be leanred from spending an entire step focusing on it.

$$ \frac{dL_{tot}}{dt} = \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} (\vec{r_{0}} \times (\vec{r_{1}} - \vec{r_{0}}) + \vec{r_{1}} \times (\vec{r_{0}} - \vec{r_{1}})) $$

Distributing these cross products around give us the following.

$$ \frac{dL_{tot}}{dt} = \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} (\vec{r_{0}} \times \vec{r_{1}} - \vec{r_{0}} \times \vec{r_{0}} + \vec{r_{1}} \times \vec{r_{0}} + \vec{r_{1}} \times \vec{r_{1}}) $$

An important note, swapping the order of the cross product will result in a change in sign. So $\vec{r_{0}} \times \vec{r_{1}} = -\vec{r_{1}} \times \vec{r_{0}} $. Eliminating cross products that equate to 0 and using this property, we get the following.

$$ \frac{dL_{tot}}{dt} = \frac{G m_{0} m_{1}}{|\vec{r_{1}} - \vec{r_{0}}|^{3}} (\vec{r_{0}} \times \vec{r_{1}} - \vec{r_{0}} \times \vec{r_{1}}) $$

These two terms cancel, and give us the final result.

$$ \frac{dL_{tot}}{dt} = 0 $$

Thus, angular momentum is conserved.

### Conservation of Energy
Alright, so I'm really glad I did this one. This required me to brush up and re-learn some vector calculus that I forgot about. Before we start with showing how energy is conserved, I want to first showcase two different equations for vector derivation. One important equation we will use for this task is the derivative of the magnitude of a vector. To demonstrate this, I will use the vector $\vec{v}$. We will use the dot product definition for magnitude, namely:

$$ |\vec{v}|^2 = \vec{v} \cdot \vec{v}, \quad |\vec{v}| = \sqrt{\vec{v} \cdot \vec{v}} $$

#### Derivative of the Magnitude Squared of a Vector
Let's re-write our current derivatrive using the definition stated above, and then apply product rule.

$$ \frac{d |\vec{v}|^{2}}{dt} = \frac{d}{dt} (\vec{v} \cdot \vec{v}) $$
$$ = \frac{d \vec{v}}{dt} \cdot \vec{v} + \vec{v} \cdot \frac{d \vec{v}}{dt} $$
$$ = \dot{\vec{v}} \cdot \vec{v} + \vec{v} \cdot \dot{\vec{v}} $$
$$ = 2 \vec{v} \cdot \dot{\vec{v}} $$

#### Derivative of the Reciprocal of the Magnitude of a Vector
Similar to above, we will re-write our derivative using the defnition stated earlier, and then apply a mix of product and chain rule.

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
