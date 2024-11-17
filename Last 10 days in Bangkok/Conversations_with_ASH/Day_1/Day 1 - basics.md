# what is a smart contract


A smart contract is a type of software that focuses on transactions between pieces of logic. 
what makes them unique is that they are immutable and deterministic - meaning, that because they are pieces of logic that exist on a blockchain, the history and information that goes into their execution is unchangable and consistently recreatable. 

Because of this nature of blockchains - this means that you can have 'trustless' agreements between two parties. This means you can have two individuals who do not know each other, transact in a reliable 'trustable' way, without 'counterparty' risk.

Now some of this language is not fully appropriate for everything that a smart contract can do, but that is what sets it apart from traditional software. And because of this, you can have reliable decentralized systems capable of performing all sorts of tasks.

### Points to Respond To

- **Immutability and Determinism**: Could you expand on how these characteristics benefit users of a smart contract in practical terms? Try to think of a specific example, like how this quality might help in a decentralized finance (DeFi) context.

- **Trustless Agreement Example**: Provide an example of a real-world scenario where two individuals might benefit from using a smart contract to make an agreement without needing to trust one another.


Immutablility and determinism allow users of smart contracts, and blockchains in general, the ability to trust that these 'pieces of logic' or software, will have the same, predictable results, given a certain set of conditions. This means that they can trust it to be consistent. 

this is important in areas like de-fi because there is a need for reliability in the transactions. People need to know that the value going into these systems and coming out of these systems is accurate and reliable. Part of what is important to blockchains in general is that they can be clear and transparent systems - meaning all the information on the transactions is public and visible.

A specific example could be a situation where there needs to be reliability in that I paid something. A trustless example could be as simple as paying for goods online. Proof that I paid, and proof that I sent it, without requiring a middleman to handle the interaction.

### **Transparency vs. Centralized Systems**: 

How does the transparency of a smart contract compare to using a centralized system like a bank? What kinds of advantages does this bring for financial services?

It makes all parties accountable for what is done, and allows for parties to be more willing to take on risk, with the understanding that all the information influencing the system is apparent. In centralized institutions, like banks or even governments, there is a need to 'trust the institution', but history has many examples where these instutions did not execute according to the commitments they made or leveraged their position to manipulate the situation.

### **Escrow in Practice**

Consider the example of a smart contract being used as an escrow for purchasing property. What elements does the smart contract replace, and what new assurances does it provide compared to a traditional escrow service?

It basically replaces the services that a transaction company provides as a middleman. It allows individuals to make commitments to each other in a specific and reliable manner, transparently to each other, without the needs for these added costs. 

## ### **Technical Practice Areas**

To build strong coding muscle memory, we should focus on small, repeatable exercises that help you internalize key Solidity patterns and concepts. Here are a few practice areas we can work through:

1. **Basic Contract Structures**:
    
    - Write simple smart contracts to get the hang of structuring contracts, defining state variables, and writing functions.
    - Focus on repeating common Solidity constructs: visibility specifiers, state changes, using mappings, etc.
2. **Common Patterns**:
    
    - Practice implementing typical Solidity patterns like "Ownable," "Pausable," or modifier functions.
    - These are key for contract security and control flow, and repeating them will help make writing these second nature.
3. **Token Contracts**:
    
    - Write an ERC20 or ERC721 token contract from scratch. We can do it step-by-step without reference, aiming to commit the structure and key parts to memory.
    - Focus on adding functionality like minting, burning, transferring, and approving.
4. **Security Patterns**:
    
    - Practice implementing reentrancy guards, require statements, and thinking about the contract’s state transitions to solidify secure coding.
    - Create a vulnerable contract, then fix it, so you understand both the mistakes and the proper patterns.

#### **Exercise 1: Write a Simple Storage Contract**

**Goal**: Practice defining state variables, getters, and setters.

- Write a contract named `SimpleStorage` that has one state variable called `storedValue` of type `uint`.
- Write a function to set the value and another function to get the value.
- Add modifiers to enforce that only the owner can set the value.


#### **Exercise 2: Implement the Ownable Pattern**

**Goal**: Practice control patterns like "Ownable."

- Create a contract called `OwnableExample`.
- Define an owner state variable, and set it during contract deployment.
- Write a `modifier` called `onlyOwner` that restricts access to certain functions.
- Create a function called `changeOwner` that allows the current owner to set a new owner.

# We then worked back and forth


