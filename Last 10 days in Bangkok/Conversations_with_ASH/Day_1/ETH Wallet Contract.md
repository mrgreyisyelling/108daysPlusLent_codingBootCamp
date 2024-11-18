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
