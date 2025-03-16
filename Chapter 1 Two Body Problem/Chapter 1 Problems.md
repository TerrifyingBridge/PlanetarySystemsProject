# Chapter 1 Problems
This file will outline my solutions to the practice problems in the back of the book. Each chapter of the book has a number of different practice problems (some more than others), and I want to try my hand at solving all of them. Truthfully, I think this is very ambitious, especially since growing up I wasn't always able to finish all of the practice problems in my math text books (I probably could now, but that's a lot of work). Each of the problems for each chapter have a difficulty ranking. I will be keeping this trend as well when outlining the problems using the same notation. In case you are not aware, the book has three different difficulty ratings: 1, 2, and 3. In this book, 1 is the easiest and 3 is the hardest. The book also uses brackets to show off these ratings so they will look like this: [1]. Before jumping into it, there are a couple of things I would like to preface that will not be in the rest of the problem files for future chapters.

The problems for each chapter aren't exactly organized by the section you need to finish reading in order to solve them. For example, the first three problems in chapter 1 require you to understand section 1.3 while problem 9 can be completed upon finishing section 1.2. Because of this, my original plan was to wait until the end of the chapter to complete them. This way, I know that I had the capability to solve every problem. However, I fear that when/if I finish a chapter, I will force myself to do a bunch of problems instead of actually going through and learning the parts that I find interesting. So, I have decided to just do the problems as I see fit and whenever I feel like it. This might change as things continue but that's my current plan. 

Each problem will have a main title, and the actual problem itself. From there I will give my solution and final commentary at the end. One thing I also thought would be fun is to give my own take on the difficulty of the problems. I like to have a bit more fine measurement, so my rating scale will be a 1 through 5 scale (1 being easy and 5 being difficult), with the exception of 6 which means I wasn't able to solve it and gave up. To stand out from the book, I will place my difficulty in {} instead. Lastly, on the off chance anyone actually reads these problems besides me: **I am not always going to be able to verify if these solutions are correct**. This whole endeavor is my personal project and virtually no one is helping me, so if I can't figure it out on my own or look up a solution, I have almost no way of verifying if I am correct. I am fine with it, but I am sure someone copying me will not.

## Problem 1 - [1] {1}
> A **geosynchronous orbit** is an orbit with period equal to the spin period of the Earth. Show that a circular geosynchronous orbit has radius $r_{\text{sync}} = 42164 \text{ km}$. You may approximate the Earth as spherical and ignore the effects of the Moon and Sun. Hint: $42241 \text{ km}$ is not correct.

### My Solution
This problem isn't too bad, as it is mostly plugging values into equations and then solving for the only unknown. The only equation we really need is the following.

$$ P = 2 \pi (\frac{a^{3}}{GM_{\text{E}}})^{1/2} $$

All of these are givens, since we're working with the Earth (the book gives us the values of the Earth's period and mass in Appendix A), we can just the known values, and since the orbit we're looking for is circular, the semi-major axis and the radius are the same and thus, $r_{\text{sync}} = a$. This can be easily re-arranged for $r_{\text{sync}}$ and yields the following equation.

$$ r_{\text{sync}} = (\frac{P^{2} GM_{\text{E}}}{4 \pi^{2}}) ^ {\frac{1}{3}} $$

According to Appendix A, $P_{\text{E}} = 0.99727 \text{ days}$ and $GM_{\text{E}} = 3.986004 \times 10^{14} \text{ m}^{3} \text{s}^{-2}$ However, before plugging in these values, we have to make sure that our period is in the correct units. There are 86400 seconds in a day, so we have a simple conversion.

$$ 0.99727 \text{ days} \times 86400 = 86164.128 \text{ seconds} $$

Now we can plug in our values.

$$ r_{\text{sync}} = (\frac{(86164.128)^{2} (3.986004 \times 10^{14})}{4 \pi^{2}}) ^ {\frac{1}{3}} $$
$$ r_{\text{sync}} = (7.496024337 \times 10^{22})^{\frac{1}{3}} $$
$$ r_{\text{sync}} = 42164180.38 \text{ m}$$
$$ r_{\text{sync}} = 42164.18038 \text{ km} $$
$$ r_{\text{sync}} \approx 42164 \text{ km} $$

### My Commentary
This problem was rather simple, and was just centered around basic use of an equation. Can't say I have too much commentary besides talking about the hint mentioned, as it implies the existence of a common misunderstanding that would yield an answer of $42241 \text{ km}$ instead. That incorrect answer was easy to find, as it comes from having the period of Earth's rotation being exactly 1 day instead of 0.99727 days. Outside of that, nothing too much to say. It took my significantly longer to type this up than to actually do it.

## Problem 2 - [1] {3}
> Prove the following formulas for time averages over a bound Kepler orbit of semimajor axis $a$ and eccentricity $e$: 

$$
\begin{aligned}
\langle v^4 \rangle =& \left(\frac{GM}{a}\right)^{2} \left[4\left(1 - e^{2}\right)^{-1/2} - 3\right] \\
\langle v^{2} / r \rangle =& \frac{GM}{a^{2}} \left[2\left(1 - e^{2}\right)^{-1/2} - 1 \right] \\
\langle \left(\mathbf{r} \cdot \mathbf{v}\right)^{2} / r^{3} \rangle =& \frac{GM}{a^{2}} \left[\left(1 - e^{2}\right)^{-1/2} - 1\right]
\end{aligned}$$

### My Solution
Since this problem involves three different orbital averages, I will go through them one at a time to make things a bit more digestible. Before doing this, I think it is important to find an equation for $v$ that we will be using for the first two averages. From the book, we have these two equations.

$$
\begin{aligned}
E =&\frac{1}{2}v^{2} - \frac{GM}{r} \\
E =& -\frac{GM}{2a}
\end{aligned}
$$

Both of these equations have an $E$ in common (they are both the same energy), so we can put them equal to each other and solve for $v$. The algebra is more or less trivial, so I will show you the result I ended up using.

$$ v^{2} = GM\left(\frac{2}{r} - \frac{1}{a}\right) = \frac{GM}{ar} \left(2a - r\right) $$

Since both of the first two orbital averages contain an even power for velocity, I left my found result in terms of $v^{2}$. With this out of the way, let's move onto the orbital averages. 

