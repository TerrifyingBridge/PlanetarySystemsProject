# Section 1.7 - Multipole Expansion of a Potential
This section focuses on expanding the graviational potential for a massed body. It starts with centering the coordinate system to the center of mass, and pointing out how we define graviational potential between two points, and over an object. The potential is then expanded using a taylor series, which is then re-written using associated Legendre Polynomials and Spherical Harmonics. Using these relations, the book showcases the equations for the graviational monopole, dipole, and quadrapole. From here, the book focuses on the quadrapole and what it actually means. It shows that for prefectly spherical objects, this value is 0, but for oblate objects (like most celestial bodies) this is non-zero and positive. The book briefly ends by talking about how the quadrapole showcases what happens due to rotational flattening.

| Subsection of Document | Description of Subsection |
| -----------------------|---------------------------|
| [Self Imposed Exercises](#self-imposed-exercises) | An outline of any exercises I thought would be beneifical or fun to work through that relate to the section of the book, usually exercises I make for myself. |
| [Project Description](#project-description) | A description of the coding project I designed for this section of the book, as well as any relevant information I used. |
| [Reflecting Thoughts](#reflecting-thoughts) | Reflective thoughts about the chapter itself, the self imposed exercises I worked through, and the coding project I made for the section. |

## Self Imposed Exercises
This section is focused primarily on the various multipoles for the graviational potential, with heaviy emphasis on the quadrupole moment. The book mentions that these are found through observations and the inertia of the rotating body, and Appendix A tells you what the values of these moments are for each planet (and the Sun). A large reason that the quadrupole moment (and the other multipole moments as well) aren't easily determined, is because you need a density function for the object in order to find the quadrupole moment (amongst other things). 

I thought it would be fun to derive some of these quadrupole moments, and calculate an approximation to these values. I was curious how the quadrupole moment changes with different density functions, and I also wanted to see how close I could get to the measured values. For this exercise, I first used a constant density function, and then made my own linear version which was fitted to the Sun's density distribution. After this, I found the quadrupole moment through its definition, and compared them to the actual values that have been measured.

### Quick Definition
Before jumping into the actual derivations, I first want to actually point out the definition for a multipole moment. Here is where the naming convention gets a bit confusing (for me at least). The multipole moment ends up relating to a degree of a Legendre Polynomial of degree $\ell$ where $\ell$ is the power of two that relates to the multipole. For example, for a monopole we have $\ell = 0$, for a dipole we have $\ell = 1$, for a quadrupole we have $\ell = 2$ and so on. For a degree $\ell$, the multipole for that $\ell$ is as follows.

$$ J_{\ell} = \frac{-1}{MR_{p}^{\ell}} \int_{V} \boldsymbol{\rho}(\mathbf{r})P_{\ell}(\cos(\theta))r^{\ell}dV $$

For this definition, we have $M$ being the mass of the object, $R_{p}$ being the nominal radius, $\boldsymbol{\rho}(\mathbf{r}))$ being the density function for the object, and $P_{\ell}(\cos(\theta))$ being the Legendre Polynomial. For this exercise, I only concerned myself with the quadrupole moment, and thus, I only really care about the case when $\ell = 2$. Using the definition outlined above, we have the following equation for the quadrupole moment.

$$ J_{2} = \frac{-1}{MR_{p}^{2}} \int_{V} \boldsymbol{\rho}(\mathbf{r})P_{2}(\cos(\theta))r^{2}dV $$

### Oblate Spheriod Equation in Spherical Coordinates
Before jumping into the quadrupole moment, we need to do a little bit of work determining the bounds for the radial variable. We can make our lives a bit easier, as a body isn't just some random ellipsoid, it's more closely approximated through an oblated spherioid. This means that we can consider just two maximum radii (semi-major and semi-minor values) instead of three. Since a celestial body is usually rotating around a polar axis, the semi-major axis ends up being the equatorial radius and the smei-minor axis is the polar radius.

First, we need to start off with the equation of an oblate spheriod (with semi-major axis in the $xy$-plane and semi-minor axis on the $z$ axis) in cartesian coordinates. To make things a bit clear, my specific spherical coordinates system is $r$ for radial distance, $\varphi$ for azimuth / equatorial angle, $\theta$ for polar angle, $a$ for semi-major axis, and $c$ for semi-minor axis.

$$ \frac{x^{2} + y^{2}}{a^{x}} + \frac{z^{2}}{c^{2}}  = 1 $$

Now, we use the tradiational spherical coordinates for $x$, $y$, and $z$.

$$
\begin{aligned}
x &= r\sin(\theta)\cos(\varphi) \\
y &= r\sin(\theta)\sin(\varphi) \\
z &= r\cos(\theta)
\end{aligned}
$$

To determine the bounds for the radial distance, we need to plug in these values for $x$, $y$, and $z$ and solve the resulting equation for $r$. 

$$
\begin{aligned}
\frac{(r\sin(\theta)\cos(\varphi))^{2} + (r\sin(\theta)\sin(\varphi))^{2}}{a^{2}} + \frac{r^{2}\cos^{2}(\theta)}{c^{2}} &= 1 \\
\frac{r^{2}\sin^{2}(\theta)\left[\cos^{2}(\varphi) + \sin^{2}(\varphi)\right]}{a^{2}} + \frac{r^{2}\cos^{2}(\theta)}{c^{2}} &= 1 \\
r^{2}\left[\frac{\sin^{2}(\theta)}{a^{2}} + \frac{\cos^{2}(\theta)}{c^{2}}\right] &= 1 \\
r^{2}\left[c^{2}\sin^{2}(\theta) + a^{2}\cos^{2}(\theta)\right] &= a^{2}c^{2} \\
r^{2}\left[c^{2}\left(1 - \cos^{2}(\theta)\right) + a^{2}\cos^{2}(\theta)\right] &= a^{2}c^{2} \\
r^{2}\left[c^{2} - c^{2}\cos^{2}(\theta) + a^{2}\cos^{2}(\theta)\right] &= a^{2}c^{2} \\
r^{2}\left[c^{2} + \left(a^{2}-c^{2}\right)\cos^{2}(\theta)\right] &= a^{2}c^{2} \\
r^{2} &= \frac{a^{2}c^{2}}{c^{2} + \left(a^{2}-c^{2}\right)\cos^{2}(\theta)}
\end{aligned}
$$

From here, I made a decision that probably didn't help, but made things look nicer in my opinion. I didn't want to juggle around two different length variables, so I decided to re-write $a$ in terms of $c$. For rotatig celestial bodies, we always have $a \geq c$. From here, it follows that there exists some $\alpha \geq 1$ such that $a = \alpha c$. Thus, $\alpha$ just becomes the multiplier for the polar radius that relates it to the equatorial radius. While this doesn't decrease our number of variables, (still two), I think it makes it easier to keep track of. Re-writting the equation above with this in mind, we get the following.

$$
\begin{aligned}
r^{2} &= \frac{\left(\alpha^{2}c^{2}\right)c^{2}}{c^{2} + \left[\left(\alpha^{2}c^{2}\right) - c^{2}\right]\cos^{2}(\theta)} \\
r^{2} &= \frac{\alpha^{2}c^{2}}{1 + \left[\alpha^{2} - 1\right]\cos^{2}(\theta)} \\
r &= \frac{\alpha c}{\sqrt{1 + \left[\alpha^{2} - 1\right]\cos^{2}(\theta)}}
\end{aligned}
$$

I think this equation is a bit cleaner to look at than having both radii. Regardless, this the equation of the radial distance from the origin for an oblate spheriod centered at the origin (much like a celestial body). One can verify some parts of these equation as when the body is a sphere, $\alpha = 1$ and the denominator is simply 1 and gives us a constant radial distance. However, a more confident way to show this equation holds is to use it as the upper bound when finding the volume generated by this oblate spheriod. I verified this myself by going through the math and showing that it was equal to the known volume of an oblate spheriod. I will not show this proof, mainly because this section will already have a lot more math in it to come. If you want to see it, I recommend doing it yourself as an exercise (haha! now I'm giving exercises to the reader >:) ). 

### Quadrupole Moment for a Constant Density
Before trying to verify the quadrupole moment of the Sun, I wanted to first do an easier task first, which is finding the quadrupole moment for a celestial body with a constant density, namely $\boldsymbol{\rho}(\mathbf{r}) = \rho$. Having the density term just be a constant means we can take it out of our integral, and just focus on trying to solve it itself. Substituting the 2nd degree Legendre Polynomial in, we can re-write our quadrupole moment as follows.

$$ J_{2} = \frac{- \rho}{2MR_{p}^{2}} \int_{0}^{2\pi}\int_{0}^{\pi}\int_{0}^{\frac{\alpha c}{\sqrt{1 + \lambda \cos^{2}(\theta)}}} \left(3\cos^{2}(\theta) - 1\right) r^{4}\sin(\theta)drd\theta d\phi$$

I want to explain a couple steps that I skipped in setting up this integral. For starters, we are working with spherical coordinates so the integrating terms are in terms of the distance from the origin $r$, the azimuth angle $\phi$, and the polar angel $\theta$. The bounds for the azimuth and polar angle are around the entire body all together. The bounds for the azimuth angle are $0$ to $2\pi$ and for the polar angle it is $0$ to $\pi$ as you might exepct. We want to integrate $r$ for the entire body as well, but this depends on the polar angle. To compensate for this, we go to the bound for a given polar angle that we found in the previous exercise. I also added the second degree Legendre Polynomial and took out the $\frac{1}{2}$ from it and put it out front. Since we are integrating across spherical coordinates, there is an extra $r^{2}\sin(\theta)$ term that needs to be added. Lastly, I shortened down $\alpha^{2} - 1 = \lambda$ to make it easier to type and not get terms confused.

Truthfully, this integral kinda sucks to do. I will show you how I ended up solving it, but be prepared for some math. I am also going to skip a couple rather easy steps to make way for the longer and more complex parts of solving it. Speaking of, we can integrate the $\phi$ term immediately. This is because nothing actually depends on $\phi$, so we can treat everything else like a constant. Doing this integral simply adds a $2\pi$ term out front. One step we do have to take before doing anything is integrate with respect to $r$, so let's do that really quick.

$$
\begin{aligned}
& \frac{-2\pi \rho}{2MR_{p}^{2}} \int_{0}^{\pi} \left.\left(3\cos^{2}(\theta) - 1\right)\sin(\theta) \frac{r^{5}}{5} \right\vert_{0}^{\frac{\alpha c}{\sqrt{1 + \lambda \cos^{2}(\theta)}}} \\
= & \frac{-\pi \rho}{5MR_{p}^{2}} \int_{0}^{\pi} \frac{\left(3\cos^{2}(\theta) - 1\right)\sin(\theta)\alpha^{5}c^{5}}{\left(1 + \lambda \cos^{2}(\theta)\right)^{5/2}}d\theta \\
= & \frac{-\alpha^{5}c^{5}\pi \rho}{5MR_{p}^{2}} \int_{0}^{\pi} \frac{\left(3\cos^{2}(\theta) - 1\right)\sin(\theta)}{\left(1 + \lambda \cos^{2}(\theta)\right)^{5/2}} d\theta
\end{aligned}
$$

## Project Description
There were a number of iterations I went through when it came to what to actually do for this project. Eventually, I thought it would be rather neat to actually showcase the various multi-pole moments around a celestial body. Having the definition is one part, but it would be cool to have an application that shows how they effect the gravitational potential. Thus started the project for this current section. While there are technically an infinite number of multi-poles, I decided to cap mine out at 11 (starting with a monopole and ending with 2^10-pole).

This project was significantly smaller than the previous project, but it still has some important moving parts. For my description of the project, I want to break it down into two different parts. The first part of this project was my representation of the different multi-poles and the second part was the GUI that goes with the program itself.

### Groundwork For Multi-Poles
In order to program each of the multi-pole contributions, I firsted needed to figure out what each of these multi-poles were. The book has many different representations for these, but I ended up using the one derived from spherical harmonics after simplifying. This makes things a bit easier to determine which multi-pole belongs to what, as they are multiplied by their respective moments. The definition the book gives is as follows.

$$ \Phi(r, \theta) = -\frac{GM}{r}\left[1 - \sum_{\ell = 1}^{\infty}J_{\ell}\left(\frac{R_{p}}{r}\right)^{\ell}P_{\ell}\left(\cos(\theta)\right)\right] $$

Where $M$ is the mass of the object, $R_{p}$ is an arbitrary reference radius, $J_{\ell}$ is the multi-pole moment, $\ell$ is the degree of the Legendre Polynomial, and $P_{\ell}\left(\cos(\theta)\right)$ is the Legendre Polynomial itself. It should be noted that the book technically starts the sum at $\ell = 2$ instead of $1$, as it was shown earlier in the book that this value is $0$ when our origin is at the center of mass. I wanted to leave this term in here as it will show up in the program, and it would have been much harder to remove it. The book also mentions for most bodies that are symmetric about the equatorial plane, the odd multi-pole moments end up being 0 as well. My program still includes them for a showcase, even if they don't really exit.

This equation pretty much gives me what I need to plot. I want the user to provide a value for $\ell$ and I want my program to spit out what each value does. For simplicity, our units can be such that the $\frac{-GMJ_{\ell}}{r}$ term ends up being 1, as I really only want to show the difference between the maximum and mimimum for each multi-pole. That means we only need the Legendre Polynomials. These are defined as follows using the back of the book.

$$ P_{\ell}^{m}(x) = \frac{(-1)^{m}}{2^{\ell}\ell!}\left(1 - x^{2}\right)^{m/2}\frac{d^{\ell + m}}{dx^{\ell + m}}\left(x^{2}-1 \right)^{\ell} $$

This is a tad gross, but we can make life a bit easier. Our equation derived for the potential only requires us to use $\ell$ and not $m$. Thus, we can treat $m = 0$ which gives us the following relation instead.

$$ P_{\ell}(x) = \frac{1}{2^{\ell}\ell!}\frac{d^{\ell}}{dx^{\ell}}\left(x^{2}-1\right)^{\ell} $$

Unfortunately, my programming skills aren't quite good enough to make a function which implements this polynomial as is. To compensate for this, I first needed to find the actual derivative for a spcific Legendre Polynomial. However, taking this derivative is pretty gross and requires a bunch of product and chain rule. Overall, I wasn't able to find a nice squeaky clean solution. I got around this issue by first expanding out the polynomial term through binomial expansion.

$$
\begin{aligned}
P_{\ell}(x) =& \frac{1}{2^{\ell}\ell!}\frac{d^{\ell}}{dx^{\ell}} \left( \sum_{n=0}^{\ell} \binom{\ell}{n}(-1)^{n}\left(x^{2}\right)^{\ell - n} \right) \\ 
P_{\ell}(x) =& \frac{1}{2^{\ell}\ell!}\frac{d^{\ell}}{dx^{\ell}} \left( \sum_{n=0}^{\ell} \binom{\ell}{n}(-1)^{n}x^{2\ell - 2n} \right)
\end{aligned}
$$

Now this is a lot easier to take a derivative of. We can treat each term individually and take the $\ell$'th derivative of each one. Using simple power rule, we can obtain the following.

$$
\begin{aligned}
P_{\ell}(x) =& \frac{1}{2^{\ell}\ell!}\frac{d^{\ell}}{dx^{\ell}} \left( \sum_{n=0}^{\ell} \binom{\ell}{n}(-1)^{n} \frac{\left(2\ell - 2n\right)!}{\left(2\ell - 2n - \ell \right)!} x^{2\ell - 2n - \ell} \right) \\
P_{\ell}(x) =& \frac{1}{2^{\ell}\ell!}\frac{d^{\ell}}{dx^{\ell}} \left( \sum_{n=0}^{\lfloor \ell / 2 \rfloor} \binom{\ell}{n}(-1)^{n} \frac{\left(2\ell - 2n\right)!}{\left(\ell - 2n\right)!} x^{\ell - 2n} \right)
\end{aligned}
$$

And thus we have our polynomial. Before directly moving on, I wanted to point something out that I couldn't figure out how to format properly in this markdown file. The top part of the sum is $\lfloor \ell / 2 \rfloor$ (the floor function), as when $\ell - 2n \leq 0$ then the derivative would just be 0. However this is hard to actually see through the representation because the symbols are so cramped together. I wasn't sure how to fix this, and I apologize for any confusion.

### Plotting the Multi-Poles
I promise there is actual coding here. In fact, I'll prove it to you right now. The equation above provides me with all the tools I need in order to make a function for a general Legendre Polynomial. My general process ended up being two parts long: generate a list of the coefficients of the Legendre Polynomials, and use the coefficents to find the actual value when pluggin in $\cos(\theta)$ into the equation. The first part of this process was done using the following function.

```python
def generate_coefficients(degree: int) -> list[int]:
    temp_list: list[int] = []
    for n in range(degree):
        if (degree - 2 * n >= 0):
            scalar: float = math.pow(2, degree) * math.factorial(degree)
            temp_list.append(int(math.pow(-1, n) * math.comb(degree, n) * math.factorial(2 * degree - 2 * n) / (
                    scalar * math.factorial(degree - 2 * n))))
    return temp_list
```

As can be seen, I create an empty list of integers which were then filled with the coefficients found using the equation above. The biggest notable difference is the conditional inside the for loop. At the time, I was too lazy to find the actual bound for the loop and just used the conditional. I just ended up leaving it in, even though it would be much slicker code if I removed the conditional and just changed the bounds of the for loop. Moving on, now that I had a function that generates the coefficients, we can loop through this again and replace $x$ with $\cos(theta)$. The funciton for this is also what you might expect, but my explicit solution is as follows.

```python
def n_pole(degree: int, azimuth: float) -> float:
    coefficients: list[int] = generate_coefficients(degree)
    coefficients.reverse()
    val: float = np.cos(azimuth)
    temp: float = 0
    for i in range(len(coefficients)):
        temp += coefficients[i] * math.pow(val, (degree % 2) + 2 * i)
    return -temp
```

The reason why I reversed the coefficients is because the way I generated them, it was in terms of greated power of $x$ to least, but I wanted my indexing of the for loop to directly relate to the power of $x$. I could have made this loop go backwards, but I like this solution more even if it is a bit inefficient. The other point of note is that I ended up multiplying the return value by $-1$. This is because in the original definition for the specific multi-pole, they are all negative signed, so this is me compensating for that. Now with these functions, I was armed to start plotting what each of the multi-pole graphs looked like.

## Reflecting Thoughts
### Section Thoughts
This section was really rough, but was a very interestin read. The book mentions that the contents are for "graduate students and advanced undergrads" but I can confindently say I have never used Legendre polynomials or Spherical harmonics during my undergraduate career. This isn't to say I couldn't figure it out, it just required a bunch of extra reading and trying to figure out what these concepts even are. Oddly enough, the appendix in the back of the book was more helpful in understanding these concepts then looking them up on the internet. The internet was primarily focused on more math based definitions or electromagnitism. That being said, I did spend a while just trying to understand what the background was for this section.

The content itself was also pretty interesting, if hard to follow. Many equations tended to blow up in size and complexity, and had a lot of terms being shuffled around. I was mainly happy I was able to follow it as well as I did. That being said, there are some short comings to my knowledge about this section. We're reaching the point where trying to understand the background material to a decent extent is going to take a while. For example, I could focus an entire project just on Spherical harmonics or Legendre polynomials alone. However, I do not have the time to focus on these concepts too heavily. Because of this, I am trying to focus just on where they come from, and how they're defined. While I might not understand exactly how they are derived, that will have to be okay for now (especially since the appendix doesn't focus too heavily on it either). While I wish I could just learn everything, unfortunately there is a limit into how much I can while also trying to stay on topic. Overall, I liked this section a lot, even if it wasn't the most groundbreaking topic (although who knows? maybe it will become that later in the book).

### Project Thoughts
Hehe
