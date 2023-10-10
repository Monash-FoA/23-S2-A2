from __future__ import annotations
from dataclasses import dataclass

from mountain import Mountain

from typing import TYPE_CHECKING, Union
from data_structures.linked_stack import LinkedStack

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
        return TrailSeries(None, self.following)
        # raise NotImplementedError()

    def add_mountain_before(self, mountain: Mountain) -> TrailStore:
        """
        Returns a *new* trail which would be the result of:
        Adding a mountain in series before the current one.
        """
        # print(TrailSeries(mountain, TrailSeries(self.mountain, self.following)))

        # print(TrailSeries(mountain, self))
        return TrailSeries(mountain, Trail(TrailSeries(self.mountain, Trail(self.following))))

        # print(self.mountain)
        # print(7)

        # return TrailSeries(mountain, TrailSeries(TrailSeries.mountain, TrailSeries.following))

        # raise NotImplementedError()

    def add_empty_branch_before(self) -> TrailStore:
        """Returns a *new* trail which would be the result of:
        Adding an empty branch, where the current trailstore is now the following path.
        """
        # return TrailStore()

        # return (Trail(None), self)
        # print(1)

        # return TrailSeries(Trail(None), TrailSeries(TrailSeries.mountain, TrailSeries.following))
        return TrailSplit(Trail(None),Trail(None), Trail(self))

        # raise NotImplementedError()

    def add_mountain_after(self, mountain: Mountain) -> TrailStore:
        """Returns a *new* trail which would be the result of:
        Adding a mountain after the current mountain, but before the following trail.
        """
        # return TrailSeries(TrailSeries(cls.mountain, mountain), cls.following)
        return TrailSeries(self.mountain, Trail(TrailSeries(mountain,Trail(self.following))))
        # raise NotImplementedError()

    def add_empty_branch_after(self) -> TrailStore:
        """
        Returns a *new* trail which would be the result of:
        Adding an empty branch after the current mountain, but before the following trail.
        """
        # return TrailSeries(TrailSeries(TrailSeries.mountain, Trail(None)), TrailSeries.following)
        if self.following.store:
            return TrailSeries(self.mountain, Trail(TrailSplit(Trail(None),Trail(None),Trail(TrailSeries(self.following.store.mountain,Trail(None))))))
        else:
            return TrailSeries(self.mountain, Trail(TrailSplit(Trail(None),Trail(None),Trail(None))))


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
        if self.store:
            return Trail(TrailSeries(mountain, Trail(TrailSeries(self.store.mountain, Trail(self.store)))))
        else:
            return Trail(TrailSeries(mountain, Trail(None)))
        # return Trail()

        # raise NotImplementedError()

    def add_empty_branch_before(self) -> Trail:
        """
        Returns a *new* trail which would be the result of:
        Adding an empty branch before everything currently in the trail.
        """
        if self.store:
            return Trail(TrailSplit(Trail(None),Trail(None), Trail(TrailSeries(self.store.mountain, Trail(None)))))
        else:
            return Trail(TrailSplit(Trail(None), Trail(None), Trail(None)))

    def follow_path(self, personality: WalkerPersonality) -> None:
        """Follow a path and add mountains according to a personality.

        
        """
        current_trail = self  # Renamed from present_trail to current_trail
        has_passed_split = False  # Renamed from past_split to has_passed_split for clearer naming
        trail_stack = LinkedStack()  # Renamed from follow_stack to trail_stack
        
        while True:  # Using True instead of 1 for clarity and Pythonic style
            if type(current_trail.store) == TrailSplit:
                trail_stack.push(current_trail.store.following)
                walker_choice = personality.select_branch(current_trail.store.top, current_trail.store.bottom)  # Renamed from person_choice to walker_choice
                if walker_choice.value == 1:
                    current_trail = current_trail.store.top
                elif walker_choice.value == 2:
                    current_trail = current_trail.store.bottom
                else:
                    break
            elif type(current_trail.store) == TrailSeries:
                personality.add_mountain(current_trail.store.mountain)
                if current_trail.store.following.store:
                    current_trail = current_trail.store.following
                elif not trail_stack.is_empty():
                    current_trail = trail_stack.pop()
                else:
                    break
            else:
                if not trail_stack.is_empty():
                    current_trail = trail_stack.pop()
                else:
                    break



    def collect_all_mountains(self) -> list[Mountain]:
        """Returns a list of all mountains on the trail."""
        all_mountains = []
        stack_to_explore = [self]

        while stack_to_explore:
            current_trail = stack_to_explore.pop()

            # If the current trail points to None (end of a path), continue to next iteration.
            if current_trail.store is None:
                continue

            # If TrailSplit, add both possibilities (top and bottom) to be explored next.
            elif isinstance(current_trail.store, TrailSplit):
                stack_to_explore.append(current_trail.store.top)
                stack_to_explore.append(current_trail.store.bottom)
            
            # If TrailSeries, add the mountain to our list and add following trail to be explored next.
            elif isinstance(current_trail.store, TrailSeries):
                all_mountains.append(current_trail.store.mountain)
                stack_to_explore.append(current_trail.store.following)

            # Any other unforeseen object type (safety measure to avoid infinite loop).
            else:
                raise TypeError("Unsupported type in the trail.")

        return all_mountains


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
