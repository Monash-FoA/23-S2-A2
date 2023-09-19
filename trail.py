from __future__ import annotations
from dataclasses import dataclass

from mountain import Mountain

from typing import TYPE_CHECKING, Union

# Avoid circular imports for typing.
if TYPE_CHECKING:
    from personality import WalkerPersonality

@dataclass
class TrailSplit:
    """
    A split in the trail.
       _____top______
      /              \
    -<                >-following-
      \____bottom____/
    """

    top: Trail
    bottom: Trail
    following: Trail

    def remove_branch(self) -> TrailStore:
        #input == TrailSplit only(?)
        """Removes the branch, should just leave the remaining following trail."""

         # remaining_split = TrailSplit(top=None, bottom=self.bottom, following=self.following)
         # input("\nbottom: " + str(self.bottom))
        # input("\ntop: " + str(self.top))
        # input("\nfollowing: " + str(self.following))

        # print("\n\n")
        # if self.top is Trail(None):
#

        # return TrailSplit(self.top, bottom=None, following=self.following)

        # return TrailSeries(self.following.store.mountain, self.following.store.following)#self.following)
        # return TrailSeries(self.following, Trail(None))
        return self.following

        #.store#self.following)


        # Mountain(name='c', difficulty_level=5, length=5)

        # return TrailSeries(TrailSplit.top, TrailSplit.following)

        # raise NotImplementedError()

        """
        split = TrailSplit(
            empty,
            Trail(series_b),
            Trail(
                TrailSeries(c, Trail(None))))

        TrailSeries(mountain=c,following=Trail(store=None))



        res2 = split.remove_branch()
        self.assertIsInstance(res2, TrailSeries)
        self.assertEqual(res2.mountain, c)
        self.assertEqual(res2.following.store, None)
        """


@dataclass
class TrailSeries:
    """
    A mountain, followed by the rest of the trail

    --mountain--following--

    TS (mountain(...), following Trail)

    TrailSeries(mountain, forllowing)


    """

    mountain: Mountain
    following: Trail

    def remove_mountain(self) -> TrailStore:
        """
        Returns a *new* trail which would be the result of:
        Removing the mountain at the beginning of this series.
        """
        # Trail?
        # return self.following
        return self.following
        # raise NotImplementedError()

    def add_mountain_before(self, mountain: Mountain) -> TrailStore:
        """
        Returns a *new* trail which would be the result of:
        Adding a mountain in series before the current one.
        """
        # print(TrailSeries(mountain, TrailSeries(self.mountain, self.following)))

        # print(TrailSeries(mountain, self))
        return Trail(mountain, self)

        # print(self.mountain)
        # print(7)

        # return TrailSeries(mountain, TrailSeries(TrailSeries.mountain, TrailSeries.following))

        # raise NotImplementedError()

    def add_empty_branch_before(self) -> TrailStore:
        """Returns a *new* trail which would be the result of:
        Adding an empty branch, where the current trailstore is now the following path.
        """
        # return TrailStore()

        return (Trail(None), self)
        # print(1)

        # return TrailSeries(Trail(None), TrailSeries(TrailSeries.mountain, TrailSeries.following))

        # raise NotImplementedError()

    def add_mountain_after(self, mountain: Mountain) -> TrailStore:
        """Returns a *new* trail which would be the result of:
        Adding a mountain after the current mountain, but before the following trail.
        """
        # return TrailSeries(TrailSeries(cls.mountain, mountain), cls.following)
        return TrailSeries(self.mountain, TrailSeries(mountain, self.following))
        # raise NotImplementedError()

    def add_empty_branch_after(self) -> TrailStore:
        """
        Returns a *new* trail which would be the result of:
        Adding an empty branch after the current mountain, but before the following trail.
        """
        # return TrailSeries(TrailSeries(TrailSeries.mountain, Trail(None)), TrailSeries.following)
        return self.mountain, TrailSeries(Trail(None), self.following)


        # raise NotImplementedError()

TrailStore = Union[TrailSplit, TrailSeries, None]

