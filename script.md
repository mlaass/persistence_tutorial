# script

Hello and welcome to this presentation. We will bee looking at the persistence algorithm for trajectory simplification.
The Basic algorithm was introduced in 2014 in the paper "Persistence based online signal and trajectory simplification for mobile devices"

In 2016, I had the privilege to implement this algorithm and find an improvement, that we published in 2021 in the paper "Improving persistence based trajectory simplification".

## trajectory simplification

Lets start by understanding trajectory simplification. For our algorithms we will use the definition of a trajectory as a series of points, ignoring time. This is Ok for geometric algorithms, but there are other definitions that take time into account.

If we want to simplifiy a trajectory, what we are looking for is a way to find the most important points that preserve the shape of the trajectory and discard all other points.

## Douglas Peucker

A well known way to do this is the Douglas Peucker algorithm, which starts by keeping the start and endpoint and searches for the point that is furthest away from the line between the start and the end. And if that point is further away than a predefined epsilon value it will keep it and recursively apply the same principle to the resulting two sub trajectories until it wont find a point with a distance greater than epsilon.

[TODO DP visualisation]

Douglas-Peucker  is great, but has a complexity of O(n^2).

<?--
While you could argue that this does not matter so much on modern machines, it is still a concern for mobile and embedded applications where battery life plays a role and resources are limited or in big data and high performance applications when you have extremely big trajectories or just need shave of cycles to bring down your electricity bill.
--?>

The Persistence algorithm has a complexity of O(n) time and we will show that with some parameter tuning it can compete with Douglas Peucker.


## The algorithm

Persistence works on the  curvature of the trajectory, so we need to convert the trajectory first.

### curvature

To calculate our curvature graph, we simply take the angle in each point between the lines connecting the next and the previous point.

We simply iterate over all points and get the following graph.

This is the input for the actual persistence algorithm, which can be visualized with the sweepline vsiualisation.

### sweepline

The line sweeps from the bottom up and we start a new component at each minimum when components meet at a maximum they merge into the larger one. At the end we have a set of components, the so called "barcode" that connect minima and maxima. The smaller bars represent less important features which we can use to simplify in the next step.

But before we do this, let's look at the actual implementation of the algorithm a bit closer.

### Min Max


The actual implementation starts by calculating the local extrema. We do this by comparing each value to the directly neighbouring values  and if the neighbours are both smaller it is a local maximum and if they are both bigger it is a local minimum.

### ComponentGrowth
In the actual implementation we know that we have a component foreach pair of minima and maxima, so we set up a component for each minimum a component is comprised of a left and right index aswell as a minimum and maximum index and a binary flag indicating if it is done or not.

We then have a loop that goes through all acctive components growing them on the left or right, choosing the side with the lower value. Once it reaches a maximum it check if the maximum is already used by another component.

If it is not taken the component is marked as done and the maximum is marked as used.

If the maximum is already used both components are merged and the component with the lower minimum stays active while the other one is flagged as done.

This is repeated until all components are marked as done.

### Beta Pruning
Looking at the componets in barcode format, we can easily see that the small components represent smaller features and the big components represent bigger features.
Therefore we can prune all components with a size smaller than beta.

[TODO animate beta pruning]
### noise reduction
We can see that through beta pruning we can significantly reduce our original trajectory but there are some artifacts, that remain, that should be removed.


### SDS technique
Our suggestion to remove such noise is segment distance simplification, is to remove all points that are closer to a given epsilon value to the line between their neighbouring points.
 This can be done in several steps each time increasing the epsilon value.

 [TODO animate SDS]

 This technique has proven quite effective in removing noise and has been shown to outperform both simple beta pruning and the multi-resolution simplification suggested in the original paper.


