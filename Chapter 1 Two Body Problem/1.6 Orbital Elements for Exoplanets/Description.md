# Section 1.6 - Orbital Elements for Exoplanets
This section focuses on exoplanets, and what orbital elements that we can find using the different methods of exoplanet detection. Each method of detection has a rather detailed explanation about what information is given using observations and provides a small bit of background when it comes to trying to find exoplanets in the first place. In addition to this, there is also mention of the limitations of each method and what we cannot detect or measure. The book goes over four different methods for exoplanet detection: radial velocity method, transiting planet method, astrometry method, and direct imaging method. Graviational microlensing is mentioned as a method but not focused on in this section as it doesn't provide us many constraints for the orbital elements for the exoplanets. 

| Subsection of Document | Description of Subsection |
| -----------------------|---------------------------|
| [Self Imposed Exercises](#self-imposed-exercises) | An outline of any exercises I thought would be beneifical or fun to work through that relate to the section of the book, usually exercises I make for myself. |
| [Project Description](#project-description) | A description of the coding project I designed for this section of the book, as well as any relevant information I used. |
| [Reflecting Thoughts](#reflecting-thoughts) | Reflective thoughts about the chapter itself, the self imposed exercises I worked through, and the coding project I made for the section. |

## Self Imposed Exercises
When first reading this section, the parts that confused me the most were the astrometry and direct imaging coeffients, as they are mostly just stated. Assuming you can determine the wobble of a star or directly observe a planet, you can fit them the equations given and find a best value for A, B, F, and G. From there it's a matter of solving for the orbital elements once you have them. However, I wasn't sure where these coefficents come from, so I figured it that was a good place to start when it came to the self imposed challenges. For this particlar part of the file, I'll go through both the astrometry coeffients as well as the direct imaging coefficents.  

## Project Description
Since this section focused on what orbital elements we can determine from the different methods of exoplanet detection, I thought it would be fun to showcase what some of these methods looked like. I still wanted to implement the actual orbital elements though, so for each detection method I showcased, I also showed what orbital elements can be determined from them. Due to the book not including micorlensing as a method to focus on, my project implements the radial velocity, transit, astrometry, and direct imaging methods. Like in previous projects, I wanted to create a GUI to make it more digestible of a program for users.

My main goal for this was to have the user create their own two body system, and then pick their detection method from there. This does come with a weird side effect, where in order to give the stats of a system, you will already know the orbital elements of the exoplanet. However, this is a showcase, not to be used directly as a tool for any future projects. Going this route means I need to use a different method for finding the orbital path of the system. Since we're not just using an initial starting positiong and velocity, we have to go about it through a different method. To help with this task, I created a new Python file named `two_body_system.py`.

### Helper File: `two_body_system.py`
The first part of this file I want to mention is the `AstroBody` class. This is mostly just used as a glorified list, as this class doesn't contain any methods, and simply stores the mass and radius of an celestial body (star, planet, etc.). I also gave the class a position attribute, however this is never used. The code for the class can be seen below.

```python
class AstroBody:
    def __init__(self, mass: float, radius: float):
        self.mass = mass
        self.radius = radius
        self.position = v.Vector3D(0, 0, 0)
```

The real meat and potates of this Python file is the `TwoBodySystem` class. This class is meant to house any information or methods I might want that relates to a two body system. The constructor takes in six different parameters, namely the mass, radius, argument of periapsis, eccentricity, initial separation distance, and inclination. To make my life a bit easier, all orbits in this simulation start at periapsis. Another assumption is that the ascending node is simply always defined to be 0 radians. My justification to this is because for any system, since the line of sight is always in the $z$-axis, we can rotate the $xy$-plane to simply have the ascending node along the positive $x$-axis. This of course doesn't translate well to real life (as in observations, we don't know the orientation of the system right off the bat), but it is fine for this showcase. Using this method also helps keep the argument of periapsis defined when inclination is 0 when it otherwise wouldn't be.

The constructor for this class does a decent amount, and starts off by finding some important values for the system. It finds the period of orbit, the semi-major axis (used for the simplification to a one body system), and mean motion. This constructor also initializes a bunch of lists that will be used later. I'll showcase the code for the constructor below (minus the initalizations).

```python
    def __init__(self, body1: AstroBody, body2: AstroBody, init_sep_dist: float, eccentricity: float,
                 inclination: float, peri: float):
        self.body1 = body1
        self.body2 = body2
        self.eccentricity = eccentricity
        self.inclination = inclination
        self.semi_major_axis = init_sep_dist * constants.PhysicalConstants.au / (1 - self.eccentricity)
        self.period = self.calc_period(init_sep_dist * constants.PhysicalConstants.au)
        self.mean_motion = oe.calc_mean_motion(self.semi_major_axis, int(self.body1.mass + self.body2.mass))
        self.peri = peri
```

The process for finding the orbital path from these elements is as follows.
1. Create a time array with starting time 0 seconds and final time the length of the period with even interval spacing between them
2. Traverse through the time array and look at each specific time
3. For each time value, use the mean motion to determine the mean anomaly
4. Using the mean anomaly and eccentricity, we use Kepler's equation ot find the eccentricity anomaly, which is saved in its own list for later
5. Using the eccentric anomaly, we determine the value of the true anomaly, which is saved in its own list for later
6. Using the eccentric anomaly, semi-major axis, and eccentricity, determine the current separation between the two bodies using the one body simplificaiton
7. Transform the current separation along with the unit vectors of the celestial bodies to transfer the one body simplification to the current two body problem, which tells us the position for both bodies
8. These values are then saved in their own lists for later use.

Probably doesn't sound like a lot, but the code is rather gross, and a decent amount of steps. Regardless, I implemented these steps, and plotted my first orbit. I first did this in 2D istead of 3D (which made some aspects of my code a bit messier later on). The result can be seen below.

<p align = "center">
<img src = "assets/test_orbit.gif" width="500" alt="2d orbit">
</p>

Overall, it doesn't look too bad. This is mainly due to 2D being a much simplier coordinate transformation than 3D. Next, I implemented the same code, but for 3D this time instead of 2D. I made some modifications of the code and then tried to plot the system from here. The result can be seen below.

<p align = "center">
<img src = "assets/3d_wrong_orbit.png" width = "500" alt = "bad 3d orbit">
</p>

So this isn't correct. As you can see from the figure, the star is not on the orbital plane the exoplanet is orbiting on, and it isn't at the focus. This was annoying to fix, but I did find the bug. It came from a missing parenthesis when transforming to the cartesean 3D coordinate system. Fixing the issue the plot looks as it should.

<p align = "center">
<img src = "assets/test_3d_orbit.gif" width="500" alt = "good 3d orbit">
</p>

As you can see, this is a proper 3D orbit. One thing that can't be seen very well, but I can assure you is happening, is the wobble of the star (blue body). I did try these with similarly massed objects and the result is exactly what you would expect. I wanted to bring up the parenthesis problem earlier because this part happened a lot. My lack of organization this project led to a number of just typing things incorrectly and then spending too much time trying to fix it. Regarldess, here is the code for finding the orbtial path.

```python
    def fill_path_list(self, time: np.ndarray) -> None:
        total_mass = self.body1.mass + self.body2.mass
        for step in time:
            mean_anomaly = oe.calc_mean_anomaly(0, self.mean_motion, step)
            eccentric_anomaly = oe.calc_eccentric_anomaly(mean_anomaly, self.eccentricity, 1e-10)
            self.eccentric_anomaly_path.append(eccentric_anomaly)
            true_anomaly = oe.calc_true_anomaly(self.eccentricity, eccentric_anomaly)
            self.true_anomaly_path.append(true_anomaly)
            current_sep = self.calc_radius_eccentric_anomaly(self.semi_major_axis, eccentric_anomaly)

            current_pos = v.Vector3D(np.cos(true_anomaly + self.peri),
                                     np.cos(self.inclination) * np.sin(true_anomaly + self.peri),
                                     np.sin(self.inclination) * np.sin(true_anomaly + self.peri))
            current_pos.multiply(current_sep)

            body1_pos = v.Vector3D.multiply_scalar(current_pos,
                                                   -1 * self.body2.mass / (total_mass * constants.PhysicalConstants.au))
            body2_pos = v.Vector3D.multiply_scalar(current_pos,
                                                   self.body1.mass / (total_mass * constants.PhysicalConstants.au))

            self.body1_pos_x.append(body1_pos.x)
            self.body1_pos_y.append(body1_pos.y)
            self.body1_pos_z.append(body1_pos.z)
            self.body2_pos_x.append(body2_pos.x)
            self.body2_pos_y.append(body2_pos.y)
            self.body2_pos_z.append(body2_pos.z)
```

You can see the consequence of not using vectors at the bottom of the method. Since I was alternating between 2D and 3D, I just made lists for each of the axes for both bodies, when I really should have just made 2 lists full of vectors. Oh well. Lastly, there is much more to this class than I have talked about here. This is because most of the remaining methods deal with specific detection methods that I implemented later As we look at the different detection methods, I will elaborate on the specific part of this class for that method to keep things simple.

### Radial Velocity
Radial Velocity was the first detection method I decided to work on. All detection methods each have their own test file so that it was simply a matter of copy and pasting the result into `main.py`. Because of this, the beginning code for radial velocity can be found here, while the final polished code is in `main.py`. Since each detection method goes this route, I will not directly mention this again. 

My main goal for this method was to showcase the actual orbit of the two body system, and constrast it with another graph showing the line of sight velocity of the star that is moving at the same time the orbit is. This process is rather straightforward, especially since we already have a true anomaly list for the system that was derived from an interval of time equal to the period of the orbit. From here, it is simply a matter of making another list that houses the line of sight velocity. THe book dervies what this equation is and, for clarity, this equation can be seen below.

$$ v_{\text{los}} = - \frac{m_{1}}{m_{0} + m_{1}} \left[ \frac{2\pi G(m_{0} + m_{1})}{P}\right]^{1/3}\frac{\sin(I)}{(1 - e^{2})^{1/2}}\left[\cos(f + \omega) + e\cos(\omega)\right] $$

Adding this to a list wasn't too complex either. Using the true anomaly for a certain time value, I used the above equation to find the velocity in the line of sight. From here it is just as simple as plotting it over the period of the orbit. The code / methods that directly relate to this isn't entirely interesting, so I'll leave it to you to go through the files and look, but I do want to showcase the result upon plotting / animating this graph. While the axes aren't labeled (yet), you can see the orbit of the two body system on the left and the line of sight velocity on the right. The values for this make since given the initial conditions of the orbit.

<p align = center>
<img src = "assets/rad_vel.gif" width = "700" alt = "rad_vel">
</p>

### Astrometry
The second detection method I focused on was astrometry, due to it mostly being rather simple and quick to make. The general idea behind this method is detecting the wobble of a star projected on the sky plane perpendicular to our line of sight, and how this changes over time. Given a full period, we can fit these to a linear combination of sine and cosine in terms of the true anomaly and determine the orbital elements based on the coeffients found. Since this project lives in a nice perfect world where we set the center of mass to be at (0, 0, 0), the equaiton we want to fit the star's projectoin of orbit to is as follows.

$$
\begin{aligned}
x_{0} &= -\frac{1 - e^{2}}{1 + e\cos(f)}\left(A\cos(f) + F\sin(f)\right) \\
y_{0} &= -\frac{1 - e^{2}}{1 + e\cos(f)}\left(B\cos(f) + G\sin(f)\right)
\end{aligned}
$$

Where $A$, $B$, $C$, and $D$ are the Thiele-Innes elements. What are these elements you might ask? Well you shouldn't. Go read the self imposed exercises. Regardless, because we already know the orbital elements of the exoplanet, we can find these elements pretty much exactly. Got to love the power of cheating. Regardless, 

## Reflecting Thoughts
### Section 1.6 Thoughts
This section was a lot more digestable to get through than most of the previous sections, although I am slowly coming to the conclusion that I it is me warming up to the material. I do think I was a bit harsh in the beginning when I mentioned that there were jumps in the book, because these jumps would have been trivial to those who already know and have retained a lot of physics information. As someone who has been teaching computer science for 3 years and hasn't been in a physics class in 4 years, the start (I believe) was me being rather rusty, and I believe that this section showcases that well.

I believe that this section is probably the more conceptually difficult section, but it was easy to digest and following what was happening in each subsection of the book. The only part that lost me was the astrometry coefficents, and this was more so because there was a lot of stuff in those coefficents rather than me getting stuck on why they were what they were. Truthfully, I don't have too many interesting things to say about this section because of how straightforward it was to read and understand. I did enjoy this section a lot, as I'm really interested in exoplanet research as well as their general dynamics (hence why I have this book), so I was really excited to get to this moment. Overall, it was a fun chapter, and I look forward to many more to come.

### Self Imposed Exercises Thoughts
testhaha

### Project Thoughts
Hot damn that was a large project. I am currently writting this reflection right as I finished the project so that it is fresh in my mind, although I still might take breaks between paragraphs. This project was much larger than all of my other projects and you can tell if you look at the python code. The main file alone was about 650 lines of code, and the helper file I made for this project was about 300 lines of code too. I can definitely feel some bloating going on with these projects, as each new project I get excited about seems to be just ever so larger than the one before it (with the exception being Section 1.5). It probably didn't help that there was also a lot going on in this chapter, but looking back at it, I probably could have cut one or two of the exoplanet detection methods to save time.

Speaking of large files, the helper file `two_body_system.py` which was both a large help to this project, and a little bit of a hit on my ego. I am happy I am using OOP when I can, because actually using objects is making this much easier to organize everything, even if they just become glorified lists. However, the class `two_body_system` is a mess. I made it as I went along and simply added stuff into it when I needed it, and now it is horrifically disorganized. One such example is the mish-mash of units for distances, as sometimes a variable is in meters while the other is in au. Making this file made me realize I should really try to plan these things ahead because there are methods all over the place and waaayyy too many attributes. It never became too much to keep track of, but I would want to clean that up in the future.

As much as I was not excited about the work I did during Section 1.5, I am glad I pulled through and actually did it. Having a file that just held all important constants is so much nicer as a reference that slowly importing and using the constants I need. This especially helped when making my test stars and planets, as I could just reference the Sun's stats or real planet stats. While I didn't use too many of the constants, just having it there was so nice to have. Just goes to show that even adding some small helpers can make a big difference in the future. The only part I'm not proud of is the use of the shortening the filename to `c` when it was called. I didn't really have a better idea, but I didn't exactly like that choice either.

One of the things I am most proud of in this project is how the GUI looks. It isn't perfect, and even I sometimes confuse which slider is which for the two rows at the top, but I think it looks much cleaner than the GUIs that came before. It was also nice not having to work on error handling with the text boxes. I wish I had more good things to say about the GUI, because I truly am proud of it. That being said, this was by far my least favorite part of the project. If I have learned anything making these programming projects, it's that I hate making GUIs. It isn't fun, and trying to make everything fit in the right spot just sucks. I am not sure how I can make this process go smoother, but I have a feeling it might just not be possible without investing in a program to help with, but I really want to keep my expenses on these to a minimum (money spent so far: $0).

I was the most excited about this part when I started to make this project, but it more or less dwindled as I made it. Working on radial velocity was really cool, and I loved how it turned out. Then, when I started working on direct imaging and astrometry, I realized they were pretty much the same thing (just looking at a different object), and visually not much difference between them and the actual orbit (2D projection and all that). The worst offender was the transit method. It was interesting, and I'm glad I did it, but it was by far the most challenging. Even still there are a bunch of bugs that I'm hoping no one notices before reading this paragraph. One such example is the orbital path of the planet changes depends on the figure size (which changes for each computer), and it doesn't directly corrispond with the flux chart. I am not sure how to also make the flux chart a square without screwing with the units, but I didn't feel like fixing it. This was hard, but really cool when I was able to finish it.

Overall, this project was super long and rather indictative of a trend I am noticing with each section (except for Section 1.5). Each project is getting bigger and more involved than the last, and this is starting to take me a lot longer per section. It isn't entirely fair to compare time on this one (as this one took off near the end of break, so I had to complete it while working), but this one took around 3-4 weeks. My python files are much larger and are way more involved than they normally are. While I am very happy with how this turned out, this project could be polished much more and could be a lot better. But I need to move on. Moving forward, I am going to try to limit how big these projects get, and be more okay with smaller projects such as the scope of Section 1.4 or Section 1.2.

### Conclusing Thoughts
last test
