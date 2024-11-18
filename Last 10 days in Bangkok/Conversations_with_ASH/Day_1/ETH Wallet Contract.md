# ETH Wallet Contract


Awesome! Let's continue. We successfully completed the **Simple Storage Contract**, so now we’ll build on the fundamentals and start working on more advanced concepts. 

---

### **Next Project: ETH Wallet Contract**

This project focuses on:
1. **Learning about Ether transfers** (receiving, sending, and balances).
2. **Exploring the `payable` keyword**.
3. **Adding events for deposit and withdrawal tracking**.
4. **Practicing access control for withdrawals**.

---

### **Plan for the ETH Wallet**
#### **Key Features**
1. The contract should accept deposits from any user.
2. It should allow the owner to withdraw Ether.
3. Emit events for deposits and withdrawals for transparency.
4. Provide a function to check the contract's balance.

---

### **Step 1: Define Requirements**
Here’s what we need for the wallet contract:
1. **State Variables**:
   - `owner`: The address of the wallet owner.
2. **Events**:
   - `Deposit(address sender, uint256 amount)`: Logs deposits.
   - `Withdrawal(address recipient, uint256 amount)`: Logs withdrawals.
3. **Functions**:
   - `deposit()`: Accept Ether into the contract.
   - `withdraw(uint256 amount)`: Allow the owner to withdraw.
   - `getBalance()`: Return the contract’s current Ether balance.

---

### **Your Turn: Write the Pseudocode**
1. Write pseudocode for the wallet contract in the Hardhat project.
2. Start with state variables, events, and basic function signatures.

Let me know when you’ve drafted the pseudocode, and I’ll guide you in refining and implementing it!

-----------------------
-----
## M:

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

contract Wallet{
    address owner public;
    mapping (address => uint256) accountBalances public;
    uint256 contractBalance public;
    event Deposit(address sender, uint256 amount);
    event Withdrawal(address recipient, uint256 amount);

    constructor(){
        owner = msg.sender;
    }

    modifier onlyOwner(){
        require(owner==msg.sender, "Not the Owner");
        _;
    }

    function depositEth(uint256 deposit) public payable{
        contractBalance += deposit;
        accountBalances += (msg.sender => deposit);
        emit Deposit(msg.sender, deposit);
    }

    function withdraw(uint256 amount) public onlyOwner returns(uint256){
        require(contractBalance >= amount & accountBalances(msg.sender=>amount) >= amount, "Not enougth Eth");
        contractBalance -= amount;
        accountBalances -= (msg.sender => amount);
        emit Withdrawal(msg.sender, amount);
    }

    function getContractBalance() public view returns(unit256){
        return contractBalance;

    }

    function getIndividualBalance() public view returns(unit256){
        return accountBalance(msg.sender => amount);
    }

}
```

----
---

## Corrections by ASH:


You're making great progress with this pseudocode! However, there are several syntax and logic issues in the code. I'll provide **constructive feedback** for each part of the contract and allow you to fix it step by step. Let’s take it one point at a time.

---

### **Feedback and Fix Suggestions**

1. **Syntax Errors**
   - **State Variable Declarations**:
     ```solidity
     address owner public;
     mapping (address => uint256) accountBalances public;
     uint256 contractBalance public;
     ```
     - Correct order: visibility (`public`) must come after the type and variable name.
     - Corrected:
       ```solidity
       address public owner;
       mapping (address => uint256) public accountBalances;
       uint256 public contractBalance;
       ```

2. **Logic Errors in `depositEth`**:
   - **Mapping Update**:
     ```solidity
     accountBalances += (msg.sender => deposit);
     ```
     This is not valid Solidity syntax. You update a mapping like this:
     ```solidity
     accountBalances[msg.sender] += deposit;
     ```

   - **Parameter `deposit`**:
     - The amount of Ether sent should be determined using `msg.value`. The `deposit` parameter is unnecessary and may confuse users.
     - Update `depositEth`:
       ```solidity
       function depositEth() public payable {
           contractBalance += msg.value;
           accountBalances[msg.sender] += msg.value;
           emit Deposit(msg.sender, msg.value);
       }
       ```

3. **Logic Errors in `withdraw`**:
   - **Mapping Access**:
     ```solidity
     accountBalances(msg.sender => amount)
     ```
     This syntax is invalid. Use:
     ```solidity
     accountBalances[msg.sender]
     ```

   - **Condition Logic**:
     ```solidity
     require(contractBalance >= amount & accountBalances[msg.sender] >= amount, "Not enough Eth");
     ```
     - `&` is a bitwise operator; use `&&` for logical AND.
     - Corrected:
       ```solidity
       require(contractBalance >= amount && accountBalances[msg.sender] >= amount, "Not enough Eth");
       ```

   - **Deducting from Mapping**:
     ```solidity
     accountBalances -= (msg.sender => amount);
     ```
     - Invalid syntax; correct it:
       ```solidity
       accountBalances[msg.sender] -= amount;
       ```

   - **Sending Ether to the Owner**:
     You need to transfer the Ether back to the owner using:
     ```solidity
     payable(msg.sender).transfer(amount);
     ```

   - Updated `withdraw`:
     ```solidity
     function withdraw(uint256 amount) public onlyOwner {
         require(contractBalance >= amount && accountBalances[msg.sender] >= amount, "Not enough Eth");
         contractBalance -= amount;
         accountBalances[msg.sender] -= amount;
         payable(msg.sender).transfer(amount);
         emit Withdrawal(msg.sender, amount);
     }
     ```

4. **`getContractBalance` Function**
   - **Typo**:
     ```solidity
     returns(unit256)
     ```
     - It should be `uint256` instead of `unit256`.

   - Updated:
     ```solidity
     function getContractBalance() public view returns (uint256) {
         return contractBalance;
     }
     ```

5. **`getIndividualBalance` Function**
   - **Mapping Access Issue**:
     ```solidity
     accountBalance(msg.sender => amount)
     ```
     - Fix:
       ```solidity
       accountBalances[msg.sender]
       ```

   - **Typo in `uint256`**:
     Replace `unit256` with `uint256`.

   - Updated:
     ```solidity
     function getIndividualBalance() public view returns (uint256) {
         return accountBalances[msg.sender];
     }
     ```

---

### **Corrected Contract**

Here’s the updated and corrected version based on your draft:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

contract Wallet {
    address public owner;
    mapping(address => uint256) public accountBalances;
    uint256 public contractBalance;

    event Deposit(address sender, uint256 amount);
    event Withdrawal(address recipient, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(owner == msg.sender, "Not the Owner");
        _;
    }

    function depositEth() public payable {
        contractBalance += msg.value;
        accountBalances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) public onlyOwner {
        require(contractBalance >= amount && accountBalances[msg.sender] >= amount, "Not enough Eth");
        contractBalance -= amount;
        accountBalances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit Withdrawal(msg.sender, amount);
    }

    function getContractBalance() public view returns (uint256) {
        return contractBalance;
    }

    function getIndividualBalance() public view returns (uint256) {
        return accountBalances[msg.sender];
    }
}
```