@dataclass
class Trail:
    """ Trail(None)
    """

    store: TrailStore = None

    def add_mountain_before(self, mountain: Mountain) -> Trail:
        """
        Returns a *new* trail which would be the result of:
        Adding a mountain before everything currently in the trail.
        """
        return Trail(mountain, self.store)
        # return Trail()

        # raise NotImplementedError()

    def add_empty_branch_before(self) -> Trail:
        """
        Returns a *new* trail which would be the result of:
        Adding an empty branch before everything currently in the trail.
        """
        raise NotImplementedError()

    def follow_path(self, personality: WalkerPersonality) -> None:
        """Follow a path and add mountains according to a personality."""
        raise NotImplementedError()

    def collect_all_mountains(self) -> list[Mountain]:
        """Returns a list of all mountains on the trail."""
        raise NotImplementedError()

    def difficulty_maximum_paths(self, max_difficulty: int) -> list[list[Mountain]]: # Input to this should not exceed k > 50, at most 5 branches.
        # 1008/2085 ONLY!
        raise NotImplementedError()

    def difficulty_difference_paths(self, max_difference: int) -> list[list[Mountain]]: # Input to this should not exceed k > 50, at most 5 branches.
        # 1054 ONLY!
        raise NotImplementedError()



if __name__=="__main__":
    m = Mountain("M", 3, 4)
    empty = Trail(None)
    series = TrailSeries(m, empty)

    m2 = Mountain("I", 5, 6)


    res1 = series.add_mountain_after(m2)
    print("\tres1 type: \n\t", type(res1)) # == TrailSeries
    print("\n\tres1 mountain: \n\t", res1.mountain) # == m
    print("\n\tres1 following: \n\t", res1.following.store) # == m2

    # self.assertIsInstance(res1.following.store, TrailSeries)
    # self.assertEqual(res1.following.store.mountain, m2)
    #
    # res2 = series.add_mountain_before(m2)
    # self.assertIsInstance(res2, TrailSeries)
    # self.assertEqual(res2.mountain, m2)
    # self.assertIsInstance(res2.following.store, TrailSeries)
    # self.assertEqual(res2.following.store.mountain, m)
    #
    # res3 = series.add_empty_branch_after()
    # self.assertIsInstance(res3, TrailSeries)
    # self.assertEqual(res3.mountain, m)
    # self.assertIsInstance(res3.following.store, TrailSplit)
    # self.assertEqual(res3.following.store.bottom.store, None)
    # self.assertEqual(res3.following.store.top.store, None)
    # self.assertEqual(res3.following.store.following.store, None)
    #
    # res4 = series.add_empty_branch_before()
    # self.assertIsInstance(res4, TrailSplit)
    # self.assertEqual(res4.bottom.store, None)
    # self.assertEqual(res4.top.store, None)
    # self.assertIsInstance(res4.following.store, TrailSeries)
    # self.assertEqual(res4.following.store.mountain, m)


# if __name__=="__main__":
#
#     a, b, c, d = (Mountain(letter, 5, 5) for letter in "abcd")
#
#     empty = Trail(None)
#
#     series_b = TrailSeries(b, Trail(TrailSeries(d, Trail(None))))
#
#     split = TrailSplit(empty, Trail(series_b), Trail(TrailSeries(c, Trail(None))))
#
#     t = Trail(TrailSeries(a, Trail(b)))
#
#     split = TrailSplit(empty,Trail(series_b),Trail(TrailSeries(c, Trail(None))))
#
#     # print(series_b, '\n')
#     series_b.add_mountain_before(c)
#     # print()
#
#     print(type(series_b.following.store))
#
#     # print(series_b.remove_mountain())
#     # print(split.remove_branch())
#     # print(series_b.add_empty_branch_before())
#
#     # print(series_b.remove_mountain())
#
#     # print('\n')
#     # print("\nCORRECT: TrailSeries(mountain=c,following=Trail(store=None)")
#     # print(split.remove_branch())
#
#     #
#     #res2 = split.remove_branch()
#     # self.assertIsInstance(res2, TrailSeries)
#     # self.assertEqual(res2.mountain, c)
#     # self.assertEqual(res2.following.store, None)
