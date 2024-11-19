// scripts/test_votingSystem.js

const hre = require("hardhat");

async function main() {
    const [owner, user_1, user_2] = await hre.ethers.getSigners();

    console.log("Using Account:", owner.address);

    // Deploy votingSystem
    const VotingSystem = await hre.ethers.getContractFactory("VotingSystem");
    const votingSystem = await VotingSystem.deploy();
    await votingSystem.deployed();

    console.log("VotingSystem contract deployed to:", votingSystem.address);

    // Initial state
    console.log("Owner address:", await votingSystem.owner());
    console.log("proposal Count:", await votingSystem.proposalCount());

    // Create a proposal
    const proposalDescription = "Description 1";
    tx = await votingSystem.connect(owner).createProposal(proposalDescription);
    await tx.wait();
    console.log("Proposal Created by owner");
    try {
        tx = await votingSystem.connect(user_1).createProposal(proposalDescription);
        await tx.wait();
        console.log("Proposal created by user_1 (unexpected)");
      } catch (error) {
        console.error("Failed to create proposal by user_1:", error.message);
      }

    // cast a vote

    proposalID = await votingSystem.proposalCount();
    tx = await votingSystem.connect(owner).castVote(proposalID);
    await tx.wait();
    console.log("vote cast by owner");
    try {
        tx = await votingSystem.connect(owner).castVote(proposalID);
        await tx.wait();
        console.log("Vote cast by owner twice (unexpected)");
      } catch (error) {
        console.error("Failed to cast vote by owner twice:", error.message);
      }
    tx = await votingSystem.connect(user_1).castVote(proposalID);
    await tx.wait();
    console.log("vote cast by user_1");
    tx = await votingSystem.connect(user_2).castVote(proposalID);
    await tx.wait();
    console.log("vote cast by user_2");
    
    // get votes on proposal
    voteCount = await votingSystem.connect(owner).getVotes(proposalID);
    console.log("Vote Count", voteCount.toString());
    console.log("Votes Counted");      
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });