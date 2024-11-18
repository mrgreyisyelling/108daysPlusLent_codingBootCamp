// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

contract Wallet{
    address public owner;
    address public pendingOwner;
    mapping (address => uint256) public accountBalances;
    uint256 public contractBalance;
    event Deposit(address sender, uint256 amount);
    event Withdrawal(address recipient, uint256 amount);
    event transferOwnershipBegan(address oldOwner, address newOwner);
    event transferOwnershipend(address newOwner);


    constructor(){
        owner = msg.sender;
    }

    modifier onlyOwner(){
        require(owner==msg.sender, "Not the Owner");
        _;
    }

    modifier onlyPendingOwner(){
        require(pendingOwner==msg.sender, "not the new Owner");
    }

    function transferOwnership(address newOwner) public onlyOwner{
        oldOwner = owner;
        pendingOwner = newOwner;
        emit transferOwnershipBegan(oldOwner, pendingOwner)
    }

    function acceptOwnership() public onlyPendingOwner{
        owner = pendingOwner
        emit transferOwnershipend(owner) 
    }

    

    function depositEth() public payable{
        contractBalance += msg.value;
        accountBalances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) public onlyOwner{
        require(contractBalance >= amount && accountBalances[msg.sender] >= amount, "Not enougth Eth");
        contractBalance -= amount;
        accountBalances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit Withdrawal(msg.sender, amount);
    }

    function getContractBalance() public view returns(uint256){
        return contractBalance;

    }

    function getIndividualBalance() public view returns(uint256){
        return accountBalances[msg.sender];
    }

}