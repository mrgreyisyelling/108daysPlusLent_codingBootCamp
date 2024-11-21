## ZTM topics

----
Architecture of a Typical DApp (6:50) - Start
Ethereum Networks (3:38) - Start
Normal vs. View Functions (3:11) - Start
Payable and Pure Functions (4:48) - Start
Public vs. Private Functions (4:46) - Start
What is ERC and EIP? (4:33) - Start
Immutable vs. Constant State (4:10) - Start
 Public vs. Private State (3:58) - Start
 Mapping Getters (1:36) - Start
 Bloom Filters (2:58) - Start
 Memory, Calldata or Storage (6:04) - Start
 Message Variable (4:47) - Start
  Block Variable (3:35) - Start
  Contract Type (3:02) - Start
  Creating New Contracts in Solidity (0:59) - Start
  Burning Tokens (2:54) - Start
  Stages with Enums (3:06) - Start
   Checked Arithmetic (4:55) - Start
    Structuring State Data (2:42) - Start
     Getting Wiser with Libraries (4:54) - Start
## Inheritance
Polymorphism (5:11) - Start
Virtual and Override (5:03) - Start
Abstract (2:38) - Start
The Smart Contract Heirs (3:52) - Start
 Interfaces (5:20) - Start


Foundry

- [ ] Development Setup (2:01) - Start
- [ ] Install VS Code (1:32) - Start
- [ ] Customize VS Code (4:54) - Start
- [ ] Install Foundry (3:35) - Start
- [ ] Foundry Overview (1:30) - Start
- [ ] Cast (2:59) - Start
- [ ] Setting Up Infura Key (2:28) - Start
- [ ] Anvil (2:27) - Start
- [ ] Chisel (1:46) - Start
- [ ] Foundry Init (4:29) - Start
- [ ] Foundry Test Setup (4:34) - Start
- [ ] Foundry Failing Test (4:42) - Start
- [ ] Foundry Succeeding Test (3:31) - Start
- [ ] Foundry Assertions (3:34) - Start
- [ ] Forge Test Verbose (3:37) - Start
- [ ] Code Formatting (1:00) - Start
- [ ] Testing Structure (3:37) - Start
- [ ] Console Logging (3:24) - Start
- [ ] Revert Test (3:24) - Start
- [ ] VM and forge-std (4:31) - Start
- [ ] Event Test (3:37) - Start
- [ ] Forge Create (3:41) - Start
- [ ] Forge Script (3:34) - Start
- [ ] Forge Script Improvements (7:41) - Start
- [ ] Exercise: Foundry - Start


## Hardhat

- [ ] Introduction (0:49) - Start
- [ ] Foundry vs. Hardhat (1:34) - Start
- [ ] Hardhat Requirements (1:29) - Start
- [ ] Initializing Project (2:24) - Start
- [ ] Files and HH (4:11) - Start
- [ ] Test Setup (1:12) - Start
- [ ] Token Transfer Test (2:39) - Start
- [ ] Normal Mocking (3:53) - Start
- [ ] Smock Mocking (7:10) - Start
- [ ] Transfer Assertions (1:11) - Start
- [ ] Logging (2:58) - Start
- [ ] Sending From Different Accounts (1:38) - Start
- [ ] Reverts (1:18) - Start
- [ ] Event Testing (3:11) - Start
- [ ] Refactor Code (3:07) - Start
- [ ] Fixtures (2:04) - Start
- [ ] Network Helpers (1:18) - Start
- [ ] Script (1:42) - Start
- [ ] Deployment (3:07) - Start
- [ ] Contract Verification (3:14) - Start
- [ ] Hardhat + Foundry (1:38) - Start
- [ ] Exercise: Hardhat - Start



## DeFi Example: Implementing Your Own Stablecoin

- [ ] Centralized Stablecoins (2:22) - Start
- [ ] Decentralized Stablecoins (1:46) - Start
- [ ] Designing a Decentralized Stablecoin (4:13) - Start
- [ ] Visualizing Collateral Price Increase (3:55) - Start
- [ ] Visualizing Collateral Price Decrease (3:03) - Start
- [ ] Visualizing Bankrupt Stablecoin (3:25) - Start
- [ ] Collateral vs Tokens (1:57) - Start
- [ ] Depositor Coin Mint + Burn (5:20) - Start
- [ ] Stablecoin Mint (2:13) - Start
- [ ] Stablecoin Burn (3:01) - Start
- [ ] Deposit Collateral Buffer (3:32) - Start
- [ ] Withdraw Collateral Buffer (2:41) - Start
- [ ] Calculating Surplus (3:54) - Start
- [ ] ETH Price (3:31) - Start
- [ ] Ask The Oracle (4:56) - Start
- [ ] Adding Fees (3:36) - Start
- [ ] Deploying Depositor Coin (3:12) - Start
- [ ] Calculating Deficit (5:02) - Start
- [ ] Handling Under Water (3:54) - Start
- [ ] Initial Surplus Ratio (3:56) - Start
- [ ] Time-locked Depositor Coin (3:26) - Start
- [ ] Allowing First Depositor Coin Minting (2:47) - Start
- [ ] Fixed Point Math (3:49) - Start
- [ ] Custom Addition Operator (3:32) - Start
- [ ] More Custom Operators (3:47) - Start
- [ ] Integrating Fixed Points into Deposits (4:45) - Start
- [ ] Integrating Fixed Points into Withdrawals (4:52) - Start
- [ ] Fixed Point Libraries (3:43) - Start
- [ ] Customizing Your Errors (3:53) - Start
- [ ] Exercise: Stablecoin - Start


