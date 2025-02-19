# Package Sort
Sorts packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

The sort function returns the following:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

## Directions
- Download and run `sort.py` to test the function
- Provide inputs as prompted

## Test Results
| Width | Height | Length | Mass | Output |
|--------|--------|--------|--------|--------|
| 0 | 1 | 1 | 1 | `Error: Inputs must be greater than 0` |
| 1,2 | 1.2 | 1.2 | 1.2 | `Error: Inputs must be properly formatted as floats` |
| 99.9 | 99.9 | 99.9 | 19.9 | `STANDARD` |
| 150 | 10 | 10 | 10 | `SPECIAL` |
| 10 | 10 | 10 | 20 | `SPECIAL` |
| 150 | 1 | 1 | 20 | `REJECTED` |
| 100 | 100 | 100 | 20 | `REJECTED` |
