//spsometihng
pragma solidity ^0.8.27;


contract GasTracker{

    function gasHeavy(uint256 seedNumber) public {
        uint256 counter = 0
        for (uint i = 0; i < seedNumber; i++) {
            counter += i+i+i;
        }
    }

    function gasLight(uint256 seednumber) public{
        seedNumber+seedNumber;
    }

    function gasIntermediate(uint256 seednumber) public{
        seedNumber*seedNumber
    }


}