pragma solidity ^0.9.0;

contract SimpleStorage { 

  uint256 public storedValue; 
  address public owner;
  event ValueChanged(uint256 newValue); // I don't know the syntax/logic for events
  
  constructor() {
    owner = msg.sender;
  }
  
  modifier ownerOnly() {
    require(owner == msg.sender, "Not the contract owner");
    _; 
  }
  
  function setValue (uint256 newValue) public ownerOnly{
    storedValue = newValue;
    emit ValueChanged(storedValue);
  }

  function getValue() public view returns (uint256){
    return storedValue;
  }

  function resetValue() public ownerOnly {
    storedValue = 0;
  }
}