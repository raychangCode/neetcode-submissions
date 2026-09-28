class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # ignore all the triplets that contain any val greater than the target at any idx
        # see  we can find all matches at given idx

        matches = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    matches.add(i)

        return len(matches) == 3
            