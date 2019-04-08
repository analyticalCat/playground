# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervalSet = []
        

    def addNum(self, val: int) -> None:
        if len(self.intervalSet) == 0:
            self.intervalSet.append(Interval(val, val))
        else:

            idx = 0
            while idx < len(self.intervalSet):
                interval = self.intervalSet[idx]

                if val >= interval.start and val<=interval.end: 
                    #if the value falls in range of any interval, nothing needs to be done
                    idx += 1
                    break

                elif val > interval.end:
                    if idx == len(self.intervalSet)-1:
                        #elif the new number is the largest, add a interval at the end of the list or expand the upbound 
                        if val == interval.end+1:
                            interval.end += 1
                        else:
                            self.intervalSet.append(Interval(val, val))
                        break
                    else:
                        idx += 1
                        continue

                elif val < interval.start:
                    #if the new value is less than the lower bound, 4 options: merge 2 intervals, expand the last or the current, new interval.
                    if idx==0:
                        if val == interval.start-1:
                            interval.start -= 1
                            break
                        else:
                            #create a new interval.  case:  3, 1, ...
                            self.intervalSet.insert(0, Interval(val,val))

                    else:
                        intervalminus = self.intervalSet[idx-1]
                        if val == self.intervalSet[idx-1].end + 1:
                            if val == interval.start - 1 :
                                #merge two intervals
                                intervalminus.end = interval.end
                                self.intervalSet.remove(interval)
                            else: 
                                #increase idx-1's upbound
                                intervalminus.end +=1
                        else:
                            #
                            if val == interval.start - 1 :
                                #decrease the idx's lower bound
                                interval.start -= 1
                            else:
                                #create a new interval
                                self.intervalSet.insert(idx, Interval(val, val))
                        break


    def getIntervals(self) :
        return self.intervalSet


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(3)
param_2 = obj.getIntervals()
print(param_2)
obj.addNum(1)
param_2 = obj.getIntervals()
print(param_2)
obj.addNum(7)
param_2 = obj.getIntervals()
print(param_2)
obj.addNum(2)
param_2 = obj.getIntervals()
print(param_2)
obj.addNum(6)
param_2 = obj.getIntervals()
print(param_2)