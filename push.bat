@echo off
:again
echo y|gcloud preview app deploy --version=default2 --stop-previous-version
choice /c nxYZ /m "AGAIN?"
if errorlevel 3 goto again