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
> - use `option`, we manage our risk way much better than stock with equivalent gain
> 
> - as option `buyer`, look for cheaper one ~ less IV and more time
> 
> - as option `seller`, look for expensive one ~ more IV and less time
> 
> Don't lose money
>
> `bell curve` ~ probability with normal distribution is the key of our analysis
>
> `Stock` is completely random in short-term; it is voting machine, and good for long-term
> 
> `Delta` is the risk manager; With option, you can pre-determine how much risk you're gonna bet and how much benefit you're gonna take upfront
> 
> `weekly option advantages more to option seller, especialy non-earning week`


## `Random walk down`, stock is supposed to move sideway and we will never know up/down
- As buyer, you need to expect stock in certain direction to move toward B.E., while seller benefits from the beginning and or it will be cusion when market goes against our position
- Buying option is gambling in the casino. To make it more reasonable, you need to make risk like 1% (3% max.)
  

- stock vs option (module 1:1-2)
- strike price (module 1:3-4 + module 3:0-1,4)

> Example, By given stock = 200k, strike 210k with bull expection. Now, stock 200k->250k, then profit = 250-210 = 40k x 100 = 4m

> Example, By given stock = 200k, strike 260k with bull-exploded expection. Now, stock 200k->250k, then profit = 250-260 = -10k = 0 #profit could not get below 0 

## Premium, contract, intrinsic/extrinsic value (module 1:4,5)

`premium`: 
- price paid to acquire option **contract**, and determined by **intrinsic** and **extrinsic** value
- priced based on volatality


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


##  payoff chart, black scholes chart, time decay chart (module 3:2 + module 4:5)
`Payoff chart` 
![Payoff Chart]()

`Black Scholes chart` 
![Black Scholes chart]()


`Decay Chart`
![Decay Chart](images/Chart_Monthly_weekly.jpg)

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



## Greek (module 3:6), delta, theta (module 4:1,3), gamma, vega (module 4:2,4)

`Delta`: how much option's price changed respecting $1 change of underlying 
- get us better understanding of our directional exposure
- the higher delta, the higher exposure
  - deep ITM, delta will be extremely high 
  - deep ITM + coming expiry, delta will be even extremely higher like 0.99
  - For **~+1/-1delta**, option move the same as stock (moving together; moving in tandem)
  - `buy very deep ITM` = buy stock with less investment since it move the same as stock
- `ATM` gives **0.5delta** always bcoz of blackshore model
  - 50:50 chance like flipping a coin
- tell us `how likely an option I have bought will expire  ITM` `how likely an option I have sold will expire OTM`
  - ATM: delta ~ 0.5
  - ITM: delta > 0.5
  - OTM: delta < 0.5
  - key to manage risk 

> Example, for seller with 0.2 Delta, 
> 
> Thus, it's 20% chance expire out of the money meaning you only have 20% chance that option's gonna to expire worthless.

- the farther OTM, the lower premium 
  - option seller will collect less from the lower premium
- tell us `how much exposure to a stock we have`. We can replace buying stock with buy delta 
  - x delta on option means we have x shares worth of equivalent exposure  
  - when you buy call, you're possitive delta (>0)
  - when you sell, you're negative delta meaning you're selling delta or reducing your exposure
  
> Example, instead of buying 20 shares of AMZN, we buy call option with 0.2 delta of AMZN
>
> It is the same exposure and yield result like buying 20 shares of AMZN 
> 
> Because 
> 
> (1) 100 delta will get option's price move identically (100%) to stock's price meaning option's price will move $1 if stock goes up $1
> 
> (2) 1 option contract has 100 shares of underlying
> 
> Thus, instead of investing whole position in stock, leveraging option to get in the market with pre-determine risk level

> Example, given stock@100 and 101 call for $1 with 0.5 delta, how much is option worth when stock goes up to 101
> 
> option's price = $1 + (1 x 0.5) = $1.50 


> Example, given AAPL @ 100, AAPL Call 110 for $5 with delta of 0.4, 1 month out, and earnings in 1 wk, how much is this option worth?
> 
> change = 110 - 100 = 10
> 
> delta = 10 x 0.4 = 4
> 
> Regardless of other factors, option's worth = 5 + 4 = $9
> now, invest of $5 x 100 turns to $9 x 100 = $900

> Example, You buy a call option for the January 2020 AAPL Call option at the $150 strike. Apple is currently at $125 per share. What is the best choice for what the delta is **likely** to be for the following example? 
> 
> Choice: 50, 35, 80, 100 delta
>
> In this case, we bought call OTM, so delta < 50 which is 35 


`Theta`: measure rate of **time decay** in the value of option/premium
- represent erosion of the option's value
- `theta decreases from buyer side and increase to seller side as time goes by`
- track `how much value options losing in value everyday`
  - option is essetially falling in value every single day
- The closer to the expiry, the more acceleration of theta for the seller    
  - For weekly option, theta is extremely high bcoz of very less time to decay
- As time passes, 
  - OTM 
      - buyer loses; theta decrease
      - seller wins; theta increase
  - ITM = buyer wins and seller loses
- always negative value, 
  - option's value losing its value as time goes by
  - Likewise, options seller gains those value 


`Theta/Time decay`
- the closer to expiry, the faster option losing in value 
- **Monthly** option losses value slower than **weekly** option
- For seller, if theta = 1, then you collect 100 = 1 x 100 shares everyday
- For weekly option seller,
  - less things happen, especially non-earning week
- For earning week,
  - dont' open position from scratch
  - option's really expensive
  - stock moves a lot
  
  
![Decay Chart](images/Chart_Monthly_weekly.jpg)



`Gamma`: measure change in **delta**
- the higher gamma, the more sensitive your portfolio

> Example, given 0.5 delta and 0.1 gamma, how much delta will be if stock goes up $1 
> 
> gamma = $1 x 0.1 = 0.1
> 
> new delta = 0.5 + 0.1 = 0.6

`Vega`: measure risk of changes in IV (volatality)
- the higher volatality, the more expensive option, the more likelihood of option passing strike price
- indicate `how much option pricing would be based on 1% change of underlying volatality`
- affect less for short-term



## dividend calendar
`dividend payoff`

## fundamental analysis: to select good stock for all possible ways (module 2:0-1)
`ROE`

## technical analysis: to get used to its behavior not to foresee (module 2:2-7)
`MA`

`RSI`

`Bollinger`

## Quiz
> Exam, NIO stock is trading at $39 per share. A $40 call option for 1-month out costs $5.63. What is the **breakeven** price for your call option? 
> ..
> result = 40 + 5.63 = $45.63


> Exam, You bought 3 call contracts on Apple stock. It was trading at $119 at the time of the purchase. You picked the $125 call for $2.75 expiring this week before earnings. After earnings on Friday the stock ends at $132.50 per share. How much **money** did you make?
> ..
> 132.5 - (125 + 2.75) = 4.75 * 3 * 100 = $1,425


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


# Appendix: Strategy in Action

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