#### Part (a) - Orbital Average: $\langle v^{4} \rangle$
The orbital average method I ended up using for this integral ended up being the one in terms of eccentric anomaly, which has the following definition.

$$ \langle X \rangle = \frac{1}{2\pi} \int_{0}^{2\pi}\left(1 - e \cos(u)\right)Xdu \quad = \quad \frac{1}{2\pi} \int_{0}^{2\pi} \frac{r(u)}{a} X du $$

This last part I added in to make initial simplification a bit easier to work with.  Now, let's add in our $v^{4}$ term.

$$\begin{aligned}
\langle v^{4} \rangle =& \frac{1}{2\pi} \int_{0}^{2\pi}\left(\frac{GM}{ar}\right)^{2} \left(2a - r\right)^{2} \frac{r}{a}du \\
=& \frac{1}{2\pi} \left(\frac{GM}{a}\right)^{2} \int_{0}^{2\pi} \left(\frac{4a^{2}}{r^{2}} - \frac{4a}{r} + 1\right) \frac{r}{a} du \\
=& \frac{1}{2\pi} \left(\frac{GM}{a}\right)^{2} \int_{0}^{2\pi} \left(\frac{4a}{r} - 4 + \frac{r}{a}\right)du \\
=& \frac{1}{2\pi} \left(\frac{GM}{a}\right)^{2} \left[4\int_{0}^{2\pi}\frac{a}{r}du -4\int_{0}^{2\pi}du + \int_{0}^{2\pi}\frac{r}{a}du\right]
\end{aligned}$$

Now we have three fun integrals to work with. Moving forward, I will evaluate each of these integrals individually and plug the values back in at the end. Purely because I like to start with the easier integrals first, we're going to start with the last integral and move our way forward.

$$\begin{aligned}
\int_{0}^{2\pi}\frac{r}{a}du =& \int_{0}^{2\pi}\left(1 - c\cos(u)\right)du \\
=& \left.u - e\sin(u)\right|_{0}^{2\pi} \\
=& 2\pi - e(0) - (0 - e(0))\\
=& 2\pi
\end{aligned}$$

Alright this one wasn't so bad. Let's move onto the middle integral now.

$$4\int_{0}^{2\pi} du = \left.4u\right|_{0}^{2\pi} = 4(2\pi) - 4(0) = 8\pi$$

Also not so bad. Unfortunately, these integrals do not stay this way for long. I will now evaluate the remaining integral.

$$
4\int_{0}^{2\pi} \frac{a}{r}du = 4\int_{0}^{2\pi} \frac{du}{1 - e\cos(u)}
$$

Here is where we will take a fun little substitution, where we have to do a bit of leg work to actually use.

$$ t = \tan\left(\frac{u}{2}\right) \quad \quad dt = \frac{1}{2}\sec^{2}\left(\frac{u}{2}\right)du $$

We can set up a triangle with angle $\frac{u}{2}$ and from there gather the equations for both sine and cosine.

$$ \sin\left(\frac{u}{2}\right) = \frac{t}{\sqrt{1 + t^{2}}} \quad \quad \cos\left(\frac{u}{2}\right) = \frac{1}{\sqrt{1 + t^{2}}} $$

We can find these values in terms of just the eccentric anomaly by using the double angle formula for both sine and cosine.

$$ \begin{aligned}
\sin(u) =& 2 \sin \left( \frac{u}{2} \right) \cos \left( \frac{u}{2} \right) = \frac{2t}{1 + t^{2}} \\
\cos(u) =& \cos^{2} \left(\frac{u}{2}\right) - \sin^{2} \left(\frac{u}{2}\right) = \frac{1 - t^{2}}{1 + t^{2}}
\end{aligned}$$

The last part we have to use this for is actually substituting in everything, but first, we also need to account for our $du$ term.

$$ dt = \frac{1}{2} \sec^{2} \left(\frac{u}{2}\right)du \quad \Rightarrow \quad du = 2 \cos^{2}\left(\frac{u}{2}\right)dt$$
$$ du = \frac{2}{1 + t^{2}}dt $$

Okay! Now that we have all of that prep work done, we can substitute these expressions in our integral.

$$ \begin{aligned}
4 \int \frac{du}{1 - e \cos(u)} =& 4 \int \frac{ \frac{2 dt}{1 + t^{2}} }{ 1 - e \left( \frac{1 - t^{2}}{1 + t^{2}} \right) } \\
=& 4\int \frac{2dt}{1 + t^{2} - e \left(1 - t^{2}\right)} \\
=& 8 \int \frac{dt}{\left( 1 - e \right) + \left( 1 + e \right)t^{2}} \\
=& \frac{8}{1 - e} \int \frac{dt}{1 + \frac{1 + e}{1 - e} t^{2}} \\
=& \frac{8}{1 - e} \cdot \frac{\sqrt{1 - e}}{\sqrt{1 + e}} \arctan \left(\sqrt{\frac{1 + e}{1 - e}} t\right) \\
=& \left.\frac{8}{\sqrt{1 - e^{2}}} \arctan \left( \sqrt{\frac{1 + e}{1 - e}} \tan \left( \frac{u}{2} \right) \right) \right|_{0}^{2\pi} \\
=& \frac{8}{\sqrt{1 - e^{2}}} \left[ \arctan(0) - \arctan(0) \right]
\end{aligned}$$

Before completing this, I wanted to interject for a quick note. This part initially stumped me, as it looks like that this evaluation will become $0$. However, there is a small trick going on. While the second $\arctan$ is most certainly $0$, the first one ends up being $\pi$. This is because this is looking at the part of tangent which is $0$ on the other side of the unit circle (i.e. $\sin (\pi) / \cos(\pi)$ ). While the tangent is $0$, the $\arctan$ result is simply $\pi$.

$$ \begin{aligned}
=& \frac{8}{\sqrt{1 - e^{2}}} \left[\pi\right] \\
=& 8\pi \left(1 - e^{2}\right)^{-1/2}
\end{aligned}$$

Now that we have all of the integrals evaluated, we get to put them all together.

