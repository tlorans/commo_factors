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

The theory of normal backwardation postulates that commodity futures markets exist to facilitate hedging. It is assumed that hedgers are net short; namely, the positions of producers who sell their output forward exceed the positions of consumers who purchase their input forward. Net short hedgers, willing to transfer their risk of a price decline to net long speculators, must entice them to take long futures positions. This is done by setting the futures price today below the spot price expected at maturity of the futures contract. In other words, futures prices are expected to rise as maturity approaches, so that net long speculators earn a positive risk premium for taking on the price risk that net short hedgers are willing to get rid of. The theory of normal backwardation thus provides a rational for long-only commodity strategies. 

However, noting that hedgers are not necessarily short, Cootner proposes a theoretical model, called the hedging pressures hypothesis, that allows for the possibility of net long, as well as net short, hedgers. As before with the normal backwardation theory, when hedgers are net short, the futures prices has to be set low relative to the spot price expected at maturity to entice speculators to take long future positions. Vice verse, when hedgers are net long, the futures price has to be set high relative to the spot price expected at maturity to entice speculators to take short-futures positions. As maturity approaches, the futures price of a backwardated / contangoed contract is expected to increase / decrease toward the expected spot price, enabling long / short speculators to earn a positive risk premium. It follows that if the hedging pressure hypothesis holds, speculators should be rewarded for taking long positions in backwardated contracts (when hedgers are net short) and short positions in contangoed contracts (when hedgers are net long). 

## Momentum


