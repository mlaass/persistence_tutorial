# script

Hello and welcome, in this introduction. We will bee looking at the persistence algorithm for trajectory simplification.
The Basic algorithm was introduced in 2014 in the paper "Persistence based online signal and trajectory simplification for mobile devices"

I had the privilege to implement this algorithm myself in 2016 and find an improvement, which we published in 2021 in the paper "Improving persistence based trajectory simplification".

Lets start by understanding trajectory simplification. For our algorithms we will use the definition of a trajectory as a series of points, ignoring time. This is Ok for geometric algorithms, but there are algorithms that take time into account, just so you know.

If we want to simplifiy such a trajectory, what we are looking for is a way to find the most important points that preserve the shape of the trajectory, so we can discard the rest.

A well know way to do this is Douglas Peucker, which starts by keeping just the start and endpoint and searches in the rest for the point that is furthest away from the line between the start and the end. And if it is further away than a predefined epsilon value will recursively apply the same principle to the resulting two sub trajectories.

[TODO DP visualisation]

The only problem with Douglas Peucker is its complexity which is O(n^2).

While you could argue that this does not matter so much on modern machines, it is still a concern for mobile and embedded applications where battery life plays a role and resources are limited or in big data and high performance applications when you have extremely big trajectories or just need shave of cycles to bring down your electricity bill.

The Persistence algorithm can be done in O(n) time and we will show that with some parameter tuning it can compete with Douglas Peucker.


## The algorithm

Persistence works on the graph of the curvature of the trajectory, so we need to convert the trajectory first.

Imagine you drive in a car every time you turn, you have to turn the steering wheel by a certain amount that corresponds to the curvature of the road.

We can say if you drive left for example the angle of the steering wheel is negative and when you drive right it is positive.


To calculate our curvature graph, we simply take the angle in each point between the lines connecting the next and the previous point, lets call it alpha.

[TODO alpha image]

We repeat that for every point and there we have it: The the curvature of the trajectory.

But this is just the first step, now we calculate the minima and maxima of our curvature function. We d this by marking the points as maxima whose directly neighbouring points are smaller and the opposite for the minima.

[TODO animate mininma maxima camera]


This is the input for the actual persistence algorithm, which we can get an inuitive understanding for, with the sweepline visualisation.