$$ \begin{aligned}
\langle v^{4} \rangle =& \frac{1}{2\pi} \left( \frac{GM}{a} \right)^{2} \left[ 8\pi \left(1 - e^{2}\right)^{-1/2} - 8\pi + 2\pi \right] \\
=& \left( \frac{GM}{a} \right)^{2} \left[ 4 \left(1 - e^{2}\right)^{-1/2} - 3 \right]
\end{aligned} $$

Thus, our orbital average is complete.

#### Part (b) - Orbital Average: $\langle v^{2} / r \rangle$
This problem has less groundwork to go over than the previous problem did, as we already have our equation for velocity. However, this is a little bit extra we have to do, as we're working with a division of $r$. Similarly, I did this problem using the other orbital average definition, and I want to go over a little bit of that simplification. For starters, we have by definition of an orbit the following equation.

$$ r = \frac{a\left(1 - e^{2}\right)}{1 + e \cos(f)} $$

Using some algebraic manipulation, we can achieve the following from this definition.

$$ \frac{1}{\left(1 + e\cos(f)\right)^{2}} = \frac{r^{2}}{a^{2}\left(1 - e^{2}\right)^{2}} $$

Thus, we can start our orbital average using the following.

$$
\begin{aligned}
\langle v^{2} / r \rangle =& \frac{\left(1 - e^{2}\right)^{3/2}}{2\pi} \int_{0}^{2\pi} \frac{v^{2}}{r} \frac{r^{2}}{a^{2}\left(1 - e^{2}\right)^{2}} df \\
=& \frac{GM\left(1 - e^{2}\right)^{3/2}}{2\pi} \int_{0}^{2\pi} \frac{2a - r}{r^{2}a} \frac{r^{2}}{a^{2}\left(1 - e^{2}\right)^{2}} df \\
=& \frac{GM\left(1 - e^{2}\right)^{-1/2}}{2\pi a^{3}} \int_{0}^{2\pi} \left(2a - r\right)df \\
=& \frac{GM\left(1 - e^{2}\right)^{-1/2}}{2\pi a^{3}} \int_{0}^{2\pi} \left(2a - \frac{a\left(1 - e^{2}\right)}{1 + e\cos(f)}\right)df \\
=& \frac{GM\left(1 - e^{2}\right)^{-1/2}}{2\pi a^{2}} \left[\int_{0}^{2\pi} 2df - \left(1 - e^{2}\right) \int_{0}^{2\pi} \frac{df}{1 + e\cos(f)}\right]
\end{aligned}
$$

Now this isn't so bad. For the sake of getting it out of the way, let's do the first integral first.

$$ 2\int_{0}^{2\pi}df = 2\left[f\right]_{0}^{2\pi} = 4\pi $$

Truthfully, I probably could have skipped this particular integral, but I thought it would be fun to at least show. Clarity and all that. Anyway, let's do the integral we all came here for. Similar to last time, I am going to make the following substitution.

$$ t = \tan\left(\frac{f}{2}\right) \quad \quad dt = \frac{1}{2} \sec^{2}\left(\frac{f}{2}\right) $$

I am going to skip the various about of moving variables around for this integral. If you want to see it again, I encourage you to re-read that segment of the previous part for this problem. Now we have everything we need to start plugging things in.

$$ \begin{aligned}
\left(1 - e^{2}\right) \int \frac{df}{1 + e\cos(f)} =& \left(1 - e^{2}\right) \int \frac{\frac{2dt}{1 + t^{2}}}{1 + e \frac{1 - t^{2}}{1 + t^{2}}} \\
=& 2\left(1 - e^{2}\right) \int \frac{dt}{1 + t^{2} + e - e t^{2}} \\
=& 2\left(1 - e^{2}\right) \int \frac{dt}{(1 + e) + (1 - e)t^{2}} \\
=& \frac{2\left(1 - e^{2}\right)}{1 + e} \int \frac{dt}{1 + \left(\frac{1 - e}{1 + e}\right) t^{2}}\\
=& 2\left(1 - e\right) \sqrt{\frac{1 + e}{1 - e}} \arctan (\sqrt{\frac{1 - e}{1 + e}} t) \\
=& 2 \left(1 - e^{2}\right)^{1/2} \left.\arctan\left(\sqrt{\frac{1 - e}{1 + e}}\tan\left(\frac{f}{2}\right)\right)\right|_{0}^{2\pi} \\
=& 2\left(1 - e^{2}\right)^{1/2} \left[\pi - 0\right] \\
=& 2\pi\left(1 - e^{2}\right)^{1/2}
\end{aligned}$$

Like the previous problem, the first $\arctan$ term is $\pi$ since it is on the left side of the unit circle, while the other $\arctan$ term is 0 as one would expect. Now that we have both values, we can plug them into our original integral.

$$ \begin{aligned}
\langle \frac{v^{2}}{r} \rangle =& \frac{GM\left(1 - e^{2}\right)^{-1/2}}{2\pi a^{2}} \left[4\pi - 2\pi\left(1 - e^{2}\right)^{1/2}\right] \\
=& \frac{GM}{a^{2}}\left[2\left(1 - e^{2}\right)^{-1/2} - 1\right]
\end{aligned} $$

Thus, our orbital average has been solved.

### My Commentary
I loathed this problem. All three parts were horrible. Truth be told, I probably put in more work than was intended, but (in my opinion) that was not clear going in. As can be seen from my solutions above, these three problems involved some nasty and stupid integrals. Some of these tricks were the first time I've ever seen them so a lot of work went into actually trying to figure out how all these were done. I would not label these problems as the easiest difficulty, as these were some of the grossest integrals I've been asked to solve. I think a big reason my score wasn't larger was because I was trying to wager logical difficulty with perseverance, as I don't think the latter should be weighted too much. I believe that is what the author of the book was going for with his difficulty rating, as I'm sure these integrals are easy if you just look up the answer or use an integral table. For some reason that route felt super unfulfilling, and I did the monstrosity that can be seen above. I didn't like this problem.

## Problem 3 - [1] {2}
>Prove the following formulas for time averages over a bound Kepler orbit of semi-major axis $a$ and eccentricity $e$:

$$\begin{aligned}
\langle \left(a / r\right)^{4} \cos(f)\rangle =& \frac{e}{\left(1-e^{2}\right)^{5/2}}, \\
\langle \left(a / r\right)^{4} \cos^{3}(f)\rangle =& \frac{3e}{4\left(1-e^{2}\right)^{5/2}}, \\
\langle \left(a / r\right)^{4} \cos(f)\sin^{2}(f)\rangle =& \frac{e}{4\left(1-e^{2}\right)^{5/2}}, \\
\langle \left(r / a\right)^{3} \cos(f)\rangle =& \frac{-5}{8}e\left(4 + 3e^{2}\right), \\
\langle \left(r / a\right)^{3} \cos^{3}(f)\rangle =& \frac{-5}{8}e\left(3 + 4e^{2}\right), \\
\langle \left(r / a\right)^{3} \cos(f)\sin^{2}(f)\rangle =& \frac{-5}{8}e\left(1 - e^{2}\right).
\end{aligned}$$

### My Solution
This part is a bit more straightforward than the previous problem, as there isn't really any ground work we have to cover before starting except for one. Since this problem has a bunch of different sines and cosines, I decided to prove one of the integrals of a general power for cosine from $0$ to $2\pi$. This proof can be outlined in the markdown file here (come soon lol). But rather than have to derive and re-do all powers of cosine, I figured this was easier (and more fun) use of my time.

#### Part (a) - $\langle \left(a / r\right)^{4} \cos(f)\rangle$
For this part, I figured that the orbital average in terms of the true anomaly would be the easiest to evaluate. Doing so yields us the following integral.

$$\begin{aligned}
\langle \left(a / r\right)^{4} \cos(f)\rangle =& \frac{\left(1-e^{2}\right)^{3/2}}{2\pi} \int_{0}^{2\pi} \left(\frac{1 + e \cos(f)}{1 - e^{2}}\right)^{4} \frac{\cos(f) df}{\left(1 + e\cos(f)\right)^{2}} \\
=& \frac{\left(1-e^{2}\right)^{3/2}}{2\pi \left(1 - e^{2}\right)^{8/2}} \int_{0}^{2\pi} \left(1 + e\cos(f)\right)^{2}\cos(f)df \\
=& \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}} \int_{0}^{2\pi} \left(1 + 2e\cos(f) + e^{2}\cos^{2}(f)\right) \cos(f)df \\
=& \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}} \int_{0}^{2\pi} \left(\cos(f) + 2e\cos^{2}(f) + e^{2}\cos^{3}(f)\right)df
\end{aligned}$$

Here is where we invoke the properties of integrating powers of cosine. The odd powers become $0$ and the even powers are evaluated according to the equation in here (coming soon), which makes $\int_{0}^{2\pi}\cos^{2}(f) = \pi$. 

$$\begin{aligned}
=& \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}} \left[0 + 2e\pi + 0\right] \\
=& \frac{1}{\left(1 - e^{2}\right)^{5/2}} \left[e\right] \\
=& \frac{e}{\left(1-e^{2}\right)^{5/2}}
\end{aligned}$$

Thus, we have proved our orbital average.

#### Part (b) - $\langle \left(a / r\right)^{4} \cos^{3}(f)\rangle$
Like the pervious problem, I decided to use the true anomaly to solve this orbital average. Plugging in everything into the orbital average integral gives us the following.

$$\begin{aligned}
\langle \left(a / r\right)^{4} \cos^{3}(f)\rangle =& \frac{\left(1-e^{2}\right)^{3/2}}{2\pi} \int_{0}^{2\pi} \left(\frac{1+e\cos(f)}{1 - e^{2}}\right)^{4} \frac{\cos^{3}(f)df}{\left(1 + e\cos(f)\right)^{2}} \\
=& \frac{\left(1-e^{2}\right)^{3/2}}{2\pi \left(1-e^{2}\right)^{8/2}} \int_{0}^{2\pi} \left(1 + e\cos(f)\right)^{2} \cos^{3}(f)df \\
=& \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}} \int_{0}^{2\pi} \left(1 + 2e\cos(f) + e^{2}\cos^{2}(f)\right) \cos^{3}(f)df \\
=& \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}} \int_{0}^{2\pi} \left(\cos^{3}(f) + 2e \cos^{4}(f) + e^{2}\cos^{5}(f)\right)df
\end{aligned}$$ 

Here, we invoke the equations that we used before. The odd powers of cosine become $0$ and $\int_{0}^{2\pi}\cos^{4}(f) = \frac{3\pi}{4}$. Replacing these values, we get the following result.

$$\begin{aligned}
=& \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}} \left[0 + 2e \left(\frac{3\pi}{4}\right) + 0\right] \\
=& \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}} \left[\frac{3\pi e}{2}\right] \\
=& \frac{3e}{4\left(1-e^{2}\right)^{5/2}}
\end{aligned}$$

Thus, we have proven our orbital average.

#### Part (c) - $\langle \left(a / r\right)^{4} \cos(f)\sin^{2}(f)\rangle$
Like the previous two, I am using the true anomaly for this problem as well. This is because the orbital average ends up simplifying very nicely when going about simplifying the integral.

$$\begin{aligned}
\langle \left(a / r\right)^{4} \cos(f)\sin^{2}(f)\rangle =& \frac{\left(1-e^{2}\right)^{3/2}}{2\pi} \int_{0}^{2\pi} \left(\frac{1 + e\cos(f)}{1-e^{2}}\right)^{4} \frac{\cos(f) \sin^{2}(f)df}{\left(1 + e \cos(f)\right)^{2}} \\
=& \frac{\left(1-e^{2}\right)^{3/2}}{2\pi \left(1-e^{2}\right)^{8/2}} \int_{0}^{2\pi} \left(1 + e\cos(f)\right)^{2} \cos(f) \left(1 - \cos^{2}(f)\right) df \\
=& \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}} \int_{0}^{2\pi} \left(\left(1 + e\cos(f)\right)^{2}\cos(f) - \left(1 + e\cos(f)\right)^{2}\cos^{3}(f)\right)df \\
=& \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}} \int_{0}^{2\pi} \left(1 + e\cos(f)\right)^{2}\cos(f)df - \frac{1}{2\pi \left(1 - e^{2}\right)^{5/2}}\int_{0}^{2\pi} \left(1 + e\cos(f)\right)^{2} \cos^{3}(f)df \\
=& \langle \left(a / r\right)^{4} \cos(f)\rangle - \langle \left(a / r\right)^{4} \cos^{3}(f)\rangle
\end{aligned}$$

