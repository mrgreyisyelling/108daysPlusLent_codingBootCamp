const { ethers } = require("hardhat");

async function main() {
    // Get the first signer (deployer)
    const [deployer] = await ethers.getSigners();

    console.log("Deploying contracts with the account:", deployer.address);

    // Deploy the Wallet contract
    const Wallet = await ethers.getContractFactory("Wallet");
    const wallet = await Wallet.deploy();

    await wallet.deployed();

    console.log("Wallet contract deployed to:", wallet.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
