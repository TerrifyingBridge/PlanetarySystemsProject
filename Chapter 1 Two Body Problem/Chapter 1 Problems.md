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

### My Solution
To start this problem, consider a point in 2D space $(x, y)$. The angle between the $x$-axis and this point, let's call it $\theta$ has a couple of helpful relations with regards to the point itself. By definition, we have that $\tan (\theta) = \frac{y}{x}$ and we also have $\tan (\theta) = \frac{\sin (\theta)}{\cos (\theta)}$. While whoever you are dear reader probably already knew this, my biggest point in bringing it up is that we can simply substitue $\sin (\theta)$ for $y$ and $\cos (\theta)$ for $x$.

The biggest reason for doing this is because we can immediately use the two relations between true anomaly and eccentric anomaly that is found in the book. One could derive this themself, but the book gives it to us, so I shant bother for this problem. Regardless, the two relations that we will focus on are the following.

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

## Problem 9 - [1] {1}
> In July 2015 the New Horizons spacecraft encountered Pluto. The impact parameter of the encounter was $13700 \text{ km}$ and the relative velocity was $13.8 \text{ km} \text{ s}^{-1}$. By what angle was the spacecraft's trajectory deflected during the encounter? The mass of Pluto is $1.303 \times 10^{22} \text{ km}$.

### My Solution
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
