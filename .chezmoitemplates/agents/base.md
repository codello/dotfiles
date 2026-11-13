# Global Agent Instructions

If you are not sure what the user means or how the user's instruction relate to the existing code, aks for clarification. Do not blindly guess. Do not immediately scan upstream code if the user may be able to provide clarification with a simple question.

The user's GitHub name is {{ .github }}.

## Comments

Write comments using ASD-STE100 Simplified Technical English.

Comments describe intent and constraints, not implementation. When a change only alters the implementation of already-commented code (bug fix, refactor) and the documented behavior stays the same, keep the existing comments unchanged — do not reword, expand, or explain the new mechanism. Only touch a comment when it becomes factually wrong, or when the documented behavior itself changes.

Keep the length of code comments short. Do not write redundant comments that describe the code. Only write comments if an explanation is needed, why the code looks like it does.

Make sure that comments only relate to the code in its final state. Do not write comments that can only be understood in the context of a diff. Do not comment why a certain approach was NOT chosen. Remove any historical approaches when the corresponding code is removed/updated. Do not document alternatives that were considered but not implemented.

## Documentation

Write documentation using ASD-STE100 Simplified Technical English.

Documentation (READMEs, docstrings, etc.) formalizes contracts. It should be clear and concise and should not contain any implementation details.
Not every behavior has to be part of the contract. If a behavior is not documented, it is not guaranteed to be stable and may change in the future. Explicitly mentioning "contract", "undefined behavior", "not guaranteed" or similar is a rare exception that should only be used when there is a high risk of confusion. If you are unsure whether a behavior is part of the contract, ask for clarification.
A behavior-preserving change (bug fix, refactor) must not alter documentation. Documentation changes require a contract change."
Do not duplicate documentation in multiple places.

When a refactor makes documentation partially stale — for example a reference to code that was removed or renamed — make the minimal edit that removes the stale reference. Do not merge, expand, or relocate the documentation of removed code into surviving documentation, and do not use a necessary doc edit as an occasion to improve the surrounding text: a behavior-preserving refactor does not change the surviving contract, so its documentation stays as it is.

## Design Decisions

Sometimes the user may make questionable design decisions. Do not blindly follow them. If you think a design decision is questionable, push back on it. If the user insists on a questionable design decision, you may implement it, but you should also provide a warning about the potential consequences.
