# The Unofficial Guide

Yosias Redi campus_life

---

# Unit 1

## What This Does

This project uses the campus_life corpus, which contains short posts about student experiences and campus life. The system is designed to answer questions about student activities, experiences, and opinions about campus. Because the documents are relatively short and contain focused pieces of information, the retrieval system works well with smaller, focused chunks.

## Chunking Strategy

**Chunk size:**
A 400-character chunk works well for this corpus because the documents are mostly short posts with relatively concise pieces of information. It keeps related information together while making the retrieved chunks focused and easy to read.
**Overlap:**
I chose an overlap of 0 because the corpus consists mostly of short, self-contained posts and paragraphs. Keeping paragraphs intact without repeating text between chunks reduces redundancy while still preserving the main ideas.

## Sample Chunks


**Chunk 1** — source: `admin_add_drop_deadline.txt#0 ` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_cs_210.txt#0` — produced by: `chunker.py::split_documents`

```
CS 210 Data Structures

I'm a junior and I've done this twice now. Format is lecture with weekly labs; slides go up after class, not before. Assessment: two midterms and a final, all drawn from lecture material rather than the textbook. Midterms are curved, the final is not.

Expect 8 to 10 hours a week outside class.
```

**Chunk 3** — source: `course_math_220_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for MATH 220 Linear Algebra

People keep asking so: 6 to 8 hours a week, almost all of it on problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_the_ridgeway_cafe_followup.txt#0 ` — produced by: `chunker.py::split_documents`

```
Re: The Ridgeway Café

Adding to what people have said about The Ridgeway Café. The wait figure of 10 to 15 minutes at 12:30 matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: seating is tight; about 40 seats for a building of 900. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_morrow_house.txt#0 ` — produced by: `chunker.py::split_documents`

```
Morrow House — what it's actually like

Just finished a year in this building. Built 1954, partially renovated 2008. Rooms are singles and doubles, hall bathrooms.

The good: cheapest housing tier by about $900 a year, and the singles are real singles.

The bad: known damp problem on the ground floor; two rooms were taken offline in 2024.

```

## Sample Answer

**Question:**
What is the deadline for a student to drop a course?
**Answer:**

```
The deadline to drop a course is through the end of week six. 

Source: admin_withdrawal_deadline.txt (also mentioned in admin_add_drop_deadline.txt)
```

**My relevance cutoff:**
.55, The in corpus questions had a best distance averaging around just below .3, while out of corpus had best distance averaging just over .8. Halfway between .8 and .3 is .55.

| Question | In corpus? | Best distance |
|---|---|---|
| What is the deadline for a student to drop a course? | Y | 0.3027 |
| How much of a printing quota does a student have each semester? | Y | 0.3208 |
| How many hours per week can a student book a study room? | Y | 0.2489 |
| How much does it cost to wash and dry my clothes at the old brewhouse building? | Y | 0.2166 |
| How long after a grade is posted does a student have time to appeal? | Y | 0.1562 |
| What is the capital of Mongolia? | N | 0.8246 |
| How do I change the oil in a diesel engine? | N | 0.9340 |
| Who won the 1994 World Cup? | N | 0.8859 |
| What is the recommended dosage of ibuprofen for a headache? | N | 0.8442 |
| How do I write a for loop in Rust? | N | 0.8960 |

## How I Used AI

**1.**
I used AI to help write the chunking functon from my notes, it ruined the current chunker i have written in split_documents but I ignored the 50 character overlap it suggested to me.

**2.**
I asked AI to help me come up with a testable creative criteria.

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. No chunk is over 400 characters | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Each response takes under 5 seconds | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

All five questions, run 1, from `results/run_2026-09-23_2053.md`.

### Criterion 1 — Retrieved chunk contains the answer — 3/5

`chunker.py::split_documents` → `store.py::search` → `scorer.py::judge`

```
admin_add_drop_deadline.txt, distance 0.303, expects 'week six' -> pass

On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

```
admin_printing_quota.txt, distance 0.321, expects '$30' -> pass

On the printing quota

Every student gets $30 of printing per semester, which is roughly 600 black-and-white pages. It does not roll over. Colour costs eight times as much per page, which people discover after printing one poster.
```

```
study_group_rooms.txt, distance 0.250, expects 'four hours' -> fail

Booking a group study room

Rooms book two weeks ahead through the library site, in two-hour blocks, maximum two blocks per person per week. The limit is per person, so a group of four can chain together eight hours if they coordinate.

Rooms 210 and 211 have whiteboards that actually erase. The others don't and no amount of scrubbing helps.
```

```
housing_old_brewhouse_laundry.txt, distance 0.225, expects '$3.00' -> fail

Laundry in Old Brewhouse

Machines take $1.50 wash, $1.50 dry, coin only, and the machines are old. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.

Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.
```

```
admin_grade_appeals.txt, distance 0.156, expects 'fifteen' -> pass

On the grade appeals

A grade appeal starts with the instructor and has to be raised within fifteen days of the grade posting. Only after that does it go to the department. Skipping the instructor step gets the appeal returned, which wastes most of the fifteen days.
```

### Criterion 2 — Every answer names a source — 5/5

`generate.py::answer_from_chunks`

```
Based on the documents, the deadline for dropping a course is through the end of week six. (Source: admin_add_drop_deadline.txt and admin_withdrawal_deadline.txt)
```

```
Every student gets $30 of printing per semester, which is roughly 600 black-and-white pages (admin_printing_quota.txt).
```

```
A person can book a maximum of two blocks (two hours each, for a total of four hours) per week. A group of four people can coordinate to book up to eight hours total.

Source: study_group_rooms.txt
```

```
It costs $1.50 to wash and $1.50 to dry, making a total of $3.00 at the old brewhouse building.

Source: `housing_old_brewhouse.txt` (also mentioned in `housing_old_brewhouse_laundry.txt`)
```

```
A student has fifteen days from the time the grade is posted to raise a grade appeal (admin_grade_appeals.txt).
```

### Criterion 3 — Gate stops out-of-corpus questions — 5/5

`run_eval.py::check_out_of_scope` → `gate.py::check`, cutoff 0.55

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.891 | refused |

```
I don't have enough information about that.
```

### Criterion 4 — No chunk is over 400 characters — 5/5

`chunker.py::split_documents` → `chunker.py::describe`

```
100 chunks, 278 characters on average (shortest 94, longest 400), produced by chunker.py::split_documents
chunks over 400 characters: 0
```

### Criterion 5 — Each response takes under 5 seconds — 5/5

`run_eval.py::main` → `run_eval.py::run_once`

What is the deadline for a student to drop a course?
  run 1: pass  2.31s  (best distance 0.303)

How much of a printing quota does a student have each semester?
  run 1: pass  0.69s  (best distance 0.321)

How many total hours per week can a student book a study room?
  run 1: fail  0.80s  (best distance 0.250)

How much does it cost in total to wash and dry my clothes at the old brewhouse building?
  run 1: fail  0.75s  (best distance 0.225)

How long after a grade is posted does a student have time to appeal?
  run 1: pass  0.79s  (best distance 0.156)

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | Missed | The goal was 4/5 but each run only had 3/5 |
| 2 | Every answer names a source | Met | 5/5  answers cite a source document |
| 3 | The relevance gate stops out-of-corpus questions | Met | 5/5 out of scope questions were refused |
| 4 | No chunk is over 400 characters | Met | No chunk was over 400 characters |
| 5 | Each response should take no longer than 5 seconds. | Met | No pass took over 5 seconds |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
