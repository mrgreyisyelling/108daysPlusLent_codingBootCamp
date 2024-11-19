### **Project 3: Voting System**

#### **Objective**
Create a voting system where:
1. Users can vote on proposals.
2. Each user can vote only once per proposal.
3. Only the owner can create proposals.

---

#### **Requirements**

1. **Tracking Proposals**:
   - Use a `mapping(uint => uint)` to keep track of the number of votes each proposal receives.
   - Each proposal is identified by a `proposalId` (an unsigned integer).

2. **Tracking Voter Participation**:
   - Use a `mapping(address => mapping(uint => bool))` to track whether a user has voted for a specific proposal.

3. **Ownership**:
   - Only the contract owner can create new proposals.
   - Add an `onlyOwner` modifier to enforce this.

4. **Core Functions**:
   - **Create Proposal**:
     - Accepts a `string memory description` as input.
     - Generates a unique `proposalId` and stores the description.
   - **Vote**:
     - Accepts a `proposalId` as input.
     - Checks if the user has already voted.
     - Updates the vote count for the proposal.
   - **Get Votes**:
     - Accepts a `proposalId` as input.
     - Returns the total number of votes for that proposal.

5. **Events**:
   - **ProposalCreated**:
     - Logs the `proposalId` and `description`.
   - **VoteCast**:
     - Logs the `proposalId` and `voter address`.

---

#### **Abstract Pseudo Code**

1. **State Variables**:
   - A `mapping` to track votes for proposals.
   - A `mapping` to track if a user has voted.
   - A `struct` (optional) to store the proposal description.

2. **Modifiers**:
   - `onlyOwner`: Ensures only the owner can create proposals.

3. **Functions**:
   - `createProposal(description)`:
     - Increment a `proposalCounter` for unique IDs.
     - Map the `description` to the proposal.
     - Emit `ProposalCreated`.

   - `vote(proposalId)`:
     - Check if the `proposalId` exists.
     - Verify if the user has already voted.
     - Increment the vote count for the proposal.
     - Mark the user as having voted.
     - Emit `VoteCast`.

   - `getVotes(proposalId)`:
     - Return the vote count for the `proposalId`.

---

Take this and start implementing! Let me know how you'd like to approach the logic, and I can guide you step-by-step.