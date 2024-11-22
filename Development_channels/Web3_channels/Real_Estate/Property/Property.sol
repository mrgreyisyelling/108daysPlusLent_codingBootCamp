// SPDX-License-Identifier: MIT
// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.8.27;

contract Property{

    // Property Metadata
    struct Metadata{
        string location;
        string description;
        uint256 appraisedValue;
        address ownershipAuthority;
    }

    mapping(uint256 => Metadata) public properties;
    Metadata public propertyMetaData;

    // Events
    event PropertyCreated(string location, string description, uint256 appraisedValue);
    event locationUpdated(string field, string newValue);
    event descriptionUpdated(string field, string newValue);
    event appraisedValueUpdated(string field, uint256 newValue);
    event OwnershipAuthorityUpdated(address newAuthority);

    modifier onlyOwnership

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


// 2. Workflow to Propose a Change in Authority

//     Caller Initiates a Change:
//         The individual (current NFT owner) calls the ERC-721 contract to request an ownership authority change in the metadata contract.

//     ERC-721 Verifies Ownership:
//         The ERC-721 contract validates the caller’s ownership of the NFT (ownerOf(tokenId)).

//     ERC-721 Calls Metadata Contract:
//         Once ownership is verified, the ERC-721 contract (as the designated authority) calls the metadata contract’s proposeOwnershipAuthorityChange function.

//     Metadata Contract Updates Authority:
//         The metadata contract allows this update because it trusts the current ownership authority to have already verified ownership.