# subtree_dists
Functions to calculate summary stats of distances within and between subtrees

Basic functions to iterate across a subtree and calculate tree distances between nodes subtended by the basal node. Not written to run from command line.

Expects a tree in the following format

```
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
```
