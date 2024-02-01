$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())

if($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        
    $db_user = Read-Host "Enter the username"
    $db_password = Read-Host "Enter the password"
    $db_host = Read-Host "Enter the host"
    $db_port = Read-Host "Enter the port"
    $db_name = Read-Host "Enter the database name"

    $connStr = "mysql+mysqlconnector://${db_user}:${db_password}@${db_host}:${db_port}/${db_name}"
    # look if chocolatey is installed and install it if not
    if(!(Get-Command choco -ErrorAction SilentlyContinue)) {
        Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))}

        # install mysql
        choco install mysql -y

        # return to the root folder if in func folder
        if($PWD.Path -like "*\func") {
            cd ..
        }
        #create python virtual environment
        python -m venv testenv

        #acivate virtual environment
        .\testenv\Scripts\Activate.ps1

        #install poetry
        pip install poetry

        #install dependencies
        poetry install --no-root

        #check if .env file created 
        if(Test-Path .env) {
            Remove-Item .env
        }
        New-Item -Path .env -ItemType file 
        #add db connection string to .env file
        Add-Content -Path .env -Value "DB_CONNECTION_STRING=$connStr"
} else {
    Write-Host "Not running as Administrator"
    Write-Host "Please run this script as Administrator"
    exit
}