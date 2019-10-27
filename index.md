![IconImage](Title.PNG)  
### The site is under construction!
## The initial structure:
![Structure](Structure.png)
### DataManager:
**(Status: First version finished, link coming soon.)**<br>
**Short description:** This component manages the data. It gets the latest data and puts it in the database to limit the calls to the API.
### StrategyManager: 
**(Status: Not started yet)**<br>
**Short description:** This component manages all the strategies. Since strategies can vary a lot there have to be some abstract classes.
### TradeSimulator: 
**(Status: Not started yet)**<br>
**Short description:** This component does the backtesting/backtrading. It goes through the data day by day and reports the results back to the strategy manager. The results can later be used for training or for actual trading.
