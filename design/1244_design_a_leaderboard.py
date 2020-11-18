from operator import itemgetter


class Leaderboard:

    def __init__(self):
        self.leaderboard = dict()

    def addScore(self, playerId: int, score: int) -> None:
        """
        Update the leaderboard by adding score to the given player's score.
        If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
        """
        if playerId in self.leaderboard:
            self.leaderboard[playerId] += score
        else:
            self.leaderboard[playerId] = score

    def top(self, K: int) -> int:
        """ Return the score sum of the top K players."""
        res = dict(sorted(self.leaderboard.items(), key=itemgetter(1), reverse=True)[:K])
        total = 0
        for item in res.values():
            total += item
        return total

    def reset(self, playerId: int) -> None:
        """
        Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard).
        It is guaranteed that the player was added to the leaderboard before calling this function.
        """
        self.leaderboard[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
