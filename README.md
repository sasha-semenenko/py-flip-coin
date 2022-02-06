# Toss coin

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

If you flip a coin, heads will come up 50% of the time.
But if you flip a coin 10 times, what is the chance 
that heads will come up 5 times? 2 times?

Write `flip_coin` function, that conducts at least 10000 cases 
of flipping a coin 10 times. It should return list with tuples, 
where first value is number of possible heads dropped (0 to 10),
and second value is percent of how many that number of heads
dropped out of all cases.
```python
print(flip_coin())
# [(0, 11), (1, 7), (2, 4), (3, 18) ... ]
```
If you have done all correctly, you should note that
the biggest percentage of heads dropped number
is about the middle, 4-6 times and tends to 0 when it is
about the edges 0-1 and 9-10. It calls normal distribution or
Gaussian distribution.

# Extra

Draw a graph that shows the distribution.

`matplotlib` is relevant library for this purpose.

- [matplotlib, Diagrams](https://eax.me/python-matplotlib/)
- [matplotlib, Graphs](https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/#p1)
- [matplotlib, Axis](https://pyprog.pro/mpl/mpl_axis_ticks.html)

You should get graph like this:
