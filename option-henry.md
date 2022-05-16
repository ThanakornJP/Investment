# Outline 
1. Basic 1 
- stock vs option
- contract, premium, strike price
- ITM, ATM, OTM
- intrinsic vs extrinsic value 
- payoff chart, black scheles chart, time decay chart
- B.E., moneyness (profitability)
    - when to use option, future, CFD, and stock 
2. Basic 2
- volume, open interest
- bid/ask spread 
- IV 
- delta, theta
- gamma, vega
- dividend calendar
- fundamental analysis: to select good stock for all possible ways  
    - dividend payoff 
    - ROE
- technical analysis: to get used to its behavior not to foresee  
    - MA
    - RSI, Bollinger

3. Strategy 
- buy call/put and thinking system (payoff chart, B.E., probability, risk mgmt)
- sell call/put and thinking system (payoff chart, B.E., probability, risk mgmt)
- know names and its synonyms 
    - beginner strategy: option only 
        - `long call`: buy call, pay to gain when stock rises
        - `long put`: buy put, pay to gain when stock falls
        - `short put`: sell put, losing gain when stock falls
        - `short call`/`naked call`: sell ITM/OTM call, losing gain when stock goes up 
    - intermediate strategy: option + stock
        - `synthetic call`: buy put + buy stock, pay to gain when stock rises 
        - `covered call`: sell OTM call + buy stock, losing gain when stock falls 
        - `covered put`/`married put`: sell stock + sell ATM/OTM put, losing gain when stock rises
        - `protective call`/`synthetic long put`: sell stock + buy ATM call, pay to gain when stock falls
    - intermediate strategy: option + option
        - `bull call spread`: buy ITM call + sell OTM call, losing gain when stock falls
        - `bull put spread`: buy OTM put + sell ITM put, losing gain when stock falls
        - `bear call spread`: buy OTM call + sell ITM call, losing gain when stock rises
        - `bear put spread`: buy ITM put + sell OTM put, losing gain when stock rises
        - `long straddle`/`buy straddle`: buy ATM put + buy ATM call, pay to gain when stock rises/falls         
        - `long strangle`/`buy strangle`: buy OTM put + buy OTM call, pay to gain when stock rises/falls
    - advance
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
---

### Long Call: Buy Call 
        - position = 1
        - market = bullish
        - risk/reward = limited/unlimited
        - B.E. = strike price + premium
        ![Payoff Chart](https://www.chittorgarh.com/images/screenshots/long-call-options-strategy-payoff-chart.png)


### Protective call / Synthetic long put: Sell and Buy ATM Call
        - position = 2
        - market = bearish
        - risk/reward = limited/unlimited
        - B.E. = stock price - call premium
        ![Payoff Chart](https://www.chittorgarh.com/images/screenshots/protective-call-options-strategy-payoff-chart.png)


