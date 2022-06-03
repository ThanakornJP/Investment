# Outline 
1. Basic 
2. Strategy 
3. Getting started (module 5)
4. Module 6: Why writing put?
5. Module 7: wheel + straddles + strangles
6. Module 8: small accout secret (spread + condor)



# 1. Basic 
> **Notes**
> 
> .....
> .....



- stock vs option (module 1:1-2)
- strike price (module 1:3-4 + module 3:0-1,4)

> Example, By given stock = 200k, strike 210k with bull expection. Now, stock 200k->250k, then profit = 250-210 = 40k x 100 = 4m

> Example, By given stock = 200k, strike 260k with bull-exploded expection. Now, stock 200k->250k, then profit = 250-260 = -10k = 0 #profit could not get below 0 

## Premium, contract, intrinsic/extrinsic value (module 1:4,5)

`premium`: price paid to acquire option **contract**, and determined by **intrinsic** and **extrinsic** value

`contract`: obligation to buy/sell at given price on specific date
- `call contract` giving the right to **buy** 100x of underlying stock with a specified price and time. **Market Optimisitc**
- `put contract` giving the right to **sell** 100x of underlying stock with a specified price and time. **Market Pressimistic**

`intrinsic value`: ITM - how much you stock passes strike

`extrinsic value`: factor outside like time(expiry date), IV

`expiry`: contract date; the more time, the more value

> Example, Given stock 162 and strike 150, intrinsic value = 162 - 150 = 12
> 
> Example, option 1month is worth less than option 3months

## ITM, ATM, OTM (module 1:7 + module 2:8)

`ATM`: strike price =~ stock price 

`OTM`
- OTM/Call: strike > stock
- OTM/Put: string < stock
  
`ITM`
- ITM/Call: strike < stock
- ITM/Put: strike > stock


##  payoff chart, black scheles chart, time decay chart (module 3:2 + module 4:5)
`Payoff` = xx

## B.E., moneyness (profitability) (module 1:7 + module 3:3,5 ) ... when to use option, future, CFD, and stock

`Option buyers essentially **gains** less than stock investors, but gain more **ROI** percentage and less risk`

`B.E` 
    `B.E. of Call option` = strike + contract's fee 
    `B.E. of Put option` = strike + contract's fee

> Example, Given AAPL at 100 and **105** call for 5, what are B.E. and return when AAPL at 120?
>  
> **As stock buyer**, 
> - Initially, pay 100 (underlying price) x 100 upfront = **10,000** -- investment
> - B.E. point = entry point = **100**
> - At 120, return = 120 - B.E. = 120 - **100** = 20
> - return = 20 * 100 = 2,000 
> - RR = return / risk = 2,000 / 10,000 = 0.2
> - Gain = (100 --> 120) = 20%
>
> **As option buyer**,
> - Initially, pay 5 (contract fee) x 100 upfront = **500** -- investment
> - B.E. point = entry point + investment = **105** + **5** = 110
> - At 120, 120 - B.E. = 120 - **110** = 10 
> - return = 10 * 100 = 1,000
> - RR = return / risk = 1,000 / 500 = 2 
> - Gain = (5 --> 10) = 100%
> 
>
> Thus, at any given point after B.E., option buyers will gain 10 less than stock investors, but significantly less risk


## volume, open interest, bid/ask spread (module 4:6)

## IV (module 1:6 + module 7:5-6)
`IV`: price fluctuation 
- how much things moving up and down within given period
- the most influential to option pricing --> contract's fee is calculated based on IV and other factors

**Note** `bell curve` ~ probability with normal distribution is the key of our analysis


## Greek (module 3:6), delta, theta (module 4:1,3), gamma, vega (module 4:2,4)
`Delta`

`Theta`

## dividend calendar
`dividend payoff`

## fundamental analysis: to select good stock for all possible ways (module 2:0-1)
`ROE`

### technical analysis: to get used to its behavior not to foresee (module 2:2-7)
`MA`

`RSI`

`Bollinger`


# 2. Strategy 

> **Notes**
> 
> .....
> .....


## BUY call/put and thinking system (payoff chart, B.E., probability, risk mgmt)
...

## SELL call/put and thinking system (payoff chart, B.E., probability, risk mgmt)
...


## Beginner strategy: option only
- `long call`: buy call, pay to gain when stock rises
- `long put`: buy put, pay to gain when stock falls
- `short put`: sell put, losing gain when stock falls
- `short call`/`naked call`: sell ITM/OTM call, losing gain when stock goes up 

## Intermediate strategy: option + stock
- `synthetic call`: buy put + buy stock, pay to gain when stock rises 
- `covered call`: sell OTM call + buy stock, losing gain when stock falls 
- `covered put`/`married put`: sell stock + sell ATM/OTM put, losing gain when stock rises
- `protective call`/`synthetic long put`: sell stock + buy ATM call, pay to gain when stock falls

## Professional strategy: option + option
- `bull call spread`: buy ITM call + sell OTM call, losing gain when stock falls
- `bull put spread`: buy OTM put + sell ITM put, losing gain when stock falls
- `bear call spread`: buy OTM call + sell ITM call, losing gain when stock rises
- `bear put spread`: buy ITM put + sell OTM put, losing gain when stock rises
- `long straddle`/`buy straddle`: buy ATM put + buy ATM call, pay to gain when stock rises/falls         
- `long strangle`/`buy strangle`: buy OTM put + buy OTM call, pay to gain when stock rises/falls

## Advance strategy: option + option
- long combo
- collar
- short straddle / sell straddle / naked straddle
- short strangle / sell strangle 
- long call butterfly
- short call butterfly
- long condor / long call condor 
- short condor / short call condor 
- box spread 
- short box 
- covered strangle


![Payoff Chart](https://www.newtraderu.com/wp-content/uploads/2021/10/Snip-Option-Strategy-CheatSheet.pdf-Personal-Microsoft-Edge-1024x720.png)

# 3. Getting started (module 5)
- stock + option mindset: put stocks to work (module 5: 0-3)
- weekly monthly yearly (module 5:5)
- ROI (module 5:6)
- entry (module 2:8 + module 5:4)
- exit (module 2:9 + module 5:7)  

# 4. Module 6: Why writing put?
# 5. Module 7: wheel + straddles + strangles
# 6. Module 8: small accout secret (spread + condor)


# Reference

## Long Call: Buy Call 
- position = 1
- market = bullish
- risk/reward = limited/unlimited
- B.E. = strike price + premium
![Payoff Chart](https://www.chittorgarh.com/images/screenshots/long-call-options-strategy-payoff-chart.png)


## Protective call / Synthetic long put: Sell and Buy ATM Call
- position = 2
- market = bearish
- risk/reward = limited/unlimited
- B.E. = stock price - call premium
![Payoff Chart](https://www.chittorgarh.com/images/screenshots/protective-call-options-strategy-payoff-chart.png)


