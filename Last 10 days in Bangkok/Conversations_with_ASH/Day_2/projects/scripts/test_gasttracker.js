// scripts/test_GasTracker.js

const hre = require("hardhat");

async function main() {
    const [owner, user_1, user_2] = await hre.ethers.getSigners();

    console.log("Using Account:", owner.address);

    // Deploy GasTracker
    const GasTracker = await hre.ethers.getContractFactory("GasTracker");
    const gasTracker = await GasTracker.deploy();
    await gasTracker.deployed();

    console.log("GasTracker contract deployed to:", gasTracker.address);

    // test gas light
    console.log("Test Gas Light");
    seedNumber = 25;
    tx = await gasTracker.gasLight(seedNumber);
    receipt = await tx.wait();
    console.log("Test Gas Light::Gas Used::", receipt.gasUsed.toString());

    // test gasIntermediate
    console.log("Test Gas Intermediate");
    seedNumber = 25;
    tx = await gasTracker.gasIntermediate(seedNumber);
    receipt = await tx.wait();
    console.log("Test Gas Intermediate::Gas Used::", receipt.gasUsed.toString());

    // test gasHeavy
    console.log("Test Gas Heavy");
    seedNumber = 25;
    tx = await gasTracker.gasHeavy(seedNumber);
    receipt = await tx.wait();
    console.log("Test Gas Heavy::Gas Used::", receipt.gasUsed.toString());
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });