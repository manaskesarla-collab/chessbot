# Step 9: Deploy as a Lichess bot

## What it means
Put the engine online as a bot account on Lichess so strangers and other bots play it in rated games. A public, third-party rating is much stronger evidence than your own test suite.

## What you need to do

1. **Create a fresh Lichess account** and do **not play any games on it**. Lichess only lets an account with zero games be upgraded to a bot, and the upgrade is permanent.
2. **Create an API token** with the bot play scope and upgrade the account to a bot.
3. **Install the `lichess-bot` bridge** (the official open-source program that connects a UCI engine to Lichess).
4. **Wrap your engine as UCI.** Use the Step 6 UCI script. Make it fast to start, handle `go` with time limits, and never crash or hang.
5. **Configure `lichess-bot`:** engine path, accepted time controls (rapid, for example 10+0 or 15+10), rated challenges accepted, concurrency of 1 game.
6. **Handle time management.** Map the clock to a simulation count or time budget so the bot never flags.
7. **Run it on your Mac** and keep it awake. Let it play rated games for about a week. The rating starts uncertain and converges to a trustworthy number.
8. **Log games** and review losses for crashes, illegal moves or timeouts, which are bugs rather than weakness.
9. **Keep secrets safe:** the token goes in an untracked file or environment variable, never into git.

## Key terms
- **Bot account:** a Lichess account run by software.
- **UCI:** the protocol between the bridge and your engine.
- **Provisional rating:** an early rating with large uncertainty.

## What this step leads to
The live link and the final rating you quote on your resume. It also surfaces real-world bugs (time handling, crashes) that local tests miss.

## How you know it's done
- [ ] Bot accepts and completes rated games without errors
- [ ] 50+ rated games played and the rating is no longer provisional
- [ ] Profile URL recorded for the README

## Common pitfalls
- Playing games on the account before upgrading it, which makes the upgrade impossible.
- Time losses from a slow engine.
- Leaking the API token.
- Reading a provisional rating as final.

## Resume angle
A live link lets a recruiter check the rating themselves.