## A Decentralized Casino

- [ ] Randomness on the Blockchain (3:29) - Start
- [ ] Why Randomness for Ethereum PoS? (3:08) - Start
- [ ] Understanding Prevrandao (3:13) - Start
- [ ] Play Game Function (4:14) - Start
- [ ] Play Game Remix (3:50) - Start
- [ ] Play Game with Randomness (5:44) - Start
- [ ] Alternative Prevrandao Uses (1:45) - Start
- [ ] Prevrandao Discussion (1:55) - Start
- [ ] Commitments (9:15) - Start
- [ ] Implementing Chainlink VRF (9:43) - Start
- [ ] Testing Chainlink VRF (4:38) - Start
- [ ] Fallback Functions (3:50) - Start
- [ ] Arrays (6:11) - Start
- [ ] Winners with Arrays (5:03) - Start
- [ ] Exercise: Decentralized Casino - Start


----
----

---

### **Core Solidity Features**

- **Function Types**: Payable, Pure, View; Normal vs. View functions; Public vs. Private functions.
- **State Management**: Immutable vs. Constant variables; Public vs. Private state variables.
- **Data Structures**: Mappings and Getters; Bloom Filters; Arrays.
- **Unique Variables**: `msg.sender`, `block` variables, `address` type.
- **Memory Management**: Memory vs. Storage vs. Calldata.
- **Arithmetic**: Checked Arithmetic, Fixed-Point Math.
- **Custom Errors**: Defining and using custom error types.

---

### **Design Patterns**

- **Contract Creation**: Deploying contracts programmatically; Nested contracts; Factory patterns.
- **State Management**: Using Enums and Structs for state organization.
- **Libraries**: Using and creating libraries for reusable logic.
- **Inheritance and Polymorphism**: Virtual, Override, Abstract contracts, and Interfaces.
- **Function Modifiers**: Writing reusable access control and conditional logic.

---

### **DeFi Concepts**

- **Stablecoins**: Centralized vs. Decentralized models, Collateral management, Minting/Burning mechanics.
- **Staking**: Token locking, Reward calculations, and Time-based mechanisms.
- **Fees and Revenue**: Implementing transaction fees, surplus handling, and custom pricing.

---

### **Randomness and Oracles**

- **Randomness**: Implementing randomness with Prevrandao or Chainlink VRF.
- **Oracles**: Chainlink price feeds, connecting off-chain data to smart contracts.

---

### **Security**

- **Reentrancy**: Recognizing and preventing attacks with checks and guards.
- **Gas Efficiency**: Writing gas-optimized code, analyzing gas costs, and understanding Solidity internals.
- **Access Control**: Role-based access; Admin patterns.

---

### **Testing and Debugging**

- **Foundry and Hardhat**: Setup, testing structures, logging, and debugging with tools.
- **Mocking**: Using libraries for mocking contracts.
- **Testing Events**: Asserting event emissions, Revert tests.
- **Deployment and Verification**: Automating deployment scripts; verifying contracts.

---

### **Advanced DApp Features**

- **Interoperability**: Contract interaction; calling other contracts; ERC20 and ERC721 token standards.
- **Decentralized Governance**: Voting systems; Weighted votes; Timelocks.
- **Advanced Events**: Logging data and creating custom event-driven flows.

---

### **Application-Specific Use Cases**

- **Decentralized Casino**: Building games; Randomness in outcomes; Payout systems.
- **DAO Mechanics**: Proposal creation, funding allocation, voting mechanisms.
- **Custom Tokens**: Minting, burning, and creating unique tokenomics models.
- **Time-Locked Contracts**: Managing funds and rewards with delayed execution.

---

### **Tools and Frameworks**

- **Foundry**: Testing and scripting with Forge; using Anvil for local chains.
- **Hardhat**: Deployment, mocking, and debugging; integrating with libraries and plugins.