---

### **Next Steps**
1. Review these changes and understand the corrections made.
2. Test this contract by:
   - Depositing Ether from multiple accounts.
   - Checking balances using `getContractBalance` and `getIndividualBalance`.
   - Withdrawing Ether as the owner.
3. Let me know if you'd like to proceed with deployment or refine further!


---
---
## M: 

ash gave me a way to do everything through a script:

_scripts/interact_wallet.js_

```javascript

const { ethers } = require("hardhat");

async function main() {
    // Replace with your deployed contract address
    const contractAddress = "0x5FbDB2315678afecb367f032d93F642f64180aa3";

    // Get the signer (default first account in Hardhat node)
    const [deployer] = await ethers.getSigners();
    console.log("Using account:", deployer.address);

    // Connect to the deployed Wallet contract
    const wallet = await ethers.getContractAt("Wallet", contractAddress);

    // Check the owner
    const owner = await wallet.owner();
    console.log("Owner address:", owner);

    // Get contract balance
    const balance = await wallet.getContractBalance();
    console.log("Contract Balance:", ethers.utils.formatEther(balance), "ETH");

    // Deposit Ether into the contract
    console.log("Depositing 1.0 ETH...");
    const depositTx = await wallet.depositEth({ value: ethers.utils.parseEther("1.0") });
    await depositTx.wait();
    console.log("Deposit successful!");

    // Check individual balance
    const individualBalance = await wallet.getIndividualBalance();
    console.log("Individual Balance:", ethers.utils.formatEther(individualBalance), "ETH");

    // Withdraw Ether (only if you're the owner)
    console.log("Withdrawing 0.5 ETH...");
    const withdrawTx = await wallet.withdraw(ethers.utils.parseEther("0.5"));
    await withdrawTx.wait();
    console.log("Withdrawal successful!");

    try {
        
        const withdrawalAmount = ethers.utils.parseEther("1.0"); // Define withdrawal amount in Ether

        if (balance.lt(withdrawalAmount)) {
            console.error("Withdrawal failed: Not enough funds in the contract.");
            return;
        }
    
        if (individualBalance.lt(withdrawalAmount)) {
            console.error("Withdrawal failed: Not enough individual balance.");
            return;
        }
        
        console.log("Attempting to withdraw 1.0 ETH...");
        const withdrawTx = await wallet.withdraw(ethers.utils.parseEther("1.0"));
        await withdrawTx.wait();
        console.log("Withdrawal successful!");
    } catch (error) {
        console.error("Withdrawal failed:", error.message);
    }

    // Check balances again
    const newContractBalance = await wallet.getContractBalance();
    console.log("Updated Contract Balance:", ethers.utils.formatEther(newContractBalance), "ETH");

    const newIndividualBalance = await wallet.getIndividualBalance();
    console.log("Updated Individual Balance:", ethers.utils.formatEther(newIndividualBalance), "ETH");
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});


```

