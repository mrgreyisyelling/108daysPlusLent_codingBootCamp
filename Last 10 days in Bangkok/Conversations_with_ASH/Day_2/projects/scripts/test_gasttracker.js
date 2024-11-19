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
    await tx.wait();
    

    // test gasIntermediate
    console.log("Test Gas Intermediate");
    seedNumber = 25;
    tx = await gasTracker.gasIntermediate(seedNumber);
    await tx.wait();

    // test gasHeavy
    console.log("Test Gas Heavy");
    seedNumber = 25;
    tx = await gasTracker.gasHeavy(seedNumber);
    await tx.wait();
   
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });