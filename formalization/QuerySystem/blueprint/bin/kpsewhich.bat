@echo off
rem Minimal kpsewhich shim so plasTeX can resolve local .tex inputs without a
rem full TeX distribution installed.
rem
rem plasTeX calls kpsewhich to locate \input and \usepackage targets. On
rem Windows it invokes it with shell=True, so a missing kpsewhich returns an
rem empty stdout instead of raising -- which means plasTeX's own TEXINPUTS
rem fallback (only reached via an exception) never runs, and the render dies
rem with "Could not find any file named: web.tex".
rem
rem Style packages are not our problem: plasTeX implements the standard ones in
rem Python, and blueprint.sty is implemented by the leanblueprint plugin.
setlocal
if "%~1"=="" exit /b 1
if exist "%~1" (
  for %%I in ("%~1") do echo %%~fI
  exit /b 0
)
for %%D in ("%TEXINPUTS:;=" "%") do (
  if not "%%~D"=="" if exist "%%~D\%~1" (
    for %%I in ("%%~D\%~1") do echo %%~fI
    exit /b 0
  )
)
exit /b 1
