// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

contract SimpleStorage {

    uint256 public storedValue;
    address public owner;
    event ValueChanged(uint256 oldValue,uint256 newValue);

    constructor(){
        owner = msg.sender;
    }
    modifier onlyOwner(){
        require(owner == msg.sender, "Not the Owner");
        _;
    }

    function setValue(uint256 newValue) public onlyOwner{
        require(newValue > 10, "Value must be greater than 10");
        uint256 oldValue = storedValue;
        storedValue = newValue;
        emit ValueChanged(oldValue,newValue);
    }
    
    function getValue() public view returns(uint256){
        return storedValue;
    }   

}