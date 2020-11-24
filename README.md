# Easy21
## Usage
Install required packages by running 
<br /> <br /> `pip install -r requirements.txt`<br /><br />
To use Markov Decision Process and Monte Carlo to estimate state action value function, run 
<br /> <br /> `python Markov_Decision_Process.py`<br /><br />
To use Monte Carlo Control to estimate state action value function, run 
<br /> <br /> `python Monte_Carlo_Control.py`<br /><br />

## Results
Algorithm|State-Action Value Function | Policy (yellow - hit, purple - stay) 
-----------:|:-------------------------:|:-------------------------:
Markov Decision Process|![alt text](./imgs/MDPMaxR.png)| ![alt text](./imgs/MDPPolicy.png) ![](https://...Dark.png)  |  ![](https://...Ocean.png)
Monte Carlo Control (Linearly Decreasing Epsilon) |![alt text](./imgs/VariableEpsilon,10000Trials/state-value-function-round-9990.png)| ![alt text](./imgs/VariableEpsilon,10000Trials/policy-round-9990.png)

### Evolution of Monte Carlo Control
Algorithm|State-Action Value Function | Policy (yellow - hit, purple - stay) 
-----------:|:-------------------------:|:-------------------------:
Epsilon = 0 |![alt text](./imgs/Epsilon=0,-1000Trials/state-value-function-summary.gif)| ![alt text](./imgs/Epsilon=0,-1000Trials/policy-summary.gif) ![](https://...Dark.png)  |  ![](https://...Ocean.png)
Epsilon = 1|![alt text](./imgs/Epsilon=1,1000Trials/state-value-function-summary.gif)| ![alt text](./imgs/Epsilon=1,1000Trials/policy-summary.gif)
Linearly Decreasing Epsilon |![alt text](./imgs/VariableEpsilon-1000Trials/state-value-function-summary.gif)| ![alt text](./imgs/VariableEpsilon-1000Trials/policy-summary.gif)
## Discussion
A complete description of the project: https://github.com/XingyuHe/Easy21/blob/master/ProjectMath.pdf



