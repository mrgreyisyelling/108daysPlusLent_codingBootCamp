// scripts/deploy_votingSystem.js

const hre = require("hardhat");

async function main() {
    // Fetch the deployer's account
    const [deployer] = await hre.ethers.getSigners();

    console.log("Deploying GasTracker contract with the account:", deployer.address);

    // Step 1: Get the contract factory
    const GasTrackerContractFactory = await hre.ethers.getContractFactory("GasTracker");

    // Step 2: Deploy the contract
    const gasTrackerContract = await GasTrackerContractFactory.deploy();

    // Step 3: Wait for the deployment to complete
    await gasTrackerContract.deployed();

    console.log("GasTracker contract deployed to address:", gasTrackerContract.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
