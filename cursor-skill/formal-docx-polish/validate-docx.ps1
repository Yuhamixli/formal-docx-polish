param(
    [Parameter(Mandatory = $true)][string]$InputPath,
    [ValidateSet("generic", "request", "plan", "report", "regulation", "meeting")]
    [string]$Kind = "generic",
    [switch]$Strict
)

$ScriptPath = Join-Path $PSScriptRoot "scripts\validate_docx.py"
if ($Strict) {
    python $ScriptPath $InputPath --kind $Kind --strict
} else {
    python $ScriptPath $InputPath --kind $Kind
}
exit $LASTEXITCODE
