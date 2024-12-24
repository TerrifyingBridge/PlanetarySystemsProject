# Section 1.5 - Units and Reference Frames
This section briefly goes over the various units and reference frames that we use when observing the universe / solar system. The book starts off by talking about how we keep track of time in astronomy, then transitions into talking about how we measure distance. During this moment, the book also gives background as to why the units are what they are. The book finishes this section by talking about the reference frame we use for a coordinate system when talking about other objects in the universe.

Due to how small this section ended up being, along with the general content, there will be no self imposed exercises for this section. The section was mostly general justification for the units as well as what they are, and I couldn't figure out a good idea for what to do. I figure that instead of bashing my head against a wall trying to figure out what to do, I would just move on since the later sections of this chapter are a lot more intense.

| Subsection of Document | Description of Subsection |
| -----------------------|---------------------------|
| [Project Description](#project-description) | A description of the coding project I designed for this section of the book, as well as any relevant information I used. |
| [Concluding Thoughts](#concluding-thoughts) | Reflective thoughts about the chapter itself, the self imposed exercises I worked through, and the coding project I made for the section. |

## Project Description
Like the self imposed exercise section, I could not think of a true project I could do for this section, which I more or less knew going in. I did want to do something, so I figured I would create a code list of important constants to use whenever I need to. The values I put into this small databse will be a compilation of Appendix A for the text book I am using. I figure this way, I can reference this Python file instead of having to constantly redefine variables with these constant values.

### Constants.py
To achieve this goal, I create a new Python file named ```constants.py``` which hosts all of these values. The book breaks up Appendix A into different sections (solar constants, planet constants, etc.), and I wanted to be able to do a similar thing with my file. To achieve this, I created different Python classes for each section, then made each constant a class variable so it could be easily referenced. An example of this code can be seen below for my Venus class.

```python
class Venus:
    semi_major_axis = 0.72334
    eccentricity = 0.00678
    inclination = 3.39
    orbital_period_days = 224.701
    orbital_period_years = 0.61520
    mass_parameter = 3.24859e14
    mass = 4.86731e24
    sun_planet_mass_ratio = 408523.7
    spin_period = 243.018
    obliquity = 177.36
    moment_of_inertia_1 = 0.342
    moment_of_inertia_2 = 4.461e-6
    moment_of_inertia_3 = 2.171e-6
    gravitational_love_number = 0.307
    mean_radius = 6052
    reference_radius = 6051
```

This way, if I ever needed the semi-major axis for Venus, all I would have to type is ```Venus.semi_major_axis``` and the file would give me exactly that. I believe that this format looks a lot cleaner and will make future coding projects a lot easier to read when I invoke any constants I may need. This constant file was also safely stored in the Helpers directory, as I plan on using it in future projects whenever it is needed. However, this made my Section 1.5 directory very empty, so to prove that I did actual coding, I kept the main copy I was working on inside this current directory. There isn't any code to run for this project, just the creation of a database.

## Concluding Thoughts
Since there isn't much going in, I figured that this section doesn't need to be broken down into subsections, especially since I don't have too much to say. The actual section itself was rather interesting, and I enjoyed getting a bit more context for why a lot of academia does what it does. Not a lot was terribly new to me, but I still learned a little bit more about the topic, such as ideally using a mass paramter instead of a derived mass and gravitational constant. I feel like this section was an important aside, but not one that fit cleanly anywhere so it became its own section. 

I am not terribly happy calling this one a project for what it's worth. I am happy I went through the process to actually put these values into a Python file, but besides that I am a little bummed I wasn't able to think of an actual idea. However, not everything in the book can be interesting enough to force a project out of it, and the book was not made with having a coding project in mind for each section. I believe I did the best I could with what I had, and it gives me more time to focus on the more interesting chapters rather than getting hung up on something that isn't worth a however many hour project.

My biggest fear with allowing myself no self imposed exercises or a much smaller project is that I will end up making a trend of it. I really want to keep sections like this to a minimum if possible and only gloss over a section if there is absolutely nothing to come out of it. This of course asks the question of "when does a section not give you enough?" and truthfully I do not know. I think I'm fine with this section being what it is, but moving forward I really want this to be the only section I do this with, but I am not sure how possible that is (since I haven't read the whole book). Regardless, I am going to move on to bigger and better things. Overall, it was a fun little section to work through.