Here, we can substitute in the values we found from parts (a) and (b), as the integral is just the difference between the two values.

$$\begin{aligned}
=& \frac{e}{\left(1-e^{2}\right)^{5/2}} - \frac{3e}{4\left(1-e^{2}\right)^{5/2}} \\
=& \frac{4e}{4\left(1-e^{2}\right)^{5/2}} - \frac{3e}{4\left(1 - e^{2}\right)^{5/2}} \\
=& \frac{e}{4\left(1-e^{2}\right)^{5/2}}
\end{aligned}$$

Thus, we have proven our orbital average.

### My Commentary

## Problem 4 - [1] {1}
> Many computing languages provide the function $\text{atan2}(y, x)$, which yields the angle in radians between the positive $x$-axis and the vector from the origin to the point $(x, y)$. Find an expression for the true anomaly of a bound orbit in terms of the eccentric anomaly using this function.

### My Solution
To start this problem, consider a point in 2D space $(x, y)$. The angle between the $x$-axis and this point, let's call it $\theta$ has a couple of helpful relations with regards to the point itself. By definition, we have that $\tan (\theta) = \frac{y}{x}$ and we also have $\tan (\theta) = \frac{\sin (\theta)}{\cos (\theta)}$. While whoever you are dear reader probably already knew this, my biggest point in bringing it up is that we can simply substitute $\sin (\theta)$ for $y$ and $\cos (\theta)$ for $x$.

The biggest reason for doing this is because we can immediately use the two relations between true anomaly and eccentric anomaly that is found in the book. One could derive this themself, but the book gives it to us, so I shan't bother for this problem. Regardless, the two relations that we will focus on are the following.

$$ \cos (f) = \frac{\cos (u) - e}{1 - e \cos (u)} \quad \quad \sin (f) = \frac{(1 - e^{2})^{1/2}\sin (u)}{1 - e \cos (u)} $$

Where $f$ is the true anomaly, $u$ is the eccentric anomaly, and $e$ is the eccentricity of the orbit. From here it is rather simple to find an expression for true anomaly in terms of eccentric anomaly using the $\text{atan2}(y, x)$ function. Before we complete the final step, let's clean up some of the fractions after finding $\tan (f)$

$$
\begin{aligned}
\tan(f) &= \frac{\sin(f)}{\cos(f)} \\
&= \frac{(1 - e^{2})^{1/2}\sin (u)}{1 - e \cos (u)} \cdot \frac{1 - e \cos (u)}{\cos (u) - e} \\
&= \frac{(1 - e^{2})^{1/2}\sin (u)}{\cos (u) - e}
\end{aligned}
$$

Finally, now it is just a matter of using the $\text{atan2}(y, x)$ function to bring everything together. The solution is as follows.

$$ f = \text{atan2} \left( (1 - e^{2})^{1/2}\sin (u), \cos (u) - e \right) $$

### My Commentary
Truthfully, this problem felt way too easy and I was really worried that I didn't put enough effort into it, or just simply missed something. Especially since the book just gives us many relations between the true anomaly and eccentric anomaly I felt like I was missing something. Fortunately, this is rather easy to verify.

The problem itself invokes programming languages, so that is how I went about testing this. Before verifying my specific solution, I wanted to verify the general relations. By this point, I knew these relations weren't incorrect, but it was more so for my own sake of mind. This process had me create a 1D array full of 100 elements evenly spaced between 0 and $2 \pi$, and this became my baseline true anomaly. I then used the relation from the book that allows me to calculate the eccentric anomaly, which can be seen below.

$$ \cos(u) = \frac{\cos(f) + e}{1 + e\cos(f)} $$

From here, I created a 1D array full of zeros of the same length of the other array, and set out to fill it with the eccentric anomaly values that corresponded to the true anomaly values from the first array. To solve for all angles between 0 and $2\pi$, I used the fact that both $f$ and $u$ have to be on the same semi-circle. I also had a eccentricity variable that I changed throughout this process to make sure everything was correct (but here, it is just 0.5). The code for this part is seen below.

```python
e = 0.5
f1 = np.linspace(0, 2*np.pi, 100)
u1 = np.zeros(len(f1))

for i in range(len(f1)):
    f = f1[i]
    top = np.cos(f) + e
    bot = 1 + e*np.cos(f)
    if (0 <= f <= np.pi):
        u1[i] = np.arccos(top / bot)
    else:
        u1[i] = 2*np.pi - np.arccos(top / bot)
```

Now that this is out of the way, I wanted to go backwards. I created a copy of the eccentric anomaly array and stored it another variable (this step is unnecessary but I think it looks cleaner), and then made another 1D array of all zeros like before. I used the other cosine relation between true anomaly and eccentric anomaly and filled the array of all zeros with the corresponding true anomaly. The code for this is below.

```python
f2 = np.zeros(len(f1))
u2 = u1.copy()

for i in range(len(u2)):
    u = u2[i]
    top = np.cos(u) - e
    bot = 1 - e*np.cos(u)
    if (0 <= u <= np.pi):
        f2[i] = np.arccos(top / bot)
    else:
        f2[i] = 2*np.pi - np.arccos(top/bot)
```

From here, I took the difference in each of the values for both $\mathtt{f1}$ and $\mathtt{f2}$ to see if there was any difference. If there was a difference, then something was wrong, as they should be the same. Lo and behold, the result was exactly what one would expect.

```python
[ 0.00000000e+00 -1.05471187e-15 -5.55111512e-16 -1.72084569e-15
  3.33066907e-16 -5.55111512e-16  2.22044605e-16 -1.11022302e-16
  0.00000000e+00  6.66133815e-16 -5.55111512e-16  1.11022302e-16
 -2.22044605e-16 -1.11022302e-16  0.00000000e+00  0.00000000e+00 ...
```

Now that we have that, I wanted to verify my solution to the problem. Like last time, I made a copy of the eccentric anomaly array (just so I was using the same one), and made another array full of zeros like before. I filled this one with the true anomaly (also like before), but with using the relation I found in this problem instead. The result is the following code.

