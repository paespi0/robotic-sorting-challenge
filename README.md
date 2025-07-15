# Robotic Package Sorting Function

This project contains a function that determines how robotic arms in Thoughtful’s automation factory should sort packages based on their size and weight.

## 🧠 Logic

A package is:
- **Bulky** if volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm
- **Heavy** if mass ≥ 20 kg

### Stack Rules:
- `REJECTED`: Both bulky and heavy
- `SPECIAL`: Either bulky or heavy
- `STANDARD`: Neither bulky nor heavy

## 🚀 Function

```python
sort(width, height, length, mass) -> str
