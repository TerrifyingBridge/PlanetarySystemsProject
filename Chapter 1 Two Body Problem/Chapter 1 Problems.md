# Chapter 1 Problems
This file will outline my solutions to the practice problems in the back of the book. Each chapter of the book has a number of different practice problems (some more than others), and I want to try my hand at solving all of them. Truthfully, I think this is very ambitious, especially since growing up I wasn't always able to finish all of the practice problems in my math text books (I probably could now, but that's a lot of work). Each of the problems for each chapter have a difficulty ranking. I will be keeping this trend as well when outlining the problems using the same notation. In case you are not aware, the book has three different difficulty ratinges: 1, 2, and 3. In this book, 1 is the easiest and 3 is the hardest. The book also uses brackets to show off these ratings so they will look like this: [1]. Before jumping into it, there are a couple of things I would like to preface that will not be in the rest of the problem files for future chapters.

The problems for each chapter aren't exactly organized by the section you need to finish reading in order to solve them. For example, the first three problems in chapter 1 require you to understand section 1.3 while problem 9 can be completed upon finishing section 1.2. Because of this, my original plan was to wait until the end of the chapter to complete them. This way, I know that I had the capability to solve every problem. However, I fear that when/if I finish a chapter, I will force myself to do a bunch of problems instead of actually going through and learning the parts that I find interesting. So, I have decided to just do the problems as I see fit and whenever I feel like it. This might change as things continue but that's my current plan. 

Each problem will have a main title, and the actual problem itself. From there I will give my solution and final commentary at the end. One thing I also thought would be fun is to give my own take on the difficulty of the problems. I like to have a bit more fine measurment, so my rating scale will be a 1 through 5 scale (1 being easy and 5 being difficult), with the exception of 6 which means I wasn't able to solve it and gave up. To stand out from the book, I will place my difficulty in {} instead. Lastly, on the off chance anyone actually reads these problems besides me: **I am not always going to be able to verify if these solutions are correct**. This whole endeavor is my personal project and virtually no one is helping me, so if I can't figure it out on my own or look up a solution, I have almost no way of verifying if I am correct. I am fine with it, but I am sure someone copying me will not.

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
This problem was rather simple, and was just centered around basic use of an equation. Can't say I have too much commentary besides talking about the hint mentioned, as it implies the existance of a common misunderstanding that would yield an answer of $42241 \text{ km}$ instead. That incorrect answer was easy to find, as it comes from having the period of Earth's rotation being exactly 1 day instead of 0.99727 days. Outside of that, nothing too much to say. It took my significantly longer to type this up than to actually do it.

## Problem 4 - [1] {1}
> Many computing languages provide the function $\text{atan2}(y, x)$, which yields the angle in radians between the positive $x$-axis and the vector from the origin to the point $(x, y)$. Find an expression for the true anomaly of a bound orbit in terms of the eccentric anomaly using this function.

To start this problem, consider a point in 2D space $(x, y)$. The angle between the $x$-axis and this point, let's call it $\theta$ has a couple of helpful relations with regards to the point itself. By definition, we have that $\tan (\theta) = \frac{y}{x}$ and we also have $\tan (\theta) = \frac{\sin (\theta}{\cos (\theta}$. While whoever you are dear reader probably already knew this, my biggest point in bringing it up is that we can simply substitue $\sin (\theta)$ for $y$ and $\cos (\theta)$ for $x$.

The biggest reason for doing this is because we can immediately use the two relations between true anomaly and eccentric anomaly that is found in the book. One could derive this themself, but the book gives it to us, so I shant bother for this problem. Regardless, the two relations that we will focus on are the following.

## Problem 9 - [1] {1}
### My Solution
> In July 2015 the New Horizons spacecraft encountered Pluto. The impact parameter of the encounter was $13700 \text{ km}$ and the relative velocity was $13.8 \text{ km} \text{ s}^{-1}$. By what angle was the spacecraft's trajectory deflected during the encounter? The mass of Pluto is $1.303 \times 10^{22} \text{ km}$.

This problem is rather straightforward. As given to us by the book in Section 1.2, we have a relation between the delfection angle $\theta$ of an unbound orbit with the mass $M$, impact parameter $b$, and velocity of the object $v$. This relation is as follows.

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

I'm violating significant sigures here (not that I've been consistent in the first place), but I just really like how it rounds to a bunch of $6$'s. 

### My Commentary
This problem is probably the easiest one for this chapter if I had to guess. I am not all the way through the problems, but as of right now, it just seems really easy. There isn't much to do besides plug in values, and there is only minor solving for $\theta$. That being said, the result made me question my answer. Getting such a small number made me question if I was correct, so I checked my work with online resources. I saw that the actual deflection was by about 1 degree or so, and that's close enough, even if it's off by like 2 orders of magnitude especially since the numbers I found for the actual event were different than what the book said (ex: the fly-by velocity was $11 \text{ km} \text{ s}^{-1}$ instead of $13.8 \text{ km} \text{ s}^{-1}$). I am choosing to believe this is the correct solution the book intended as I am unsure how to find this angle while also keeping this problem a 1 difficulty.
