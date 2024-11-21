# Checklist of Topics Covered in RWA Bootcamp

## 1. Introduction and Recap of Day 1
- Overview of Day 1 Topics
  - Introduction to real-world asset tokenization.
  - Deployed initial smart contracts for tokenizing real estate.
  - [ ] Tokenization concept explained.
  - [ ] Smart contract deployment discussed.
- Gitbook and Resources
  - Provided URL for Gitbook resource.
  - Access details for Day 1 recordings on YouTube.
  - [ ] Gitbook URL shared.
  - [ ] YouTube video resource available.

## 2. Tokenization of Real Estate
- ERC 1155 Standard for Real Estate
  - Explanation of ERC 1155 and its use for real estate assets.
  - Benefits of ERC 1155 for representing non-fungible assets with fungible components.
  - [ ] ERC 1155 as a token standard.
  - [ ] Representation of real estate assets.
- Mock Real Estate using Zillow API
  - Use of Zillow API to retrieve mock real estate data.
  - Tokenizing the real estate as an ERC 1155 token.
  - [ ] Zillow API integration.
  - [ ] Mock data usage in tokenization.

## 3. Day 2 Exercises
- Focus on Practical Development
  - Recap of Day 1 and preparation for Day 2 exercises.
  - Emphasis on minimal theory and focus on coding and practical engineering.
  - [ ] Recap of Day 1.
  - [ ] Practical development focus.
- Overview of Exercises
  - Lending/Borrowing platform using real estate as collateral.
  - Implementation of a simple English auction contract.
  - [ ] Lending and borrowing use case.
  - [ ] English auction explained.

## 4. ERC 1155 Token and Usage
- Deploying the ERC 1155 Token Contract
  - Creation of a smart contract to represent tokenized real estate.
  - [ ] Smart contract for ERC 1155 deployment.
- Issuer Smart Contract
  - Minting of ERC 1155 tokens for real estate.
  - Issuance of tokens to the wallet address (e.g., Alice).
  - [ ] Token minting process.
  - [ ] Token issuance to owners.

## 5. Fractional Ownership of Real Estate
- Tokenizing Fractional Ownership
  - Each ERC 1155 token represents a share of the property.
  - Example: Alice owning 100% of tokens, transferring 25% to Bob.
  - [ ] Fractional ownership concept.
  - [ ] Token transfers to other users.
- Calculation of Ownership
  - Demonstrating ownership split, e.g., transferring 5 out of 20 tokens.
  - Calculation of new ownership percentages between Alice and Bob.
  - [ ] Ownership calculation with examples.
  - [ ] Transfer and distribution percentage recalculation.

## 6. Use Cases
- Lending and Borrowing using Tokenized Real Estate
  - Creating a minimal lending/borrowing platform for real estate tokens.
  - Mock lending using fractional shares as collateral.
  - [ ] Lending platform concept.
  - [ ] Collateralized borrowing explained.
- English Auction Implementation
  - Auctioning fractional shares of tokenized real estate.
  - Introduction to English and Dutch auctions.
  - Smart contract setup for decentralized auctioning.
  - [ ] English auction smart contract.
  - [ ] Dutch auction overview.

## 7. Smart Contract for Lending and Borrowing
- Leveraging Chainlink Price Feeds
  - Use of Chainlink price feeds to determine USD valuation of assets.
  - Importance of accurate price feeds for valuation calculations.
  - [ ] Chainlink price feed integration.
  - [ ] USD valuation using Chainlink.
- Collateralized Lending with Tokenized Real Estate
  - Locking ERC 1155 tokens as collateral.
  - Issuing USDC loans based on the valuation of the collateral.
  - [ ] Collateral concept and token locking.
  - [ ] Issuing loans against real estate collateral.
- Loan Amount and Liquidation Threshold
  - Calculation of Loan-to-Value (LTV) ratio.
  - Hardcoded values for initial and liquidation thresholds.
  - [ ] Loan-to-Value ratio calculation.
  - [ ] Liquidation threshold setting.

## 8. Slippage Protection and Loan Repayment
- Slippage Tolerance in Lending/Borrowing
  - Protecting against price slippage when issuing loans.
  - Setting minimum loan amounts to avoid loss due to price manipulation.
  - [ ] Slippage protection mechanism.
  - [ ] Minimum loan amount parameters.
- Mechanism for Loan Repayment
  - Repaying USDC to release ERC 1155 tokens from collateral.
  - Liquidation conditions if the asset’s value drops below the threshold.
  - [ ] Loan repayment procedure.
  - [ ] Liquidation process explained.

## 9. Chainlink Price Feeds Integration
- Converting USD Valuation to USDC
  - Use of Chainlink price feeds to convert USD value to USDC.
  - Handling stablecoin fluctuations between 0.99 and 1.01 USD.
  - [ ] Conversion from USD to USDC.
  - [ ] Handling stablecoin fluctuations.
- Decimal Handling in Price Feeds
  - Importance of considering feed decimals.
  - Normalizing valuations to match USDC token decimals.
  - [ ] Decimal handling in price feeds.
  - [ ] Normalizing valuation to correct decimals.
- Avoiding Hardcoding of Stablecoin Values
  - Risks associated with hardcoding 1 USDC as $1.
  - Ensuring calculations are dynamic and accurate.
  - [ ] Risks of hardcoding stablecoin values.
  - [ ] Dynamic calculations for stablecoin integration.

## 10. Exercise Walkthrough and Code Review
- Detailed Explanation of the Lending Contract
  - Walkthrough of the key functions: borrowing, repaying, and liquidation.
  - Emphasis on understanding design decisions and contract architecture.
  - [ ] Borrow function breakdown.
  - [ ] Repay and liquidation function overview.
- Security and Interaction Patterns
  - Use of non-reentrant modifiers to prevent attacks.
  - Following the Checks-Effects-Interactions pattern for safe operations.
  - [ ] Non-reentrancy for contract security.
  - [ ] Checks-Effects-Interactions pattern.
- ERC 1155 Receiver Implementation
  - Handling the receipt of ERC 1155 tokens within the smart contract.
  - Validation of sender and implementation of `onERC1155Received`.
  - [ ] ERC 1155 receiver function implementation.
  - [ ] Validation of token sender.

## 11. Deployment Steps
- Deployment to Avalanche Fuji Testnet
  - Setting up and deploying contracts on Avalanche Fuji.
  - Providing parameters such as token addresses and Chainlink aggregator address.
  - [ ] Deploying to Avalanche Fuji.
  - [ ] Required parameters for deployment.
- Dependencies for Deployment
  - Requirements for USDC token and price feed aggregator.
  - Steps for using Chainlink to automate price updates.
  - [ ] USDC token requirements.
  - [ ] Using Chainlink for price automation.

## 12. Summary and Questions
- Recap of Key Concepts
  - Review of real estate tokenization, lending, and auction concepts.
  - Reinforcement of Chainlink’s role in price feed integration.
  - [ ] Real estate tokenization summary.
  - [ ] Chainlink price feed importance.
- Q&A Session
  - Addressing participant questions.
  - Invitation to continue learning through follow-up resources and Discord discussions.
  - [ ] Participant Q&A summary.
  - [ ] Follow-up learning resources.

