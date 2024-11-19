// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;


contract GasTracker{
    event GasUsed(string functionName, uint256 GasUsed);

    function gasHeavy(uint256 seedNumber) public {
        uint256 gasStart = gasleft();

        uint256 counter = 0;
        for (uint i = 0; i < seedNumber; i++) {
            counter += i+i+i;
        }

        uint256 gasEnd = gasleft();
        emit GasUsed("gasHeavy", gasStart-gasEnd);
    }

    function gasLight(uint256 seedNumber) public{
        uint256 gasStart = gasleft();

        seedNumber+seedNumber;

        uint256 gasEnd = gasleft();
        emit GasUsed("gasLight", gasStart-gasEnd);
    }

    function gasIntermediate(uint256 seedNumber) public{
        uint256 gasStart = gasleft();
        
        seedNumber*seedNumber;

        uint256 gasEnd = gasleft();
        emit GasUsed("gasIntermediate", gasStart-gasEnd);
    }


}