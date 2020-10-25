class Trade:

    def __init__(self, distance, start, end):
        self.distance = distance
        self.start = start
        self.end = end

    # sorting
    def __gt__(self, other):
        return self.distance < other.distance

    # printing
    def __repr__(self):
        return "{} at {},{}".format(self.distance, self.start, self.end)


class TradeGroup:

    def __init__(self, trades):
        self.distance = 0
        for i in trades:
            self.distance += i.distance
        self.trades = trades

    def __gt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return "{} with trades {}".format(self.distance, self.trades)


class TradingStocks:

    def calculate_distances(prices):
        trades_list = []
        if len(prices) < 2:
            return 0
        for i in range(0, len(prices) - 1):
            for j in range(i + 1, len(prices) - 1):
                distance = prices[j] - prices[i]
                if distance > 0:
                    trades_list.append(Trade(distance, i, j))
        trades_list.sort()
        return trades_list

    def maximum_profit(self, prices, trades):
        trades_list = TradingStocks.calculate_distances(prices)
        if trades == 1:
            return trades_list[0]
        k = 0
        possible_trades = []
        # while k < trades:
        for i in range(0, len(trades_list) - 1):
            trade_group = []
            # hier rekursion irgendwo (?)
            # trade_group = TradeGroup(0,[])
            # while (len(trade_group) < trades) and (i+1+k <= len(trades_list)-1):
            while i + 1 + k <= len(trades_list) - 1:
                trade_group = []
                for j in range(i + 1 + k, len(trades_list) - 1):
                    if not (trades_list[j].start >= trades_list[i].start and trades_list[j].start <= trades_list[i].end) or (
                            trades_list[i].start <= trades_list[j].end <= trades_list[i].end):
                        if trades_list[i] in trade_group and len(trade_group) < trades:
                            trade_group.append(trades_list[j])
                        else:
                            trade_group.extend([trades_list[i], trades_list[j]])
                if len(trade_group) == 0:
                    trade_group.append(trades_list[i])
                possible_trades.append(TradeGroup(trade_group))
                k += 1
        possible_trades.sort()
        return possible_trades


ts = TradingStocks()
possible_trades = ts.maximum_profit([3,2,6,5,0,3], 2)
print(possible_trades)