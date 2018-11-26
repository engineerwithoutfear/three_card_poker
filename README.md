# TASK

Implement a program that determines the winner of a collection of three card poker hands.

# INPUT

The input is read over `stdin`.
The first line contains an integer in range 0 < x < 24 representing the number of players. Each following line consists of an integer indicating the player's id, followed by their card hand represented as three space separated cards. Cards will be portrayed in the format `<rank><suit>`.

ranks:
-
* an integer from `2` to `9` for numbered cards less than ten
* `T` for ten
* `J` for jack
* `Q` for queen
* `K` for king
* `A` for ace

suit:
-
* `h` for hearts
* `d` for diamonds
* `s` for spades
* `c` for clubs

# OUTPUT

Print the id(s) of the winning player(s) to `stdout`. In the event of a tie, the ids of the winning players should be output on one line, space-separated, in ascending order.


# DEFINITIONS

* **Straight Flush:** A straight flush is a hand that is both a straight and a flush.

* **Three Of A Kind:** A three of a kind is a hand in which all three of the cards have the same rank.

* **Straight:** A straight is a hand in which the cards have ranks that are in a "run." This means that they are of the format `n, n+1, n+2`. Aces can be used as either or a 1 or 14 in a straight, but not both at the same time. Therefore `A-2-3` is a run but `K-A-2` is not.

* **Flush:** A flush is a hand in which all three cards have the same suit.

* **Pair:** A pair is a hand in which two of the cards have the same rank, but the third is different.

* **High Card:** Any hand that doesn't fit into one of the other categories is considered a "high card" hand.

# RANKINGS

Straight Flush > Three of a Kind > Straight > Flush > Pair > High Card


# TIE BREAKING STEPS

1. If two hand are tied, the winner is the hand whose highest card is ranked higher.

2. If the highest cards are equal, then the second highest cards should be compared.

3. If those are equal, the third highest cards should be compared.

4. If all three are equal, then the hands are tied.

**The exception to this is pairs, which use different rules:**

1. If multiple hands are pairs, the pair with the higher rank wins.
2.  If the pair is tied, then the remaining card is used to decide the winner.


# TO RUN MY WONDERFUL PROGRAM

```
./run_my_tests3 "python poker.py"
```


# THOUGHTS/NOTES


* The number of players will always be greater than 0 and less than 24. Since 23 (possible) players x 3 cards is 69, this program must be evaluating some sort of mutant poker that uses more than one 52 card deck of cards. Upon realizing this I had to go back and rework some of my logic to accomodate it.
