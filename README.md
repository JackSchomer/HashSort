# HashSort

An attempt to create a O(N) sorting function for the lulz.

# Implementation

Unlike standard (bad) sorting algorithms that take O(N log n) time, HashSort takes O(3N) time. Instead of actually building the final sorted array, HashSort builds a "compressed" representation that, when passed to the HashedVals function along with a currentvalue, returns the next value that would exist in the sorted array if the sorted array existed. Thus, in many ways the resulting HashedVals function seed is more valuable than the real sorted array anyway.
