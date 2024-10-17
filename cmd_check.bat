@Rem check registry for ansi colour code
reg query HKCU\Console\ | find /I "VirtualTerminalLevel" > nul
if %errorlevel% NEQ 0 (
    @Rem ANSI settings not found.
    exit /b 1
) else (
    exit /b 0
)