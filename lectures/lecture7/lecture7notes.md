# Lecture 7 Notes

## Spirals

How would you use turtle graphics to draw a spiral? There are at least two
kinds: square, and curvy. Write Python programs to draw both.

### Challenge 1

Draw a *square spiral*.


### Challenge 2

Draw a more curvy-looking spiral.


## Random Walks

A [random walk](https://en.wikipedia.org/wiki/Random_walk) is when the turtle
moves around the screen in a random-seeming way. There are a number of
different ways to do this.


### Challenge 3

Make the turtle do a curvy-looking random walk.


### Challenge 4

Make the turtle do a more rectangular-looking random walk, i.e. turns are
only left or right 90 degrees.


### Challenge 5

When the turtle finishes it's random walk, print out the straight-line
distance from it's starting point of (0, 0) in the center of the screen to the point
where it stops.

You can get (x, y)-position of the turtle using the functions `turtle.xcor()`
and `turtle.ycor()`:

```python
x = turtle.xcor()
y = turtle.ycor()
```

Or you can do it like this:

```python
x, y = turtle.position()
```

The distance from point $(0, 0)$ to point $(x, y)$ is $\sqrt{x^2 + y^2}$.


## Sample Solutions

- [square_spiral.py](square_spiral.py)
- [curvy_spiral.py](curvy_spiral.py)
- [curvy_random_walk.py](curvy_random_walk.py)
- [square_random_walk.py](square_random_walk.py)
- [random_walk_dist.py](random_walk_dist.py)
