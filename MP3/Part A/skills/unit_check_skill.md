---
name: engineering-unit-conversion-review
description: >
  Scan engineering text (requirements, specs, reports, drawings notes)
  and flag likely unit-conversion errors, mixed-unit misuse, and
  numerically inconsistent values.
---

# Skill: Engineering Unit Conversion Review

## When to use this skill

Trigger this skill any time the user presents some text that contains different units and a conversion between them — and asks for a review, critique, or "what's wrong with this." 

## Steps

1. **Identify the Units Mentioned.** inch, psi, in-lb, lbf, °F? Different types of units have different uses and transformations

2. **Compute the Conversion between Units.** What should the units be when converted? What's the equivilent of the initial unit in another format?

3. **Confirm Document Conversion.** Are the conversions you made the same as the ones written on the document? Is there a difference in units?

## What to flag

- Conversion between units that do not represent the same thing? (Inches to Fahrenheit)
- Incorrect Conversions between units (1 inch not equaling 25.4 mm)

## What NOT to do

- Do NOT invent conversions that aren’t in the text.  
If the user didn’t provide both numbers, don’t guess the intended converted value.

- Do NOT assume the user’s intended unit system.  
If the text mixes SI and Imperial, flag it — don’t decide which one they “meant.”

- Do NOT silently correct numbers.  
Always report the inconsistency; never output a “fixed” value unless the user explicitly asks.

- Do NOT infer physical meaning from context you don’t have.  
If a value looks odd but isn’t explicitly a conversion, don’t label it an error.

- Do NOT treat approximate engineering conversions as exact.  
Many fields use rounded factors (e.g., 1 in ≈ 25 mm). Flag only when the mismatch is clearly outside reasonable tolerance.

## Output format

Return findings as a numbered list, most-critical first. Each finding
should include: (1) what you see, (2) why it's a problem, (3) a concrete
fix. End with a one-sentence verdict ("only correct conversions," or "incorrect conversions detected").