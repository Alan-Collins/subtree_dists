#!/usr/bin/env python3

import sys
import statistics
from typing import Generator

def dists_from_subtree_root(tree: dict[str, list[dict[...]]], dist: int = 0) -> Generator[int, None, None]:
	"""Given a tree, sum edge lengths to each terminal node and return them"""
	edgeweight = tree["distance"]
	subtree = tree["branches"]
	if len(subtree) == 2: # layers remaining
		for sub in subtree:
			for x in dists_from_subtree_root(sub, dist+edgeweight):
				yield x
	else:
		# yield total depth
		yield edgeweight+dist


def get_subtrees_dists(tree: dict[str, list[dict[...]]]) -> Generator[int, None, None]:
	"""Given a tree, return distances between pairs of nodes for which this node is basal"""
	subtree = tree["branches"]
	if subtree: 
		dists = []
		for sub in subtree:
			dists.append([i for i in dists_from_subtree_root(sub)])
		for a in dists[0]:
			for b in dists[1]:
				yield a + b
		for sub in subtree:
			for x in get_subtrees_dists(sub):
				yield x


def within_subtree_dist(tree: dict[str, list[dict[...]]]) -> tuple[float, float, float]:
	"""get median, min, and max pairwise dists between all leaves in subtree
	
	Args:
		tree: subtree at selected level

	Returns:
		median, min, and max pairwise distances between leaves in selected subtree
	
	"""

	dists = []
	# Use recursive function to get subtree dists as well
	for x in get_subtrees_dists(tree):
		dists.append(x)
	
	med_dist = statistics.median(dists)
	min_dist = min(dists)
	max_dist = max(dists)

	return med_dist, min_dist, max_dist


def between_subtree_dist(tree: dict[str, list[dict[...]]]) -> tuple[float, float, float]:
	"""get median, min, and max pairwise dists between leaves in the two subtrees subtended by selected node
	
	Args:
		tree: subtree at selected level

	Returns:
		median, min, and max pairwise distances 
		between leaves in subtrees subtended by selected node
	
	"""

	dists = []
	for subtree in tree["branches"]:
		subdists = []
		for x in dists_from_subtree_root(subtree):
			subdists.append(x)
		dists.append(subdists)

	between_dists = []
	for a in dists[0]:
		for b in dists[1]:
			between_dists.append(a + b)
	
	med_dist = statistics.median(between_dists)
	min_dist = min(between_dists)
	max_dist = max(between_dists)

	return med_dist, min_dist, max_dist



# ((A:12, B:10):3, (C:23, D:19):5);
tree = {
	"distance": 0,
	"branches": [
		{
			"distance": 3,
			"branches": [
				{
					"distance": 12,
					"branches": []
				},
				{
					"distance": 10,
					"branches": []
				}
			]
		},
		{
			"distance": 5,
			"branches": [
				{
					"distance": 23,
					"branches": []
				},
				{
					"distance": 19,
					"branches": []
				}
			]
		}
	]
}

between = between_subtree_dist(tree)
within = within_subtree_dist(tree)
print(f"Between subtree stats: {between[0]} [{between[1]}, {between[2]}]")
print(f"Within subtree stats: {within[0]} [{within[1]}, {within[2]}]")
