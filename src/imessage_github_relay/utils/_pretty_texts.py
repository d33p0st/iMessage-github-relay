
class PrettyTexts:
    CMD_COLOR_FIX_PROMPT = """⚠️  Windows Operating System Detected.
🚫  This OS does not support Terminal ANSI sequences.
💡  To fix this, run: `imessage-github-relay --fix-cmd` 🛠️

👨‍💻  If you are a developer, try setting `_CMD_COLOR_FIX_PROMPT` parameter to `False` to detect and fix this automatically. 🔧"""

    CMD_COLOR_FIX_FAIL = """❌ CMD ANSI Sequence Fix Failed.
🔄  Please try running the fix command again: `imessage-github-relay --fix-cmd` 🛠️

📋  Ensure you have the necessary permissions and environment settings."""

    CMD_COLOR_OS_INCOMPATIBLE = """🖥️  Windows-Only Fix Detected.
⚙️  This fix is designed specifically for Windows systems.

✅ Your current OS does not require this fix. No action is needed! 🚀
"""