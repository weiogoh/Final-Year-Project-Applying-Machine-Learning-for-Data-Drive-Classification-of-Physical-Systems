# Applying Machine Learning for Data Drive Classification of Physical Systems

Project Overview
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

This repository hosts a computational framework designed to automate the classification of chemical hazards under the UN Globally Harmonised System (GHS). Traditional laboratory evaluations and expert-led assessments often fail to scale effectively due to significant cost and time constraints. By processing a dataset of 159,562 chemical records from PubChem, this research benchmarks ten machine learning algorithms against nine distinct hazard pictograms.The framework addresses three fundamental challenges in biochemical informatics: high feature dimensionality, extreme class imbalance and predictive stability.

Significant Research Findings
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Restoration of Rare Hazard Signals
A core contribution of this study is the recovery of predictive signals for low-frequency hazards. In its raw state, the Explosive category (representing just 0.08% of the dataset) was virtually undetectable.
The Result: By implementing a filtered balancing strategy, the F1-score for Explosives surged from 0.0817 to 0.9497, a 1,061% improvement in detectability.

2. Exposing the "Accuracy Trap"
The analysis confirms that Accuracy is a deceptive metric for safety-critical systems.
The Observation: For rare hazards like Compressed Gas or Explosives, several models returned accuracy scores exceeding 99.9% while failing to identify a single positive hazard case.
The Standard: This project prioritises the F1-score to ensure a meaningful balance between precision and recall, ensuring high-risk triggers are not ignored.

3. The Scientific Bridge: Molecular Descriptors
The models successfully learned genuine chemical principles rather than arbitrary patterns.
Biological Reactivity: Health hazards (Irritants) prioritised descriptors like TPSA and Hydrogen Bond Acceptor count, which govern interaction with living tissue.
Physical Drivers: Physical hazards (Explosives, Compressed Gas) prioritised Mass and Molecular Weight, which drive kinetic energy and bulk behaviour.

4. The "Irritant Artifact" Warning
The research documents a statistical anomaly where the balanced Irritant model achieved 1.0 Accuracy but 0.0 F1-score. This was caused by extreme dataset homogeneity and serves as a vital warning that perfect accuracy can be a mathematical illusion if class diversity is lost during data splitting.

The Main Controller: A 10-Circuit Machine
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Main_Controller in part 2 acts as the central "engine" of this framework.

- Operational Concept: The controller is designed like a machine containing 10 independent circuit lines, each representing a specific machine learning algorithm.

- Selection Logic: Upon execution, you select which "circuits" the data will flow through by entering the corresponding model numbers.

- Targeted Execution: Only your chosen models will activate, allowing for modular testing of specific algorithms without running the entire suite.

- Usage Recommendation: While the system supports running multiple models simultaneously, it is highly recommended to run them one-by-one.

- Resource Management: High-complexity models require significant RAM and processing time to evaluate all feature interactions.

- System Integrity: Running one circuit at a time prevents memory overflows and ensures that the large result files are generated cleanly without system crashes.

Repository Roadmap
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

The repository is organised into three distinct phases to ensure full scientific transparency and reproducibility:-

Part 1: Feature Selection and Reduction
Pre-processing of raw PubChem data and identification of the 7 primary molecular descriptors (Complexity, XLogP3, Monoisotopic Mass, TPSA, Exact Mass, Molecular Weight and HBA count).
Details: See /Part 1 Feature Selection/README.md

Part 2: Model Evaluation
Exhaustive benchmarking of 10 algorithms across 127 unique feature combinations per hazard class.
Details: See /Part 2 Modal Evaluation/README.md

Part 3: Balancing Analysis
Comparative analysis between imbalanced and balanced environments, using Dartboard Plots to measure predictive consistency across 150 runs.
Details: See /Part 3 Balancing Analysis/README.md

Future Direction: Multi-Binary "1+1" Architecture
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

We propose a final architecture for automated Safety Data Sheet (SDS) generation consisting of nine specialised, parallel binary sub-classifier. To enhance reliability, we recommend a Voting Ensemble that flags conflicting model predictions for mandatory human expert review, creating a robust regulatory safety net.

Tech Stack
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Language: Python 3.x

- Data Handling: Pandas, NumPy

- Machine Learning: Scikit-learn

- Visualisation: Matplotlib (Heatmaps and Dartboard Plots)

- Logic: itertools and re (Regex)
