const { ethers } = require("hardhat");

async function main() {
    // Replace with your deployed contract address
    const contractAddress = "0x5FbDB2315678afecb367f032d93F642f64180aa3";

    // Get the signer (default first account in Hardhat node)
    const [deployer] = await ethers.getSigners();
    console.log("Using account:", deployer.address);

    // Connect to the deployed Wallet contract
    const wallet = await ethers.getContractAt("Wallet", contractAddress);

    // Check the owner
    const owner = await wallet.owner();
    console.log("Owner address:", owner);

    // Get contract balance
    const balance = await wallet.getContractBalance();
    console.log("Contract Balance:", ethers.utils.formatEther(balance), "ETH");

    // Deposit Ether into the contract
    console.log("Depositing 1.0 ETH...");
    const depositTx = await wallet.depositEth({ value: ethers.utils.parseEther("1.0") });
    await depositTx.wait();
    console.log("Deposit successful!");

    // Check individual balance
    const individualBalance = await wallet.getIndividualBalance();
    console.log("Individual Balance:", ethers.utils.formatEther(individualBalance), "ETH");

    // Withdraw Ether (only if you're the owner)
    console.log("Withdrawing 0.5 ETH...");
    const withdrawTx = await wallet.withdraw(ethers.utils.parseEther("0.5"));
    await withdrawTx.wait();
    console.log("Withdrawal successful!");

    try {
        
        const withdrawalAmount = ethers.utils.parseEther("1.0"); // Define withdrawal amount in Ether

        if (balance.lt(withdrawalAmount)) {
            console.error("Withdrawal failed: Not enough funds in the contract.");
            return;
        }
    
        if (individualBalance.lt(withdrawalAmount)) {
            console.error("Withdrawal failed: Not enough individual balance.");
            return;
        }
        
        console.log("Attempting to withdraw 1.0 ETH...");
        const withdrawTx = await wallet.withdraw(ethers.utils.parseEther("1.0"));
        await withdrawTx.wait();
        console.log("Withdrawal successful!");
    } catch (error) {
        console.error("Withdrawal failed:", error.message);
    }

    // Check balances again
    const newContractBalance = await wallet.getContractBalance();
    console.log("Updated Contract Balance:", ethers.utils.formatEther(newContractBalance), "ETH");

    const newIndividualBalance = await wallet.getIndividualBalance();
    console.log("Updated Individual Balance:", ethers.utils.formatEther(newIndividualBalance), "ETH");
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
