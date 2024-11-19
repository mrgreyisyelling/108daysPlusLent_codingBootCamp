Here’s how to set up Hardhat step by step:

---

### **Step 1: Install Hardhat**
1. Open your terminal in the project folder.
2. Run the following command to install Hardhat as a development dependency:
   ```bash
   npm install --save-dev hardhat
   ```

---

### **Step 2: Initialize a Hardhat Project**
1. Create a new Hardhat configuration:
   ```bash
   npx hardhat
   ```
2. Select **"Create an empty Hardhat.config.js"** for now.

---

### **Step 3: Install Additional Dependencies**
1. Install the **Ethers.js** library and the Hardhat plugin for it:
   ```bash
   npm install --save-dev @nomiclabs/hardhat-ethers ethers
   ```
2. Install the dotenv package (optional, for managing environment variables like private keys):
   ```bash
   npm install dotenv
   ```

---

### **Step 4: Directory Structure**
1. In your project folder, create the following directories:
   - `contracts`: For your Solidity files.
   - `scripts`: For deployment and interaction scripts.
   - `test`: For your test files.

---

### **Step 5: Add Your Solidity Contract**
1. Save your `SimpleStorage` contract in the `contracts` folder:
   - File path: `contracts/SimpleStorage.sol`.

---

### **Step 6: Compile the Contract**
1. Compile your contract to ensure there are no syntax errors:
   ```bash
   npx hardhat compile
   ```
2. If successful, the compiled artifacts will appear in the `artifacts` and `cache` folders.

---

### **Step 7: Deploy the Contract**
1. Create a deployment script in the `scripts` folder:
   - File path: `scripts/deploy.js`.
   - Example content:
     ```javascript
     const hre = require("hardhat");

     async function main() {
         const SimpleStorage = await hre.ethers.getContractFactory("SimpleStorage");
         const storage = await SimpleStorage.deploy();
         await storage.deployed();

         console.log("SimpleStorage deployed to:", storage.address);
     }

     main().catch((error) => {
         console.error(error);
         process.exitCode = 1;
     });
     ```

2. Run a local Hardhat node:
   ```bash
   npx hardhat node
   ```

3. Deploy the contract:
   ```bash
   npx hardhat run scripts/deploy.js --network localhost
   ```

---

### **Step 8: Interact with the Contract**
1. Open the Hardhat console:
   ```bash
   npx hardhat console --network localhost
   ```
2. Interact with the deployed contract:
   ```javascript
   const storage = await ethers.getContractAt("SimpleStorage", "deployed_contract_address");

   // Get the stored value
   await storage.getValue();

   // Set a new value (replace '42' with a number greater than 10)
   await storage.setValue(42);
   ```

---

Let me know if you need further clarification or hit any roadblocks!