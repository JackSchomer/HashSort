# HashSort

An attempt to create a O(N) sorting function for the lulz.

# Implementation

Rather than actually sort the array, HashSort generates a function (using an binary array) that, when passed a value, returns the next value that would be expected from the sorted array if the sorted array existed.

So long as the difference between Max and Min values of the array to be sorted aren't massive, this algorithm performs surpsisingly well.
