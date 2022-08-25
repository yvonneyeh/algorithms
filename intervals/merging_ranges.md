# Merging ranges

- [InterviewCake](https://www.interviewcake.com/question/python3/merging-ranges)
- [LeetCode 56](https://leetcode.com/problems/merge-intervals/)

Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as a tuple of integers (`start_time`, `end_time`). These integers represent the number of 30-minute blocks past 9:00am.

For example:

```
(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm
```

Write a function `merge_ranges()` that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

For example, given:
```
  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
```

your function would return:
```
  [(0, 1), (3, 8), (9, 12)]
```

Do not assume the meetings are in order. The meeting times are coming from multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges. Here we've simplified our times down to the number of 30-minute slots past 9:00 am. But we want the function to work even for very large numbers, like Unix timestamps. In any case, the spirit of the challenge is to merge meetings where start_time and end_time don't have an upper bound.



### Edge cases:

- The end time of the first meeting and the start time of the second meeting are equal. For example: `[(1, 2), (2, 3)]`
- The second meeting ends before the first meeting ends. For example: `[(1, 5), (2, 3)]`


### Naive algorithm
1. We treat the meeting with earlier start time as "first," and the other as "second."
2. If the end time of the first meeting is equal to or greater than the start time of the second meeting, we merge the two meetings into one time range. The resulting time range's start time is the first meeting's start, and its end time is the later of the two meetings' end times.
3. Else, we leave them separate.

So, we could compare every meeting to every other meeting in this way, merging them or leaving them separate.

Comparing all pairs of meetings would take `O(n^2)` time. We can do better!

### Solution

- Sorted our list of meetings by start time so meetings that could be merged will always be adjacent

- Sort our meetings, then walk through the sorted list and see if each meeting can be merged with the one after it.

- Sorting takes `O(n log n)` time in the worst case. If we can then do the merging in one pass, that's another `O(n)` time, for `O(n log n)` overall. That's not as good as `O(n)`, but it's better than `O(n^2)`.

### More efficient algorithm
1. First, we sort our input list of meetings by start time so any meetings that might need to be merged are now next to each other.
2. Then we walk through our sorted meetings from left to right.
  At each step, either:
  - We `can` merge the current meeting with the previous one, so we do.
  - We `can't` merge the current meeting with the previous one, so we know the previous meeting can't be merged with any future meetings and we throw the current meeting into `merged_meetings`.


```
def merge_ranges(meetings):

  # Sort by start time
  sorted_meetings = sorted(meetings)

  # Initialize merged_meetings with the earliest meeting
  merged_meetings = [sorted_meetings[0]]

  for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
      last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

      # If the current meeting overlaps with the last merged meeting, use the
      # later end time of the two
      if (current_meeting_start <= last_merged_meeting_end):
          merged_meetings[-1] = (last_merged_meeting_start,
                                 max(last_merged_meeting_end,
                                     current_meeting_end))
      else:
          # Add the current meeting since it doesn't overlap
          merged_meetings.append((current_meeting_start, current_meeting_end))

  return merged_meetings
```


### Complexity
- Time: `O(n log n)`
- Space: `O(n)`

Even though we only walk through our list of meetings once to merge them, we sort all the meetings first, giving us a runtime of O(nlgn). It's worth noting that if our input were sorted, we could skip the sort and do this in O(n) time!

We create a new list of merged meeting times. In the worst case, none of the meetings overlap, giving us a list identical to the input list. Thus we have a worst-case space cost of O(n).

### Follow-up
- What if we did have an upper bound on the input values? Could we improve our runtime? Would it cost us memory?
- Could we do this "in place" on the input list and save some space? What are the pros and cons of doing this in place?


### What We Learned
This one arguably uses a greedy approach as well, except this time we had to sort the list first.

How did we figure that out?

We started off trying to solve the problem in one pass, and we noticed that it wouldn't work. We then noticed the reason it wouldn't work: to see if a given meeting can be merged, we have to look at all the other meetings! That's because the order of the meetings is random.

That's what got us thinking: what if the list were sorted? We saw that then a greedy approach would work. We had to spend O(n log n) time on sorting the list, but it was better than our initial brute force approach, which cost us O(n^2) time!
