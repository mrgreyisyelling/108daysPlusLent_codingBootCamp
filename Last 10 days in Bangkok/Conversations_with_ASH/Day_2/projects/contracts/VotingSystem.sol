//SP
pragma solidity ^0.8.27;

contract VotingSystem(){

// track proposals
// track vote participation
// ownership - only owner can create new proposals
//functions
// create proposal
// vote
// Get votes
//Events
// proposalCreated
// VoteCast

mapping ProposalVotes(uint256 => uint256) public;
mapping VoterVotes(address => mapping(uint => bool)) public;
mapping ProposalDescription(uint => string) public;
address owner public;
uint proposalCount public;

event ProposalCreated(uint ProposalID, string Description);
event VoteCast(address Voter, uint ProposalID);

modifier onlyOwner() {
    require(msg.sender == owner, "not the owner");
    _;
}

function createProposal(string Description) public onlyOwner{
    proposalCount += 1;
    ProposalVotes[proposalCount] = 0;
    ProposalDescription[proposalCount] = Description;
    emit ProposalCreated(proposalCount, Description);
}

function castVote(uint ProposalID) public{
    require(ProposalID <= proposalCount, "Proposal Doesn't Exist");
    require(ProposalDescription[ProposalID] != Null, "Proposal Doesn't Exxist");
    require(VoterVotes[msg.sender][ProposalID] == False, "Voter has Voted already");
    VoterVotes[msg.sender][ProposalID] = True;
    ProposalVotes[ProposalID] += 1;    
    emit VoteCast(msg.sender, ProposalID);
}

function getVotes(uint ProposalID) public returns(uint256){
    return ProposalVotes[ProposalID]
}