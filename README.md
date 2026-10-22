# Intelligent Systems & Intelligent Agents — Practical Work

**Student:** Sanjeevsaran J.  
**Student ID:** IT24104155  
**Academic year:** 2026 · Year 3, Semester 1

This repository organizes practical work into separate Git branches so an instructor can review the contents of each week independently. **Select a branch from the table below**; the default `main` branch is an index, not a combined code submission.

> **Module note:** The source materials are from **two distinct modules**: IT3012 (Intelligent Agents) and SE3062 (Intelligent Systems). They are labelled separately below to avoid confusion. Check the relevant module's CourseWeb instructions before using this repository as a submission link.

## Weekly practicals (Weeks 01–04)

| Branch | Module / topic | What to review | Current scope |
|---|---|---|---|
| [Week_01](../../tree/Week_01) | **IT3012** — introductory grid agents | `agent.py`, `grid_game.py`, `visual_grid_game.py`, `simulator.py`, `test_suite.py` | Original files copied from [IT3012 Practical Base — lab01](https://github.com/IT24104155/IT3012---Practical-Base/tree/lab01) |
| [Week_02](../../tree/Week_02) | **IT3012** — search algorithms / BFS | Same project files, including the updated `agent.py` | Original files copied from [IT3012 Practical Base — lab02](https://github.com/IT24104155/IT3012---Practical-Base/tree/lab02) |
| [Week_03](../../tree/Week_03) | **SE3062** — intelligent-agent architectures | `Lab03_Report.md` | Transcription of the supplied group report; original PDF layout is not included |
| [Week_04](../../tree/Week_04) | **IT3012** — informed search / A* | `agent.py`, `test_astar.py`, `WEEK04_README.md` | Standalone A* implementation; original game/GUI integration not verified |

**How to review:** Open the relevant branch link above, then inspect its code or report files. For Weeks 01 and 02, each branch preserves its own version of the project; the code is **not** merged into `main`.

## Additional SE3062 practicals

| Branch | Topic | Current scope |
|---|---|---|
| [lab-07](../../tree/lab-07) | Logical Reasoning & Forward Chaining | `logic_engine.py`, `test_logic.py`; integration with earlier grid game remains incomplete |
| [lab-08](../../tree/lab-08) | Game Theory & Adversarial Search | Standalone `practical08.py` and README; original notebook not committed; NegMAS not verified |
| [lab-08-csp](../../tree/lab-08-csp) | Constraint Satisfaction Problems | Standalone `csp_practical8.py` and README; completed notebook is not committed |

## Running the Python work

Use Python 3 from the selected branch's directory:

```bash
# For Week_04:
python test_astar.py

# For lab-07:
python test_logic.py

# For lab-08:
python practical08.py

# For lab-08-csp:
python csp_practical8.py
```

The older Week 01/02 grid-game project may have its own dependencies and execution steps; inspect its `simulator.py`, `visual_grid_game.py`, and `test_suite.py`.

## Submission and limitations

- The repository is **public** and designed for read-only instructor review.
- **Weeks 01 and 02:** restored from the earlier GitHub practical-base repository, with matching file contents verified at the time of copying.
- **Week 03:** this was a group **written report**, not an implementation of `agent.py`. Its Markdown copy preserves the written content, not the PDF page design.
- **Week 04:** the A* example is independently implemented. The original Labs 1–3 application was not integrated into this branch; treat it as partial work, not a confirmed end-to-end game.
- Additional practical branches contain standalone solutions, with scope and outstanding items documented in their own READMEs.
- Git commit timestamps reflect when these files were uploaded to this repository; they do **not** represent when the work was first carried out.

**Repository:** https://github.com/IT24104155/SE3062-Intelligent-Systems
