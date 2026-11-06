# Step 10: Make it resume-worthy

## What it means
A good result nobody can understand is wasted. This step turns the work into something a recruiter or interviewer can read in two minutes and trust.

## What you need to do

1. **README.** Include a project summary, an architecture diagram (encoder to ResNet to policy/value heads to MCTS to self-play loop), the Elo-vs-stage chart, the Lichess profile link, and exact commands to reproduce results.
2. **Ablations.** A table comparing supervised only, + MCTS, + RL (and optionally with and without human-data mixing, different simulation counts). Each row shows Elo with a confidence interval. This proves you understand what each part contributes.
3. **Honest write-up.** State the compute budget (Mac only, hours of training), what did not work, and the limits of the claim (which rating scale, how many games). Interviewers trust honesty.
4. **Clean code.** Tests passing, type hints, ruff and mypy clean, YAML configs, and one command to train and one to play.
5. **Reproducibility.** Pinned dependencies via `uv.lock`, fixed seeds, saved configs next to every checkpoint, and a small released checkpoint (or download script).
6. **Optional web demo.** A small page where a visitor plays the bot (for example a lightweight Flask or FastAPI server with a chessboard front end).
7. **Resume bullet.** Template:
   > Built an AlphaZero-style chess engine (ResNet policy/value net + PUCT MCTS), pretrained on N million Lichess positions and improved via self-play RL; reached a ~X Lichess rapid rating (+Y Elo from RL fine-tuning) on a single-laptop budget.

   Fill in only numbers you measured.

## Key terms
- **Ablation:** removing or adding one component to measure its contribution.
- **Reproducibility:** someone else can rerun and get the same result.

## What this step leads to
The finished, shareable project: the repo, chart, live bot and resume line.

## How you know it's done
- [ ] A stranger can clone, run the tests and play the bot from the README alone
- [ ] Every number in the README is backed by a file in `results/`
- [ ] Resume bullet contains only measured values

## Common pitfalls
- Claiming a rating from a different scale.
- Hiding failures; they are valuable material in interviews.
- Large binaries committed to git.

## Resume angle
This whole step is the resume angle.
