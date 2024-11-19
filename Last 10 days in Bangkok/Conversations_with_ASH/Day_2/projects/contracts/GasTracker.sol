// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;


contract GasTracker{
    event GasUsed(string functionName, uint256 GasUsed);

    function gasHeavy(uint256 seedNumber) public {
        unit256 gasStart = gasleft();

        uint256 counter = 0;
        for (uint i = 0; i < seedNumber; i++) {
            counter += i+i+i;
        }

        unit256 gasEnd = gasleft();
        emit GasUsed("gasHeavy", gasStart-gasEnd);
    }

    function gasLight(uint256 seednumber) public{
        unit256 gasStart = gasleft();

        seedNumber+seedNumber;

        unit256 gasEnd = gasleft();
        emit GasUsed("gasHeavy", gasStart-gasEnd);
    }

    function gasIntermediate(uint256 seednumber) public{
        unit256 gasStart = gasleft();
        
        seedNumber*seedNumber;

        unit256 gasEnd = gasleft();
        emit GasUsed("gasHeavy", gasStart-gasEnd);
    }


}