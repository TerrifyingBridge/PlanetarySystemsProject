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

According to Appendix A, $P_{\text{E}} = 0.99727 \text{ days}$ and $GM_{\text{E}} = 3.985004 \times 10^{14} \text{ m}^{3} \text{s}^{-2}$ However, before plugging in these values, we have to make sure that our period is in the correct units. There are 86400 seconds in a day, so we have a simple conversion.

$$ 0.99727 \text{ days} \times 86400 = 86164.128 \text{ seconds} $$

Now we can plug in our values.

$$ r_{\text{sync}} = (\frac{(86164.128)^{2} (3.985004 \times 10^{14})}{4 \pi^{2}}) ^ {\frac{1}{3}} $$
