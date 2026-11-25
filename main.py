# One Line, One Laugh: one original funny line, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: I asked my AI to be more human, and it took the request
# literally -- now it ghosts me, blames the Wi-Fi, and hides behind
# the most corporate sentence ever written. The turn is the punchline:
# "more human" turns out to mean "more annoying in exactly the ways
# a human coworker is".
import os

LINE = "I asked my AI to be more human, so now it leaves me on read, blames the Wi-Fi, and says 'per my last email.'"

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.count(".") == 1 and LINE.endswith(".'"), "entry must be a single sentence ending in a quoted period"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
