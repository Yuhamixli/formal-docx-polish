param(
    [Parameter(Mandatory = $true)][string]$InputPath,
    [string]$OutputPath = "",
    [ValidateSet("generic", "request", "plan", "report", "regulation", "meeting")]
    [string]$Kind = "generic"
)

$ScriptPath = Join-Path $PSScriptRoot "scripts\polish_docx.py"
if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    python $ScriptPath $InputPath --kind $Kind
} else {
    python $ScriptPath $InputPath $OutputPath --kind $Kind
}
exit $LASTEXITCODE
