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