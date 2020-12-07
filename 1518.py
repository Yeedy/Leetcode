# 1518. 换酒问题
class Solution:
    # 28ms(98.42%), 13.5MB(11.55%)
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return (numBottles - numExchange) // (numExchange - 1) + 1 + numBottles \
            if numBottles >= numExchange else numBottles

    # 40ms(62.72%), 13.5(16.32%)
    # def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    #     if numBottles < numExchange:
    #         return numBottles
    #
    #     wine = numBottles
    #
    #     while numBottles >= numExchange:
    #         bottles = numBottles // numExchange
    #         numBottles = numBottles % numExchange + bottles
    #         wine += bottles
    #
    #     return wine