```python
u_test = u1.copy()
f_test = np.zeros(len(u_test))

for i in range(len(u_test)):
    u = u_test[i]
    f_test[i] = math.atan2((np.sqrt(1 - e**2)*np.sin(u)), np.cos(u) - e)
```

Here, I subtracted the resulting 1D array with my original 1D array I made for the true anomaly. Similar to my verification from before, I got more or less the same result.

```python
[ 0.00000000e+00 -2.16493490e-15 -8.04911693e-16 -1.38777878e-15
  2.22044605e-16 -2.22044605e-16  2.22044605e-16 -3.88578059e-16
  0.00000000e+00  7.77156117e-16 -3.33066907e-16 -1.11022302e-16
 -1.11022302e-16 -1.11022302e-16  1.11022302e-16  0.00000000e+00 ...
```

I guess this goes to show that sometimes problems are as simple as they seem. I am glad that I went through and checked my work, but truthfully, I spent more time checking my work than I did solving the original problem. I guess I am just used to being absolutely stuck on a certain problem to the point where when I find one that comes naturally to me I don't trust my own solution. I suppose it was fun checking my work, but overall, it was a pretty simple problem.

## Problem 5 - [1] {1}
> Find the maximum time that a comet on a parabolic orbit can spend inside the Earth's orbit ($r < 1 \text{au}$) during a single perihelion passage. You may ignore perturbations from the planets.

### My Solution
This problem directly references the perihelion, which indicates that we are working with the Sun as the main body of orbit. Since the orbiting body is a comet, I treated this as a massless orbiting particle around the Sun, as when compared to the Sun's values, they will be incredibly negligible. If this is an incorrect assumption, then the rest of this answer will probably be wrong.

The first order of business is to have a start to the problem. In order to get the time spent in an orbit, we have to actually have the orbit itself. Fortunately, the book provides us the equation of the distance from the center of the mass in terms of true anomaly, which is as follows.

$$ r = \frac{2q}{1 + \cos(f)} $$

Where $r$ is the disance between the particle and center of mass, $q$ is the distance of the perihelion, and $f$ is the true anomaly. In order to pursue this endevor, we need a limit on $q$. It can be shown that the smaller $q$ is, the more time the comet will spend less than 1 au from the Sun. The limit I ended up choosing was $q = R_{\odot}$ where $R_{\odot}$ is the radius of the Sun. Any closer, and the comet will crash into the Sun. 

Before plugging in values into this equation to solve for $f$, I am going to simply solve for $f$ first so we're not stuck with a bunch of numbers. Solving for $f$ in terms of $r$ and $q$ gives us this.

$$
\begin{aligned}
r =& \frac{2q}{1 + \cos(f)} \\
r + r\cos(f) =& 2q \\
r\cos(f) =& 2q - r \\
\cos(f) =& \frac{2q - r}{r} \\
f =& \cos^{-1}\left( \frac{2q - r}{r} \right)
\end{aligned}
$$

We do have to be careful on the true anomaly that we get from this equation. Inverse cosine has a range of $[0, \pi]$, while the true anomaly is defined for values outside of this range. Fortunately, this isn't a huge problem, as we only need to focus on values in this range to solve the problem. Once we get a value for true anomaly for one side of the parabolic orbit, then the other side will simply be the negative true anomaly of that. This equates to simply finding the time it takes to go from perihelion to the 1 au and multiply it by 2.

Alright, now it's number time. Full disclosure, I used a calculator for this, and I don't really feel like putting in a bunch of numbers, especially since most can be referenced easily. So, for these problems, instead of showing the numbers for each step, I will tell you what I plugged in and what it ended up being.

$$
\begin{aligned}
f_{1} &= \cos^{-1} \left( \frac{2*R_{\odot} - 1 \text{au}}{1 \text{au}} \right) \\
f_{1} &\approx 3.005098 \text{ rads}
\end{aligned}
$$

Now that we have the true anomaly at the point where the orbit is at 1 au, we can find the time by using an equation that the book mentions. The book finds an equation in terms of an initial starting time, but because we just need the difference between time (to find total time spent in an orbit), we can simply assume that $t_{0} = 0$. Because of this, I have removed this particular part from the expression. It can be seen below.

$$ \left(\frac{GM}{2q^{3}} \right)^{1/2} t = \tan\left(\frac{1}{2}f\right) + \frac{1}{3}\tan^{3}\left(\frac{1}{2}f\right) $$

Not the prettiest, but not nearly that bad either. Finding our time is just as simple as plugging all values in, and solving for $t$. Doing so yields us the following result.

$$
\begin{aligned}
t &= \left(\frac{2R_{\odot}^{3}}{GM_{\odot}}\right)^{1/2} \cdot \left(\tan\left(\frac{1}{2}f_{1}\right) + \frac{1}{3}\tan^{3}\left(\frac{1}{2}f_{1}\right) \right) \\
t &\approx 43941 \text{ sec}
\end{aligned}
$$

