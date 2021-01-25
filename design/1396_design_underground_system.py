class UndergroundSystem:

    def __init__(self):
        self.travelTime = dict()  # dict( (stationA,stationC) -> (total_time, no of trips))
        self.singleTrip = dict()  # dict( cardId -> [SwipeInStation, time])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.singleTrip[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.singleTrip:
            return

        swipeInStation = self.singleTrip[id][0]
        startTime = self.singleTrip[id][1]
        duration = t - startTime
        trip = (swipeInStation, stationName)

        if trip in self.travelTime:
            self.travelTime[trip][0] += duration
            self.travelTime[trip][1] += 1
        else:
            self.travelTime[trip] = [duration, 1]

        self.singleTrip.pop(id)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = (startStation, endStation)
        if trip in self.travelTime:
            totalTime = self.travelTime[trip][0]
            numTrip = self.travelTime[trip][1]
            return totalTime / numTrip
        else:
            raise ValueError("No enough information")


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
