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
Text3

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

GUI paragraph

detection method paragraph

overall thoughts paragraph

### Conclusing Thoughts
last test