This is the time from the perihelion to 1 au, so in order to find the time between 1 au and the other 1 au, we simply multiply this answer by two (which we're allowed to do, because of symmetry of cosine). Thus, our final answer is as follows.

$$ t \approx 87882 \text{ sec} \approx 24.4 \text{ hours} $$

### My Commentary
I am very unsure of my answer and my general process. I believe that if those two assumptions are true, then the solution I found should be valid (unless I made a calculation error). That being said, every level 1 difficulty problem has been really easy to get through, (except for the integrals, but that's just because they're a lot of work, not really because of difficulty), so I am assuming it can't be that far off.

Regardless, this doesn't exactly match what I've found online, as the only source I've found said that this time period is a couple of days long, while my answer is about only 1 day (Earth days that is). However, the "source" was Google's AI assistant which I don't entirely trust at the moment. This trust is immediately made worse, as when I looked for resources a second time, the same Google AI mentioned a few weeks. 

Long story short, I don't entirely know if this is correct or not, but it seems to make sense to me. It was fun working with parabolic orbits. Most of my projects that deal with orbits are either elliptical or hyperbolic, so being forced to work with parabolic orbits is pretty cool. I wish there was more to do with parabolic orbits, but they don't really stand out, and probably aren't that common either.

## Problem 6 - [1] {1}
> A spacecraft travels around the Earth on a circular orbit with an altitude of 300km. The spacecraft engine can give it one or more velocity impulses $\Delta v$ 
> (a) What $\Delta v$ (in $\text{km } \text{s}^{-1})$ is needed to place the spacecraft on an orbit that escapes from the Earth's gravitational field?
> (b) The mission designers want to place the spacecraft in a geosynchronous orbit, that is, a circular orbit of radius $r_{\text{sync}} = 42164 \text{km}$ ([[Chapter 1 Problems#Problem 1 - [1] {1}|Problem 1.1]]). This can be done by two impulses, the first to place the spacecraft on an eccentric orbit with apoapsis equal to $r_{\text{sync}}$ (a **Hohmann transfer orbit** )and the second at apoapsis to circularize the orbit. What is the total $\Delta v$ required?
> (c) Suppose that the transfer to geosynchronous orbit is accomplished by a slow steady burn, so that the spacecraft spirals out on a nearly circular orbit. What is the total $\Delta v$ required?

### My Solution
#### Part (a) - Escaping Earth's Gravity
To solve this problem, we need to find both the velocity of the spacecraft when it is in the circular orbit, and the velocity of the spacecraft when it has escaped the Earth's gravitational field. Both of these problems can be done using the following equations for energy.

$$ E = \frac{1}{2} v^{2} - \frac{GM}{r} \quad \quad \quad \quad E = \frac{-GM}{2a} $$
Where $v$ is the velocity of an orbiting body, $M$ is the mass of the central object, $r$ is the distance from the central mass, and $a$ is the semi-major axis of the orbiting body. Setting both of these equations equal to each other, we can solve this equation for the velocity of the system.

$$ \begin{aligned}
\frac{-GM}{2a} =& \frac{1}{2} v^{2} - \frac{GM}{r} \\
\frac{1}{2} v^{2} =& \frac{GM}{r} - \frac{GM}{2a} \\
v^{2} =& GM \left(\frac{2}{r} - \frac{1}{a}\right) \\
v =& \sqrt{GM\left(\frac{2}{r} - \frac{1}{a}\right)}
\end{aligned}$$

However, this is only half the battle, because we need to know the escape velocity as well. As mentioned before, we can use the equation for energy to figure this out (The book also provides it, but I'm going to do the extra step). The orbit goes from an elliptical orbit to a parabolic orbit when the total energy of the System goes from negative to 0. So, to determine the escape velocity, we need to find when the total energy is equal to 0.

$$ \begin{aligned} 
\frac{1}{2} v^{2}_{\text{esc}} - \frac{GM}{r} =& 0 \\
\frac{1}{2} v^{2}_{\text{esc}} =& \frac{GM}{r} \\
v^{2}_{\text{esc}} =& \frac{2GM}{r} \\
v_{\text{esc}} =& \sqrt{\frac{2GM}{r}}
\end{aligned} $$

Alright, with these equations, we are equipped to solve this problem. In order to find the difference between the two velocities, we need to actually know both of them. We use the mass parameter for the Earth and the sum of the Earth's radius and 300km for the distance from the center of mass.

$$ v_{0} = \sqrt{\frac{GM_{\text{E}}}{R_{\text{E}} + 300\text{km}}} \quad \quad \quad \quad v_{\text{esc}} = \sqrt{\frac{GM_{\text{E}}}{R_{\text{E}} + 300\text{km}}} $$

$$ v_{0} \approx 7.73 \text{km } \text{s}^{-1} \quad \quad \quad \quad v_{\text{esc}} \approx 10.93 \text{km } \text{s}^{-1} $$

From here, we just need to take the difference by subtracting the initial velocity from the escape velocity.

$$ \Delta v \approx 10.9 - 7.73 = 3.2 \text{km } \text{s}^{-1} $$

Thus giving us our final answer.

#### Part (b) - Hohmann Transfer Orbit
This problem ends up having two parts to look at, and is more or less how I broke it down. The spacecraft travels from a small circular orbit to a very elliptical orbit, and then from an elliptical orbit to a larger circular orbit. To solve this problem, you have to find the $\Delta v$ of the first orbit transition and the $\Delta v$ of the second orbit transition, then add them together at the end. 

For the difference in the first orbit transition, I used the notation $\Delta v_{1}$ for the first difference in velocity. Fortunately, we have already found the initial velocity, as it is the same as what was found in [[Chapter 1 Problems#Part (a) - Orbital Average $ langle v {4} rangle$|Part (a)]]. To find the velocity of an orbit with apoapsis at $r_{\text{sync}}$ , we need to use the equation of velocity found earlier. We will also use the concept that any increase in velocity in a circular orbit ends up being the new periapsis of the elliptical orbit that results from the impulse. The way I think of it is that having this increase in velocity will change the orbit, and gravity will slow it down at every other point in the orbit, thus making the point the impulse was added the point where velocity is greatest, and thus making it the periapsis. I didn't end up proving this, but it was my train of logic. Regardless, in order to find this velocity, we need to know the semi-major axis of the resulting elliptical orbit. 

$$ a = \frac{r_{1} + r_{2}}{2} = \frac{r_{\text{sync}} + \left(R_{\text{E}} + 300\text{km}\right)}{2} \approx 24421 \text{ km} $$

Now with this value, we can plug in all known values and solve for the velocity.

$$ v_{\text{peri}} = \sqrt{GM_{\text{E}}\left(\frac{2}{R_{\text{E}} + 300\text{km} } - \frac{1}{24421\text{km}}\right)} $$

$$ v_{\text{peri}} \approx 10.15 \text{km } \text{s}^{-1} $$

Now that we have both velocities, we can find the difference for the first orbital transition.

$$ \Delta v_{1} = v_{\text{peri}} - v_{0} \approx 10.15 - 7.73 \approx 2.42 \text{km } \text{s}^{-1}  $$

With one orbit transition down, we can focus on the other orbit. This orbit transition happens at the apoapsis of the new elliptical orbit, and transitions to the circular orbit. To do this, we need to calculate the velocity at the apoapsis as well as the velocity of the circular orbit at $r_{\text{sync}}$. We will use the equation for velocity in terms of radius and semi-major axis from before.

$$ v_{\text{apo}} = \sqrt{GM_{\text{E}} \left(\frac{2}{r_{\text{sync}}} - \frac{1}{24421 \text{km}}\right)} \approx 1.61 \text{km } \text{s}^{-1} $$

Now we play the same game for the final circular orbit.

$$ v_{\text{sync}} = \sqrt{GM_{\text{E}} \left(\frac{2}{r_{\text{sync}}} - \frac{1}{r_{\text{sync}}}\right)} \approx 3.07 \text{km } \text{s}^{-1} $$

With both velocities found, we can find the difference between the two to find the impulse for the second orbit transition.

$$ \Delta v_{2} = v_{\text{sync}} - v_{\text{apo}} \approx 3.07 - 1.61 = 1.47 \text{km } \text{s}^{-1} $$

In order to find the total impulses, we simply add the two $\Delta v$'s together.

$$ \Delta v = \Delta v_{1} + \Delta v_{2} \approx 2.42 + 1.47 = 3.89 \text{km } \text{s}^{-1} $$

Thus, our problem is complete.

#### Part (c) - Slow Burn Transfer
For the slow burn transfer, the problem states that the spacecraft is spiraling out to the geosynchronous orbit at a near circular and constant rate. The way I took this to mean is that at each instantaneous moment in time, you can think of the spacecraft's orbital path as circular. This implies that the velocity impulse is pushing the spacecraft out and against it's current direction of travel to keep it in such a form. Fortunately, this makes solving for it easy, as we take the difference in circular orbit velocity at the start and at the end. Fortunately, we have already found both of these numbers in [[Chapter 1 Problems#Part (a) - Orbital Average $ langle v {4} rangle$|Part (a)]] and [[Chapter 1 Problems#Part (b) - Orbital Average $ langle v {2} / r rangle$|Part (b)]]. To find our solution, we just have to subtract the two.

$$ \Delta v = v_{\text{sync}} - v_{0} \approx 3.07 - 7.73 = -4.65 \text{km } \text{s}^{-1} $$

The negative value here implying that the spacecraft is slowing down rather than speeding up over the impulse, thus giving us our final solution. We can make some really quick observations about this while we are here too. Looking at the absolute values between this answer and from [[Chapter 1 Problems#Part (b) - Orbital Average $ langle v {2} / r rangle$|Part (b)]] we see that the Hohmann orbit transfer requires lower total impulse. 

### My Commentary
I actually ended up enjoying this problem quite a bit even though it was pretty easy. I thought it was pretty cool to see how a simple rocket traveling through space would be different based on different impulses at certain points. I have always heard about accelerating at apoapsis for more efficient orbit transfer and the like before, but never actually done the math to figure out exactly how good it is or anything like that. 

That being said, there are some problems I have with my answers that I wish I could improve. I am not certain my answer to part (c) is correct, as it seems too easy and it feels like it shouldn't work that way. The book does mention nearly circular orbits, but maybe there is a Taylor expansion I would need to do but I am not sure. I thought about constructing it in a way so that I could use limits for arbitrarily small impulses to make sure, but I figured that would be too much work for a problem with a difficulty of 1. That being said, [[Chapter 1 Problems#Problem 2 - [1] {3}|Problem 1.2]] also has a difficulty of 1 and that problem is a lot harder than that in my opinion.

## Problem 9 - [1] {1}
> In July 2015 the New Horizons spacecraft encountered Pluto. The impact parameter of the encounter was $13700 \text{ km}$ and the relative velocity was $13.8 \text{ km} \text{ s}^{-1}$. By what angle was the spacecraft's trajectory deflected during the encounter? The mass of Pluto is $1.303 \times 10^{22} \text{ km}$.

### My Solution
This problem is rather straightforward. As given to us by the book in Section 1.2, we have a relation between the deflection angle $\theta$ of an unbound orbit with the mass $M$, impact parameter $b$, and velocity of the object $v$. This relation is as follows.

$$ \tan(\frac{1}{2}\theta) = \frac{GM}{bv^{2}} $$

We have all of these values given to us, but first we need to put them in the correct units. This gives us the following.

$$ b = 13700000 \text{ m} $$
$$ M = 1.303\times 10^{22} \text{kg} $$
$$ v = 13800 \text{ m} \text{ s}^{-1} $$
$$ G = 6.67430 \times 10^{-11} \text{ m}^{3} \text{ kg}^{-1} \text{ s}^{-2} $$

Now it's just a matter of plugging everything in.

$$ \tan(\frac{1}{2}\theta) = \frac{(6.67430 \times 10^{-11})(1.303\times 10^{22})}{(13700000)(13800)^{2}} $$
$$ \tan(\frac{1}{2}\theta) = 3.333 \times 10^{-4} $$

From here we use $\tan^{-1}$ to find the angle. Technically, we don't even have to really use the $\tan^{-1}$ function, since for very small angles, $\tan(\theta) \approx \theta$, and this is indeed a very small angle. However, for clarity, I used $\tan^{-1}$ just to be safe.

$$ \frac{1}{2}\theta = \tan^{-1}(3.333 \times 10^{-4}) \approx 3.333 \times 10^{-4} $$
$$ \theta \approx 6.6666 \times 10^{-4} \text{ rads}$$
$$ \theta \approx 0.0382^{\circ} $$

I'm violating significant figures here (not that I've been consistent in the first place), but I just really like how it rounds to a bunch of $6$'s. 

### My Commentary
This problem is probably the easiest one for this chapter if I had to guess. I am not all the way through the problems, but as of right now, it just seems really easy. There isn't much to do besides plug in values, and there is only minor solving for $\theta$. That being said, the result made me question my answer. Getting such a small number made me question if I was correct, so I checked my work with online resources. I saw that the actual deflection was by about 1 degree or so, and that's close enough, even if it's off by like 2 orders of magnitude. I was made a bit more confident too since the numbers I found for the actual event were different than what the book said (ex: the fly-by velocity was $11 \text{ km} \text{ s}^{-1}$ instead of $13.8 \text{ km} \text{ s}^{-1}$). I am choosing to believe this is the correct solution the book intended as I am unsure how to find this angle while also keeping this problem a 1 difficulty.
