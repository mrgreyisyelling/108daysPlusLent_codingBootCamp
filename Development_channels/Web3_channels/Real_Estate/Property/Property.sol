// SPDX-License-Identifier: MIT
// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.8.27;

contract Property{

    // Property Metadata
    struct Metadata{
        string location;
        string description;
        uint256 appraisedValue;
    }

    Metadata public propertyMetaData;

    // Events
    event PropertyCreated(string location, string description, uint256 appraisedValue);
    event locationUpdated(string field, string newValue);
    event descriptionUpdated(string field, string newValue);
    event appraisedValueUpdated(string field, uint256 newValue);


    // Constructor to initialize property
    contructor(string memory location, string memory description, uint256 appraisedValue){
        propertyMetadata= Metadata(location, description, appraisedValue);
        emit PropertyCreated(location, description, appraisedValue);
    }

    function updateLocation(string memory location) public {
        propertyMetaData.location = newValue;
        emit locationUpdated("location",newValue);
    }

    function updateDescription(string memory description) public {
        propertyMetaData.description = description;
        emit descriptionUpdated("description",description);
    }

    function updateAppraisedValue(uint256 appraisedValue) public {
        propertyMetaData.description = description;
        emit appraisedValueUpdated("appraisedValue",appraisedValue);
    }


}
