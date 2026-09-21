# Acceptance criteria — The Unofficial Guide
---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
Less than 80% pass rate would be a 60% pass rate which is failure, to account for the model struggling with one question is fair.
---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
Every question has a source document that is related and holds the answer, if that document is not found then something is wrong with the pipeline.
---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

**Why this target:**
This is a good target because maybe in one scenario their could be a hallucination about a source document having a relation to the question, but anything more than that would mean that their is not a high enough cutoff for their to be recongition of what there is no source knowledge of.
---

## 4. No chunk is over 400 characters.

**Why this target:**
I picked this target because in this corpus most useful information sits in a single sentence so no long chunks are needed.
---

## 5. Each response should take no longer than 5 seconds.

**Why this target:**
The answers to these questions are simple and require only pulling from one document chunk each, the response should be relatively quick.
---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
