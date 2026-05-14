# Reflection

# MP3 to MP4 Transtition

### What I productized:  
> I turned the iterative design‑review workflow into a repeatable pipeline — prompt → AI analysis → stress verification → design revision → drawing generation. What used to require manual calculation and CAD setup now runs automatically through the stack: gear ratio selection, Lewis bending checks, and printable geometry validation. The AI can now produce dimensioned drawings and stress tables directly from requirement text.

### Where the stack breaks:  
> It still struggles with contextual judgment — when assumptions shift (e.g., material quality, torque source, or print orientation), the model doesn’t always re‑anchor its equations. It also can’t yet handle multi‑part assemblies with dynamic constraints or tolerance propagation across mating components. In short, it’s strong on single‑part logic, weak on system‑level reasoning.

### Next move for MP4:  
> MP4 will focus on working the entire assembly, not just isolated parts. The goal is to make the AI understand how components interact — tolerances, load paths, and motion constraints — so it can reason across the full mechanical system. Instead of optimizing one gear, MP4 will iterate the whole MiniClaw assembly, verifying fit, function, and manufacturability as a unified design.

### Trust ledger:

> Success: My skill caught the material‑strength mismatch early (PLA at 25–30 MPa), forcing the AI to redesign with larger module and face width — that saved the gear from theoretical failure.

> Miss: The AI confidently chose m = 1.5 mm before checking undercut limits; my skill didn’t flag the 12‑tooth risk soon enough. That’s the blind spot — trusting clean math before verifying geometry.