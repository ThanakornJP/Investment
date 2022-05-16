# Outline 
1. Basic 1 
- stock vs option (module 1:1-2)
- contract, premium, strike price (module 1:3-4 + module 3:0-1,4)
- ITM, ATM, OTM (module 2:8)
- intrinsic vs extrinsic value (module 1:5)
- payoff chart, black scheles chart, time decay chart (module 3:2 + module 4:5)
- B.E., moneyness (profitability) (module 1:7 + module 3:3,5 )
    - when to use option, future, CFD, and stock 
2. Basic 2
- volume, open interest 
- bid/ask spread (module 4:6)
- IV (module 1:6 + module 7:5-6)
- greek (module 3:6)
- delta, theta (module 4:1,3)
- gamma, vega (module 4:2,4)
- dividend calendar
- fundamental analysis: to select good stock for all possible ways (module 2:0-1)
    - dividend payoff 
    - ROE
- technical analysis: to get used to its behavior not to foresee (module 2:2-7)
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

4. Getting started (module 5)
- stock + option mindset: put stocks to work (module 5: 0-3)
- weekly monthly yearly (module 5:5)
- ROI (module 5:6)
- entry (module 2:8 + module 5:4)
- exit (module 2:9 + module 5:7)  

5. Module 6: Why writing put?
6. Module 7: wheel + straddles + strangles
7. Module 8: small accout secret (spread + condor)

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


