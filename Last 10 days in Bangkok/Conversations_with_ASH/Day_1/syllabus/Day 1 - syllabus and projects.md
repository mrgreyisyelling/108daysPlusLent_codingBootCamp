
#### **Objective**:
Build a strong foundation in blockchain and Ethereum fundamentals while creating and interacting with simple Solidity contracts. Transition from basic concepts to practical experience using local development tools like Hardhat.

---

### **Topics Covered**
1. **Blockchain and Ethereum Basics**:
   - What is a blockchain? 
     - Decentralization, immutability, and transactions.
   - Ethereum overview:
     - Ethereum Virtual Machine (EVM).
     - Gas: How it’s calculated and why it matters.
     - Accounts: EOAs vs. smart contracts.

2. **Solidity Basics**:
   - Data types:
     - `uint`, `int`, `bool`, `address`, `string`.
   - Functions:
     - Visibility (`public`, `private`, `internal`, `external`).
     - `view` and `pure` functions.
     - `payable` functions for handling ETH.
   - State variables and local variables.
   - Modifiers and `require()` for error handling.

3. **Event Logging**:
   - Writing and emitting events.
   - Viewing transaction logs for transparency.

4. **Development Environment Setup**:
   - Installing and configuring Hardhat.
   - Writing, compiling, and deploying smart contracts locally.

---

### **Projects**

#### **Project 1: Simple Storage Contract**
- **Objective**: Write a contract to store, retrieve, and manage data.
- **Steps**:
  1. Define a state variable `storedValue` of type `uint`.
  2. Write a function `setValue(uint newValue)`:
     - Use `require()` to enforce that the value must be greater than 10.
     - Emit a `ValueChanged(uint newValue)` event.
  3. Write a function `getValue()` to retrieve the value.
  4. Add ownership:
     - Introduce an `owner` state variable.
     - Create a `modifier onlyOwner()` to restrict certain functions to the contract owner.
     - Use this modifier to restrict `setValue()` to the owner.

---

#### **Project 2: ETH Wallet Contract**
- **Objective**: Build a basic wallet to handle ETH deposits and withdrawals.
- **Steps**:
  1. Write a `payable` function `deposit()` that allows users to send ETH to the contract.
  2. Track balances using a `mapping(address => uint)`.
  3. Write a function `withdraw(uint amount)`:
     - Use `require()` to ensure the sender has enough balance.
     - Transfer ETH to the sender.
  4. Add an event `Deposit(address sender, uint amount)` for deposits.
  5. Add an event `Withdrawal(address recipient, uint amount)` for withdrawals.

---

#### **Project 3: Voting System**
- **Objective**: Introduce mappings, arrays, and events to create a simple voting mechanism.
- **Steps**:
  1. Define a `mapping(uint => uint)` to track votes for each proposal (indexed by `uint`).
  2. Write a function `vote(uint proposalId)`:
     - Emit an event `VoteCast(address voter, uint proposalId)`.
     - Track votes in the mapping.
  3. Add a `require()` statement to ensure voters can’t vote multiple times on the same proposal (use a `mapping(address => bool)` for tracking).
  4. Write a function `getVotes(uint proposalId)`:
     - Return the total votes for a given proposal.
  5. Add ownership to allow only the owner to create new proposals.

---

#### **Project 4: Gas Tracker**
- **Objective**: Understand gas costs by writing functions with varying computational costs.
- **Steps**:
  1. Write a function `gasIntensive()` that uses a loop to perform a computationally heavy operation.
  2. Write a function `lightOperation()` that performs a simple arithmetic operation.
  3. Deploy the contract and interact with both functions, observing gas costs.
  4. Analyze why certain operations consume more gas than others.

---

### **Development Environment**

#### **Installing Hardhat**
1. **Install Node.js**:
   - Ensure Node.js is installed (`node -v` and `npm -v` to check).

2. **Install Hardhat**:
   - Run:
     ```bash
     npm install --save-dev hardhat
     ```

3. **Set Up a Hardhat Project**:
   - Initialize a new project:
     ```bash
     npx hardhat
     ```
   - Choose “Create an empty Hardhat.config.js”.

4. **Install Additional Plugins**:
   - Install Ethers.js for interacting with contracts:
     ```bash
     npm install --save-dev @nomiclabs/hardhat-ethers ethers
     ```

---

### **Goals for Day 1**
1. Write and deploy a Simple Storage Contract.
2. Expand the contract with ownership and event logging.
3. Build an ETH Wallet Contract to handle deposits and withdrawals.
4. Explore gas costs with the Gas Tracker project.
5. Practice using Hardhat to write, compile, deploy, and test contracts.

---

Let me know when you’re ready to start, or if you’d like additional details on any specific part!

