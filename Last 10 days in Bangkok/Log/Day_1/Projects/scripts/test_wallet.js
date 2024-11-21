// scripts/test_wallet.js

const hre = require("hardhat");

async function main() {
  const [owner, user] = await hre.ethers.getSigners();

  console.log("Using account:", owner.address);

  // Deploy Wallet contract
  const Wallet = await hre.ethers.getContractFactory("Wallet");
  const wallet = await Wallet.deploy();
  await wallet.deployed();

  console.log("Wallet contract deployed to:", wallet.address);

  // Initial state
  console.log("Owner address:", await wallet.owner());
  console.log("Contract Balance:", hre.ethers.utils.formatEther(await wallet.getContractBalance()));

  // Deposit ETH
  console.log("Depositing 1.0 ETH...");
  let tx = await wallet.connect(owner).depositEth({ value: hre.ethers.utils.parseEther("1.0") });
  await tx.wait();
  console.log("Deposit successful!");

  // Check individual balance
  console.log("Individual Balance:", hre.ethers.utils.formatEther(await wallet.getIndividualBalance()));

  // Withdraw ETH
  console.log("Withdrawing 0.5 ETH...");
  tx = await wallet.connect(owner).withdraw(hre.ethers.utils.parseEther("0.5"));
  await tx.wait();
  console.log("Withdrawal successful!");

  // Attempt to transfer ownership
  console.log("Transferring ownership...");
  tx = await wallet.transferOwnership(user.address);
  await tx.wait();
  console.log("Ownership transfer initiated!");

  console.log("Accepting ownership...");
  tx = await wallet.connect(user).acceptOwnership();
  await tx.wait();
  console.log("Ownership transfer completed!");

  // Pause and Unpause
  console.log("Pausing the contract...");
  tx = await wallet.connect(user).setPause(true);
  await tx.wait();
  console.log("Contract paused!");

  try {
    console.log("Attempting to deposit 1.0 ETH while paused...");
    await wallet.connect(user).depositEth({ value: hre.ethers.utils.parseEther("1.0") });
  } catch (error) {
    console.error("Deposit failed:", error.message);
  }

  console.log("Unpausing the contract...");
  tx = await wallet.connect(user).setPause(false);
  await tx.wait();
  console.log("Contract unpaused!");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
