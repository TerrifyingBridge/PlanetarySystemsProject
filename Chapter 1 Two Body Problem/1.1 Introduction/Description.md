# Section 1.1 - Introduction
This particular section focuses on a basic outline of celestial mechanics. Like very basic. The extent of this section talks about the acceleration for a simple 2-body problem and looks at the immediate consequence of this. They mention conversation of energy and momentum, and simplifies it down to a 1-body problem. Outside of that, there isn't too much going on.
## Self Imposed Exercises
Since this is the first descriptiong, I'll explain what I plan on doing here. This book jumps over a couple of concepts it deems as too simple to emphasize (at least I think, it's not an intro book, so I don't blame Scott for not focusing on stuff like conversation of energy), so it skips them. Part of this project is to re-learn these concepts (and learn some LaTeX), so I'll choose a couple derivations or explanations to get practice with this.

Onto the general description of what I am going to do, of which there are three: conservation of angular momentum, conservation of energy, and simplification to a 1-body problem. None of these should be too difficult, just a lot of grinding algebra and vector operations. However, before we get into actually showing these, we need to make sure we have our basics outlined. For a 2-body system, our equations of motions are as follows.

$$ \frac{d^{2} \vec{r_{0}}}{d t^{2}} =  \frac{Gm_{1}(\vec{r_{1}} - \vec{r_{0}})}{|\vec{r_{1}} - \vec{r_{0}}|^{3}}, 
\quad \frac{d^{2} \vec{r_{1}}}{d t^{2}} =  \frac{Gm_{0}(\vec{r_{0}} - \vec{r_{1}})}{|\vec{r_{0}} - \vec{r_{1}}|^{3}}$$

Where $m_{0}$ and $m_{1}% are the masses of the objects, $G$ is the graviational constant, and $\vec{r_{0}}$ and $\vec{r_{1}}$ are the position vectors of the objects. These two definitions will be helpful in showing the following exercises.

### Conversation of Angular Momentum
Honestly, this one is kind of cheating, since *technically* the section shows conversation of the relative angular momentum. But I'm going to show it for the 2-body system. To start off, let's get some basic definitions. The book gives us the following equation.

$$ L_{tot}  = m_{0} \vec{r_{0}} \times \dot{\vec{r_{0}}} + m_{1} \vec{r_{1}} \times \dot{\vec{r_{1}}}$$

Where $L_{tot}$ is the total angular momentum of the system, $m_{0}$ and $m_{1}$ are the masses of the two objects, $r_{0}$ and $r_{1}$ are the position vectors of the two objects, and $\dot{\vec{r_{0}}}$ and $\dot{\vec{r_{1}}}$ are the velocity vectors of the two objects.

Alright, now to show that the angular momentum is conserved, we need to show that the time derivative is equal to 0. Using a little bit of product rule gets us the following.

$$ \frac{dL_{tot}}{dt} = m_{0} (\frac{d \vec{r_{0}}}{dt} \times \dot{\vec{r_{0}}} + \vec{r_{0}} \times \frac{d \dot{\vec{r_{0}}}}{dt}) + m_{1} (\frac{d \vec{r_{1}}}{dt} \times \dot{\vec{r_{1}}} + \vec{r_{1}} \times \frac{d \dot{\vec{r_{1}}}}{dt})$$

Gross. Trust me, it looks gross in LaTeX too. Let's use dot notation to make this look nicer.

$$ \frac{dL_{tot}}{dt} = m_{0} (\dot{\vec{r_{0}}} \ times \dot{\vec{r_{0}}} + \vec{r_{0}} \times \ddot{\vec{r_{0}}}) + m_{1} (\dot{\vec{r_{1}}} \ times \dot{\vec{r_{1}}} + \vec{r_{1}} \times \ddot{\vec{r_{1}}}) $$
