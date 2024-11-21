//SP
pragma solidity ^0.8.27;

contract VotingSystem{

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

mapping (uint256 => uint256) public proposalVotes;
mapping (address => mapping(uint256 => bool))  public voterVotes;
mapping (uint256 => string) public proposalDescription;
address public owner;
uint256 public proposalCount;

event ProposalCreated(uint proposalID, string description);
event VoteCast(address voter, uint proposalID);

constructor(){
    owner = msg.sender;
    proposalCount =0;
}

modifier onlyOwner() {
    require(msg.sender == owner, "not the owner");
    _;
}

function createProposal(string memory description) public onlyOwner{ //Why memory?
    proposalCount += 1;
    proposalVotes[proposalCount] = 0;
    proposalDescription[proposalCount] = description;
    emit ProposalCreated(proposalCount, description);
}

function castVote(uint256 proposalID) public{
    require(proposalID <= proposalCount, "Proposal Doesn't Exist");
    require(bytes(proposalDescription[proposalID]).length > 0, "Proposal Doesn't Exxist"); // why use bytes?
    require(!voterVotes[msg.sender][proposalID], "Voter has Voted already");
    voterVotes[msg.sender][proposalID] = true;
    proposalVotes[proposalID] += 1;    
    emit VoteCast(msg.sender, proposalID);
}

function getVotes(uint proposalID) public view returns(uint256){
    return proposalVotes[proposalID];
}
}