------------
--------------

## Ash:

Awesome, glad that worked! Let’s build on what you’ve learned and expand your skills. Here’s what we can do next, focusing on deeper Solidity concepts and reinforcing best practices:

---

### **Next Steps**

#### **1. Expand the Wallet Contract**
Add more advanced features to your Wallet contract to practice Solidity concepts:
- **Transfer Ownership**: Implement a function to allow the owner to transfer ownership.
- **Emergency Stop**: Add a mechanism to pause all deposits and withdrawals in case of emergencies (`Circuit Breaker` pattern).
- **Multiple Depositors**: Extend the functionality to track multiple depositors and allow them to withdraw their specific balances.

#### **2. Test Your Contract**
Learn how to write automated tests for your contract using Hardhat's testing framework:
- Create a test file in the `test/` folder (e.g., `wallet.test.js`).
- Write unit tests for:
  - Successful deposits and withdrawals.
  - Reverts when conditions (e.g., insufficient balance) aren’t met.
- Example:
  ```javascript
  describe("Wallet Contract", function () {
      it("Should allow the owner to deposit and withdraw", async function () {
          const [owner] = await ethers.getSigners();
          const Wallet = await ethers.getContractFactory("Wallet");
          const wallet = await Wallet.deploy();

          await wallet.depositEth({ value: ethers.utils.parseEther("1.0") });
          const contractBalance = await wallet.getContractBalance();
          expect(contractBalance).to.equal(ethers.utils.parseEther("1.0"));

          await wallet.withdraw(ethers.utils.parseEther("0.5"));
          const updatedBalance = await wallet.getContractBalance();
          expect(updatedBalance).to.equal(ethers.utils.parseEther("0.5"));
      });
  });
  ```

---

#### **3. Learn About Hardhat Tasks**
Create reusable scripts to perform specific tasks like deploying contracts, interacting with them, or querying data:
- Example of a custom Hardhat task:
  ```javascript
  task("check-balance", "Prints the contract's balance")
      .setAction(async () => {
          const contractAddress = "0xYourContractAddress";
          const wallet = await ethers.getContractAt("Wallet", contractAddress);
          const balance = await wallet.getContractBalance();
          console.log("Contract Balance:", ethers.utils.formatEther(balance));
      });
  ```

Run the task:
```bash
npx hardhat check-balance --network localhost
```

---

#### **4. Dive Deeper into Solidity Topics**
Build mini-projects to practice advanced concepts:
1. **Inheritance**: Create a parent `Ownable` contract and inherit its functionality in your Wallet.
2. **Events and Logging**: Enhance the contract to emit events for all state changes and test the logs.
3. **Modifiers**: Add more complex modifiers to enforce roles and permissions.

---

#### **5. Integrate a Frontend**
If you’re ready to go beyond Hardhat:
1. Use React.js with ethers.js to build a simple frontend for your Wallet contract.
2. Implement:
   - Connect Wallet.
   - Deposit Ether.
   - Withdraw Ether.
   - Display Balances.

---

#### **Suggested Focus for Now**
For today, let's:
1. Add a **transfer ownership** function and a **pause/unpause** mechanism to the Wallet contract.
2. Write basic tests to validate the new features.

If that sounds good, I’ll guide you step-by-step through the implementation. Let me know where you’d like to start!

-----------------------
--------------------
