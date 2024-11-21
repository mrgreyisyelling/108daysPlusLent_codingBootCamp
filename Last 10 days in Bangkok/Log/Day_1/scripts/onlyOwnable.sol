pragma solidity ^0.9.0;

contract OwnableExample {

  address public owner;
  event OwnerChanged(address oldOwner, address newOwner);
  event PendingOwnerChange(address oldOwner, address newOwner);
  address public pendingOwner;
  
  constructor() {
    owner = msg.sender;
  }

  modifier ownerOnly() {
    require(owner == msg.sender, "Not the owner");
    _;
  }

  modifier onlyPendingOwner() {
    require(pendingOwner == msg.sender, "Not the pending owner");
    _;
  }

  function changeOwner(address newOwner) public ownerOnly{
      address oldOwner = owner;
      owner = newOwner;
      emit OwnerChanged(oldOwner, newOwner);
  }

  function initiateOwneshipTransfer(address newOwner) public ownerOnly{
      pendingOwner = newOwner;
      emit PendingOwnerChange(owner, pendingOwner);
  }

  function acceptOwnership() public onlyPendingOwner{
      address oldOwner = owner;
      owner = pendingOwner;
      pendingOwner = address(0);
      emit OwnerChanged(oldOwner, owner);
  }
}
