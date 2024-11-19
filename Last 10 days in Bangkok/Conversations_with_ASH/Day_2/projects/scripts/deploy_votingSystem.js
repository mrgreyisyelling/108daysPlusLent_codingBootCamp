// scripts/deploy_votingSystem.js

const hre = require("hardhat");

async function main() {
    // Fetch the deployer's account
    const [deployer] = await hre.ethers.getSigners();

    console.log("Deploying VotingSystem contract with the account:", deployer.address);

    // Step 1: Get the contract factory
    const VotingSystemContractFactory = await hre.ethers.getContractFactory("VotingSystem");

    // Step 2: Deploy the contract
    const votingSystemContract = await VotingSystemContractFactory.deploy();

    // Step 3: Wait for the deployment to complete
    await votingSystemContract.deployed();

    console.log("VotingSystem contract deployed to address:", votingSystemContract.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
