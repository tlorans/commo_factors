# Introduction to Commodity Factors

There is much evidence that average commodity returns are related to observable characteristics such as momentum, basis (spot-futures spread) and hedging pressure. We can use the cost-of-carry model - the commodity market's analog to the dividend discount model - to explain why these characteristics are related to expected returns. The model states that the futures price of a commodity reflects the present value of the spot price adjusted for storage costs, financing costs, and the convenience yield:

$$
F_t = S_t e^{(r + u - c)(T-t)}
$$

In this equation, \\( F_t \\) is the futures price at time \\(t\\), \\(S_t\\) is the spot price at time \\(t\\), \\(r\\) is the risk-free interest rate, \\(u\\) is the storage cost, \\(c\\) is the convenience yield, and \\(T\\) is the maturity of the futures contract.

## The Theory of Storage

The theory of storage, relates the basis, or the difference between the spot and futures prices of a commodity, to the cost of storage (transportation, warehousing and insurance costs), the interests foregone in purchasing the physical commodity and the convenience yield earned from owning the spot asset.

According to the theory of storage, a negative basis (also called roll-yield) or an upward-sloping term structure of the futures prices comes hand-in-hand with high inventories. Market are then said to be in **contango**. In this scenario, the commodity is in abundant supply, inventory holders can buy it cheap in the spot market and sell it forward at a profit that compensates them for the costs incurred while storing and financing the asset. Assuming a constant spot price, the futures price of a contangoed contract is expected to decrease in value as maturity approaches, suggesting that a short position in a contangoed market is probably optimal. 

To illustrate this, suppose the current spot price of a commodity is \\(S_t = 100\\), the 6-month futures contract trades at \\(F_t = 103\\), the annualized risk-free rate is \\(r = 0.05\\), the annualized storage cost is \\(u = 0.02\\), and the time to maturity is 6 months. Rearranging to solve for the convenience yield \\(c\\):

$$
c = r + u - \frac{1}{T-t} \ln\left(\frac{F_t}{S_t}\right)
$$

Substituting the values:
$$
c = 0.05 + 0.02 - \frac{1}{0.5} \ln\left(\frac{103}{100}\right) \approx 0.07 - 2 \cdot \ln(1.03) \approx 0.07 - 0.0591 \approx 0.0109 \text{ or } 1.09\%
$$

So, the implied convenience yield is only about 1.09% - much lower than the combined storage and financing costs of 7%. This reflects a contangoed market where:
- inventories are high,
- the convenience of holding the commodity is low, and
- the futures price is expected to decrease as maturity approaches.
In this case, a short position in the futures contract is expected to be profitable, since the futures price will tend to decline toward the spot as maturity approaches. The position basis \\(F_t > S_t\\) implies that the expected return on the futures contract is negative, assuming the spot price remains constant.

Alternatively, the theory of storage argues that the basis or roll-yield should be positive when inventories are low or in the event of a stock-out. The term structure of future prices then slopes downward and markets are said to be in **backwardation**. Under this scenario, the commodity is expensive since it is scarce and the benefits of owning the physical asset (called convenience yield) exceed storage and financing costs. Again assuming a constant spot price, the futures price of a backwardated asset is deemed to appreciate with maturity, suggesting, this time around, that a long position is likely to be profitable.

To illustrate this, now suppose the current spot price of a commodity is \\(S_t = 100\\), the 6-month futures contract trades at \\(F_t = 98\\), the annualized risk-free rate is \\(r = 0.05\\), the annualized storage cost is \\(u = 0.02\\), and the time to maturity is 6 months. Plugging these values into the convenience yield formula:

$$
c = 0.05 + 0.02 - \frac{1}{0.5} \ln\left(\frac{98}{100}\right) \approx 0.05 + 0.02 - 2 \cdot \ln(0.98) \approx 0.05 + 0.02 + 0.0404 \approx 0.1104 \text{ or } 11.04\%
$$

So the implied convenience yield is about 11.04% - much higher than the combined storage and financing costs of 7%. This reflects a backwardated market. In this case, this suggests that holding the physical commodity confers benefits (e.g, protection from stock-outs) large enough to make futures prices lower than spot prices. The expected return from buying the future today and taking delivery later is positive. In this case, the position basis \\(F_t < S_t\\) implies that the expected return on the futures contract is positive, assuming the spot price remains constant, and a long position in the futures contract is expected to be profitable, since the futures price will tend to increase toward the spot as maturity approaches.


## Hedging Pressure Hypothesis

The hedging pressure hypothesis posits that the net position of hedgers (those who seek to mitigate price risk) and speculators (those who seek to profit from price changes) in the futures market can affect the term structure of futures prices. Specifically, when hedgers are net long (holding more long positions than short positions), they are willing to pay a premium for futures contracts, leading to a positive basis and a backwardated market. Conversely, when hedgers are net short, they may be forced to sell futures contracts at a discount, resulting in a negative basis and a contangoed market.

## Momentum


