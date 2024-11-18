
Plan we are going to follow
[[Day 1 - syllabus and projects]]


-----

### **Getting Started: Day 1**

We’ll begin with the first project: the **Simple Storage Contract**, focusing on the basics of Solidity, contract deployment, and local development using Hardhat.

---

#### **Step 1: Set Up Your Hardhat Environment**

1. **Install Node.js**:
   - Confirm you have Node.js installed:
     ```bash
     node -v
     npm -v
     ```
   - If not, download it from [nodejs.org](https://nodejs.org/).

2. **Create a New Hardhat Project**:
   - Navigate to your development directory:
     ```bash
     mkdir solidity-basics && cd solidity-basics
     ```
   - Install Hardhat:
     ```bash
     npm install --save-dev hardhat
     ```
   - Initialize the project:
     ```bash
     npx hardhat
     ```
   - Select "Create an empty Hardhat.config.js."

3. **Install Plugins**:
   - Install Ethers.js and the Hardhat Ethers plugin:
     ```bash
     npm install --save-dev @nomiclabs/hardhat-ethers ethers
     ```

---

#### **Step 2: Write the Simple Storage Contract**

1. **Create the Contract**:
   - In your project folder, create a `contracts` directory and add a file named `SimpleStorage.sol`.

2. **Code for Simple Storage Contract**:
   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.0;

   contract SimpleStorage {
       uint256 public storedValue;
       address public owner;

       event ValueChanged(uint256 newValue);

       constructor() {
           owner = msg.sender;
       }

       modifier onlyOwner() {
           require(msg.sender == owner, "Not the owner");
           _;
       }

       function setValue(uint256 newValue) public onlyOwner {
           require(newValue > 10, "Value must be greater than 10");
           storedValue = newValue;
           emit ValueChanged(newValue);
       }

       function getValue() public view returns (uint256) {
           return storedValue;
       }
   }
   ```

---

#### **Step 3: Compile the Contract**

1. Run the Hardhat compile command:
   ```bash
   npx hardhat compile
   ```

2. Check for errors and ensure the contract compiles successfully.

---

#### **Step 4: Deploy the Contract**

1. **Create a Deployment Script**:
   - In the `scripts` directory, create a file named `deploy.js`.

2. **Deployment Script**:
   ```javascript
   const hre = require("hardhat");

   async function main() {
       const SimpleStorage = await hre.ethers.getContractFactory("SimpleStorage");
       const storage = await SimpleStorage.deploy();
       await storage.deployed();

       console.log("SimpleStorage deployed to:", storage.address);
   }

   main().catch((error) => {
       console.error(error);
       process.exitCode = 1;
   });
   ```

3. **Run the Script**:
   - Start a local Hardhat node:
     ```bash
     npx hardhat node
     ```
   - Deploy the contract to the local network:
     ```bash
     npx hardhat run scripts/deploy.js --network localhost
     ```

---

#### **Step 5: Interact with the Contract**

1. **Connect to Hardhat Console**:
   - Open the console:
     ```bash
     npx hardhat console --network localhost
     ```

2. **Interact Using Ethers.js**:
   ```javascript
   const storage = await ethers.getContractAt("SimpleStorage", "deployed_contract_address");

   // Get the stored value
   await storage.getValue();

   // Set a new value
   await storage.setValue(42);
   ```

---

#### **Step 6: Reflect and Expand**
1. **Reflections**:
   - Why did we use `require()` in the `setValue()` function?
   - What happens if a non-owner calls `setValue()`?

2. **Expand**:
   - Modify the contract to accept ETH and track contributions from each address.
   - Add an event to log deposits.

---

Let’s get started with these steps. Once we complete this project, we’ll move on to the next one! Let me know when you’re ready to dive deeper or if you hit any snags.

---
---
M: Normally - lets have me build the contract to your plan, basically both of us coding along together. Give me only code when you need me to do something explicitly technical for the first time - like setting up hardhat, etc. Otherwise, create an outline for yourself to follow for the class, and then have me work through the process of you giving me the requirements, one by one, and me writing the code myself - first as pseudo code and then developing it from there

---
----
Got it! I’ll follow this approach going forward. Let’s start with the **Simple Storage Contract** project.

---

### **Requirements for Simple Storage Contract**

#### **Step 1: Pseudocode the Plan**
Here’s what we want the contract to achieve:
1. **Store a value**:
   - Users should be able to store a number (`uint`) in the contract.
2. **Retrieve the value**:
   - Users should be able to view the stored number.
3. **Access control**:
   - Only the contract owner can update the stored value.
4. **Emit an event**:
   - Whenever the value is updated, log the new value on the blockchain.

---

### **Requirement 1: Define State Variables**
Write pseudocode for:
- A variable to store the number (`storedValue`).
- A variable to store the owner's address (`owner`).

Let me know when you’ve written the pseudocode, and we’ll move to the next step!